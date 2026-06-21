# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9896
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9718
  - SRC_RELEASE_TOTAL: 709
  - SRC_WAIT_ACCURACY: 0.1987
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 420
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 0.7500
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 0.9100
  - TGT_WAIT_TOTAL: 300
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1298.7960
  - PROCESS_TIME_MS_P50: 1245.5240
  - PROCESS_TIME_MS_P95: 2115.4640
  - PROCESS_TIME_MS_MAX: 2592.7980

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1093 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 944 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src>用我们</src><tgt>Parents need to</tgt>` | 920 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生那爱胶水</src><tgt><\|wait\|></tgt>` | 1101 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1001 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十分，</src><tgt>use our love glue very much</tgt>` | 1366 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>可以做孩子</src><tgt><\|wait\|></tgt>` | 864 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心里凝养。</src><tgt><\|wait\|></tgt>` | 1714 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心耐心</src><tgt><\|wait\|></tgt>` | 1901 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>等他孩子</src><tgt>to nurture their children's hearts. Be patient and</tgt>` | 791 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1829 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1128 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>的总结点，</src><tgt><\|wait\|></tgt>` | 834 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个优势也很大，</src><tgt>Why is the summary point so strong? This advantage is also huge,</tgt>` | 1581 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，我在</src><tgt><\|wait\|></tgt>` | 1214 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1134 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>的活动</src><tgt>and then, I</tgt>` | 479 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1589 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>和陶人一起</src><tgt><\|wait\|></tgt>` | 2103 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>开展</src><tgt>spent my vacation with Tao Ren and</tgt>` | 1585 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 731 |

---

### Test Example 3 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>lastly, </src><tgt><\|wait\|></tgt>` | 1107 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>he repeats </src><tgt>最后，他重复</tgt>` | 1248 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>learning the answer to repeat </src><tgt><\|wait\|></tgt>` | 1202 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>by being a good app </src><tgt><\|wait\|></tgt>` | 1221 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>and do more of it </src><tgt>学习答案，并多做一些</tgt>` | 1338 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and when you're not </src><tgt><\|wait\|></tgt>` | 1418 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good enough, </src><tgt><\|wait\|></tgt>` | 703 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>get the people around you to help you with </src><tgt>它能帮助你</tgt>` | 2156 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1878 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>in tell next time </src><tgt><\|wait\|></tgt>` | 1798 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气数</src><tgt><\|wait\|></tgt>` | 991 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src>但是只有</src><tgt>気数をつけるのは簡単ですが、</tgt>` | 1282 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>一个师傅</src><tgt><\|wait\|></tgt>` | 1230 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>指导到</src><tgt><\|wait\|></tgt>` | 1167 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>炉火</src><tgt>師匠の指導があれば、炉火は</tgt>` | 1328 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>处于中间。</src><tgt><\|wait\|></tgt>` | 1451 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 622 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反</src><tgt><\|wait\|></tgt>` | 2018 |
| 10 | `<src>要成为</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src>要成为一个</src><tgt>中間にあります。ですから、</tgt>` | 2106 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>师傅。</src><tgt><\|wait\|></tgt>` | 1769 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后，</src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 1003 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>的液体检清</src><tgt>淘撒が終わったら、内部の液体検査を</tgt>` | 1402 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 1230 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷了，然后就</src><tgt><\|wait\|></tgt>` | 1338 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>停留在</src><tgt>済ませて、エネルギーも刷って、</tgt>` | 1146 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1669 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 2030 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>态。</src><tgt>比較的低エネルギーな動作状態に留まります。</tgt>` | 605 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就</src><tgt><\|wait\|></tgt>` | 1819 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>所谓的</src><tgt><\|wait\|></tgt>` | 1763 |

---

### Test Example 6 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1031 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 962 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src>始まったもので</src><tgt>大概从这里开始</tgt>` | 931 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 787 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご方法</src><tgt><\|wait\|></tgt>` | 1178 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ご言やん</src><tgt>开始的，</tgt>` | 1372 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 932 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt><\|wait\|></tgt>` | 1671 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 708 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>などという人の</src><tgt>像，比如塞尚、卢纳尔</tgt>` | 1893 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵は田舎の</src><tgt><\|wait\|></tgt>` | 2016 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>中学生でも</src><tgt><\|wait\|></tgt>` | 1824 |

---

### Test Example 7 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 980 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>영심이 </src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt>I'm Youngsimi,</tgt>` | 1298 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼영심이 </src><tgt><\|wait\|></tgt>` | 1332 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>소소영심이가 </src><tgt><\|wait\|></tgt>` | 1468 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt>Kal Youngsimi, Soso Youngsimi,</tgt>` | 1039 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1791 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1757 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>they're mixed up. Seriously,</tgt>` | 639 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행동 으로도 </src><tgt><\|wait\|></tgt>` | 1907 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 1967 |

---

### Test Example 8 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 750 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>仲まだ</src><tgt>从一开始，特别是</tgt>` | 1258 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>1年生ですからね。</src><tgt><\|wait\|></tgt>` | 1288 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>はいはいはい、その時点で</src><tgt><\|wait\|></tgt>` | 1312 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1126 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>美学、</src><tgt>我们还是大一新生。嗯，当时</tgt>` | 1429 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>をこう</src><tgt><\|wait\|></tgt>` | 697 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>対図していった</src><tgt><\|wait\|></tgt>` | 2039 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>10年経っても</src><tgt><\|wait\|></tgt>` | 2074 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した</src><tgt>对美学这么深入，十年过去了，还是</tgt>` | 1998 |

---

### Test Example 9 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴지 너무 </src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이 저희 에 </src><tgt><\|wait\|></tgt>` | 973 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>일수 있지만 </src><tgt>これは</tgt>` | 1207 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기가 </src><tgt><\|wait\|></tgt>` | 1250 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>あまりにも</tgt>` | 1200 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>필요 로 보이 고 </src><tgt><\|wait\|></tgt>` | 1733 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 이 보살 로 </src><tgt><\|wait\|></tgt>` | 1514 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보일 필요 로 보이 세 우주 가 </src><tgt>本当に菩薩であるべきです。夢のように見えて、私だけが菩薩に見えるように見えて、宇宙が</tgt>` | 1887 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>간다. 이 보살 이란 </src><tgt><\|wait\|></tgt>` | 1308 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>그런데. </src><tgt><\|wait\|></tgt>` | 1776 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 825 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 998 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>いただきたいようなものも</src><tgt>I'd like you to have things like T-shirts,</tgt>` | 1517 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1232 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参考ください。</src><tgt><\|wait\|></tgt>` | 1222 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt>so please refer to them.</tgt>` | 586 |
| 8 | `<src>以上になりまして、</src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1617 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1911 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 504 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>皆さんには</src><tgt>That's all for the contact information.</tgt>` | 2098 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>何かありますので、</src><tgt><\|wait\|></tgt>` | 1907 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 836 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely </src><tgt>極めて重要な研究を</tgt>` | 1251 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>happy people. This is </src><tgt><\|wait\|></tgt>` | 1220 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1203 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking </src><tgt>行いました。これは研究の入り口です。見てください、</tgt>` | 1419 |
| 7 | `<src>looking at the ten percent </src><tgt>これは最先端の研究です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1673 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>at 10% of the happiest </src><tgt><\|wait\|></tgt>` | 993 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1376 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there. People who live </src><tgt>最も幸せな人々の10%がいます。彼らは</tgt>` | 2475 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>can learn from. </src><tgt><\|wait\|></tgt>` | 1874 |

---

### Test Example 12 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 860 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1123 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 쳐박히고 </src><tgt><\|wait\|></tgt>` | 1292 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I'm</tgt>` | 1341 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신의 </src><tgt><\|wait\|></tgt>` | 1201 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모로 겪인 </src><tgt><\|wait\|></tgt>` | 1238 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt>how I've been buried in my own</tgt>` | 1862 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2066 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 1376 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1038 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt>generation, like Harun Park and others.</tgt>` | 2031 |

---

### Test Example 13 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 719 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt>저를</tgt>` | 1140 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>鬼岛，</src><tgt><\|wait\|></tgt>` | 1074 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够保持</src><tgt><\|wait\|></tgt>` | 928 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>它安全的时候，</src><tgt>귀도 섬으로 돌아가서 안전하게 지낼 수 있도록</tgt>` | 1666 |
| 7 | `<src>在做热汤</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在多日</src><tgt><\|wait\|></tgt>` | 541 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>康复阶段</src><tgt><\|wait\|></tgt>` | 1610 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的时候，</src><tgt>며칠 동안 회복하는 동안</tgt>` | 2138 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我暂时</src><tgt><\|wait\|></tgt>` | 1363 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>会做一个小小的愿望，</src><tgt><\|wait\|></tgt>` | 1079 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哦，</src><tgt>작은 소원을 하나 빌어볼까 합니다.</tgt>` | 2068 |

---

### Test Example 14 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1238 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들은 </src><tgt><\|wait\|></tgt>` | 1027 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt>The NickS on the list</tgt>` | 1241 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1368 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1287 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1180 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>닉스 들이었기 때문 </src><tgt>were actually not highly intelligent, but were randomly selected.</tgt>` | 2009 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1986 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1824 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 697 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>The teachers who didn't know the Sasi</tgt>` | 2065 |

---

### Test Example 15 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A Aが</src><tgt><\|wait\|></tgt>` | 1056 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>あるんですね。</src><tgt>There's an A A, right?</tgt>` | 1308 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その場面で</src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>A Bするときに</src><tgt><\|wait\|></tgt>` | 1208 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>Aへの乱攻を</src><tgt>When A B happens in that situation,</tgt>` | 1333 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、</src><tgt><\|wait\|></tgt>` | 1446 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あのその</src><tgt><\|wait\|></tgt>` | 646 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>A Cを</src><tgt>you look into the attack on A, and then</tgt>` | 2166 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>するA Cを保証する</src><tgt><\|wait\|></tgt>` | 1978 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といった使い方を</src><tgt><\|wait\|></tgt>` | 1756 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>されています。</src><tgt>you use it to guarantee A C.</tgt>` | 1112 |

---

### Test Example 16 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunah Teru, </src><tgt><\|wait\|></tgt>` | 1118 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I am currently studying </src><tgt>제 이름은 테루 차나입니다. 현재</tgt>` | 1449 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a </src><tgt><\|wait\|></tgt>` | 1174 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>BA in Finance </src><tgt><\|wait\|></tgt>` | 1201 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a BA in </src><tgt>재무학 학사 과정과 심리학 학사 과정을</tgt>` | 1223 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Psychology. </src><tgt><\|wait\|></tgt>` | 1636 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>I'm here in New York. </src><tgt><\|wait\|></tgt>` | 2031 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And in the </src><tgt>수강하고 있습니다. 뉴욕에 있고요,</tgt>` | 645 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1950 |
| 11 | `<src><\|wait\|></src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1689 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt>미래에는 기업 컨설팅 분야로</tgt>` | 1572 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1152 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1134 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt>感觉Advantageさん有点拉开了距离，</tgt>` | 1289 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大賞とかで</src><tgt><\|wait\|></tgt>` | 1338 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱり多いですね。</src><tgt><\|wait\|></tgt>` | 1206 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>解消したい方って</src><tgt>大家好像都想解决这个问题，</tgt>` | 1276 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐにご意識いただけたら</src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>いい</src><tgt><\|wait\|></tgt>` | 1866 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>ので見てみて</src><tgt>如果能马上意识到这一点，那就太好了。</tgt>` | 762 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と本気で</src><tgt><\|wait\|></tgt>` | 1952 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>本気で</src><tgt><\|wait\|></tgt>` | 1781 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>強いので、なので</src><tgt>因为这真的很重要，所以</tgt>` | 1592 |

---

### Test Example 18 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your </src><tgt><\|wait\|></tgt>` | 810 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>body saying? </src><tgt><\|wait\|></tgt>` | 1019 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>Drop pin to your body. </src><tgt>你的身体在说什么？把图钉钉在你的身体上。</tgt>` | 1947 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 783 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>attention start? </src><tgt><\|wait\|></tgt>` | 1245 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>What is it? Is it </src><tgt>注意力从哪里开始？是什么？</tgt>` | 1154 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>a day? </src><tgt><\|wait\|></tgt>` | 1764 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it in your chest? </src><tgt><\|wait\|></tgt>` | 2296 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>Or is it </src><tgt>是一天的问题吗？是在胸口吗？还是</tgt>` | 2229 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a blank like you use </src><tgt><\|wait\|></tgt>` | 1938 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>saying. </src><tgt><\|wait\|></tgt>` | 1465 |

---

### Test Example 19 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 895 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>선진 쪽에 </src><tgt><\|wait\|></tgt>` | 1068 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여 달라고 해가지고 내가 </src><tgt>I asked them to kill me</tgt>` | 1380 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 길을 아수다. </src><tgt><\|wait\|></tgt>` | 1926 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 쯤에 </src><tgt><\|wait\|></tgt>` | 1110 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>죽여 달라고 해자 </src><tgt><\|wait\|></tgt>` | 775 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>안느냐? 내가 </src><tgt>and they're all dead. I asked them to kill me at another party, didn't I? I</tgt>` | 2206 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1928 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>중요한 거야. </src><tgt><\|wait\|></tgt>` | 2140 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt>don't hear that kind of talk. That's important.</tgt>` | 2148 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1391 |

---

### Test Example 20 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 1077 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>these examples, </src><tgt>好的，这些例子之后，</tgt>` | 1319 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1286 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1164 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>它告诉我们</tgt>` | 1269 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1684 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 548 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>these </src><tgt>实际上</tgt>` | 1822 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>values. So </src><tgt><\|wait\|></tgt>` | 1736 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this game. </src><tgt><\|wait\|></tgt>` | 757 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>board array </src><tgt>使用这些值。所以，</tgt>` | 1889 |
| 13 | `<src><\|wait\|></src><tgt>这个game.scored数组。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1483 |

---

### Test Example 21 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 876 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是是</src><tgt><\|wait\|></tgt>` | 1055 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>二期实操，</src><tgt>2つ目は2期実操です。</tgt>` | 1322 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>配副在</src><tgt><\|wait\|></tgt>` | 1241 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>一期一线</src><tgt><\|wait\|></tgt>` | 1220 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼大的男女们，</src><tgt>一期一线で</tgt>` | 1309 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1379 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 706 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好事期间，</src><tgt>微信で</tgt>` | 2011 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1805 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>微信沟通好</src><tgt><\|wait\|></tgt>` | 690 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>平衡的性膀</src><tgt>良いコミュニケーションが取れる</tgt>` | 1890 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1498 |

---

### Test Example 22 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 785 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间，</src><tgt>If you're in a high school setting with someone who's not unattractive,</tgt>` | 2233 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>又</src><tgt><\|wait\|></tgt>` | 1223 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>有这种矛盾性，</src><tgt><\|wait\|></tgt>` | 1246 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道</src><tgt>and you have this contradiction—</tgt>` | 620 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>会是</src><tgt><\|wait\|></tgt>` | 1601 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里</src><tgt><\|wait\|></tgt>` | 2158 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>does it start that night?</tgt>` | 1897 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 664 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1803 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>与林篇。</src><tgt>Yang Zisi and Lin Pian.</tgt>` | 1552 |

---

### Test Example 23 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为这个情况</src><tgt><\|wait\|></tgt>` | 893 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 1025 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>遇到问题，</src><tgt>Because of this situation, we're running into problems,</tgt>` | 1375 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就更改了回报主管</src><tgt><\|wait\|></tgt>` | 1653 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1015 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>我们笑这个状况，</src><tgt><\|wait\|></tgt>` | 1128 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt>and we've changed the reporting manager or notified the other party about this situation. Don't think</tgt>` | 2095 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 2060 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>工具理性</src><tgt><\|wait\|></tgt>` | 1890 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>承当责任，真的而已，</src><tgt>that you have to bear all the responsibility yourself. It's really just a matter of tool rationality.</tgt>` | 2469 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是给做受众。</src><tgt><\|wait\|></tgt>` | 1576 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1117 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 812 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが緩むと</src><tgt>이것이 기어입니다. 기어가 헐거워지면</tgt>` | 1589 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 1178 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>逆にできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1208 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>ので、</src><tgt>신호가 오히려 안 되게 되니까,</tgt>` | 1335 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1417 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 690 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | 2187 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1955 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1757 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src>はい、</src><tgt>붙어 있다는 거죠. 네,</tgt>` | 1030 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文部材完了を</src><tgt><\|wait\|></tgt>` | 1194 |

---

### Test Example 25 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 893 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>so here, </src><tgt><\|wait\|></tgt>` | 1085 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>you have to </src><tgt>자, 여기서는</tgt>` | 1251 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>do 7.2 GB </src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>already, right? </src><tgt><\|wait\|></tgt>` | 1270 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>And </src><tgt>이미 7.2GB가 필요하죠? 그리고</tgt>` | 1264 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1656 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the Hasekiyo-shi </src><tgt><\|wait\|></tgt>` | 1657 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>の仕組みは </src><tgt>하세키요시의</tgt>` | 868 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>もうコン </src><tgt><\|wait\|></tgt>` | 1916 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7.2 GB </src><tgt><\|wait\|></tgt>` | 1945 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>GB </src><tgt>이미 7.2GB가</tgt>` | 1573 |
| 13 | `<src>です。</src><tgt>어근, 접미사, 어미로 이루어져 있습니다.</tgt>` | `<src>this. </src><tgt><\|wait\|></tgt>` | 1130 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber </src><tgt><\|wait\|></tgt>` | 945 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>band, </src><tgt><\|wait\|></tgt>` | 970 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds also store </src><tgt>고무줄처럼 늘어난 화학 결합은</tgt>` | 1403 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy, </src><tgt><\|wait\|></tgt>` | 1273 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | 1700 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy gets </src><tgt>에너지를 저장합니다. 그 결합이 끊어지면</tgt>` | 927 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to </src><tgt><\|wait\|></tgt>` | 1628 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | 2164 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light, </src><tgt>그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다.</tgt>` | 2445 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>or gets used </src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds </src><tgt><\|wait\|></tgt>` | 1464 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1145 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1193 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt>19번째 수정헌법의 의미는</tgt>` | 1218 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore </src><tgt><\|wait\|></tgt>` | 1260 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>its history as a guide </src><tgt><\|wait\|></tgt>` | 1340 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to help political </src><tgt>역사를 통해 정치적</tgt>` | 1156 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change </src><tgt><\|wait\|></tgt>` | 1626 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 503 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>변화에 어떻게 도움을 줄 수 있는지</tgt>` | 2092 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1922 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1822 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, of course, I'm </src><tgt>미국에서 일어날 수 있는 변화를 돕는 가이드로서의 역사입니다. 물론</tgt>` | 2061 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>married. </src><tgt><\|wait\|></tgt>` | 1025 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 </src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이것들은 </src><tgt><\|wait\|></tgt>` | 967 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>거진 유니트 링과 </src><tgt>These are essentially unit rings</tgt>` | 1366 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거는 거진 </src><tgt><\|wait\|></tgt>` | 1590 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사한 링이 </src><tgt><\|wait\|></tgt>` | 1378 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>그런 걸 굉장히 </src><tgt><\|wait\|></tgt>` | 726 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt>and they are very similar to these rings.</tgt>` | 1841 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 다물리라 </src><tgt><\|wait\|></tgt>` | 2282 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이것이 다기다 </src><tgt><\|wait\|></tgt>` | 2044 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>그런 걸로 </src><tgt><\|wait\|></tgt>` | 1794 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt>They are all naturally closed, so this is all about that.</tgt>` | 1479 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그것에다가 </src><tgt><\|wait\|></tgt>` | 706 |
| 13 | `<src>아연. </src><tgt>And on top of that, there's zinc.</tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1017 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1021 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>皆さんにお伝えしたいのは、このローマでは</tgt>` | 1348 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是以前造成的</src><tgt><\|wait\|></tgt>` | 1319 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1282 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>以前のことで起こったことではなく、</tgt>` | 1179 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1679 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>原因啊，</src><tgt><\|wait\|></tgt>` | 1652 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>跟丰收也不可能是</src><tgt>今直面している原因や豊作は</tgt>` | 895 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>一起之间</src><tgt><\|wait\|></tgt>` | 1882 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就演变出来。</src><tgt><\|wait\|></tgt>` | 1814 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src>的</src><tgt>同時に起こるものではない。</tgt>` | 1149 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 984 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>我的朋友呢，</src><tgt><\|wait\|></tgt>` | 1094 |

---

### Test Example 30 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new </src><tgt><\|wait\|></tgt>` | 905 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>there </src><tgt><\|wait\|></tgt>` | 811 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新东西，</tgt>` | 1089 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>was such an interface before. </src><tgt><\|wait\|></tgt>` | 1084 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1007 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>NetFutureTC. </src><tgt><\|wait\|></tgt>` | 1242 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt>以前就是NetFutureTC这个界面。</tgt>` | 1026 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 1652 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1293 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>for uchet </src><tgt><\|wait\|></tgt>` | 1128 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>所以这只是Uchet</tgt>` | 2032 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src>but </src><tgt><\|wait\|></tgt>` | 1792 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developer or engineer </src><tgt><\|wait\|></tgt>` | 1111 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>should be </src><tgt><\|wait\|></tgt>` | 956 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt>开发者或工程师应该知道这一点。</tgt>` | 1294 |

---

### Test Example 31 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 940 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切都正常，</src><tgt><\|wait\|></tgt>` | 1096 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>毫无反应，</src><tgt>Everything was normal back then, no reaction at all,</tgt>` | 1333 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以坚持</src><tgt><\|wait\|></tgt>` | 1213 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>不开刀，</src><tgt><\|wait\|></tgt>` | 1229 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1216 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt>so I stuck to the plan, didn't cut corners. The deadline was about twelve days,</tgt>` | 1948 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来审段，</src><tgt><\|wait\|></tgt>` | 2177 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 2027 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>to review the draft. I worked my tail off, and I pulled my legs,</tgt>` | 1863 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 896 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1224 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt>and they all left with the same confusion.</tgt>` | 1318 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 840 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>前头，</src><tgt><\|wait\|></tgt>` | 1014 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>那如果你</src><tgt>彼は前方に進んだ。もし</tgt>` | 1287 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了前头之后</src><tgt><\|wait\|></tgt>` | 1293 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你</src><tgt><\|wait\|></tgt>` | 1135 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src>务必</src><tgt>前方に到達したら、必ず</tgt>` | 1288 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>走着，</src><tgt><\|wait\|></tgt>` | 1421 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说</src><tgt><\|wait\|></tgt>` | 695 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src>哎，那我在继续</src><tgt>歩きなさい。そう言ったら、</tgt>` | 2174 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>操作下去哦。</src><tgt><\|wait\|></tgt>` | 1961 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1782 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt>「あ、じゃあ、私は操作を続けよう」って言ったでしょ？</tgt>` | 1653 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么会这么讲？因为呢，</src><tgt><\|wait\|></tgt>` | 1192 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 982 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>あるいは、何か書いたものを</tgt>` | 1293 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1311 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1208 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know </src><tgt>書いたり、テキストを書いたりするなら、その内容が全く分からない</tgt>` | 1471 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>just like, oh, </src><tgt><\|wait\|></tgt>` | 2116 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>なんていうか、「あ、この単語、</tgt>` | 2087 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>starts with a double </src><tgt><\|wait\|></tgt>` | 1809 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 828 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>P, double L, M, I don't know </src><tgt>P、L、M、I、なんていうか、</tgt>` | 2135 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>it. </src><tgt><\|wait\|></tgt>` | 1028 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>低张的部分</src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1028 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src>一个</src><tgt>저장된 부분은</tgt>` | 1243 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>待吊的人，但是</src><tgt><\|wait\|></tgt>` | 1383 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1468 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src>这通场</src><tgt>다시 붙일 수 있는 사람입니다. 하지만 역방향으로 작동합니다. 이 통장</tgt>` | 1374 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>像这样</src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>一个状况，</src><tgt><\|wait\|></tgt>` | 2169 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>需要去特别注意</src><tgt>이런 상황이 필요합니다. 특별히 주의해야 할 점은</tgt>` | 2395 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>它能不能</src><tgt><\|wait\|></tgt>` | 1725 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到与</src><tgt><\|wait\|></tgt>` | 1493 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>它吊不到</src><tgt>이것이</tgt>` | 1143 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与逆的</src><tgt><\|wait\|></tgt>` | 817 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>意思了。</src><tgt><\|wait\|></tgt>` | 741 |

---

### Test Example 35 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 872 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 </src><tgt><\|wait\|></tgt>` | 1055 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>중호보서 100만으로 </src><tgt>そのうち150個が中号ボソ100万で</tgt>` | 2207 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업들이 </src><tgt><\|wait\|></tgt>` | 1274 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1165 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>非常に小さな企業が多くありました。一般的には</tgt>` | 887 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 </src><tgt><\|wait\|></tgt>` | 2057 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>해화백이 겹겨 </src><tgt>中小企業は成長するか、あるいは</tgt>` | 2174 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>되는데, 예번에 소기 없던 </src><tgt><\|wait\|></tgt>` | 2110 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1415 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>폐업도 하지 않는 </src><tgt>廃業もしていません。前年が低迷していた</tgt>` | 1567 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1136 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1029 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get </src><tgt>やる気を出している人、</tgt>` | 1299 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1257 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and that ten of them </src><tgt><\|wait\|></tgt>` | 1268 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that are really important </src><tgt>そして、その10人が本当に</tgt>` | 1352 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1694 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to </src><tgt><\|wait\|></tgt>` | 1634 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>重要だと</tgt>` | 877 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1912 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | 1811 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>at the end of this video. </src><tgt>この動画の最後に1分程度の動画を撮ってきます。</tgt>` | 1703 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage of each one </src><tgt><\|wait\|></tgt>` | 1175 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1034 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>それぞれの内容をもう少し詳しく</tgt>` | 633 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 958 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手</src><tgt><\|wait\|></tgt>` | 832 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>とかですか。</src><tgt>因为是二手车之类的，</tgt>` | 1192 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 564 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>まあ1秒に</src><tgt><\|wait\|></tgt>` | 1246 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt>大概10秒，</tgt>` | 1032 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>設定なんですかね。</src><tgt><\|wait\|></tgt>` | 1805 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>ね。</src><tgt><\|wait\|></tgt>` | 2118 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt>大概1秒左右的设置吧。</tgt>` | 1685 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 732 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>11</src><tgt><\|wait\|></tgt>` | 1786 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>二って</src><tgt><\|wait\|></tgt>` | 1491 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>然后大概11二二，</tgt>` | 1162 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1284 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 429 |

---

### Test Example 38 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 798 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src>Hiemel이라고 하는 </src><tgt>哦，</tgt>` | 1259 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터도 </src><tgt><\|wait\|></tgt>` | 1313 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있고 </src><tgt><\|wait\|></tgt>` | 1280 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>사람도 </src><tgt>计算机也能理解，</tgt>` | 1167 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해할 수 있는 </src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터의 언어에 </src><tgt><\|wait\|></tgt>` | 644 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src><\|wait\|></src><tgt>人们也能理解的计算机语言。</tgt>` | 2066 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법이 맞게 </src><tgt><\|wait\|></tgt>` | 2113 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>우리가 이제 그것들을 작성 해야 </src><tgt><\|wait\|></tgt>` | 2063 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>되는데 </src><tgt>语法正确，</tgt>` | 1374 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것들을 작성 하는 </src><tgt><\|wait\|></tgt>` | 1190 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>프로그램 이 필요 합니다. </src><tgt><\|wait\|></tgt>` | 1229 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src><\|wait\|></src><tgt>我们需要编写程序来编写这些程序。</tgt>` | 1014 |

---

### Test Example 39 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 817 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알고 있나요? </src><tgt><\|wait\|></tgt>` | 1113 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>여기 가 이방인으로 </src><tgt>また知っていますか？</tgt>` | 1303 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1431 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 1190 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>우상에게로 </src><tgt>この異邦人として言葉を失った偶像に</tgt>` | 1227 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그리는 그대로 </src><tgt><\|wait\|></tgt>` | 1764 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 2181 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>그러다 </src><tgt>そのまま引きずられて行ったのです。</tgt>` | 2034 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 1012 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1313 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리노니 </src><tgt><\|wait\|></tgt>` | 1485 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt>そうして、私はあなたたちに</tgt>` | 1386 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1042 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 998 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1187 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세인바라 </src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>目を閉じて、セインバラを</tgt>` | 1310 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 서름이 </src><tgt><\|wait\|></tgt>` | 1275 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차리도 </src><tgt><\|wait\|></tgt>` | 1230 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>돋은 느낌이야. </src><tgt>もう見えてる。</tgt>` | 1280 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들어서 </src><tgt><\|wait\|></tgt>` | 1811 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 2115 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>귀신이 </src><tgt>それを揺らして一緒に遊ぼうっていうんだ。</tgt>` | 639 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>오면 물릴 거고 </src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>세인이 오면 </src><tgt><\|wait\|></tgt>` | 1946 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 지켜주고 </src><tgt>来たら水浸しにして、セインが来たら守って、</tgt>` | 2035 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>지려주니까 </src><tgt><\|wait\|></tgt>` | 927 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 1076 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>安心するんだ。目を閉じて。</tgt>` | 1092 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational </src><tgt><\|wait\|></tgt>` | 985 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>containment. How far </src><tgt><\|wait\|></tgt>` | 894 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>did you actually </src><tgt>교육적 격리. 실제로 얼마나</tgt>` | 1328 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your </src><tgt><\|wait\|></tgt>` | 999 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you </src><tgt><\|wait\|></tgt>` | 1019 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>graduate from high school? </src><tgt>교육에 참여했나요? 고등학교를 졸업했나요?</tgt>` | 1666 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 668 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>containment. Did you </src><tgt><\|wait\|></tgt>` | 1532 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>go to college, </src><tgt>그것은 한 단계의 격리입니다. 대학에 갔나요?</tgt>` | 2369 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and so did you graduate </src><tgt><\|wait\|></tgt>` | 2093 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>that's another level of </src><tgt><\|wait\|></tgt>` | 1958 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>containment. </src><tgt>그것은 또 다른 단계의 격리입니다.</tgt>` | 1790 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 1278 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt>지금은 여기까지입니다. 다음에 뵙겠습니다.</tgt>` | 1150 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 965 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어차피 보면 </src><tgt><\|wait\|></tgt>` | 1122 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt>反正看，</tgt>` | 1308 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1291 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이런 인생 이자 </src><tgt><\|wait\|></tgt>` | 1258 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 같은 </src><tgt>人生就是和20岁一起度过的，</tgt>` | 1292 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1671 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1846 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>像这样的，弟弟妹妹。所以</tgt>` | 669 |
| 10 | `<src>책임감 보다는 </src><tgt>所以比起责任感，</tgt>` | `<src>재인감모다는 </src><tgt><\|wait\|></tgt>` | 2003 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금은 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1932 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt>在“在感冒”上，</tgt>` | 1570 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1138 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1114 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt>自己稍微放低一点。</tgt>` | 443 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 1053 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1056 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 이런 경우 들을 </src><tgt><\|wait\|></tgt>` | 1237 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>수도 있습니다. 저희 가 </src><tgt>ですから、もちろんこのようなケースもあります。私たちは</tgt>` | 1441 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1300 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1136 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 懇意 タン ト へ </src><tgt>AさんとBさんが</tgt>` | 1157 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Biki コンサルタント へ </src><tgt><\|wait\|></tgt>` | 1775 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>가고 A라는 </src><tgt><\|wait\|></tgt>` | 2119 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>사람 이 </src><tgt>コンサルタントに懇意に相談し、Aさんが</tgt>` | 1841 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 786 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>들었을 때 </src><tgt><\|wait\|></tgt>` | 1802 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>悪性コードを</tgt>` | 1410 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로사이트스 </src><tgt><\|wait\|></tgt>` | 1311 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>T에서 </src><tgt><\|wait\|></tgt>` | 1070 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>XPY까지 </src><tgt><\|wait\|></tgt>` | 891 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까? </src><tgt>感染すると、XPYまで感染するのでしょうか？</tgt>` | 802 |

---

### Test Example 44 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 929 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then </src><tgt><\|wait\|></tgt>` | 800 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self defining </src><tgt>アクティビティ、次に自己定義</tgt>` | 1220 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>what we think the standard is because you're </src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>absolutely correct </src><tgt><\|wait\|></tgt>` | 1230 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality </src><tgt>の基準をどう考えているかです。なぜなら、あなたが完全に正しいと思っているからです。しかし、</tgt>` | 1637 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1682 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid </src><tgt><\|wait\|></tgt>` | 1605 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the block </src><tgt>現実は、私たちは新しいブロックのメンバーだからです。</tgt>` | 944 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>and because the standards have changed </src><tgt><\|wait\|></tgt>` | 2060 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>from </src><tgt><\|wait\|></tgt>` | 1716 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>そして基準は20年前に変わってしまったからです。</tgt>` | 1727 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1272 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard because </src><tgt><\|wait\|></tgt>` | 1131 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>everything at this point </src><tgt>私たちは、今のところ、20年前に比べて基準に縛られているのです。</tgt>` | 1119 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められています。なぜなら、今はすべてがより高い基準を求められているからです。</tgt>` | `<src>being higher </src><tgt><\|wait\|></tgt>` | 666 |

---

### Test Example 45 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 922 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个餐饮可以说是</src><tgt><\|wait\|></tgt></tgt>` | 1201 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>很不好的，但是</src><tgt>食事に関しては、正直言ってあまり良くないですね。でも</tgt>` | 1543 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>偏向正财的部分</src><tgt><\|wait\|></tgt></tgt>` | 1657 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt></tgt>` | 1039 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>一直是在事业方面的</src><tgt>事業的な側面は</tgt>` | 752 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长所依赖的</src><tgt><\|wait\|></tgt></tgt>` | 1833 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>红利，</src><tgt><\|wait\|></tgt></tgt>` | 2180 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>如果</src><tgt>業績の成長に依存している恩恵、</tgt>` | 2145 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>在投资理财方面</src><tgt><\|wait\|></tgt></tgt>` | 2064 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt></tgt>` | 1455 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>投資や資産運用に関しては今月も悪くないですが、</tgt>` | 1559 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对来说就</src><tgt><\|wait\|></tgt></tgt>` | 1076 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了</src><tgt><\|wait\|></tgt></tgt>` | 1026 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>那么一点点。</src><tgt>少し弱まった程度です。</tgt>` | 725 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 1007 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和关于</src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>针对对手的感情</src><tgt>伝聞によると、</tgt>` | 1157 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>和真实意图的。</src><tgt><\|wait\|></tgt>` | 1136 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>很多是</src><tgt>相手の感情や真意に関するものが多いです。</tgt>` | 1276 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>包括</src><tgt><\|wait\|></tgt>` | 513 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>经常会听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1702 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>“</src><tgt><\|wait\|></tgt>` | 2084 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt>よく聞くのは、「見てください、</tgt>` | 1716 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 805 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>躲黄了。”</src><tgt><\|wait\|></tgt>` | 1874 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt>この人はまた逃げているんです」とか、</tgt>` | 1808 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>说明了一件事。</src><tgt><\|wait\|></tgt>` | 1001 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1069 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt>その人の目はもう逃げていることを示しています。つまり、</tgt>` | 1204 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是说。</src><tgt><\|wait\|></tgt>` | 630 |

---

### Test Example 47 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1075 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやれ</src><tgt><\|wait\|></tgt>` | 1123 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그렇다면 그냥 젖게 해라. 나는</tgt>` | 1321 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1251 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひどい目だ</src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>끔찍한 눈이군.</tgt>` | 1222 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1673 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えてる</src><tgt><\|wait\|></tgt>` | 1331 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不れる不規則よ。</src><tgt><\|wait\|></tgt>` | 1179 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>이제 한계는 아예 넘어서 버렸어. 이 불규칙함은</tgt>` | 2332 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1765 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長年にわたり</src><tgt><\|wait\|></tgt>` | 1467 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やってるんだ。</src><tgt>오랫동안 해왔어.</tgt>` | 1272 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1148 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい快族線を見た</src><tgt><\|wait\|></tgt>` | 1084 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>ことがない。</src><tgt>나는 이렇게 대단한 쾌속선은 본 적이 없어.</tgt>` | 839 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 984 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인상 하는 </src><tgt><\|wait\|></tgt>` | 1009 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인다면 </src><tgt>If the stock index is rising,</tgt>` | 1376 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형주도 </src><tgt><\|wait\|></tgt>` | 1692 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 906 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>어 큰 폭의 상승 을 하겠지만 </src><tgt>large-cap stocks will also see a significant rise,</tgt>` | 1303 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1616 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 2189 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 2005 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt>but first, the most volatile stocks</tgt>` | 1047 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1414 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1490 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>유동 시총이 </src><tgt><\|wait\|></tgt>` | 1214 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가변 온종목 을 </src><tgt>move the market first because they are the most volatile.</tgt>` | 1261 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 1151 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 507 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1134 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていうだけじゃなくて</src><tgt>This isn't just a visual development environment,</tgt>` | 1363 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1325 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1361 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>こういうのも</src><tgt>it's a visual Python development environment.</tgt>` | 1037 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアル</src><tgt><\|wait\|></tgt>` | 1797 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>の書いてあとそれは</src><tgt><\|wait\|></tgt>` | 2130 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードなんそっから生成される</src><tgt><\|wait\|></tgt>` | 2073 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつやそれが実行</src><tgt>It's also a flow graph visualizer for Python code, and that's generated from Python code. That's what runs.</tgt>` | 2373 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>することによって信号処理</src><tgt><\|wait\|></tgt>` | 1545 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1079 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことをしているから</src><tgt>So it's used for signal processing.</tgt>` | 1195 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 972 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 653 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 468 |

---

### Test Example 50 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 876 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the sorts </src><tgt><\|wait\|></tgt>` | 985 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>that are </src><tgt>모든 종류의</tgt>` | 1256 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>not the same. </src><tgt><\|wait\|></tgt>` | 1252 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But we are </src><tgt><\|wait\|></tgt>` | 1215 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>in the midst of </src><tgt>다르지 않습니다. 하지만 우리는</tgt>` | 1339 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>the same kind of </src><tgt><\|wait\|></tgt>` | 1560 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>love. </src><tgt><\|wait\|></tgt>` | 516 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>It's a time </src><tgt>같은 사랑 속에 있습니다.</tgt>` | 2157 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to enter </src><tgt><\|wait\|></tgt>` | 1871 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1525 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>At the time, that is, </src><tgt><\|wait\|></tgt>` | 872 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>it's all </src><tgt>세상에 들어가는 시간입니다. 즉,</tgt>` | 1869 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>it's all </src><tgt><\|wait\|></tgt>` | 912 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>that sort of </src><tgt><\|wait\|></tgt>` | 1027 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>the same kind. </src><tgt>모두 같은 종류입니다.</tgt>` | 1042 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 635 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>to evolve. </src><tgt><\|wait\|></tgt>` | 469 |

---

### Test Example 51 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1155 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매 니다. </src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>이 운전 을 </src><tgt>进去的时候，我真的非常迷茫。这个</tgt>` | 1385 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>있으면은 뭐 </src><tgt><\|wait\|></tgt>` | 983 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>강북으로 가면 </src><tgt>走过路的时候，如果去江南，</tgt>` | 1923 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 </src><tgt><\|wait\|></tgt>` | 2089 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가면 또 장려 리요. </src><tgt><\|wait\|></tgt>` | 2292 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1713 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>진짜 꽤네요. </src><tgt>说得太多了。如果去外国，那更是鼓励。真的挺</tgt>` | 1894 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1181 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt><\|wait\|></tgt>` | 1069 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>노가요. </src><tgt>挺厉害的。现在，</tgt>` | 1080 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 아닌 거 같아요. </src><tgt><\|wait\|></tgt>` | 777 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>예. </src><tgt><\|wait\|></tgt>` | 466 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1132 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src>be able to move </src><tgt>另外，您也无法</tgt>` | 1286 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1131 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt>在资源之间移动媒体对象。</tgt>` | 1273 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>so if </src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the situation </src><tgt><\|wait\|></tgt>` | 728 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>where you </src><tgt><\|wait\|></tgt>` | 1995 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt>所以，如果您发现</tgt>` | 2098 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 1769 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 908 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>instead of </src><tgt>将错误的媒体文件添加到了某个资源中，</tgt>` | 1518 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>the last one, and we can see about </src><tgt><\|wait\|></tgt>` | 1087 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 980 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt>我们能看到最后一个媒体文件，然后确保</tgt>` | 1155 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>it get backed up </src><tgt><\|wait\|></tgt>` | 574 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 512 |

---

### Test Example 53 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 830 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람들이 </src><tgt><\|wait\|></tgt>` | 995 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석을 해 놓았습니다. </src><tgt>そして、多くの人がそれについて分析しています。</tgt>` | 1569 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1092 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠자이의 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1836 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니 가 </src><tgt>このロクチャイの分析を見ると、ソニーは</tgt>` | 707 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이오렉트의 </src><tgt><\|wait\|></tgt>` | 1751 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPP 파이프를 </src><tgt><\|wait\|></tgt>` | 2188 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>IorectのFPPパイプを128ビットに</tgt>` | 2448 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮추어서 로포인다. </src><tgt><\|wait\|></tgt>` | 1963 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 1612 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>엑스에서도 없는 </src><tgt>下げてローフォインダとされています。Xboxにもない</tgt>` | 1467 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 880 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>S2가 </src><tgt><\|wait\|></tgt>` | 990 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>여기도 없다. </src><tgt>インフィニットキャッシュS2もありません。</tgt>` | 757 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 456 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1319 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1018 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで少し間違った道を進んでしまって、</tgt>` | 1532 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>about the </src><tgt><\|wait\|></tgt>` | 1080 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1207 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1160 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance versus </src><tgt>AHRの重要性について間違った道を進んでしまって、</tgt>` | 1798 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 1613 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 860 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt>このバリアントデータベースは、明らかに</tgt>` | 2115 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1879 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1462 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt>私の大好きなものの一つです。つまり、</tgt>` | 1336 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields that </src><tgt><\|wait\|></tgt>` | 1145 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>need to be in these </src><tgt><\|wait\|></tgt>` | 765 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt>これらのデータソースに含めるべき分野について合意しないと、</tgt>` | 990 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 561 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt><\|wait\|></tgt>` | 411 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>そこから情報を引き出すことができませんよね？</tgt>` | 417 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 911 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 977 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>is a hungry </src><tgt>ある時、彼はイエスが</tgt>` | 1295 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>and he knows that </src><tgt><\|wait\|></tgt>` | 1419 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1188 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>for he's been in the wilderness </src><tgt>飢えていることを知っている。そして、</tgt>` | 1230 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for a sporty day </src><tgt><\|wait\|></tgt>` | 1772 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>is that he's hungry, </src><tgt><\|wait\|></tgt>` | 2212 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>and so he says to Jesus, </src><tgt>スポーツの日を過ごすために飢えていることを知っている。だからイエスにこう言ったんだ。</tgt>` | 2593 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the son of God, </src><tgt><\|wait\|></tgt>` | 1825 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 1480 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread. </src><tgt>神の子なら、証明してみせろ。この石をパンに変えろ。</tgt>` | 1777 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 656 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with that </src><tgt><\|wait\|></tgt>` | 924 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>イエスはどうやってその誘惑に対処したんだろう？</tgt>` | 805 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 478 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 406 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>Jonathan lived by the law alone. </src><tgt>いや、ジョナサンは律法だけで生きていた。</tgt>` | 639 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 831 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>individual right, </src><tgt>个人权利</tgt>` | 1066 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 820 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1300 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I I I don't I don't </src><tgt>在前面不是领头羊，而最高法院是最后加入的。我</tgt>` | 2225 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt><\|wait\|></tgt>` | 1721 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1747 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>the vanguard of social change </src><tgt><\|wait\|></tgt>` | 752 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>不希望法院成为社会变革的先锋。</tgt>` | 2091 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 1827 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1502 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1147 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt>但他们更反映的是</tgt>` | 964 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 651 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 972 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>已经形成的共识。</tgt>` | 680 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 508 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 427 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 395 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who </src><tgt>你有一些联邦法官</tgt>` | 370 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 963 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>一下</src><tgt><\|wait\|></tgt>` | 1036 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 1308 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1333 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是</src><tgt><\|wait\|></tgt>` | 1190 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>克汀的部分，</src><tgt>사진에는 크틴 부분도 보이고,</tgt>` | 1340 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>而克汀一般</src><tgt><\|wait\|></tgt>` | 1707 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>就是属于</src><tgt><\|wait\|></tgt>` | 1738 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>我们</src><tgt>크틴은 보통 우리가</tgt>` | 758 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在收集的地方</src><tgt><\|wait\|></tgt>` | 1902 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>，所以呢，</src><tgt><\|wait\|></tgt>` | 1953 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>它是身体的部分。</src><tgt>모으는 곳에 있는 부분이에요. 그래서 몸의 부분이죠.</tgt>` | 1887 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它会反映的是</src><tgt><\|wait\|></tgt>` | 1184 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>我们需要给</src><tgt><\|wait\|></tgt>` | 1083 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 998 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地</src><tgt>이것은 우리가 자신에게 시간을 좀 주어 잘</tgt>` | 812 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做下来收集，</src><tgt><\|wait\|></tgt>` | 528 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们看到这边</src><tgt><\|wait\|></tgt>` | 451 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>是包含五一人的嘛。</src><tgt>수집할 수 있도록 하는 거예요. 여기에는 51명이 포함되어 있죠.</tgt>` | 704 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 368 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以也是说，</src><tgt><\|wait\|></tgt>` | 367 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 913 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1022 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src>and they often </src><tgt>この人々は全く珍しく、</tgt>` | 1302 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1329 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely </src><tgt><\|wait\|></tgt>` | 1109 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>revolutionize the world. </src><tgt>世界を完全に変革する。</tgt>` | 1351 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The </src><tgt><\|wait\|></tgt>` | 1678 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>personality is </src><tgt><\|wait\|></tgt>` | 1594 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt>その性格は矛盾している。</tgt>` | 907 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1977 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1890 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, they also </src><tgt>外向的である一方で、</tgt>` | 1610 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1126 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 934 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src>And like to </src><tgt>無意味な会話も嫌う。</tgt>` | 711 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>get straight to the </src><tgt><\|wait\|></tgt>` | 1008 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 629 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt>そして本題に入りたい。</tgt>` | 532 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate </src><tgt><\|wait\|></tgt>` | 457 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and they </src><tgt><\|wait\|></tgt>` | 346 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 336 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate </src><tgt>議論を恐れない。</tgt>` | 369 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 347 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>and CP stands </src><tgt><\|wait\|></tgt>` | 365 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for. </src><tgt>CPはそれを支持している。</tgt>` | 376 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이전 </src><tgt><\|wait\|></tgt>` | 943 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>성공 을 경험 을 </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>한 명분 이 후부 를 </src><tgt>The previous successful person</tgt>` | 1272 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1257 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후부의 당수를 </src><tgt><\|wait\|></tgt>` | 1394 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1058 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색 까지 </src><tgt>was also doing it for the future of the future, and even</tgt>` | 1945 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제는 </src><tgt><\|wait\|></tgt>` | 2145 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤성률 후보 가 </src><tgt><\|wait\|></tgt>` | 2035 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정일 을 </src><tgt>did the favor of Yoon Sung-ryul, the candidate for the future of the future, and even</tgt>` | 2462 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제관 순간 </src><tgt><\|wait\|></tgt>` | 1481 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석 은 들은 에 놓고 </src><tgt><\|wait\|></tgt>` | 1325 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤성률 후보 </src><tgt>put the name of Kim Jong-il in the ballot box at the moment of the election.</tgt>` | 1414 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 835 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뜻끼를 품은 </src><tgt><\|wait\|></tgt>` | 563 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 476 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt>He was thinking of throwing the ballot box in to show his aggressive intent.</tgt>` | 627 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 356 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 297 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가 세 번 발 </src><tgt><\|wait\|></tgt>` | 307 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 청상 납권 </src><tgt>It was a deliberate move. This was the third time</tgt>` | 347 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 291 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 372 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt><\|wait\|></tgt>` | 321 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재입니까? </src><tgt>that the Democratic Party was hoping for a big win?</tgt>` | 364 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt><\|wait\|></tgt>` | 827 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。</src><tgt>Well, I'd like to make something after a meal now.</tgt>` | 1551 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1187 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 1202 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ゴルフスローンホテルも</src><tgt>So, I'd like to try this Golf Sloan Hotel.</tgt>` | 1424 |
| 7 | `<src>朝食が食べれる場所</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>朝食が食べれる</src><tgt><\|wait\|></tgt>` | 1701 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>場所になってる</src><tgt><\|wait\|></tgt>` | 779 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってる</src><tgt>It's a place where you can have breakfast,</tgt>` | 1767 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>ので今後ね</src><tgt><\|wait\|></tgt>` | 2030 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルフスローンホテル</src><tgt><\|wait\|></tgt>` | 1946 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>so I'd like to stay here in the future.</tgt>` | 1767 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt><\|wait\|></tgt>` | 1158 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 1128 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てみてまあいいんじゃない</src><tgt>If you're considering it,</tgt>` | 1124 |
| 16 | `<src><\|wait\|></src><tgt>thinking about staying here in the future,</tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 691 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>はい思います。</src><tgt>I think it's a good idea.</tgt>` | 582 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 410 |
| 19 | `<src>駅ももう</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 442 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>From here, you can walk to Busan Station,</tgt>` | 364 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかるか</src><tgt><\|wait\|></tgt>` | 312 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんな </src><tgt><\|wait\|></tgt>` | 324 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>いかそんなレベルのね</src><tgt>or maybe it takes a minute or so,</tgt>` | 418 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のねまあホテル</src><tgt><\|wait\|></tgt>` | 337 |
| 25 | `<src>ホテルになってますので</src><tgt>so the location is really good.</tgt>` | `<src>なってますので</src><tgt>so the location is pretty good,</tgt>` | 332 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 282 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt>so if you're interested,</tgt>` | 227 |
| 28 | `<src>ください</src><tgt>If you'd like, please consider it.</tgt>` | `<src>ください。それなら</src><tgt><\|wait\|></tgt>` | 193 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt>please consider it. Then for this time,</tgt>` | 208 |
