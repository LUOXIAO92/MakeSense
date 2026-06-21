# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9499
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4238
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
  - PROCESS_TIME_MS_AVG: 1462.3470
  - PROCESS_TIME_MS_P50: 1464.3200
  - PROCESS_TIME_MS_P95: 2562.6150
  - PROCESS_TIME_MS_MAX: 3544.2940

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 2102 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>在声音里</src>` | 886 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个音量很大？</src>` | 1410 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 479 |
| 5 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 993 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放这个</src>` | 1047 |
| 7 | `<src>儿核桃</src>` | `<src>喝陶人，</src>` | 1051 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1591 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>感觉</src>` | 1889 |
| 10 | `<src>这种核桃</src>` | `<src>这些</src>` | 563 |
| 11 | `<src>仁儿。</src>` | `<src>和陶人。</src>` | 2038 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1758 |
| 2 | `<src>あの特に</src>` | `<src>あの</src>` | 770 |
| 3 | `<src>これなんかまだ</src>` | `<src>特に中学生</src>` | 1452 |
| 4 | `<src>一年生ですからね。</src>` | `<src>まだ一年生ですからね。</src>` | 1057 |
| 5 | `<src>この時点で</src>` | `<src>その時点で</src>` | 535 |
| 6 | `<src>こう短く</src>` | `<src>こう密告、</src>` | 1797 |
| 7 | `<src>剪定を</src>` | `<src>選挙を</src>` | 1538 |
| 8 | `<src><\|wait\|></src>` | `<src>こう対数して</src>` | 864 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>あげると</src>` | 1680 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 1240 |
| 11 | `<src>大した。</src>` | `<src>対数だ。</src>` | 2439 |

---

### Test Example 3 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 2007 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 803 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1535 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심이 </src>` | 1170 |
| 5 | `<src>옹심이가 </src>` | `<src>새우 용심이 가 </src>` | 974 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1212 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. 야 </src>` | 1638 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1907 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 646 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로 </src>` | 2480 |
| 11 | `<src>진짜. </src>` | `<src>조금 죽기 만 </src>` | 1207 |

---

### Test Example 4 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对</src>` | 1800 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>这种情况，</src>` | 858 |
| 3 | `<src>遇到问题</src>` | `<src>我们就是遇到问题</src>` | 1389 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管</src>` | 906 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 759 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们笑这个状况。</src>` | 1802 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1558 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1510 |
| 9 | `<src>独立承担。</src>` | `<src>工具理承担。</src>` | 1186 |
| 10 | `<src>整体而言，</src>` | `<src>责任而已，</src>` | 3202 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该做Solution。</src>` | 515 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단 에 있는 </src>` | 2415 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>직성들은 </src>` | 646 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1549 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1216 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1146 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 984 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>직성들이 </src>` | 1624 |
| 8 | `<src>때문 입니다. </src>` | `<src>되었기 때문 입니다. </src>` | 2189 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1065 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2419 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐던 교사 들은 </src>` | 671 |

---

### Test Example 6 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要气数</src>` | 2144 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的，</src>` | 766 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 1684 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有</src>` | 1019 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导</src>` | 924 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1173 |
| 7 | `<src>处于中间，</src>` | `<src>如何处于中间，</src>` | 1697 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2249 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1108 |
| 10 | `<src>要成为</src>` | `<src><\|wait\|></src>` | 2557 |
| 11 | `<src>一个师父。</src>` | `<src>要成为一个师傅，</src>` | 1250 |

---

### Test Example 7 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2167 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 790 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的 electrolyte</src>` | 1671 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也</src>` | 976 |
| 5 | `<src>然后</src>` | `<src>衰弱了，</src>` | 915 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 1242 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 1677 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 2250 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 1666 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是</src>` | 2127 |
| 11 | `<src>抑郁状态。</src>` | `<src>所谓的低于状态。</src>` | 1471 |

---

### Test Example 8 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your </src>` | 1870 |
| 2 | `<src>doing? </src>` | `<src>body saying? </src>` | 712 |
| 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 2108 |
| 4 | `<src>your body. </src>` | `<src>Where does </src>` | 743 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension </src>` | 1250 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 827 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 1625 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it tension in your chest? </src>` | 2279 |
| 9 | `<src>I ask them what </src>` | `<src>I have </src>` | 1396 |
| 10 | `<src><\|wait\|></src>` | `<src>a small wrench </src>` | 2362 |
| 11 | `<src>language are you using? </src>` | `<src>you use. </src>` | 1664 |

---

### Test Example 9 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1856 |
| 2 | `<src>Did very important research </src>` | `<src>important research </src>` | 798 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1770 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1198 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip the stem. </src>` | 1778 |
| 6 | `<src>research, </src>` | `<src>Research. </src>` | 1565 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 324 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2195 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 2023 |
| 10 | `<src>out there, </src>` | `<src>out there. </src>` | 1842 |
| 11 | `<src>people that we can learn from. </src>` | `<src>People that we can learn from. </src>` | 1753 |

---

### Test Example 10 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなど</src>` | 2286 |
| 2 | `<src>あの</src>` | `<src>があの</src>` | 708 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくという</src>` | 1576 |
| 4 | `<src>といったようなものも</src>` | `<src>ようなものも</src>` | 1130 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 960 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1186 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1677 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 2070 |
| 9 | `<src>えっと</src>` | `<src>で、</src>` | 447 |
| 10 | `<src><\|wait\|></src>` | `<src>何でしょうか。</src>` | 2683 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>内側がありますので</src>` | 957 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>お心お持ちください。</src>` | 3105 |

---

### Test Example 11 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2267 |
| 2 | `<src>家长需要做的是，</src>` | `<src>做的是</src>` | 725 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1717 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深沉的爱</src>` | 1315 |
| 5 | `<src>爱浇水、</src>` | `<src>交水，</src>` | 1727 |
| 6 | `<src>施肥，</src>` | `<src>十分</src>` | 1536 |
| 7 | `<src>给足</src>` | `<src>刻苦</src>` | 1036 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心灵养。</src>` | 1699 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3059 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>你耐心等</src>` | 629 |
| 11 | `<src>慢慢长大。</src>` | `<src>孩子慢慢长大。</src>` | 3089 |

---

### Test Example 12 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1817 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 846 |
| 3 | `<src><\|wait\|></src>` | `<src>天気</src>` | 432 |
| 4 | `<src>テキという設備寺が</src>` | `<src>と摂取量が</src>` | 1407 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたが、</src>` | 1075 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1133 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 915 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井氏の仕組み</src>` | 1686 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 2218 |
| 10 | `<src>は五経、</src>` | `<src>五項、</src>` | 1117 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2492 |
| 12 | `<src>設備寺、五比</src>` | `<src>摂取量、</src>` | 1101 |
| 13 | `<src>です。</src>` | `<src>五筆です。</src>` | 2359 |

---

### Test Example 13 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1873 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src><\|wait\|></src>` | 867 |
| 3 | `<src>촉발 시키고 </src>` | `<src>애플 을 켜 버리 슉슉 치고 </src>` | 2741 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 984 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1115 |
| 6 | `<src><\|wait\|></src>` | `<src>모든 을 </src>` | 1522 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>조깅 해려나 </src>` | 1886 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 796 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 3190 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 707 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 3013 |

---

### Test Example 14 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大体</src>` | 2087 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 815 |
| 3 | `<src>始めた</src>` | `<src>始まった</src>` | 1540 |
| 4 | `<src>もので、</src>` | `<src>もので</src>` | 1093 |
| 5 | `<src>ゴッホ、</src>` | `<src>防御、</src>` | 581 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1658 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1547 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザムヌ、</src>` | 1654 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 997 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の</src>` | 3455 |
| 11 | `<src>は、田舎の</src>` | `<src>絵、</src>` | 1215 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 2269 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2260 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 743 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1727 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learned to repeat. </src>` | 1233 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find out if you're good at </src>` | 1937 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1659 |
| 7 | `<src><\|wait\|></src>` | `<src>And what you </src>` | 2152 |
| 8 | `<src>And what you're not good at, </src>` | `<src>are not good at, </src>` | 690 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with </src>` | 3245 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1469 |
| 11 | `<src>And until next time. </src>` | `<src>it. And until next time. </src>` | 2038 |

---

### Test Example 16 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>あとなんか</src>` | 2453 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が離れてくる</src>` | 743 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>みたいな感じで</src>` | 1444 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オーシャラーとかタタガエっぱ</src>` | 1459 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1713 |
| 6 | `<src>開業したい方って</src>` | `<src>海泳したい方って</src>` | 1593 |
| 7 | `<src>すごい</src>` | `<src>すぐ泳ぎに行きたい</src>` | 1603 |
| 8 | `<src>自己意識高いし、</src>` | `<src>方、</src>` | 984 |
| 9 | `<src>自分で</src>` | `<src>ジムで</src>` | 2042 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>もっと本気で</src>` | 1717 |
| 11 | `<src>傾向が強いので、</src>` | `<src>頑張って泳ぐ</src>` | 1775 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1711 |

---

### Test Example 17 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2077 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 851 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 432 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと、</src>` | 1485 |
| 5 | `<src><\|wait\|></src>` | `<src>信号が消えなくなって</src>` | 1281 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>しまうので、</src>` | 1667 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1550 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 975 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1746 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついている</src>` | 2594 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 1046 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1602 |
| 13 | `<src>分解完了。</src>` | `<src>ハイ分解完了。</src>` | 1904 |

---

### Test Example 18 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1795 |
| 2 | `<src>映画でですね、</src>` | `<src>AAが</src>` | 888 |
| 3 | `<src>いろんな場面で</src>` | `<src>あるんですね。いろんな場面で</src>` | 1646 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>生生刻画とか</src>` | 1216 |
| 5 | `<src>調べるときに、</src>` | `<src>テザベるときに</src>` | 1632 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあAAのランクを</src>` | 492 |
| 7 | `<src>ことで、あの</src>` | `<src>調べて、</src>` | 1583 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>あの生生刻画とか</src>` | 2417 |
| 9 | `<src>保証する、生息である</src>` | `<src>を増減する、生刻で</src>` | 2936 |
| 10 | `<src>ことを保証する</src>` | `<src>いうことを保証するといった</src>` | 862 |
| 11 | `<src>といったような</src>` | `<src>わけ、使い方を</src>` | 1666 |
| 12 | `<src>使い方をされます。</src>` | `<src>定めました。</src>` | 1790 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1722 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 893 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相怪的人之间</src>` | 2163 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 812 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>有着某种心理，</src>` | 1790 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1576 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 785 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天夜里</src>` | 1869 |
| 9 | `<src><\|wait\|></src>` | `<src>开始的？</src>` | 2422 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1297 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思维</src>` | 1809 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 2025 |

---

### Test Example 20 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>다른 </src>` | 1854 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>산지 를 </src>` | 884 |
| 3 | `<src>해가지고 내가 </src>` | `<src>죽여달라고 해가지고 내가 </src>` | 1872 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 는 것도 </src>` | 1143 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>아스다. 다른 잔치 </src>` | 1845 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여달라고 해자 </src>` | 1701 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>안 되냐? 내가 </src>` | 2310 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>큰 소리 안 듣고 있는 </src>` | 2559 |
| 9 | `<src><\|wait\|></src>` | `<src>줄어드냐? </src>` | 1343 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>아 </src>` | 1873 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1912 |

---

### Test Example 21 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 2084 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chunhataru, </src>` | 767 |
| 3 | `<src>I am currently </src>` | `<src>and I'm currently studying </src>` | 2048 |
| 4 | `<src><\|wait\|></src>` | `<src>in A/B testing. </src>` | 985 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>Finance and </src>` | 1672 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>a touch of psychology. </src>` | 1620 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1560 |
| 8 | `<src>here at the ANU, </src>` | `<src>Yeah, here I am. </src>` | 1138 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3017 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>And in the future, I want to go into </src>` | 805 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2884 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consulting. </src>` | 1126 |

---

### Test Example 22 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 2001 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 739 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 1779 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1217 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1794 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1552 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 1306 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, </src>` | 1401 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 3158 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets used </src>` | 662 |
| 11 | `<src>or gets used to make </src>` | `<src>to make different bonds. </src>` | 2938 |
| 12 | `<src>different bonds. </src>` | `<src><\|wait\|></src>` | 1159 |

---

### Test Example 23 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1880 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 723 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个</src>` | 1692 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，</src>` | 1051 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够</src>` | 983 |
| 6 | `<src>在他下班的时候，</src>` | `<src>好自在的状态</src>` | 1130 |
| 7 | `<src>在做热汤</src>` | `<src>的时候，在做日航</src>` | 1697 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭，</src>` | 2189 |
| 9 | `<src><\|wait\|></src>` | `<src>就是说</src>` | 1827 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时背上</src>` | 2054 |
| 11 | `<src>小小的愿望</src>` | `<src>这四面一个小小的小小</src>` | 3159 |
| 12 | `<src>哈。</src>` | `<src>的愿望哈。</src>` | 1255 |

---

### Test Example 24 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1979 |
| 2 | `<src><\|wait\|></src>` | `<src>이걸 너무 </src>` | 807 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>절여 야 </src>` | 1759 |
| 4 | `<src><\|wait\|></src>` | `<src>할 수 있지만 진짜 보살 도요 </src>` | 1323 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 의 </src>` | 1781 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 </src>` | 1722 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 보이 고 </src>` | 2244 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1227 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보살 로 보이 려고 </src>` | 2589 |
| 10 | `<src>지금 나한테 </src>` | `<src>보여 주지 못하 는 </src>` | 3219 |
| 11 | `<src>보살 이라는데. </src>` | `<src>이 보살 이라는 게 </src>` | 1366 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1963 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 820 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>胡波乱跳，</src>` | 2023 |
| 4 | `<src>所以</src>` | `<src><\|wait\|></src>` | 937 |
| 5 | `<src>坚持不开刀。</src>` | `<src>所以坚持不开刀，</src>` | 1778 |
| 6 | `<src>期间</src>` | `<src>切肩大概</src>` | 1568 |
| 7 | `<src>大概有十位医生</src>` | `<src>有十二生</src>` | 754 |
| 8 | `<src>来诊断，</src>` | `<src>来剪断，</src>` | 1828 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 1386 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 2334 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1246 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 2147 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 1347 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Well, </src>` | 1956 |
| 2 | `<src>have to produce </src>` | `<src>if you have to produce </src>` | 896 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1686 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1136 |
| 5 | `<src>you realize that </src>` | `<src>you realize </src>` | 1335 |
| 6 | `<src>you don't even know how </src>` | `<src>that you don't even know </src>` | 767 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 1551 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. </src>` | 2195 |
| 9 | `<src>is this word </src>` | `<src>Like, oh, is this word </src>` | 1197 |
| 10 | `<src>spelled with a double </src>` | `<src>starting with </src>` | 2479 |
| 11 | `<src><\|wait\|></src>` | `<src>a double P, </src>` | 1088 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double L. I don't know </src>` | 2555 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1378 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2313 |
| 2 | `<src>The meaning of </src>` | `<src><\|wait\|></src>` | 729 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment </src>` | 2082 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore </src>` | 812 |
| 5 | `<src>history as a guide </src>` | `<src>its history as a guide </src>` | 1785 |
| 6 | `<src>to how political </src>` | `<src>to how </src>` | 1552 |
| 7 | `<src><\|wait\|></src>` | `<src>political change </src>` | 702 |
| 8 | `<src>change can happen </src>` | `<src>can happen </src>` | 1857 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1257 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2405 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1225 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 2347 |
| 13 | `<src>myriad. </src>` | `<src>I'mirred. </src>` | 1512 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1827 |
| 2 | `<src><\|wait\|></src>` | `<src>就是进入</src>` | 865 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二极管二极管，</src>` | 1601 |
| 4 | `<src>服务</src>` | `<src><\|wait\|></src>` | 1119 |
| 5 | `<src>在一级一线</src>` | `<src>复在一级一线</src>` | 803 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼上的大牛们。</src>` | 1463 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1605 |
| 8 | `<src><\|wait\|></src>` | `<src>呃，</src>` | 2287 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信号，</src>` | 1213 |
| 10 | `<src>发现</src>` | `<src>好事几年你会发现，</src>` | 2563 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信号</src>` | 1357 |
| 12 | `<src>的新榜反而</src>` | `<src>分分的新棒</src>` | 2113 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1524 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>扎了一个</src>` | 1769 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>线头，</src>` | 814 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 1547 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>找到了线头之后，</src>` | 1247 |
| 5 | `<src>请你务必就要</src>` | `<src>请务必</src>` | 981 |
| 6 | `<src><\|wait\|></src>` | `<src>抓住</src>` | 1072 |
| 7 | `<src>先守住，</src>` | `<src>手，</src>` | 1512 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，</src>` | 1617 |
| 9 | `<src><\|wait\|></src>` | `<src>那我</src>` | 897 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>再继续操作下去哦。</src>` | 2238 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1583 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么</src>` | 1424 |
| 13 | `<src><\|wait\|></src>` | `<src>我们这么讲？</src>` | 2054 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢，</src>` | 1548 |

---

### Test Example 30 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2352 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 732 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1791 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1093 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1765 |
| 6 | `<src>tells us to use </src>` | `<src>tells us </src>` | 323 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1498 |
| 8 | `<src>actually </src>` | `<src>to use actually </src>` | 2299 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1643 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2182 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1635 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game.coord array </src>` | 1891 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1658 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 2118 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이런 것들은 </src>` | 636 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 리튬을 </src>` | 1948 |
| 4 | `<src>이제 거진 </src>` | `<src>뭐 거의 </src>` | 877 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 금기 나 </src>` | 1836 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>금기 나랑 굉장히 </src>` | 1584 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 738 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연히 미네랄 이다. </src>` | 2067 |
| 9 | `<src>이렇게 </src>` | `<src>이거 </src>` | 3013 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>굉장히 </src>` | 592 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>그런 거죠. 이제 </src>` | 1583 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1914 |
| 13 | `<src>아연. </src>` | `<src>아견. </src>` | 1931 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1899 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개가 </src>` | 758 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중화 버스로 유명 미만 으로 </src>` | 2307 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 793 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1695 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1665 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 </src>` | 2011 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>성장 하거나 혹은 </src>` | 576 |
| 9 | `<src>걷게 되는데 </src>` | `<src>해화법에 그게 되는데 </src>` | 3383 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>이거 는 </src>` | 1230 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>소기업 들은 </src>` | 2255 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장 도 폐업 도 하지 않는 </src>` | 1429 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들 보이 게 된 거죠. </src>` | 1470 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2306 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这</src>` | 559 |
| 3 | `<src>在这个罗马呢</src>` | `<src>这个罗马呢，</src>` | 1874 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是以前造成的，</src>` | 1145 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1770 |
| 6 | `<src>你现在</src>` | `<src><\|wait\|></src>` | 1556 |
| 7 | `<src>所面临的一些</src>` | `<src>你现在有什么</src>` | 995 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>违规</src>` | 1555 |
| 9 | `<src>也不可能是</src>` | `<src>跟粉丝</src>` | 1449 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 2301 |
| 11 | `<src><\|wait\|></src>` | `<src>一起之间就</src>` | 1460 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 2081 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1688 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1273 |

---

### Test Example 34 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2337 |
| 2 | `<src><\|wait\|></src>` | `<src>새로 </src>` | 687 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 1536 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>이제 서름이 </src>` | 1141 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋은 자태 리 </src>` | 863 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>돋은 느낌 이 </src>` | 1365 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>들어서 </src>` | 1513 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1877 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 </src>` | 790 |
| 10 | `<src>물릴 거고 </src>` | `<src>너무 놀릴 </src>` | 2692 |
| 11 | `<src>신이 오면 </src>` | `<src>거고 미니 이면 </src>` | 983 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1553 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주라고 하니까 </src>` | 1887 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 2033 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1006 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1961 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这一张的部分，</src>` | 760 |
| 3 | `<src>一个在钓鱼</src>` | `<src>我们看到的是一个</src>` | 1768 |
| 4 | `<src>的人，但是</src>` | `<src>戴雪的人，但是</src>` | 1213 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是属于蜜香的。</src>` | 1774 |
| 6 | `<src>所以</src>` | `<src><\|wait\|></src>` | 1547 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>这通香花</src>` | 1483 |
| 8 | `<src>时候，就要去</src>` | `<src>这样的一个状况，</src>` | 1192 |
| 9 | `<src>特别注意，</src>` | `<src>需要特别注意的是，</src>` | 2713 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能</src>` | 914 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够得到</src>` | 2430 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他跳舞，</src>` | 1639 |
| 13 | `<src><\|wait\|></src>` | `<src>与他的意式</src>` | 1546 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 934 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1940 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 873 |
| 3 | `<src><\|wait\|></src>` | `<src>there was </src>` | 1569 |
| 4 | `<src>such interfaces before, </src>` | `<src>such instances </src>` | 1057 |
| 5 | `<src><\|wait\|></src>` | `<src>before. </src>` | 672 |
| 6 | `<src>netfilter, TC. </src>` | `<src>Next future TC </src>` | 1532 |
| 7 | `<src>Yeah, so </src>` | `<src><\|wait\|></src>` | 1669 |
| 8 | `<src>this is just </src>` | `<src>is just </src>` | 2249 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1389 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2457 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1462 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1917 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1364 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repos should be </src>` | 1358 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1184 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1938 |
| 2 | `<src>HTML이라고 </src>` | `<src>呃，</src>` | 669 |
| 3 | `<src><\|wait\|></src>` | `<src>HJL이라고 하는 </src>` | 1569 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피터도 </src>` | 1185 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 904 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1195 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1664 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 어 </src>` | 2244 |
| 9 | `<src>문법 에 </src>` | `<src>어노의 문법 을 </src>` | 1181 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>알게 우리 가 이제 </src>` | 2608 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>그것 들을 </src>` | 1400 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 2127 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그것 들을 </src>` | 1478 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1419 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 975 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who </src>` | 2227 |
| 2 | `<src>just getting going </src>` | `<src>is just getting going </src>` | 754 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1689 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1093 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I got ten of them </src>` | 1636 |
| 6 | `<src>that I think are </src>` | `<src>that are </src>` | 421 |
| 7 | `<src>really important. </src>` | `<src>really important </src>` | 1662 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2281 |
| 9 | `<src>I'm going to go into. </src>` | `<src>and I'm going to go </src>` | 1469 |
| 10 | `<src>I have about </src>` | `<src>and do I have about </src>` | 2354 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 1445 |
| 12 | `<src>that follow this video </src>` | `<src>at follow this video </src>` | 2051 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one </src>` | 1540 |
| 14 | `<src>that cover each one </src>` | `<src><\|wait\|></src>` | 1344 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1016 |

---

### Test Example 39 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2216 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 743 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1786 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1001 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 1043 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1103 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 1615 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. </src>` | 2179 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 1198 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And if so, </src>` | 2561 |
| 11 | `<src>That's another level of </src>` | `<src>did you graduate? </src>` | 1398 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 2260 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1843 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1253 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 871 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2333 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 592 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 1689 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正财的部分</src>` | 1198 |
| 5 | `<src>也就是</src>` | `<src>。也就是</src>` | 1717 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的业绩</src>` | 1579 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>相当大的</src>` | 966 |
| 8 | `<src>与收入的</src>` | `<src>主导的行业收入的</src>` | 1801 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果</src>` | 2891 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资理财方面</src>` | 722 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 2525 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1407 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说，</src>` | 1620 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了</src>` | 1014 |
| 15 | `<src><\|wait\|></src>` | `<src>一点。</src>` | 879 |

---

### Test Example 41 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>実は</src>` | 1943 |
| 2 | `<src>十一二手とか</src>` | `<src>一二手とか</src>` | 889 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>ですか？</src>` | 1533 |
| 4 | `<src>十秒で。</src>` | `<src>おそらく十秒で</src>` | 1143 |
| 5 | `<src>まあ</src>` | `<src><\|wait\|></src>` | 670 |
| 6 | `<src>一秒に</src>` | `<src>まあ一秒に</src>` | 1550 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一秒ぐらいの</src>` | 1691 |
| 8 | `<src>計算ですか</src>` | `<src>せっかく</src>` | 2236 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1386 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2365 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1290 |
| 12 | `<src><\|wait\|></src>` | `<src>十</src>` | 2036 |
| 13 | `<src>十一二手で</src>` | `<src>一二日で</src>` | 1317 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1107 |
| 15 | `<src>宮馬とかが</src>` | `<src>見合う馬とかが</src>` | 1134 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 770 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2053 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어치 보면 </src>` | 917 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 2145 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 815 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1786 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 도 가족 같은 </src>` | 1608 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>동생 이잖아. </src>` | 1366 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1141 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 1053 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 한 거다는 </src>` | 2599 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 1314 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 2151 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1219 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1178 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고 </src>` | 1069 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>생각 했습니다. </src>` | 930 |

---

### Test Example 43 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어 가면 </src>` | 2175 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해매 입니다. </src>` | 885 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1701 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 온 거 </src>` | 1035 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 걸어 다니 고 </src>` | 1092 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>그러 게 </src>` | 995 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 1656 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 2218 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 인의 나가 는 것도 </src>` | 381 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장려 리요. </src>` | 3130 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 치안 이요. </src>` | 555 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 3016 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1285 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모여 봐요. </src>` | 1262 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 된 거 같아요. </src>` | 1307 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 822 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね</src>` | 2208 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 768 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>と言だったりして</src>` | 1766 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルPython</src>` | 1098 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 1764 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも</src>` | 338 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルンを</src>` | 1552 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>書いてあとそれは</src>` | 2127 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコード</src>` | 383 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されるって</src>` | 3362 |
| 11 | `<src>実行されることで</src>` | `<src>それが実行されることで</src>` | 1141 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるっていう</src>` | 2381 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているから</src>` | 1402 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1265 |
| 15 | `<src>はい。</src>` | `<src>です。</src>` | 1025 |
| 16 | `<src>じゃあ。</src>` | `<src>はいじゃあ</src>` | 1156 |

---

### Test Example 45 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2031 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう蒸らせてやれ。</src>` | 992 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 1534 |
| 4 | `<src><\|wait\|></src>` | `<src>今</src>` | 1037 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>引き締めを見ている。</src>` | 728 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1495 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1699 |
| 8 | `<src><\|wait\|></src>` | `<src>超に超えている</src>` | 2270 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈火勢気よ。</src>` | 1465 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2294 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1427 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなでいくを</src>` | 2129 |
| 13 | `<src>が、</src>` | `<src>やっている</src>` | 1681 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなに</src>` | 1208 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>すごい海賊線を</src>` | 1000 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 888 |

---

### Test Example 46 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1966 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 </src>` | 758 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 </src>` | 1686 |
| 4 | `<src>있을 때에 </src>` | `<src>이방인 으로 있을 때에 </src>` | 1316 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 1739 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하는 우상 에게로 </src>` | 1723 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 그대로 </src>` | 2272 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 1680 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2170 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 </src>` | 1432 |
| 11 | `<src>너희 에게 </src>` | `<src>내가 너희에게 </src>` | 2080 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1884 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1183 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 945 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 760 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2146 |
| 2 | `<src>Activity than </src>` | `<src>Activity, </src>` | 710 |
| 3 | `<src>self-defining what we think </src>` | `<src>then self-defining </src>` | 1820 |
| 4 | `<src>the standard is because you're </src>` | `<src>what we think that standard is, </src>` | 1299 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1779 |
| 6 | `<src>but the reality </src>` | `<src><\|wait\|></src>` | 1622 |
| 7 | `<src>is is that </src>` | `<src>But the reality is that </src>` | 2285 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new cat </src>` | 1310 |
| 9 | `<src>block and because the </src>` | `<src>in the block, </src>` | 2475 |
| 10 | `<src>standards have </src>` | `<src>and because the standards have </src>` | 1486 |
| 11 | `<src>changed from 20 </src>` | `<src><\|wait\|></src>` | 1908 |
| 12 | `<src>years ago, </src>` | `<src>changed from 20 years ago, </src>` | 1479 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1441 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard </src>` | 976 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 960 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to </src>` | 264 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1894 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 733 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놓았습니다. </src>` | 2185 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 646 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>이 로쿠자 의 분석 을 보시면 </src>` | 1864 |
| 6 | `<src>소니가 </src>` | `<src>소니 가 </src>` | 1584 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 칩에 </src>` | 1036 |
| 8 | `<src>파이프 를 </src>` | `<src>FPD 파이프 를 </src>` | 1735 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 3311 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나충가서 로 보인 다. </src>` | 878 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2569 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스 박스 시리즈, 엑스에서도 없는 </src>` | 1506 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1178 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시, </src>` | 1282 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>S2가 여기 도 없다. </src>` | 1065 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 649 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2203 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩和感觉</src>` | 766 |
| 3 | `<src>的感情或</src>` | `<src>对手的感情</src>` | 1693 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的。</src>` | 1117 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1441 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 554 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常会</src>` | 1698 |
| 8 | `<src>会听到人们</src>` | `<src>听到人们这样说：“</src>` | 2404 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 2284 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1417 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1739 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在胡闹了。”</src>` | 1886 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1805 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1112 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 944 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 750 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 633 |

---

### Test Example 50 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 2021 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 886 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. </src>` | 1652 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 1339 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1790 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨턴트 예요. </src>` | 1835 |
| 7 | `<src><\|wait\|></src>` | `<src>이게 컨설턴트 </src>` | 2280 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>여가지고 </src>` | 1452 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2376 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2808 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>줬을 때 </src>` | 1148 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1601 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 938 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로 사이트 스크립트 에서 </src>` | 1017 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>X 파일 까지 </src>` | 746 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까 </src>` | 651 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 2302 |
| 2 | `<src><\|wait\|></src>` | `<src>인증 상승 하는 </src>` | 503 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다음에 </src>` | 2062 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 977 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1681 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 </src>` | 1602 |
| 7 | `<src>먼저 </src>` | `<src>하겠지만 먼저 </src>` | 1770 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 897 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 3544 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 1488 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 1905 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 </src>` | 1420 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 </src>` | 1188 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>욕기 총이 가벼운 종목 을 </src>` | 1312 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 997 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 706 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>Fourth of </src>` | 1792 |
| 2 | `<src>首次觉知到</src>` | `<src>the month </src>` | 796 |
| 3 | `<src>那个现象：</src>` | `<src>to conclude that </src>` | 1571 |
| 4 | `<src>每当我们</src>` | `<src>the vision </src>` | 1100 |
| 5 | `<src><\|wait\|></src>` | `<src>is to </src>` | 670 |
| 6 | `<src>处于爱之中，</src>` | `<src>love, </src>` | 1525 |
| 7 | `<src>所谓的爱，</src>` | `<src>so-called love. </src>` | 1716 |
| 8 | `<src>我们也</src>` | `<src>We also </src>` | 2291 |
| 9 | `<src>同时进入恨。</src>` | `<src>enter the </src>` | 1464 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2297 |
| 11 | `<src>在早上的时候，</src>` | `<src>heat in the summer </src>` | 1677 |
| 12 | `<src>它是爱；</src>` | `<src>when it's hot. </src>` | 1911 |
| 13 | `<src>到了晚上，</src>` | `<src>It's</src>` | 1786 |
| 14 | `<src>它就变成恨。</src>` | `<src>down in the evening, </src>` | 1146 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 912 |
| 16 | `<src>那个钟摆</src>` | `<src>that cold, </src>` | 873 |
| 17 | `<src><\|wait\|></src>` | `<src>that stays </src>` | 634 |
| 18 | `<src>继续在移动。</src>` | `<src>in the night. </src>` | 480 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2164 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 720 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to move </src>` | 2206 |
| 4 | `<src>move media objects </src>` | `<src>meedia objects </src>` | 757 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1786 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources </src>` | 1559 |
| 7 | `<src>So, if </src>` | `<src>though, </src>` | 856 |
| 8 | `<src>you get into </src>` | `<src>if you get into </src>` | 1778 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 2287 |
| 10 | `<src>where you realize </src>` | `<src>where you realize you've added </src>` | 1481 |
| 11 | `<src>you've added the wrong media </src>` | `<src><\|wait\|></src>` | 2764 |
| 12 | `<src>files to a particular resource, </src>` | `<src>the wrong media files </src>` | 1434 |
| 13 | `<src>you need to let us know, </src>` | `<src>to a particular resource, </src>` | 1427 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1222 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 893 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files </src>` | 483 |
| 17 | `<src>get backed up </src>` | `<src>and then making sure they get back up </src>` | 905 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 235 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 2173 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 481 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1707 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1018 |
| 5 | `<src>he's been without food, </src>` | `<src>he's going to </src>` | 1104 |
| 6 | `<src><\|wait\|></src>` | `<src>be in the wilderness </src>` | 1034 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>for forty days </src>` | 1577 |
| 8 | `<src>And so he says </src>` | `<src>that he's hungry, </src>` | 2292 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>and so he says to Jesus, </src>` | 1315 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>Hey, if you're the Son of God, prove it. </src>` | 2723 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3012 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread. </src>` | 1365 |
| 13 | `<src><\|wait\|></src>` | `<src>How did </src>` | 1156 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>Jesus deal with that? </src>` | 1074 |
| 15 | `<src>temptation? </src>` | `<src>The temptation. </src>` | 805 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 719 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, Jonathan </src>` | 636 |
| 18 | `<src>by bread alone. </src>` | `<src>lead by bread alone. </src>` | 518 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2489 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 615 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1795 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1042 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the AHR field </src>` | 1591 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 447 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1601 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 1458 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1114 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 2681 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1046 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that </src>` | 2780 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>if we don't agree </src>` | 1481 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1200 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in </src>` | 1046 |
| 16 | `<src>data sources that we can </src>` | `<src>these data sources </src>` | 873 |
| 17 | `<src>draw from, </src>` | `<src>that we can draw from. </src>` | 786 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>There's nothing to draw from, right? </src>` | 977 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 285 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2355 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful </src>` | 689 |
| 3 | `<src>right, </src>` | `<src>individual write, </src>` | 1554 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1184 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 920 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I don't know </src>` | 1344 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1605 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2036 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 468 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2791 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 814 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1579 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1888 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1616 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1248 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 911 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 926 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 643 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 474 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 288 |
| 21 | `<src>who. </src>` | `<src>who </src>` | 151 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我們看一下</src>` | 1980 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的圖片哦，</src>` | 876 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1702 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>圖片的部分呢，</src>` | 1092 |
| 5 | `<src>的一个是客厅</src>` | `<src>我們可以看到</src>` | 1046 |
| 6 | `<src>的部分。</src>` | `<src>一個是客廳的部分，</src>` | 1077 |
| 7 | `<src>那客厅一般</src>` | `<src>客廳一般</src>` | 1555 |
| 8 | `<src>都是属于</src>` | `<src>都是屬於</src>` | 2225 |
| 9 | `<src>我们</src>` | `<src>我們在</src>` | 537 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 2993 |
| 11 | `<src><\|wait\|></src>` | `<src>休息的地方，</src>` | 675 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，</src>` | 2890 |
| 13 | `<src>也会反映的是</src>` | `<src>是身體的部分會反應的是</src>` | 1476 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要</src>` | 1174 |
| 15 | `<src>一点时间，</src>` | `<src>给自己一點時間</src>` | 1056 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好地做</src>` | 861 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>下洗去，</src>` | 568 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我們可以看到這邊是</src>` | 754 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>消防員的嘛。</src>` | 382 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 229 |
| 21 | `<src>所以是说。</src>` | `<src>所以是說。</src>` | 348 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1949 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 755 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1682 |
| 4 | `<src>show up to </src>` | `<src>grow up </src>` | 1006 |
| 5 | `<src><\|wait\|></src>` | `<src>to completely </src>` | 826 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>revolutionize the world. </src>` | 1370 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1623 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 2255 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1499 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2278 |
| 11 | `<src>While they're </src>` | `<src>Well, they're </src>` | 1441 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted. </src>` | 2035 |
| 13 | `<src>they also hate </src>` | `<src>They also hate </src>` | 1467 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations. </src>` | 1495 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 953 |
| 16 | `<src><\|wait\|></src>` | `<src>And like to get straight to </src>` | 958 |
| 17 | `<src>get straight to the point. </src>` | `<src>the point. </src>` | 647 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 447 |
| 19 | `<src>play </src>` | `<src>to play </src>` | 306 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, </src>` | 348 |
| 21 | `<src><\|wait\|></src>` | `<src>and never shy away </src>` | 251 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 292 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 254 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 357 |
| 25 | `<src>ENTP stands for </src>` | `<src>for. </src>` | 253 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 의 이준석은 </src>` | 2491 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무 를 </src>` | 282 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>거부 한 명분 이 후보 를 </src>` | 2272 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 하면서 </src>` | 627 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 1793 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 하면서 </src>` | 1564 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1176 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1566 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 3178 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 557 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 3026 |
| 12 | `<src>이준석은 </src>` | `<src>이준석 은 들은 해놓고 </src>` | 1350 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 </src>` | 1193 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>를 떨어뜨리 겠다는 </src>` | 1275 |
| 15 | `<src><\|wait\|></src>` | `<src>뜻끼를 품은 </src>` | 923 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 387 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 646 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 452 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 306 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 292 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석 성상납건 </src>` | 281 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 269 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 289 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기 </src>` | 318 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재 입니까? </src>` | 307 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>でまあ</src>` | 2091 |
| 2 | `<src>食堂ね</src>` | `<src>食後の</src>` | 800 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってみたいな</src>` | 1644 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>です。なので</src>` | 1119 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ここのねゴルフスコンホテル</src>` | 1145 |
| 6 | `<src>も</src>` | `<src>も朝食が</src>` | 1043 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1602 |
| 8 | `<src>になってる</src>` | `<src>になっている</src>` | 2278 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっているので</src>` | 1312 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2389 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルフスコンホテル</src>` | 1325 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいな</src>` | 2150 |
| 13 | `<src>なっていう方はですね</src>` | `<src>という方はですね</src>` | 1285 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 1216 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てまあいいんじゃない</src>` | 1196 |
| 16 | `<src><\|wait\|></src>` | `<src>なと</src>` | 924 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 335 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここホテルからですね</src>` | 647 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 433 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 311 |
| 21 | `<src>歩いて一分</src>` | `<src>一本かかるか</src>` | 318 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんでないか</src>` | 282 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 282 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地ねまあホテル</src>` | 294 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 311 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 273 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさって</src>` | 155 |
| 28 | `<src>ください</src>` | `<src>みてください。それでは</src>` | 186 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね</src>` | 136 |
