# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9262
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5298
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.7414
  - TGT_RELEASE_TOTAL: 495
  - TGT_WAIT_ACCURACY: 0.7032
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1344.9390
  - PROCESS_TIME_MS_P50: 1366.6270
  - PROCESS_TIME_MS_P95: 2048.4970
  - PROCESS_TIME_MS_MAX: 3076.7590

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>是容易的，</src><tgt>気数を気にするのは簡単です。</tgt>` | 1803 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>但是</src><tgt>でも、</tgt>` | 646 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师傅</src><tgt>師匠が</tgt>` | 1359 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1480 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>知道如何</src><tgt><\|wait\|></tgt>` | 1157 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>处于中间，</src><tgt>どういう状態にあるかを知っているのは一人だけです。</tgt>` | 1567 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>だから</tgt>` | 723 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要凡</src><tgt><\|wait\|></tgt>` | 1808 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 1496 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>一个师傅。</src><tgt>凡人には、師匠にならなければなりません。</tgt>` | 1261 |

---

### Test Example 2 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt>你的身体</tgt>` | 866 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>在做什么？</tgt>` | 1085 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1172 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>your body. </src><tgt>进入你的身体。</tgt>` | 1372 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>紧张感</tgt>` | 1223 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>从哪里开始？是什么？</tgt>` | 1131 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | 1632 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是胸闷吗？</tgt>` | 1005 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>I ask them </src><tgt>我问他们，</tgt>` | 1872 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>what language are you </src><tgt>你</tgt>` | 1651 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>using? </src><tgt>在用什么语言？</tgt>` | 1615 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1058 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家人需要做的是，</src><tgt>What your family needs to do is</tgt>` | 1199 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1264 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>深深的爱浇水，</src><tgt>water it with our deep love,</tgt>` | 1325 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 790 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给她</src><tgt><\|wait\|></tgt>` | 1286 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心灵营养，</src><tgt>give your child spiritual nourishment,</tgt>` | 1550 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1932 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>点耐心等</src><tgt><\|wait\|></tgt>` | 1741 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>and be patient as your child grows up.</tgt>` | 2039 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 818 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1163 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1184 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>1年生ですからね。</src><tgt>一开始，孩子还才一年级呢。</tgt>` | 1650 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>あの時点で</src><tgt>那时候</tgt>` | 1281 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短い間隔</src><tgt><\|wait\|></tgt>` | 1355 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>線条を</src><tgt><\|wait\|></tgt>` | 1659 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こうタイムズして</src><tgt><\|wait\|></tgt>` | 586 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>待てあげると</src><tgt>如果保持短间隔，</tgt>` | 1793 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>1年経っても</src><tgt>一年后</tgt>` | 1686 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>待した。</src><tgt>再等，</tgt>` | 2114 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>砂漠を越えた後、</tgt>` | 1962 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的盐碱</src><tgt>内部の</tgt>` | 573 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了，</src><tgt>塩基性のエネルギーも弱まり、</tgt>` | 1645 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1220 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1426 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1560 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的运行</src><tgt><\|wait\|></tgt>` | 1541 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>状态。</src><tgt>比較的低エネルギーな状態に留まってしまいます。</tgt>` | 1429 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>これが</tgt>` | 1015 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>逆淤状态。</src><tgt>いわゆる逆淤状態です。</tgt>` | 2212 |

---

### Test Example 6 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1264 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>乖的监督者里面，</src><tgt>Among the obedient supervisors,</tgt>` | 1633 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个优秀的人</src><tgt><\|wait\|></tgt>` | 780 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>也很大。然后呢，</src><tgt>the excellent ones are also very great. And then,</tgt>` | 1778 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt><\|wait\|></tgt>` | 1412 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶渊</src><tgt><\|wait\|></tgt>` | 1480 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1769 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>这个儿去。</src><tgt>I'm going to play with Tao Yuan's son.</tgt>` | 1751 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 826 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>这种和陶渊。</src><tgt>This kind of...</tgt>` | 1941 |

---

### Test Example 7 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 984 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 너무 지저 여요. </src><tgt>これ、これ、すごく気持ち悪いです。</tgt>` | 2032 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>할 수 있지만 </src><tgt>できることはあるけど、</tgt>` | 629 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 고사 였죠. </src><tgt>本当に不作法でしたよね。</tgt>` | 1567 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 고사 </src><tgt>いや、</tgt>` | 1354 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>한다는 꿈일 </src><tgt>自分の不作法を</tgt>` | 1567 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>부르 고 있고 </src><tgt>夢にしているんです。</tgt>` | 1410 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>私だけが</tgt>` | 1748 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>고사 를 볼 필요 를 보이 세 우주 가 </src><tgt>不作法を</tgt>` | 1687 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>진짜 부사들이랑 </src><tgt>見る必要はない。宇宙は本当に不作法の人たちと</tgt>` | 1314 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1456 |

---

### Test Example 8 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1081 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 816 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1430 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1031 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We also have things like T- shirts available,</tgt>` | 981 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ぜひご参加ください。</src><tgt>so please join us.</tgt>` | 1397 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt>For contact,</tgt>` | 1321 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になりますので</src><tgt>that's all,</tgt>` | 1562 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1698 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こちら</src><tgt><\|wait\|></tgt>` | 1005 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>の案内がありますので</src><tgt>we have an announcement here,</tgt>` | 1466 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>もう少々お待ちください。</src><tgt>so please wait a moment.</tgt>` | 2197 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right. </src><tgt>好的。</tgt>` | 1140 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>And then, </src><tgt>接下来，</tgt>` | 858 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>这些例子之后，</tgt>` | 1411 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1006 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 680 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1600 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1415 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1472 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1360 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>实际上要用这些值。</tgt>` | 965 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt>所以</tgt>` | 1522 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game dot sort array. </src><tgt>这个game.sort数组。</tgt>` | 1861 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 747 |

---

### Test Example 10 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1002 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复。</tgt>` | 1246 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learn to repeat. </src><tgt>学会重复。</tgt>` | 1025 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>Find what you're good at. </src><tgt>找到你擅长的地方。</tgt>` | 1008 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>And do more of it. </src><tgt>多做一些。</tgt>` | 1413 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And when you're not good </src><tgt>当你</tgt>` | 1616 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1347 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>at it, get to people around you to help you with </src><tgt>不擅长的时候，</tgt>` | 2240 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1665 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>it. And and tell next time </src><tgt>找身边的人帮忙。下次</tgt>` | 2372 |

---

### Test Example 11 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>아 저는 </src><tgt>Ah, I'm</tgt>` | 1143 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1192 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>봉심이 칼 </src><tgt><\|wait\|></tgt>` | 1126 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 1343 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>a person with a sharp mind, a person with a sharp mind.</tgt>` | 1585 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>봉심이가 </src><tgt><\|wait\|></tgt>` | 1319 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞여 있는 건데요. </src><tgt>So it's a mix.</tgt>` | 1908 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>야 </src><tgt>Hey,</tgt>` | 1642 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1166 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>해당 으로 </src><tgt><\|wait\|></tgt>` | 1173 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 주기 만들 잖아요. </src><tgt>you know, it's a bit of a challenge.</tgt>` | 2389 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>通常从这里开始，</tgt>` | 1174 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので、</src><tgt>我们</tgt>` | 1112 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 991 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 789 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1489 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1423 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1646 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1929 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどのという人の絵</src><tgt><\|wait\|></tgt>` | 1759 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1961 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 835 |

---

### Test Example 13 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 1035 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 1205 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>extremely happy people. This is </src><tgt>非常に幸せな人々の研究をしました。</tgt>` | 1589 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1493 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>これは研究の入り口です。</tgt>` | 1697 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1428 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1930 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1639 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, people who </src><tgt>最も幸せな人々の10%を見てみると、</tgt>` | 2109 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt>そこから学ぶことができます。</tgt>` | 934 |

---

### Test Example 14 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 942 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1275 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 을 접불식기 고 </src><tgt><\|wait\|></tgt>` | 1146 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1325 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1472 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>페모르 기 쪽인 </src><tgt><\|wait\|></tgt>` | 1360 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1364 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 768 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1884 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>같은 세대 들입니다. </src><tgt>I'm in the same generation as Park Han- sang, who's in the same generation as my girlfriend, who's in the same generation as my girlfriend.</tgt>` | 3077 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt><\|wait\|></tgt>` | 1386 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주겨 달라 이거 주고 내가 </src><tgt>He asked for another massage, and then he</tgt>` | 1175 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>주기 레볼루아스다. </src><tgt>gave me a Revoluard.</tgt>` | 1671 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜을 </src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 </src><tgt><\|wait\|></tgt>` | 1407 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해지 않았냐. 내가 </src><tgt>Didn't he ask for another massage? I</tgt>` | 1757 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1968 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 줄 알았느냐? </src><tgt>thought I wasn't listening to that?</tgt>` | 2054 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아. </src><tgt>Ah.</tgt>` | 1840 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1183 |

---

### Test Example 16 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 953 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | 1641 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 770 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>when we run into a problem, we should quickly report it to our supervisor.</tgt>` | 2047 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt>Or let them know</tgt>` | 1091 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们有这样的状况，</src><tgt>that we're in this situation,</tgt>` | 2150 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt>and don't</tgt>` | 819 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>try to handle everything yourself.</tgt>` | 2068 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>不理成担。</src><tgt>Don't ignore it or take responsibility for it.</tgt>` | 2028 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>整体而言，</src><tgt>Overall,</tgt>` | 1948 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>事业是</src><tgt><\|wait\|></tgt>` | 1296 |

---

### Test Example 17 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1304 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt>Students in the auspicious positions</tgt>` | 1424 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 879 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt>were not actually highly intelligent.</tgt>` | 1645 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1427 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1649 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1443 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니까? </src><tgt>So what about the students who were selected at random?</tgt>` | 2227 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1605 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | 2186 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>교사 들은 </src><tgt>The teachers who didn't know the truth</tgt>` | 1481 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そう</src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>です。そこで</src><tgt>맞아요. 그래서</tgt>` | 1226 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天国という</src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>設定が</src><tgt>천국 설정이</tgt>` | 1387 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | 1277 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>그리고</tgt>` | 616 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井青氏の仕組み</src><tgt>나가이 아오 씨의</tgt>` | 1464 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt>구조는</tgt>` | 1802 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>僕</src><tgt><\|wait\|></tgt>` | 1613 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>と</src><tgt><\|wait\|></tgt>` | 1086 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設定が</src><tgt>저와 설정이</tgt>` | 1534 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>モブです。</src><tgt>모브입니다.</tgt>` | 1370 |

---

### Test Example 19 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>まあだんだん</src><tgt>嗯，</tgt>` | 1255 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が</src><tgt><\|wait\|></tgt>` | 1258 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离在慢慢拉开，</tgt>` | 1204 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>おしゃれルカだけがね</src><tgt>只有Olga</tgt>` | 1534 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>多いですね。</src><tgt>这么时髦。</tgt>` | 1347 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>想去海边的人</tgt>` | 1588 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい行き来して다가</src><tgt>经常来回</tgt>` | 1607 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>シー</src><tgt><\|wait\|></tgt>` | 1815 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュレで</src><tgt><\|wait\|></tgt>` | 1400 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>もとんスキャンを</src><tgt><\|wait\|></tgt>` | 856 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>取取しゃがけ光が強いので</src><tgt>用这个扫描仪，光线很强，</tgt>` | 2357 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なのでなので</src><tgt>所以</tgt>` | 1659 |

---

### Test Example 20 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt>이것이</tgt>` | 1121 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 964 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアです。ギアが</src><tgt>기어입니다.</tgt>` | 1321 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>緩むと芯が</src><tgt>기어가 헐거워지면</tgt>` | 1280 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>逆ができないく</src><tgt>심이</tgt>` | 767 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>なってしまうので</src><tgt>제대로 안 맞아서</tgt>` | 1310 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | 1572 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>역나사 너트가</tgt>` | 2051 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt>달려 있다는</tgt>` | 1717 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>거죠.</tgt>` | 1867 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 754 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイブンブレーキを。</src><tgt>하이 브레이크를...</tgt>` | 1991 |

---

### Test Example 21 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 946 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If a female high school student</tgt>` | 1663 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 728 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1387 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt>has some kind of connection with someone with a strange appearance,</tgt>` | 1894 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>could it be</tgt>` | 1465 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1299 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天</src><tgt><\|wait\|></tgt>` | 1939 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>夜里开始的？</src><tgt>that started that night?</tgt>` | 1916 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1932 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思绪</src><tgt>Yangzi's thoughts</tgt>` | 1003 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>片：“</src><tgt>drifted on:</tgt>` | 1667 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 744 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1173 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1226 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>的一个轨道哈，让我</src><tgt>제 삶의 궤도로 돌아가게 해 주세요.</tgt>` | 1809 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>能够哈</src><tgt><\|wait\|></tgt>` | 1249 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>在他下班的时候</src><tgt>그가 퇴근할 때</tgt>` | 1697 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热炕</src><tgt><\|wait\|></tgt>` | 1416 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭给他吃，</src><tgt>따뜻한 밥을 먹여주고,</tgt>` | 2213 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就这么</src><tgt><\|wait\|></tgt>` | 1638 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我暂时被他</src><tgt>그렇게</tgt>` | 1935 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>作为妻子的一个小小的愿望哈。</src><tgt>아내로서의 작은 소망을</tgt>` | 1260 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1541 |

---

### Test Example 23 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスにですね、</src><tgt>In the A A Andes,</tgt>` | 1375 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1105 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>円生速度が</src><tgt><\|wait\|></tgt>` | 1451 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>どうかという場合、</src><tgt>when it comes to the circular velocity in various situations,</tgt>` | 1772 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>まあAAの乱交</src><tgt><\|wait\|></tgt>` | 1714 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べということで、あの</src><tgt>we're looking into the A A</tgt>` | 1362 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生生速度が</src><tgt><\|wait\|></tgt>` | 1900 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>等しい生速度である</src><tgt><\|wait\|></tgt>` | 1728 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | 1986 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 792 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされています。</src><tgt>circular velocity, ensuring that the circular velocity is equal to the circular velocity.</tgt>` | 2433 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼</tgt>` | 1423 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt>화학 결합은</tgt>` | 903 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy. And when those </src><tgt>에너지도 저장합니다.</tgt>` | 1687 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | 1609 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 잠재 에너지가</tgt>` | 1868 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 963 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 2046 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light. </src><tgt>열이나 빛 같은 다른 에너지 형태로 변환됩니다.</tgt>` | 2038 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or </src><tgt>또는</tgt>` | 1929 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>gets used to make </src><tgt><\|wait\|></tgt>` | 1183 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 1820 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个就是</src><tgt>次は</tgt>` | 876 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入第二个</src><tgt><\|wait\|></tgt>` | 1005 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>机制场，</src><tgt>第2のメカニズムフィールドです。</tgt>` | 1447 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>并服务</src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一级一线</src><tgt>第1ランクの</tgt>` | 1240 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>トップランナーたちをサポートします。</tgt>` | 1038 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说</src><tgt>例えば、</tgt>` | 988 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1466 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>维向纵送号际期间，你可以</src><tgt>「維向縦送号际」の期間中、</tgt>` | 2328 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>发见给</src><tgt><\|wait\|></tgt>` | 1666 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>维向纵好拼分的</src><tgt>維向縦好拼分を</tgt>` | 2397 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新绑</src><tgt><\|wait\|></tgt>` | 1421 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>反之啊。</src><tgt>受け取れます。</tgt>` | 1461 |

---

### Test Example 26 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt>제 이름은</tgt>` | 1001 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Kiran Patel, </src><tgt>키란 파텔입니다.</tgt>` | 1625 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt>현재</tgt>` | 771 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1424 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>a BA in Business Finance </src><tgt><\|wait\|></tgt>` | 1528 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a BSc in Psychology. </src><tgt>경영재학 학사 과정과 심리학 학사 과정을</tgt>` | 2579 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 782 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yale, </src><tgt>Yale에서</tgt>` | 1873 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1718 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>and in the future, I want to go into </src><tgt>공부하고 있습니다. 앞으로</tgt>` | 2326 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1333 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 가고 싶습니다.</tgt>` | 1753 |

---

### Test Example 27 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 932 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1959 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 609 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 유사 한 </src><tgt><\|wait\|></tgt>` | 1403 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>작용 이 </src><tgt><\|wait\|></tgt>` | 1433 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1480 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1529 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1965 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>기계 가 </src><tgt><\|wait\|></tgt>` | 1574 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>잘 작동 해 </src><tgt><\|wait\|></tgt>` | 871 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1961 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1510 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1511 |

---

### Test Example 28 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt>皆さん、</tgt>` | 1001 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1133 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>このローマでは、</tgt>` | 1299 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1334 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>造成了所以呢，</src><tgt>そうやって</tgt>` | 1261 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt>今、</tgt>` | 708 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所面临的一些</src><tgt>皆さんが直面している</tgt>` | 1792 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>遗迹啊</src><tgt>遺跡や</tgt>` | 1105 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>跟风景，</src><tgt>風景は、</tgt>` | 1911 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也不可能是你之前</src><tgt>以前とは</tgt>` | 1526 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt>違う</tgt>` | 789 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1945 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>的因此会建议</src><tgt>ので、</tgt>` | 1453 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>属鸡的朋友呢，</src><tgt>酉年生まれの方には、</tgt>` | 1682 |

---

### Test Example 29 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>我当时一切正常，</src><tgt>Everything was fine with me at the time.</tgt>` | 2005 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>活蹦乱跳，</src><tgt>I was full of energy,</tgt>` | 813 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1085 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>所以坚持不开刀。</src><tgt>so I insisted on not having the surgery.</tgt>` | 1689 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1456 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>期间大概有十位医生来</src><tgt>About ten doctors</tgt>` | 1568 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>审断，</src><tgt>came to examine me,</tgt>` | 1918 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿、</src><tgt><\|wait\|></tgt>` | 1746 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>and they would kick and lift my legs</tgt>` | 2020 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>without any problems.</tgt>` | 757 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1881 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>他们都很疑惑的来。</src><tgt>They all came with such confusion.</tgt>` | 1305 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>达到了一个</src><tgt><\|wait\|></tgt>` | 822 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>天顶，</src><tgt>天頂に達した</tgt>` | 1503 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt>なら、</tgt>` | 880 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了天顶之后，</src><tgt>天頂に達した後は、</tgt>` | 1623 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你务必</src><tgt>必ず</tgt>` | 1337 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>坐腰前</src><tgt>腰を</tgt>` | 1302 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>耸住，</src><tgt>前に突き上げて、</tgt>` | 1693 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说哎，</src><tgt>「あ、</tgt>` | 1591 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再继续操作</src><tgt>また</tgt>` | 959 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>操作を続けよう」なんて思わないでください。</tgt>` | 1736 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1963 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそう言うのか？</tgt>` | 1424 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt>それは、</tgt>` | 1636 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 610 |

---

### Test Example 31 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 853 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150만 개가 종업원 수 </src><tgt>従業員数は150万人に</tgt>` | 2138 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>10명 미만 으로 </src><tgt>の10人未満に</tgt>` | 1302 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들이 </src><tgt>あたる非常に小さな企業が</tgt>` | 1146 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>多くありました。</tgt>` | 858 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | 1533 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt>中小企業は成長したり、</tgt>` | 1684 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>혹은 폐업 할 경우 </src><tgt>あるいは廃業したりする</tgt>` | 1989 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>없어 되는데 </src><tgt>こともありますが、</tgt>` | 1721 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | 2247 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>성장 도 </src><tgt>成長も</tgt>` | 1263 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>폐업 도 하지 않을 현상 들을 </src><tgt>廃業もしないという現象を</tgt>` | 1906 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>보이 게 된 거죠. </src><tgt>見せています。</tgt>` | 556 |

---

### Test Example 32 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of" </src><tgt><\|wait\|></tgt>` | 1286 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>of the 19th </src><tgt><\|wait\|></tgt>` | 1559 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>Amendment," </src><tgt>제19조 개정안의 의미는</tgt>` | 900 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>그리고</tgt>` | 1292 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이 역사는</tgt>` | 1859 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 1529 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1317 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt>정치적 변화가</tgt>` | 1952 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침서입니다.</tgt>` | 2217 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1994 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1313 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, </src><tgt>물론</tgt>` | 1657 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>I may read. </src><tgt>제가 읽는 내용이기도 합니다.</tgt>` | 689 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or, or if you </src><tgt>あるいは、</tgt>` | 1101 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1310 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何かを文書化しなければならない場合、</tgt>` | 1074 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを作成する、</tgt>` | 1502 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1429 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1469 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1535 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>how to spell the words. Like, oh, </src><tgt>単語のスペルさえわからないことに気づく。例えば、「ああ、</tgt>` | 2962 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>is this word </src><tgt>この単語は</tgt>` | 1174 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 2101 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1368 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double lam? I don't </src><tgt>doublepとdoublemで綴られているの？</tgt>` | 2118 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src>know. </src><tgt>わからない。</tgt>` | 1149 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>这一张的部分呢，</src><tgt>이 부분은</tgt>` | 1009 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt>볼 수 있듯이</tgt>` | 1375 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 889 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>一个在跳舞的人，但是</src><tgt>춤을 추는 사람이 있는데,</tgt>` | 1701 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>他是属于逆向的</src><tgt>그는</tgt>` | 1365 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1468 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>。所以通常逢到这样的一个状况</src><tgt>역방향적인 사람입니다. 그래서 보통 이런 상황을</tgt>` | 1818 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>的时候，就要去</src><tgt>마주치면</tgt>` | 1912 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意</src><tgt>특별히 주의해야 합니다.</tgt>` | 1729 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能够</src><tgt>그 사람이</tgt>` | 2079 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1158 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>调到与他跳</src><tgt><\|wait\|></tgt>` | 1625 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 861 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>不到与你的意识哦。</src><tgt>당신의 의식과 조화를 이룰 수 있는지 말이죠.</tgt>` | 1197 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new. </src><tgt>没什么新鲜事。</tgt>` | 949 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>There was such </src><tgt><\|wait\|></tgt>` | 1258 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>interposes before, </src><tgt>以前有过这样的情况，</tgt>` | 1427 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1509 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netfilterTC, </src><tgt>netfilterTC，</tgt>` | 1368 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>yeah. </src><tgt>对。</tgt>` | 1520 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>So this is just </src><tgt>所以这只是</tgt>` | 642 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>one another place </src><tgt>另一个地方，</tgt>` | 1798 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>where it </src><tgt><\|wait\|></tgt>` | 1630 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1949 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>bad level. </src><tgt>坏的级别。</tgt>` | 807 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>Developers or engineers </src><tgt>开发者或工程师</tgt>` | 1848 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>working on Bug Repo </src><tgt>在BugRepo上</tgt>` | 1317 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>工作的人应该知道这一点。</tgt>` | 1179 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十一、二、三、</src><tgt><\|wait\|></tgt>` | 1631 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>とかでした。おそらく</src><tgt>应该是十一、二、三之类的。</tgt>` | 896 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>十秒で</src><tgt>大概十秒内</tgt>` | 1381 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1333 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1638 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>セフトンスかな</src><tgt><\|wait\|></tgt>` | 603 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt>一秒左右的片段吧。</tgt>` | 1772 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1571 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt>大概</tgt>` | 1114 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一、</src><tgt><\|wait\|></tgt>` | 1385 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>二、三、</src><tgt>十一、二、三、</tgt>` | 1591 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>であの</src><tgt>然后</tgt>` | 1424 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮川とかが</src><tgt>宫川之类的</tgt>` | 561 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>……</tgt>` | 1162 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 795 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HTML이라고 하는 </src><tgt><\|wait\|></tgt>` | 1212 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1576 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1446 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>있고 사람 도 </src><tgt><\|wait\|></tgt>` | 1386 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 어 언어 의 </src><tgt><\|wait\|></tgt>` | 2019 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1515 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 뭐랄게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1084 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 1748 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 1388 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1503 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 622 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1262 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | 1257 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that I think are </src><tgt><\|wait\|></tgt>` | 1064 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>really important. </src><tgt>これから動き出す人には、これが必要だと考えています。10個あります。本当に重要なものですね。</tgt>` | 2053 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 663 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1727 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1652 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>I have about one minute videos </src><tgt><\|wait\|></tgt>` | 2089 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の後に、1分程度の動画をいくつか</tgt>` | 1372 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt>用意しました。それぞれを解説しています。</tgt>` | 1761 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 651 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>You know, in a little more detail, </src><tgt>もう少し詳しく</tgt>` | 1338 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 981 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니와 너희 가 </src><tgt>知っているだろう。あなたたちが</tgt>` | 1875 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt>異邦人として</tgt>` | 652 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>いる時に、</tgt>` | 1300 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못하 는 </src><tgt>言えない</tgt>` | 1428 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>우상에게로 </src><tgt>偶像に</tgt>` | 1360 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>끄는 그대로 </src><tgt>従うままに、</tgt>` | 1713 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>引きずり込まれたのだ。</tgt>` | 2077 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1731 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>だから私は</tgt>` | 1944 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちに</tgt>` | 728 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>告げる。そして、</tgt>` | 1861 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | 1398 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>語る者は、</tgt>` | 1136 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1013 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>金運についてですが、</tgt>` | 1128 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | 1609 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>还不пло的，但是</src><tgt>悪くないですね。ただ、</tgt>` | 783 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分，</src><tgt>正財の面が</tgt>` | 1565 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1249 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>在事业方面的</src><tgt>仕事面が</tgt>` | 1393 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩增长所带来的</src><tgt>業績アップによる</tgt>` | 1689 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>红利与收入的</src><tgt>恩恵や収入の</tgt>` | 2048 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>提升。如果</src><tgt>向上に偏っています。</tgt>` | 1756 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>在投资理财方面呢，</src><tgt>投資や資産運用に関しては、</tgt>` | 2158 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 986 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，</src><tgt>悪くありません。</tgt>` | 1626 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>只是相对正财来说，</src><tgt>ただ、正財と比べると、</tgt>` | 1202 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>就稍微弱了一点</src><tgt>少し</tgt>` | 1113 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>点。</src><tgt>弱めです。</tgt>` | 1029 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt>그렇다면</tgt>` | 1078 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>蒸らせてやれ。</src><tgt>그냥 끓여버려.</tgt>` | 1610 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt>나는</tgt>` | 835 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1382 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>火通してみる。</src><tgt>불을 켜볼게.</tgt>` | 1498 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1349 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>이제</tgt>` | 1369 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>遠くに超えている</src><tgt>한계는</tgt>` | 800 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>船をキセキを</src><tgt>아득히 멀리 떨어진 배를 기적을</tgt>` | 2488 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1285 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2055 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長年にわだいこをやってる</src><tgt>하고 있는</tgt>` | 1276 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1599 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>が、俺はこんなにすごい</src><tgt>이 배가, 나는 이렇게 대단한</tgt>` | 818 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>海賊船を見た</src><tgt>해적선을</tgt>` | 1256 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>ことがない。</src><tgt>본 적이 없다.</tgt>` | 932 |

---

### Test Example 42 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>だから、</tgt>` | 1027 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 831 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt>こういうケースもあります。私たちは</tgt>` | 1631 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>Aという人と</tgt>` | 1340 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>Bという人が</tgt>` | 1230 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨설턴트 예요. </src><tgt>コンサルタントで、お互いに</tgt>` | 1490 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 컨설턴트가 </src><tgt>コンサルタントを</tgt>` | 1548 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>오 가지고 </src><tgt>呼んで、</tgt>` | 767 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aという人が</tgt>` | 1870 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪意のあるコードを</tgt>` | 1955 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>与えたとき、</tgt>` | 2097 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비란 사람이 </src><tgt>Bという人が</tgt>` | 1392 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1540 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로스사이트 CT에서 </src><tgt>クロスサイトCTで</tgt>` | 683 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>EX 파일까지 </src><tgt>EXファイルまで</tgt>` | 1203 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>感染するのか、</tgt>` | 1053 |

---

### Test Example 43 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1077 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어떻게 보면 </src><tgt>嗯，怎么说呢，</tgt>` | 1065 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1396 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1403 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>인생 이자 그래도 </src><tgt>也是和二十岁一起度过的生活，但</tgt>` | 1610 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>가족 같은 </src><tgt><\|wait\|></tgt>` | 1344 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아 </src><tgt>也是家人一样的弟弟，</tgt>` | 1723 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1664 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>저희 가 </src><tgt><\|wait\|></tgt>` | 1283 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>제인 가모다는 </src><tgt>我们JainGamoda</tgt>` | 1249 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1953 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1282 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1610 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | 727 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려놓 고 </src><tgt>放下了很多东西，</tgt>` | 1243 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>希望你们也能幸福。</tgt>` | 1101 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1312 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 해맨니다. </src><tgt>非常大。</tgt>` | 1423 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전을 </src><tgt><\|wait\|></tgt>` | 890 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>할 경우 는 </src><tgt>开车的话，</tgt>` | 1363 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어 다니 고는 뭐 </src><tgt>走路的话，</tgt>` | 1398 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북 으로 가면 </src><tgt>去江南区</tgt>` | 1746 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없이 </src><tgt>更是</tgt>` | 1594 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 장렬이에요. </src><tgt>去国外也是灾难。</tgt>` | 1931 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 810 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 재밌 겠네요. </src><tgt>挺有意思的。</tgt>` | 2121 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 이제 </src><tgt>不如</tgt>` | 1584 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1495 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>열심히 모았다고요. 그거 는 </src><tgt>努力攒钱？</tgt>` | 450 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>된 거 같아요. </src><tgt>好像已经做到了。</tgt>` | 1190 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 974 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1180 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1254 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1381 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? </src><tgt>실제 학력은 어느 정도까지 쌓으셨나요?</tgt>` | 1790 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>고등학교 졸업하셨나요?</tgt>` | 2254 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt>그게</tgt>` | 761 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>of attainment. </src><tgt>한 단계의 학력 수준입니다.</tgt>` | 1935 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>대학까지 가셨나요?</tgt>` | 1859 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, </src><tgt>만약 그렇다면,</tgt>` | 1987 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>졸업하셨나요?</tgt>` | 1092 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt>또 다른 단계의 학력 수준입니다.</tgt>` | 2170 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>그래서</tgt>` | 629 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>여기까지입니다.</tgt>` | 1306 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 998 |

---

### Test Example 46 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>So, this is about</tgt>` | 1237 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1501 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>というだけじゃなくて、</src><tgt>not just a visual development environment,</tgt>` | 854 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1367 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt>but a visual Python development environment.</tgt>` | 1779 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt>The reason is that</tgt>` | 1473 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルの書いてあと</src><tgt>you write a flow graph in Visual Flow Graph,</tgt>` | 1604 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それいつはPythonコード</src><tgt>and then</tgt>` | 1887 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>がそれから</src><tgt>Python code is generated from that,</tgt>` | 1786 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt>and that</tgt>` | 2028 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt>is executed,</tgt>` | 900 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt>and signal processing happens</tgt>` | 1786 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているからです。</src><tgt>in that structure.</tgt>` | 1034 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1100 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 494 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay,</tgt>` | 812 |

---

### Test Example 47 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そして、これについて</tgt>` | 896 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>多くの人が</tgt>` | 1177 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석 을 했었습니다. </src><tgt>分析しました。</tgt>` | 1135 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt>ここで</tgt>` | 1262 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>이 로쿠 자의 편집 을 보시면 </src><tgt>このロクジャの編集を見ると、</tgt>` | 1621 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니가 </src><tgt>ソニーが</tgt>` | 1347 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이력 제품에 </src><tgt>過去の製品に</tgt>` | 1708 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FP 파이 프를 </src><tgt>FPファームを</tgt>` | 1574 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>128ビットに</tgt>` | 1133 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>낮춘 것을 보입니다. </src><tgt>下げたことがわかります。</tgt>` | 1556 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1980 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈, X에서도 없는 </src><tgt>Xboxシリーズ、Xにもない</tgt>` | 1571 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1503 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>インフィニットキャッシュ、</tgt>` | 666 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>SD가 여기 도 없다. </src><tgt>SDもありません。</tgt>` | 1265 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知对手的</src><tgt>相手の</tgt>` | 1510 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>感情或</src><tgt>感情や</tgt>` | 870 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>真实意图的，</src><tgt>本心を見抜くこと、</tgt>` | 1707 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1368 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くは</tgt>` | 1396 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1543 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>好经常会听到人们</src><tgt>よく</tgt>` | 1631 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>这样说：“</src><tgt>「</tgt>` | 1013 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>見てくれ、</tgt>` | 1421 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 1968 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了。”</src><tgt>また嘘をついている」と言う。</tgt>` | 1240 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>その目は</tgt>` | 1419 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>すべてを物語っている。</tgt>` | 1064 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1123 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 657 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt>言わんばかりだ。</tgt>` | 625 |

---

### Test Example 49 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1259 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1163 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>생화 라 빌 거야. </src><tgt>生花を思い浮かべて。</tgt>` | 1255 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 돋든 </src><tgt>昔の</tgt>` | 1579 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>가자리 돋든 </src><tgt>虫や痒み、</tgt>` | 1597 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>느낌 이 너무야 </src><tgt>そんな感覚が、</tgt>` | 1831 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 흔들 어서 </src><tgt>揺れ動いて、</tgt>` | 1225 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうってことだよ。</tgt>` | 2021 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1686 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>귀신 이 오면 물릴 거고 </src><tgt>お化けが来たら噛みつかれるし、</tgt>` | 2542 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>시니 이면이야 너 </src><tgt>鬼が来たら、</tgt>` | 1795 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>지켜 주라고 </src><tgt>お前を守れって</tgt>` | 1472 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>찔러 주려 하니까 </src><tgt>刺そうとするから、</tgt>` | 1287 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>リラックスして</tgt>` | 983 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | 616 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、そして</tgt>` | 1253 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1147 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, </src><tgt>自分に基準を定めること。つまり、自分たちが基準だと考えていること。</tgt>` | 2046 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct. </src><tgt>その通りです。</tgt>` | 1181 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1474 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is is that </src><tgt>しかし、現実には、</tgt>` | 1458 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt>私たちは</tgt>` | 1932 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>block, and because the </src><tgt>新しいブロックだからです。</tgt>` | 1757 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1967 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>standards have changed from 20 </src><tgt>基準は</tgt>` | 914 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt>20年前に変わってしまって、</tgt>` | 2111 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 914 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>より高い基準を</tgt>` | 1144 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>求められています。なぜなら、今の</tgt>` | 1152 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 639 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1100 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1252 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt>If the stock index is rising,</tgt>` | 1226 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1397 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1451 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt>it will likely rise sharply,</tgt>` | 2102 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 982 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1822 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 들이 </src><tgt>but first, these smaller stocks</tgt>` | 1666 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1066 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이 기 때문 에 </src><tgt>move the market first,</tgt>` | 1789 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1834 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시 총이 </src><tgt><\|wait\|></tgt>` | 1452 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1203 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | 1069 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>같습니다. </src><tgt>so you should always keep an eye on these smaller stocks.</tgt>` | 831 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 1133 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>you will not be able to </src><tgt>你将无法</tgt>` | 1315 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1360 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1478 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | 1390 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>So, if </src><tgt>所以，</tgt>` | 1362 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into </src><tgt><\|wait\|></tgt>` | 745 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt>如果你遇到</tgt>` | 1744 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize </src><tgt>意识到</tgt>` | 1519 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>you've added the wrong media </src><tgt>添加了错误的媒体文件，</tgt>` | 1335 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>并且</tgt>` | 1467 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>you need to let us know. </src><tgt>需要通知我们。</tgt>` | 1695 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>Now, we can see about </src><tgt>现在，我们可以</tgt>` | 1642 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1116 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure they </src><tgt>移动这些媒体文件，并确保它们</tgt>` | 1064 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt>被正确备份，</tgt>` | 534 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>确保备份正确。</tgt>` | 481 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1373 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 1079 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1215 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1344 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the EHR </src><tgt><\|wait\|></tgt>` | 1247 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>field being of critical </src><tgt><\|wait\|></tgt>` | 813 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 1205 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus the </src><tgt><\|wait\|></tgt>` | 1429 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 1617 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>which is obviously </src><tgt><\|wait\|></tgt>` | 1310 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1189 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 2044 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1262 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1509 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 828 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources, that we can </src><tgt><\|wait\|></tgt>` | 1145 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from. </src><tgt><\|wait\|></tgt>` | 1077 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 641 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 453 |

---

### Test Example 54 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>FlowOD的折扣</src><tgt>FlowOD의 할인</tgt>` | 1426 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>截止到那个限，</src><tgt>마감일까지</tgt>` | 903 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1408 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>美登我们储于</src><tgt>미국에서는</tgt>` | 1498 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1329 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>爱集中所谓的</src><tgt>사랑에 집중하고</tgt>` | 1738 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1627 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>爱，我们也同时进入恨</src><tgt>사랑하는 동시에</tgt>` | 1655 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 850 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>在长上的时候，</src><tgt>증오에 빠져들고 있습니다.</tgt>` | 2316 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>它是爱。</src><tgt>그것이 바로 사랑입니다.</tgt>` | 1599 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | 1588 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>它就变成</src><tgt>그것은</tgt>` | 310 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>恨，那个钟摆。</src><tgt>증오로 변합니다. 그 시계추가요.</tgt>` | 1294 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在移动，</src><tgt>계속 움직이며</tgt>` | 493 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>然后。</src><tgt>그리고...</tgt>` | 349 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時点では、</tgt>` | 971 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>彼はイエスを</tgt>` | 1369 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is hungry. </src><tgt>飢えていると知っています。</tgt>` | 907 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1331 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's going to </src><tgt>彼は、</tgt>` | 1523 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1330 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>for forty days that he's hungry. </src><tgt>40日間、飢えながら荒野にいることを知っています。</tgt>` | 1974 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>And so he sends </src><tgt>そこで彼は</tgt>` | 1880 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>to Jesus. He says," </src><tgt>イエスに送ります。「</tgt>` | 1937 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>If you are the Son of God, prove it </src><tgt>もしあなたが神の御子なら、</tgt>` | 2507 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1794 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>turn these stones to bread." </src><tgt>この石をパンに変えなさい」と言いました。</tgt>` | 1554 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1203 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>How did Jesus deal with that? </src><tgt>イエスはどう対処したのでしょうか？</tgt>` | 1098 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>The temptation. </src><tgt>誘惑です。</tgt>` | 551 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 415 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Man, Jonathan lead by bread. </src><tgt>いやはや、ヨハネはパンによって導かれたのです。</tgt>` | 540 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>一人で。</tgt>` | 303 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1283 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 1154 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1369 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1225 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. </src><tgt>这是一个有意义的个人权利，最高法院是最后才加入的，而不是引领。</tgt>` | 1691 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>And I don't think the courts want to be </src><tgt>我不认为法院想成为</tgt>` | 1929 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1817 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1542 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. It's a </src><tgt>社会变革的先锋。</tgt>` | 1004 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>these days. </src><tgt>现在是这样。</tgt>` | 1801 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt>但他们更愿意</tgt>` | 1503 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1505 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt>反映</tgt>` | 540 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1282 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>that's already emerged. </src><tgt>已经形成的共识。</tgt>` | 1009 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>所以。</tgt>` | 510 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt>你</tgt>` | 413 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt>有了一些联邦法官，</tgt>` | 362 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 328 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>他们……</tgt>` | 317 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>그럼</tgt>` | 945 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt>그림을 한번 살펴볼게요.</tgt>` | 1613 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 884 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>그림 부분에는</tgt>` | 1520 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 1420 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>一个是客厅的部分，</src><tgt>거실 부분과</tgt>` | 1359 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | 1709 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1678 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1282 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>我们在休息的地方，</src><tgt>쉴 때 쓰는 공간이에요.</tgt>` | 1249 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt>그래서</tgt>` | 1976 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>来自身体的部分</src><tgt>몸의 부분은</tgt>` | 1377 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1685 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 605 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 1274 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 997 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>坐下来休息</src><tgt><\|wait\|></tgt>` | 574 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>。可我们可以看到这边是</src><tgt>잠시 앉아서 쉬어야 한다는 걸 보여줘요. 여기는</tgt>` | 666 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>空无一人的吗？</src><tgt>사람이 없는 것 같네요?</tgt>` | 439 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>좋아요,</tgt>` | 286 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>그러니까...</tgt>` | 276 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>彼らは</tgt>` | 879 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>非常に珍しく、</tgt>` | 1274 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>よく</tgt>` | 1059 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1289 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 981 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>completely revolutionize the world </src><tgt>世界を完全に変革する</tgt>` | 1032 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1474 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>their personality is </src><tgt>ような人物です。彼らの性格は</tgt>` | 1465 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾しています。</tgt>` | 1893 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1572 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1058 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ですが、</tgt>` | 1747 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt>同時に</tgt>` | 1528 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1768 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 1127 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 667 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>get straight to the point. </src><tgt>そして、要点を簡潔に話すのが好きです。</tgt>` | 939 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love to </src><tgt><\|wait\|></tgt>` | 462 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 429 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>play the devil's advocate, </src><tgt>また、悪魔の代弁者になるのも好きです。</tgt>` | 558 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 328 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 414 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 332 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>INTP stands for </src><tgt>INTPは</tgt>` | 339 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>introvert, </src><tgt>内向的、</tgt>` | 365 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 1108 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>강물 을 거부 한 </src><tgt><\|wait\|></tgt>` | 1562 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 721 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1387 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1596 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1428 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 냈지만 </src><tgt><\|wait\|></tgt>` | 1646 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>이제 는 </src><tgt><\|wait\|></tgt>` | 1848 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1567 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 827 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1934 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석은 드러내 놓고 </src><tgt><\|wait\|></tgt>` | 1560 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1583 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>제거 해 버리겠다는 </src><tgt><\|wait\|></tgt>` | 503 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뜻끼를 품은 </src><tgt><\|wait\|></tgt>` | 1224 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 936 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 608 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 417 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>작정 한 것입니다. </src><tgt>Previously, Lee Jun- seok had made it sound like he was rejecting the candidate and was only supporting the candidate's victory, even going so far as to seem sincere. But now, as Yoon Suk- yeol removed Kim Jong- in, Lee Jun- seok is showing his aggressive intent to remove Yoon Suk- yeol.</tgt>` | 1243 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 이준석의 </src><tgt><\|wait\|></tgt>` | 317 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>성상 답건 </src><tgt><\|wait\|></tgt>` | 326 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 309 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 383 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기의 얼마나 </src><tgt><\|wait\|></tgt>` | 311 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까? </src><tgt>How big of a boon is this for the Democratic Party's attack?</tgt>` | 421 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 848 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので</src><tgt>I want to make something after a meal now. So,</tgt>` | 1693 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1426 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>プロフェッショナルホテル</src><tgt><\|wait\|></tgt>` | 1517 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>で朝食が</src><tgt><\|wait\|></tgt>` | 1434 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1613 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になっている</src><tgt><\|wait\|></tgt>` | 1624 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>it's planned to be a place where you can have breakfast at a professional hotel.</tgt>` | 1963 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 863 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドーストーンホテル</src><tgt><\|wait\|></tgt>` | 1985 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 1535 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なっていう方はですね</src><tgt>If you're thinking of staying at the Goldstone Hotel here in the future,</tgt>` | 1835 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1236 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>まあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 1016 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt>I'd say it's a good idea to consider it. Yeah.</tgt>` | 849 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 379 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここのホテルからですね</src><tgt><\|wait\|></tgt>` | 344 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 340 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 274 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 328 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 301 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 284 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のねまあホテル</src><tgt><\|wait\|></tgt>` | 237 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 327 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 292 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 314 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それなら</src><tgt>Since the hotel is in a location where you can walk to Busan Station in about a mile, I hope you'll consider it. That way,</tgt>` | 363 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は</src><tgt><\|wait\|></tgt>` | 198 |
