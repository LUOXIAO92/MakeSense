# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9954
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9636
  - SRC_RELEASE_TOTAL: 715
  - SRC_WAIT_ACCURACY: 0.1933
  - SRC_WAIT_TOTAL: 150
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.7586
  - TGT_RELEASE_TOTAL: 493
  - TGT_WAIT_ACCURACY: 0.5215
  - TGT_WAIT_TOTAL: 372
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1309.9860
  - PROCESS_TIME_MS_P50: 1249.1670
  - PROCESS_TIME_MS_P95: 2036.4300
  - PROCESS_TIME_MS_MAX: 12321.9140

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
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt>从一开始</tgt>` | 706 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 797 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>仲までまだ</src><tgt>仲还没到</tgt>` | 1161 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>1年生ですからね。</src><tgt>大一啊。</tgt>` | 1158 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>はいはいはい、その時点で</src><tgt>好，好，好，在那时候</tgt>` | 1468 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1187 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>四角線で</src><tgt>用四角线</tgt>` | 1562 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数していって</src><tgt>对数化，</tgt>` | 1342 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>上げる</src><tgt>然后</tgt>` | 830 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>と10年経っても</src><tgt>就算过了十年，</tgt>` | 1752 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>対した</src><tgt>还是不值一提。</tgt>` | 534 |

---

### Test Example 2 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>lastly, </src><tgt>最后，</tgt>` | 802 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>he repeats </src><tgt><\|wait\|></tgt>` | 1118 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>learning to repeat </src><tgt>他重复学习</tgt>` | 1174 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>by learning to repeat </src><tgt><\|wait\|></tgt>` | 1070 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>by doing more of it </src><tgt>重复，通过多做一些</tgt>` | 1509 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1610 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>good at it, </src><tgt>练习，</tgt>` | 841 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>it gets people around you to help you with </src><tgt><\|wait\|></tgt>` | 1667 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt>周围的人就会</tgt>` | 1690 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>in tell next time </src><tgt><\|wait\|></tgt>` | 1752 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1161 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>的总结点，</src><tgt>Why the summary point?</tgt>` | 1153 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个收益也很大，</src><tgt>The return is also very high,</tgt>` | 1593 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 799 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，我在</src><tgt>and then I</tgt>` | 1591 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1318 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>跟陶人</src><tgt><\|wait\|></tgt>` | 1191 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1782 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在一起待了一段时间。</src><tgt>spent some time with Tao Ren during my vacation.</tgt>` | 714 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1455 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>和陶人</src><tgt>This kind of</tgt>` | 1870 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 1007 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>是容易的，</src><tgt>気数をつけるのは簡単です。</tgt>` | 1566 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 832 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>一个师傅</src><tgt>しかし、師匠が</tgt>` | 965 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>值得录。</src><tgt>認めてくれる</tgt>` | 1507 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如和除于</src><tgt><\|wait\|></tgt>` | 1531 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>中间。</src><tgt>ような人だけです。</tgt>` | 1171 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以，</src><tgt>だから、</tgt>` | 1465 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>反省が必要</tgt>` | 738 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 1774 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>师傅。</src><tgt>です。師匠になる</tgt>` | 2061 |

---

### Test Example 5 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 831 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 900 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떤 척박 시키고 </src><tgt>I am making it barren,</tgt>` | 1540 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 907 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 1289 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로지기인 </src><tgt><\|wait\|></tgt>` | 1324 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1389 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1073 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1191 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1876 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt>the heir of Morogigi, Haruna, and Park Han-sang, and their generation.</tgt>` | 2254 |

---

### Test Example 6 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>做的是</src><tgt>Parents need to</tgt>` | 1144 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1106 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | 1143 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1580 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十秒，</src><tgt>use our love glue for ten seconds,</tgt>` | 1945 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给子孩子</src><tgt><\|wait\|></tgt>` | 978 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心里吸引</src><tgt>to attract children's hearts.</tgt>` | 1669 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的耐心，</src><tgt><\|wait\|></tgt>` | 1885 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>等他</src><tgt><\|wait\|></tgt>` | 546 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>慢慢长大。</src><tgt>Then he slowly grows up.</tgt>` | 1788 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘纱完以后，</src><tgt>淘紗が終わったら、</tgt>` | 1414 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 757 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>的液体染清</src><tgt>内部の液体染料を</tgt>` | 1566 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 871 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>刷了落了，然后就</src><tgt>刷り落とします。それから</tgt>` | 2202 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1509 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>一个相对的</src><tgt>相対的な</tgt>` | 865 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 1435 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>态。</src><tgt>低エネルギーの動作状態に留まります。</tgt>` | 1944 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就</src><tgt><\|wait\|></tgt>` | 1719 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>所谓的</src><tgt>これが</tgt>` | 673 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1234 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들은 </src><tgt>The Nixs on the list</tgt>` | 1400 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 835 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1059 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt>actually weren't that smart,</tgt>` | 1585 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1771 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들이었기 때문 </src><tgt>they were just randomly selected Nixs.</tgt>` | 1307 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>입니다. </src><tgt>That's why.</tgt>` | 1506 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1842 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 443 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>The teachers who didn't know the Sasi</tgt>` | 2287 |

---

### Test Example 9 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 793 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>body saying? </src><tgt>你的身体在说什么？</tgt>` | 1214 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop pin to your body. </src><tgt>把针头插到你的身体上。</tgt>` | 1556 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 762 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>the tension start? </src><tgt>紧张感从哪里开始？</tgt>` | 1917 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>What is it? Is it </src><tgt>是什么？</tgt>` | 1498 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>a day? </src><tgt>是某一天？</tgt>` | 909 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it in your chest? </src><tgt>是在你的胸口吗？</tgt>` | 1809 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>Or is it </src><tgt>还是</tgt>` | 1690 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a low level of energy </src><tgt>低能量</tgt>` | 1828 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>you use saying? </src><tgt>？</tgt>` | 971 |

---

### Test Example 10 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1079 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这里开始，</tgt>` | 1110 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので</src><tgt>它开始</tgt>` | 993 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1144 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご方法</src><tgt>了。</tgt>` | 1106 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ご言やん</src><tgt><\|wait\|></tgt>` | 1419 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1512 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt>塞尚</tgt>` | 832 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1442 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の</src><tgt>像卢纳尔</tgt>` | 1914 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>絵は田舎の</src><tgt><\|wait\|></tgt>` | 1790 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>中学生でも</src><tgt>的画，</tgt>` | 1184 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 830 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt>重要な研究を</tgt>` | 877 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely </src><tgt><\|wait\|></tgt>` | 1052 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>happy people? This is </src><tgt>極めて幸せな人々の間で、様々な研究が行われたのでしょうか？</tgt>` | 1588 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem, </src><tgt>これは</tgt>` | 1476 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research. </src><tgt>研究の先端です。</tgt>` | 1541 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at </src><tgt><\|wait\|></tgt>` | 1081 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10% of the happiest </src><tgt>最も幸せな人々の10%を見れば、</tgt>` | 2142 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1690 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. </src><tgt>その人たちがいれば、</tgt>` | 1761 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>People like we can learn from. </src><tgt>私たちも学ぶことができます。</tgt>` | 1369 |

---

### Test Example 12 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 868 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt>On the other hand,</tgt>` | 1035 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여 달라고 주고 내가 죽일 려 </src><tgt>I'd rather you kill me</tgt>` | 1793 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>그것으로 하소서. </src><tgt>for that.</tgt>` | 944 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 쯤에 </src><tgt>At another feast,</tgt>` | 1715 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1472 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>하자는 거야. 내가 </src><tgt>I'd rather you kill me,</tgt>` | 1215 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt>and I'm not hearing that kind of talk.</tgt>` | 1666 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>중요한 거야. </src><tgt>That's important.</tgt>` | 1943 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1983 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1518 |

---

### Test Example 13 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 680 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt>저를</tgt>` | 750 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1158 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>鬼道号，</src><tgt>귀도호로 돌아가게 해 주세요.</tgt>` | 1428 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够好好的</src><tgt><\|wait\|></tgt>` | 1316 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>在它下面的时候，</src><tgt>그 아래에서</tgt>` | 1310 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日航</src><tgt><\|wait\|></tgt>` | 1449 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>日航日航日航</src><tgt>하루하루</tgt>` | 1577 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>日航</src><tgt><\|wait\|></tgt>` | 831 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>但是被它用作</src><tgt>니혼항공을</tgt>` | 1834 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的愿望</src><tgt><\|wait\|></tgt>` | 1947 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt>작은 소원처럼 사용하고 있어요.</tgt>` | 1894 |

---

### Test Example 14 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>アドワンさん</src><tgt>Advantageさん，</tgt>` | 1179 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れて</src><tgt><\|wait\|></tgt>` | 1294 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>くるみたいな感じで</src><tgt>感觉有点距离感</tgt>` | 1227 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 869 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>やっぱり多いですね。</src><tgt>大将还是挺多的。</tgt>` | 1725 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>囲いをしてたい方って</src><tgt>想围住</tgt>` | 1787 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ囲いこしけたい</src><tgt>的</tgt>` | 1043 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>方</src><tgt><\|wait\|></tgt>` | 1526 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>でみても</src><tgt>人，</tgt>` | 1794 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>とともに</src><tgt><\|wait\|></tgt>` | 535 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>おととしかけが強るので、</src><tgt>因为他们想马上围住，而且围住的力度也很大，</tgt>` | 2973 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので</src><tgt>所以</tgt>` | 686 |

---

### Test Example 15 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 이럴지 너무 </src><tgt>これ、</tgt>` | 1141 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좋아요. </src><tgt>いいですね。</tgt>` | 930 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>이럴 수 있지만 </src><tgt>そうなるかもしれませんが、</tgt>` | 1303 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살도요. </src><tgt>本当に菩薩も</tgt>` | 1100 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 자기 의 </src><tgt>そうじゃないんです。</tgt>` | 1588 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 피로고 </src><tgt>自分の菩薩なのに、夢を見ているんです。</tgt>` | 2310 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>보이 고 나만 </src><tgt>見えて、私だけが</tgt>` | 1703 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>이 보살 로 </src><tgt>この菩薩として</tgt>` | 687 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>보일 피로고 </src><tgt>見えて、宇宙が</tgt>` | 1863 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>없다. 이 보살 이란 </src><tgt>ないんです。この菩薩というのは</tgt>` | 2214 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>그냥 </src><tgt>ただ</tgt>` | 1579 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right, </src><tgt>好的，</tgt>` | 1175 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>and then after </src><tgt>然后</tgt>` | 981 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>these examples, </src><tgt>这些例子之后，</tgt>` | 1179 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1137 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1134 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>它告诉我们</tgt>` | 1410 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1483 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1190 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>these </src><tgt>实际上</tgt>` | 945 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>values. So </src><tgt>就是这些值。</tgt>` | 1507 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this game. </src><tgt><\|wait\|></tgt>` | 687 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>board array, </src><tgt>所以这个game.board数组，</tgt>` | 2091 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1787 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 807 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>A Aが</src><tgt>That A A</tgt>` | 782 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>あるんですね。</src><tgt>exists, right?</tgt>` | 1161 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その上面で</src><tgt><\|wait\|></tgt>` | 1178 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>正則化を行うときに</src><tgt>When you perform regularization on the upper face,</tgt>` | 1369 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>Aの乱交を</src><tgt><\|wait\|></tgt>` | 1409 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、</src><tgt>you look into the cross-correlation of A,</tgt>` | 1648 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その正則化を行う</src><tgt><\|wait\|></tgt>` | 1572 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>正則化を</src><tgt>and then perform regularization</tgt>` | 753 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>正則化を</src><tgt><\|wait\|></tgt>` | 1783 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>正則化を</src><tgt>with regularization,</tgt>` | 1972 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使った方法をされています。</src><tgt>you're using a method that uses regularization.</tgt>` | 2036 |

---

### Test Example 18 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为这个情况</src><tgt><\|wait\|></tgt>` | 869 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt>Because of this situation,</tgt>` | 1125 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题，</src><tgt>we encounter problems,</tgt>` | 1110 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就更改了回报主管</src><tgt><\|wait\|></tgt>` | 1165 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt>and we have to change the reporting manager or notify the other party</tgt>` | 2389 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt>we laugh at the situation,</tgt>` | 1659 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt>don't think about yourself</tgt>` | 1612 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>怎么都把它扛下来，</src><tgt>carrying it all,</tgt>` | 735 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>工具理性</src><tgt><\|wait\|></tgt>` | 1776 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>承当责任，真的而已，</src><tgt>and taking responsibility with a tool-rational mindset— it's really just that.</tgt>` | 2553 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>是给就是</src><tgt>It's just</tgt>` | 1487 |

---

### Test Example 19 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt>T-shirts, etc.</tgt>` | 1308 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 803 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1106 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただきたいようなものも</src><tgt><\|wait\|></tgt>` | 1218 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt>We have things like T-shirts that you might want to have ready,</tgt>` | 2226 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ぜひご参考ください。</src><tgt>so please take a look.</tgt>` | 1599 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt>For contact,</tgt>` | 710 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>that's all.</tgt>` | 1623 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1784 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>例えば</src><tgt><\|wait\|></tgt>` | 512 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ニュースの案内がありますので、</src><tgt>For example, we have news updates,</tgt>` | 2110 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>ぜひお目に合わせてください。</src><tgt>so please check them out.</tgt>` | 1757 |

---

### Test Example 20 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1165 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt>19차 수정헌법의 의미는</tgt>` | 1712 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 782 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>to explore </src><tgt>그리고</tgt>` | 788 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>its history as a guide </src><tgt>그 역사를 가이드로</tgt>` | 1530 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help political </src><tgt><\|wait\|></tgt>` | 1450 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change </src><tgt><\|wait\|></tgt>` | 1213 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>정치적 변화를 돕는 데</tgt>` | 1748 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서</tgt>` | 568 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1671 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt>수정헌법의 의미는</tgt>` | 1905 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, </src><tgt>물론</tgt>` | 1881 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>I'm Miriam. </src><tgt>미리엄입니다.</tgt>` | 622 |

---

### Test Example 21 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个</src><tgt>二つ目は</tgt>` | 845 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是进入到</src><tgt><\|wait\|></tgt>` | 826 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>二期市场，</src><tgt>第二期市場への移行です。</tgt>` | 1340 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会服务</src><tgt><\|wait\|></tgt>` | 1147 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在一期一线</src><tgt><\|wait\|></tgt>` | 1115 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>第一期の一線大牛たちを</tgt>` | 1812 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，</src><tgt>例えば、</tgt>` | 1184 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 1573 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好事期间，</src><tgt>We'll provide communication during the WeChat</tgt>` | 866 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1737 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>微信好</src><tgt>好景気を見つけられるでしょう。</tgt>` | 1838 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平凡的星棒</src><tgt><\|wait\|></tgt>` | 1756 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>反而活了。</src><tgt>むしろ、平凡な星棒が生き返ったようなものです。</tgt>` | 923 |

---

### Test Example 22 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>So this </src><tgt>그래서</tgt>` | 834 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこ で </src><tgt>그럼</tgt>` | 758 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think </src><tgt><\|wait\|></tgt>` | 1152 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>to do this at 7.2 GB </src><tgt>7.2GB로</tgt>` | 1464 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>already. </src><tgt>이미 생각하셨죠.</tgt>` | 1493 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt>그런데</tgt>` | 1321 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1281 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the heavy use of </src><tgt>무거운</tgt>` | 1552 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the system </src><tgt><\|wait\|></tgt>` | 840 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>of the whole </src><tgt><\|wait\|></tgt>` | 1789 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.2 GB </src><tgt><\|wait\|></tgt>` | 1975 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>GB </src><tgt><\|wait\|></tgt>` | 1569 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>is this. </src><tgt>7.2GB를 다 사용하고 있다는 게 문제예요.</tgt>` | 1054 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Chunah Teru, </src><tgt>제 이름은 츠나 테루입니다.</tgt>` | 1780 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1000 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in AI, </src><tgt>현재 AI를 공부하고 있습니다.</tgt>` | 970 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>back-end finance, </src><tgt><\|wait\|></tgt>` | 1536 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a bit of psychology. </src><tgt>그리고 약간의 심리학도 공부하고 있습니다.</tgt>` | 2004 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 993 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>you're into AI, </src><tgt>AI에 관심이 많으신 것 같네요.</tgt>` | 1468 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1794 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>미래에는</tgt>` | 2144 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consulting, </src><tgt><\|wait\|></tgt>` | 1741 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1239 |

---

### Test Example 24 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 762 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1163 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间，</src><tgt>If you're in a high school girl's eyes, and you're not unattractive,</tgt>` | 2247 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又</src><tgt><\|wait\|></tgt>` | 1448 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>有种矛盾性，</src><tgt>you have a sense of contradiction,</tgt>` | 1905 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道</src><tgt><\|wait\|></tgt>` | 963 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>会是</src><tgt>could it be that</tgt>` | 1741 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里</src><tgt><\|wait\|></tgt>` | 1533 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>that started the night that night?</tgt>` | 758 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1977 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1758 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>系列篇。</src><tgt>The Yang Zisi series.</tgt>` | 1339 |

---

### Test Example 25 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber </src><tgt>고무줄처럼</tgt>` | 1007 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>band, </src><tgt>밴드처럼,</tgt>` | 941 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt>화학 결합도</tgt>` | 1593 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy, </src><tgt>에너지를 저장합니다.</tgt>` | 924 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | 2206 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt>그 잠재 에너지는</tgt>` | 1651 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to </src><tgt>다른 형태로</tgt>` | 1503 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>변환됩니다.</tgt>` | 776 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt>열이나 빛 같은</tgt>` | 1834 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>or gets used </src><tgt>에너지로 사용됩니다.</tgt>` | 1966 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds </src><tgt>다른 결합을 만들 때</tgt>` | 1985 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1391 |

---

### Test Example 26 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 </src><tgt><\|wait\|></tgt>` | 1131 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt>Things like vanadium</tgt>` | 930 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유니트 링과 </src><tgt>are basically unit rings</tgt>` | 1559 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 거진 </src><tgt><\|wait\|></tgt>` | 913 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사한 링이 </src><tgt>and similar rings</tgt>` | 1740 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>그런 걸 굉장히 </src><tgt><\|wait\|></tgt>` | 1442 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt>are very, very</tgt>` | 982 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 다물리다 </src><tgt><\|wait\|></tgt>` | 1725 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이리다 </src><tgt>closed, and</tgt>` | 1846 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이리다 </src><tgt><\|wait\|></tgt>` | 420 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt>that's how it is. Now,</tgt>` | 2033 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거에다가 </src><tgt>on top of that,</tgt>` | 1723 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1359 |

---

### Test Example 27 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt>이것이</tgt>` | 1130 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>ギアです。</src><tgt>기어입니다.</tgt>` | 1152 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが緩むと</src><tgt>기어가 헐거워지면</tgt>` | 1641 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>信号が</src><tgt>신호가</tgt>` | 847 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>逆にできなくなって</src><tgt>반대로 안 되어서</tgt>` | 1708 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>안 되게 되니까</tgt>` | 1567 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | 990 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1647 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>역나사 너트가</tgt>` | 1937 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt>붙어 있다는 뜻입니다.</tgt>` | 1885 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ね。</src><tgt>네.</tgt>` | 1593 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src>はい、</src><tgt>네,</tgt>` | 703 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>文部会完了を</src><tgt>문부회 완료를</tgt>` | 1534 |

---

### Test Example 28 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt>彼は</tgt>` | 718 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>前头，</src><tgt>前方に</tgt>` | 1153 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt>いる。もし</tgt>` | 1098 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了前头之后</src><tgt>前方に到達したら、</tgt>` | 1171 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请你</src><tgt>お願いします</tgt>` | 1438 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>务必</src><tgt>必ず</tgt>` | 1396 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>走，不要</src><tgt>歩いてください。</tgt>` | 1309 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>想说，</src><tgt>「ああ、</tgt>` | 1528 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为我在去操作</src><tgt>操作しているから」なんて言わないでください。</tgt>` | 831 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>ね。</tgt>` | 1654 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1965 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt>なぜなら</tgt>` | 1523 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt>そんな言い方をするのか？なぜなら、</tgt>` | 1263 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 882 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Or or if you have </src><tgt>あるいは、</tgt>` | 1022 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt>生産する</tgt>` | 892 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written </src><tgt>文書を作成する必要がある場合、</tgt>` | 1345 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text </src><tgt>テキストを作成する</tgt>` | 997 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt>と気づく</tgt>` | 1519 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>と、</tgt>` | 1691 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt>スペルが</tgt>` | 1167 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>because it's like, oh, </src><tgt>わからない</tgt>` | 1864 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>is this word </src><tgt>なんていうか、「ああ、この単語は」</tgt>` | 2104 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>starts with a </src><tgt><\|wait\|></tgt>` | 1979 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>double p, </src><tgt>ダブルPで始まる</tgt>` | 1811 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l, </src><tgt>ダブルL、</tgt>` | 1335 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src>I don't know. </src><tgt>わからない。</tgt>` | 901 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 1313 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>啊，</src><tgt>あの、</tgt>` | 694 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>このローマでは、</tgt>` | 1141 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是以前造成</src><tgt>以前のように</tgt>` | 1141 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>的，所以呢，</src><tgt>そうではないので、</tgt>` | 1352 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt>今</tgt>` | 1134 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>所面临的一些</src><tgt>直面している</tgt>` | 1500 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt>危機や</tgt>` | 709 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>跟丰收</src><tgt>豊作</tgt>` | 1575 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也不可能是</src><tgt>も、</tgt>` | 1741 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就演变出来。</src><tgt>それらが同時に起こることはありません。</tgt>` | 565 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1889 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>的因果就会</src><tgt>因果関係は</tgt>` | 1862 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>见于这位朋友呢，</src><tgt>この友人の見解では、</tgt>` | 2108 |

---

### Test Example 31 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중에서 </src><tgt>その中で</tgt>` | 748 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150개 가 </src><tgt><\|wait\|></tgt>` | 1158 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>중요 범주 로 </src><tgt>150個が</tgt>` | 1609 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업들이 </src><tgt>非常に小さな企業</tgt>` | 963 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>많았습니다. </src><tgt>でした。</tgt>` | 1245 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的には</tgt>` | 1573 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt>中小企業は成長したり、</tgt>` | 1417 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>혹은 </src><tgt><\|wait\|></tgt>` | 1583 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>해외 뱅크에 </src><tgt>あるいは海外銀行に</tgt>` | 1917 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>거의 다는데 </src><tgt>ほとんど</tgt>` | 1758 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>외국 내 소기업 들은 성장 도 </src><tgt>成長も</tgt>` | 1246 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>폐업도 하지 않는 </src><tgt>していません。</tgt>` | 1170 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt>そういった現象が見られるようになったのです。</tgt>` | 2285 |

---

### Test Example 32 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 934 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切都正常，</src><tgt>Everything was normal back then,</tgt>` | 1374 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>毫无反应，</src><tgt><\|wait\|></tgt>` | 1051 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src>所以</src><tgt>no reaction at all. So</tgt>` | 968 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>坚持不开刀，</src><tgt>I insisted on not having surgery,</tgt>` | 2047 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>切片大概</src><tgt><\|wait\|></tgt>` | 1437 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>有十二位医生</src><tgt>and had about twelve doctors</tgt>` | 1083 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>来审断，</src><tgt>reviewing it.</tgt>` | 1601 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt>I was so tired I just</tgt>` | 2024 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一打提腿，</src><tgt><\|wait\|></tgt>` | 1859 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt>just kept kicking my legs, and it was fine.</tgt>` | 2158 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1493 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>疑惑的离开。</src><tgt>They all left looking puzzled.</tgt>` | 1130 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>帝僵的部分</src><tgt>帝僵的部分</tgt>` | 829 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt>우리가 본 것은</tgt>` | 1106 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1090 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴吊的人，但是</src><tgt>모자를 쓴 사람입니다. 하지만</tgt>` | 1289 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>他是属于逆向的</src><tgt>그는 역방향의</tgt>` | 2023 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1353 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>这种形状的</src><tgt>이런 모양의</tgt>` | 1050 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>状况会主要去</src><tgt>상황은 주로</tgt>` | 1613 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别要注意</src><tgt>특별히 주의해야 합니다.</tgt>` | 1994 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1794 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到与他</src><tgt><\|wait\|></tgt>` | 1693 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>掉不到与</src><tgt><\|wait\|></tgt>` | 752 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他的意识</src><tgt>그가 자신의 의식과</tgt>` | 1483 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>了。</src><tgt>연결되지 않느냐는 것입니다.</tgt>` | 1025 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new </src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>there </src><tgt><\|wait\|></tgt>` | 983 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1124 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>was such an episode before. </src><tgt>之前没有新的东西，</tgt>` | 1331 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1514 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>Netflix Future TC </src><tgt><\|wait\|></tgt>` | 1467 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>Yeah, </src><tgt>Netflix Future TC</tgt>` | 1182 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>so this is just </src><tgt><\|wait\|></tgt>` | 1822 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src><\|wait\|></src><tgt>就是</tgt>` | 508 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>one another place, </src><tgt><\|wait\|></tgt>` | 1735 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1977 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but </src><tgt>一个又一个地方，</tgt>` | 1709 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>developers, </src><tgt><\|wait\|></tgt>` | 445 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>engineers, </src><tgt><\|wait\|></tgt>` | 1377 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>they should be aware of that. </src><tgt>开发者、工程师都应该注意这一点。</tgt>` | 1126 |

---

### Test Example 35 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手</src><tgt>由于</tgt>` | 1021 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>とかだと</src><tgt>一二手</tgt>` | 1108 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>おそらく10秒で</src><tgt>大概10秒</tgt>` | 1229 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒</src><tgt>一秒</tgt>` | 1497 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>に</src><tgt>内</tgt>` | 1204 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt>一秒左右</tgt>` | 1384 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せつあんすかね</src><tgt>的设想呢？</tgt>` | 1651 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt>对吧。</tgt>` | 735 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 1756 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt>大概</tgt>` | 1720 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11二</src><tgt>11二</tgt>` | 1704 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>で</src><tgt>二</tgt>` | 672 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>那个</tgt>` | 1249 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt>见合う马</tgt>` | 1147 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから</src><tgt>什么的，</tgt>` | 951 |

---

### Test Example 36 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1116 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어차피 보면 </src><tgt>反正</tgt>` | 892 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt>看样子，</tgt>` | 1246 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt>20代</tgt>` | 1195 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이런 인생 이자 </src><tgt>就是</tgt>` | 1415 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt>这样的</tgt>` | 1153 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>人生，对吧？</tgt>` | 1611 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1481 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 844 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생감보다는 </src><tgt>不是</tgt>` | 1765 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt>自我感觉</tgt>` | 1998 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1593 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 635 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt>多一点。</tgt>` | 1324 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>放下</tgt>` | 989 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 </src><tgt>那些</tgt>` | 1103 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在餐饮方面</src><tgt>食事に関しては、</tgt>` | 937 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个菜你可以说是</src><tgt>この料理は</tgt>` | 1109 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>很不错的，但是</src><tgt>かなり良いですね。でも</tgt>` | 1474 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较正财的部分</src><tgt>正財の</tgt>` | 828 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1516 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>也是在事业方面的</src><tgt>部分も、事業の</tgt>` | 1783 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩增长所带来的</src><tgt>業績増加による</tgt>` | 1133 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>红利，</src><tgt>恩恵も</tgt>` | 1659 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1873 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>在投资理财方面</src><tgt>投資や資産運用に関しては、</tgt>` | 487 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 1824 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>悪くないですが、</tgt>` | 1901 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>相对来说就</src><tgt>相対的に</tgt>` | 1433 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>稍微弱了</src><tgt>少し弱くなりました。</tgt>` | 1138 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一点。</src><tgt><\|wait\|></tgt>` | 1071 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 764 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알고 있나요? </src><tgt>また知っていますか？</tgt>` | 1193 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1475 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>ここに異邦人として</tgt>` | 905 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1472 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>우상에게로 </src><tgt>言葉を失う</tgt>` | 1739 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>그리는 그대로 </src><tgt>偶像を描く</tgt>` | 973 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 갔느라 </src><tgt>まま連れて行かれ、</tgt>` | 1864 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그러다 </src><tgt><\|wait\|></tgt>` | 1855 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그럼으로 내가 </src><tgt>その結果、</tgt>` | 1850 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1297 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리노니 </src><tgt>あなたたちに</tgt>` | 1037 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님의 영으로 </src><tgt><\|wait\|></tgt>` | 1431 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>神の霊で語る者は</tgt>` | 1228 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1081 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who is </src><tgt>それは</tgt>` | 1090 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>まさに</tgt>` | 983 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt>やる気を出している人</tgt>` | 1238 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1085 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and that ten of them </src><tgt>で、その10人</tgt>` | 1535 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that are really important </src><tgt>が本当に</tgt>` | 1487 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1278 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to </src><tgt><\|wait\|></tgt>` | 1734 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>やるべき</tgt>` | 556 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1734 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt>動画を</tgt>` | 1843 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at the end of this video. </src><tgt>この動画の最後に1分間</tgt>` | 2106 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It'll cover each one. </src><tgt>紹介します。それぞれについて</tgt>` | 1839 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>And a little more </src><tgt><\|wait\|></tgt>` | 844 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, but </src><tgt>もう少し詳しく解説しますが、</tgt>` | 1141 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1163 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세인바라 </src><tgt><\|wait\|></tgt>` | 1169 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>セインバラを</tgt>` | 1271 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 소름이 </src><tgt><\|wait\|></tgt>` | 972 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>돋은 차리도 돋은 </src><tgt>もう鳥肌が</tgt>` | 2046 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>그 느낌 은 </src><tgt>立っている</tgt>` | 1309 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 998 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>한들어서 같이 놀자는 거야. </src><tgt>その感じをそのままに、一緒に遊ぼうっていう</tgt>` | 2052 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>귀신이 </src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>엄밀히 </src><tgt>気持ち悪い</tgt>` | 1736 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>그럴 거고 </src><tgt>って感じがするし、気持ち悪い</tgt>` | 1661 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>엄밀히 안 지켜 줄 거고 </src><tgt>って感じがするし、</tgt>` | 925 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>그러니까 </src><tgt>ちゃんと守ってくれないから、</tgt>` | 1547 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 마음 에. </src><tgt>リラックスしててね。</tgt>` | 868 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | 1249 |

---

### Test Example 41 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 783 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1131 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Hiemel이라고 하는 </src><tgt>哦，</tgt>` | 1182 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터도 </src><tgt>电脑叫Hiemel，</tgt>` | 1126 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있고 </src><tgt>可以理解，</tgt>` | 1668 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람도 </src><tgt>人</tgt>` | 1169 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있는 </src><tgt>也能理解</tgt>` | 1322 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터의 언어에 </src><tgt>电脑的语言</tgt>` | 1939 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1900 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법이 맞게 </src><tgt>语法正确，</tgt>` | 1847 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리가 이제 그것들을 </src><tgt><\|wait\|></tgt>` | 1612 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们现在需要写出这些，</tgt>` | 898 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1340 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>그것들을 작성 하는 프로그램 이 필요 합니다. </src><tgt>需要一个程序来写这些。</tgt>` | 1218 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1194 |

---

### Test Example 42 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和关于</src><tgt><\|wait\|></tgt>` | 1132 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>针对对手的感情</src><tgt>伝聞や、相手の感情に関する</tgt>` | 1641 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>或真实意图的。</src><tgt>あるいは真意について。</tgt>` | 1012 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くは</tgt>` | 1225 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1270 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>听到人们这样说，</src><tgt>人々がそう言うのを</tgt>` | 1866 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>啊。</src><tgt>よく聞きます。</tgt>` | 1305 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看。</src><tgt>見てください。</tgt>` | 824 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1711 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>躲黄了。</src><tgt>この人はまた逃げ出した</tgt>` | 1666 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 708 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>说明了一切。</src><tgt>ようです。彼の目はすべてを物語っています。</tgt>` | 1553 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 967 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 1062 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt>そう言っているのです。</tgt>` | 760 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>だから</tgt>` | 1027 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 요즘 이제 이런 경우 들을 </src><tgt>最近</tgt>` | 844 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>수입니다. 저희 가 </src><tgt>こういうケースが</tgt>` | 1307 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>あります。Aという人と</tgt>` | 1230 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람이 </src><tgt>Bという人が</tgt>` | 1416 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨컨트예요. </src><tgt>お互いにコンコントです。</tgt>` | 1796 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트 </src><tgt>Bがコンサルタント</tgt>` | 1348 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>여 가지고 A라는 </src><tgt>で、Aという</tgt>` | 1682 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>사람 이 </src><tgt>人が</tgt>` | 1874 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪性コードを</tgt>` | 783 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>들었을 때 </src><tgt>受けたとき</tgt>` | 1546 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>Bという人が</tgt>` | 1790 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 크로사이트스 </src><tgt>実際クロスサイトスクリプト</tgt>` | 1498 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>위에서 </src><tgt>で</tgt>` | 1044 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>XPI까지 </src><tgt>XPIまで</tgt>` | 1165 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까? </src><tgt>感染する可能性がある</tgt>` | 831 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational </src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>containment. How far </src><tgt>교육적 격리. 얼마나 멀리</tgt>` | 1618 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 931 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt><\|wait\|></tgt>` | 863 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1574 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>교육을 받았나요? 고등학교를 졸업했나요?</tgt>` | 2346 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt>그건 한 단계</tgt>` | 1342 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>containment. Did you </src><tgt>의 격리입니다. </tgt>` | 1110 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>go to college, </src><tgt>대학에 갔나요?</tgt>` | 1828 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>and so did you graduate </src><tgt>그리고 졸업했나요?</tgt>` | 2072 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>that's another level of </src><tgt>그건 또 다른 단계의</tgt>` | 1946 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>containment. </src><tgt>격리입니다.</tgt>` | 1373 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now. </src><tgt>지금은 여기까지입니다.</tgt>` | 1310 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 1170 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 747 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt>And this is,</tgt>` | 1069 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1116 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうだけじゃなくて</src><tgt>not just a visual development environment,</tgt>` | 1578 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 864 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | 2053 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1263 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアル</src><tgt>This is also a flow graph visual</tgt>` | 1138 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いてあとそれは</src><tgt><\|wait\|></tgt>` | 1539 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから生成</src><tgt>written in Python code, and then it generates</tgt>` | 2145 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>されてそれが</src><tgt><\|wait\|></tgt>` | 1902 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt>signals that run, which is signal processing.</tgt>` | 1979 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1340 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことをしているから</src><tgt>So it does that.</tgt>` | 1161 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt>That's why.</tgt>` | 1106 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt>Yes.</tgt>` | 589 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt>So,</tgt>` | 627 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1108 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 해매 니다. </src><tgt>进去的时候，真是太迷茫了。</tgt>` | 1538 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>이 운전 을 </src><tgt><\|wait\|></tgt>` | 1037 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 걸 </src><tgt><\|wait\|></tgt>` | 868 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 다니 고 </src><tgt>我走过这段路，</tgt>` | 1722 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있으면은 뭐 </src><tgt><\|wait\|></tgt>` | 1633 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북으로 가면 </src><tgt><\|wait\|></tgt>` | 1033 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt>如果去江南，那更是无话可说。</tgt>` | 1985 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가면 또 장려 리요. </src><tgt>如果出国，那更是鼓励。</tgt>` | 2001 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1866 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>진짜 꽤네요. </src><tgt>真的挺大的。</tgt>` | 1908 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1379 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt>不如现在</tgt>` | 1099 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>노가요. </src><tgt>好好努力工作。</tgt>` | 575 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>그거 는 안인 것 같아요. </src><tgt>我觉得那不是问题。</tgt>` | 1221 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>예. </src><tgt>是的。</tgt>` | 725 |

---

### Test Example 47 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt>그렇다면</tgt>` | 1109 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らせてやれ</src><tgt>젖게 해라.</tgt>` | 1209 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1109 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 940 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>火事を見ている</src><tgt>나는 불길을 보고 있는데,</tgt>` | 1414 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1209 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt>이제 한계가</tgt>` | 1491 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1571 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不れる不規則よ。</src><tgt>넘어선 불규칙해.</tgt>` | 941 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1737 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1949 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>のブナデイコを</src><tgt><\|wait\|></tgt>` | 1976 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってるんだ。</src><tgt>오랜 부나데이코를 하고 있는 거야.</tgt>` | 1998 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 723 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい快則線を見た</src><tgt>나는 이렇게 엄청난 카이조쿠센을 봤는데,</tgt>` | 1559 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>ことがない。</src><tgt>그런 적이 없어.</tgt>` | 745 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 </src><tgt>The stock market index</tgt>` | 1131 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인다면 </src><tgt>is rising,</tgt>` | 1362 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형주도 </src><tgt>and large-cap stocks</tgt>` | 1069 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt>will also see a significant rise,</tgt>` | 2147 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 726 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1679 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1921 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1826 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt>because the small-cap stocks lead the market first,</tgt>` | 1812 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 696 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시총이 </src><tgt><\|wait\|></tgt>` | 1484 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 온종목 을 </src><tgt><\|wait\|></tgt>` | 1015 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 될 것 같습니다. </src><tgt>it seems we should keep an eye on the market cap of the small-cap stocks.</tgt>` | 1726 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 635 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | 754 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람들이 </src><tgt>多くの人が</tgt>` | 951 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석을 해 놓았습니다. </src><tgt>分析してあります。</tgt>` | 1540 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 797 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>이 로쿠자이의 분석을 보시면 </src><tgt>このロクジャイの分析を見ると、</tgt>` | 2421 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>손이 가 </src><tgt><\|wait\|></tgt>` | 1400 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이외 력에 </src><tgt><\|wait\|></tgt>` | 860 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FPP 파이프를 </src><tgt><\|wait\|></tgt>` | 1588 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>このロクジャイの分析では、FPPパイプを128ビットで</tgt>` | 2241 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나출 것을 </src><tgt>出力することを</tgt>` | 1876 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>로 본다. </src><tgt>見なしています。</tgt>` | 1769 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 엑스에서도 </src><tgt>XboxシリーズのXboxでも</tgt>` | 1485 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>없는 </src><tgt><\|wait\|></tgt>` | 1118 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1160 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L2가 여기도 없다. </src><tgt>インフィニットキャッシュL2もありません。</tgt>` | 969 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 613 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 993 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining </src><tgt>活動、次に自己定義</tgt>` | 1133 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>what we think the standard is, </src><tgt>基準は、自分たちがどう考えているか</tgt>` | 1503 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt>です。なぜなら、</tgt>` | 1919 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1355 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt>現実とは、</tgt>` | 887 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid </src><tgt>私たちは新しい子だから、</tgt>` | 1829 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block </src><tgt>ブロックの中の新しい子だから、</tgt>` | 1987 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed </src><tgt>基準が変わったから、</tgt>` | 2211 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>from 20 </src><tgt>20から</tgt>` | 1775 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, we </src><tgt>20年前から、</tgt>` | 1505 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>are being held to </src><tgt>私たちは</tgt>` | 1037 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>our standard because </src><tgt>基準に縛られているんです。</tgt>` | 1132 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>everything at this point </src><tgt>なぜなら、今の時点では</tgt>` | 951 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to </src><tgt>すべてが</tgt>` | 627 |

---

### Test Example 51 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時点で、</tgt>` | 938 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 956 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is a hungry </src><tgt>彼はイエスが</tgt>` | 1280 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and he knows that </src><tgt><\|wait\|></tgt>` | 954 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he knows that </src><tgt>飢えていることを知っている。そして、</tgt>` | 1830 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>for he will in the Spirit </src><tgt>彼は聖霊の中にあることを知っている。</tgt>` | 2088 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>today, </src><tgt>今日、</tgt>` | 792 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>and so he says to </src><tgt>そして彼は</tgt>` | 1484 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>Jesus, say, "If </src><tgt>イエスよ、</tgt>` | 1901 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>the Son of God proves </src><tgt>もし神の子が</tgt>` | 1810 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it, turn these </src><tgt>真実なら、</tgt>` | 1489 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>stones to bread, </src><tgt>これらの石をパンに変えなさい、</tgt>` | 877 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>how did Jesus </src><tgt><\|wait\|></tgt>` | 1299 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>deal with that </src><tgt>イエスは</tgt>` | 1109 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>imitation?" </src><tgt>その模倣をどう扱ったのか、</tgt>` | 906 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 583 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Man, </src><tgt>おい、</tgt>` | 546 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>Jonathan lived by the law alone. </src><tgt>ジョナサンは律法だけで生きていたんだ。</tgt>` | 792 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 993 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, you will not </src><tgt>另外，</tgt>` | 993 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>be able to move </src><tgt>你将无法</tgt>` | 1238 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1040 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1084 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1188 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>either, if </src><tgt>在资源之间移动媒体对象，</tgt>` | 1713 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the </src><tgt><\|wait\|></tgt>` | 879 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>situation where you </src><tgt>如果你进入了</tgt>` | 1453 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1876 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt>你发现添加了错误的媒体文件，</tgt>` | 1836 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 1628 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>instead of </src><tgt>而不是</tgt>` | 713 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>the last one, and we can see about </src><tgt>最后一个，</tgt>` | 1789 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 854 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>us and then making sure </src><tgt>我们能看到这些媒体文件，然后确保</tgt>` | 1528 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 765 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们被正确备份。</tgt>` | 405 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src>For all the </src><tgt>모든</tgt>` | 769 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>the sorts </src><tgt><\|wait\|></tgt>` | 986 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>that are </src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src>not the same, </src><tgt>그것들은 다릅니다.</tgt>` | 1229 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but we are </src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>in the midst of </src><tgt>하지만 우리는</tgt>` | 1423 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>love. </src><tgt><\|wait\|></tgt>` | 1314 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src>We are also </src><tgt>사랑의 한가운데에 있습니다.</tgt>` | 1885 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>in the midst of </src><tgt><\|wait\|></tgt>` | 1446 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the time to </src><tgt>시간이</tgt>` | 728 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>start on the stage </src><tgt><\|wait\|></tgt>` | 2025 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>of the stage. </src><tgt>무대에 오를 때입니다.</tgt>` | 1950 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>It's down on the </src><tgt><\|wait\|></tgt>` | 1384 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>stage, and it becomes </src><tgt>무대 아래에 내려와서</tgt>` | 1319 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 1063 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>the whole thing. </src><tgt>모든 것이</tgt>` | 810 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 643 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>It continues to evolve. </src><tgt>변화합니다. 계속해서</tgt>` | 505 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1393 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の数マイル間違えてしまって</tgt>` | 1516 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで</tgt>` | 1054 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 867 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt>AHRフィールドについて</tgt>` | 1706 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt>重要な</tgt>` | 1211 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance versus </src><tgt>重要性</tgt>` | 1061 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1419 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt>バリアントデータベースの</tgt>` | 756 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt>バリアントデータベースが</tgt>` | 1850 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt>私の一番好きなものの一つです。</tgt>` | 2131 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>つまり、</tgt>` | 1788 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree </src><tgt>もし</tgt>` | 1346 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that </src><tgt><\|wait\|></tgt>` | 1143 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>need to be in these </src><tgt><\|wait\|></tgt>` | 624 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 986 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 616 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt>これらのデータソースに必要となるフィールドについて意見が合わないなら、それらは私たちが利用できるものだよね？</tgt>` | 908 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 304 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1130 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 787 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>individual right, </src><tgt>个人权利</tgt>` | 1158 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1201 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt>最后才出现，</tgt>` | 1267 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I I I don't I don't </src><tgt>不是领导者。我</tgt>` | 1983 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>have the courts want to be </src><tgt><\|wait\|></tgt>` | 1346 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1768 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of social change </src><tgt><\|wait\|></tgt>` | 1641 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 647 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>these days. </src><tgt>不希望法院成为社会变革的先锋。</tgt>` | 2142 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1703 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1384 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt>但他们更倾向于反映</tgt>` | 1228 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 1114 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged </src><tgt>已经形成的共识。</tgt>` | 789 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so. </src><tgt>所以。</tgt>` | 528 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 355 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 424 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 354 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 374 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>그럼</tgt>` | 958 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt>그림을 한번 볼까요?</tgt>` | 1372 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>图片</src><tgt><\|wait\|></tgt>` | 859 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>的部分呢，我们可以看到</src><tgt>그림 부분에서는</tgt>` | 1151 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>一个是</src><tgt><\|wait\|></tgt>` | 1470 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>克汀的部分，</src><tgt>크틴 부분도 보일 수 있어요.</tgt>` | 2050 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>而克汀</src><tgt><\|wait\|></tgt>` | 972 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>一般是属于</src><tgt>크틴은 보통</tgt>` | 1691 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1875 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>在修饰的地方，</src><tgt>수정하는 부분에 속하죠.</tgt>` | 1863 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt>그러니까</tgt>` | 1270 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分</src><tgt><\|wait\|></tgt>` | 1046 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>呢，会反映的是</src><tgt>이건 신체 부분인데,</tgt>` | 1670 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>我们需要给</src><tgt><\|wait\|></tgt>` | 927 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1109 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地</src><tgt>우리 스스로</tgt>` | 778 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>做一下来修习</src><tgt><\|wait\|></tgt>` | 723 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可我们看到</src><tgt>시간을 좀 갖고 수련해야 해요.</tgt>` | 481 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>这边是包含五一人的嘛。</src><tgt>여기에는 51인도 포함되어 있어요.</tgt>` | 433 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>자, 그럼</tgt>` | 370 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>所以是说</src><tgt><\|wait\|></tgt>` | 346 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>この人たちは</tgt>` | 827 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>全く珍しい</tgt>` | 1127 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>もので、</tgt>` | 1085 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt>よく</tgt>` | 919 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize </src><tgt>完全に</tgt>` | 698 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>the world. </src><tgt>世界をひっくり返すんです。</tgt>` | 1582 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1201 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>personality is </src><tgt>その個性は</tgt>` | 985 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾したものです。</tgt>` | 1773 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 503 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt>彼らは</tgt>` | 1727 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的ですが、</tgt>` | 2185 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt>無意味な</tgt>` | 1755 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>conversations, </src><tgt>会話も嫌います。</tgt>` | 1530 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src>and like to </src><tgt>そして</tgt>` | 1020 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt>すぐに</tgt>` | 1135 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>point. </src><tgt>本題に入ります。</tgt>` | 768 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love </src><tgt>彼らは</tgt>` | 595 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>to play the devil's advocate </src><tgt>また、</tgt>` | 394 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>and they </src><tgt>逆張りをして、</tgt>` | 404 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt>決して</tgt>` | 335 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate </src><tgt>議論から逃げません。</tgt>` | 426 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 351 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and CP stands </src><tgt>CPは</tgt>` | 319 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>for. </src><tgt>それを支持しています。</tgt>` | 306 |

---

### Test Example 58 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 의 이전 </src><tgt><\|wait\|></tgt>` | 865 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>성공 을 거부 한 </src><tgt>The previous one</tgt>` | 1267 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후부 를 </src><tgt><\|wait\|></tgt>` | 1425 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt>was based on the justification of the previous one, and</tgt>` | 1415 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후부의 당수를 </src><tgt><\|wait\|></tgt>` | 1190 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 하면서 </src><tgt>while also</tgt>` | 1303 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색 까지 </src><tgt><\|wait\|></tgt>` | 1113 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제는 </src><tgt>presenting the previous one's number, I also made a show of it, but now</tgt>` | 2049 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤성률 후보 가 </src><tgt><\|wait\|></tgt>` | 1873 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정은을 </src><tgt>candidate Yoon Sung-ryul</tgt>` | 2099 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제관 순간 </src><tgt><\|wait\|></tgt>` | 1794 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석 은 들은 에 놓고 </src><tgt>was listening to Kim Jong-un</tgt>` | 2213 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤성률 후보 </src><tgt><\|wait\|></tgt>` | 529 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt>and was about to drop candidate Yoon Sung-ryul</tgt>` | 1496 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 </src><tgt><\|wait\|></tgt>` | 749 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>품은 공격 성을 </src><tgt>with a hat, attacking</tgt>` | 444 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 436 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>the attack, he was determined to</tgt>` | 371 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>것입니다. </src><tgt>do it.</tgt>` | 342 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가 신발 </src><tgt><\|wait\|></tgt>` | 358 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 성상 납권 </src><tgt>The shoe of Lee Jun-seok</tgt>` | 484 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 249 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt>was a political scandal.</tgt>` | 313 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt><\|wait\|></tgt>` | 264 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 됩니까? </src><tgt>How much of a positive factor is the Democratic Party's attack?</tgt>` | 482 |

---

### Test Example 59 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt>Well, right now after dinner,</tgt>` | 1238 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt>I want to make something.</tgt>` | 1545 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt>So,</tgt>` | 719 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1475 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスローンホテル</src><tgt>this Golf Sloan Hotel</tgt>` | 1680 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>で朝食が</src><tgt><\|wait\|></tgt>` | 1073 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所になってる</src><tgt>is a place where you can have breakfast,</tgt>` | 1893 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってる</src><tgt>and it's scheduled for</tgt>` | 1881 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので今後ね</src><tgt>so going forward,</tgt>` | 1748 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt>this Golf Sloan Hotel</tgt>` | 1226 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>I want to stay,</tgt>` | 1171 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt>so if you're thinking about staying here,</tgt>` | 1807 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt>please consider</tgt>` | 787 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみてまあいいんじゃない</src><tgt>it looks good,</tgt>` | 1139 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt>and so on.</tgt>` | 749 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>はい思います。</src><tgt>Yes, I think so.</tgt>` | 684 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt>From this hotel,</tgt>` | 415 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt>Busan Station is also</tgt>` | 329 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>just a walk away,</tgt>` | 268 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかるか</src><tgt>it takes about a minute</tgt>` | 377 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かからないか</src><tgt>or maybe it does,</tgt>` | 362 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt>that level of</tgt>` | 332 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のねまあホテル</src><tgt>location, well, this hotel</tgt>` | 334 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt>is good,</tgt>` | 293 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>so if you'd like,</tgt>` | 314 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>please consider it.</tgt>` | 346 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それでは</src><tgt>That's all for now.</tgt>` | 286 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は</src><tgt>For this time,</tgt>` | 252 |

---

### Test Example 60 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>아 저는 </src><tgt>I'm</tgt>` | 987 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>영심이 </src><tgt><\|wait\|></tgt>` | 1140 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>칼 </src><tgt><\|wait\|></tgt>` | 981 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>영심이 </src><tgt><\|wait\|></tgt>` | 1193 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소` | 12322 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소` | 6571 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소` | 2645 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소소` | 1517 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt>really, this is</tgt>` | 164 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>행동으로 </src><tgt><\|wait\|></tgt>` | 158 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 죽입니다. </src><tgt>killing me with action.</tgt>` | 195 |
