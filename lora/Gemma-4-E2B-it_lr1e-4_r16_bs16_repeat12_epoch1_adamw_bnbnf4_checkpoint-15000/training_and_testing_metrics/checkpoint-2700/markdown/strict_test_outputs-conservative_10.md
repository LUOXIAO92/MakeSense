# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9666
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3775
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9683
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 0.9950
  - TGT_WAIT_TOTAL: 806
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1333.9330
  - PROCESS_TIME_MS_P50: 1291.9150
  - PROCESS_TIME_MS_P95: 2364.3580
  - PROCESS_TIME_MS_MAX: 3290.3620

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我的</src><tgt><\|wait\|></tgt>` | 1151 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>送纸的地方，</src><tgt><\|wait\|></tgt>` | 949 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个友邻也很大，</src><tgt><\|wait\|></tgt>` | 974 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 664 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在放个</src><tgt><\|wait\|></tgt>` | 1329 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>热汤儿，</src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1666 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>在礼器儿，</src><tgt><\|wait\|></tgt>` | 1595 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 836 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>这种热汤儿。</src><tgt>My place for sending out paper is quite large, and I'm putting out some hot soup— in a pot— that kind of hot soup.</tgt>` | 3121 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要切肤，</src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的。</src><tgt><\|wait\|></tgt>` | 1011 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1472 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有</src><tgt><\|wait\|></tgt>` | 881 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导到</src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1711 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如初于终间，</src><tgt><\|wait\|></tgt>` | 890 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1153 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1682 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为</src><tgt><\|wait\|></tgt>` | 1699 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>一个师傅，</src><tgt>肌を削るのは簡単です。しかし、師匠が最初から最後まで指導してくれなければ、それはできません。だから、反省が必要です。師匠になるには、</tgt>` | 2350 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1081 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是，</src><tgt><\|wait\|></tgt>` | 1060 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1348 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们生生的爱</src><tgt><\|wait\|></tgt>` | 1043 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>浇水，</src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1558 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 539 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>给</src><tgt><\|wait\|></tgt>` | 1680 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>孩子心灵营养，</src><tgt><\|wait\|></tgt>` | 1790 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>给内心</src><tgt><\|wait\|></tgt>` | 1960 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>慢慢长大。</src><tgt>What parents need to do is use our love to water the seeds. So nourish your child's soul and help their heart grow slowly.</tgt>` | 2117 |

---

### Test Example 4 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1027 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt><\|wait\|></tgt>` | 1409 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1346 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 626 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1494 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1714 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>また</src><tgt><\|wait\|></tgt>` | 946 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>内訳があります</src><tgt>We also have T- shirts and other items available, so please feel free to join us. That's all for the contact information.</tgt>` | 2696 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>ので、少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1027 |

---

### Test Example 5 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1057 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1295 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1012 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>方法、</src><tgt><\|wait\|></tgt>` | 1423 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 740 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1301 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1721 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1769 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>など</src><tgt><\|wait\|></tgt>` | 1659 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src>という人の絵は</src><tgt>这些画大概是从这之后开始的，比如高更、塞尚、伦纳等人的画，</tgt>` | 1907 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1007 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1203 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>객생들은 </src><tgt><\|wait\|></tgt>` | 1020 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1312 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1085 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1429 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1665 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>객생들이 </src><tgt><\|wait\|></tgt>` | 487 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>있었기 때문 입니다. </src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1707 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1978 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교사 들은 </src><tgt>The students in the auspicious seats were not actually highly intelligent. They were randomly selected. The teachers who didn't know the truth</tgt>` | 2690 |

---

### Test Example 7 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 878 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1083 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>어떨 섞발 섞이고 </src><tgt><\|wait\|></tgt>` | 1914 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 657 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1343 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt><\|wait\|></tgt>` | 1778 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1664 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1574 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 906 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들은 </src><tgt><\|wait\|></tgt>` | 1767 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>이다. </src><tgt>I am a mix of what I am. I am the same generation as the people who killed my parents— Hernan Park Hansang.</tgt>` | 2548 |

---

### Test Example 8 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1150 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1037 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1014 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 721 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1513 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1674 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1750 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. </src><tgt><\|wait\|></tgt>` | 1480 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src><\|wait\|></src><tgt>好的。然后，在这些例子之后，指令告诉我们，实际上要使用这些值。</tgt>` | 1460 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>So this game.board </src><tgt><\|wait\|></tgt>` | 1244 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>array. </src><tgt><\|wait\|></tgt>` | 834 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1013 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 1007 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1292 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1081 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설프고 용심이가 </src><tgt><\|wait\|></tgt>` | 1596 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1680 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞이 는 건데요. </src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 657 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1708 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해행으로 </src><tgt><\|wait\|></tgt>` | 1988 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>조금 주기 맞는 </src><tgt>So, I'm a sword- minded person, and my sword- mindedness is a bit mixed up. Hey, this really fits the sword- minded type.</tgt>` | 2797 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘沙完以后</src><tgt><\|wait\|></tgt>` | 1109 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 981 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>那内部的压力</src><tgt><\|wait\|></tgt>` | 1653 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 939 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>衰弱了。然后</src><tgt><\|wait\|></tgt>` | 1433 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在</src><tgt><\|wait\|></tgt>` | 1632 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1693 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 1559 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态。</src><tgt><\|wait\|></tgt>` | 786 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1784 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>低于状态。</src><tgt>淘沙が終わると、内部の圧力エネルギーも弱まります。そして、比較的低エネルギーな運行状態に留まります。これがいわゆる「低エネルギー状態」です。</tgt>` | 2792 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned and to repeat </src><tgt><\|wait\|></tgt>` | 1393 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out what you're good at. </src><tgt><\|wait\|></tgt>` | 1504 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>And do more of </src><tgt><\|wait\|></tgt>` | 1071 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it, and what you're not </src><tgt><\|wait\|></tgt>` | 1060 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at, </src><tgt><\|wait\|></tgt>` | 1692 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>get to people around you to help you with </src><tgt><\|wait\|></tgt>` | 1975 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1910 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>it. And in telling next time, </src><tgt>最后，重复。学习并重复，找出你擅长什么。多做那些，对于你不太擅长的，找身边的人帮忙。下次告诉他们，</tgt>` | 2830 |

---

### Test Example 12 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>また</src><tgt><\|wait\|></tgt>` | 1135 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>またちょっと距離が</src><tgt><\|wait\|></tgt>` | 940 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じで</src><tgt><\|wait\|></tgt>` | 801 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大社から</src><tgt><\|wait\|></tgt>` | 1044 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>タタカレ場へ遠いですね。</src><tgt><\|wait\|></tgt>` | 1599 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海遊したい方って</src><tgt><\|wait\|></tgt>` | 891 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行き来していただが、</src><tgt><\|wait\|></tgt>` | 1659 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>C</src><tgt><\|wait\|></tgt>` | 1651 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>で見て</src><tgt><\|wait\|></tgt>` | 1714 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>ととこ見ておととしゃぐ</src><tgt><\|wait\|></tgt>` | 1755 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>ここは強いので</src><tgt>又会有点远，从大社到塔塔卡雷场会很远呢。想去海游的话，可以很快来来往来，C那边看，看个地方坐着，那里很棒，</tgt>` | 2896 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 522 |

---

### Test Example 13 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 880 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 923 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body </src><tgt><\|wait\|></tgt>` | 1678 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>where does </src><tgt><\|wait\|></tgt>` | 861 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1306 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1755 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1599 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tension in your chest? </src><tgt><\|wait\|></tgt>` | 1331 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is the </src><tgt><\|wait\|></tgt>` | 920 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>whole limb </src><tgt><\|wait\|></tgt>` | 1978 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>that you're using? </src><tgt>你的身体在做什么？进入你的身体，紧张感从哪里开始？是什么？是头吗？胸部有紧张吗？还是你正在使用的整个肢体？</tgt>` | 2939 |

---

### Test Example 14 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 915 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 1000 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天国という</src><tgt><\|wait\|></tgt>` | 1292 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>施設被害が</src><tgt><\|wait\|></tgt>` | 1079 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1416 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 717 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1337 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井清義の仕組み</src><tgt><\|wait\|></tgt>` | 1840 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1673 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>五項、</src><tgt><\|wait\|></tgt>` | 1855 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src><\|wait\|></src><tgt>그렇습니다. 거기서 천국이라는 시설 피해가 있었습니다. 그래서 나가이 요시노의 체계는 다섯 가지로</tgt>` | 2000 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>施設被害、</src><tgt><\|wait\|></tgt>` | 912 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビデス。</src><tgt><\|wait\|></tgt>` | 435 |

---

### Test Example 15 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 887 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1052 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1564 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | 1006 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>This is Tip of the Stem. </src><tgt><\|wait\|></tgt>` | 1550 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research. Looking at </src><tgt><\|wait\|></tgt>` | 1616 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 1743 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1754 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | 1735 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there, </src><tgt><\|wait\|></tgt>` | 695 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>people that we can learn from. </src><tgt>非常に幸せな人たちに関する重要な研究を行いました。これが「Tip of the Stem」です。研究では、最も幸せな人々の10%を分析しました。彼らから学ぶべき点があります。</tgt>` | 2857 |

---

### Test Example 16 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 979 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1093 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | 1793 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1131 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 가 </src><tgt><\|wait\|></tgt>` | 1139 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 1689 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 보이 고 </src><tgt><\|wait\|></tgt>` | 1727 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1715 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보일 피라고 보이 서 우주 가 </src><tgt><\|wait\|></tgt>` | 1925 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>이제 나한테 보살 이란 </src><tgt><\|wait\|></tgt>` | 795 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src><\|wait\|></src><tgt>これ、すごく低レベルなことかもしれないけど、本当に菩薩だよ。いや、自分の菩薩なのに夢かと思って。私だけ菩薩に見えるようにして、宇宙が私に菩薩だと思わせようとしているんだ。</tgt>` | 2610 |

---

### Test Example 17 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 975 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1407 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 991 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1429 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑了这个状况，</src><tgt><\|wait\|></tgt>` | 1607 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 546 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1786 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>你無理承担。</src><tgt><\|wait\|></tgt>` | 1700 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | 2012 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>事业就是属象。</src><tgt>When facing such a situation, we should quickly report it to our supervisor or let the other party know. Don't think you have to handle everything yourself. Overall, your career is a ' Shu Xiang '— a ' Shu Xiang ' career.</tgt>` | 3156 |

---

### Test Example 18 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 842 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 461 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>ユルむと、</src><tgt><\|wait\|></tgt>` | 1549 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1240 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1056 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1699 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>ヤクネジの</src><tgt><\|wait\|></tgt>` | 1745 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1745 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1494 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 꺼지게 되니까, 기어 끝에 잭 나사 너트가 붙어 있는 거네요.</tgt>` | 2532 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 991 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解完了。</src><tgt><\|wait\|></tgt>` | 681 |

---

### Test Example 19 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 753 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1056 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1653 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>1年生ですからね。</src><tgt><\|wait\|></tgt>` | 1063 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1216 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こうミミシカク</src><tgt><\|wait\|></tgt>` | 1835 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>線っていうのを</src><tgt><\|wait\|></tgt>` | 1814 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう体図して</src><tgt><\|wait\|></tgt>` | 1887 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>なげると</src><tgt><\|wait\|></tgt>` | 1978 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>1年生でも</src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>大丈夫だ。</src><tgt>从一开始，特别是孩子还在一年级的时候。在那时候，如果把“ミミシカク线”画出来，一年级孩子也能没问题。</tgt>` | 1699 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 754 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1929 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt><\|wait\|></tgt>` | 626 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>心理，</src><tgt><\|wait\|></tgt>` | 1314 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1709 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1309 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天黎明</src><tgt><\|wait\|></tgt>` | 751 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1975 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt>If there's some kind of psychological connection between high school girls and people who don't look like them, could it be starting from the dawn? Yang Zisi</tgt>` | 2831 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>与天篇？</src><tgt><\|wait\|></tgt>` | 891 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 687 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1057 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1292 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | 1077 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1451 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>好自在的</src><tgt><\|wait\|></tgt>` | 974 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>时候在工作</src><tgt><\|wait\|></tgt>` | 1035 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>和生活之间</src><tgt><\|wait\|></tgt>` | 1804 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>无缝的</src><tgt><\|wait\|></tgt>` | 1803 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>过渡区，</src><tgt><\|wait\|></tgt>` | 1992 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小欲望</src><tgt>제 삶의 궤도로 돌아가게 해 주세요. 편안하게 일과 삶 사이를 자연스럽게 오갈 수 있는 그런 공간이요. 작은 욕망이</tgt>` | 2877 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 1052 |

---

### Test Example 22 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Shinwa Tero. </src><tgt><\|wait\|></tgt>` | 1088 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1550 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a business </src><tgt><\|wait\|></tgt>` | 906 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>and finance </src><tgt><\|wait\|></tgt>` | 1302 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a brother of psychology. </src><tgt><\|wait\|></tgt>` | 1348 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 633 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at the Yanu </src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1703 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | 2140 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>corporate consultancy </src><tgt>제 이름은 신와 테로입니다. 현재 비즈니스 및 금융과 심리학을 공부하고 있습니다. 여기 야누에서 공부하고 있고, 앞으로는 기업 컨설팅 분야로</tgt>` | 2909 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1392 |

---

### Test Example 23 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 에 </src><tgt><\|wait\|></tgt>` | 1064 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 이거 주고 내가 </src><tgt><\|wait\|></tgt>` | 1677 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수도다. </src><tgt><\|wait\|></tgt>` | 1539 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 에 </src><tgt><\|wait\|></tgt>` | 886 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 1613 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해달 거냐? 내가 </src><tgt><\|wait\|></tgt>` | 1851 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1956 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주인 인데냐? </src><tgt><\|wait\|></tgt>` | 2035 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>어? </src><tgt><\|wait\|></tgt>` | 1642 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src>내가 </src><tgt>He might have come here to kill me, asking me to go to another party. Is he asking me to go to another party? I'm the one who's not even heard a word, aren't I? Huh? I'm</tgt>` | 2487 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 839 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAアンデス</src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>理論の場面で</src><tgt><\|wait\|></tgt>` | 1692 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>A生則かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1462 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | 999 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあAのRankを</src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べたことで、</src><tgt><\|wait\|></tgt>` | 1704 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>あのその生則かどうかっていうの</src><tgt><\|wait\|></tgt>` | 1968 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>を証明する生則</src><tgt><\|wait\|></tgt>` | 2037 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>であることが保証されていった</src><tgt><\|wait\|></tgt>` | 1714 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>ような使い方を</src><tgt>When you're looking into whether A is a transitivity in the theory of A- A- A, you can prove it by checking the rank of A. That's how you can use it.</tgt>` | 1947 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt><\|wait\|></tgt>` | 1295 |

---

### Test Example 25 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1058 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 973 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，</src><tgt><\|wait\|></tgt>` | 973 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是因为造成了</src><tgt><\|wait\|></tgt>` | 1368 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1296 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 674 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt><\|wait\|></tgt>` | 1751 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风险</src><tgt><\|wait\|></tgt>` | 1754 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 1736 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>事业就眼变出来。</src><tgt>皆さんにお伝えしたいのは、このローマでは、危機やリスクがあなたのキャリアに直結するわけではありません。だからといって、あなたのキャリアが危機に直面するわけではありません。</tgt>` | 2635 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 629 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此，</src><tgt><\|wait\|></tgt>` | 1121 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>会建议属鸡的朋友呢，</src><tgt><\|wait\|></tgt>` | 1188 |

---

### Test Example 26 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 863 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 1481 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>also store energy. And when those </src><tgt><\|wait\|></tgt>` | 1324 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1323 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1587 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 1776 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt><\|wait\|></tgt>` | 1914 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 2061 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or </src><tgt><\|wait\|></tgt>` | 1739 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>gets used to make </src><tgt>늘어난 고무줄처럼, 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 에너지로 변환됩니다. 아니면</tgt>` | 2364 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 989 |

---

### Test Example 27 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 926 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 998 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 1126 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>还服务</src><tgt><\|wait\|></tgt>` | 1199 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1302 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们。</src><tgt><\|wait\|></tgt>` | 714 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1467 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做维向</src><tgt><\|wait\|></tgt>` | 1846 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>高速几辆，</src><tgt><\|wait\|></tgt>` | 1822 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你可以发现</src><tgt><\|wait\|></tgt>` | 2020 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>给维向和平分的</src><tgt>2つ目は、二クラスに移行して、第一線で戦う大牛たちをサポートすることです。例えば、維向高速の数台を運転していると、維向と平分が</tgt>` | 3005 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>新绑</src><tgt><\|wait\|></tgt>` | 1531 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 706 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Well, or if you have </src><tgt><\|wait\|></tgt>` | 1122 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1585 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 991 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1343 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1825 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1689 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the word. </src><tgt><\|wait\|></tgt>` | 1716 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>Like, oh, is this word </src><tgt><\|wait\|></tgt>` | 1311 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>started with </src><tgt><\|wait\|></tgt>` | 1044 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>a double p, </src><tgt>ええと、あるいは何か書く必要がある場合、文章を書く場合、単語のスペルが全くわからないことに気づくかもしれません。「あ、この単語はダブルPで始まるんだ」</tgt>` | 2876 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double m? I don't know. </src><tgt><\|wait\|></tgt>` | 1746 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 560 |

---

### Test Example 29 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>我当时一切正常，</src><tgt><\|wait\|></tgt>` | 1079 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>毫无烦恼，</src><tgt><\|wait\|></tgt>` | 1611 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>可以</src><tgt><\|wait\|></tgt>` | 857 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持出版，</src><tgt><\|wait\|></tgt>` | 1339 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1628 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二星</src><tgt><\|wait\|></tgt>` | 484 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>以内选段，</src><tgt><\|wait\|></tgt>` | 1652 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿，</src><tgt><\|wait\|></tgt>` | 1774 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 2037 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>都没有问题。</src><tgt>Back then, everything was fine. No worries at all. I could have just kept publishing. The deadline was about 12 star- year cycles. No need to rush, no need to rush, no need to rush.</tgt>` | 2972 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们们都很</src><tgt><\|wait\|></tgt>` | 1491 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>依乎的离开。</src><tgt><\|wait\|></tgt>` | 811 |

---

### Test Example 30 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1170 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt><\|wait\|></tgt>` | 1091 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>Amendment </src><tgt><\|wait\|></tgt>` | 1456 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1016 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how </src><tgt><\|wait\|></tgt>` | 1669 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1289 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 736 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1802 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2010 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>The meanings of </src><tgt>19차 수정헌법의 의미와 역사를 탐구하고, 이것이 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 되는 방식을 살펴봅니다.</tgt>` | 2880 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>the amendments, of course, </src><tgt><\|wait\|></tgt>` | 1460 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Meredith. </src><tgt><\|wait\|></tgt>` | 954 |

---

### Test Example 31 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 981 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1057 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there are </src><tgt><\|wait\|></tgt>` | 1473 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such instances before </src><tgt><\|wait\|></tgt>` | 881 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1436 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>that future TC </src><tgt><\|wait\|></tgt>` | 1573 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>is </src><tgt><\|wait\|></tgt>` | 520 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>just </src><tgt><\|wait\|></tgt>` | 1610 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1750 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at, </src><tgt><\|wait\|></tgt>` | 2067 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事，以前就有过这种情况，所以未来TC只是另一个可以看的地方，</tgt>` | 1755 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but </src><tgt><\|wait\|></tgt>` | 750 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 602 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on Bug Repositories </src><tgt><\|wait\|></tgt>` | 1842 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 476 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分</src><tgt><\|wait\|></tgt>` | 842 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1609 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个戴旧的人，但是</src><tgt><\|wait\|></tgt>` | 1105 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1439 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1591 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>这通场嘛，这样的一个状况</src><tgt><\|wait\|></tgt>` | 1846 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>是需要去</src><tgt><\|wait\|></tgt>` | 1706 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别注意的是。</src><tgt><\|wait\|></tgt>` | 1962 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>它能不能</src><tgt><\|wait\|></tgt>` | 461 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt>이 부분은 낡은 옷을 입은 사람을 보여주는데, 이건 역방향이에요. 이 전체적인 상황은 특별히 주의해야 합니다. 그 사람이</tgt>` | 2601 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他掉不到</src><tgt><\|wait\|></tgt>` | 1276 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 989 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>与你的意识上。</src><tgt><\|wait\|></tgt>` | 1185 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>砸到</src><tgt><\|wait\|></tgt>` | 767 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>一个铁头，</src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1556 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>打到了铁头之后，</src><tgt><\|wait\|></tgt>` | 1221 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1267 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1625 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>抓前守，</src><tgt><\|wait\|></tgt>` | 1670 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要像说，哎，那我</src><tgt><\|wait\|></tgt>` | 1865 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>再继续操作</src><tgt><\|wait\|></tgt>` | 1707 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 738 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt>鉄頭に当たった場合、必ず前を守ってください。そうして「あ、じゃあ、また操作続けよう」なんて思わないでください。</tgt>` | 2569 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1289 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1011 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1224 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 814 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>呃Xiamen</src><tgt><\|wait\|></tgt>` | 1034 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>일라고 하는 </src><tgt><\|wait\|></tgt>` | 1306 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1045 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1517 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt><\|wait\|></tgt>` | 1567 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 581 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 1741 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>문법 의 </src><tgt><\|wait\|></tgt>` | 1666 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>말깨 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 2043 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>코드 를 </src><tgt>呃，计算机语言，比如Xiamen，我们都能理解，</tgt>` | 2005 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성해야 되는데 </src><tgt><\|wait\|></tgt>` | 814 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1147 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1140 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1235 |

---

### Test Example 35 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 1040 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실 이 일어날 뻔 </src><tgt><\|wait\|></tgt>` | 2139 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>과거 6년 </src><tgt><\|wait\|></tgt>` | 1167 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>한 1000년 정도 </src><tgt><\|wait\|></tgt>` | 808 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>오긴장이 </src><tgt><\|wait\|></tgt>` | 1577 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1865 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연 업 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1964 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이기적인 </src><tgt><\|wait\|></tgt>` | 1880 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>이야기 할 정도 예 </src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>이제 그런 거죠. </src><tgt>Things like vanadium— they almost went missing. It's a mineral that's been there for about 6,000 to 1,000 years. It's a very selfish mineral, so you can talk about it.</tgt>` | 2493 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>이제 그 후에다가 </src><tgt><\|wait\|></tgt>` | 917 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1282 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 815 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>백오십만 개가 중화 볼 수 </src><tgt><\|wait\|></tgt>` | 1182 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>열핵 미만 으로 </src><tgt><\|wait\|></tgt>` | 1559 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1248 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1047 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1709 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1725 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 혹은 </src><tgt><\|wait\|></tgt>` | 1843 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>폐업해 길도 되는데 </src><tgt><\|wait\|></tgt>` | 2052 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이거 는 </src><tgt><\|wait\|></tgt>` | 1458 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>소기업 들은 </src><tgt>そのうち150万社は、核保有数100万未満の非常に小さな企業でした。一般的に、中小企業は成長するか、あるいは廃業することもあります。しかし、このケースでは中小企業は</tgt>` | 2143 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt><\|wait\|></tgt>` | 1613 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1482 |

---

### Test Example 37 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1065 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어찌 보면 </src><tgt><\|wait\|></tgt>` | 842 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 605 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1346 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1066 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 고 가족 </src><tgt><\|wait\|></tgt>` | 1377 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1686 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1609 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1582 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재생 한 거보다는 </src><tgt><\|wait\|></tgt>` | 955 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>조금 </src><tgt>嗯，怎么说呢，他就是和最年轻的二十岁同龄的弟弟，也是家人，对吧？所以，嗯，与其说是再生，不如说</tgt>` | 3128 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 783 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 543 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 1318 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>잘해놓고 </src><tgt><\|wait\|></tgt>` | 939 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠어. </src><tgt><\|wait\|></tgt>` | 1569 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10 </src><tgt><\|wait\|></tgt>` | 1022 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>12手とか</src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>でした。恐らく</src><tgt><\|wait\|></tgt>` | 1410 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 952 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1424 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>1秒に</src><tgt><\|wait\|></tgt>` | 854 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>行って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1170 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt><\|wait\|></tgt>` | 1709 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1772 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 2063 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>恐ろしく</src><tgt>10、12手くらいでした。おそらく10秒で、まあ1秒にやって今日ぐらいの時間だったかな。で、なんか恐ろしく</tgt>` | 2442 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11手</src><tgt><\|wait\|></tgt>` | 551 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1215 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 989 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 1160 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 872 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who </src><tgt><\|wait\|></tgt>` | 1137 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>just getting going </src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1599 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 837 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>that ten of them </src><tgt><\|wait\|></tgt>` | 1498 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are </src><tgt><\|wait\|></tgt>` | 1697 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>really important </src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 767 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1725 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1871 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>one minute videos </src><tgt>これから、今まさに動き出そうとしている人たちに、本当に重要な10のポイントについてお話しします。1分程度の動画を</tgt>` | 2730 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | 1078 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1253 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>And a little more </src><tgt><\|wait\|></tgt>` | 1236 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail, </src><tgt><\|wait\|></tgt>` | 801 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 857 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 </src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt><\|wait\|></tgt>` | 1551 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 있을 때에 </src><tgt><\|wait\|></tgt>` | 1362 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1144 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1647 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1633 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 </src><tgt><\|wait\|></tgt>` | 1640 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>갔느니라. </src><tgt><\|wait\|></tgt>` | 894 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | 1609 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>너희 에게 </src><tgt>あなたたちも知っているでしょう。ここで異邦人としているとき、言葉を話せない偶像にそのまま引きずられて行ったのです。ですから、私があなたたちに</tgt>` | 2754 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1274 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님의 영으로 </src><tgt><\|wait\|></tgt>` | 991 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는 </src><tgt><\|wait\|></tgt>` | 1209 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1087 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 960 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 1596 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较偏正财</src><tgt><\|wait\|></tgt>` | 1054 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分，也就是</src><tgt><\|wait\|></tgt>` | 1302 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面</src><tgt><\|wait\|></tgt>` | 1647 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长</src><tgt><\|wait\|></tgt>` | 1703 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>所带来的红利</src><tgt><\|wait\|></tgt>` | 1594 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>与收入的提升，</src><tgt><\|wait\|></tgt>` | 966 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果说投资领域方面</src><tgt><\|wait\|></tgt>` | 1708 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>这个月</src><tgt>金運については、今月は悪くないと言えます。ただ、偏正財の分野です。つまり、事業の業績向上による恩恵や収入アップです。投資分野については、今月</tgt>` | 2862 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>也是不错的，</src><tgt><\|wait\|></tgt>` | 1659 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对整体来说，</src><tgt><\|wait\|></tgt>` | 593 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 1285 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 616 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1107 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1057 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you </src><tgt><\|wait\|></tgt>` | 1361 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 922 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1460 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1497 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 634 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1680 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 1899 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, </src><tgt><\|wait\|></tgt>` | 1988 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>학력 수준. 실제로 학업을 얼마나 마쳤나요? 고등학교를 졸업했나요? 그건 한 단계의 학력 수준입니다. 대학에 갔나요? 그리고 졸업했나요?</tgt>` | 2911 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt><\|wait\|></tgt>` | 1886 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 481 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. </src><tgt><\|wait\|></tgt>` | 1240 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>I'll see you online. </src><tgt><\|wait\|></tgt>` | 764 |

---

### Test Example 43 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1213 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새 영화 를 </src><tgt><\|wait\|></tgt>` | 1007 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>옛날 서름이 </src><tgt><\|wait\|></tgt>` | 1247 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋든 차리 돋든 </src><tgt><\|wait\|></tgt>` | 1626 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 너무 </src><tgt><\|wait\|></tgt>` | 1708 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1802 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1810 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 너무 </src><tgt><\|wait\|></tgt>` | 1718 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 719 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>기신이 너무 </src><tgt>目を閉じて新しい映画を観よう。昔のサムライが立ち上がる感じがすごくいいから、それを揺らして一緒に遊ぼうって話なんだ。主人公がすごく魅力的で、</tgt>` | 2789 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>지켜 주라고 </src><tgt><\|wait\|></tgt>` | 1959 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러주다 보니까 </src><tgt><\|wait\|></tgt>` | 1130 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 938 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 816 |

---

### Test Example 44 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1124 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1487 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 927 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1432 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources </src><tgt><\|wait\|></tgt>` | 1705 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though, </src><tgt><\|wait\|></tgt>` | 1116 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>if you get into </src><tgt><\|wait\|></tgt>` | 941 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where </src><tgt><\|wait\|></tgt>` | 1673 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>you realize </src><tgt><\|wait\|></tgt>` | 1675 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>you've added the wrong </src><tgt>另外，你将无法在资源之间移动媒体对象。如果你发现添加了错误的媒体文件，</tgt>` | 1896 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>media files to a particular </src><tgt><\|wait\|></tgt>` | 1019 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, </src><tgt><\|wait\|></tgt>` | 547 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1609 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those </src><tgt><\|wait\|></tgt>` | 597 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>media files and then making sure </src><tgt><\|wait\|></tgt>` | 1363 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 627 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 803 |

---

### Test Example 45 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | 1135 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | 1133 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1486 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 </src><tgt><\|wait\|></tgt>` | 874 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어다니 고 </src><tgt><\|wait\|></tgt>` | 1634 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>있거나 </src><tgt><\|wait\|></tgt>` | 1610 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1689 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1448 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 </src><tgt><\|wait\|></tgt>` | 861 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. </src><tgt><\|wait\|></tgt>` | 1895 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>좀 챙겨야 </src><tgt>进去的话会非常迷路。想开车的话，如果走路的话，那更是天方夜谭。去江北，更是没得说，出国的话，更是惨烈。得好好准备。</tgt>` | 2959 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1677 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 519 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모바일 을 </src><tgt><\|wait\|></tgt>` | 1322 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>구구는 다닌 것 같아요. </src><tgt><\|wait\|></tgt>` | 757 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 743 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수가 </src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 991 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1813 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1139 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1059 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1776 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | 1808 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 1770 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 695 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>주도 하면서 움직이 기 </src><tgt>If the stock market index is rising, large- cap stocks will likely see a sharp rise. However, smaller stocks will move first, leading the market.</tgt>` | 2573 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>때문 에 </src><tgt><\|wait\|></tgt>` | 1272 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1032 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1388 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 716 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 770 |

---

### Test Example 47 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>村せてやるよ。</src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1121 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今、</src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひきてを見ている。</src><tgt><\|wait\|></tgt>` | 1266 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 706 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1533 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>とうに超えている</src><tgt><\|wait\|></tgt>` | 1819 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈の奇跡よ。</src><tgt><\|wait\|></tgt>` | 1978 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1926 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>長年</src><tgt>그럼 그냥 마을로 데려가 버릴 거야. 난 지금 히키데를 보고 있어. 이미 한계는 아득히 넘어선 불멸의 기적이야. 오랜 세월</tgt>` | 2894 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt><\|wait\|></tgt>` | 1464 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってるんだ。</src><tgt><\|wait\|></tgt>` | 825 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1483 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>解足線を</src><tgt><\|wait\|></tgt>` | 571 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | 767 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계속 </src><tgt><\|wait\|></tgt>` | 1113 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 2039 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 766 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1264 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 콘텐츠예요. </src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>B가 컨설턴트 이 </src><tgt><\|wait\|></tgt>` | 1901 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>어가지고 A라는 </src><tgt><\|wait\|></tgt>` | 1826 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람 이 </src><tgt><\|wait\|></tgt>` | 1989 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1800 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>주었을 때 </src><tgt>もちろん、こういうケースもあります。AさんとBさんがコンテンツを共有しているとします。Bさんがコンサルタントで、Aさんが悪意のあるコードを</tgt>` | 1655 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람이 </src><tgt><\|wait\|></tgt>` | 1543 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 900 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스 사이트 스큐티에서 </src><tgt><\|wait\|></tgt>` | 976 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>X-ray까지 </src><tgt><\|wait\|></tgt>` | 441 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감안 이 될까. </src><tgt><\|wait\|></tgt>` | 852 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1043 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1820 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 890 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct. </src><tgt><\|wait\|></tgt>` | 1442 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1587 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is </src><tgt><\|wait\|></tgt>` | 1723 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>that because we're the new cat </src><tgt><\|wait\|></tgt>` | 1962 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>on the block, and because </src><tgt><\|wait\|></tgt>` | 2048 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt><\|wait\|></tgt>` | 1752 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>changed from </src><tgt>活動、そして自分自身で基準を定義することです。なぜなら、あなたは完全に正しいからです。しかし現実として、私たちが新しい猫のブロックであり、基準が</tgt>` | 1683 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt><\|wait\|></tgt>` | 1549 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1159 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard </src><tgt><\|wait\|></tgt>` | 890 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 804 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 586 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1120 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1040 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうだけじゃなくて、</src><tgt><\|wait\|></tgt>` | 1640 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルパイソン</src><tgt><\|wait\|></tgt>` | 1017 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1309 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも、</src><tgt><\|wait\|></tgt>` | 1641 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルの書いて</src><tgt><\|wait\|></tgt>` | 1807 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>後、それ自体は</src><tgt><\|wait\|></tgt>` | 1807 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>パイソンコードなん、そっから生成される</src><tgt><\|wait\|></tgt>` | 2105 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>って、それが</src><tgt><\|wait\|></tgt>` | 1569 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで信号処理</src><tgt>This is not just a visual development environment; it's a Visual Python development environment. Because you write the flow graph visually, and that itself is Python code, which is then executed, that's how</tgt>` | 2053 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1483 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことをしている</src><tgt><\|wait\|></tgt>` | 1155 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>からですね。</src><tgt><\|wait\|></tgt>` | 885 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 805 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はい。じゃあ、</src><tgt><\|wait\|></tgt>` | 584 |

---

### Test Example 51 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1081 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt><\|wait\|></tgt>` | 1072 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1566 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真挚意图的。</src><tgt><\|wait\|></tgt>` | 1226 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1195 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1619 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>后经场会提到，</src><tgt><\|wait\|></tgt>` | 1615 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>人们这样说：“</src><tgt><\|wait\|></tgt>` | 944 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1603 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人</src><tgt>相手の感情や真意を推し量ったり感じ取ったりすることです。多くの人が後世の場でも言っています。そう言います。「見てください、この人は</tgt>` | 2792 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了！”</src><tgt><\|wait\|></tgt>` | 1450 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 871 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1388 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 723 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 707 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>是说。</src><tgt><\|wait\|></tgt>` | 568 |

---

### Test Example 52 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대 </src><tgt><\|wait\|></tgt>` | 766 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1048 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1702 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 795 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠 자의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1591 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 제품, </src><tgt><\|wait\|></tgt>` | 1707 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FPD 파이 프를 </src><tgt><\|wait\|></tgt>` | 1848 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128 비트 로 </src><tgt><\|wait\|></tgt>` | 2082 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나중 가서 로 포인 다. </src><tgt><\|wait\|></tgt>` | 1778 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src><\|wait\|></src><tgt>そしてこれについて多くの人が分析しています。ロクジャの分析を見ると、ソニーがイオパック製品のFPDパイプを128ビットに後から変更するようです。</tgt>` | 1853 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈, </src><tgt><\|wait\|></tgt>` | 1525 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1176 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt><\|wait\|></tgt>` | 931 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>S2가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 892 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 547 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1394 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>on the first section </src><tgt><\|wait\|></tgt>` | 1504 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 889 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR </src><tgt><\|wait\|></tgt>` | 1423 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>field being of </src><tgt><\|wait\|></tgt>` | 1033 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>critical importance </src><tgt><\|wait\|></tgt>` | 902 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1692 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 841 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously not my love. </src><tgt>EHR分野が変異データベースよりも重要だという最初のセクションで、少し混乱していました。もちろん、それは私の好みではありません。</tgt>` | 2946 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt><\|wait\|></tgt>` | 944 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>if we don't agree </src><tgt><\|wait\|></tgt>` | 646 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1521 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in </src><tgt><\|wait\|></tgt>` | 751 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>these data sources </src><tgt><\|wait\|></tgt>` | 1298 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from, </src><tgt><\|wait\|></tgt>` | 738 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | 940 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 387 |

---

### Test Example 54 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all of the </src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>short- lived </src><tgt><\|wait\|></tgt>` | 1008 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>decisions, that's the way </src><tgt><\|wait\|></tgt>` | 1801 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>we </src><tgt><\|wait\|></tgt>` | 690 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>in our future, </src><tgt><\|wait\|></tgt>` | 1736 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>in love. </src><tgt><\|wait\|></tgt>` | 1491 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>We may </src><tgt><\|wait\|></tgt>` | 668 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>all rush into </src><tgt><\|wait\|></tgt>` | 1691 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2012 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>the end in a state of </src><tgt>모든 단기적인 결정은 결국 우리가 사랑하는 미래로 나아가는 길입니다. 우리는 모두</tgt>` | 2608 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>love. </src><tgt><\|wait\|></tgt>` | 426 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>We'll reach the end. </src><tgt><\|wait\|></tgt>` | 1971 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>It will become </src><tgt><\|wait\|></tgt>` | 1179 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>end. </src><tgt><\|wait\|></tgt>` | 913 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>That's the point. </src><tgt><\|wait\|></tgt>` | 834 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>We'll be </src><tgt><\|wait\|></tgt>` | 631 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>in love. </src><tgt><\|wait\|></tgt>` | 361 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 845 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>in Noah's Genesis </src><tgt><\|wait\|></tgt>` | 1027 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>2:3, </src><tgt><\|wait\|></tgt>` | 1562 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 906 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's supposed to </src><tgt><\|wait\|></tgt>` | 1404 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1724 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry. </src><tgt><\|wait\|></tgt>` | 1799 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>And so he says to </src><tgt><\|wait\|></tgt>` | 1790 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, </src><tgt><\|wait\|></tgt>` | 1598 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the Son of God, prove it </src><tgt><\|wait\|></tgt>` | 876 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src><\|wait\|></src><tgt>そして、ノア記2章3節では、彼は自分が40日間飢えながら荒野にいるはずだと知っています。だから彼はイエスに言います。「もしあなたが神の御子なら、それを証明してみせなさい。</tgt>` | 2982 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1778 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1139 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 926 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 824 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man </src><tgt><\|wait\|></tgt>` | 531 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan led by </src><tgt><\|wait\|></tgt>` | 403 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>a brother alone. </src><tgt><\|wait\|></tgt>` | 414 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1238 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful, </src><tgt><\|wait\|></tgt>` | 1001 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1163 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1196 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1321 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. And I don't know </src><tgt><\|wait\|></tgt>` | 1216 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 955 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1651 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the the vanguard of </src><tgt><\|wait\|></tgt>` | 1757 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1265 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>These days. </src><tgt>有意义的、个人的权利，最高法院最后才介入，而不是引领。我不知道法院是否想成为社会变革的先锋。现在。</tgt>` | 2378 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 964 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 566 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1367 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 901 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 1279 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 660 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 788 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 594 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 357 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>但他们更反映的是已经形成的共识。所以。你有一些联邦法官，他们……</tgt>` | 513 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1083 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1555 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1233 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>的一个是</src><tgt><\|wait\|></tgt>` | 1101 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>客厅的部分，</src><tgt><\|wait\|></tgt>` | 1688 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | 1562 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是</src><tgt><\|wait\|></tgt>` | 584 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>属于我们</src><tgt><\|wait\|></tgt>` | 1650 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>休息的地方，</src><tgt><\|wait\|></tgt>` | 2002 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>所以呢，</src><tgt>그럼 사진을 한번 보겠습니다. 사진 부분에는 거실이 보이네요. 거실은 보통 우리가 쉬는 공간이라서,</tgt>` | 2561 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的</src><tgt><\|wait\|></tgt>` | 513 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>部分呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1961 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 1190 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 891 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | 812 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 577 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可如果我们看到</src><tgt><\|wait\|></tgt>` | 379 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是双友一人的吗？</src><tgt><\|wait\|></tgt>` | 468 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 340 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt>몸의 부분이라서, 당신에게 잠시 시간을 내어 편안하게 앉아 쉴 수 있는 공간을 의미합니다. 만약 여기 ' 쌍둥이 한 사람 ' 이라고 표시되어 있다면요? 네, 그래서 그렇습니다.</tgt>` | 896 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 856 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1036 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1647 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 897 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to completely </src><tgt><\|wait\|></tgt>` | 1314 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1784 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1667 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is </src><tgt><\|wait\|></tgt>` | 1117 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 1135 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1913 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>While they're </src><tgt>これらの人々は極めて稀で、世界を完全に革命するよう現れることもあります。その性格は矛盾しています。彼らは</tgt>` | 2736 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | 989 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1290 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1203 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 894 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like it </src><tgt><\|wait\|></tgt>` | 806 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>gets straight to the point. </src><tgt><\|wait\|></tgt>` | 675 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 316 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 352 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>the devil's advocate, </src><tgt><\|wait\|></tgt>` | 403 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never </src><tgt>外向的ですが、無意味な会話も嫌います。要点をまっすぐ言うのが好きです。悪魔の代弁者になるのも好きで、</tgt>` | 635 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>shy away from a debate. </src><tgt><\|wait\|></tgt>` | 375 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 315 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E. N. T. P. </src><tgt><\|wait\|></tgt>` | 400 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 382 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 877 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt><\|wait\|></tgt>` | 1103 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 2007 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 758 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1326 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1618 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1837 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1777 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 2041 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1821 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok had made quite a show of himself, claiming he had rejected the government and was running for the nomination and the election. But now, the moment Yoon Suk- yeol removed Kim Jong- in,</tgt>` | 2306 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1080 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 1401 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 712 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뜻끼를 품은 </src><tgt><\|wait\|></tgt>` | 826 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 515 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 354 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 </src><tgt><\|wait\|></tgt>` | 312 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 375 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 353 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상급건. </src><tgt><\|wait\|></tgt>` | 322 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt>Lee Jun- seok is preparing to attack Yoon Suk- yeol, with the intention of removing him. This is the level of attack that Lee Jun- seok, the ' chest- level' Lee Jun- seok.</tgt>` | 735 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 318 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 학이 얼마나 </src><tgt><\|wait\|></tgt>` | 409 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 320 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 10 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1016 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食堂で今</src><tgt><\|wait\|></tgt>` | 1059 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってるみたいです。なので</src><tgt><\|wait\|></tgt>` | 1312 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 1051 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>このホルモンホテル</src><tgt><\|wait\|></tgt>` | 1445 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 637 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>焼肉が食べれる場所</src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1629 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので</src><tgt><\|wait\|></tgt>` | 1727 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 951 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>ここゴルドストンホテル</src><tgt>Well, it looks like they're making it in the cafeteria right now. So, this Goldston Hotel is also going to be a place where you can have yakiniku. So, in the future,</tgt>` | 3290 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 848 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | 1128 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 1169 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>もまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1210 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt><\|wait\|></tgt>` | 844 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 780 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>ここのホテルからですね</src><tgt><\|wait\|></tgt>` | 628 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>プサン駅も</src><tgt><\|wait\|></tgt>` | 368 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 356 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt>if you're thinking about staying here, I'd recommend checking it out. It's a good option. From this hotel, you can walk</tgt>` | 604 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるか分からないか</src><tgt><\|wait\|></tgt>` | 279 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルでのね</src><tgt><\|wait\|></tgt>` | 258 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 300 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので</src><tgt><\|wait\|></tgt>` | 308 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 350 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 405 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 311 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は。</src><tgt><\|wait\|></tgt>` | 206 |
