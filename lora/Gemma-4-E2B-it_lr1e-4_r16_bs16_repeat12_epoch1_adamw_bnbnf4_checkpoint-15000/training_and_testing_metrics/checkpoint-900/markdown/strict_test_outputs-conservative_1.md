# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9977
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9526
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.3667
  - SRC_WAIT_TOTAL: 150
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 681
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 0.9545
  - TGT_RELEASE_TOTAL: 88
  - TGT_WAIT_ACCURACY: 0.9694
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1316.9260
  - PROCESS_TIME_MS_P50: 1310.3860
  - PROCESS_TIME_MS_P95: 2016.5490
  - PROCESS_TIME_MS_MAX: 12626.2800

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>做的是</src><tgt>Parents need to</tgt>` | 849 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1208 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>深沉的爱交</src><tgt>use our deep love</tgt>` | 1492 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>使</src><tgt>to make</tgt>` | 775 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>Kids</src><tgt><\|wait\|></tgt>` | 1015 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心里营养。</src><tgt>their hearts nourished.</tgt>` | 1541 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 965 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>细腻心，</src><tgt>Their hearts become tender,</tgt>` | 1451 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>等孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 1885 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>外在</src><tgt><\|wait\|></tgt>` | 1363 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>的总结点，</src><tgt>The external summary point is:</tgt>` | 915 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优势</src><tgt><\|wait\|></tgt>` | 1326 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src>很大，然后</src><tgt>the advantage is huge. Then</tgt>` | 1245 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1424 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在面对</src><tgt>I face</tgt>` | 1166 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和贪人，</src><tgt><\|wait\|></tgt>` | 1053 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1379 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>这个点，</src><tgt>this point—</tgt>` | 1743 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种贪人</src><tgt><\|wait\|></tgt>` | 1787 |
| 11 | `<src>仁儿。</src><tgt>this kind of walnut kernels.</tgt>` | `<src>呢。</src><tgt>this greed.</tgt>` | 699 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1105 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气数是容易的，</src><tgt>気数をつけるのは簡単です。</tgt>` | 1225 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>但是只有</src><tgt>ただ、</tgt>` | 957 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅值得</src><tgt><\|wait\|></tgt>` | 1481 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1214 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>鲁和除于中年。</src><tgt>中年以外は、</tgt>` | 1109 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1253 |
| 9 | `<src>虚阿凡</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>反省が必要になります。</tgt>` | 1780 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1799 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅，</src><tgt>師匠になるには、</tgt>` | 1043 |

---

### Test Example 4 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这附近</tgt>` | 898 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まったもので</src><tgt><\|wait\|></tgt>` | 1203 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src><\|wait\|></src><tgt>开始的，</tgt>` | 1434 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>五減</src><tgt>五减</tgt>` | 792 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1248 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>細山</src><tgt>细山</tgt>` | 1542 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1792 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>などという人の</src><tgt><\|wait\|></tgt>` | 580 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵、</src><tgt><\|wait\|></tgt>` | 1765 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1404 |

---

### Test Example 5 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 831 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat learn </src><tgt><\|wait\|></tgt>` | 1034 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>and then repeat </src><tgt>重复学习，</tgt>` | 1406 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by finding where you're good at. </src><tgt><\|wait\|></tgt>` | 1381 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>And do more of it </src><tgt>然后找到自己擅长的部分，多做一些。</tgt>` | 1583 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1146 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>good at, get to people </src><tgt>当你不擅长的时候，</tgt>` | 1487 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1842 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>多找身边的人帮忙，</tgt>` | 1942 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>and in tell the next time </src><tgt><\|wait\|></tgt>` | 1565 |

---

### Test Example 6 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 855 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 740 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲までまだ</src><tgt><\|wait\|></tgt>` | 1197 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>因为仲还没到一年级。</tgt>` | 1512 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1456 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう</src><tgt>在这个阶段，</tgt>` | 1296 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>四角線で</src><tgt><\|wait\|></tgt>` | 992 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数</src><tgt>我们用四角线</tgt>` | 1414 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>していってあげると</src><tgt><\|wait\|></tgt>` | 1831 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt>做对数运算，就算过了十年，</tgt>` | 2063 |
| 11 | `<src>大した。</src><tgt>十年后也不会有什么大……</tgt>` | `<src>対数だ。</src><tgt><\|wait\|></tgt>` | 1559 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1149 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘撒完以后呢，</src><tgt>淘撒が終わった後、</tgt>` | 1028 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的液体</src><tgt><\|wait\|></tgt>` | 1445 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>减轻，能量也</src><tgt>内部の液体が減り、エネルギーも</tgt>` | 1767 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>稍弱了，然后就</src><tgt><\|wait\|></tgt>` | 1057 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>停留在</src><tgt>少し弱くなり、</tgt>` | 1396 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1595 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的运行状态</src><tgt>比較的低エネルギーの</tgt>` | 1895 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>态。</src><tgt><\|wait\|></tgt>` | 809 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>運行状態に留まります。これが</tgt>` | 1667 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>一个异于</src><tgt><\|wait\|></tgt>` | 2097 |

---

### Test Example 8 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 들의 </src><tgt>The other advanced nations</tgt>` | 930 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주변 들에게 </src><tgt><\|wait\|></tgt>` | 1430 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>주기 는 내가 주길 수 도록 </src><tgt>can give them</tgt>` | 1443 |
| 5 | `<src>다른 잔찜에 </src><tgt>came in here to do it.</tgt>` | `<src>다닌 </src><tgt><\|wait\|></tgt>` | 1292 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>잠시 들의 주도 달하 자 </src><tgt>the lead in the other advanced nations</tgt>` | 1887 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>나는 </src><tgt><\|wait\|></tgt>` | 1457 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 </src><tgt>to be able to give them a little lead.</tgt>` | 1935 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>안 듣고 있는 줄은 알았느냐? </src><tgt><\|wait\|></tgt>` | 2004 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>어? </src><tgt>Did you not hear that? Huh?</tgt>` | 1354 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1252 |

---

### Test Example 9 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 일어 지 </src><tgt><\|wait\|></tgt>` | 1388 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>너무 </src><tgt>これ、</tgt>` | 436 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>좋아요, </src><tgt><\|wait\|></tgt>` | 1198 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>일 수 있지만 진짜 </src><tgt>すごくいいんですけど、</tgt>` | 1466 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>보살 들도 아니 </src><tgt><\|wait\|></tgt>` | 1536 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 의 보살 인데 꿈일 </src><tgt>本当に菩薩たちなんですけど、</tgt>` | 1797 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>풀어주고 나만 </src><tgt><\|wait\|></tgt>` | 1663 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>이 보살 로 </src><tgt>夢を解いてくれて、私だけ</tgt>` | 1869 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보일 필요 없고 우주 가 </src><tgt><\|wait\|></tgt>` | 1902 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>지단 때 보살 이란 </src><tgt>この菩薩に会う必要なくて、宇宙が</tgt>` | 1462 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1285 |

---

### Test Example 10 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 731 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt>제가</tgt>` | 767 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 986 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>鬼道哦，</src><tgt>귀도에서 살게 해 주세요.</tgt>` | 1580 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1061 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>保持它下山的时候，</src><tgt>산에서</tgt>` | 983 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在座日</src><tgt><\|wait\|></tgt>` | 1440 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>踏入</src><tgt>머무를 수 있게 해 주세요.</tgt>` | 1790 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>这个月，我当时</src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>被他</src><tgt>이달에</tgt>` | 1800 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>做一些小小的愿望哦，</src><tgt><\|wait\|></tgt>` | 1145 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src><\|wait\|></src><tgt>작은 소원들을</tgt>` | 1708 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 941 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt>重要な研究を</tgt>` | 757 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1174 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people? This is </src><tgt>極度に幸せな人たちについて調べたことはありますか？</tgt>` | 2328 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 935 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. </src><tgt>これは研究の入り口です。</tgt>` | 1549 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>最も幸せな人々の10%を見てみましょう。</tgt>` | 2030 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1702 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People that </src><tgt>彼らは外の世界にいます。彼らは</tgt>` | 1246 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1617 |

---

### Test Example 12 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>용신이 </src><tgt>I'm a Yongsin,</tgt>` | 965 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1394 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용신이 </src><tgt><\|wait\|></tgt>` | 1188 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 용신이 가 </src><tgt><\|wait\|></tgt>` | 1569 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1563 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>석연은 건데요. </src><tgt>and the sword Yongsin is a bit awkward. It's a bit of a dilemma.</tgt>` | 2124 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1705 |
| 9 | `<src>진짜 이거 </src><tgt>Man, this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1725 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>혜경으로도 </src><tgt>Seriously, even with Hye-gyeong,</tgt>` | 1181 |
| 11 | `<src>진짜. </src><tgt>seriously killer for a hangover, for real.</tgt>` | `<src>조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 1695 |

---

### Test Example 13 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 953 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>body saying? </src><tgt>你的身体在说什么？</tgt>` | 798 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1756 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt>把图钉钉在你的身体上。</tgt>` | 1240 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1099 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? Is it </src><tgt>紧张感从哪里开始？是什么？</tgt>` | 1855 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>a daycare? </src><tgt><\|wait\|></tgt>` | 1618 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it tightening in your chest? </src><tgt>是幼儿园吗？是在胸口收紧吗？</tgt>` | 2154 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it </src><tgt><\|wait\|></tgt>` | 1844 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>a blanket that you use </src><tgt>还是你用的毯子</tgt>` | 1970 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>saying? </src><tgt><\|wait\|></tgt>` | 560 |

---

### Test Example 14 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1102 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt>T-shirts and</tgt>` | 836 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1026 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただくようなものも</src><tgt>other items like that</tgt>` | 1523 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので、ぜひ</src><tgt><\|wait\|></tgt>` | 1223 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt>are available, so please feel free to join us.</tgt>` | 1579 |
| 7 | `<src>ご連絡としては</src><tgt>so please be sure to join us.</tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 890 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt>That concludes my message.</tgt>` | 1552 |
| 9 | `<src>えっと</src><tgt>That's all for the announcements,</tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1748 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>何しろ</src><tgt>Anyway,</tgt>` | 1198 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>何しろ内側がありますので、</src><tgt><\|wait\|></tgt>` | 1314 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt>please wait a moment. There's a little bit of a delay.</tgt>` | 2349 |

---

### Test Example 15 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为</src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>这个情况，我们就是</src><tgt>Because of this situation,</tgt>` | 956 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1504 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就感谢了</src><tgt>when we encounter problems,</tgt>` | 1135 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回报主管或是通知对方</src><tgt><\|wait\|></tgt>` | 1513 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我说</src><tgt>we thank our supervisors or notify them</tgt>` | 1696 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>这个状况，不要想</src><tgt><\|wait\|></tgt>` | 1771 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>自己什么都把它</src><tgt>that we'll do everything</tgt>` | 1990 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>扛下来，</src><tgt><\|wait\|></tgt>` | 1837 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>工具理承担，</src><tgt>and bear the burden ourselves. Tools and Li will take responsibility,</tgt>` | 1754 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>责任是给属人。</src><tgt><\|wait\|></tgt>` | 1025 |

---

### Test Example 16 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 </src><tgt><\|wait\|></tgt>` | 1134 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>있는 식성 들은 </src><tgt>Those with a specific diet on the list</tgt>` | 1154 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1484 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>실제로 지능 이 높지 </src><tgt>actually have high intelligence</tgt>` | 1440 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1089 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>않고 무작위 로 </src><tgt>and are not</tgt>` | 1720 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>뽑힌 식성 들이었기 </src><tgt><\|wait\|></tgt>` | 1873 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>때문 입니다. </src><tgt>selected randomly.</tgt>` | 1792 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1783 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 965 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>모을 랐던 교사 들은 </src><tgt>The teachers who collected the sashi</tgt>` | 1982 |

---

### Test Example 17 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 802 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt>If you're a female high school student</tgt>` | 1175 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不够的人之间</src><tgt><\|wait\|></tgt>` | 1729 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有这么重要</src><tgt><\|wait\|></tgt>` | 781 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>的人际？</src><tgt>and you have to care about people who aren't physically attractive?</tgt>` | 1777 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道</src><tgt><\|wait\|></tgt>` | 1250 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>会是</src><tgt>Is it really</tgt>` | 1518 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天而异</src><tgt><\|wait\|></tgt>` | 959 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>going to be a change from heaven to earth?</tgt>` | 1568 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1853 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1438 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>学历年偏。</src><tgt>Yang Zisi's academic background is quite high.</tgt>` | 1208 |

---

### Test Example 18 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1148 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>ちょっと距離が離れてくる</src><tgt>Advantageさん，</tgt>` | 1000 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1182 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>大社が</src><tgt>感觉有点像距离拉开，</tgt>` | 1451 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>あるぽいですね。</src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>回避したい方って</src><tgt>大社好像挺想躲开的。</tgt>` | 1750 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐに行こう</src><tgt><\|wait\|></tgt>` | 1522 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>しきだから</src><tgt>所以</tgt>` | 1532 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>じいずで見て</src><tgt><\|wait\|></tgt>` | 855 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と本筋に</src><tgt>大家</tgt>` | 1806 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>おとを調べることが</src><tgt><\|wait\|></tgt>` | 1399 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>強るので、なので</src><tgt>会看Jizuzu，能查到本筋的音，所以</tgt>` | 1449 |

---

### Test Example 19 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1436 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>and then after </src><tgt>好的，然后</tgt>` | 706 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1307 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | 1306 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1480 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1508 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 779 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually. </src><tgt>实际操作是</tgt>` | 1281 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1743 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>使用这些值。</tgt>` | 1411 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 950 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>So this game.coord array </src><tgt>所以这个 game.coord 数组</tgt>` | 2229 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1371 |

---

### Test Example 20 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 882 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>Aが</src><tgt>So, A</tgt>` | 799 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あるんですね。いろんな場面で</src><tgt><\|wait\|></tgt>` | 1247 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>生食かどうかっていう</src><tgt>is there. In various situations,</tgt>` | 1594 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>場合でいう時に、</src><tgt><\|wait\|></tgt>` | 1467 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>Aの欄を</src><tgt><\|wait\|></tgt>` | 1604 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうかっていう</src><tgt><\|wait\|></tgt>` | 956 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>調査する生食で</src><tgt><\|wait\|></tgt>` | 1470 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>いうことを保証する</src><tgt><\|wait\|></tgt>` | 1886 |
| 11 | `<src>といったような</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1292 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>they've made it so that you can check the A column to see if it's raw or not, and then they guarantee that it's raw by providing a raw food investigation.</tgt>` | 2500 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 1009 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこ</src><tgt>자, 여기</tgt>` | 695 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1053 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>think to set up 7.8GB </src><tgt>7.8GB를</tgt>` | 1665 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>가 </src><tgt><\|wait\|></tgt>` | 1364 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>되셨다네. </src><tgt>설정해 두셨네요.</tgt>` | 1286 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 965 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>ハセイエヨシの</src><tgt>하세이 요시의</tgt>` | 1686 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>仕組みは</src><tgt><\|wait\|></tgt>` | 1686 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>もうコン、</src><tgt>구조는</tgt>` | 1724 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 944 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>7.8GB </src><tgt>7.8GB</tgt>` | 1854 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 1439 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 877 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1033 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>緩むと</src><tgt>기어가 느슨해지면</tgt>` | 1571 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えが</src><tgt><\|wait\|></tgt>` | 1208 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>신호가 꺼져서</tgt>` | 1530 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 844 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>逆ネジの</src><tgt>기어 끝에 역나사</tgt>` | 1833 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1689 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いているっていうこと</src><tgt>너트가 붙어있게 되는데,</tgt>` | 2002 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1225 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>네, 맞습니다.</tgt>` | 1310 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>分解完了を</src><tgt><\|wait\|></tgt>` | 1538 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1158 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Chunah Terug, </src><tgt>제 이름은 츄나 테루입니다.</tgt>` | 1194 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1361 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 861 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>in international business finance </src><tgt>현재 국제 비즈니스 재무를</tgt>` | 1587 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a major of psychology. </src><tgt><\|wait\|></tgt>` | 1613 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>전공하고 있습니다. 심리학도 전공하고 있고요.</tgt>` | 1969 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yaenju, </src><tgt><\|wait\|></tgt>` | 1857 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt>여기 야엔주에</tgt>` | 1936 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 2063 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt>미래에는</tgt>` | 453 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1582 |

---

### Test Example 24 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 1169 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt>These things, like vanadium,</tgt>` | 787 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실률인가 </src><tgt><\|wait\|></tgt>` | 1819 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 거진 </src><tgt><\|wait\|></tgt>` | 881 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사한 그런 기능 이 </src><tgt><\|wait\|></tgt>` | 1392 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>나올 정도 로 굉장히 </src><tgt><\|wait\|></tgt>` | 1642 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1567 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다 </src><tgt><\|wait\|></tgt>` | 1936 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이리 가 </src><tgt><\|wait\|></tgt>` | 1403 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>될 정도 로 </src><tgt><\|wait\|></tgt>` | 952 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1667 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 845 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1587 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 919 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是指</src><tgt>2つ目は、</tgt>` | 849 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二期市场，</src><tgt><\|wait\|></tgt>` | 1180 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>还包括</src><tgt>2期市場を指します。これには</tgt>` | 1524 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一期一线</src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们，</src><tgt>1期の一線で戦う大牛たちも含まれます。</tgt>` | 1790 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1502 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做</src><tgt>例えば、</tgt>` | 935 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>微信运动好几年，</src><tgt><\|wait\|></tgt>` | 1491 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>微信運動を何年も続けていると、</tgt>` | 1969 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信运动</src><tgt><\|wait\|></tgt>` | 1978 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平分的星棒</src><tgt>微信運動の星棒が</tgt>` | 573 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1574 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of the </src><tgt>19세기</tgt>` | 903 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>nineteenth amendment, </src><tgt><\|wait\|></tgt>` | 1182 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore </src><tgt>수정안의 의미와</tgt>` | 1505 |
| 5 | `<src>history as a guide </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1546 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help </src><tgt>역사를 탐구하고, 그것이</tgt>` | 1666 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1531 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>정치적 변화를 돕는 지침이 될 수 있는</tgt>` | 1917 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 572 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt>미국에서 어떻게</tgt>` | 1828 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1664 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of course I'm </src><tgt>정치적 변화를 일으킬 수 있는지 살펴보는 것입니다. 물론</tgt>` | 1235 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Maryed. </src><tgt><\|wait\|></tgt>` | 1366 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 743 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼</tgt>` | 885 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1217 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those </src><tgt>화학 결합도 에너지를 저장해요. 그리고</tgt>` | 1920 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1251 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt>결합이 끊어지면</tgt>` | 1724 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1611 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>converted to other types of energy, </src><tgt>그 잠재 에너지는 다른 종류의 에너지로</tgt>` | 2063 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 1965 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>변환돼요. 예를 들어 열이나 빛 같은 거죠. 아니면</tgt>` | 2276 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds </src><tgt><\|wait\|></tgt>` | 885 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>다른 결합을 만드는 데 사용되기도 하고요.</tgt>` | 1489 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1375 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 459 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1226 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何か書いたり、テキストを書いたりする場合、</tgt>` | 1582 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1412 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>全く</tgt>` | 1655 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1552 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>because like oh, </src><tgt>スペルがわからないと気づくことがあるかもしれません。例えば、「あ、</tgt>` | 2017 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>is this word </src><tgt><\|wait\|></tgt>` | 1310 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>start with a double </src><tgt>この単語は</tgt>` | 1127 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>p, </src><tgt><\|wait\|></tgt>` | 2074 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l, I don't know </src><tgt>「pが二つ、lが二つ」って、</tgt>` | 1555 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1000 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1358 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在</src><tgt>皆さんにお伝えしたいのは、</tgt>` | 715 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>这个罗马呢，</src><tgt><\|wait\|></tgt>` | 1548 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是以前造成的，</src><tgt>このローマは以前から</tgt>` | 1111 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1409 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>作られたものではないんです。だから、</tgt>` | 1713 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所念你的一些</src><tgt><\|wait\|></tgt>` | 1547 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>网页啊</src><tgt>今あなたが</tgt>` | 1437 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟粉丝</src><tgt><\|wait\|></tgt>` | 786 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是</src><tgt>ウェブサイトやファンと</tgt>` | 1868 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就</src><tgt><\|wait\|></tgt>` | 1167 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的</src><tgt>交流が生まれたわけではないんです。</tgt>` | 1502 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1590 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>我的朋友呢，</src><tgt>ですから、私の友人には、</tgt>` | 1252 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1069 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then,</tgt>` | 864 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无波澜，</src><tgt><\|wait\|></tgt>` | 1486 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>so there was no ripple,</tgt>` | 1087 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不懈的</src><tgt><\|wait\|></tgt>` | 1539 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>开到七千八百</src><tgt><\|wait\|></tgt>` | 1670 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>世人</src><tgt><\|wait\|></tgt>` | 1516 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>一生来审断，</src><tgt><\|wait\|></tgt>` | 1085 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 1255 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下打腿，</src><tgt><\|wait\|></tgt>` | 1881 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>so they persisted, opening it to 7,800,000, and judged it for a lifetime. They kept pounding it, and it was fine.</tgt>` | 2614 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们呢</src><tgt><\|wait\|></tgt>` | 1596 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>都很疑惑的离开。</src><tgt>They, however, all left with confusion.</tgt>` | 1345 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 986 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>欠钱头，</src><tgt>彼は借金まみれになって、</tgt>` | 950 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1280 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>得到了欠钱头之后，</src><tgt>その借金まみれになったら、</tgt>` | 1785 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 938 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>就要先</src><tgt>必ず</tgt>` | 1487 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>守住，</src><tgt><\|wait\|></tgt>` | 1461 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想着</src><tgt>守り通すこと。そして</tgt>` | 665 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>哎，那我在去</src><tgt><\|wait\|></tgt>` | 1807 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>操作下去哦。</src><tgt>操作を続けようと思わないでください。</tgt>` | 2073 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1790 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt>なぜなら、</tgt>` | 623 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt><\|wait\|></tgt>` | 1778 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>そう言うのはなぜか？だって、</tgt>` | 1208 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>这章的部分，我们看到的是</src><tgt>이 장의 부분은</tgt>` | 952 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1399 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>个戴雪的人，但是</src><tgt>다이쉐라는 사람을 보는데,</tgt>` | 1780 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于逆向的。</src><tgt><\|wait\|></tgt>` | 1025 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>그는 역방향에 속합니다.</tgt>` | 1547 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这同样好像</src><tgt><\|wait\|></tgt>` | 1583 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>这样一个状况</src><tgt>이 상황도</tgt>` | 1774 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>需要去特别注意</src><tgt><\|wait\|></tgt>` | 728 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是，他能不能</src><tgt>특별히 주의해야 할 점은</tgt>` | 1820 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2033 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>得到与他</src><tgt>그가</tgt>` | 1381 |
| 13 | `<src><\|wait\|></src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>的意事</src><tgt><\|wait\|></tgt>` | 1095 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>哦。</src><tgt>그의 의사를 얻을 수 있는지 여부입니다.</tgt>` | 1193 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1051 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src>there </src><tgt>没什么新意，</tgt>` | 751 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1253 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>was such interfaces before. </src><tgt>以前也有过这样的接口。</tgt>` | 1445 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1498 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>NetFutureTC, </src><tgt>NetFutureTC，</tgt>` | 1571 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1080 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src>and so this is just </src><tgt>所以这只是</tgt>` | 1106 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1736 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>one another place to look at </src><tgt>另一个地方</tgt>` | 1905 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1281 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>what </src><tgt><\|wait\|></tgt>` | 1284 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1501 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>would like to </src><tgt><\|wait\|></tgt>` | 900 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>look at. </src><tgt>让开发者或工程师去看看。</tgt>` | 1240 |

---

### Test Example 34 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1219 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>is just getting going </src><tgt>まさに今、</tgt>` | 864 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1380 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>やる気を出そうとしている人、</tgt>` | 1295 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and that ten of them </src><tgt><\|wait\|></tgt>` | 1459 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that you're really </src><tgt>その10人</tgt>` | 1704 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1495 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>は本当に重要です。</tgt>` | 1133 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go and do </src><tgt><\|wait\|></tgt>` | 1311 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I have about </src><tgt>これから</tgt>` | 1744 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1313 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video. </src><tgt>この動画の続きを1分程度の動画を撮ります。</tgt>` | 1538 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 1482 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>each one </src><tgt>それぞれの動画で</tgt>` | 1007 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 831 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>H.T.M.L. </src><tgt>HTML</tgt>` | 840 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1290 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴퓨터 도 </src><tgt>计算机</tgt>` | 1143 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1511 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>也能理解，</tgt>` | 1301 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1023 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 의 언어 에 </src><tgt>人类也能理解计算机的语言，</tgt>` | 1557 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1699 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 말께 </src><tgt>就像</tgt>` | 1861 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리 가 이제 것들을 </src><tgt><\|wait\|></tgt>` | 1358 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们现在要写出这些东西，</tgt>` | 1445 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것들을 </src><tgt><\|wait\|></tgt>` | 1565 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>编写这些东西的程序</tgt>` | 1217 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1085 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 994 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>150만 개가 </src><tgt>そのうち150万個が</tgt>` | 1111 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중요 본서 </src><tgt><\|wait\|></tgt>` | 1358 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>1000억 원 기업 들이 </src><tgt>1000億円規模の企業で、</tgt>` | 1875 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1007 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多いです。一般的には</tgt>` | 1334 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>자건 업계 들은 </src><tgt><\|wait\|></tgt>` | 1712 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>財政業界は成長するか、あるいは</tgt>` | 2122 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>해화법이 그닥 되는데 </src><tgt><\|wait\|></tgt>` | 2041 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>일본 에 상기 업계 들은 </src><tgt>海運法がなかなか通らない中で、日本の</tgt>` | 2321 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1595 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>폐업 도 하지 않는 </src><tgt>財政業界も成長も倒産もしていない</tgt>` | 1368 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들을 보이기 된 거죠. </src><tgt><\|wait\|></tgt>` | 1170 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1261 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt>12手</tgt>` | 735 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>あったら</src><tgt><\|wait\|></tgt>` | 1267 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>恐らく10秒で</src><tgt>大概10秒</tgt>` | 1370 |
| 5 | `<src>まあ</src><tgt>差不多十秒。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1481 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ1秒に</src><tgt>内，</tgt>` | 1589 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1130 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間</src><tgt>大概1秒</tgt>` | 785 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>なんですかね。</src><tgt><\|wait\|></tgt>` | 1898 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt>左右，</tgt>` | 1735 |
| 11 | `<src>おそらく</src><tgt>然后</tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 958 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>12手</src><tgt>大概12手</tgt>` | 1829 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>であの</src><tgt><\|wait\|></tgt>` | 1411 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>左右，</tgt>` | 971 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1190 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから</src><tgt>所以，</tgt>` | 652 |

---

### Test Example 38 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1338 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个财运可以说是</src><tgt>財運についてですが、</tgt>` | 725 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不落的，但是</src><tgt><\|wait\|></tgt>` | 1646 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财的部分。</src><tgt>まだ十分ではないですが、正財の側面が強いと言えます。</tgt>` | 1813 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 811 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面的</src><tgt>つまり、</tgt>` | 1337 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长所带来的</src><tgt><\|wait\|></tgt>` | 1550 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>红利，</src><tgt>事業の業績向上による利益、</tgt>` | 1497 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>也就是收入的提升，</src><tgt><\|wait\|></tgt>` | 937 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>如果是在投资理财方面</src><tgt>つまり収入の増加です。投資や資産運用に関しては、</tgt>` | 2310 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1883 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>今月も良いですが、</tgt>` | 1596 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说就</src><tgt><\|wait\|></tgt>` | 900 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>稍微弱了那么一点</src><tgt>少し弱くなっている</tgt>` | 1155 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 680 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알 거니 뭐? </src><tgt>あなたたちも知っているでしょう？</tgt>` | 987 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인 으로 </src><tgt><\|wait\|></tgt>` | 1699 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt>異邦人として</tgt>` | 1018 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1173 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>우상 에게로 </src><tgt>言葉を失い、</tgt>` | 1712 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>가든지 </src><tgt><\|wait\|></tgt>` | 1545 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>그대로 </src><tgt>偶像に</tgt>` | 1641 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>걸려 갔느니라. </src><tgt><\|wait\|></tgt>` | 754 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그럼 으로 내가 </src><tgt>そのまま行かれてしまう。そうすれば、</tgt>` | 2088 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 2066 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに知らせる。それは</tgt>` | 1616 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt><\|wait\|></tgt>` | 989 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>神の霊によって語る者は、</tgt>` | 1157 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 659 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1160 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>세모라 </src><tgt>目を閉じて、</tgt>` | 876 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1072 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>이게 </src><tgt>セモラを</tgt>` | 1351 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>소름이 돋은 차리 돋은 </src><tgt><\|wait\|></tgt>` | 1453 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 온이야. </src><tgt>感じてみて。鳥肌が立つような感覚が</tgt>` | 1567 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 </src><tgt><\|wait\|></tgt>` | 958 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>흔들어서 같이 놀자는 거야. </src><tgt>このものを揺らして一緒に遊ぼうっていうんだ。</tgt>` | 1893 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 1496 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>오면 올릴 거고 </src><tgt>お化けが来たら、</tgt>` | 2096 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>세모라 </src><tgt><\|wait\|></tgt>` | 2146 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>이온 이 오면 너 지켜 줄 거고 </src><tgt>セモラが</tgt>` | 1439 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>지랄 줘서 </src><tgt><\|wait\|></tgt>` | 1114 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>그러니까 편안 마음 에. </src><tgt>来たらお化けを追い払ってくれるから、安心して。</tgt>` | 1447 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 672 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1079 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>濡らせてやれ、</src><tgt>그럼 그냥 흠뻑 젖게 해버려.</tgt>` | 1476 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1163 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>は</src><tgt>나는</tgt>` | 912 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き締めを見ている。</src><tgt><\|wait\|></tgt>` | 1465 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>단련을 보고 있는 거야.</tgt>` | 1204 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 958 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に</src><tgt>이제 한계는</tgt>` | 1493 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>超えている不滅の奇跡。</src><tgt><\|wait\|></tgt>` | 1993 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아득히 초월한 불멸의 기적이야.</tgt>` | 2163 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 2064 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船出を</src><tgt>오랜 세월</tgt>` | 1426 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1070 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt>항해를 해왔지. 나는 이렇게</tgt>` | 1200 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊船を</src><tgt><\|wait\|></tgt>` | 649 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt>대단한 해적선을 본 적이 없어.</tgt>` | 924 |

---

### Test Example 42 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1174 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感知</src><tgt>相手の</tgt>` | 818 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1310 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的。</src><tgt>感情や真意を察知したり、</tgt>` | 1566 |
| 5 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1308 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1520 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1072 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt>人々がこう言っているのをよく聞きます。</tgt>` | 1191 |
| 9 | `<src>这样说：“</src><tgt>よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1695 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt>見てください。</tgt>` | 1780 |
| 11 | `<src>这个人</src><tgt>「ほら、</tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1160 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲黄了。</src><tgt>この人はまた黄連れになっているんです。</tgt>` | 1670 |
| 13 | `<src>他的眼睛</src><tgt>また嘘をついている。目が</tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1588 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt>彼の目は全てを物語っています。</tgt>` | 1213 |
| 15 | `<src><\|wait\|></src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1073 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt>つまり、</tgt>` | 645 |
| 17 | `<src><\|wait\|></src><tgt>つまり…</tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 396 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. How far </src><tgt>교육 수준. 얼마나</tgt>` | 980 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1485 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt>나아갔나요?</tgt>` | 1142 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? </src><tgt><\|wait\|></tgt>` | 1454 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt>교육 과정은 얼마나 나아갔나요? 고등학교를 졸업했나요?</tgt>` | 2073 |
| 7 | `<src><\|wait\|></src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt>그게 한 단계의 교육 수준입니다.</tgt>` | 2028 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1965 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, did you graduate </src><tgt>대학에 갔나요? 그래서</tgt>` | 2175 |
| 11 | `<src>That's another level of </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 1455 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment? </src><tgt>그게 또 다른 교육 수준인가요?</tgt>` | 1094 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1236 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt>지금은 여기까지입니다. 다음에 뵙겠습니다.</tgt>` | 987 |
| 15 | `<src>online. </src><tgt>오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 500 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1209 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 해매 미다. </src><tgt>进去的时候，会非常迷茫。</tgt>` | 1180 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1392 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt>因为之前开过车，</tgt>` | 1231 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1317 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt>所以走路的时候，</tgt>` | 1592 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1525 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt>去江南区，</tgt>` | 953 |
| 9 | `<src><\|wait\|></src><tgt>就不用说了，去外国</tgt>` | `<src>외국 에게 나가면 또 장렬 이요. </src><tgt><\|wait\|></tgt>` | 1630 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt>更别提去国外了，那简直就是一场灾难。</tgt>` | 2100 |
| 11 | `<src>좀 창피 하네요. </src><tgt>就更惨了。真有点丢人。</tgt>` | `<src>신기하 네요. </src><tgt><\|wait\|></tgt>` | 2010 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt>挺神奇的。反而</tgt>` | 1599 |
| 13 | `<src>이제 </src><tgt>不过，</tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 874 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>뭐라고 해봐요. </src><tgt>现在努力说些什么。</tgt>` | 1241 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 아닌 것 같아요. </src><tgt><\|wait\|></tgt>` | 848 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>我觉得那不是对的。</tgt>` | 772 |

---

### Test Example 45 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 1207 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인상 하는 </src><tgt>The stock market index</tgt>` | 714 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 </src><tgt><\|wait\|></tgt>` | 1441 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>보인 다면 </src><tgt>is showing an upward trend,</tgt>` | 1174 |
| 5 | `<src>큰 폭의 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1543 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 </src><tgt>and such a large- scale rise</tgt>` | 1728 |
| 7 | `<src>먼저 </src><tgt>will see significant gains.</tgt>` | `<src>하겠지만 </src><tgt><\|wait\|></tgt>` | 1531 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt>will occur, but first</tgt>` | 1858 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 종목 들이 </src><tgt><\|wait\|></tgt>` | 1230 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt>these variable stocks</tgt>` | 1174 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 2174 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt>will move the market first,</tgt>` | 1415 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시 총이 </src><tgt><\|wait\|></tgt>` | 1087 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 종목 을 </src><tgt>and the total liquidity of variable stocks</tgt>` | 1278 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 913 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src><\|wait\|></src><tgt>will be something to watch closely.</tgt>` | 708 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>けそ</src><tgt><\|wait\|></tgt>` | 1126 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 845 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1730 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースもあります。Aという人と</tgt>` | 1348 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1194 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 컨택 을 </src><tgt>Bという人が</tgt>` | 1628 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>한 듯한 </src><tgt><\|wait\|></tgt>` | 1522 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>컨설턴트 여기 고 </src><tgt>コンタクトを取ったような、</tgt>` | 1526 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 870 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aという人が悪意のあるコードを</tgt>` | 2168 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>들었을 때 </src><tgt><\|wait\|></tgt>` | 2069 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비란 사람이 </src><tgt>受け取ったとき、Bという人が</tgt>` | 1630 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 876 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로 사이트 스크립트 에서 </src><tgt>実際にクロスサイトスクリプトで</tgt>` | 1356 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>XSS 파일까지 </src><tgt><\|wait\|></tgt>` | 731 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까 </src><tgt>XSSファイルまで感染してしまうか</tgt>` | 854 |

---

### Test Example 47 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1167 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어, 어찌 보면 </src><tgt>嗯，从某种角度看，</tgt>` | 1098 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1814 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 773 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt>他就是我们20岁时一起长大的弟弟，</tgt>` | 1885 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그리고 가족 같은 </src><tgt><\|wait\|></tgt>` | 1235 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>也是我们家人一样的弟弟。</tgt>` | 1793 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src><\|wait\|></src><tgt>所以</tgt>` | `<src>어, </src><tgt>所以，</tgt>` | 1780 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인감모다는 </src><tgt><\|wait\|></tgt>` | 925 |
| 11 | `<src>조금 </src><tgt>比起责任感，</tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1868 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>서로 </src><tgt><\|wait\|></tgt>` | 1437 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1014 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 895 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 864 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt>我希望在再因感母的节目里，大家能多一些自我交流，</tgt>` | 1302 |

---

### Test Example 48 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1221 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>アクティビティ、それから</tgt>` | 863 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining </src><tgt><\|wait\|></tgt>` | 1488 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think the standard is, </src><tgt>自分自身で基準を定義するんです。なぜなら</tgt>` | 1878 |
| 5 | `<src>absolutely correct, </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。</tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1010 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt>あなたが完全に正しいから、</tgt>` | 1377 |
| 7 | `<src>is is that </src><tgt>しかし現実には、</tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1585 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>現実が</tgt>` | 1889 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the box, </src><tgt><\|wait\|></tgt>` | 1622 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed. </src><tgt>新しい箱の猫だからです。そして基準が変わったから。</tgt>` | 1233 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1768 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>From twenty years ago, </src><tgt>20年前に</tgt>` | 1631 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1161 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard </src><tgt>私たちは基準を</tgt>` | 682 |
| 15 | `<src>everything at this point is being </src><tgt>より高い基準を求められています。なぜなら、今はすべてが</tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 761 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher standard. </src><tgt>より高い基準に合わせられています。なぜなら、今のところすべてがより高い基準に合わせられているからです。</tgt>` | 1312 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1273 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>So, this is</tgt>` | 852 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうのが</src><tgt><\|wait\|></tgt>` | 1280 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>じゃなくて</src><tgt>not a visual development environment,</tgt>` | 1194 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1560 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt>it's a visual Python development environment.</tgt>` | 1736 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアル</src><tgt><\|wait\|></tgt>` | 1766 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>に書いてあるところは</src><tgt>The part written in the visual flow graph</tgt>` | 1937 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードが</src><tgt><\|wait\|></tgt>` | 1820 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されて、それが</src><tgt>is Python code that gets generated from there,</tgt>` | 1479 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1286 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>and that's how signal processing is performed.</tgt>` | 1892 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>構造になっているから</src><tgt><\|wait\|></tgt>` | 996 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt>That's why it's structured like this.</tgt>` | 1150 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 788 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay,</tgt>` | 551 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人々が</tgt>` | 922 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1896 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 763 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1426 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니 가 </src><tgt>ロクジャの分析を見ると、ソニーが</tgt>` | 1747 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>유력 6대 </src><tgt><\|wait\|></tgt>` | 1639 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FPP 파이프를 </src><tgt>有力な6大FPPパイプを</tgt>` | 1982 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1989 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>낮추 고서 로 </src><tgt>128ビットに下げて、</tgt>` | 1879 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>포인 다. </src><tgt><\|wait\|></tgt>` | 727 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 엑스에서도 </src><tgt>XboxシリーズのXboxでも</tgt>` | 1963 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>없는 </src><tgt><\|wait\|></tgt>` | 811 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt>インフィニットキャッシュが</tgt>` | 1175 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>L2가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 930 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>ありません。</tgt>` | 540 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1253 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, you will not </src><tgt>另外，</tgt>` | 732 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1383 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>media objects </src><tgt>你无法</tgt>` | 1137 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 1353 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>so if </src><tgt><\|wait\|></tgt>` | 851 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into the situation </src><tgt>所以如果你</tgt>` | 1625 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1866 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize you've added </src><tgt>发现你添加了</tgt>` | 1892 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1162 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 1505 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, we'll let us know. </src><tgt>错误的媒体文件到某个资源，我们会通知你。</tgt>` | 2161 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>And we can see about </src><tgt><\|wait\|></tgt>` | 851 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those media files </src><tgt>我们也可以</tgt>` | 1076 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 808 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>to get that up </src><tgt>检查一下这些媒体文件，确保</tgt>` | 638 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 483 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>for all the sorts </src><tgt>모든 종류의</tgt>` | 792 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>that we've just discussed, </src><tgt><\|wait\|></tgt>` | 1888 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>but then we </src><tgt>우리가 방금 논의한 것들은</tgt>` | 1447 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 937 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>forgive ourselves </src><tgt>우리가 스스로를 용서해 주어야 합니다.</tgt>` | 1678 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>for the love </src><tgt><\|wait\|></tgt>` | 1546 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1801 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>we've been in, </src><tgt>우리가</tgt>` | 1097 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1260 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>in the time of our love </src><tgt>사랑에 빠져서</tgt>` | 2151 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>and we're in, </src><tgt><\|wait\|></tgt>` | 1397 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>we're at the end. </src><tgt>끝까지 왔습니다.</tgt>` | 1151 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>That becomes </src><tgt><\|wait\|></tgt>` | 828 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 950 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>that whole thing. </src><tgt>그 모든 것이</tgt>` | 884 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 523 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>It continues to evolve. </src><tgt>진화해 나갑니다.</tgt>` | 533 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1578 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt>最初の数マイルは</tgt>` | 794 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1590 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt>少し間違っていました。</tgt>` | 860 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>AHR field, </src><tgt><\|wait\|></tgt>` | 1537 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt>AHRフィールドは</tgt>` | 1581 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance </src><tgt><\|wait\|></tgt>` | 1359 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt>非常に重要ですが、</tgt>` | 673 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 1778 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt>バリアントデータベースは、明らかに</tgt>` | 1834 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1101 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt>私の好きなものです。つまり、</tgt>` | 1680 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1766 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that </src><tgt>フィールドについて合意できなければ、</tgt>` | 1206 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>need to be in these </src><tgt><\|wait\|></tgt>` | 1103 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>これらのデータソースに</tgt>` | 819 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>draw from. </src><tgt><\|wait\|></tgt>` | 552 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>There's nothing to draw from, right? </src><tgt>それらのフィールドを抽出できません。ですよね？</tgt>` | 676 |
| 19 | `<src><\|wait\|></src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 328 |

---

### Test Example 54 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1204 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 840 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt>个人权利</tgt>` | 1031 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1455 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt>是最后才出现的，</tgt>` | 1291 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't I don't </src><tgt><\|wait\|></tgt>` | 1622 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt>而不是主导者。我</tgt>` | 1398 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1117 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1793 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>不希望法院成为社会变革的先锋。</tgt>` | 2098 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1672 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt>但现在他们</tgt>` | 857 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1660 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt>更倾向于反映</tgt>` | 1049 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 810 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>已经形成的共识。</tgt>` | 647 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 745 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt>所以，</tgt>` | 535 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 483 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 449 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 341 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 1182 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>He knows Jesus </src><tgt>ある時、彼は</tgt>` | 606 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a hungry </src><tgt><\|wait\|></tgt>` | 1442 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>and knows that </src><tgt>イエスが飢えていることを知っている。そして、</tgt>` | 1672 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's been told </src><tgt><\|wait\|></tgt>` | 1039 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>for him in the wilderness </src><tgt>荒野で</tgt>` | 1645 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry, </src><tgt><\|wait\|></tgt>` | 1887 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>and so he says to </src><tgt>40日間飢えていたと聞かされていたので、</tgt>` | 2122 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 1849 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're the Son of God, </src><tgt>イエスよ、もしあなたが</tgt>` | 2254 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 1458 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread. </src><tgt>神の子なら証明してみせなさい。これらの石をパンに変えなさい。</tgt>` | 1684 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 1069 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>deal with that </src><tgt>イエスは</tgt>` | 895 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 589 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt>その誘惑にどう対処したのか？いや、</tgt>` | 488 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan led by </src><tgt><\|wait\|></tgt>` | 403 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>bet alone. </src><tgt>ジョナサンが一人で</tgt>` | 427 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 1 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我們看一下</src><tgt><\|wait\|></tgt>` | 1090 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的圖片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 987 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>圖片的</src><tgt><\|wait\|></tgt>` | 1363 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>UPN呢，我們可以</src><tgt>사진의 UPN은</tgt>` | 1230 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>看到的一個是</src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>克汀的部分，</src><tgt>크테인 부분으로 볼 수 있고요,</tgt>` | 1742 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而克汀一般</src><tgt><\|wait\|></tgt>` | 1598 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>是屬於</src><tgt>크테인은 보통</tgt>` | 1843 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我們在</src><tgt><\|wait\|></tgt>` | 579 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>修習的</src><tgt>우리가</tgt>` | 1741 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>地方，所以呢，</src><tgt><\|wait\|></tgt>` | 1558 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>這是身體的部分。</src><tgt>배우는 곳에서 배우는 부분이에요.</tgt>` | 1093 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>會反應的是</src><tgt><\|wait\|></tgt>` | 1606 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要</src><tgt>반응하는 건</tgt>` | 1099 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>給自己一點時間</src><tgt><\|wait\|></tgt>` | 904 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好的</src><tgt>스스로</tgt>` | 511 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下來修習，</src><tgt><\|wait\|></tgt>` | 820 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我們可以看到</src><tgt>충분히 시간을 갖고 공부해야 하는 부분이에요. 그리고</tgt>` | 663 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>這邊是包含五一人的嘛。</src><tgt><\|wait\|></tgt>` | 484 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>여기에는 51인도 포함되어 있고요.</tgt>` | 444 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以也是說。</src><tgt><\|wait\|></tgt>` | 348 |

---

### Test Example 57 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare. </src><tgt>彼らは全く珍しい人々です。</tgt>` | 867 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1479 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>show up to </src><tgt>そして彼らは</tgt>` | 979 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely </src><tgt><\|wait\|></tgt>` | 1413 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に変革するために現れることが多いのです。</tgt>` | 1368 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 817 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>personality is </src><tgt>その個性は</tgt>` | 1454 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1883 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾したものです。</tgt>` | 1721 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 961 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的である一方で、</tgt>` | 1941 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1665 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>hate meaningless conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1259 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like to </src><tgt><\|wait\|></tgt>` | 1060 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>get straight to the </src><tgt>そして</tgt>` | 712 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 453 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>要点をまっすぐ言うのが好きです。彼らは</tgt>` | 582 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 483 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>and they </src><tgt>反対意見を述べるのも好みます。</tgt>` | 422 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 375 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることは決してありません。</tgt>` | 460 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 326 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>EAP stands for </src><tgt>EAPは</tgt>` | 404 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>for. </src><tgt><\|wait\|></tgt>` | 378 |

---

### Test Example 58 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 878 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I am</tgt>` | 792 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 ` | 12626 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1593 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 ` | 6030 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt>I am a person who</tgt>` | 370 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 296 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한성 과 </src><tgt><\|wait\|></tgt>` | 326 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt>is the same generation as Park Han-seong,</tgt>` | 354 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 274 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 1468 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>정무 를 거부 한 </src><tgt>Lee Jun-seok, before this,</tgt>` | 1120 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1455 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt>was running on the platform of refusing political duties,</tgt>` | 1403 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1289 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>and claiming to be for the candidate's victory,</tgt>` | 1141 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1683 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>he even put on quite a show. But now,</tgt>` | 2050 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1942 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt>President Yoon Suk-yeol</tgt>` | 2118 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제관 순간 </src><tgt><\|wait\|></tgt>` | 626 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt>was the one who was in the room when Kim Jong-in was taken over.</tgt>` | 2066 |
| 13 | `<src><\|wait\|></src><tgt>Lee Jun -seok</tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1141 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 </src><tgt>He was there, and Yoon Suk-yeol was about to drop him.</tgt>` | 1255 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독끼를 품은 </src><tgt><\|wait\|></tgt>` | 585 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 426 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt>He was about to show his aggressive side,</tgt>` | 439 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 359 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt>and he was determined.</tgt>` | 390 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 360 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 성상 납권 </src><tgt>Lee Jun-seok's portrait</tgt>` | 464 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 375 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt>was a symbol of the Democratic Party's</tgt>` | 468 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt><\|wait\|></tgt>` | 317 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 입니까? </src><tgt>how much of a boon to their attack?</tgt>` | 375 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 1 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1042 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt>Well, right now after dinner,</tgt>` | 1023 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1496 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt>I want to make something.</tgt>` | 1074 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1481 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ゴルフスローンホテルも</src><tgt>So, this Golf Sloan Hotel</tgt>` | 1604 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1329 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt>is a place where you can have breakfast,</tgt>` | 857 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってるので、</src><tgt><\|wait\|></tgt>` | 1726 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt>so I'm planning to</tgt>` | 1869 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 1328 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>stay here</tgt>` | 1287 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 1549 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt>if you're considering staying at the Golf Sloan Hotel,</tgt>` | 1438 |
| 15 | `<src>もまあいいんじゃないか</src><tgt>thinking about staying here in the future,</tgt>` | `<src>見てみて、まあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1123 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt>and think it's a good idea,</tgt>` | 846 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 536 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt>I think it's a good idea.</tgt>` | 549 |
| 19 | `<src>駅ももう</src><tgt>From this hotel,</tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 445 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>From here, you can walk to Busan Station,</tgt>` | 470 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 314 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんな</src><tgt>it only takes about a minute,</tgt>` | 397 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>かそんなレベルでのね</src><tgt><\|wait\|></tgt>` | 389 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいねまあホテル</src><tgt>so the location is really good,</tgt>` | 468 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 261 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>so if you're interested,</tgt>` | 310 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 312 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それなら</src><tgt>please consider it.</tgt>` | 204 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt><\|wait\|></tgt>` | 186 |
