# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9456
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.3113
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
  - PROCESS_TIME_MS_AVG: 1417.9840
  - PROCESS_TIME_MS_P50: 1423.3170
  - PROCESS_TIME_MS_P95: 2206.7140
  - PROCESS_TIME_MS_MAX: 12735.5960

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
| 1 | `<src><\|wait\|></src>` | `<src>为什么</src>` | 2106 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>的总结点，</src>` | 1540 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个优选也很大。</src>` | 1029 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1270 |
| 5 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 258 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在</src>` | 1291 |
| 7 | `<src>儿核桃</src>` | `<src>面对和陶人</src>` | 1541 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 982 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>这个领域，</src>` | 1445 |
| 10 | `<src>这种核桃</src>` | `<src>这种和陶人</src>` | 1933 |
| 11 | `<src>仁儿。</src>` | `<src><\|wait\|></src>` | 2176 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2030 |
| 2 | `<src>家长需要做的是，</src>` | `<src>做的是</src>` | 1780 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 820 |
| 4 | `<src>用我们深深的</src>` | `<src>深沉的爱交</src>` | 1301 |
| 5 | `<src>爱浇水、</src>` | `<src>水，</src>` | 1357 |
| 6 | `<src>施肥，</src>` | `<src>十倍</src>` | 750 |
| 7 | `<src>给足</src>` | `<src>给</src>` | 1170 |
| 8 | `<src>孩子心理营养，</src>` | `<src>做孩子心灵营养。</src>` | 1855 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 626 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>细腻心，</src>` | 2030 |
| 11 | `<src>慢慢长大。</src>` | `<src>等孩子慢慢长大。</src>` | 1798 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1648 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1525 |
| 3 | `<src>これなんかまだ</src>` | `<src>仲まだ</src>` | 948 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 859 |
| 5 | `<src>この時点で</src>` | `<src>はいはいはい。</src>` | 678 |
| 6 | `<src>こう短く</src>` | `<src>この時期に</src>` | 1517 |
| 7 | `<src>剪定を</src>` | `<src>資格選択を</src>` | 1796 |
| 8 | `<src><\|wait\|></src>` | `<src>こう</src>` | 1756 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>退ずしていたら</src>` | 694 |
| 10 | `<src>十年経っても</src>` | `<src>一年経っても</src>` | 2016 |
| 11 | `<src>大した。</src>` | `<src>退ずた。</src>` | 1722 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要气数</src>` | 1936 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的，</src>` | 1844 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 845 |
| 4 | `<src>只有一个师父</src>` | `<src>但是只有</src>` | 1178 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导到</src>` | 1401 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1487 |
| 7 | `<src>处于中间，</src>` | `<src>炉出余中线。</src>` | 1098 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1256 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 1135 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2101 |
| 11 | `<src>一个师父。</src>` | `<src>一个师傅，</src>` | 1161 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大体</src>` | 1985 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1525 |
| 3 | `<src>始めた</src>` | `<src>始まったもので、</src>` | 959 |
| 4 | `<src>もので、</src>` | `<src><\|wait\|></src>` | 977 |
| 5 | `<src>ゴッホ、</src>` | `<src>ご法</src>` | 497 |
| 6 | `<src>ゴーギャン、</src>` | `<src>五減</src>` | 1370 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1525 |
| 8 | `<src>セザンヌ、</src>` | `<src>細身の</src>` | 804 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 1632 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどという人の</src>` | 1493 |
| 11 | `<src>は、田舎の</src>` | `<src><\|wait\|></src>` | 2557 |
| 12 | `<src>中学生でも。</src>` | `<src>岩中の</src>` | 827 |

---

### Test Example 6 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2069 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 1499 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくという</src>` | 940 |
| 4 | `<src>といったようなものも</src>` | `<src>ようなものも</src>` | 865 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので、ぜひ</src>` | 726 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 1386 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1506 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 1224 |
| 9 | `<src>えっと</src>` | `<src>て、えっと</src>` | 1156 |
| 10 | `<src><\|wait\|></src>` | `<src>連絡の</src>` | 1446 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>通知の案内がありますので、</src>` | 2645 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>少々お待ちください。</src>` | 1179 |

---

### Test Example 7 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1912 |
| 2 | `<src>옹심이, </src>` | `<src>용신이 </src>` | 1880 |
| 3 | `<src><\|wait\|></src>` | `<src>칼 </src>` | 724 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>용신 이 </src>` | 1279 |
| 5 | `<src>옹심이가 </src>` | `<src>어설 용신이 가 </src>` | 1390 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1442 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>석연 하는 건데요. </src>` | 1056 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1378 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1345 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해경으로 조금 죽입니다. </src>` | 2922 |
| 11 | `<src>진짜. </src>` | `<src>진짜 </src>` | 1249 |

---

### Test Example 8 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1610 |
| 2 | `<src><\|wait\|></src>` | `<src>回到我</src>` | 1503 |
| 3 | `<src>回到我生活</src>` | `<src>生活在一个</src>` | 986 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>鬼岛哈，让我</src>` | 1130 |
| 5 | `<src>让我能够哈，</src>` | `<src>能够好在它</src>` | 455 |
| 6 | `<src>在他下班的时候，</src>` | `<src>下山的时候，</src>` | 1391 |
| 7 | `<src>在做热汤</src>` | `<src>在座日</src>` | 1514 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>躺在</src>` | 1077 |
| 9 | `<src><\|wait\|></src>` | `<src>网格里，我当时</src>` | 1342 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>被它用</src>` | 1690 |
| 11 | `<src>小小的愿望</src>` | `<src>一个小小的一个愿望哈，</src>` | 2403 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 1339 |

---

### Test Example 9 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>淘撒完以后，</src>` | 2005 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src><\|wait\|></src>` | 1811 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>那内部的叶片</src>` | 919 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>清洁能量</src>` | 1154 |
| 5 | `<src>然后</src>` | `<src>也刷出来了，</src>` | 1422 |
| 6 | `<src>就停留在一个</src>` | `<src>然后就停留在</src>` | 1750 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 1367 |
| 8 | `<src>能量的运行</src>` | `<src>一个相对的低能量的</src>` | 899 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 2062 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1977 |
| 11 | `<src>抑郁状态。</src>` | `<src>逆流状态。</src>` | 1431 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>因为</src>` | 1772 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>这个情况，我们就是</src>` | 1666 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题，</src>` | 900 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的</src>` | 1330 |
| 5 | `<src>或是通知对方，</src>` | `<src>汇报主管，或是通知对方</src>` | 1387 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我一下</src>` | 869 |
| 7 | `<src>不要想自己</src>` | `<src>这个状况，不要想自己</src>` | 1347 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1847 |
| 9 | `<src>独立承担。</src>` | `<src>抗下来，</src>` | 1924 |
| 10 | `<src>整体而言，</src>` | `<src>你理财承担，</src>` | 2203 |
| 11 | `<src>事业运就属凶。</src>` | `<src>责任而已，</src>` | 1499 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1744 |
| 2 | `<src>Did very important research </src>` | `<src>important research </src>` | 1653 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 890 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people? This is </src>` | 1355 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1436 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 1448 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at 10% </src>` | 1123 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1412 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 2074 |
| 10 | `<src>out there, </src>` | `<src>out there, people like </src>` | 2081 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1598 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your </src>` | 1663 |
| 2 | `<src>doing? </src>` | `<src>body saying? </src>` | 1730 |
| 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 946 |
| 4 | `<src>your body. </src>` | `<src>Where does </src>` | 1190 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension start? </src>` | 1368 |
| 6 | `<src>start? What is it? </src>` | `<src>What is it? Is it </src>` | 1444 |
| 7 | `<src>Is it a headache? </src>` | `<src>a head day? </src>` | 817 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it tension in your chest? </src>` | 1838 |
| 9 | `<src>I ask them what </src>` | `<src>Or is it </src>` | 2009 |
| 10 | `<src><\|wait\|></src>` | `<src>a lower back where you use </src>` | 2107 |
| 11 | `<src>language are you using? </src>` | `<src>saying? </src>` | 1765 |

---

### Test Example 13 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1768 |
| 2 | `<src>映画でですね、</src>` | `<src>Aが</src>` | 1483 |
| 3 | `<src>いろんな場面で</src>` | `<src>あるんですね。いろんな場面で</src>` | 1089 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>生食かどうか</src>` | 1338 |
| 5 | `<src>調べるときに、</src>` | `<src>っていう場合</src>` | 1043 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>にAの欄を</src>` | 680 |
| 7 | `<src>ことで、あの</src>` | `<src>調べて、あの</src>` | 1704 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>生食かどうか</src>` | 1813 |
| 9 | `<src>保証する、生息である</src>` | `<src>を</src>` | 1093 |
| 10 | `<src>ことを保証する</src>` | `<src>生食であることを保証する</src>` | 2571 |
| 11 | `<src>といったような</src>` | `<src>といった使い方を</src>` | 743 |
| 12 | `<src>使い方をされます。</src>` | `<src>されています。</src>` | 1803 |

---

### Test Example 14 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>So this </src>` | 1804 |
| 2 | `<src>そこで</src>` | `<src>so here, </src>` | 1533 |
| 3 | `<src><\|wait\|></src>` | `<src>they think </src>` | 943 |
| 4 | `<src>テキという設備寺が</src>` | `<src>to use 7.8 gigas </src>` | 1123 |
| 5 | `<src>ありましたね。</src>` | `<src>of memory, right? </src>` | 454 |
| 6 | `<src>で、</src>` | `<src>So </src>` | 1290 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1518 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>the process of </src>` | 808 |
| 9 | `<src><\|wait\|></src>` | `<src>the CPU </src>` | 1622 |
| 10 | `<src>は五経、</src>` | `<src>moving </src>` | 1221 |
| 11 | `<src><\|wait\|></src>` | `<src>7.8 gigas </src>` | 2866 |
| 12 | `<src>設備寺、五比</src>` | `<src><\|wait\|></src>` | 884 |
| 13 | `<src>です。</src>` | `<src>of memory. </src>` | 1833 |

---

### Test Example 15 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>다른 </src>` | 1820 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>선지 를 </src>` | 1785 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주게 달래 야가지고 내가 </src>` | 1066 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길래 </src>` | 1166 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>주로 들어왔 수가 </src>` | 1451 |
| 6 | `<src>죽여 달라 </src>` | `<src>다른 잔지 문제 를 </src>` | 1770 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>달래 자는 거야. 내가 </src>` | 1909 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그런 소리 </src>` | 1277 |
| 9 | `<src><\|wait\|></src>` | `<src>안 듣고 있는 줄 알았는 거야. </src>` | 3007 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 1118 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 1649 |

---

### Test Example 16 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1691 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 1791 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相不够的</src>` | 948 |
| 4 | `<src><\|wait\|></src>` | `<src>人之间，</src>` | 1228 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>又这么重要</src>` | 1422 |
| 6 | `<src>难道会是</src>` | `<src>人际，</src>` | 1535 |
| 7 | `<src><\|wait\|></src>` | `<src>难道会是</src>` | 862 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里</src>` | 1548 |
| 9 | `<src><\|wait\|></src>` | `<src>开始的？</src>` | 1509 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2565 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 1133 |
| 12 | `<src>连篇。</src>` | `<src>学历年偏。</src>` | 1760 |

---

### Test Example 17 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1868 |
| 2 | `<src><\|wait\|></src>` | `<src>이럴지 너무 </src>` | 1884 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>이 저희 할 일 수 있지만 </src>` | 947 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 들요 </src>` | 1216 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 의 </src>` | 1475 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 </src>` | 1932 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 하고 있고 </src>` | 1705 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 1187 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보살 로 보일 피라고 </src>` | 2952 |
| 10 | `<src>지금 나한테 </src>` | `<src>보이 세 우주 가 지던지 보살 이란 </src>` | 1307 |
| 11 | `<src>보살 이라는데. </src>` | `<src><\|wait\|></src>` | 1758 |

---

### Test Example 18 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단 에 </src>` | 2108 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>있는 닉스들은 </src>` | 1991 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 641 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1357 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1508 |
| 6 | `<src>무작위로 </src>` | `<src>않았고 무작위 로 </src>` | 1926 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>뽑힌 닉스들이 </src>` | 1847 |
| 8 | `<src>때문 입니다. </src>` | `<src>있었기 때문 입니다. </src>` | 2258 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1911 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사시를 </src>` | 1386 |
| 11 | `<src>교사 들은. </src>` | `<src>모을 랐던 교사 들은 </src>` | 2029 |

---

### Test Example 19 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 2145 |
| 2 | `<src>and then </src>` | `<src>and then after </src>` | 1721 |
| 3 | `<src>after these examples, </src>` | `<src>these examples, </src>` | 834 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1284 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 942 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 801 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1704 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1754 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 681 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1997 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1715 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game.coord array </src>` | 1677 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1735 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1884 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chunaru Tsuruta. </src>` | 2069 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 684 |
| 4 | `<src><\|wait\|></src>` | `<src>in AI, </src>` | 1174 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>back-end finance, </src>` | 1462 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a bit of </src>` | 1679 |
| 7 | `<src><\|wait\|></src>` | `<src>psychology. </src>` | 1500 |
| 8 | `<src>here at the ANU, </src>` | `<src>Here at YU, </src>` | 767 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 2171 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 1979 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate </src>` | 1719 |
| 12 | `<src>corporate consultancy. </src>` | `<src>consultancy. </src>` | 1655 |

---

### Test Example 21 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2073 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1739 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 840 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learned to repeat, </src>` | 1346 |
| 5 | `<src>Find what you're good at </src>` | `<src>find out you're good at </src>` | 1569 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1832 |
| 7 | `<src><\|wait\|></src>` | `<src>And when you're not </src>` | 1942 |
| 8 | `<src>And what you're not good at, </src>` | `<src>good at it, </src>` | 1507 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with </src>` | 2708 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1644 |
| 11 | `<src>And until next time. </src>` | `<src>it, and then tell next time </src>` | 1814 |

---

### Test Example 22 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个</src>` | 1793 |
| 2 | `<src><\|wait\|></src>` | `<src>就是进入</src>` | 1477 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二期市场，</src>` | 1013 |
| 4 | `<src>服务</src>` | `<src>会服务</src>` | 863 |
| 5 | `<src>在一级一线</src>` | `<src>在一期一线</src>` | 637 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 1653 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1593 |
| 8 | `<src><\|wait\|></src>` | `<src>在做</src>` | 1871 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>微信运动</src>` | 763 |
| 10 | `<src>发现</src>` | `<src>好事企业，你会发现</src>` | 2321 |
| 11 | `<src>给微信公众号评分</src>` | `<src>微信运动</src>` | 1337 |
| 12 | `<src>的新榜反而</src>` | `<src>非常好平分的</src>` | 1755 |
| 13 | `<src>火了。</src>` | `<src>星棒活动了。</src>` | 1708 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1758 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1860 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds also store </src>` | 854 |
| 4 | `<src>also store energy, </src>` | `<src>energy. And when those </src>` | 1289 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1498 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy gets </src>` | 1708 |
| 7 | `<src>gets converted to </src>` | `<src>converted to other </src>` | 1852 |
| 8 | `<src>other types of energy, </src>` | `<src>types of energy, </src>` | 685 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 2190 |
| 10 | `<src><\|wait\|></src>` | `<src>Or gets used </src>` | 1547 |
| 11 | `<src>or gets used to make </src>` | `<src>to make different bonds, </src>` | 1768 |
| 12 | `<src>different bonds. </src>` | `<src><\|wait\|></src>` | 1701 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2069 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 1481 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 984 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと</src>` | 430 |
| 5 | `<src><\|wait\|></src>` | `<src>信号が消えが</src>` | 1186 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>できなくなってしまうので、</src>` | 1564 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1698 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 1806 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1204 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いている</src>` | 2198 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 1009 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 1881 |
| 13 | `<src>分解完了。</src>` | `<src>ハイ分解完了。</src>` | 1722 |

---

### Test Example 25 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>アドワンさん</src>` | 2130 |
| 2 | `<src>距離が</src>` | `<src>ちょっと距離が離れてくる</src>` | 1995 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>みたいな感じで</src>` | 648 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オーシャラとか</src>` | 1289 |
| 5 | `<src>多いですね。</src>` | `<src>タガがね</src>` | 1577 |
| 6 | `<src>開業したい方って</src>` | `<src>多いですね。海遊したい方って</src>` | 1997 |
| 7 | `<src>すごい</src>` | `<src>すぐに行こう</src>` | 1631 |
| 8 | `<src>自己意識高いし、</src>` | `<src>して다가 </src>` | 1061 |
| 9 | `<src>自分で</src>` | `<src>シージュレジムと</src>` | 2484 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>トンチンと音を</src>` | 918 |
| 11 | `<src>傾向が強いので、</src>` | `<src>と打つ方が強いので。</src>` | 2252 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 1433 |

---

### Test Example 26 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1864 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1764 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>毫无波澜，</src>` | 896 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1221 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不懈的</src>` | 1371 |
| 6 | `<src>期间</src>` | `<src>开到七千</src>` | 758 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十二生</src>` | 1326 |
| 8 | `<src>来诊断，</src>` | `<src>来设定，</src>` | 1782 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 1295 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 2883 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 770 |
| 12 | `<src>他们</src>` | `<src>当然都很</src>` | 1903 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>有好的离开。</src>` | 1388 |

---

### Test Example 27 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2005 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 1578 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 907 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是以前造成的</src>` | 1301 |
| 5 | `<src>所以呢，</src>` | `<src>的，所以呢，</src>` | 977 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 635 |
| 7 | `<src>所面临的一些</src>` | `<src>所念你的一些</src>` | 1754 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>网页啊</src>` | 1717 |
| 9 | `<src>也不可能是</src>` | `<src>跟粉丝</src>` | 424 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 1714 |
| 11 | `<src><\|wait\|></src>` | `<src>一起之间就</src>` | 2318 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来</src>` | 1085 |
| 13 | `<src>因此会建议</src>` | `<src>的，因此会建议</src>` | 1816 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>我的朋友呢，</src>` | 1478 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2104 |
| 2 | `<src>The meaning of </src>` | `<src><\|wait\|></src>` | 1849 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the nineteenth amendment </src>` | 845 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore </src>` | 1216 |
| 5 | `<src>history as a guide </src>` | `<src>its history as a guide </src>` | 1679 |
| 6 | `<src>to how political </src>` | `<src>to help </src>` | 1595 |
| 7 | `<src><\|wait\|></src>` | `<src>political change </src>` | 1596 |
| 8 | `<src>change can happen </src>` | `<src>can happen </src>` | 525 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2035 |
| 10 | `<src><\|wait\|></src>` | `<src>The meaning </src>` | 2039 |
| 11 | `<src>The meanings </src>` | `<src><\|wait\|></src>` | 1142 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, I'm </src>` | 2074 |
| 13 | `<src>myriad. </src>` | `<src>Mary Reed. </src>` | 1358 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or or if you have </src>` | 1925 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 1578 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 891 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1339 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1378 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1118 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 962 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. It's like, oh, </src>` | 2031 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2089 |
| 10 | `<src>spelled with a double </src>` | `<src>start with a double P? </src>` | 2055 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1750 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>Double L, I don't know. </src>` | 2052 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 1243 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1833 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>이런 것들은 </src>` | 1810 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 유전 실링과 </src>` | 1003 |
| 4 | `<src>이제 거진 </src>` | `<src>이거 거진 </src>` | 1138 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유산 한 적인 </src>` | 1607 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>그런 알 중도 굉장히 </src>` | 1731 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1763 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연히 미네랄 이다 </src>` | 1281 |
| 9 | `<src>이렇게 </src>` | `<src>이거 </src>` | 2402 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>굉장히 잘 들어와요. </src>` | 826 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이거 그런 거죠. 이제 </src>` | 2417 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1425 |
| 13 | `<src>아연. </src>` | `<src>아, </src>` | 1321 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>他到了一个</src>` | 1684 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>欠钱头，</src>` | 1855 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 724 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>得到了欠钱头之后，</src>` | 1380 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必</src>` | 1544 |
| 6 | `<src><\|wait\|></src>` | `<src>就要先</src>` | 1640 |
| 7 | `<src>先守住，</src>` | `<src>守住，</src>` | 1650 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着</src>` | 478 |
| 9 | `<src><\|wait\|></src>` | `<src>呃，那我在去操作</src>` | 1964 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦，</src>` | 2174 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1417 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么</src>` | 1636 |
| 13 | `<src><\|wait\|></src>` | `<src>那么会这么讲？因为呢，</src>` | 1508 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1187 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1706 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150개 가 </src>` | 1990 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>중호분에서 1000만으로 </src>` | 1065 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 977 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1388 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1781 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>자건 업자 들은 성장 하기 </src>` | 1937 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 해외 벡 </src>` | 1326 |
| 9 | `<src>걷게 되는데 </src>` | `<src>익을 겪게 되는데 </src>` | 2896 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>이거 는 </src>` | 1099 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>소기업 들은 성장 도 </src>` | 1896 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 </src>` | 1483 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들을 보이 게 된 거죠. </src>` | 1378 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src><\|wait\|></src>` | 1751 |
| 2 | `<src>我们可以看到的是</src>` | `<src>这章的部分，我们</src>` | 1901 |
| 3 | `<src>一个在钓鱼</src>` | `<src>看到的是个</src>` | 792 |
| 4 | `<src>的人，但是</src>` | `<src>戴雪人，但是</src>` | 1305 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>他是属于逆向的。</src>` | 1509 |
| 6 | `<src>所以</src>` | `<src>这通场</src>` | 1763 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>好像嘛，</src>` | 1798 |
| 8 | `<src>时候，就要去</src>` | `<src>这样一个状况</src>` | 1298 |
| 9 | `<src>特别注意，</src>` | `<src>需要去特别注意</src>` | 2777 |
| 10 | `<src>是它能不能够</src>` | `<src>是，他能不能</src>` | 421 |
| 11 | `<src>钓到鱼，</src>` | `<src>得到</src>` | 1823 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他掉不到</src>` | 1722 |
| 13 | `<src><\|wait\|></src>` | `<src>与你的意识</src>` | 1112 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1161 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1740 |
| 2 | `<src>HTML이라고 </src>` | `<src>HJM </src>` | 1604 |
| 3 | `<src><\|wait\|></src>` | `<src>이라고 하는 </src>` | 844 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피터도 </src>` | 1248 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 332 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1381 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 1755 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1906 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 929 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 의 역할. 우리가 이제 </src>` | 2491 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 </src>` | 960 |
| 12 | `<src>되는데 </src>` | `<src>작성 해야 되는데 </src>` | 1582 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1565 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 필요 합니다. </src>` | 1633 |
| 15 | `<src>필요 합니다. </src>` | `<src><\|wait\|></src>` | 1288 |

---

### Test Example 35 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1898 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个财运可以说是</src>` | 1859 |
| 3 | `<src>很不错的，但是</src>` | `<src>很难的，但是</src>` | 872 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正财的部分</src>` | 1255 |
| 5 | `<src>也就是</src>` | `<src>也是</src>` | 1326 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 1539 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩增长所带来的</src>` | 1251 |
| 8 | `<src>与收入的</src>` | `<src>红利，</src>` | 1132 |
| 9 | `<src>提升。如果是在</src>` | `<src>收入的提升，</src>` | 1527 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果</src>` | 2459 |
| 11 | `<src>这个月</src>` | `<src>在投资理财方面这个月</src>` | 359 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 2388 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对来说就</src>` | 1334 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点</src>` | 1316 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 895 |

---

### Test Example 36 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2134 |
| 2 | `<src><\|wait\|></src>` | `<src>세모라 </src>` | 1621 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 897 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>이게 </src>` | 1282 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>소름이 돋은 차리 돋은 </src>` | 665 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 온이야. </src>` | 1153 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 </src>` | 1591 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>흔들어서 같이 놀자는 거야. </src>` | 1921 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 </src>` | 1069 |
| 10 | `<src>물릴 거고 </src>` | `<src>오면 올릴 거고 </src>` | 2483 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 894 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1993 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주라고 하니까 </src>` | 1769 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 마음 에 </src>` | 1415 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 815 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>ジュウ</src>` | 1917 |
| 2 | `<src>十一二手とか</src>` | `<src>一二手とか</src>` | 1652 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>ですか？</src>` | 846 |
| 4 | `<src>十秒で。</src>` | `<src>おそらく</src>` | 842 |
| 5 | `<src>まあ</src>` | `<src>10秒でまあ</src>` | 725 |
| 6 | `<src>一秒に</src>` | `<src>1秒に</src>` | 1384 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>1秒ぐらいの</src>` | 1678 |
| 8 | `<src>計算ですか</src>` | `<src>せつなんですかね。</src>` | 1711 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 533 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1750 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2253 |
| 12 | `<src><\|wait\|></src>` | `<src>11</src>` | 899 |
| 13 | `<src>十一二手で</src>` | `<src>二手で</src>` | 1830 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1274 |
| 15 | `<src>宮馬とかが</src>` | `<src>見合うまとかが</src>` | 1427 |
| 16 | `<src>あるから。</src>` | `<src>だから</src>` | 1109 |

---

### Test Example 38 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2025 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>濡らせてやれ、</src>` | 2011 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 645 |
| 4 | `<src><\|wait\|></src>` | `<src>は</src>` | 1215 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>引き締めを見ている。</src>` | 1055 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 592 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1650 |
| 8 | `<src><\|wait\|></src>` | `<src>超に</src>` | 1532 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>超えてる不滅の奇跡。</src>` | 835 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2082 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1820 |
| 12 | `<src>船大工をやってる</src>` | `<src>船出を</src>` | 1313 |
| 13 | `<src>が、</src>` | `<src>やってる。</src>` | 1623 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなに</src>` | 1411 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>すごい解鎖線を</src>` | 1201 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 1207 |

---

### Test Example 39 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1850 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1758 |
| 3 | `<src><\|wait\|></src>` | `<src>there was </src>` | 851 |
| 4 | `<src>such interfaces before, </src>` | `<src>such instances before </src>` | 1295 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1394 |
| 6 | `<src>netfilter, TC. </src>` | `<src>that future TC </src>` | 1470 |
| 7 | `<src>Yeah, so </src>` | `<src>is there. </src>` | 804 |
| 8 | `<src>this is just </src>` | `<src>So this is just </src>` | 1738 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1867 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2267 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1360 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1686 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1304 |
| 14 | `<src>working on BugRepo </src>` | `<src>at Google should be </src>` | 1200 |
| 15 | `<src>should be aware of that. </src>` | `<src>aware of that. </src>` | 1257 |

---

### Test Example 40 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who </src>` | 2024 |
| 2 | `<src>just getting going </src>` | `<src>is just getting going </src>` | 1912 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 783 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1226 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I got ten of them </src>` | 1440 |
| 6 | `<src>that I think are </src>` | `<src>that are really </src>` | 1531 |
| 7 | `<src>really important. </src>` | `<src>important. </src>` | 752 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1648 |
| 9 | `<src>I'm going to go into. </src>` | `<src>Um, I'm going to go and do </src>` | 1952 |
| 10 | `<src>I have about </src>` | `<src>I have about </src>` | 2173 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 1262 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video. </src>` | 1835 |
| 13 | `<src><\|wait\|></src>` | `<src>They cover each one, </src>` | 1453 |
| 14 | `<src>that cover each one </src>` | `<src>and a little more </src>` | 1089 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>detail, </src>` | 1266 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1751 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알 거니 뭐? </src>` | 1911 |
| 3 | `<src>이방인으로 </src>` | `<src>여기 가 이방인 으로 </src>` | 944 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1150 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하는 </src>` | 1487 |
| 6 | `<src>우상에게로 </src>` | `<src>우상 에게로 </src>` | 1692 |
| 7 | `<src>끄는 그대로 </src>` | `<src>가든지 </src>` | 1732 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 </src>` | 416 |
| 9 | `<src><\|wait\|></src>` | `<src>걸려 갔느니라. </src>` | 1834 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그럼 으로 내가 </src>` | 2270 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1431 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1752 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님의 영으로 </src>` | 1543 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1245 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1132 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2052 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어, 어찌 보면 </src>` | 1776 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1026 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1144 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 1424 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 다고 </src>` | 1538 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 1586 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 787 |
| 9 | `<src><\|wait\|></src>` | `<src>어, </src>` | 1214 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생감모다는 </src>` | 2845 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 852 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 1874 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1316 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 거 </src>` | 1260 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고 </src>` | 918 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 </src>` | 1224 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1996 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. How far </src>` | 1997 |
| 3 | `<src>How far did you </src>` | `<src>did you actually </src>` | 710 |
| 4 | `<src><\|wait\|></src>` | `<src>go in your </src>` | 1228 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>education? Did you </src>` | 1431 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1726 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 1928 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. </src>` | 506 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 2215 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And so, did you graduate </src>` | 1849 |
| 11 | `<src>That's another level of </src>` | `<src>that? </src>` | 1989 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 1755 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for now. </src>` | 1429 |
| 14 | `<src>now. I'll see you </src>` | `<src>I'll see you </src>` | 1026 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1016 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね</src>` | 1998 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1889 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうのが</src>` | 732 |
| 4 | `<src><\|wait\|></src>` | `<src>出られて、ビジュアル</src>` | 1366 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>Python開発環境なんですね。</src>` | 1507 |
| 6 | `<src>というのもフローリフを</src>` | `<src>こういうのも</src>` | 1583 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフをビジュアルに</src>` | 1908 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>書いてあとはそれは</src>` | 641 |
| 9 | `<src>にそこから</src>` | `<src>Pythonコードが</src>` | 2014 |
| 10 | `<src>生成されて、それが</src>` | `<src>そっから生成されるって</src>` | 1857 |
| 11 | `<src>実行されることで</src>` | `<src>それが実行されることで信号処理</src>` | 1985 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 1612 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことをしている</src>` | 1034 |
| 14 | `<src><\|wait\|></src>` | `<src>から</src>` | 1072 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 1194 |
| 16 | `<src>じゃあ。</src>` | `<src>はいじゃあ</src>` | 464 |

---

### Test Example 45 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 </src>` | 1994 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1777 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들도 있습니다. 저희 가 </src>` | 1073 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1203 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람이 </src>` | 1344 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨택 을 한 텐트 에요. </src>` | 2094 |
| 7 | `<src><\|wait\|></src>` | `<src>B가 컨설턴트 에 </src>` | 1807 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>오고 A라는 </src>` | 1231 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 2671 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 430 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>들었을 때 </src>` | 2120 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람이 </src>` | 1576 |
| 13 | `<src>실제 </src>` | `<src>실제 크로 사이트 스크 </src>` | 1335 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>스위트에서 </src>` | 935 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>XPI까지 </src>` | 1196 |
| 16 | `<src>감염 이 될까. </src>` | `<src>가능 이 될까 </src>` | 264 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>드러가면 </src>` | 2154 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 해명 이다. </src>` | 2060 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 610 |
| 4 | `<src><\|wait\|></src>` | `<src>하고 온 거로 </src>` | 1273 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 다니 고 </src>` | 1451 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>가는 거네. 뭐 </src>` | 1777 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1803 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 626 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가면 또 장렬 이요. </src>` | 2723 |
| 10 | `<src>또 장렬이에요. </src>` | `<src><\|wait\|></src>` | 1168 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 챙기 냐고 </src>` | 2038 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1710 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1134 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>노가요. </src>` | 1126 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다행인 것 같아요. </src>` | 1257 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 764 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1986 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或干支</src>` | 1911 |
| 3 | `<src>的感情或</src>` | `<src>对属的感情</src>` | 868 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的。</src>` | 1226 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1342 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1420 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 872 |
| 8 | `<src>会听到人们</src>` | `<src>好经常会听到人们这样说：</src>` | 1735 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1440 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2547 |
| 11 | `<src>这个人</src>` | `<src>这个人又在</src>` | 1083 |
| 12 | `<src>又在说谎了，</src>` | `<src>躲黄了。</src>` | 1715 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1283 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1449 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1141 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说</src>` | 796 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 743 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1689 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1830 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놓았습니다. </src>` | 997 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 1033 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>이 로쿠자 의 분석 을 보시면 </src>` | 1469 |
| 6 | `<src>소니가 </src>` | `<src>소니 가 </src>` | 1541 |
| 7 | `<src>26비트 FP </src>` | `<src>이오렉트 에 </src>` | 1263 |
| 8 | `<src>파이프 를 </src>` | `<src>FPP 파이프 를 </src>` | 1199 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128 비트 로 </src>` | 2142 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나충가서 로포인 다. </src>` | 2066 |
| 11 | `<src><\|wait\|></src>` | `<src>엑스박스 시리즈 </src>` | 1979 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>엑스에서도 없는 </src>` | 1618 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1076 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시, </src>` | 1305 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>S2가 여기 도 없다. </src>` | 1308 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 758 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1916 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1610 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining </src>` | 911 |
| 4 | `<src>the standard is because you're </src>` | `<src>what we think the standard is, </src>` | 1421 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct </src>` | 1651 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1706 |
| 7 | `<src>is is that </src>` | `<src>is that </src>` | 1766 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid </src>` | 1124 |
| 9 | `<src>block and because the </src>` | `<src>at the block, </src>` | 2162 |
| 10 | `<src>standards have </src>` | `<src>and because the standards have changed. </src>` | 1239 |
| 11 | `<src>changed from 20 </src>` | `<src><\|wait\|></src>` | 2244 |
| 12 | `<src>years ago, </src>` | `<src>From twenty years ago, </src>` | 1482 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1454 |
| 14 | `<src>a higher standard because </src>` | `<src>our standard </src>` | 1000 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1073 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to </src>` | 790 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 1860 |
| 2 | `<src><\|wait\|></src>` | `<src>인상 하는 </src>` | 1584 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 968 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 1418 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1425 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>어 큰 폭의 상승 을 </src>` | 1860 |
| 7 | `<src>먼저 </src>` | `<src>하겠지만 먼저 </src>` | 1785 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 1047 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2658 |
| 10 | `<src>먼저 </src>` | `<src>이 먼저 시장 을 </src>` | 815 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직이기 때문 에 </src>` | 2513 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>항상 </src>` | 1326 |
| 13 | `<src>요 시총이 </src>` | `<src>유동 시 총이 가벼운 종목 </src>` | 1542 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>을 </src>` | 1173 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈으로 봐야 될 것 같습니다. </src>` | 775 |
| 16 | `<src>같습니다. </src>` | `<src><\|wait\|></src>` | 729 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1936 |
| 2 | `<src>Also, </src>` | `<src>Also, you will not </src>` | 1756 |
| 3 | `<src>you will not be able to </src>` | `<src>be able to move </src>` | 949 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 1178 |
| 5 | `<src><\|wait\|></src>` | `<src>between the </src>` | 1376 |
| 6 | `<src>between the resources. </src>` | `<src>resources </src>` | 851 |
| 7 | `<src>So, if </src>` | `<src>so if </src>` | 1111 |
| 8 | `<src>you get into </src>` | `<src>you get into the </src>` | 1859 |
| 9 | `<src>a situation </src>` | `<src>situation where you </src>` | 844 |
| 10 | `<src>where you realize </src>` | `<src>realize you've added </src>` | 2338 |
| 11 | `<src>you've added the wrong media </src>` | `<src>the wrong media </src>` | 1272 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular </src>` | 1811 |
| 13 | `<src>you need to let us know, </src>` | `<src>resource, we'll need to let us know. </src>` | 1987 |
| 14 | `<src>and we can see about </src>` | `<src>And we can see about </src>` | 1428 |
| 15 | `<src><\|wait\|></src>` | `<src>giving those media files </src>` | 900 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>and then making sure </src>` | 1159 |
| 17 | `<src>get backed up </src>` | `<src>we get that up </src>` | 767 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 518 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>For all </src>` | 1678 |
| 2 | `<src>首次觉知到</src>` | `<src>the source </src>` | 1787 |
| 3 | `<src>那个现象：</src>` | `<src>that leads to that phenomenon, </src>` | 942 |
| 4 | `<src>每当我们</src>` | `<src>but </src>` | 1161 |
| 5 | `<src><\|wait\|></src>` | `<src>we are </src>` | 1422 |
| 6 | `<src>处于爱之中，</src>` | `<src>in the heart </src>` | 1491 |
| 7 | `<src>所谓的爱，</src>` | `<src>of love, </src>` | 877 |
| 8 | `<src>我们也</src>` | `<src>and we also </src>` | 1656 |
| 9 | `<src>同时进入恨。</src>` | `<src>enter the </src>` | 2191 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1938 |
| 11 | `<src>在早上的时候，</src>` | `<src>time of the </src>` | 1346 |
| 12 | `<src>它是爱；</src>` | `<src>world of love. </src>` | 1732 |
| 13 | `<src>到了晚上，</src>` | `<src>It comes to the end. </src>` | 1492 |
| 14 | `<src>它就变成恨。</src>` | `<src>It becomes </src>` | 1151 |
| 15 | `<src><\|wait\|></src>` | `<src>that </src>` | 1083 |
| 16 | `<src>那个钟摆</src>` | `<src>the whole world. </src>` | 639 |
| 17 | `<src><\|wait\|></src>` | `<src>It continues </src>` | 770 |
| 18 | `<src>继续在移动。</src>` | `<src>to do. </src>` | 549 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1739 |
| 2 | `<src>he knows Jesus </src>` | `<src>He knows Jesus </src>` | 1703 |
| 3 | `<src>is hungry. </src>` | `<src>is a hungry </src>` | 837 |
| 4 | `<src>He knows that </src>` | `<src>and knows that </src>` | 1284 |
| 5 | `<src>he's been without food, </src>` | `<src>he's supposed to be </src>` | 1397 |
| 6 | `<src><\|wait\|></src>` | `<src>in the wilderness </src>` | 1462 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>for forty days that he's hungry, </src>` | 1410 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 1196 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1302 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it </src>` | 2851 |
| 11 | `<src><\|wait\|></src>` | `<src>turn these </src>` | 1645 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread. </src>` | 1726 |
| 13 | `<src><\|wait\|></src>` | `<src>How did he </src>` | 1297 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>just deal with that </src>` | 1234 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 1133 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 358 |
| 17 | `<src>Man shall not live </src>` | `<src>Man, </src>` | 740 |
| 18 | `<src>by bread alone. </src>` | `<src>Jonathan led by the stone. </src>` | 578 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2207 |
| 2 | `<src>in turmoil </src>` | `<src>in the rearview mirror </src>` | 1692 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 800 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1312 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR field </src>` | 1067 |
| 6 | `<src><\|wait\|></src>` | `<src>being of critical </src>` | 577 |
| 7 | `<src>being of critical importance </src>` | `<src>importance </src>` | 1448 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 1209 |
| 9 | `<src><\|wait\|></src>` | `<src>variant database </src>` | 1125 |
| 10 | `<src>databases, </src>` | `<src>systems, which is obviously </src>` | 1490 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>one of my loves. </src>` | 2641 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 1242 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree upon </src>` | 1861 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that </src>` | 1455 |
| 15 | `<src>to be in these </src>` | `<src>need to be in these </src>` | 1101 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 1341 |
| 17 | `<src>draw from, </src>` | `<src>draw from, there's nothing </src>` | 531 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>to draw from, right? </src>` | 751 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 521 |

---

### Test Example 55 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1785 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src><\|wait\|></src>` | 1750 |
| 3 | `<src>촉발 시키고 </src>` | `<src>어퍼 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 젭팔 ` | 12736 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1760 |
| 5 | `<src>자신 의 </src>` | `<src>자신의 </src>` | 1232 |
| 6 | `<src><\|wait\|></src>` | `<src>모로 죠깅 </src>` | 1426 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>해르나 </src>` | 1093 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 853 |
| 9 | `<src>박한상과 </src>` | `<src>박한성 과 </src>` | 757 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들이 </src>` | 564 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>있습니다. </src>` | 363 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我們看一下</src>` | 1872 |
| 2 | `<src>它的图片哦，</src>` | `<src>一下</src>` | 1474 |
| 3 | `<src><\|wait\|></src>` | `<src>它的圖片哦，</src>` | 1026 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>圖片的部分呢，</src>` | 1243 |
| 5 | `<src>的一个是客厅</src>` | `<src>我們可以看到</src>` | 332 |
| 6 | `<src>的部分。</src>` | `<src>一個是克汀的部分，</src>` | 1565 |
| 7 | `<src>那客厅一般</src>` | `<src>克汀一般</src>` | 1674 |
| 8 | `<src>都是属于</src>` | `<src>都是屬於</src>` | 1764 |
| 9 | `<src>我们</src>` | `<src>我們在</src>` | 604 |
| 10 | `<src>在休息的地方，</src>` | `<src>修習的地方</src>` | 2068 |
| 11 | `<src><\|wait\|></src>` | `<src>，所以呢，</src>` | 1739 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>這是身體的部分</src>` | 1684 |
| 13 | `<src>也会反映的是</src>` | `<src>會反應的是</src>` | 1716 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要</src>` | 1158 |
| 15 | `<src>一点时间，</src>` | `<src>給自己一點時間</src>` | 1280 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 1113 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>做下來修習，</src>` | 483 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可以看到這邊是</src>` | 762 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>消防員的嘛。</src>` | 553 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 328 |
| 21 | `<src>所以是说。</src>` | `<src>所以也是說。</src>` | 350 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2172 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful </src>` | 1488 |
| 3 | `<src>right, </src>` | `<src>individual write, </src>` | 966 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1199 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 370 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I I don't know </src>` | 1576 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1808 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1690 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the vanguard of </src>` | 1365 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2828 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 921 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1932 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 1295 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 1408 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1119 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged </src>` | 853 |
| 17 | `<src><\|wait\|></src>` | `<src>so </src>` | 748 |
| 18 | `<src>So you have some </src>` | `<src>you have </src>` | 547 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 356 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 176 |
| 21 | `<src>who. </src>` | `<src>who </src>` | 260 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1738 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare. </src>` | 1740 |
| 3 | `<src>and they often </src>` | `<src>And they often </src>` | 801 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 1290 |
| 5 | `<src><\|wait\|></src>` | `<src>to completely </src>` | 390 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>revolutionize the world. </src>` | 1376 |
| 7 | `<src><\|wait\|></src>` | `<src>The </src>` | 1566 |
| 8 | `<src>Their personality is </src>` | `<src>personality is </src>` | 1647 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 580 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1257 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 2696 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, they also </src>` | 1177 |
| 13 | `<src>they also hate </src>` | `<src>hate </src>` | 1714 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations. </src>` | 1482 |
| 15 | `<src>and like to </src>` | `<src>And like to </src>` | 1175 |
| 16 | `<src><\|wait\|></src>` | `<src>get straight to the </src>` | 1186 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 774 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 789 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate </src>` | 598 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and they </src>` | 318 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy away </src>` | 376 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 281 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 272 |
| 24 | `<src><\|wait\|></src>` | `<src>E and CP </src>` | 254 |
| 25 | `<src>ENTP stands for </src>` | `<src>stand for. </src>` | 258 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 의 이준석은 </src>` | 1837 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>정무를 거부 한 </src>` | 2043 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 713 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1204 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 1503 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1770 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1853 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1337 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2868 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 926 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1949 |
| 12 | `<src>이준석은 </src>` | `<src>이준석 은 들은해놓고 </src>` | 1504 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 가 </src>` | 1181 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>떨어뜨리 겠다는 </src>` | 1325 |
| 15 | `<src><\|wait\|></src>` | `<src>독끼를 품은 </src>` | 651 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 758 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 533 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 356 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 409 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 292 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석 성상 납권 </src>` | 294 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 261 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당이 </src>` | 223 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 에 얼마나 </src>` | 267 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재 입니까? </src>` | 276 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1971 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 1499 |
| 3 | `<src>今作ってる</src>` | `<src>作ってみたいです。</src>` | 1064 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>なので</src>` | 1291 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ここのね</src>` | 404 |
| 6 | `<src>も</src>` | `<src>ゴルフスローンホテル</src>` | 1299 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>で朝食が食べれる場所</src>` | 1908 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1664 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1034 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2017 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルフスローンホテル</src>` | 1444 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 2309 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なという方はですね</src>` | 1423 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさって</src>` | 1213 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>見てみてまあいいんじゃない</src>` | 1023 |
| 16 | `<src><\|wait\|></src>` | `<src>なと</src>` | 1219 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。</src>` | 632 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ここホテルからですね</src>` | 275 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 519 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 401 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかる</src>` | 350 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんな</src>` | 273 |
| 23 | `<src>レベルのね</src>` | `<src>かそんなレベルでのね</src>` | 284 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 345 |
| 25 | `<src>ホテルになってますので</src>` | `<src>なってますので</src>` | 182 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 235 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさって</src>` | 274 |
| 28 | `<src>ください</src>` | `<src>みてください。それなら</src>` | 157 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は</src>` | 141 |
