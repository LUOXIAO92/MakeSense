# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9234
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4834
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.0000
  - TGT_RELEASE_TOTAL: 0
  - TGT_WAIT_ACCURACY: 0.0000
  - TGT_WAIT_TOTAL: 0
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1414.7040
  - PROCESS_TIME_MS_P50: 1441.2140
  - PROCESS_TIME_MS_P95: 2405.7290
  - PROCESS_TIME_MS_MAX: 3452.0850

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1953 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1011 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1335 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1306 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1581 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有的这个状况，</src>` | 413 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1552 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1550 |
| 9 | `<src>独立承担。</src>` | `<src>你不利沉担，</src>` | 622 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 2671 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业就是</src>` | 1222 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要做</src>` | 2164 |
| 2 | `<src>家长需要做的是，</src>` | `<src>的是，</src>` | 798 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 1554 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 1265 |
| 5 | `<src>爱浇水、</src>` | `<src>深深的爱浇水，</src>` | 1516 |
| 6 | `<src>施肥，</src>` | `<src>所以</src>` | 449 |
| 7 | `<src>给足</src>` | `<src><\|wait\|></src>` | 1713 |
| 8 | `<src>孩子心理营养，</src>` | `<src>给足孩子心灵营养，</src>` | 1839 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 278 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>给耐心等</src>` | 2833 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 1050 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 2160 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>在相似点</src>` | 813 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个优秀人</src>` | 1392 |
| 4 | `<src>然后</src>` | `<src>很大？</src>` | 404 |
| 5 | `<src><\|wait\|></src>` | `<src>然后呢，</src>` | 1187 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放大</src>` | 1809 |
| 7 | `<src>儿核桃</src>` | `<src>喝陶人，</src>` | 1875 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1801 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉是</src>` | 975 |
| 10 | `<src>这种核桃</src>` | `<src>这种喝陶人</src>` | 2634 |
| 11 | `<src>仁儿。</src>` | `<src>啊。</src>` | 535 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2043 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1029 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1297 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个</src>` | 750 |
| 5 | `<src><\|wait\|></src>` | `<src>师傅指导，</src>` | 636 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1828 |
| 7 | `<src>处于中间，</src>` | `<src>如何趋于中间</src>` | 1722 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1380 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 685 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 2927 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 1064 |

---

### Test Example 5 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1853 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Aptitude Pro. </src>` | 978 |
| 3 | `<src>촉발 시키고 </src>` | `<src>축복 받히고 </src>` | 1578 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1176 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1799 |
| 6 | `<src><\|wait\|></src>` | `<src>범어를 </src>` | 382 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>죽인 대로나 </src>` | 1607 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1769 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1202 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 2654 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>이다. </src>` | 1032 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1890 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 749 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1487 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1221 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 619 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1424 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1721 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 1912 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 2181 |
| 10 | `<src><\|wait\|></src>` | `<src>language you </src>` | 1644 |
| 11 | `<src>language are you using? </src>` | `<src>use. </src>` | 1099 |

---

### Test Example 7 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1725 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 822 |
| 3 | `<src>これなんかまだ</src>` | `<src>子供がまだ</src>` | 1621 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生ですからね。</src>` | 1277 |
| 5 | `<src>この時点で</src>` | `<src>はいはい。あの時点で</src>` | 1597 |
| 6 | `<src>こう短く</src>` | `<src>こう短い間隔</src>` | 395 |
| 7 | `<src>剪定を</src>` | `<src>線手を</src>` | 1750 |
| 8 | `<src><\|wait\|></src>` | `<src>こうタイズして</src>` | 1835 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>待てる</src>` | 1122 |
| 10 | `<src>十年経っても</src>` | `<src>と10年経っても</src>` | 2744 |
| 11 | `<src>大した。</src>` | `<src>大丈夫だ。</src>` | 1093 |

---

### Test Example 8 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1768 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 827 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1584 |
| 4 | `<src><\|wait\|></src>` | `<src>之间有这种</src>` | 390 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>人际，</src>` | 1013 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1757 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1531 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天</src>` | 450 |
| 9 | `<src><\|wait\|></src>` | `<src>夜里开始的？</src>` | 1837 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2634 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1329 |
| 12 | `<src>连篇。</src>` | `<src>片片。</src>` | 1172 |

---

### Test Example 9 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2318 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 801 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1425 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1323 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1791 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 495 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1483 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니까? </src>` | 1886 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2122 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 1678 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 1371 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying important </src>` | 1907 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 741 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1620 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. This is </src>` | 1338 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem. </src>` | 1804 |
| 6 | `<src>research, </src>` | `<src>Research. Looking at </src>` | 1649 |
| 7 | `<src>looking at the ten percent </src>` | `<src>10% </src>` | 508 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 1684 |
| 9 | `<src>of the happiest people </src>` | `<src><\|wait\|></src>` | 2584 |
| 10 | `<src>out there, </src>` | `<src>people out there, people who </src>` | 1384 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1278 |

---

### Test Example 11 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2045 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 870 |
| 3 | `<src>始めた</src>` | `<src>始めたもので、</src>` | 1569 |
| 4 | `<src>もので、</src>` | `<src><\|wait\|></src>` | 1249 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1159 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 807 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1673 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1741 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 382 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどの</src>` | 2865 |
| 11 | `<src>は、田舎の</src>` | `<src>という人の絵は</src>` | 1058 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 1626 |

---

### Test Example 12 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>淘沙完以后</src>` | 2184 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>呢，</src>` | 752 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的冶铁矿</src>` | 1635 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了。</src>` | 1252 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1751 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在</src>` | 1572 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 445 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的运行</src>` | 1842 |
| 9 | `<src>状态，</src>` | `<src>状态。</src>` | 2775 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1134 |
| 11 | `<src>抑郁状态。</src>` | `<src>易于状态，</src>` | 1804 |

---

### Test Example 13 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1977 |
| 2 | `<src>옹심이, </src>` | `<src>용심히 </src>` | 811 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1589 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심히 </src>` | 1210 |
| 5 | `<src>옹심이가 </src>` | `<src>그 솔 용심히가 </src>` | 387 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1619 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이는 건데요. </src>` | 1911 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1809 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1522 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해당 으로 조금 죽입니다. </src>` | 2471 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 1861 |

---

### Test Example 14 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1859 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 796 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 1358 |
| 4 | `<src>テキという設備寺が</src>` | `<src>豊作を</src>` | 451 |
| 5 | `<src>ありましたね。</src>` | `<src>楽しみましたね。</src>` | 1130 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1382 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 590 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井製油所の仕組み</src>` | 1827 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1735 |
| 10 | `<src>は五経、</src>` | `<src>もうコン、</src>` | 1086 |
| 11 | `<src><\|wait\|></src>` | `<src>豊作を</src>` | 2528 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 709 |
| 13 | `<src>です。</src>` | `<src>楽しみます。</src>` | 1943 |

---

### Test Example 15 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2191 |
| 2 | `<src>あの</src>` | `<src><\|wait\|></src>` | 886 |
| 3 | `<src>いただもらえる</src>` | `<src>あのいただもらえる</src>` | 1551 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1239 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1785 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1413 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 528 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりますので</src>` | 1762 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1077 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2519 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 693 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1993 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2018 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜을 </src>` | 879 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 1603 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주기려고 들어왔 수다. </src>` | 1266 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜을 </src>` | 1754 |
| 6 | `<src>죽여 달라 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 1802 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>안되나. 내가 </src>` | 1812 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>무슨 소리 안 듣고 </src>` | 750 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 3118 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아. </src>` | 906 |
| 11 | `<src>내가 가. </src>` | `<src><\|wait\|></src>` | 1770 |

---

### Test Example 17 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1694 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 820 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 1624 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，让我</src>` | 1311 |
| 5 | `<src>让我能够哈，</src>` | `<src>能够哈</src>` | 1576 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 408 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1684 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>的时候，在做热汤的时候，</src>` | 1907 |
| 9 | `<src><\|wait\|></src>` | `<src>我当时</src>` | 1256 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被他作为知音</src>` | 2583 |
| 11 | `<src>小小的愿望</src>` | `<src>的一个小小的愿望哈。</src>` | 1173 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 1597 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2122 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 829 |
| 3 | `<src>ギアが</src>` | `<src>ギアです。ギアが</src>` | 1572 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと、信号が</src>` | 382 |
| 5 | `<src><\|wait\|></src>` | `<src>行き先ができなくなってしまう</src>` | 1068 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1716 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1288 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 661 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1862 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いている</src>` | 1372 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 2346 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1063 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 1786 |

---

### Test Example 19 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2217 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 903 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment, </src>` | 1414 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1231 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1090 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 877 |
| 7 | `<src><\|wait\|></src>` | `<src>change can </src>` | 1539 |
| 8 | `<src>change can happen </src>` | `<src><\|wait\|></src>` | 484 |
| 9 | `<src>in the United States. </src>` | `<src>happen in the United States. </src>` | 1842 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2134 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1618 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1326 |
| 13 | `<src>myriad. </src>` | `<src>I may read. </src>` | 1805 |

---

### Test Example 20 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1904 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 902 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1454 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy. And when those </src>` | 1361 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1882 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1663 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1272 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, like </src>` | 848 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 3137 |
| 10 | `<src><\|wait\|></src>` | `<src>Or </src>` | 760 |
| 11 | `<src>or gets used to make </src>` | `<src>gets used to make </src>` | 1283 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1718 |

---

### Test Example 21 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1840 |
| 2 | `<src>映画でですね、</src>` | `<src>AAアンデスにですね</src>` | 958 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1590 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>霊性速度かどうかっていうの</src>` | 1326 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに</src>` | 1728 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>AAのランキングを</src>` | 1559 |
| 7 | `<src>ことで、あの</src>` | `<src>調べて、あの</src>` | 450 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その霊性速度かどうかっていうの</src>` | 1891 |
| 9 | `<src>保証する、生息である</src>` | `<src>を証明する</src>` | 2838 |
| 10 | `<src>ことを保証する</src>` | `<src>速度であること保証する</src>` | 1090 |
| 11 | `<src>といったような</src>` | `<src>といったらその使い方を</src>` | 1460 |
| 12 | `<src>使い方をされます。</src>` | `<src>されます。</src>` | 1508 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2270 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 826 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1605 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1235 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1790 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1528 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 456 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1718 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1155 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2445 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 682 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game dot sort </src>` | 2210 |
| 13 | `<src><\|wait\|></src>` | `<src>array. </src>` | 1373 |

---

### Test Example 23 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1939 |
| 2 | `<src><\|wait\|></src>` | `<src>이거 너무 지저 여요. </src>` | 1095 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>할 수 있지만 </src>` | 1431 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 고사 래요. </src>` | 1327 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 </src>` | 1721 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>자기 고사 래요. 근데 꿈일 프로 </src>` | 2058 |
| 7 | `<src>뭐 있고 </src>` | `<src>하고 있고 나만 </src>` | 1815 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>이 고사 래요 </src>` | 3016 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 프로라고 보이 색이 </src>` | 1094 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가진다. 진짜 고사 래요. </src>` | 2223 |
| 11 | `<src>보살 이라는데. </src>` | `<src><\|wait\|></src>` | 1352 |

---

### Test Example 24 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2189 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 845 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1582 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to repeat. </src>` | 1279 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at. </src>` | 1903 |
| 6 | `<src>and do more of it. </src>` | `<src>And do more of it. </src>` | 1798 |
| 7 | `<src><\|wait\|></src>` | `<src>And when you're not good </src>` | 1917 |
| 8 | `<src>And what you're not good at, </src>` | `<src>at it, </src>` | 3194 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get to people around you to help you with </src>` | 983 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1998 |
| 11 | `<src>And until next time. </src>` | `<src>and and tell next time. </src>` | 1575 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1891 |
| 2 | `<src><\|wait\|></src>` | `<src>进入第二个</src>` | 807 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>机制场，</src>` | 1616 |
| 4 | `<src>服务</src>` | `<src>在第一机制场</src>` | 1321 |
| 5 | `<src>在一级一线</src>` | `<src><\|wait\|></src>` | 1783 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们</src>` | 612 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1325 |
| 8 | `<src><\|wait\|></src>` | `<src>呃，在做维向</src>` | 1877 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>运动高速几呢，</src>` | 1522 |
| 10 | `<src>发现</src>` | `<src>你可以发现</src>` | 2198 |
| 11 | `<src>给微信公众号评分</src>` | `<src>维向运动和平分</src>` | 879 |
| 12 | `<src>的新榜反而</src>` | `<src><\|wait\|></src>` | 1817 |
| 13 | `<src>火了。</src>` | `<src>的星仿佛跑火了。</src>` | 1525 |

---

### Test Example 26 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>达到了一个</src>` | 1734 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>天头。</src>` | 807 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1408 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了天头之后，</src>` | 388 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1215 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1783 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1729 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着哎，</src>` | 1396 |
| 9 | `<src><\|wait\|></src>` | `<src>那我再继续操作</src>` | 709 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦。</src>` | 2783 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1147 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2143 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1432 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1038 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src><\|wait\|></src>` | 2006 |
| 2 | `<src>一切正常，</src>` | `<src>我当时一切正常，</src>` | 924 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活得波鹏乱跳，</src>` | 1594 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1186 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开刀，</src>` | 1875 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 1795 |
| 7 | `<src>大概有十位医生</src>` | `<src><\|wait\|></src>` | 1780 |
| 8 | `<src>来诊断，</src>` | `<src>一世医生来审断，</src>` | 928 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下条腿</src>` | 2586 |
| 10 | `<src>一下提腿，</src>` | `<src><\|wait\|></src>` | 675 |
| 11 | `<src>都没有问题。</src>` | `<src>以上剃腿都没有问题，</src>` | 1876 |
| 12 | `<src>他们</src>` | `<src><\|wait\|></src>` | 1624 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>他们都很疑惑的离开。</src>` | 1105 |

---

### Test Example 28 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1853 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수를 </src>` | 2038 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 469 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1215 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1727 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1424 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 619 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업할 </src>` | 1853 |
| 9 | `<src>걷게 되는데 </src>` | `<src>기회 도 되는데 </src>` | 2778 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업 들은 </src>` | 1202 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1731 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업도 하지 않는 </src>` | 1759 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1142 |

---

### Test Example 29 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだん</src>` | 2371 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が</src>` | 778 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1588 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>おしゃれルカで</src>` | 1223 |
| 5 | `<src>多いですね。</src>` | `<src>青ポイですね。</src>` | 1838 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊したい方って</src>` | 1916 |
| 7 | `<src>すごい</src>` | `<src>すごいポイ行き帰行き</src>` | 1844 |
| 8 | `<src>自己意識高いし、</src>` | `<src>たがいに、</src>` | 3231 |
| 9 | `<src>自分で</src>` | `<src>でいうねで</src>` | 907 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>多分その通りじゃ</src>` | 2016 |
| 11 | `<src>傾向が強いので、</src>` | `<src>結婚が強ので、</src>` | 1517 |
| 12 | `<src>なので。</src>` | `<src>なので、</src>` | 1085 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1936 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 2065 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 431 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 1234 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 1769 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1558 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 450 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1873 |
| 9 | `<src>이렇게 </src>` | `<src>기계 가 </src>` | 2282 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>잘 작동 을 </src>` | 1571 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2193 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1542 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1532 |

---

### Test Example 31 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1997 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chirun Patel, </src>` | 906 |
| 3 | `<src>I am currently </src>` | `<src>and I am currently studying </src>` | 1555 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1238 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>a BA in Business Finance </src>` | 1840 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a BSc in Psychology. </src>` | 1876 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1845 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at the university, </src>` | 2769 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1233 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2410 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1356 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1476 |

---

### Test Example 32 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2170 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 731 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1540 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1271 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1778 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1978 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1776 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1549 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2212 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 859 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1830 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1623 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1374 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2200 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 680 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 1658 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是意味着</src>` | 1217 |
| 5 | `<src>所以呢，</src>` | `<src>罪呢，</src>` | 1767 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 388 |
| 7 | `<src>所面临的一些</src>` | `<src>所念的一些</src>` | 1581 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>恶业啊</src>` | 1851 |
| 9 | `<src>也不可能是</src>` | `<src>跟不幸</src>` | 3128 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你</src>` | 916 |
| 11 | `<src><\|wait\|></src>` | `<src>期间就</src>` | 1326 |
| 12 | `<src>演变出来的，</src>` | `<src>免变出来的，</src>` | 1673 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1419 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1421 |

---

### Test Example 34 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 2002 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 853 |
| 3 | `<src><\|wait\|></src>` | `<src>There was such </src>` | 1583 |
| 4 | `<src>such interfaces before, </src>` | `<src>interposes before, </src>` | 1210 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1485 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilterTC, </src>` | 491 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 1746 |
| 8 | `<src>this is just </src>` | `<src>and so this is just </src>` | 1848 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1268 |
| 10 | `<src>to look at. </src>` | `<src>where it </src>` | 2406 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 611 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1944 |
| 13 | `<src>developers or engineers </src>` | `<src>develops or engineers </src>` | 1508 |
| 14 | `<src>working on BugRepo </src>` | `<src>webkit will be </src>` | 1184 |
| 15 | `<src>should be aware of that. </src>` | `<src>ever aware of that. </src>` | 1412 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 2034 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 749 |
| 3 | `<src>一个在钓鱼</src>` | `<src><\|wait\|></src>` | 1554 |
| 4 | `<src>的人，但是</src>` | `<src>一个在跳舞的人，但是</src>` | 1302 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是属于逆向的，</src>` | 1825 |
| 6 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1746 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>所以通常逢到这样的一个状况</src>` | 1838 |
| 8 | `<src>时候，就要去</src>` | `<src>的时候，就要去</src>` | 1103 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意</src>` | 2387 |
| 10 | `<src>是它能不能够</src>` | `<src>是他能不能够</src>` | 784 |
| 11 | `<src>钓到鱼，</src>` | `<src><\|wait\|></src>` | 1969 |
| 12 | `<src>它钓不到鱼</src>` | `<src>调到与他跳</src>` | 1570 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1430 |
| 14 | `<src>的意思哦。</src>` | `<src>不到与意思上。</src>` | 1143 |

---

### Test Example 36 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2129 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 894 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1529 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1175 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 1154 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 868 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1704 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. </src>` | 1797 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 666 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, did you </src>` | 3185 |
| 11 | `<src>That's another level of </src>` | `<src>graduate? </src>` | 694 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 2133 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1493 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1584 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1143 |

---

### Test Example 37 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2288 |
| 2 | `<src><\|wait\|></src>` | `<src>선생 이 뭐라 </src>` | 1003 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야? </src>` | 1438 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 돋든 </src>` | 1292 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>가자리 돋든 </src>` | 1801 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>내 기명응이야. </src>` | 1701 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1732 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 406 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 오면 </src>` | 1831 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1891 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 1228 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1594 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주려 하니까 </src>` | 1663 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1281 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1253 |

---

### Test Example 38 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2091 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 832 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1605 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1225 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>통생이자 </src>` | 538 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 도 가족 </src>` | 1467 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아 </src>` | 1684 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1275 |
| 9 | `<src><\|wait\|></src>` | `<src>저희 가 </src>` | 787 |
| 10 | `<src>책임감 보다는 </src>` | `<src>하는 거라 는 </src>` | 2115 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 1841 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 1794 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1523 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1116 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1235 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1441 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 2249 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 753 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1584 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1230 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1827 |
| 6 | `<src>that I think are </src>` | `<src>that are really </src>` | 1795 |
| 7 | `<src>really important. </src>` | `<src>important. </src>` | 1584 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 417 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into </src>` | 2744 |
| 10 | `<src>I have about </src>` | `<src><\|wait\|></src>` | 1219 |
| 11 | `<src>one minute videos </src>` | `<src>I have about one minute videos </src>` | 1729 |
| 12 | `<src>that follow this video </src>` | `<src>at the end of this video </src>` | 1757 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one. </src>` | 1063 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1355 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>In a little more detail, </src>` | 1269 |

---

### Test Example 40 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2078 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>眠らせてやれ</src>` | 990 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1435 |
| 4 | `<src><\|wait\|></src>` | `<src>今、</src>` | 1221 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>ひき手を見てる。</src>` | 1349 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 657 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1796 |
| 8 | `<src><\|wait\|></src>` | `<src>遠い超えている</src>` | 1809 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>船の軌跡よ。</src>` | 1209 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2501 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 591 |
| 12 | `<src>船大工をやってる</src>` | `<src>船出庫をやってる</src>` | 2124 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1358 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1549 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 1139 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 847 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2140 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 856 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不动了，但是</src>` | 1452 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分。</src>` | 1287 |
| 5 | `<src>也就是</src>` | `<src><\|wait\|></src>` | 1757 |
| 6 | `<src>在事业方面的</src>` | `<src>也就是在事业方面的</src>` | 1693 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩增长所带来的</src>` | 1322 |
| 8 | `<src>与收入的</src>` | `<src>红利，以及收入的</src>` | 854 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果</src>` | 3143 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面呢，</src>` | 957 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1967 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1531 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说，</src>` | 1457 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就算</src>` | 1114 |
| 15 | `<src><\|wait\|></src>` | `<src>又乐那么一点。</src>` | 946 |

---

### Test Example 42 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1862 |
| 2 | `<src>HTML이라고 </src>` | `<src>어 Htielmei, </src>` | 1019 |
| 3 | `<src><\|wait\|></src>` | `<src>이라고 하는 </src>` | 1315 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피터도 </src>` | 1321 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1806 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1905 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1799 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1236 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 2489 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 의 뭐랄게 </src>` | 799 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>우리 가 이제 코드 를 </src>` | 1968 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 1438 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1481 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1072 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 851 |

---

### Test Example 43 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 2052 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 821 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1601 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 986 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 432 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. </src>` | 1888 |
| 7 | `<src><\|wait\|></src>` | `<src>뭐 이렇게 컨설턴트가 </src>` | 1816 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여기 있고, A라는 </src>` | 1920 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1609 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2251 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 1203 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람이 </src>` | 1610 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1535 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 CT에서 </src>` | 1297 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 1066 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까? </src>` | 665 |

---

### Test Example 44 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1907 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1042 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1405 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1245 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1843 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1889 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1835 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 3253 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 793 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2036 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1474 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 995 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1428 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1160 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 625 |

---

### Test Example 45 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2090 |
| 2 | `<src>十一二手とか</src>` | `<src>十一、二、三とか</src>` | 999 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>言った。おそらく</src>` | 1478 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で</src>` | 1202 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1796 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1914 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>言っていく</src>` | 1845 |
| 8 | `<src>計算ですか</src>` | `<src>ぐらいのセッションとかね。</src>` | 1628 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 2180 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1004 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1606 |
| 12 | `<src><\|wait\|></src>` | `<src>十一、</src>` | 1300 |
| 13 | `<src>十一二手で</src>` | `<src>二、三</src>` | 1358 |
| 14 | `<src>あの</src>` | `<src><\|wait\|></src>` | 1146 |
| 15 | `<src>宮馬とかが</src>` | `<src>とかが</src>` | 957 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 656 |

---

### Test Example 46 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1815 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 872 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 했노 습니다. </src>` | 1617 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1134 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>이 로쿠 자의 분석 을 보시면 </src>` | 1797 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 392 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 제품 을 </src>` | 1607 |
| 8 | `<src>파이프 를 </src>` | `<src>FPD 파이 프를 </src>` | 1838 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 </src>` | 1706 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 보입니다. </src>` | 2257 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1141 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈 엑스에서도 없는 </src>` | 1780 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1549 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 M.S.E. </src>` | 1555 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>가 여기 도 없다. </src>` | 1174 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 802 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2126 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手的</src>` | 1000 |
| 3 | `<src>的感情或</src>` | `<src>感情或</src>` | 1318 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1304 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1373 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 549 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 1856 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会听到人们这样说：</src>` | 1906 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1656 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2138 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1102 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了。</src>` | 1643 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1476 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1417 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1086 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 671 |
| 17 | `<src><\|wait\|></src>` | `<src>是说。</src>` | 784 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2207 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 902 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて、</src>` | 1473 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1194 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1875 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも、フローグラフを</src>` | 1896 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 1843 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあとはPythonコード</src>` | 1691 |
| 9 | `<src>にそこから</src>` | `<src>がそれから</src>` | 2131 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1220 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1523 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1710 |
| 13 | `<src>構造になっているからです。</src>` | `<src>機能になっているから</src>` | 1315 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1047 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 600 |
| 16 | `<src>じゃあ。</src>` | `<src>はい。じゃあ</src>` | 801 |

---

### Test Example 49 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 2063 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 789 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>인상 하는 흐름 을 보인 다면 </src>` | 1616 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 1227 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1741 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 1624 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 446 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1782 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 3452 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 711 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 2081 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이기 때문 에 </src>` | 1497 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 </src>` | 1609 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1261 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 670 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 735 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2033 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 860 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1631 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 1236 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1916 |
| 6 | `<src>but the reality </src>` | `<src>But the reality </src>` | 1737 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1773 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on </src>` | 1235 |
| 9 | `<src>block and because the </src>` | `<src>the block, and because </src>` | 2625 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 791 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 2018 </src>` | 2005 |
| 12 | `<src>years ago, </src>` | `<src>to years ago, </src>` | 1633 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1353 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 1080 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point is </src>` | 735 |
| 16 | `<src>held to a higher standard. </src>` | `<src>being held to a higher standard. </src>` | 777 |

---

### Test Example 51 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2336 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 785 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨다. </src>` | 1580 |
| 4 | `<src><\|wait\|></src>` | `<src>운전을 할 건 </src>` | 1218 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 1786 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>거로 거로 다니 고는 뭐 </src>` | 1928 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1821 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 1274 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장려 리예요. </src>` | 2815 |
| 10 | `<src>또 장렬이에요. </src>` | `<src><\|wait\|></src>` | 1611 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 재밌 겠네요. </src>` | 1822 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1010 |
| 13 | `<src>이제 </src>` | `<src><\|wait\|></src>` | 1279 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>열심히 모아봐요. 그거 는 </src>` | 1411 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>된 거 같아요. </src>` | 819 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 394 |

---

### Test Example 52 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2407 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 741 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 1592 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1198 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR </src>` | 1275 |
| 6 | `<src><\|wait\|></src>` | `<src>field being of critical </src>` | 688 |
| 7 | `<src>being of critical importance </src>` | `<src>importance </src>` | 1509 |
| 8 | `<src>versus variant </src>` | `<src>versus the </src>` | 514 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1683 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 1570 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2412 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1138 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree </src>` | 1739 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1556 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these </src>` | 1419 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1272 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 843 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 558 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 312 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1843 |
| 2 | `<src>首次觉知到</src>` | `<src>FlowOD的折扣</src>` | 902 |
| 3 | `<src>那个现象：</src>` | `<src>截止到那个限项，</src>` | 1583 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1201 |
| 5 | `<src><\|wait\|></src>` | `<src>美登我们储于</src>` | 1911 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 1816 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱的数值的爱，</src>` | 1837 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1397 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时</src>` | 2359 |
| 10 | `<src><\|wait\|></src>` | `<src>进入恨，</src>` | 1039 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 1765 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱，</src>` | 1390 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1467 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1173 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 669 |
| 16 | `<src>那个钟摆</src>` | `<src>那这种</src>` | 783 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 606 |
| 18 | `<src>继续在移动。</src>` | `<src>摆继续在移动。</src>` | 426 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2052 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 805 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1682 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1212 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1782 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1572 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 425 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1817 |
| 9 | `<src>a situation </src>` | `<src>a situation where </src>` | 2963 |
| 10 | `<src>where you realize </src>` | `<src>you realize </src>` | 1001 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1891 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1707 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know. </src>` | 1120 |
| 14 | `<src>and we can see about </src>` | `<src>Now we can see about </src>` | 1423 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1033 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 919 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 605 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 377 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1990 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 733 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1548 |
| 4 | `<src>He knows that </src>` | `<src>He knows that he's </src>` | 1313 |
| 5 | `<src>he's been without food, </src>` | `<src>knows that for he </src>` | 1823 |
| 6 | `<src><\|wait\|></src>` | `<src>been in the wilderness </src>` | 1717 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>forty days that he's hungry. </src>` | 1920 |
| 8 | `<src>And so he says </src>` | `<src>And so he says to </src>` | 1310 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus," Hey, </src>` | 2467 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it." </src>` | 1104 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1743 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1659 |
| 13 | `<src><\|wait\|></src>` | `<src>How did Jesus </src>` | 1273 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>deal with that? </src>` | 1154 |
| 15 | `<src>temptation? </src>` | `<src>He temptation. </src>` | 600 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 820 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, Jonathan led by </src>` | 608 |
| 18 | `<src>by bread alone. </src>` | `<src>brare alone. </src>` | 373 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2298 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 844 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1489 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1218 |
| 5 | `<src>came along </src>` | `<src>came along </src><br>` | 368 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1665 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1852 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1797 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1380 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2380 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 919 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1772 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1403 |
| 14 | `<src>the consensus </src>` | `<src><\|wait\|></src>` | 1492 |
| 15 | `<src><\|wait\|></src>` | `<src>the consensus </src>` | 1073 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 878 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 784 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 592 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 399 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 347 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 340 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2034 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 899 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1545 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 1282 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1818 |
| 6 | `<src>的部分。</src>` | `<src>客厅的部分，</src>` | 1652 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1115 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1001 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 2599 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1317 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 2047 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>是身体的部分</src>` | 1538 |
| 13 | `<src>也会反映的是</src>` | `<src>会反映的是</src>` | 980 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1335 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 1251 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以</src>` | 384 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>好好地坐下来休息，</src>` | 599 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 594 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的吗？</src>` | 372 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 309 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 360 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1878 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 852 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1587 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1197 |
| 5 | `<src><\|wait\|></src>` | `<src>completely </src>` | 1027 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>revolutionize the world. </src>` | 931 |
| 7 | `<src><\|wait\|></src>` | `<src>The personality of </src>` | 1792 |
| 8 | `<src>Their personality is </src>` | `<src>someone </src>` | 1758 |
| 9 | `<src>something of a </src>` | `<src>having a contradiction, </src>` | 552 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2840 |
| 11 | `<src>While they're </src>` | `<src>while they're </src>` | 913 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1998 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1523 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1271 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1161 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to </src>` | 1102 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 797 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 643 |
| 19 | `<src>play </src>` | `<src>play </src>` | 348 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, </src>` | 385 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 389 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 274 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 267 |
| 24 | `<src><\|wait\|></src>` | `<src>E.g., CP stands for </src>` | 283 |
| 25 | `<src>ENTP stands for </src>` | `<src>conservative. </src>` | 276 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 2310 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>경무를 거부 한 </src>` | 629 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1458 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1250 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1880 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1774 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 냈지만 </src>` | 1898 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>이제 는 </src>` | 1798 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2179 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1219 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1642 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 드러내 놓고 </src>` | 1592 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 를 </src>` | 1347 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1358 |
| 15 | `<src><\|wait\|></src>` | `<src>뜻끼를 품은 </src>` | 863 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 575 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 420 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 360 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 330 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 161 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납건. </src>` | 259 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 254 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 226 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 298 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 265 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2034 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 823 |
| 3 | `<src>今作ってる</src>` | `<src>作ってみたいです。なので</src>` | 1594 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>ここで</src>` | 483 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>このプロフェッショナルホテル</src>` | 964 |
| 6 | `<src>も</src>` | `<src>で朝食が</src>` | 1744 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1552 |
| 8 | `<src>になってる</src>` | `<src>になっている</src>` | 456 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっているので</src>` | 1801 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2599 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドーストーンホテル</src>` | 1400 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 2091 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なという方はですね</src>` | 1455 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1211 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>まあいいんじゃないか</src>` | 1327 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1088 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 776 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここのホテルからですね</src>` | 574 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 403 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 296 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 161 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかからないか</src>` | 371 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 280 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 352 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 189 |
| 26 | `<src>よかったらですね</src>` | `<src>寄ったらですね</src>` | 260 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 256 |
| 28 | `<src>ください</src>` | `<src>ください。それなら</src>` | 166 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は</src>` | 159 |
