# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9471
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4503
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9524
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 806
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1295.4690
  - PROCESS_TIME_MS_P50: 1183.1450
  - PROCESS_TIME_MS_P95: 2190.2510
  - PROCESS_TIME_MS_MAX: 3316.4060

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 821 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1041 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 을 켜 버리 고 </src><tgt><\|wait\|></tgt>` | 1587 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 931 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1751 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모든 것을 </src><tgt><\|wait\|></tgt>` | 1119 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>죽이 는 </src><tgt><\|wait\|></tgt>` | 957 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1763 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한 사람 과 </src><tgt><\|wait\|></tgt>` | 2016 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 1434 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>것입니다. </src><tgt>I turn on Apple and kill everyone in my generation, the same generation as the pale- skinned people.</tgt>` | 1701 |

---

### Test Example 2 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 999 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1243 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>새우 용심이 가 </src><tgt><\|wait\|></tgt>` | 1851 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1129 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞이 는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1219 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1519 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1951 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해행으로 </src><tgt><\|wait\|></tgt>` | 966 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽기 만 </src><tgt>So, I'm mixing the sword spirit with the shrimp spirit. Oh, this is really</tgt>` | 2212 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1158 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>在松子这里呢？</src><tgt><\|wait\|></tgt>` | 1064 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个油量很大，</src><tgt><\|wait\|></tgt>` | 1374 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 975 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1410 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在放的是</src><tgt><\|wait\|></tgt>` | 1321 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和桃仁。</src><tgt><\|wait\|></tgt>` | 952 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1847 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>感觉</src><tgt><\|wait\|></tgt>` | 974 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1616 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>和桃仁。</src><tgt>Why is it at the pine nut? There's a lot of oil here. And I'm adding sesame and peach kernels. These</tgt>` | 2816 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 764 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 938 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>特に仲まだ</src><tgt><\|wait\|></tgt>` | 1102 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1217 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>その時点で</src><tgt><\|wait\|></tgt>` | 1177 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告</src><tgt><\|wait\|></tgt>` | 1259 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>前提を</src><tgt><\|wait\|></tgt>` | 1206 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1325 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>大図してやってあげる</src><tgt><\|wait\|></tgt>` | 1187 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 2037 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>大した</src><tgt>从一开始，那个，特别是仲还没一年级，对吧？那时候就先设定好密告的前提，大张旗鼓地做，十年过去了，</tgt>` | 2899 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1089 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1057 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まった</src><tgt><\|wait\|></tgt>` | 1083 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1108 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1162 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt><\|wait\|></tgt>` | 1373 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1176 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt><\|wait\|></tgt>` | 1871 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 760 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 2034 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src>絵、</src><tgt>大概是从这块开始的，</tgt>` | 2046 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 684 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1241 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>직성 들은 </src><tgt><\|wait\|></tgt>` | 1104 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1073 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1184 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1516 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1424 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>직성 들이 </src><tgt><\|wait\|></tgt>` | 1060 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>였기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 1676 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1947 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 901 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>The teachers on the list were actually not highly intelligent; they were just randomly selected. The teachers who didn't know the truth</tgt>` | 2467 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1137 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 987 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱交</src><tgt><\|wait\|></tgt>` | 1345 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水</src><tgt><\|wait\|></tgt>` | 1447 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>十飞，</src><tgt><\|wait\|></tgt>` | 1380 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给</src><tgt><\|wait\|></tgt>` | 803 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>主孩子心灵营养。</src><tgt><\|wait\|></tgt>` | 1861 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1675 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>你耐心等</src><tgt><\|wait\|></tgt>` | 1095 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>Parents need to use our deep love to pour out ten flights of water, nourishing their children's hearts. Be patient and wait for your child to grow up slowly.</tgt>` | 2692 |

---

### Test Example 8 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 941 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导到</src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1231 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>突破于中年，</src><tgt><\|wait\|></tgt>` | 1123 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1829 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 918 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1781 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅，</src><tgt>気数を気にするのは簡単です。でも、中年の壁を突破できるのは師匠の指導がある人だけです。だから、反省が必要です。師匠になるには、</tgt>` | 2944 |

---

### Test Example 9 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1112 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后呢，</src><tgt><\|wait\|></tgt>` | 1300 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的 electrolyte</src><tgt><\|wait\|></tgt>` | 1185 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 872 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>衰弱了，</src><tgt><\|wait\|></tgt>` | 1712 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>然后就停留在</src><tgt><\|wait\|></tgt>` | 1231 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1050 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>一个相对的低能量的</src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态。</src><tgt><\|wait\|></tgt>` | 1980 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是</src><tgt><\|wait\|></tgt>` | 1448 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>所谓的低于状态。</src><tgt>砂を洗い流すと、内部の電解質のエネルギーも衰えて、相対的に低エネルギーな稼働状態に留まります。これがいわゆる低エネルギー状態です。</tgt>` | 1977 |

---

### Test Example 10 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1201 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1382 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 990 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 1025 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>こういですね</src><tgt><\|wait\|></tgt>` | 1554 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>会話して</src><tgt><\|wait\|></tgt>` | 1375 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>いかれていきたい</src><tgt><\|wait\|></tgt>` | 919 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>とか、</src><tgt><\|wait\|></tgt>` | 1748 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>じゃあで見てと</src><tgt><\|wait\|></tgt>` | 2018 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と本気で</src><tgt><\|wait\|></tgt>` | 792 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>こうこうこうこう</src><tgt>还有，大将好像有点想拉开距离，想聊聊，然后看，然后</tgt>` | 2353 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>強いのでなので</src><tgt><\|wait\|></tgt>` | 647 |

---

### Test Example 11 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 869 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>산지 를 </src><tgt><\|wait\|></tgt>` | 824 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라고 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1286 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 기려고 들어왔어 수도 </src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 면 </src><tgt><\|wait\|></tgt>` | 1564 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여달라고 </src><tgt><\|wait\|></tgt>` | 1386 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해달라 는 거야. 내가 </src><tgt><\|wait\|></tgt>` | 1093 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1787 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주변 에 </src><tgt><\|wait\|></tgt>` | 1984 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>야. </src><tgt><\|wait\|></tgt>` | 1908 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src>내가 </src><tgt>They asked me to kill another mountain, so I came here to kill them. It's the same thing, they want me to kill them. I'm not even hearing a thing. I'm</tgt>` | 1732 |

---

### Test Example 12 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对</src><tgt><\|wait\|></tgt>` | 825 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>这种情况，</src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>我们就是遇到问题</src><tgt><\|wait\|></tgt>` | 1155 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1157 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>汇报主管，或是通知对方</src><tgt><\|wait\|></tgt>` | 1320 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们有笑这个状况。</src><tgt><\|wait\|></tgt>` | 1418 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1045 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1898 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>工具理承担。</src><tgt><\|wait\|></tgt>` | 1479 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>责任而已，</src><tgt><\|wait\|></tgt>` | 1223 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>是应该做Solution。</src><tgt>When you face a situation like this, just report it to your supervisor or let the other person know. Don't think you have to handle everything yourself. It's just your responsibility to take action and find a solution.</tgt>` | 3218 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 861 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 986 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? </src><tgt><\|wait\|></tgt>` | 1183 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>This is tip of the stem. </src><tgt><\|wait\|></tgt>` | 1917 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research looking at </src><tgt><\|wait\|></tgt>` | 1067 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1069 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1618 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1965 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. </src><tgt><\|wait\|></tgt>` | 1057 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>People that we can learn from. </src><tgt>極めて幸せな人たちに関する重要な研究を、様々な角度から行いましたか？これが枝の先端です。最も幸せな人々の10%を研究対象としています。そこから私たちは学ぶことができます。</tgt>` | 2867 |

---

### Test Example 14 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 813 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>body doing? </src><tgt><\|wait\|></tgt>` | 980 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body. </src><tgt><\|wait\|></tgt>` | 1510 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 872 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1508 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1467 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1185 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it tension in your chest? </src><tgt><\|wait\|></tgt>` | 1712 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it </src><tgt><\|wait\|></tgt>` | 2084 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the lower back where you </src><tgt><\|wait\|></tgt>` | 1950 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>use it? </src><tgt>你的身体在做什么？进入你的身体。紧张感从哪里开始？是什么？是头？胸部紧张吗？还是下背部？</tgt>` | 1697 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1130 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1010 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1156 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned that you repeat </src><tgt><\|wait\|></tgt>` | 1287 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>five or you're good at </src><tgt><\|wait\|></tgt>` | 2016 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1517 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And what you </src><tgt><\|wait\|></tgt>` | 1882 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>not good at, </src><tgt><\|wait\|></tgt>` | 1044 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get the people around you to help you with </src><tgt><\|wait\|></tgt>` | 1896 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1877 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>and tell next time </src><tgt>最后，重复。你学到重复五次就很好，多做几次。你不太擅长的事情，让身边的人来帮你，下次</tgt>` | 1536 |

---

### Test Example 16 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 836 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 907 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1040 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>という設定が</src><tgt><\|wait\|></tgt>` | 1161 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたが、</src><tgt><\|wait\|></tgt>` | 895 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1434 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1414 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt><\|wait\|></tgt>` | 1343 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1069 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>五個。</src><tgt><\|wait\|></tgt>` | 1937 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src><\|wait\|></src><tgt>그렇습니다. 거기서 ' 생각 ' 이라는 설정이 있었는데, 그 장에이치로 씨의 시스템은 다섯 가지입니다.</tgt>` | 2784 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>設定が</src><tgt><\|wait\|></tgt>` | 477 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>五つ。</src><tgt><\|wait\|></tgt>` | 956 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 826 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAがですね</src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いるな場面で</src><tgt><\|wait\|></tgt>` | 1160 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生生刻画を</src><tgt><\|wait\|></tgt>` | 1248 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>考えている時に</src><tgt><\|wait\|></tgt>` | 1451 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあAAの</src><tgt><\|wait\|></tgt>` | 1485 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>乱交調べということで</src><tgt><\|wait\|></tgt>` | 834 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あの生生刻画を</src><tgt><\|wait\|></tgt>` | 1988 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>考えてもしょうする生生刻画</src><tgt><\|wait\|></tgt>` | 2094 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>ということで保証するといった</src><tgt><\|wait\|></tgt>` | 1716 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>使い方を</src><tgt>When you're thinking about live drawing in a situation where AA is present, you can also guarantee that the live drawing will be done by AA, based on the live drawing investigation of AA.</tgt>` | 1743 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt><\|wait\|></tgt>` | 950 |

---

### Test Example 18 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이걸 너무 </src><tgt><\|wait\|></tgt>` | 1000 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>지어야 를 </src><tgt><\|wait\|></tgt>` | 1161 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>할 수 있지만 진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1406 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 1806 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 1546 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 보이 고 </src><tgt><\|wait\|></tgt>` | 1738 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 보살 로 </src><tgt><\|wait\|></tgt>` | 722 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 피라고 보이 세 우주 가 </src><tgt><\|wait\|></tgt>` | 2380 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 이라는 </src><tgt><\|wait\|></tgt>` | 2067 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src><\|wait\|></src><tgt>これをあまりに作らなきゃいけないと思っても、本当に菩薩ですよ。いや、自分の菩薩なのに夢だと見えて、私だけ菩薩に見えて宇宙が本当に菩薩という</tgt>` | 1793 |

---

### Test Example 19 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>があの</src><tgt><\|wait\|></tgt>` | 980 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 1070 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも用意して</src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>おりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1493 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1447 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 815 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1834 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1725 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何でしょうか。</src><tgt><\|wait\|></tgt>` | 958 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>内側がありますので</src><tgt>We have some T- shirts and other items available, so please feel free to join us. That's all for the contact information. Um, what is it? There's an inside part.</tgt>` | 3046 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>商品をお持ちください。</src><tgt><\|wait\|></tgt>` | 1082 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 883 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相怪的人之间</src><tgt><\|wait\|></tgt>` | 1581 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 742 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>有着某种心理，</src><tgt><\|wait\|></tgt>` | 1849 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1146 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天夜里</src><tgt><\|wait\|></tgt>` | 1568 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1973 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2035 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子思维</src><tgt>If a female high school student has some kind of psychological attachment to someone who looks strange, could it be that she started from scratch overnight?</tgt>` | 1505 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇？</src><tgt><\|wait\|></tgt>` | 1023 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 683 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 815 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个</src><tgt><\|wait\|></tgt>` | 1136 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>轨道哈，</src><tgt><\|wait\|></tgt>` | 1146 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 994 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>扎下面的时候，</src><tgt><\|wait\|></tgt>` | 1490 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日航</src><tgt><\|wait\|></tgt>` | 1396 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>日航的</src><tgt><\|wait\|></tgt>` | 1306 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>时候，我当时</src><tgt><\|wait\|></tgt>` | 1099 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被他做制服</src><tgt><\|wait\|></tgt>` | 2152 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的小小的一个愿望哈，</src><tgt>제 삶의 궤도로 돌아가게 해 주세요. 제가 잘 정착할 수 있도록, 니혼자카를 할 때, 그때 그가 제복을 입은 작은 소망을</tgt>` | 3316 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1091 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1203 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1260 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1084 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1236 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1413 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1043 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1823 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 918 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1795 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src><\|wait\|></src><tgt>好的。然后，在这些例子之后，指令告诉我们，实际上要使用这些值。</tgt>` | 2485 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>So this game.coord array </src><tgt><\|wait\|></tgt>` | 775 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1149 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 945 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunhataru, </src><tgt><\|wait\|></tgt>` | 1242 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1315 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in A/B testing </src><tgt><\|wait\|></tgt>` | 997 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>and finance </src><tgt><\|wait\|></tgt>` | 1685 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a touch of psychology. </src><tgt><\|wait\|></tgt>` | 1247 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Yeah, here I am. </src><tgt><\|wait\|></tgt>` | 1616 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And in the </src><tgt><\|wait\|></tgt>` | 2097 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 2039 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>corporate </src><tgt>제 이름은 츄나타루예요. 현재 A/B 테스트와 금융을 공부하고 있고, 심리학도 조금 접하고 있어요. 네, 여기 있어요. 앞으로는</tgt>` | 1950 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1062 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1085 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 812 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアです。ギアが</src><tgt><\|wait\|></tgt>` | 1164 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと</src><tgt><\|wait\|></tgt>` | 1154 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなって</src><tgt><\|wait\|></tgt>` | 1189 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>しまうので、</src><tgt><\|wait\|></tgt>` | 1233 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1378 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1285 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>逆ネジのナットが</src><tgt><\|wait\|></tgt>` | 1225 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついてるっていうこと</src><tgt><\|wait\|></tgt>` | 2106 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 안 들어오니까, 기어 끝에 역나사 볼트가 붙어 있는 거죠.</tgt>` | 2938 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1012 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解完了。</src><tgt><\|wait\|></tgt>` | 1114 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 853 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1306 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. </src><tgt><\|wait\|></tgt>` | 1036 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>And when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1958 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1108 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 1049 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1989 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 2030 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>to make </src><tgt>고무줄처럼 늘어난 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다. 또는</tgt>` | 2263 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1251 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 846 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是进入到</src><tgt><\|wait\|></tgt>` | 819 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 1129 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>并服务</src><tgt><\|wait\|></tgt>` | 1142 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 816 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们。</src><tgt><\|wait\|></tgt>` | 1696 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1306 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1114 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>维生运动好事几点，</src><tgt><\|wait\|></tgt>` | 1412 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 2037 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>给维生运动</src><tgt>2つ目は、二クラスに移行して、一線一線で戦うトッププレイヤーたちをサポートすることです。例えば、維生運動の好事几点をするなら、</tgt>` | 3042 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>公平的星棒</src><tgt><\|wait\|></tgt>` | 1116 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1383 |

---

### Test Example 27 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这</src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>个罗马呢，</src><tgt><\|wait\|></tgt>` | 1266 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是因为</src><tgt><\|wait\|></tgt>` | 1045 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>造成了，所以呢，</src><tgt><\|wait\|></tgt>` | 1461 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1321 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>熟悉了</src><tgt><\|wait\|></tgt>` | 880 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>你的一些衣基啊</src><tgt><\|wait\|></tgt>` | 1886 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景，</src><tgt><\|wait\|></tgt>` | 848 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 1781 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>戏之间就</src><tgt>皆さんに注意してほしいのですが、このローマは、あなたが今慣れ親しんだ服や風景が原因で、</tgt>` | 2712 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 611 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 1175 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>一位的朋友呢，</src><tgt><\|wait\|></tgt>` | 1256 |

---

### Test Example 28 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 913 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>胡波乱跳，</src><tgt><\|wait\|></tgt>` | 1457 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 991 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1814 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>切肩大概</src><tgt><\|wait\|></tgt>` | 1127 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 943 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来剪断，</src><tgt><\|wait\|></tgt>` | 1774 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 1953 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 984 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>都没有问题。</src><tgt>Everything was normal back then, I was just flustered. So I insisted on not cutting it open. I had to cut it about twelve times to cut through it. I had to kick it, lift it, and it was all fine.</tgt>` | 3011 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他能</src><tgt><\|wait\|></tgt>` | 946 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很疑惑的打开。</src><tgt><\|wait\|></tgt>` | 1302 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>扎了一个</src><tgt><\|wait\|></tgt>` | 779 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>箭头上，</src><tgt><\|wait\|></tgt>` | 1053 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1192 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了箭头上，</src><tgt><\|wait\|></tgt>` | 1132 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1558 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>抓住</src><tgt><\|wait\|></tgt>` | 1243 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手，</src><tgt><\|wait\|></tgt>` | 846 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着哎，</src><tgt><\|wait\|></tgt>` | 1876 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再去操作</src><tgt><\|wait\|></tgt>` | 1156 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 1488 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt>矢を刺しました。矢を刺した場合は、必ず手で掴んでください。そうしないと、操作を続けようとして、</tgt>` | 2793 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 859 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1064 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1161 |

---

### Test Example 30 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1240 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1588 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 787 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1896 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how </src><tgt><\|wait\|></tgt>` | 1295 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1112 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 1330 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 2004 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2056 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>The meanings of </src><tgt>19번째 수정헌법의 의미를 살펴보고, 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침으로 그 역사를 탐구해 보겠습니다.</tgt>` | 1865 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>the amendment. Of course, </src><tgt><\|wait\|></tgt>` | 1077 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Mary. </src><tgt><\|wait\|></tgt>` | 1324 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 905 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>or if you have to </src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>produce something written, </src><tgt><\|wait\|></tgt>` | 1387 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1035 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize </src><tgt><\|wait\|></tgt>` | 1589 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>that you don't even know </src><tgt><\|wait\|></tgt>` | 1384 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1130 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. It's like, oh, </src><tgt><\|wait\|></tgt>` | 1826 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 2047 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a double </src><tgt><\|wait\|></tgt>` | 1967 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src><\|wait\|></src><tgt>ええと、あるいは何か書く必要がある場合、文章を書く必要がある場合、そもそも単語のスペルがわからないことに気づく。まるで「あ、この単語は</tgt>` | 1973 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>P, double N. I don't know </src><tgt><\|wait\|></tgt>` | 1347 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 891 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 992 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个戴雪的人，但是他是</src><tgt><\|wait\|></tgt>` | 1244 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的，</src><tgt><\|wait\|></tgt>` | 1905 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1317 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这通场吗这样的一个状况</src><tgt><\|wait\|></tgt>` | 1491 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>需要去</src><tgt><\|wait\|></tgt>` | 929 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意的是。</src><tgt><\|wait\|></tgt>` | 1944 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1589 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt>이 부분은 눈을 덮은 사람을 보여줍니다. 하지만 그는 역방향입니다. 이 상황을 특별히 주의해야 합니다. 그가</tgt>` | 1636 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他跳不到</src><tgt><\|wait\|></tgt>` | 1111 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1374 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>与你的意识。</src><tgt><\|wait\|></tgt>` | 1062 |

---

### Test Example 33 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐 이라는 </src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 1168 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유도 전류 인가 </src><tgt><\|wait\|></tgt>` | 1607 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 701 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 전기 나르 충동 을 </src><tgt><\|wait\|></tgt>` | 2031 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>보긴 </src><tgt><\|wait\|></tgt>` | 1248 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 </src><tgt><\|wait\|></tgt>` | 1184 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>아주 당뇨 미네랄 이다. </src><tgt><\|wait\|></tgt>` | 1431 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1992 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 </src><tgt><\|wait\|></tgt>` | 1896 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>제 그런 거죠. 이제 </src><tgt>Things like vanadium are basically induced currents, or rather, they look like electric current pulses. They are very, very, very, uh, they are called diabetes minerals. That's what it is. Now,</tgt>` | 2263 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1396 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아니면 </src><tgt><\|wait\|></tgt>` | 1097 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 864 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개가 </src><tgt><\|wait\|></tgt>` | 1110 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중화 버스 10만 미만 으로 </src><tgt><\|wait\|></tgt>` | 1819 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1018 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1430 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1456 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1625 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 혹은 </src><tgt><\|wait\|></tgt>` | 818 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해화법에 그껴도 되는데 </src><tgt><\|wait\|></tgt>` | 2397 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이거 는 </src><tgt><\|wait\|></tgt>` | 1787 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>소기업 들은 </src><tgt>そのうち150社は中国バス10万台未満の非常に小さな企業でした。一般的に、中小企業は成長するか、あるいは海運法に縛られてもいいのですが、これは中小企業は</tgt>` | 2140 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt><\|wait\|></tgt>` | 1484 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1419 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 949 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1004 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there's </src><tgt><\|wait\|></tgt>` | 1256 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such instances </src><tgt><\|wait\|></tgt>` | 1042 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>before. </src><tgt><\|wait\|></tgt>` | 1228 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>Net future TC </src><tgt><\|wait\|></tgt>` | 1265 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1176 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>is just </src><tgt><\|wait\|></tgt>` | 1875 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1064 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1717 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事，这种情况以前发生过。NetfutureTC只是另一个地方看。嗯，</tgt>` | 2469 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 697 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>But developers or engineers </src><tgt><\|wait\|></tgt>` | 1149 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>who's been in Bug Repos should be </src><tgt><\|wait\|></tgt>` | 1519 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 1125 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>実は</src><tgt><\|wait\|></tgt>` | 950 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手とか</src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>ですか？</src><tgt><\|wait\|></tgt>` | 1090 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>恐らく十秒で</src><tgt><\|wait\|></tgt>` | 1259 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1153 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1249 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1331 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せつなんですかね。</src><tgt><\|wait\|></tgt>` | 1962 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1536 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1094 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>恐らく</src><tgt>其实是1二手吗？大概十秒，嗯，一秒左右吧。然后</tgt>` | 2443 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一</src><tgt><\|wait\|></tgt>` | 602 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>二で</src><tgt><\|wait\|></tgt>` | 981 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1299 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1168 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 611 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 881 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>呃，</src><tgt><\|wait\|></tgt>` | 979 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>hterm이라고 하는 </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1058 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1949 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1322 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1248 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 어 언어 의 </src><tgt><\|wait\|></tgt>` | 1388 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2061 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 을 알게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 2190 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>그것 들을 </src><tgt>呃，计算机，也就是hterm，</tgt>` | 737 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1121 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 1374 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1164 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 674 |

---

### Test Example 38 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1383 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1191 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏正财的部分</src><tgt><\|wait\|></tgt>` | 896 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1795 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>一直是在事业方面的业绩</src><tgt><\|wait\|></tgt>` | 1211 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>和所带的红利。</src><tgt><\|wait\|></tgt>` | 1186 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1429 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>收入的提升。如果</src><tgt><\|wait\|></tgt>` | 2001 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>在投资理财方面</src><tgt><\|wait\|></tgt>` | 1728 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>这个月</src><tgt>財運についてですが、今月はかなり良いと言えます。ただ、正財の部分は、仕事の業績や、持ち前の縁起の良さによる収入の増加が中心です。投資や資産運用に関しては、今月</tgt>` | 2162 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | 1011 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说</src><tgt><\|wait\|></tgt>` | 1171 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 1147 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一点。</src><tgt><\|wait\|></tgt>` | 440 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1174 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>is just getting going </src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1274 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1030 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I got ten of them </src><tgt><\|wait\|></tgt>` | 1964 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are </src><tgt><\|wait\|></tgt>` | 1289 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important. </src><tgt><\|wait\|></tgt>` | 1146 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1333 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go </src><tgt><\|wait\|></tgt>` | 2128 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>and do I have about </src><tgt><\|wait\|></tgt>` | 1937 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>one minute videos </src><tgt>「今まさに動き出そうとしている人、これ、本当に大事なやつなんです。1分間の動画を</tgt>` | 1384 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>of all this video. </src><tgt><\|wait\|></tgt>` | 1128 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 1347 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>each one </src><tgt><\|wait\|></tgt>` | 1026 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 758 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1080 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어치 보면 </src><tgt><\|wait\|></tgt>` | 1135 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1603 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 815 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1761 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1210 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1132 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1495 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1574 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 한 거라는 </src><tgt><\|wait\|></tgt>` | 1090 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>조금 </src><tgt>呃，你看，他就是和你一起经历20岁的人，也是家人一样的弟弟。所以，</tgt>` | 2404 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 632 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1086 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 1287 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내놓고 </src><tgt><\|wait\|></tgt>` | 1110 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>생각 했습니다. </src><tgt><\|wait\|></tgt>` | 735 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1209 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새로 </src><tgt><\|wait\|></tgt>` | 991 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>밝을 거야. </src><tgt><\|wait\|></tgt>` | 1165 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1085 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>서름이 </src><tgt><\|wait\|></tgt>` | 1184 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>돋은 자태 도 </src><tgt><\|wait\|></tgt>` | 1376 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>보기 너무 </src><tgt><\|wait\|></tgt>` | 1112 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>힘들 어서 같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1972 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 1165 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>너무 놀릴 </src><tgt><\|wait\|></tgt>` | 1571 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>거고 미니 오미야 </src><tgt>目を閉じて、新しい光が見えるよ。今、目つきが鋭い姿を見せて、一緒に遊ぼうって言ってるんだ。お化けが怖くて、</tgt>` | 3108 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1163 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주다니까 </src><tgt><\|wait\|></tgt>` | 1343 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 1222 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 565 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1060 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう蒸らせてやれ。</src><tgt><\|wait\|></tgt>` | 1036 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1071 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1201 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>火勢を見ている。</src><tgt><\|wait\|></tgt>` | 1215 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1283 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 1870 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈火勢気勢。</src><tgt><\|wait\|></tgt>` | 936 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>長年</src><tgt>그럼 그냥 끓여버려. 난 불길이 치솟는 걸 보고 있어. 이미 한계치를 훨씬 넘어선 불길이, 불길이</tgt>` | 2845 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふな大国を</src><tgt><\|wait\|></tgt>` | 1091 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やっている。</src><tgt><\|wait\|></tgt>` | 1141 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1099 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい海賊線を</src><tgt><\|wait\|></tgt>` | 963 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 912 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 980 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1306 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 981 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1449 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1550 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1085 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1659 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1975 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, </src><tgt><\|wait\|></tgt>` | 1318 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>학력 수준. 실제로 교육은 얼마나 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계의 학력 수준입니다. 대학에 가셨나요? 만약 그렇다면, 졸업하셨나요?</tgt>` | 2663 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1140 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1282 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 1245 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 903 |

---

### Test Example 44 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 852 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 </src><tgt><\|wait\|></tgt>` | 1174 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>이방인 으로 있을 때에 </src><tgt><\|wait\|></tgt>` | 1195 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1813 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 우상 에게로 </src><tgt><\|wait\|></tgt>` | 1591 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1467 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1032 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2021 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 </src><tgt><\|wait\|></tgt>` | 1820 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>내가 너희에게 </src><tgt>あなたたちも知っているでしょう。ここで異邦人としているとき、言葉を話せない偶像へとそのまま連れて行かれてしまったのです。ですから、私はあなたたちに</tgt>` | 1954 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1065 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1294 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1088 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1010 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 862 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. </src><tgt><\|wait\|></tgt>` | 1240 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1360 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1676 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨턴트 예요. </src><tgt><\|wait\|></tgt>` | 1421 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>미리 컨설턴트 </src><tgt><\|wait\|></tgt>` | 1218 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>여가지고 </src><tgt><\|wait\|></tgt>` | 1474 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1946 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1878 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>そうですね、もちろんこういうケースもあります。AさんとBさんがコンサルタントで、事前にコンサルタントとして、Aさんが悪意のあるコードを</tgt>` | 1480 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1074 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로 사이트 </src><tgt><\|wait\|></tgt>` | 1477 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>스크립트 에서 </src><tgt><\|wait\|></tgt>` | 1128 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>X 파일까지 </src><tgt><\|wait\|></tgt>` | 624 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까 </src><tgt><\|wait\|></tgt>` | 1054 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감에 </src><tgt><\|wait\|></tgt>` | 1263 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매 입니다. </src><tgt><\|wait\|></tgt>` | 1299 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1082 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1048 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1644 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 간 데 </src><tgt><\|wait\|></tgt>` | 1313 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 </src><tgt><\|wait\|></tgt>` | 1130 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>가면 말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1663 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 는 것도 </src><tgt><\|wait\|></tgt>` | 2142 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장려 리요. </src><tgt><\|wait\|></tgt>` | 1989 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>좀 취해야 </src><tgt>进去的时候非常迷茫。因为我开车过来，所以走路的时候，去江南区的话，那更是没得说，出国的话也是鼓励的。得</tgt>` | 1769 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>네 대신 에 </src><tgt><\|wait\|></tgt>` | 1031 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt><\|wait\|></tgt>` | 1102 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>노발. </src><tgt><\|wait\|></tgt>` | 1167 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>그거 는 다인 거 같아요. </src><tgt><\|wait\|></tgt>` | 694 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 700 |

---

### Test Example 47 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>Fourth of </src><tgt><\|wait\|></tgt>` | 790 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the month </src><tgt><\|wait\|></tgt>` | 986 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>is the day </src><tgt><\|wait\|></tgt>` | 1115 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 1122 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>we are </src><tgt><\|wait\|></tgt>` | 1192 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>in love </src><tgt><\|wait\|></tgt>` | 1179 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>with each other. </src><tgt><\|wait\|></tgt>` | 1381 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1681 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>也同时进入</src><tgt><\|wait\|></tgt>` | 662 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2038 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>恨在早上的时候，</src><tgt>4일은 우리가 서로 사랑하는 날입니다. 아침에 우리는 서로를 사랑하는 동시에,</tgt>` | 2680 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>他爱。</src><tgt><\|wait\|></tgt>` | 517 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上。</src><tgt><\|wait\|></tgt>` | 1063 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>他就变成恨。</src><tgt><\|wait\|></tgt>` | 1385 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1156 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个钟摆。</src><tgt><\|wait\|></tgt>` | 611 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 959 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | 458 |

---

### Test Example 48 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, </src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>then self-defining </src><tgt><\|wait\|></tgt>` | 1374 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think that standard is, </src><tgt><\|wait\|></tgt>` | 1245 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1948 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1344 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is that </src><tgt><\|wait\|></tgt>` | 1523 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt><\|wait\|></tgt>` | 1037 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block, </src><tgt><\|wait\|></tgt>` | 2100 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have </src><tgt><\|wait\|></tgt>` | 1937 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>活動、そして自分自身でその基準を定義すること。なぜなら、あなたは完全に正しいからです。しかし現実には、私たちはブロックの新しい猫であり、</tgt>` | 1616 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 years ago. </src><tgt><\|wait\|></tgt>` | 1208 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>We are being held to </src><tgt><\|wait\|></tgt>` | 1299 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt><\|wait\|></tgt>` | 1064 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 959 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to a higher standard. </src><tgt><\|wait\|></tgt>` | 642 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 </src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 </src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다음에 </src><tgt><\|wait\|></tgt>` | 1580 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 864 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1744 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 1472 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1187 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1280 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 2147 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1932 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>주도 하면서 </src><tgt>The stock index is showing an upward trend. After this, we'll see some large- cap stocks lead the market with a sharp rise. But first, these lighter stocks will lead the market</tgt>` | 2091 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 1149 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시 총이 </src><tgt><\|wait\|></tgt>` | 1183 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 920 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1039 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | 551 |

---

### Test Example 50 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1132 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉</src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1269 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真实意图的。</src><tgt><\|wait\|></tgt>` | 1112 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1790 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1300 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1163 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1440 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2030 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1960 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人</src><tgt>相手の感情や本当の意図を推し量ったり感じ取ったりするんです。よく、こう言われるんですよ。「ねえ、この人は</tgt>` | 1603 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了。</src><tgt><\|wait\|></tgt>` | 1199 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1206 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1184 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 549 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 790 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 568 |

---

### Test Example 51 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1138 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1160 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1420 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 827 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 2039 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt><\|wait\|></tgt>` | 1301 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルに書いた</src><tgt><\|wait\|></tgt>` | 1815 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>後、それとは</src><tgt><\|wait\|></tgt>` | 716 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから</src><tgt><\|wait\|></tgt>` | 2260 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | 1879 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで信号処理</src><tgt>This is, well, not just a visual development environment, but a visual Python development environment. Because you write a flow graph in Visual, and then that's converted into Python code, which is executed, and that's how</tgt>` | 2368 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1286 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているから</src><tgt><\|wait\|></tgt>` | 1067 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 620 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 931 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はいじゃあ</src><tgt><\|wait\|></tgt>` | 584 |

---

### Test Example 52 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 838 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1167 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1614 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 635 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자 의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 2030 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 1320 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 칩에 </src><tgt><\|wait\|></tgt>` | 1378 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPD 파이프 를 </src><tgt><\|wait\|></tgt>` | 1131 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 2204 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나충가서 로 보인 다. </src><tgt><\|wait\|></tgt>` | 2250 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src><\|wait\|></src><tgt>そして、これについて多くの人が分析しています。このロクジャの分析を見ると、ソニーがこのロクチップのFPDパイプを128ビットに、つまり</tgt>` | 1678 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1522 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1196 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>CS가 </src><tgt><\|wait\|></tgt>` | 645 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>여기 도 없다. </src><tgt><\|wait\|></tgt>` | 977 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 560 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, </src><tgt><\|wait\|></tgt>` | 1002 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to move </src><tgt><\|wait\|></tgt>` | 1415 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>meedia objects </src><tgt><\|wait\|></tgt>` | 1033 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1449 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources </src><tgt><\|wait\|></tgt>` | 1447 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, </src><tgt><\|wait\|></tgt>` | 834 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 1973 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1784 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>where you realize you've added </src><tgt><\|wait\|></tgt>` | 927 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src><\|wait\|></src><tgt>另外，你将无法在资源之间移动媒体对象，但如果你发现</tgt>` | 2253 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 673 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource, </src><tgt><\|wait\|></tgt>` | 1149 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1289 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1155 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files </src><tgt><\|wait\|></tgt>` | 683 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 845 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>it gets back to proper way. </src><tgt><\|wait\|></tgt>` | 627 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 917 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>and it warns Jesus </src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>of hunger. </src><tgt><\|wait\|></tgt>` | 1203 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1036 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1879 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1378 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days </src><tgt><\|wait\|></tgt>` | 1107 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>that he's hungry, </src><tgt><\|wait\|></tgt>` | 1451 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>and so he says to Jesus, </src><tgt><\|wait\|></tgt>` | 2264 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>Hey, if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | 2375 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src><\|wait\|></src><tgt>ある時、イエスは飢えについて警告します。彼は、40日間荒野にいる間、飢えることになるだろうと知っています。だからイエスにこう言います。「おい、もしお前が神の子なら、証明してみろ」</tgt>` | 2334 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1341 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did </src><tgt><\|wait\|></tgt>` | 1047 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>Jesus deal with that </src><tgt><\|wait\|></tgt>` | 839 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 512 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 420 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan </src><tgt><\|wait\|></tgt>` | 436 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>led by bread alone. </src><tgt><\|wait\|></tgt>` | 436 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 799 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual write, </src><tgt><\|wait\|></tgt>` | 1136 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1178 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 794 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. And I don't know </src><tgt><\|wait\|></tgt>` | 1857 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1349 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1843 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1080 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1648 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt>有意义的个人写作，最高法院最后才加入，而不是引领。我不知道法院是否想成为社会变革的先锋。现在。</tgt>` | 2733 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 998 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 934 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1151 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1054 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 520 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 841 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 550 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 396 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 214 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 373 |

---

### Test Example 56 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1337 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1091 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1388 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 926 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1864 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1294 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1163 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1281 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1954 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 973 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously to my loves. </src><tgt>最初のセクションで、AHRフィールドが重要であるという話に少し迷い込んでしまいました。バリアントデータベースと比べると、明らかに私の愛する人たちにとって</tgt>` | 2691 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt><\|wait\|></tgt>` | 1032 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>if we don't agree </src><tgt><\|wait\|></tgt>` | 1392 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1021 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in </src><tgt><\|wait\|></tgt>` | 680 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>these data sources </src><tgt><\|wait\|></tgt>` | 993 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. </src><tgt><\|wait\|></tgt>` | 575 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>There's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 528 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 445 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1180 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1282 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 1047 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1636 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>一个是克汀的部分，</src><tgt><\|wait\|></tgt>` | 1272 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>克汀一般</src><tgt><\|wait\|></tgt>` | 1087 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1583 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1959 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>我们在吸收</src><tgt><\|wait\|></tgt>` | 822 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>的地方，</src><tgt>그럼 사진을 한번 볼까요? 사진 부분에서 크틴이 보이네요. 크틴은 보통 우리가 흡수하는 곳에</tgt>` | 2493 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 989 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分会反应的是</src><tgt><\|wait\|></tgt>` | 1213 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 996 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1112 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的做</src><tgt><\|wait\|></tgt>` | 864 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>下来吸收，</src><tgt><\|wait\|></tgt>` | 526 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们可以看到</src><tgt><\|wait\|></tgt>` | 401 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是五个一人的嘛。</src><tgt><\|wait\|></tgt>` | 469 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 429 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 364 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 987 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1303 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 981 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1445 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>to completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1547 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 966 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is </src><tgt><\|wait\|></tgt>` | 1720 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1982 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 803 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>Well, they're </src><tgt>彼らは完全に稀で、世界を完全に変革しに来ることがよくあります。その性格は矛盾しているんです。まあ、彼らは</tgt>` | 2603 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted. </src><tgt><\|wait\|></tgt>` | 1067 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>They also hate </src><tgt><\|wait\|></tgt>` | 1148 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1067 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 991 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like to get straight to </src><tgt><\|wait\|></tgt>` | 968 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 529 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 287 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 420 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>the devil's advocate, </src><tgt><\|wait\|></tgt>` | 477 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 379 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 316 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 314 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. stands for </src><tgt><\|wait\|></tgt>` | 377 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for. </src><tgt><\|wait\|></tgt>` | 289 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>경무를 거부 한 </src><tgt><\|wait\|></tgt>` | 1333 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1289 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 802 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1954 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1382 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1632 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 826 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2116 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1949 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>Lee Jun- seok previously claimed he was running for the nomination to reject the nomination of the former minister, and even boasted about it. But now, the moment Yoon Suk- yeol removed Kim Jong- in</tgt>` | 2222 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 애놓고 </src><tgt><\|wait\|></tgt>` | 1525 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1059 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 757 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 품은 </src><tgt><\|wait\|></tgt>` | 871 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 586 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 455 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 454 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt><\|wait\|></tgt>` | 357 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 306 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 청상납건 </src><tgt><\|wait\|></tgt>` | 305 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 271 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 284 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 229 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>얼마나 큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 275 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>で、まあ</src><tgt><\|wait\|></tgt>` | 1029 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 937 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいな</src><tgt><\|wait\|></tgt>` | 1146 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>です。なので</src><tgt><\|wait\|></tgt>` | 1187 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね、ゴルフスロホテル</src><tgt><\|wait\|></tgt>` | 1267 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も朝食が</src><tgt><\|wait\|></tgt>` | 1427 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1140 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1872 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっている</src><tgt><\|wait\|></tgt>` | 1207 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので、今後ね</src><tgt><\|wait\|></tgt>` | 1514 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>ここゴルドストンホテル</src><tgt>So, I'd like to make a meal after dinner. Since the golf resort hotel here has breakfast available, I'm planning to</tgt>` | 2764 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt><\|wait\|></tgt>` | 1000 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>という方はですね、</src><tgt><\|wait\|></tgt>` | 1118 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt><\|wait\|></tgt>` | 998 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見て、まあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1163 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと、はい。</src><tgt><\|wait\|></tgt>` | 873 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 431 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね、</src><tgt><\|wait\|></tgt>` | 497 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 426 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 468 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本かかるか</src><tgt><\|wait\|></tgt>` | 361 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんでないか</src><tgt><\|wait\|></tgt>` | 319 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 314 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地ね、まあホテル</src><tgt><\|wait\|></tgt>` | 357 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので、</src><tgt><\|wait\|></tgt>` | 330 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 270 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 207 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 190 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね、今回は</src><tgt><\|wait\|></tgt>` | 183 |
