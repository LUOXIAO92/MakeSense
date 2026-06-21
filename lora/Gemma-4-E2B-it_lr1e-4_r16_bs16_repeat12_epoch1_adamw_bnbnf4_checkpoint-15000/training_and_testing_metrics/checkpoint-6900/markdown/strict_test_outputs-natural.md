# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9513
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7020
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.8283
  - TGT_RELEASE_TOTAL: 495
  - TGT_WAIT_ACCURACY: 0.7032
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1323.4510
  - PROCESS_TIME_MS_P50: 1359.9250
  - PROCESS_TIME_MS_P95: 2051.9690
  - PROCESS_TIME_MS_MAX: 3700.5640

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>放在此处一点，</src><tgt>Place it here,</tgt>` | 1008 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个友星尼亚很大。</src><tgt>this area is quite large.</tgt>` | 1398 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1381 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt>Then,</tgt>` | 944 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我再放大。</src><tgt>I'll zoom in again.</tgt>` | 921 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人，</src><tgt>And the clay people,</tgt>` | 1940 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1367 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>感觉吧？</src><tgt>you feel it, right?</tgt>` | 1455 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1052 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>和陶人，</src><tgt>these clay people...</tgt>` | 1675 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt>从一开始</tgt>` | 838 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1244 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>这个，毕竟才一年级嘛。</tgt>` | 1526 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>この時点で</src><tgt>这时候</tgt>` | 1367 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 825 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1527 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1379 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>こうタイズしてってあげると</src><tgt>如果剪短枝条，</tgt>` | 2056 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>十年経っても</src><tgt>十年后</tgt>` | 627 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>大した。</src><tgt>也还行。</tgt>` | 2031 |

---

### Test Example 3 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | 1259 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 937 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离在慢慢拉开，</tgt>` | 1513 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>オシャレる方がやっぱ</src><tgt>穿得好看的人</tgt>` | 1348 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>多いですね。</src><tgt>确实比较多。</tgt>` | 1570 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>開業して</src><tgt><\|wait\|></tgt>` | 1277 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>行き来して다가</src><tgt>来来回来</tgt>` | 1050 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>市</src><tgt><\|wait\|></tgt>` | 1049 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>徐々に</src><tgt>在市里</tgt>` | 1201 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と透明性が</src><tgt><\|wait\|></tgt>` | 1445 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>高くなるので、</src><tgt>逐渐透明化，</tgt>` | 1674 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので</src><tgt>所以</tgt>` | 830 |

---

### Test Example 4 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1196 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是</src><tgt>What parents need to do is</tgt>` | 1544 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 857 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1329 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt>water them with our deep love,</tgt>` | 1576 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>fertilize them,</tgt>` | 747 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1419 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心理营养，</src><tgt>and provide the children with the psychological nourishment they need.</tgt>` | 2078 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1652 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>并耐心等待</src><tgt>And patiently wait</tgt>` | 888 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>as they grow up.</tgt>` | 1908 |

---

### Test Example 5 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气熟，</src><tgt>気合を入れないと、</tgt>` | 1546 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>是容易的。</src><tgt>簡単ですよ。</tgt>` | 764 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>但是</src><tgt>でも、</tgt>` | 1024 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师父</src><tgt>師匠が</tgt>` | 1170 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>知道，</src><tgt><\|wait\|></tgt>` | 550 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如何处于</src><tgt><\|wait\|></tgt>` | 1481 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>终点，</src><tgt>終点にどうやってたどり着くかを知っているのは一人のみです。</tgt>` | 2712 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>だから</tgt>` | 1377 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>虚牙反。</src><tgt>虚牙反です。</tgt>` | 1659 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 735 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师父。</src><tgt>師匠になるには、</tgt>` | 2086 |

---

### Test Example 6 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>抛洒完以后呢，</src><tgt>撒き終わった後、</tgt>` | 1776 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的压力减轻，</src><tgt>内部の圧力が</tgt>` | 928 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了，</src><tgt>弱まり、エネルギーも</tgt>` | 1128 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>然后</src><tgt>衰弱します。そして</tgt>` | 1605 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | 1785 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1135 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>能量的运行</src><tgt>比較的低いエネルギーの</tgt>` | 1376 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>状态，</src><tgt>運行状態に留まります。</tgt>` | 1654 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | 1552 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | 1172 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大抵</src><tgt>通常</tgt>` | 1068 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这之后</tgt>` | 1005 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1295 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>开始，</tgt>` | 1162 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt>高更</tgt>` | 584 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>和高安</tgt>` | 1502 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1358 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt>和塞尚</tgt>` | 1533 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt>等</tgt>` | 1321 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1638 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>は、田舎の</src><tgt>画家的作品，</tgt>` | 1744 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>中学生でも。</src><tgt>连乡村中学生</tgt>` | 1039 |

---

### Test Example 8 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | 957 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | 983 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1151 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` | 1430 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>紧张感</tgt>` | 1352 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>从哪里开始？是什么？</tgt>` | 1168 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | 1469 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是胸闷吗？</tgt>` | 1882 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>I ask them what </src><tgt>我问他们</tgt>` | 1705 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1063 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | 1794 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>자 그러면 </src><tgt>Alright,</tgt>` | 1000 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>농심이 </src><tgt><\|wait\|></tgt>` | 1010 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1328 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>아 칼 농심이 </src><tgt><\|wait\|></tgt>` | 1257 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>소스 농심이 </src><tgt><\|wait\|></tgt>` | 566 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1388 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데 요. </src><tgt>so, there's Nongshim, oh, Kal Nongshim, and also Sauce Nongshim mixed together.</tgt>` | 2952 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>야 </src><tgt>Wow,</tgt>` | 1267 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1631 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>해당 으로 </src><tgt><\|wait\|></tgt>` | 1254 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 죽입니다, 지금. </src><tgt>this is really starting to die now.</tgt>` | 1961 |

---

### Test Example 10 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1129 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>Apple 철빨시키고 </src><tgt><\|wait\|></tgt>` | 1200 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1378 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1334 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>페모를 </src><tgt><\|wait\|></tgt>` | 797 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>죽인 데려나 </src><tgt><\|wait\|></tgt>` | 1757 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1384 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1363 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt><\|wait\|></tgt>` | 1320 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>없다. </src><tgt>I'm Apple, I'm a ' Cheol- ppal- sik- go ', and I'm from the same generation as Park Han- sang, who killed my ' Pemo '.</tgt>` | 3701 |

---

### Test Example 11 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>情况，我们就是</src><tgt>In the face of this situation,</tgt>` | 1537 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 820 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>if you run into a problem, just report it to your supervisor immediately.</tgt>` | 1613 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt>Or</tgt>` | 1445 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们学校这个状况，</src><tgt>let the school know about the situation.</tgt>` | 1912 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt>Don't think</tgt>` | 1176 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>you have to handle everything yourself.</tgt>` | 1957 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>不理成担，</src><tgt>Just take responsibility.</tgt>` | 1200 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>整体而言</src><tgt>Overall,</tgt>` | 2023 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>是给主讯。</src><tgt>it's about the main message.</tgt>` | 1719 |

---

### Test Example 12 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | 1184 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주겨 달라 해가지고 내가 </src><tgt>They asked me to get another cup, so I</tgt>` | 1781 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>주길 넣어주도 </src><tgt>put in</tgt>` | 792 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1551 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>아스다. 다른 잔찜에 주겨 달라 해. </src><tgt>another cup. They asked for another cup.</tgt>` | 1864 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>제 말이야. 내가 </src><tgt>I mean,</tgt>` | 1196 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1592 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알았느냐? </src><tgt>did you think I didn't hear that?</tgt>` | 1843 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2036 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 가. </src><tgt>I'm going.</tgt>` | 1591 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1267 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1072 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复。</tgt>` | 1131 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>学会洗漱再重复。</tgt>` | 1478 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>Find what you're good at </src><tgt>找到你擅长</tgt>` | 1702 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>的事情，多做一些。</tgt>` | 2036 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1256 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>And what you're not good at, </src><tgt>而你不擅长的，</tgt>` | 2301 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with. </src><tgt>就请周围的人帮忙。</tgt>` | 903 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1944 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>And until next time. </src><tgt>我们下次再见。</tgt>` | 1725 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 989 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1285 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 993 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is typical </src><tgt>非常に幸せな人たちについて重要な研究を行いました。これは</tgt>` | 1650 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1487 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>of the STEM research, </src><tgt>STEM研究の典型的なものですね。</tgt>` | 1868 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>looking at the 10% </src><tgt><\|wait\|></tgt>` | 1301 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1274 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>最も幸せな人々の10%を</tgt>` | 1779 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, </src><tgt>見ているんです。</tgt>` | 2097 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>people that we can learn from. </src><tgt>私たちが学べる人たちです。</tgt>` | 1846 |

---

### Test Example 15 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そうです。</src><tgt>맞아요.</tgt>` | 912 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこで</src><tgt>그럼</tgt>` | 809 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天気</src><tgt><\|wait\|></tgt>` | 1344 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>豊を受付時が</src><tgt>텐키 토세츠비시기가</tgt>` | 1319 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>来ましたね。</src><tgt>왔네요.</tgt>` | 586 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>그래서</tgt>` | 1425 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1378 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>危険呼出の仕組み</src><tgt>키켄 호슈츠의</tgt>` | 1689 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1364 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>は五本</src><tgt>구조는</tgt>` | 1545 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1312 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>受注時</src><tgt><\|wait\|></tgt>` | 1316 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>五本です。</src><tgt>5본입니다.</tgt>` | 1628 |

---

### Test Example 16 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1276 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 1386 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 901 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1481 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1626 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1881 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1085 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 의미 입니다. </src><tgt>The fact that they were randomly selected is what it means.</tgt>` | 2293 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 984 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 모를 last </src><tgt><\|wait\|></tgt>` | 2162 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>면 교사 들은 </src><tgt>The teachers who don't know the truth</tgt>` | 1865 |

---

### Test Example 17 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツ</src><tgt><\|wait\|></tgt>` | 1126 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>などがあの</src><tgt><\|wait\|></tgt>` | 867 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくもらえる</src><tgt><\|wait\|></tgt>` | 1431 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt>We also have things like T- shirts available.</tgt>` | 1555 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ので、ぜひ</src><tgt><\|wait\|></tgt>` | 1578 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt>So please feel free to join us.</tgt>` | 1387 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1394 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になりますので、</src><tgt>That's all for the contact information.</tgt>` | 1495 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt>Um,</tgt>` | 1610 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>この</src><tgt><\|wait\|></tgt>` | 848 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ランチの案内がありますので</src><tgt>there's a lunch announcement here,</tgt>` | 2143 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>この商品も</src><tgt><\|wait\|></tgt>` | 1622 |

---

### Test Example 18 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right, </src><tgt>好的，</tgt>` | 1183 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>and then </src><tgt>然后</tgt>` | 824 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | 1515 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1210 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 495 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1544 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1813 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1081 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1378 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So </src><tgt>要使用这些值。所以</tgt>` | 1700 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1953 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | 1025 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1443 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a high school girl</tgt>` | 1804 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相怪的人</src><tgt><\|wait\|></tgt>` | 839 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1077 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>and there's some kind of connection with someone who looks strange,</tgt>` | 2038 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>could it be</tgt>` | 1654 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里开始的？</src><tgt>that started that night?</tgt>` | 1759 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1114 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2052 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt>Yangzi's thoughts</tgt>` | 1390 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>连篇。</src><tgt>were filled with them.</tgt>` | 1242 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt>제 이름은</tgt>` | 1079 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Kerenath Duru. </src><tgt>케레나스 두루입니다.</tgt>` | 1842 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently </src><tgt>현재</tgt>` | 583 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1255 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | 1619 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Bachelor of Psychology </src><tgt>경영학 학사 과정과</tgt>` | 1474 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at the ANU, </src><tgt>ANU에서 심리학 학사 과정을</tgt>` | 1666 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1485 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>이수하고 있습니다. 앞으로</tgt>` | 2299 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy </src><tgt><\|wait\|></tgt>` | 1448 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>and. </src><tgt>기업 컨설팅 분야로 가고 싶습니다.</tgt>` | 1571 |

---

### Test Example 21 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个就是</src><tgt>次は</tgt>` | 921 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 971 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>选择啊，</src><tgt>選択肢です。</tgt>` | 1345 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>配福</src><tgt>福を呼び込む</tgt>` | 1185 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一级一线</src><tgt>第一段階の</tgt>` | 598 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>トップランナーたちです。</tgt>` | 1617 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，</src><tgt>例えば、</tgt>` | 1584 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1135 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>在做维向攻总好事几点，</src><tgt>「維向攻」の</tgt>` | 1989 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现给维向</src><tgt>「維向」に</tgt>` | 1362 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>好拼分的</src><tgt>良い配分を</tgt>` | 1978 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新棒反而</src><tgt>与えると、</tgt>` | 1596 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>活了。</src><tgt>逆に活路が見つかることがあります。</tgt>` | 1585 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 832 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1026 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1248 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로 돌아가서</tgt>` | 1536 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够哈</src><tgt><\|wait\|></tgt>` | 1639 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>在他下班的时候，</src><tgt>그가 퇴근할 때</tgt>` | 2139 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1499 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국이나 밥을 해주고 싶어요. 정말</tgt>` | 2181 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1197 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时悲痛的时候，就这么一个</src><tgt>그때는</tgt>` | 1862 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>小小的小愿望</src><tgt>그 작은 소망 하나가</tgt>` | 1711 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt>있었어요.</tgt>` | 1077 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 995 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>Like a stretched rubber band, </src><tgt>늘어난 고무줄처럼</tgt>` | 1841 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt>화학 결합은</tgt>` | 800 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy, </src><tgt>에너지를 저장합니다.</tgt>` | 1109 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>and when those bonds are broken, </src><tgt>그리고 그 결합이 끊어지면</tgt>` | 1889 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 잠재 에너지가</tgt>` | 1891 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1300 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>다른 형태의 에너지로</tgt>` | 1677 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt>전환됩니다. 예를 들어 열이나 빛 같은 거죠.</tgt>` | 1374 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1986 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>or gets used to make </src><tgt>아니면</tgt>` | 1684 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 1554 |

---

### Test Example 24 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 너무 </src><tgt>これ、</tgt>` | 1056 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1122 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>저열한 일일 수 있지만 </src><tgt>ちょっと地味なことかもしれませんけど、</tgt>` | 1573 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1084 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>진짜 보살 도요. 아니 </src><tgt>本当に菩薩ですよ。いや、</tgt>` | 1899 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに、飾る必要が</tgt>` | 2512 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>뭐 있고 </src><tgt>あるんです。で、</tgt>` | 1432 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>南韓で菩薩に見える必要が</tgt>` | 2147 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>뭐 있어요. 우주 가 </src><tgt>あるんです。宇宙が</tgt>` | 2287 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | 1698 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>보살 이라는데. </src><tgt>菩薩だと言っているんです。</tgt>` | 1457 |

---

### Test Example 25 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Vanadium and these things are</tgt>` | 2016 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt>almost like insulin</tgt>` | 1147 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 607 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1651 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1185 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt>in terms of action— they are very, very similar.</tgt>` | 2053 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1133 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 2110 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt>That's why we call them diabetes minerals.</tgt>` | 1601 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>And then,</tgt>` | 1374 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아연. </src><tgt>zinc...</tgt>` | 657 |

---

### Test Example 26 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1054 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was fine back then.</tgt>` | 1327 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>活蹦乱跳，</src><tgt>I was full of energy,</tgt>` | 1152 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1248 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>所以坚持不开刀。</src><tgt>so I insisted on not having the surgery.</tgt>` | 1708 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1476 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>提前大概有一周医生来</src><tgt>The doctor</tgt>` | 1492 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>诊断，</src><tgt>came to diagnose me about a week early,</tgt>` | 1710 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1372 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>已塌vartheta，</src><tgt>with the ' leg kick '—</tgt>` | 2135 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>there were no problems at all.</tgt>` | 1450 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>They were all</tgt>` | 1296 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>愉快的一会。</src><tgt>in a good mood.</tgt>` | 867 |

---

### Test Example 27 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これがギア</src><tgt>이게</tgt>` | 1159 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>です。ギアが</src><tgt>기어입니다.</tgt>` | 1380 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>緩むと芯が</src><tgt>기어가 풀리면 심이</tgt>` | 1515 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまう</src><tgt>위아래로</tgt>` | 1636 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt>움직일 수 없게 되니까,</tgt>` | 1495 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 앞쪽에</tgt>` | 1442 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1431 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>역나사 너트가</tgt>` | 1746 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうこと</src><tgt>달려 있다는</tgt>` | 2070 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>거죠.</tgt>` | 1142 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1291 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイブンブレーキを。</src><tgt>하이 브레이크를...</tgt>` | 1204 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or, or if you </src><tgt>あるいは、</tgt>` | 1176 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1086 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何かを文書で作成しなければならない場合、</tgt>` | 1308 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを書く、</tgt>` | 1262 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1624 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1335 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. Like, oh, </src><tgt>言葉の綴りさえわからないことに気づくかもしれません。「ああ、</tgt>` | 2315 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>is this word </src><tgt>この単語は</tgt>` | 1091 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 2021 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1398 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't </src><tgt>ダブルP？ダブルL？</tgt>` | 1751 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src>know. </src><tgt>わからない。</tgt>` | 432 |

---

### Test Example 29 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 901 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>映画でですね、</src><tgt>In the movie,</tgt>` | 1102 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1247 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1523 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>調べるときに、</src><tgt>when you're checking whether the movie is actually living there in various scenes,</tgt>` | 2016 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 1871 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことで、あの</src><tgt>by looking at the movie's eggs,</tgt>` | 1858 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1700 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | 1062 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | 1690 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 1532 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt>they use it to confirm whether it's living there— to guarantee that it is living there.</tgt>` | 1788 |

---

### Test Example 30 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1226 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1028 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment, </src><tgt>제19차 수정헌법의 의미는</tgt>` | 1763 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>그리고</tgt>` | 949 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다.</tgt>` | 1654 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt>이것이</tgt>` | 1375 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1421 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt>정치적 변화가</tgt>` | 1443 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침서입니다.</tgt>` | 2129 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2077 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1497 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, are </src><tgt>물론 수정헌법의 의미는</tgt>` | 1751 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>myriad. </src><tgt>매우 다양합니다.</tgt>` | 1182 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>达到了一个甜头，那</src><tgt>良い兆しが訪れました。</tgt>` | 1764 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt>もし</tgt>` | 497 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了甜头之后，</src><tgt>その兆しを得た後、</tgt>` | 1415 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必就要</src><tgt>必ず</tgt>` | 1574 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1381 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>先守住，</src><tgt>守り抜いてください。</tgt>` | 1572 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，那我再</src><tgt>「ああ、</tgt>` | 1599 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1451 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>继续操作下去哦。</src><tgt>まだ操作を続けよう」なんて考えないでください。</tgt>` | 2238 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1378 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1470 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 771 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>因为呢。</src><tgt>なぜなら……</tgt>` | 1353 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1165 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>要提醒大家，</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1601 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马</src><tgt>このローマの</tgt>` | 753 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>呢，不是一天造成的，</src><tgt>問題は一日にしてできたものではないということです。</tgt>` | 1530 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>所以呢，</src><tgt>ですから、</tgt>` | 1495 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt>今</tgt>` | 1329 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所面临的一些</src><tgt>直面している</tgt>` | 1412 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊，跟风险</src><tgt>危機やリスクは、</tgt>` | 1463 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 1652 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>一夕之间就</src><tgt>一晩で</tgt>` | 1277 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1451 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的，</src><tgt>生じたものではありません。</tgt>` | 1820 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>因此会建议</src><tgt>ですから、</tgt>` | 1275 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの方には、</tgt>` | 1492 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new. </src><tgt>没什么新鲜事。</tgt>` | 1089 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There were </src><tgt><\|wait\|></tgt>` | 1067 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such intoxicists before, </src><tgt>以前也有过这种人，</tgt>` | 1526 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1497 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>net future TC, </src><tgt>比如未来的TC，</tgt>` | 914 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>and so I </src><tgt>所以我</tgt>` | 1212 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1203 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>said just one another place </src><tgt>只是说</tgt>` | 1368 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>ruche, </src><tgt>另一个地方，</tgt>` | 1471 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2101 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but the devil </src><tgt>但</tgt>` | 1017 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>presider and minister of </src><tgt>魔鬼的执政官和</tgt>` | 1801 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>weapons would be </src><tgt>军务大臣</tgt>` | 850 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt>应该知道这件事。</tgt>` | 1416 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>这一张的部分呢，</src><tgt>이 부분은</tgt>` | 1159 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 979 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1047 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>在钓鱼的人，但是</src><tgt>낚시를 하는 사람을 보고 있는데요,</tgt>` | 1550 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>它是属于逆向的</src><tgt>이건 역방향으로</tgt>` | 1720 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src>。所以</src><tgt>작동합니다.</tgt>` | 1777 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>通常逢到这样一个状况的</src><tgt>보통 이런 상황이</tgt>` | 1316 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>时候，就要去</src><tgt>생길 때는</tgt>` | 1362 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意，</src><tgt>특히 주의해야 합니다.</tgt>` | 1538 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是它能不能够</src><tgt>그게</tgt>` | 2045 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>钓到鱼，</src><tgt>물고기를</tgt>` | 1204 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>它钓不到</src><tgt><\|wait\|></tgt>` | 1336 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1086 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>鱼的意识哦。</src><tgt>낚을 수 있는지 없는지 말이죠.</tgt>` | 1546 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>嗯，</tgt>` | 804 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | 836 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1469 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1213 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 580 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1615 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1810 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1441 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | 1247 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1444 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 2051 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>我们得按照HTML这个计算机语言的语法来写代码，</tgt>` | 1713 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | 1543 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | 470 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要一个写代码的程序。</tgt>` | 1415 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 868 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150만 개가 종업원 수 </src><tgt>従業員数の150万人が</tgt>` | 2056 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>10명 미만 으로 </src><tgt>10人未満に</tgt>` | 1198 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな企業が</tgt>` | 705 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 1497 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | 1453 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt>中小企業は成長するか、</tgt>` | 1799 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>혹은 폐업 할 길을 </src><tgt>あるいは廃業する道</tgt>` | 2000 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>걷게 되는데 </src><tgt>を歩むことになりますが、</tgt>` | 1072 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | 2247 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>성장 도 </src><tgt>成長も</tgt>` | 1583 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>폐업 도 하지 않는 </src><tgt>廃業もしない</tgt>` | 1529 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 들만 보이 게 된 거죠. </src><tgt>という現象だけが見られるようになりました。</tgt>` | 1674 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1413 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 983 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1063 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and I have ten of them that are </src><tgt>始めたばかりの人には、</tgt>` | 1570 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>really important </src><tgt><\|wait\|></tgt>` | 726 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1527 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually. </src><tgt>本当に大事なこと10個あります。</tgt>` | 1697 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1491 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 959 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>I have about one minute videos </src><tgt><\|wait\|></tgt>` | 2038 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>about this video. </src><tgt>この動画について、1分程度の動画をいくつか紹介します。</tgt>` | 1913 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>They cover each one, </src><tgt>それぞれについて</tgt>` | 1491 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1274 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>and a little more detail, </src><tgt>詳しく解説します。</tgt>` | 840 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1159 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十連字とか</src><tgt><\|wait\|></tgt>` | 1267 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですね。おそらく</src><tgt>应该是十连字之类的吧。</tgt>` | 1115 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>十秒で。</src><tgt>大概十秒内。</tgt>` | 1336 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt>嗯，</tgt>` | 1567 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1380 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1417 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1434 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>成長ですからね。</src><tgt>就是今天左右的成长嘛。</tgt>` | 1730 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1207 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt>大概</tgt>` | 1275 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1536 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>十一連字</src><tgt>十一连字</tgt>` | 1491 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>ねあの</src><tgt><\|wait\|></tgt>` | 490 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt>啊，宫马之类的</tgt>` | 1415 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>あるから。</src><tgt>也有。</tgt>` | 875 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>金運についてですが、</tgt>` | 1480 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | 1073 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt>とても良いと言えます。ただ、</tgt>` | 1151 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>偏健康正财的部分</src><tgt>健康や正当な収入に関する部分は</tgt>` | 1243 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1513 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>又都在事业方面的</src><tgt>仕事面では</tgt>` | 1541 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩成长所带来的红利</src><tgt>業績アップの恩恵も</tgt>` | 1638 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>与收入的</src><tgt>収入の</tgt>` | 1271 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>提升。如果是在</src><tgt>向上につながります。</tgt>` | 1582 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>投资理财方面呢，</src><tgt>投資や資産運用に関しては、</tgt>` | 2181 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 1307 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>悪くありません。ただ、</tgt>` | 1472 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>相对正财来说就</src><tgt>正当な収入に比べると</tgt>` | 910 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>稍微弱了</src><tgt><\|wait\|></tgt>` | 1357 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt>少し弱めかもしれません。</tgt>` | 890 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 984 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니와 너희 가 </src><tgt>知っているだろうが、</tgt>` | 1807 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt>異邦人として</tgt>` | 832 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>いる間に、</tgt>` | 1104 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>話せない</tgt>` | 1635 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>우상에게로 </src><tgt>偶像に</tgt>` | 1897 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>끄는 그대로 </src><tgt>引きずり込むのと同じように、</tgt>` | 1551 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 </src><tgt><\|wait\|></tgt>` | 1128 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt>引きずられていったのだ。</tgt>` | 1660 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>だから、私は</tgt>` | 2016 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちに</tgt>` | 1505 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>告げます。</tgt>` | 1332 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | 776 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는. </src><tgt>語る者は……</tgt>` | 1435 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 943 |

---

### Test Example 41 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어가 면 </src><tgt>一旦进入，</tgt>` | 1177 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>就会完全迷失方向。</tgt>` | 1506 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 932 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1360 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>하건 걸어 걸어다니 고는. </src><tgt>开车还是走路，</tgt>` | 1558 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt>到了江北</tgt>` | 1052 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt>更是难说，</tgt>` | 1519 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt>出国的话</tgt>` | 1249 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장렬이에요. </src><tgt>简直是灾难。</tgt>` | 1213 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 창피 하네요. </src><tgt>真有点尴尬。</tgt>` | 2092 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 이제 </src><tgt>不如</tgt>` | 1417 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1263 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>물어볼. </src><tgt>努力去问吧。</tgt>` | 835 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>그거 는 다인 것 같아요. </src><tgt>我觉得那应该没问题。</tgt>` | 1515 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 902 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1191 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt>학력 수준. 얼마나</tgt>` | 1607 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you </src><tgt><\|wait\|></tgt>` | 745 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt>실제로</tgt>` | 1293 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? Did you </src><tgt>학업을 마쳤나요?</tgt>` | 1658 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>고등학교를 졸업했나요?</tgt>` | 1474 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt>그게</tgt>` | 1522 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. Did you go </src><tgt>한 단계의 학력 수준입니다.</tgt>` | 1880 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>to college, </src><tgt>대학에 다녔나요?</tgt>` | 1342 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>and if so, did you graduate? </src><tgt>그리고 졸업했나요?</tgt>` | 2126 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of </src><tgt>그게 또 다른</tgt>` | 1570 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt>학력 수준입니다.</tgt>` | 1413 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>자, 이제</tgt>` | 613 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>여기까지입니다.</tgt>` | 1459 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 950 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 간 코 </src><tgt>目、鼻、</tgt>` | 1272 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>생활 발 </src><tgt>生活、</tgt>` | 887 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야 </src><tgt>生活を</tgt>` | 1330 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1169 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>연세 서름이 돋은 자차 리 </src><tgt>送るんです。年配の車が</tgt>` | 1478 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>돋은 느끼 면 </src><tgt>出てきたら、</tgt>` | 713 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 흔들 어서 </src><tgt>それを振って</tgt>` | 1983 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうってことですよ。</tgt>` | 1987 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>기신이 너무 </src><tgt>気性が</tgt>` | 1667 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>부릴 거고 </src><tgt>あまりに激しいし、</tgt>` | 1046 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>시니오미야 너 </src><tgt>シニッシュも激しい。</tgt>` | 2067 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1574 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>지켜 주라고 찔러 줄 거니 까 </src><tgt>だから守ってあげなきゃいけないんだ。だから</tgt>` | 1545 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>リラックスして</tgt>` | 1358 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 간다. </src><tgt>楽しんでください。</tgt>` | 918 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt>그럼</tgt>` | 1080 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう眠らせてやれ。</src><tgt>그냥 재워버려.</tgt>` | 1329 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt>난</tgt>` | 1038 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今激烈</src><tgt>지금</tgt>` | 1152 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>を見ている。</src><tgt>격렬한 걸 보고 있어.</tgt>` | 667 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1383 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>더 이상</tgt>` | 1646 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>遠い越えている</src><tgt>한계는</tgt>` | 1245 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>船の犠牲群。</src><tgt>이미 넘어섰어. 배의 희생자들.</tgt>` | 2345 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 986 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src></src><tgt><\|wait\|></tgt>` | 1996 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>流れ込む大宮を</src><tgt>흐르는 오미야를</tgt>` | 1787 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってるが、</src><tgt>다루고 있지만,</tgt>` | 1590 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt>난</tgt>` | 418 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선을</tgt>` | 1445 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>본 적이 없어.</tgt>` | 813 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계속 뭐 </src><tgt>ずっと</tgt>` | 1091 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>물론 이제 </src><tgt>もちろん、</tgt>` | 831 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt>こういうケースはあります。</tgt>` | 1541 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>Aさん</tgt>` | 1416 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>とBさんが</tgt>` | 1162 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨턴트예요 </src><tgt>お互いにコンテントです。</tgt>` | 874 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨설턴트가 </src><tgt>コンサルタントが</tgt>` | 2041 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>어 가지고 </src><tgt><\|wait\|></tgt>` | 1106 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>いて、Aさんが</tgt>` | 1566 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪性コードを</tgt>` | 1252 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>与えた場合、</tgt>` | 2226 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비란 사람 이 </src><tgt>被害者が</tgt>` | 1626 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt>実際に</tgt>` | 1388 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로스사이트 스킷에서 </src><tgt>クロスサイトスクリプトで</tgt>` | 619 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>예기스파일까지 </src><tgt>iexplore.exeまで</tgt>` | 1270 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>感染する可能性がある。</tgt>` | 925 |

---

### Test Example 46 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1217 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어 짧게 보면 </src><tgt>嗯，从短时间来看，</tgt>` | 1545 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 987 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1241 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | 1657 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1353 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | 1555 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1288 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1659 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | 1287 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1431 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스루. </src><tgt><\|wait\|></tgt>` | 1662 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1436 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>막 </src><tgt><\|wait\|></tgt>` | 1193 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 다 </src><tgt><\|wait\|></tgt>` | 713 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>내놓 고 행복 했으면 좋겠다 </src><tgt><\|wait\|></tgt>` | 853 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1115 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手</src><tgt>相手の</tgt>` | 1136 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>的感情或</src><tgt>感情や</tgt>` | 1144 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>真实意图的，</src><tgt>真意を察知したり感じ取ったりすること、</tgt>` | 1551 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1606 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くは</tgt>` | 1341 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>后经场会</src><tgt>後で</tgt>` | 1431 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>提到人们这样</src><tgt>「</tgt>` | 1425 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>说：“</src><tgt><\|wait\|></tgt>` | 1660 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>見て、</tgt>` | 1117 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 1436 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | 1786 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>その目は</tgt>` | 1450 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。”</src><tgt>すべてを物語っている。</tgt>` | 1176 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 718 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说。</src><tgt>つまり、</tgt>` | 726 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 649 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>So, this is</tgt>` | 1364 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1188 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というだけじゃなくて</src><tgt>not just about the visual development environment.</tgt>` | 1122 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1231 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>It's a visual Python development environment.</tgt>` | 1913 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt>That's because</tgt>` | 1936 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt>after you write a flowchart visually,</tgt>` | 1933 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt>it automatically</tgt>` | 1743 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>がそれから</src><tgt>generates the Python code</tgt>` | 1623 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>and then</tgt>` | 1127 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt>executes it,</tgt>` | 1688 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1394 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているからです。</src><tgt>and signal processing takes place.</tgt>` | 1501 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 929 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt>Yes.</tgt>` | 324 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ。</src><tgt>So,</tgt>` | 479 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | 897 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人が</tgt>` | 1369 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>내놓 았습니다. </src><tgt>分析を提出しました。</tgt>` | 1052 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 로쿠자 의 </src><tgt>ここで</tgt>` | 1253 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>분석 을 보시면 </src><tgt>ロクジャの分析を見ると、</tgt>` | 1721 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니가 </src><tgt>ソニーが</tgt>` | 1535 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | 1423 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | 1813 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트로 </src><tgt>128ビットに</tgt>` | 1464 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>낮춘 것을 보여 줍니다. </src><tgt>下げたことがわかります。</tgt>` | 2332 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1636 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>Xbox Series X에서도 없는 </src><tgt>XboxSeriesXにはない</tgt>` | 1499 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1444 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュ</tgt>` | 793 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L3가 여기 도 없다. </src><tgt>L3もありません。</tgt>` | 538 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 480 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1133 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1269 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1115 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, </src><tgt>自分なりの基準を自分で決めること。</tgt>` | 1477 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct. </src><tgt>その通りです。</tgt>` | 1617 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1782 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is, </src><tgt>でも現実には、</tgt>` | 1371 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>is that because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 2116 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block and because the </src><tgt>私たちが新しい世代だからです。そして、</tgt>` | 1035 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>standards have </src><tgt>基準が</tgt>` | 1940 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1578 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>20年前に変わったので、</tgt>` | 1733 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1232 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>より高い基準を求められています。</tgt>` | 857 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point is being </src><tgt>なぜなら、今の</tgt>` | 756 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>held to a higher standard. </src><tgt>あらゆるものがより高い基準で評価されているからです。</tgt>` | 750 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1342 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 872 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index is rising,</tgt>` | 1467 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1114 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | 1625 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will also rise sharply,</tgt>` | 2091 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1181 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1295 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt><\|wait\|></tgt>` | 1702 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 2098 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1563 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 항상 </src><tgt>but since these lighter stocks move the market first,</tgt>` | 1781 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | 1353 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 778 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 593 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>you should always keep an eye on the market cap of these lighter stocks.</tgt>` | 829 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1128 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 883 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>you will not be able to </src><tgt>你将无法</tgt>` | 1366 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1404 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 960 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | 975 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>So, if </src><tgt>所以，如果</tgt>` | 1840 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 1273 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt>你遇到</tgt>` | 1167 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize </src><tgt>发现</tgt>` | 1472 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt>添加了错误的媒体</tgt>` | 2199 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>文件到某个资源中，</tgt>` | 1489 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>you need to let us know, </src><tgt>你需要告诉我们，</tgt>` | 1610 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt>我们就能</tgt>` | 611 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1351 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure they </src><tgt>移动这些媒体文件，并确保它们</tgt>` | 1092 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 641 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>得到正确备份。</tgt>` | 628 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 929 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>为了以的首知觉</src><tgt>초기 지각을</tgt>` | 1609 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>得到那个现象，</src><tgt>얻기 위해</tgt>` | 832 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1297 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>每当我们处于</src><tgt><\|wait\|></tgt>` | 1607 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1374 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>爱之中熟悉的爱，</src><tgt>우리가 익숙한 사랑 속에 있을 때,</tgt>` | 1797 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1338 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>我们也同时进入</src><tgt>우리는 동시에</tgt>` | 1497 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1655 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>恨在早上的时候，</src><tgt>분노도</tgt>` | 1080 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>它在爱。</src><tgt>사랑을 경험합니다.</tgt>` | 1714 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | 1280 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 1246 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 716 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>恨那个钟摆，</src><tgt>분노는 시계추처럼</tgt>` | 815 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 488 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>一动一动。</src><tgt>계속 흔들립니다.</tgt>` | 668 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1546 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1083 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section about </src><tgt>最初のセクションで、少し間違ったところを</tgt>` | 1575 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 869 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>the EHR field </src><tgt><\|wait\|></tgt>` | 1497 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 741 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1546 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus the </src><tgt><\|wait\|></tgt>` | 1179 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1257 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 1476 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously the one of my loves. </src><tgt>間違えていました。EHRの重要性について、変異データベースと比べて。変異データベースは、もちろん私が一番好きなものです。</tgt>` | 3169 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>つまり、</tgt>` | 1315 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1251 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1448 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 823 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>データソースに含めるべきフィールドについて合意できなければ、</tgt>` | 740 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from, </src><tgt>そこから引き出せる</tgt>` | 489 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>データは何もありませんよね？</tgt>` | 662 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 323 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時、</tgt>` | 1213 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>彼はイエスを</tgt>` | 978 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is hungry. </src><tgt>飢えと知ります。</tgt>` | 1079 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1321 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's been without food, </src><tgt>彼は、</tgt>` | 1623 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1394 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>40日間荒野に留まり、飢えを経験してきたことを知っています。</tgt>` | 2837 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>And so he says </src><tgt>だから彼は</tgt>` | 1686 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>to Jesus," Hey, if you're Jesus, </src><tgt>イエスに言いました。「イエスよ、</tgt>` | 1913 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, prove it." </src><tgt>もし神の御子なら、証明してみろ」と。</tgt>` | 1837 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn these </src><tgt><\|wait\|></tgt>` | 1238 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>stones to bread." </src><tgt>この石をパンに変えろ」と。</tgt>` | 1101 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt>彼はどうやって</tgt>` | 1360 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>just deal with that? </src><tgt>それに対処したのでしょうか？</tgt>` | 984 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>The temptation. </src><tgt>誘惑について。</tgt>` | 650 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt>いや、</tgt>` | 421 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Jonathan lead by </src><tgt>ジョナタンは</tgt>` | 463 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>brother alone. </src><tgt>兄を一人で導きました。</tgt>` | 454 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1431 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 1092 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | 1137 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>最高法院</tgt>` | 1362 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1340 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>最后才跟上。我</tgt>` | 1147 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>And I don't think the courts want to be </src><tgt>不认为法院想</tgt>` | 1926 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1433 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | 1698 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>change </src><tgt>成为社会变革的先锋。</tgt>` | 1035 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>these days </src><tgt>如今，</tgt>` | 1579 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1588 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>but they rather reflect </src><tgt>它们更多地反映了</tgt>` | 1615 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1170 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 786 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>已经形成的共识。</tgt>` | 705 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 633 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>So you have some </src><tgt>所以，</tgt>` | 629 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>federal judges </src><tgt>你有一些联邦法官</tgt>` | 470 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 376 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>……</tgt>` | 354 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>그럼</tgt>` | 1066 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그림을 한번 살펴볼게요.</tgt>` | 1653 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 788 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt>그 부분에서는</tgt>` | 1348 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | 1661 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>的部分，</src><tgt>거실 쪽이 보이고,</tgt>` | 1972 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1140 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>它客厅一般都是</src><tgt>거실은 보통</tgt>` | 1441 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>属于我们</src><tgt><\|wait\|></tgt>` | 1382 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1542 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在休息的地方，所以</src><tgt>우리가 쉬는 공간이라서</tgt>` | 1535 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>呢，是身体的</src><tgt>몸의</tgt>` | 1506 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>部分会反映的是</src><tgt>부분이</tgt>` | 1180 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1262 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>一点时间，可以</src><tgt>조금 시간을</tgt>` | 721 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>好好的</src><tgt><\|wait\|></tgt>` | 621 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>坐下来休息。可是</src><tgt>내려놓고 편안하게 쉬어야 한다는 걸 반영해요. 하지만</tgt>` | 968 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>我们可以看到这边是</src><tgt>여기</tgt>` | 477 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>空无一人的嘛，</src><tgt>사람이 없네요.</tgt>` | 478 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt>아,</tgt>` | 242 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>그러니까...</tgt>` | 345 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>彼らは</tgt>` | 911 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>非常に稀で、</tgt>` | 1135 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>よく</tgt>` | 1134 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1439 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world. </src><tgt>世界を完全に変革するような存在です。</tgt>` | 1465 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1024 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | 1414 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾していると言えるでしょう。</tgt>` | 1734 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 980 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 2018 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的ですが、</tgt>` | 1774 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate </src><tgt><\|wait\|></tgt>` | 1402 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations, </src><tgt>無意味な会話や</tgt>` | 554 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1292 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like it gets straight to the </src><tgt>つまらない話が大嫌いです。そして、</tgt>` | 1125 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>point. </src><tgt>要点をズバッと突きます。</tgt>` | 663 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love to </src><tgt>彼らは</tgt>` | 508 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>play </src><tgt><\|wait\|></tgt>` | 438 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, </src><tgt>悪魔の肩を貸すことも好きで、</tgt>` | 533 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and they're never shy </src><tgt><\|wait\|></tgt>` | 307 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>of a debate. </src><tgt>議論を避けることは決してありません。</tgt>` | 358 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 325 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>INTP stands for </src><tgt>INTPは</tgt>` | 359 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>student for. </src><tgt>「Studentfor」の略です。</tgt>` | 374 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1574 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1421 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1171 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 712 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1584 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1922 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1458 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>put on a show, claiming he was rejecting the party's work ethics for the sake of the candidate and the party's victory. But now</tgt>` | 2786 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2245 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1629 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Jong- in,</tgt>` | 1664 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석은 </src><tgt>Lee Jun- seok</tgt>` | 1487 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>드러내 놓고 윤석열 </src><tgt>exposed him</tgt>` | 961 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 718 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 664 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 450 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 384 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 383 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>작정 한 것입니다. </src><tgt>with the intent to attack and drive Yoon Suk- yeol out of the race.</tgt>` | 458 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 이준석의 </src><tgt><\|wait\|></tgt>` | 301 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 306 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>성상급건 </src><tgt><\|wait\|></tgt>` | 336 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 264 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>민주당 이 공격 하기에 </src><tgt><\|wait\|></tgt>` | 291 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>How much of a boon is the Democratic Party's attack on Lee Jun- seok's image?</tgt>` | 491 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1081 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後ね</src><tgt><\|wait\|></tgt>` | 1002 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってるみたいな</src><tgt><\|wait\|></tgt>` | 1350 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>です。なので</src><tgt>It's like I'm making it right now after a meal.</tgt>` | 1652 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ここの毛織のホテル</src><tgt><\|wait\|></tgt>` | 1587 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>でも</src><tgt><\|wait\|></tgt>` | 1588 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1317 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1370 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので</src><tgt>So, since this hotel has breakfast,</tgt>` | 1697 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1834 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドーストーンホテル</src><tgt><\|wait\|></tgt>` | 905 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1615 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね</src><tgt>if you're thinking of staying at the Goldstone Hotel in the future,</tgt>` | 1497 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1355 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 963 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt>you might want to consider it. Yeah.</tgt>` | 709 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 511 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここのホテルからですね</src><tgt>From this hotel,</tgt>` | 375 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 404 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 288 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分</src><tgt><\|wait\|></tgt>` | 331 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 355 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 363 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のねまあホテル</src><tgt><\|wait\|></tgt>` | 359 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt>the location is so good that you can walk to Busan Station in about a minute.</tgt>` | 484 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>行ったらですね</src><tgt>So if you go there,</tgt>` | 275 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>you might want to consider it.</tgt>` | 334 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それだけ</src><tgt><\|wait\|></tgt>` | 276 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は。</src><tgt>That's it for this time.</tgt>` | 209 |
