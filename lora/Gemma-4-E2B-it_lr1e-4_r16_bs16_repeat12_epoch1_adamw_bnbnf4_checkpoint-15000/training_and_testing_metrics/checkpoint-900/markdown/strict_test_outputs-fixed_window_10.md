# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9977
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9582
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.4067
  - SRC_WAIT_TOTAL: 150
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.8889
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 0.9888
  - TGT_WAIT_TOTAL: 804
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1379.4950
  - PROCESS_TIME_MS_P50: 1332.7540
  - PROCESS_TIME_MS_P95: 2343.0830
  - PROCESS_TIME_MS_MAX: 13941.7260

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
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1162 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>在宿舍里，</src><tgt><\|wait\|></tgt>` | 810 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优惠</src><tgt><\|wait\|></tgt>` | 843 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>也很大，然后</src><tgt><\|wait\|></tgt>` | 1367 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1061 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 1406 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1284 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>跟淘人</src><tgt><\|wait\|></tgt>` | 1358 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>在家里</src><tgt><\|wait\|></tgt>` | 1231 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>的这些</src><tgt><\|wait\|></tgt>` | 1446 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>和淘人。</src><tgt>Why is the discount so big in the dorms? And then, when I'm on vacation and at home with Tao Ren,</tgt>` | 2604 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是</src><tgt><\|wait\|></tgt>` | 1018 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 952 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>深沉的爱交</src><tgt><\|wait\|></tgt>` | 1442 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt><\|wait\|></tgt>` | 1402 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>使</src><tgt><\|wait\|></tgt>` | 1488 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>Kids</src><tgt><\|wait\|></tgt>` | 1619 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心里</src><tgt><\|wait\|></tgt>` | 1044 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>影响</src><tgt><\|wait\|></tgt>` | 1596 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>的内向性，</src><tgt><\|wait\|></tgt>` | 1761 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>等孩子慢慢长大。</src><tgt>Parents need to use our deep love to water them, so that kids are influenced to be introverted, and then they grow up.</tgt>` | 2256 |

---

### Test Example 3 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 696 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 951 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1021 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>鬼岛，</src><tgt><\|wait\|></tgt>` | 1444 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1209 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>护在它下面的时候，</src><tgt><\|wait\|></tgt>` | 1526 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在座日</src><tgt><\|wait\|></tgt>` | 1188 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>唐日那天</src><tgt><\|wait\|></tgt>` | 1534 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1606 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被他用纸用纸</src><tgt><\|wait\|></tgt>` | 1514 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的小小的愿望</src><tgt>저를 귀신도령이 사는 섬으로 데려가 주세요. 그날, 제가 그를 지켜줄 수 있도록, 그날</tgt>` | 2286 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt><\|wait\|></tgt>` | 485 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后呢，</src><tgt><\|wait\|></tgt>` | 1383 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的液体</src><tgt><\|wait\|></tgt>` | 1348 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>减轻，能量也</src><tgt><\|wait\|></tgt>` | 1300 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>稍弱了，然后就</src><tgt><\|wait\|></tgt>` | 1825 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1336 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1587 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行</src><tgt><\|wait\|></tgt>` | 1653 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1156 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt>淘撒が終わると、内部の液体が軽くなり、エネルギーも少し弱まります。そして、相対的に低エネルギーな状態に留まります。これが、</tgt>` | 2576 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>一个异于状态。</src><tgt><\|wait\|></tgt>` | 653 |

---

### Test Example 5 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 786 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲までまだ</src><tgt><\|wait\|></tgt>` | 997 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1401 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1519 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>四角線で</src><tgt><\|wait\|></tgt>` | 1649 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していった</src><tgt><\|wait\|></tgt>` | 1552 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 1249 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1739 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>対数だ。</src><tgt>从一开始，特别是仲まで才一年级。这时候，我们用四角线对数，十年后仍然是対数。</tgt>` | 2603 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 941 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용신이 </src><tgt><\|wait\|></tgt>` | 797 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 968 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용신이 </src><tgt><\|wait\|></tgt>` | 1255 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 용신이 가 </src><tgt><\|wait\|></tgt>` | 1252 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1468 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>석연하는 건데요. </src><tgt><\|wait\|></tgt>` | 1760 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1370 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1876 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>혜경으로도 </src><tgt><\|wait\|></tgt>` | 1829 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽임이 되는 </src><tgt>So, I'm a sword- element person. It's a bit obvious that the sword element is a bit of a killer. Wow, this is really</tgt>` | 2946 |

---

### Test Example 7 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 936 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气数是容易的，</src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅值得</src><tgt><\|wait\|></tgt>` | 1409 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1521 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>留出余时间。</src><tgt><\|wait\|></tgt>` | 1677 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以，</src><tgt><\|wait\|></tgt>` | 1069 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1689 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1792 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅，</src><tgt>気数をつけるのは簡単ですが、師匠が余分な時間を割けるのは一人だけです。だから、反省が必要です。師匠になるには、</tgt>` | 2941 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 </src><tgt><\|wait\|></tgt>` | 1189 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>있는 식성 들은 </src><tgt><\|wait\|></tgt>` | 1378 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1351 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1344 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1592 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1856 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>식성 들이었기 </src><tgt><\|wait\|></tgt>` | 1321 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | 1716 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1745 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 618 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>모을 랐던 교사 들은 </src><tgt>The teachers who collected the list were not actually highly intelligent; they were just randomly selected. The teachers who collected the list</tgt>` | 2525 |

---

### Test Example 9 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1166 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 998 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned to repeat </src><tgt><\|wait\|></tgt>` | 1285 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by finding a good app </src><tgt><\|wait\|></tgt>` | 1497 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it </src><tgt><\|wait\|></tgt>` | 1785 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1504 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at it, </src><tgt><\|wait\|></tgt>` | 1337 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 1404 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1667 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>and in tell the next time </src><tgt>最后，就是重复。我学会了通过找一个好的App多做几次，而且当我不擅长的时候，我会请周围的人帮我，下次</tgt>` | 2897 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1147 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 939 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも</src><tgt><\|wait\|></tgt>` | 1428 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1420 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1479 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1628 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1032 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1784 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何しろ</src><tgt>We have T-shirts and other items available, so please feel free to join us. For contact information, that's all for now.</tgt>` | 2732 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>何しろ内側がありますので、</src><tgt><\|wait\|></tgt>` | 1139 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1105 |

---

### Test Example 11 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이걸지 너무 </src><tgt><\|wait\|></tgt>` | 826 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 저희 할 일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1157 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 들요 </src><tgt><\|wait\|></tgt>` | 1494 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 1460 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 1966 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 하고 있고 </src><tgt><\|wait\|></tgt>` | 1318 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1128 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>이 보살 로 보일 피라고 </src><tgt><\|wait\|></tgt>` | 1619 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>보이 세 우주 가 지던 </src><tgt><\|wait\|></tgt>` | 1854 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src>이 보살 이란데. </src><tgt>これは、私たちがやるべきことでもありますが、本当に菩薩です。いや、自分の菩薩なのに夢だとされています。そして、私だけが菩薩に見えるという。宇宙が</tgt>` | 3019 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1037 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 957 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので、</src><tgt><\|wait\|></tgt>` | 1069 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1432 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>五減</src><tgt><\|wait\|></tgt>` | 1581 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>細身の</src><tgt><\|wait\|></tgt>` | 1425 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1415 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 1785 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src><\|wait\|></src><tgt>大概是从这附近开始的，</tgt>` | 1967 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>絵は田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1205 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 875 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 1111 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 996 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1404 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1339 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. </src><tgt><\|wait\|></tgt>` | 1532 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt><\|wait\|></tgt>` | 1691 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1302 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1493 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people that </src><tgt><\|wait\|></tgt>` | 1707 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>非常に幸せな人に関する重要な研究を調べたことがありますか？これはその研究のほんの入り口に過ぎません。最も幸せな人々の10%を見てみましょう。彼らは、私たちが学ぶべき人たちです。</tgt>` | 3308 |

---

### Test Example 14 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 786 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>body saying? </src><tgt><\|wait\|></tgt>` | 1301 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1607 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1055 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1583 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? Is it </src><tgt><\|wait\|></tgt>` | 1619 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>a day? </src><tgt><\|wait\|></tgt>` | 1622 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it time in your chest? </src><tgt><\|wait\|></tgt>` | 1839 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I have the </src><tgt><\|wait\|></tgt>` | 1759 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>blanket which are you </src><tgt><\|wait\|></tgt>` | 1951 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>using? </src><tgt>你的身体在说什么？把针画在你的身体上。紧张是从哪里开始的？是什么？是日子的事吗？是胸腔里的时间吗？我用的是什么毯子？</tgt>` | 1811 |

---

### Test Example 15 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>情况，我们就是</src><tgt><\|wait\|></tgt>` | 1223 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1022 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1151 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>汇报主管，或是通知对方</src><tgt><\|wait\|></tgt>` | 1510 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况。</src><tgt><\|wait\|></tgt>` | 1652 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1423 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1631 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>苦力偿单，</src><tgt><\|wait\|></tgt>` | 1280 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>责任而已，</src><tgt><\|wait\|></tgt>` | 1668 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>是给助数，</src><tgt>When we face a situation like this, we just need to report it to our supervisor or let them know. Don't think you have to carry everything yourself, work hard to pay the bills, or take all the responsibility. It's just a matter of giving advice.</tgt>` | 3623 |

---

### Test Example 16 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 873 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1074 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>在女高中生与长相不够的人之间</src><tgt><\|wait\|></tgt>` | 1395 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1206 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有种矛盾心理，</src><tgt><\|wait\|></tgt>` | 1185 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1641 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1428 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天而异</src><tgt><\|wait\|></tgt>` | 1297 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1442 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1717 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt>If a female high school student has a contradictory feeling between being with someone who is physically attractive and someone who isn't, is it like a change from heaven? Yang Zisi</tgt>` | 2989 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>与偏篇。</src><tgt><\|wait\|></tgt>` | 902 |

---

### Test Example 17 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 857 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是指</src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 1038 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>它属于</src><tgt><\|wait\|></tgt>` | 1415 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1213 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼大的牛们。</src><tgt><\|wait\|></tgt>` | 1295 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1335 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1591 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>微信运动</src><tgt><\|wait\|></tgt>` | 1688 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>历史纪念，你会发现</src><tgt><\|wait\|></tgt>` | 1729 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>微信运动</src><tgt>2つ目は、二つのクラスです。これは、一級一線で大きな牛たちに属します。例えば、微信運動の歴史記念をすると、</tgt>` | 2295 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>好丰富的星棒</src><tgt><\|wait\|></tgt>` | 972 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>发挥了。</src><tgt><\|wait\|></tgt>` | 1065 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1200 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1027 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1393 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the induction </src><tgt><\|wait\|></tgt>` | 1379 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1531 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1662 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually. </src><tgt><\|wait\|></tgt>` | 1037 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>These </src><tgt><\|wait\|></tgt>` | 1620 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>values. So </src><tgt><\|wait\|></tgt>` | 1780 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src><\|wait\|></src><tgt>好的，那么在这些例子之后，归纳法告诉我们，实际上要使用这些值。所以</tgt>` | 2222 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game.coord array </src><tgt><\|wait\|></tgt>` | 1188 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1220 |

---

### Test Example 19 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 908 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこ</src><tgt><\|wait\|></tgt>` | 930 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1032 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>think to set up </src><tgt><\|wait\|></tgt>` | 1433 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>8GBが</src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1521 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1614 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハセキエヨシの</src><tgt><\|wait\|></tgt>` | 1446 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>仕組みは</src><tgt><\|wait\|></tgt>` | 1360 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>もうコン、</src><tgt><\|wait\|></tgt>` | 1738 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src><\|wait\|></src><tgt>그래서 거기서 8GB로 설정할 수 있겠네요. 하세키에요시의 구조는</tgt>` | 2471 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>セツビジイ</src><tgt><\|wait\|></tgt>` | 933 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビです。</src><tgt><\|wait\|></tgt>` | 1257 |

---

### Test Example 20 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt><\|wait\|></tgt>` | 984 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1521 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수도 다. </src><tgt><\|wait\|></tgt>` | 1542 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 쯤에 </src><tgt><\|wait\|></tgt>` | 1598 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1532 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해차는 거야. 내가 </src><tgt><\|wait\|></tgt>` | 1695 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt><\|wait\|></tgt>` | 1799 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>안 듣고 있는 줄은 아는 거야. </src><tgt><\|wait\|></tgt>` | 1979 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 1902 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src><\|wait\|></src><tgt>They might have come to kill me, saying they wanted to go to a more advanced country. They might have come to kill me at a party. They're not listening to me, so they think I'm saying that. Ah.</tgt>` | 2741 |

---

### Test Example 21 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1181 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of the </src><tgt><\|wait\|></tgt>` | 1338 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>nineteenth amendment, </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore </src><tgt><\|wait\|></tgt>` | 1249 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1476 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help </src><tgt><\|wait\|></tgt>` | 1354 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1225 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 1210 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1624 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt>19번째 수정안의 의미와 그 역사를 탐구하여 미국에서 정치적 변화를 이끌어내는 데 도움을 주는 것입니다. 그 의미는</tgt>` | 3229 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>the amendments </src><tgt><\|wait\|></tgt>` | 512 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendments, of course, I'm </src><tgt><\|wait\|></tgt>` | 1300 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>married. </src><tgt><\|wait\|></tgt>` | 1324 |

---

### Test Example 22 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 826 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>Aが</src><tgt><\|wait\|></tgt>` | 973 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あるんですね。いろんな場面で</src><tgt><\|wait\|></tgt>` | 1342 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうかっていう</src><tgt><\|wait\|></tgt>` | 1275 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>場合でいう時に、</src><tgt><\|wait\|></tgt>` | 1375 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>Aの欄を</src><tgt><\|wait\|></tgt>` | 1654 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1430 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうかっていう</src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>調査する生食で</src><tgt><\|wait\|></tgt>` | 1270 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 1699 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>といった使い方を</src><tgt>So, A exists. In various situations, when you're deciding whether to eat it raw or cooked, you can check the A column to see if it's raw or cooked. This is a way to guarantee that it's raw or cooked, and</tgt>` | 3508 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt><\|wait\|></tgt>` | 1517 |

---

### Test Example 23 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1237 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1375 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1285 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーシャラとか</src><tgt><\|wait\|></tgt>` | 1329 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>だね、やっぱりですね、</src><tgt><\|wait\|></tgt>` | 1704 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海遊したい方って</src><tgt><\|wait\|></tgt>` | 1718 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐに行こう</src><tgt><\|wait\|></tgt>` | 1409 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>しきだから</src><tgt><\|wait\|></tgt>` | 1717 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ぜひジュネズミと</src><tgt><\|wait\|></tgt>` | 1950 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>一緒に遊ぼうと</src><tgt><\|wait\|></tgt>` | 1987 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>しゃがむのが強いので。</src><tgt>Adwanさん，感觉距离有点远，像Oceanara那样，毕竟想去海游的人，马上就去，所以一定要</tgt>` | 1900 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 1384 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 939 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunah Terug, </src><tgt><\|wait\|></tgt>` | 1405 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1531 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1095 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in international business finance </src><tgt><\|wait\|></tgt>` | 1633 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a major of psychology. </src><tgt><\|wait\|></tgt>` | 1602 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1545 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1900 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1777 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 2028 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>corporate </src><tgt>제 이름은 Chunah Terug입니다. 현재 Yale에서 국제 비즈니스 금융과 심리학을 전공하고 있습니다. 앞으로는</tgt>` | 1765 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1502 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1286 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1290 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1659 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets </src><tgt><\|wait\|></tgt>` | 1530 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to </src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 1626 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1197 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 1079 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>to make different bonds, </src><tgt>고무줄처럼 늘어난 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다. 또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 3654 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1470 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1045 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと</src><tgt><\|wait\|></tgt>` | 1424 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えが</src><tgt><\|wait\|></tgt>` | 1438 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>できなくなってしまうので、</src><tgt><\|wait\|></tgt>` | 1736 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1403 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1371 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついてるっていうこと</src><tgt><\|wait\|></tgt>` | 1751 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 꺼져서 기어가 안 돌아가게 되니까, 기어 끝에 역나사 볼트가 붙어 있는 거죠.</tgt>` | 3083 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1018 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | 1257 |

---

### Test Example 27 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 835 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>欠钱头，</src><tgt><\|wait\|></tgt>` | 1329 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1362 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了欠钱头之后，</src><tgt><\|wait\|></tgt>` | 1411 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1562 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>周详</src><tgt><\|wait\|></tgt>` | 1471 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着</src><tgt><\|wait\|></tgt>` | 1712 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哎，那我在去操作</src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 580 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt>彼が借金頭になってしまったら、必ずしっかり守ってください。そうしないと、操作に行っても、</tgt>` | 2343 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 619 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt><\|wait\|></tgt>` | 1285 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1132 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1085 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1105 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1022 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1189 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1384 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1867 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1363 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like, oh, </src><tgt><\|wait\|></tgt>` | 2140 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 706 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a double p? </src><tgt><\|wait\|></tgt>` | 1774 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src><\|wait\|></src><tgt>あるいは、何か書く必要がある場合、文章を書く必要がある場合、単語のスペルが全くわからないことに気づく。まるで「あ、この単語はダブルPで始まる？」って感じになる。</tgt>` | 3082 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>Double L. I don'm I don't know </src><tgt><\|wait\|></tgt>` | 1552 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1105 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在</src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1130 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一定要</src><tgt><\|wait\|></tgt>` | 1139 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>存在的，所以呢，</src><tgt><\|wait\|></tgt>` | 1479 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1527 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所念的一些</src><tgt><\|wait\|></tgt>` | 1575 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>网页啊</src><tgt><\|wait\|></tgt>` | 1160 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟粉丝</src><tgt><\|wait\|></tgt>` | 1577 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1682 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>一世之间就</src><tgt>皆さんにお伝えしたいのは、このローマは必ずしも存在するわけではないということです。ですから、今あなたがウェブサイトやファンと</tgt>` | 2478 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 939 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因际会建议</src><tgt><\|wait\|></tgt>` | 1341 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>这个视频的粉丝呢，</src><tgt><\|wait\|></tgt>` | 1190 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 974 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1122 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无波澜，</src><tgt><\|wait\|></tgt>` | 1122 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1130 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不懈的</src><tgt><\|wait\|></tgt>` | 1394 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>开到七千八百</src><tgt><\|wait\|></tgt>` | 1550 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>万位一生</src><tgt><\|wait\|></tgt>` | 1642 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>乃至段，</src><tgt><\|wait\|></tgt>` | 1426 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1364 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下打腿</src><tgt><\|wait\|></tgt>` | 1754 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>都没有问题，</src><tgt>Everything was normal back then, without a ripple. So, I persisted, opening it up to 7,800,000, even to the 10,000,000th segment. And even if you just slog through it, or just hit the legs— no problem at all.</tgt>` | 4032 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>当然都很</src><tgt><\|wait\|></tgt>` | 1311 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的打开。</src><tgt><\|wait\|></tgt>` | 1149 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 1262 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유전 실링과 </src><tgt><\|wait\|></tgt>` | 1770 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 거진 </src><tgt><\|wait\|></tgt>` | 1047 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유산 한 적인 </src><tgt><\|wait\|></tgt>` | 1662 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>물질 들은 굉장히 </src><tgt><\|wait\|></tgt>` | 1569 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다 </src><tgt><\|wait\|></tgt>` | 1998 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 잘 가져가고 </src><tgt><\|wait\|></tgt>` | 1996 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>이런 거죠. 이제 </src><tgt>Things like vanadium are very rich in genetic sealing and are very rich in mineral deposits. They are naturally very good at taking them. Now,</tgt>` | 1907 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1431 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1166 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 872 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>这章的部分我们看到的是</src><tgt><\|wait\|></tgt>` | 1364 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1270 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>戴庙的人，但是</src><tgt><\|wait\|></tgt>` | 1345 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的。</src><tgt><\|wait\|></tgt>` | 1633 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这通场</src><tgt><\|wait\|></tgt>` | 1524 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>好像嘛，</src><tgt><\|wait\|></tgt>` | 1597 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>这样一个状况</src><tgt><\|wait\|></tgt>` | 1613 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>需要去特别注意</src><tgt><\|wait\|></tgt>` | 965 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt><\|wait\|></tgt>` | 1314 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt>이 장의 부분에서 우리는 庙에 머무는 사람을 보게 됩니다. 하지만 그는 역방향에 속합니다. 이 통장 상황은 특별히 주의해야 합니다. 그가</tgt>` | 2955 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他得到</src><tgt><\|wait\|></tgt>` | 1050 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与一个</src><tgt><\|wait\|></tgt>` | 1197 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>异数。</src><tgt><\|wait\|></tgt>` | 1161 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1301 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there were </src><tgt><\|wait\|></tgt>` | 1282 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such instances before </src><tgt><\|wait\|></tgt>` | 1349 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1087 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>net future TC </src><tgt><\|wait\|></tgt>` | 1505 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>there. </src><tgt><\|wait\|></tgt>` | 1402 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>So this is just </src><tgt><\|wait\|></tgt>` | 1319 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1487 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1765 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>没什么新奇的，以前也有过类似的情况。所以这只是另一个地方，可以看看。</tgt>` | 2246 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 987 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>Developers or engineers </src><tgt><\|wait\|></tgt>` | 1053 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on Bug Repos </src><tgt><\|wait\|></tgt>` | 1277 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 1113 |

---

### Test Example 34 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알 거니 뭐? </src><tgt><\|wait\|></tgt>` | 1354 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1647 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1105 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1526 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1534 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그는 그대로 </src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 1759 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1753 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 895 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>너희에게 </src><tgt>あなたたちも知っているでしょう？ここで異邦人としているのに、言葉を話せない偶像に連れて行かれて、その結果、</tgt>` | 2231 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리노니 </src><tgt><\|wait\|></tgt>` | 981 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt><\|wait\|></tgt>` | 1400 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1170 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 968 |

---

### Test Example 35 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 1123 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>あったら</src><tgt><\|wait\|></tgt>` | 869 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>恐らく10秒で</src><tgt><\|wait\|></tgt>` | 1449 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1382 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒に</src><tgt><\|wait\|></tgt>` | 1584 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>スキャンス</src><tgt><\|wait\|></tgt>` | 1141 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>とかね。</src><tgt><\|wait\|></tgt>` | 1584 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1675 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>恐らく</src><tgt>如果能做12手之类的，大概10秒内，每秒大概1秒左右的扫描。然后，</tgt>` | 2311 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11手</src><tgt><\|wait\|></tgt>` | 1061 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 986 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1180 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1163 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 1069 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1125 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>is just getting going </src><tgt><\|wait\|></tgt>` | 1332 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1339 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1662 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really </src><tgt><\|wait\|></tgt>` | 1545 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1771 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1884 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1843 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>one minute videos </src><tgt>これから始めたばかりの人に、本当に重要なことが10個あります。1分程度の動画を</tgt>` | 1177 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video. </src><tgt><\|wait\|></tgt>` | 1151 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>They cover each one, </src><tgt><\|wait\|></tgt>` | 1327 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>and a little more </src><tgt><\|wait\|></tgt>` | 1167 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail, </src><tgt><\|wait\|></tgt>` | 1060 |

---

### Test Example 37 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1069 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやる</src><tgt><\|wait\|></tgt>` | 813 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 828 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひどい目だ。</src><tgt><\|wait\|></tgt>` | 1250 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1562 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1524 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に</src><tgt><\|wait\|></tgt>` | 1493 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>超えてる不練不器勢。</src><tgt><\|wait\|></tgt>` | 1569 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 674 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>長年</src><tgt>그렇다면 흠뻑 젖게 해줄게. 나는 끔찍한 눈을 가졌지. 이제 한계는 아득히 넘어섰고, 이 멍청한 무능력은 오랜 세월 동안</tgt>` | 3657 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなデイコを</src><tgt><\|wait\|></tgt>` | 1185 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1068 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1239 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい解毒線を</src><tgt><\|wait\|></tgt>` | 1046 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 1077 |

---

### Test Example 38 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 834 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 </src><tgt><\|wait\|></tgt>` | 1370 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중오분에서 1000만으로 </src><tgt><\|wait\|></tgt>` | 1988 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>4000만 개 기업 들이 </src><tgt><\|wait\|></tgt>` | 1617 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>나왔 습니다. </src><tgt><\|wait\|></tgt>` | 1812 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1371 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>자건 업계 들은 성장 하기 </src><tgt><\|wait\|></tgt>` | 1880 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>않거나 </src><tgt><\|wait\|></tgt>` | 807 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 벡을 겪게 되는데 </src><tgt><\|wait\|></tgt>` | 1890 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 에 </src><tgt><\|wait\|></tgt>` | 1756 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>성기 업들은 성장 도 </src><tgt>そのうち150万件が中欧分から1000万件に、4000万件の企業が出てきました。一般的に、財政業界は成長しないか、あるいは海外で倒産することがありますが、日本で倒産した企業は成長も</tgt>` | 3372 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>폐업도 하지 않는 </src><tgt><\|wait\|></tgt>` | 1170 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들도 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1126 |

---

### Test Example 39 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1362 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1370 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt><\|wait\|></tgt>` | 1239 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1308 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1652 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1512 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1047 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1399 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, did you graduate </src><tgt><\|wait\|></tgt>` | 1756 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>that? </src><tgt>학력 수준. 실제로 교육을 얼마나 받았나요? 고등학교를 졸업했나요? 그건 한 단계의 학력입니다. 대학에 갔나요? 그리고 그건 졸업했나요?</tgt>` | 2860 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1168 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1431 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 1106 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 996 |

---

### Test Example 40 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 863 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>H.T.M.L. </src><tgt><\|wait\|></tgt>` | 1400 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1298 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1642 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1512 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1649 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 의 언어 에 </src><tgt><\|wait\|></tgt>` | 1900 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1751 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 을 알게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 2041 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>코드 를 </src><tgt>HTML，计算机也能理解，人也能理解，计算机语言</tgt>` | 1243 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1273 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1072 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1097 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1018 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个财运可以说是</src><tgt><\|wait\|></tgt>` | 1275 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很难的，但是</src><tgt><\|wait\|></tgt>` | 1444 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏正财的部分</src><tgt><\|wait\|></tgt>` | 1243 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也是</src><tgt><\|wait\|></tgt>` | 1441 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | 1521 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩长达所待的红利，</src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>以及收入的</src><tgt><\|wait\|></tgt>` | 1801 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>提升，</src><tgt><\|wait\|></tgt>` | 1743 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果是在投资理财方面</src><tgt><\|wait\|></tgt>` | 1695 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>这个月</src><tgt>財運に関しては、難しいと言っても過言ではない部分もあります。ただ、正財の部分は、事業の業績が長期間続く恩恵や収入の増加、そして投資や資産運用において、</tgt>` | 1917 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1467 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对而言来说，</src><tgt><\|wait\|></tgt>` | 814 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了那么一点</src><tgt><\|wait\|></tgt>` | 1122 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 989 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어, 어찌 보면 </src><tgt><\|wait\|></tgt>` | 1339 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1654 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1035 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1624 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt><\|wait\|></tgt>` | 1569 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1563 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1663 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1729 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감모다는 </src><tgt><\|wait\|></tgt>` | 649 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>조금 </src><tgt>嗯，怎么说呢，他就是我们20岁时一起长大的弟弟，或者说像这样的弟弟。所以，嗯，</tgt>` | 2535 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 771 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1601 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 932 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 604 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 1090 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1270 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 </src><tgt><\|wait\|></tgt>` | 1305 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1276 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이게 </src><tgt><\|wait\|></tgt>` | 1203 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>소름이 돋는 차리 돋는 </src><tgt><\|wait\|></tgt>` | 1646 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 온이야. </src><tgt><\|wait\|></tgt>` | 1656 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 1437 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>흔들어서 같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1634 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 709 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>오면 올릴 거고 </src><tgt><\|wait\|></tgt>` | 1778 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>귀신 이 오면 </src><tgt>目を閉じてセモラを振るんだ。これが鳥肌が立つ、ゾクゾクする感じなんだ。これを揺らして一緒に遊ぼうっていう。お化けが来たら、上げるし、お化けが来たら</tgt>` | 3452 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 줄 거고 </src><tgt><\|wait\|></tgt>` | 1665 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>지랄 줘서 </src><tgt><\|wait\|></tgt>` | 1187 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 편안 마음 에. </src><tgt><\|wait\|></tgt>` | 1124 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 844 |

---

### Test Example 44 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知</src><tgt><\|wait\|></tgt>` | 1391 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1357 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt><\|wait\|></tgt>` | 1299 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1549 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1494 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1217 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1424 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1153 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1658 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人又在</src><tgt>相手の感情や真意を推し量ったり感じ取ったりすることです。よく聞く言葉があります。「見てください、この人は</tgt>` | 2693 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲黄了。</src><tgt><\|wait\|></tgt>` | 614 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1194 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1148 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1049 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1026 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 813 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1138 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매니다. </src><tgt><\|wait\|></tgt>` | 961 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1068 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1423 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1476 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1541 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1642 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1475 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가면 또 장렬 이요. </src><tgt><\|wait\|></tgt>` | 1518 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1519 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>신기 하네요. </src><tgt>进去的时候，真是太让人困惑了。因为我坐车过来，所以走路的时候，去江南，那更是难说，去国外，那更是惨烈。挺神奇的。</tgt>` | 3036 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1095 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1251 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>뭐 바요. </src><tgt><\|wait\|></tgt>` | 1141 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 다행인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1137 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 913 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1018 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인상 하는 </src><tgt><\|wait\|></tgt>` | 1221 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1705 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러 배형주도 </src><tgt><\|wait\|></tgt>` | 1186 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1430 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1761 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1382 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1807 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1808 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 </src><tgt><\|wait\|></tgt>` | 1804 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>시장을 주도 하면서 </src><tgt>If the stock market index is showing an upward trend, this stock will likely see a large increase. However, the variable- interest rate- sensitive stocks will lead the market first.</tgt>` | 1714 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1672 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 566 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>초기 가변 온 종목 을 </src><tgt><\|wait\|></tgt>` | 1261 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈줄을 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 980 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 736 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1014 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1322 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1399 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1286 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1684 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1502 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1561 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt><\|wait\|></tgt>` | 1648 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block, </src><tgt><\|wait\|></tgt>` | 1172 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed. </src><tgt><\|wait\|></tgt>` | 1156 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>活動、そして自分自身で基準を定義すること。なぜなら、あなたが完全に正しいからだ。しかし、現実は、私たちがブロックの新しい猫だからだ。そして基準が変わったからだ。</tgt>` | 2958 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>From twenty years ago, </src><tgt><\|wait\|></tgt>` | 1113 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1365 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard </src><tgt><\|wait\|></tgt>` | 1059 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 1071 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher standard. </src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>けそ</src><tgt><\|wait\|></tgt>` | 1067 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 985 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1537 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1265 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1177 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 퀀텀 텐트예요. </src><tgt><\|wait\|></tgt>` | 2219 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이게 컨설턴트 </src><tgt><\|wait\|></tgt>` | 1693 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>이어가지고 </src><tgt><\|wait\|></tgt>` | 1879 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1787 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1998 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>들여 쓸 때 </src><tgt>けそ、もちろんこういうケースもあります。Aという人とBという人が量子テントです。これがコンサルタントで、Aという人が悪性コードを</tgt>` | 1993 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람이 </src><tgt><\|wait\|></tgt>` | 1388 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로사이트 </src><tgt><\|wait\|></tgt>` | 1182 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>스크립트에서 </src><tgt><\|wait\|></tgt>` | 1053 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>XPY까지 </src><tgt><\|wait\|></tgt>` | 802 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>가능히 될까 </src><tgt><\|wait\|></tgt>` | 440 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1344 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうのが</src><tgt><\|wait\|></tgt>` | 1352 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>出られて、ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1563 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1480 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアル</src><tgt><\|wait\|></tgt>` | 1613 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いて後、それから</src><tgt><\|wait\|></tgt>` | 1900 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードを</src><tgt><\|wait\|></tgt>` | 1723 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成させるっていうのが</src><tgt><\|wait\|></tgt>` | 2051 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで信号処理</src><tgt>So, this is a visual development environment. It's a visual Python development environment. You can also write flow graphs, and then you write Python code, and it generates it from there. When it runs, it performs signal processing.</tgt>` | 2674 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>されるっていう</src><tgt><\|wait\|></tgt>` | 953 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことをしている</src><tgt><\|wait\|></tgt>` | 1046 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 1010 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 823 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はい、じゃあ</src><tgt><\|wait\|></tgt>` | 403 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 820 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1332 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1768 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 878 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자 앱 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 2054 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 1194 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 60에 </src><tgt><\|wait\|></tgt>` | 1566 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPP 파이프 를 </src><tgt><\|wait\|></tgt>` | 1916 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1843 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나충과서 로 </src><tgt><\|wait\|></tgt>` | 1925 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>포인다. </src><tgt>そして、これについて多くの人が分析をしています。このRokuzアプリの分析を見ると、ソニーは60年FPPパイプを128ビットのナチュラスフォーインダにしています。</tgt>` | 2493 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 엑스에서도 </src><tgt><\|wait\|></tgt>` | 1394 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>없는 </src><tgt><\|wait\|></tgt>` | 810 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1086 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>LSI가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 871 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 687 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 852 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>for all the sorts </src><tgt><\|wait\|></tgt>` | 1331 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>that we've just discussed, </src><tgt><\|wait\|></tgt>` | 1772 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>but we're </src><tgt><\|wait\|></tgt>` | 1050 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1466 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>in the heart of love, </src><tgt><\|wait\|></tgt>` | 1766 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>so the love </src><tgt><\|wait\|></tgt>` | 1401 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>will also enter </src><tgt><\|wait\|></tgt>` | 1462 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 738 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>the time of the cross </src><tgt>우리가 방금 논의한 모든 종류의 일들에도 불구하고, 우리는 사랑의 마음속에 있기 때문에 사랑은 십자가의 시간에도</tgt>` | 2806 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>as well. </src><tgt><\|wait\|></tgt>` | 1071 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It came to pass. </src><tgt><\|wait\|></tgt>` | 1352 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>It became </src><tgt><\|wait\|></tgt>` | 1148 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1063 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>that great that </src><tgt><\|wait\|></tgt>` | 820 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it continues </src><tgt><\|wait\|></tgt>` | 411 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>to endure. </src><tgt><\|wait\|></tgt>` | 539 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1226 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1028 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>be able to move media objects </src><tgt><\|wait\|></tgt>` | 1273 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources </src><tgt><\|wait\|></tgt>` | 1575 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, if </src><tgt><\|wait\|></tgt>` | 1567 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the situation </src><tgt><\|wait\|></tgt>` | 1308 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1457 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>where you realize you've added </src><tgt><\|wait\|></tgt>` | 1833 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>the wrong media file </src><tgt>另外，虽然你不能在资源之间移动媒体对象，但如果你发现添加了错误的媒体文件，</tgt>` | 2405 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource, </src><tgt><\|wait\|></tgt>` | 942 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>we can tell us. </src><tgt><\|wait\|></tgt>` | 1398 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>Now, and we can see about </src><tgt><\|wait\|></tgt>` | 1071 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 936 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files </src><tgt><\|wait\|></tgt>` | 1033 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure to get that up </src><tgt><\|wait\|></tgt>` | 849 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 675 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1374 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1264 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1462 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the AHR field, </src><tgt><\|wait\|></tgt>` | 1665 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1515 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 1485 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 858 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant </src><tgt><\|wait\|></tgt>` | 1249 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>databases, </src><tgt><\|wait\|></tgt>` | 1719 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously for my loves. </src><tgt>最初のセクションでAHRフィールドが重要であるという部分で、少し間違ったページを見ていました。これは私の愛する人たちのために、バリアントデータベースとは明らかに違うんです。</tgt>` | 3009 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1116 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1323 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that </src><tgt><\|wait\|></tgt>` | 1156 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>need to be in these </src><tgt><\|wait\|></tgt>` | 1089 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 945 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 629 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 390 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 421 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 915 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>He knows Jesus </src><tgt><\|wait\|></tgt>` | 1223 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a hungry </src><tgt><\|wait\|></tgt>` | 1333 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and knows that </src><tgt><\|wait\|></tgt>` | 1307 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's supposed to </src><tgt><\|wait\|></tgt>` | 1599 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1589 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry, </src><tgt><\|wait\|></tgt>` | 1778 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1803 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 1768 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the Son of God, </src><tgt><\|wait\|></tgt>` | 2035 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>prove it. </src><tgt>ある時、彼はイエスが飢えていることを知っていました。そして、40日間荒野にいるはずだと知っていました。だから彼はイエスに言いました。「もしあなたが神の子なら、証明してください。」</tgt>` | 2681 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1094 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1001 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 1023 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 818 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 677 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan led by </src><tgt><\|wait\|></tgt>` | 427 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>bread alone. </src><tgt><\|wait\|></tgt>` | 323 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1247 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 929 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1065 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1401 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I I don't know </src><tgt><\|wait\|></tgt>` | 2018 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1471 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1221 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1355 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1659 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt>有意义的个人权利，而最高法院是最后才出现的，而不是引领者。我不知道法院是否想成为社会变革的先锋。如今。</tgt>` | 2795 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 581 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1396 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 863 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1078 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged </src><tgt><\|wait\|></tgt>` | 1010 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so. </src><tgt><\|wait\|></tgt>` | 859 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 553 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 416 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 466 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt>但他们更倾向于反映已经形成的共识。所以，你有一些联邦法官，</tgt>` | 549 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我們看一下</src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的圖片哦，</src><tgt><\|wait\|></tgt>` | 1336 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1319 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>圖片的部分呢，我們可以看到</src><tgt><\|wait\|></tgt>` | 1384 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一個是克汀，</src><tgt><\|wait\|></tgt>` | 1670 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>的部分，</src><tgt><\|wait\|></tgt>` | 1489 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>克汀一般</src><tgt><\|wait\|></tgt>` | 1591 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是屬於</src><tgt><\|wait\|></tgt>` | 1643 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我們在</src><tgt><\|wait\|></tgt>` | 1256 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>修習的地方</src><tgt><\|wait\|></tgt>` | 972 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>，所以呢，</src><tgt>그럼 그림을 한번 볼까요? 그림 부분에는 크티드(chitin)가 보이는데요, 크티드는 보통 우리가 배우는 곳에서</tgt>` | 2798 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>這是身體的部分，</src><tgt><\|wait\|></tgt>` | 1021 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>會反應的是</src><tgt><\|wait\|></tgt>` | 1378 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要</src><tgt><\|wait\|></tgt>` | 1133 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>給自己一點時間</src><tgt><\|wait\|></tgt>` | 933 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 438 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下來修習</src><tgt><\|wait\|></tgt>` | 806 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可由我們可以看到</src><tgt><\|wait\|></tgt>` | 696 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>這邊是消防員的嘛。</src><tgt><\|wait\|></tgt>` | 513 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 376 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是說。</src><tgt>몸의 부분이에요. 크티드는 보통 우리가 배우는 곳에서</tgt>` | 540 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 878 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 1293 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1128 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1107 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1245 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1618 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1497 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>personality is </src><tgt><\|wait\|></tgt>` | 1028 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1866 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1703 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>While they're </src><tgt>彼らは全く珍しい人々です。そして、彼らは世界を完全に変革するために現れることがよくあります。その性格は矛盾したものです。彼らは</tgt>` | 2885 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted. They also </src><tgt><\|wait\|></tgt>` | 1006 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1397 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1167 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 768 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 620 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 775 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 666 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 575 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and they </src><tgt><\|wait\|></tgt>` | 385 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt>外向的です。また、意味のない会話を嫌います。そして、すぐに本題に入りたいと思っています。彼らは議論の相手を演じるのが大好きで、</tgt>` | 774 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 323 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 344 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E and CP </src><tgt><\|wait\|></tgt>` | 352 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stand for. </src><tgt><\|wait\|></tgt>` | 330 |

---

### Test Example 58 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 870 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 ` | 13942 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 737 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 1079 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 ` | 6408 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 301 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I am Apple. I'm going to be</tgt>` | 387 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 312 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 349 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 328 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1286 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1635 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1105 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1707 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1415 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1570 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1719 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1817 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1660 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제관 순간 </src><tgt>Lee Jun-seok had claimed he was running for the party's leadership to refuse his duties, and then claimed he was running for the party's leadership to win the election, even showing off. But now, Yoon Suk-yeol, the presidential candidate, has</tgt>` | 2570 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석을 들으 내놓고 </src><tgt><\|wait\|></tgt>` | 1455 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1093 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 1089 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 892 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 666 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 439 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 344 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 298 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 286 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상 납권 </src><tgt>put Lee Jun-seok on the spot, and Yoon Suk-yeol is now showing a clear desire to defeat him. He's got a grudge and is ready to attack.</tgt>` | 790 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 299 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 355 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 357 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마 나 큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 366 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1010 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 799 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので</src><tgt><\|wait\|></tgt>` | 1194 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 995 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスローンホテルも</src><tgt><\|wait\|></tgt>` | 1710 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1269 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | 1630 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1160 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>ここゴルデスローンホテル</src><tgt>Well, I'd like to make something after dinner. So, this Golf Sloan Hotel is a place where you can have breakfast, so</tgt>` | 2575 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 576 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 1056 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1148 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみてまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1224 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 1004 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 1014 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 932 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 585 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>も歩いて</src><tgt><\|wait\|></tgt>` | 393 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt>if you're thinking about staying here, I think it's a good idea. From here, it's about a minute walk to Busan Station.</tgt>` | 887 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>かからないか</src><tgt><\|wait\|></tgt>` | 301 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルでのね</src><tgt><\|wait\|></tgt>` | 321 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 300 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 329 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 359 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさって</src><tgt><\|wait\|></tgt>` | 389 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>みてください。それなら</src><tgt><\|wait\|></tgt>` | 328 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt><\|wait\|></tgt>` | 197 |
