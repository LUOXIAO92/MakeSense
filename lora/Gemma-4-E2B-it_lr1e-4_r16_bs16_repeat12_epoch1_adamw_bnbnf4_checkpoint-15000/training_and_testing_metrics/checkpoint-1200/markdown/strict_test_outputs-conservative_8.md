# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9526
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4371
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.9429
  - TGT_RELEASE_TOTAL: 70
  - TGT_WAIT_ACCURACY: 0.9962
  - TGT_WAIT_TOTAL: 799
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1344.4170
  - PROCESS_TIME_MS_P50: 1320.3460
  - PROCESS_TIME_MS_P95: 2048.7590
  - PROCESS_TIME_MS_MAX: 3725.0250

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1139 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>外在声音这一点，</src><tgt><\|wait\|></tgt>` | 1157 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个优势</src><tgt><\|wait\|></tgt>` | 1454 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>很大。然后</src><tgt><\|wait\|></tgt>` | 1245 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢，</src><tgt><\|wait\|></tgt>` | 1269 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在面对</src><tgt><\|wait\|></tgt>` | 992 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶人</src><tgt><\|wait\|></tgt>` | 1108 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1591 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels—</tgt>` | `<src>这个特点，</src><tgt>The external voice is a big advantage. And when I face Tao Ren,</tgt>` | 1823 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1529 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和陶人。</src><tgt><\|wait\|></tgt>` | 1177 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 722 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1072 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>仲まだ一年生</src><tgt><\|wait\|></tgt>` | 1473 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>ですからね。</src><tgt><\|wait\|></tgt>` | 1233 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1242 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告</src><tgt><\|wait\|></tgt>` | 1063 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選択を</src><tgt><\|wait\|></tgt>` | 1078 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう退ず</src><tgt><\|wait\|></tgt>` | 1655 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，</tgt>` | `<src>してあげると</src><tgt>一开始，特别是仲还没上一年级，所以这个时候如果选择密告，</tgt>` | 1922 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>受験立てても</src><tgt><\|wait\|></tgt>` | 1524 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>退した。</src><tgt><\|wait\|></tgt>` | 1537 |

---

### Test Example 3 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 1086 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1148 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1351 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 600 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1426 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1587 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>어떤 분입니다. </src><tgt><\|wait\|></tgt>` | 1727 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt>The students on the list were actually not highly intelligent. They were randomly selected students.</tgt>` | 1852 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 1516 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>모을 닫던 교사 들은 </src><tgt><\|wait\|></tgt>` | 1889 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘撒完以后呢，</src><tgt><\|wait\|></tgt>` | 1151 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力</src><tgt><\|wait\|></tgt>` | 1367 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 1223 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>衰弱了，然后就</src><tgt><\|wait\|></tgt>` | 1591 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>停留在</src><tgt><\|wait\|></tgt>` | 1642 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1458 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 597 |
| 9 | `<src>状态，</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。</tgt>` | `<src>态。</src><tgt>淘撒が終わると、内部のエネルギーも衰弱して、相対的に低エネルギーな運行状態に留まってしまいます。</tgt>` | 2484 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 790 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>异于状态。</src><tgt><\|wait\|></tgt>` | 1790 |

---

### Test Example 5 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 798 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 907 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 슉빠시끼고 </src><tgt><\|wait\|></tgt>` | 1408 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 589 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모럴 조깅 </src><tgt><\|wait\|></tgt>` | 1452 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1662 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1623 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt>I'm Apple, and I'm doing my own moral jogging. I'm Park Chan's</tgt>` | 1994 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 1598 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1832 |

---

### Test Example 6 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 785 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>saying? </src><tgt><\|wait\|></tgt>` | 1031 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1508 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1233 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension start? </src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? </src><tgt><\|wait\|></tgt>` | 1661 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a head? </src><tgt><\|wait\|></tgt>` | 1655 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it tension in your chest? </src><tgt><\|wait\|></tgt>` | 881 |
| 9 | `<src>I ask them what </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I have a </src><tgt>你的身体在说什么？把针尖放在身体上。紧张感从哪里开始？是什么？是头？是胸部？</tgt>` | 2218 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>strong link with you. </src><tgt><\|wait\|></tgt>` | 1049 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>Using. </src><tgt><\|wait\|></tgt>` | 1659 |

---

### Test Example 7 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt><\|wait\|></tgt>` | 1043 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1221 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people? This is </src><tgt><\|wait\|></tgt>` | 1369 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem. </src><tgt><\|wait\|></tgt>` | 877 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research looking at </src><tgt><\|wait\|></tgt>` | 956 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1654 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10% of the happiest </src><tgt><\|wait\|></tgt>` | 1750 |
| 9 | `<src>of the happiest people </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people </src><tgt>非常に幸せな人々の研究を、様々な角度から行いました。これはまだ序の口です。最も幸せな人々の10%を研究する</tgt>` | 2901 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. People that </src><tgt><\|wait\|></tgt>` | 986 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1838 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 939 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 1025 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1437 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1254 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>汇报主管，或是通知对方</src><tgt><\|wait\|></tgt>` | 1505 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现在这个状况。</src><tgt><\|wait\|></tgt>` | 1252 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 644 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1771 |
| 9 | `<src>独立承担。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>工具理性</src><tgt>When faced with this situation, we just need to report it to our supervisor or let them know about the situation. Don't think you can handle everything yourself. Tools are rational,</tgt>` | 2994 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>承单，责任而已，</src><tgt><\|wait\|></tgt>` | 1223 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是给工具。</src><tgt><\|wait\|></tgt>` | 1496 |

---

### Test Example 9 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1119 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あのいただろうといったような</src><tgt><\|wait\|></tgt>` | 1479 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ものも用意しております</src><tgt><\|wait\|></tgt>` | 1253 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1220 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1074 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1089 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1592 |
| 9 | `<src>えっと</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements,</tgt>` | `<src>て、えっと</src><tgt>We have T-shirts and other items available, so please feel free to join us. For contact, that's all for now.</tgt>` | 2146 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>連絡は</src><tgt><\|wait\|></tgt>` | 1354 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>内側がありますので</src><tgt><\|wait\|></tgt>` | 1403 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1127 |

---

### Test Example 10 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 661 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1097 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个</src><tgt><\|wait\|></tgt>` | 1260 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>轨道，让我</src><tgt><\|wait\|></tgt>` | 1146 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够好自在</src><tgt><\|wait\|></tgt>` | 657 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>他下班的时候，</src><tgt><\|wait\|></tgt>` | 1377 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在工作</src><tgt><\|wait\|></tgt>` | 1648 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>和餐上，</src><tgt><\|wait\|></tgt>` | 1680 |
| 9 | `<src><\|wait\|></src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>我当时</src><tgt>제가 제 삶의 궤도로 돌아가서, 퇴근 후 일과 식사를</tgt>` | 1990 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被他</src><tgt><\|wait\|></tgt>` | 1442 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>作为妻子的一个小小的一个愿望</src><tgt><\|wait\|></tgt>` | 1906 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src>哈。</src><tgt><\|wait\|></tgt>` | 943 |

---

### Test Example 11 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大体</src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>初めての</src><tgt><\|wait\|></tgt>` | 1443 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1309 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1471 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt><\|wait\|></tgt>` | 1688 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1457 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt><\|wait\|></tgt>` | 612 |
| 9 | `<src>ルナールなど</src><tgt>大致是从这一带开始的，</tgt>` | `<src><\|wait\|></src><tgt>大概从这开始，</tgt>` | 1530 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 1742 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>絵</src><tgt><\|wait\|></tgt>` | 1765 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 976 |

---

### Test Example 12 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>あとなんか</src><tgt><\|wait\|></tgt>` | 1238 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1158 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1353 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 1241 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱりですね</src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>介護したい方って</src><tgt><\|wait\|></tgt>` | 1257 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐに行こう意識が</src><tgt><\|wait\|></tgt>` | 863 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>高いし</src><tgt><\|wait\|></tgt>` | 1514 |
| 9 | `<src>自分で</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且</tgt>` | `<src>家で見てと</src><tgt>还有，大将好像有点想离得远一点，所以想照顾人的人，</tgt>` | 2046 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>友達やととしながら</src><tgt><\|wait\|></tgt>` | 1528 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>こうが強いので</src><tgt><\|wait\|></tgt>` | 1887 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1657 |

---

### Test Example 13 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做什么？</src><tgt><\|wait\|></tgt>` | 1114 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1459 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们身生的爱交</src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt><\|wait\|></tgt>` | 1473 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1728 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给</src><tgt><\|wait\|></tgt>` | 1646 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>主孩子心灵</src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src><\|wait\|></src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment,</tgt>` | `<src>营养，</src><tgt>What do parents need to do? Use our love and water to nourish our children's hearts,</tgt>` | 2246 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>给那孩子</src><tgt><\|wait\|></tgt>` | 1715 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1841 |

---

### Test Example 14 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气数是容易的，</src><tgt><\|wait\|></tgt>` | 1205 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1326 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt><\|wait\|></tgt>` | 1322 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导到</src><tgt><\|wait\|></tgt>` | 1509 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1671 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>如初于中坚。</src><tgt><\|wait\|></tgt>` | 1689 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1650 |
| 9 | `<src>虚阿凡</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>気数運は簡単に上がりますが、師匠の指導があって初めて中堅に達します。だからこそ、反省が必要なのです。</tgt>` | 2056 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1832 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师傅，</src><tgt><\|wait\|></tgt>` | 2039 |

---

### Test Example 15 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1090 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 1443 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1283 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설 용심이 가 </src><tgt><\|wait\|></tgt>` | 1597 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1684 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1661 |
| 9 | `<src>진짜 이거 </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>So I have a mix of sword and dragon spirit. Wow, this is really</tgt>` | 2061 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>행으로도 조금 죽입니다. </src><tgt><\|wait\|></tgt>` | 1987 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>진짜 </src><tgt><\|wait\|></tgt>` | 1875 |

---

### Test Example 16 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 786 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAがですね</src><tgt><\|wait\|></tgt>` | 929 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1100 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうか</src><tgt><\|wait\|></tgt>` | 1019 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>によっては</src><tgt><\|wait\|></tgt>` | 882 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>Aの欄を</src><tgt><\|wait\|></tgt>` | 1604 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1649 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生食かどうか</src><tgt><\|wait\|></tgt>` | 1660 |
| 9 | `<src>保証する、生息である</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence—</tgt>` | `<src>を調べる生食かどうか</src><tgt>So, in various situations, depending on whether it's raw or cooked, you check the A column to see if it's raw or cooked.</tgt>` | 2983 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>を保証するって</src><tgt><\|wait\|></tgt>` | 904 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>いったい何の使い方を</src><tgt><\|wait\|></tgt>` | 1881 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されます。</src><tgt><\|wait\|></tgt>` | 1870 |

---

### Test Example 17 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 985 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chunhatteru. </src><tgt><\|wait\|></tgt>` | 1150 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1378 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a BA in </src><tgt><\|wait\|></tgt>` | 1266 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Finance and a </src><tgt><\|wait\|></tgt>` | 1478 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>B.A. in Psychology. </src><tgt><\|wait\|></tgt>` | 1702 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1653 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at Yale, </src><tgt><\|wait\|></tgt>` | 1115 |
| 9 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>and in the </src><tgt>제 이름은 Chunhatteru입니다. 현재 Yale에서 금융학 학사 학위와 심리학 학사 학위를 동시에 전공하고 있습니다.</tgt>` | 2049 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go into </src><tgt><\|wait\|></tgt>` | 1169 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate </src><tgt><\|wait\|></tgt>` | 1483 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1894 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 730 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 1122 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不够的人之间</src><tgt><\|wait\|></tgt>` | 1505 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有着某种</src><tgt><\|wait\|></tgt>` | 1217 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>典型性，</src><tgt><\|wait\|></tgt>` | 1285 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1126 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 982 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从天体系列</src><tgt><\|wait\|></tgt>` | 1657 |
| 9 | `<src><\|wait\|></src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night?</tgt>` | `<src>开始的？</src><tgt>If there's a certain type of typicality between a female high school student and someone who isn't physically attractive, could it be from the start of the ' Celestial Series'?</tgt>` | 3116 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1085 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 1622 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>系列篇。</src><tgt><\|wait\|></tgt>` | 1760 |

---

### Test Example 19 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 830 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 1053 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>to set up </src><tgt><\|wait\|></tgt>` | 805 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>7GBが</src><tgt><\|wait\|></tgt>` | 1223 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>ありましたが、</src><tgt><\|wait\|></tgt>` | 1502 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1653 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井氏の仕組み</src><tgt><\|wait\|></tgt>` | 1720 |
| 9 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>は</src><tgt>그래서 7GB를 설정하려고 했는데, 나가이 씨의 시스템은</tgt>` | 1856 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>もうコン</src><tgt><\|wait\|></tgt>` | 1565 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>7GB</src><tgt><\|wait\|></tgt>` | 1147 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1328 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビです。</src><tgt><\|wait\|></tgt>` | 1812 |

---

### Test Example 20 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1106 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 872 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1139 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 927 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1011 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1557 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1701 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1643 |
| 9 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们</tgt>` | `<src><\|wait\|></src><tgt>好的。然后，在这些例子之后，指令告诉我们，实际上</tgt>` | 1836 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. So </src><tgt><\|wait\|></tgt>` | 1634 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1530 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game.board array </src><tgt><\|wait\|></tgt>` | 1025 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1723 |

---

### Test Example 21 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 916 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 층을 </src><tgt><\|wait\|></tgt>` | 1115 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라고 주고 내가 </src><tgt><\|wait\|></tgt>` | 1491 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수도다. </src><tgt><\|wait\|></tgt>` | 1422 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1403 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔팀 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 1750 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>하자나? 내가 </src><tgt><\|wait\|></tgt>` | 1652 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1690 |
| 9 | `<src><\|wait\|></src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room?</tgt>` | `<src>줄은 아니야. </src><tgt>I might have come here to kill the other floor. I'm not asking the other team to kill them, am I? I'm not the one who's not hearing that.</tgt>` | 3637 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 940 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1451 |

---

### Test Example 22 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라는 </src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>이런 것들은 </src><tgt><\|wait\|></tgt>` | 1074 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실 이 일어났 습니다. </src><tgt><\|wait\|></tgt>` | 1841 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 915 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>거진 유산 한 적인 </src><tgt><\|wait\|></tgt>` | 1569 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>종류 로 굉장히 </src><tgt><\|wait\|></tgt>` | 1663 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1589 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다. </src><tgt><\|wait\|></tgt>` | 1306 |
| 9 | `<src>이렇게 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where</tgt>` | `<src>이거 굉장히 </src><tgt>There was a lot of loss of vanadium. This is definitely a mineral. It's</tgt>` | 1051 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1244 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1824 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그 후에다가 </src><tgt><\|wait\|></tgt>` | 930 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아니면 </src><tgt><\|wait\|></tgt>` | 1580 |

---

### Test Example 23 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 이럴 찌 너무 </src><tgt><\|wait\|></tgt>` | 1133 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 947 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>이 저열하려 했지만 </src><tgt><\|wait\|></tgt>` | 1491 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1304 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 의 </src><tgt><\|wait\|></tgt>` | 1522 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 인데 꿈일 </src><tgt><\|wait\|></tgt>` | 1860 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 하고 있고 </src><tgt><\|wait\|></tgt>` | 1581 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 보살 로 </src><tgt><\|wait\|></tgt>` | 1673 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보일 피라고 보이 세 우주 까지 </src><tgt>これ、あまりにも低く見ようとしていたんですが、本当に菩薩です。いや、自分の菩薩で、夢だと聞いています。私だけ菩薩に見えるように、宇宙まで</tgt>` | 3704 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>간다. 이 보살 이란 </src><tgt><\|wait\|></tgt>` | 1684 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>그냥 </src><tgt><\|wait\|></tgt>` | 715 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1064 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 834 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1144 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 784 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>出せなくなって</src><tgt><\|wait\|></tgt>` | 1215 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>しまうので、</src><tgt><\|wait\|></tgt>` | 1546 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1668 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1644 |
| 9 | `<src>ナットが</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>ナットが</src><tgt>이게 기어입니다. 기어가 헐거워지면 신호가 안 나오게 되니까, 기어 끝에 역나사 너트가</tgt>` | 2444 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1211 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1787 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい</src><tgt><\|wait\|></tgt>` | 1096 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>文型完了を</src><tgt><\|wait\|></tgt>` | 1458 |

---

### Test Example 25 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1181 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1060 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1431 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learned and to repeat </src><tgt><\|wait\|></tgt>` | 1304 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out you're good at </src><tgt><\|wait\|></tgt>` | 1596 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1715 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1801 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>yet. </src><tgt><\|wait\|></tgt>` | 1555 |
| 9 | `<src>get the people around you to help you with. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src>Get the people around you to help you with </src><tgt>最后，就是重复。学习并重复，找出自己擅长的地方，然后多做一些。嗯，你还没那么好。让身边的人来帮你</tgt>` | 3582 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 825 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and and tell the next time </src><tgt><\|wait\|></tgt>` | 1865 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 831 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是说</src><tgt><\|wait\|></tgt>` | 1106 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二classList，</src><tgt><\|wait\|></tgt>` | 1261 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>它服务</src><tgt><\|wait\|></tgt>` | 1129 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 667 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们。</src><tgt><\|wait\|></tgt>` | 1380 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1611 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1717 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>维生运动好事期间，</src><tgt>2つ目は、二クラスです。これは、一級・一線で戦うトップクラスのプレイヤーをサポートします。例えば、維生運動の好事期間中、</tgt>` | 3136 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1011 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维生运动</src><tgt><\|wait\|></tgt>` | 1696 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>平分的星棒，</src><tgt><\|wait\|></tgt>` | 1872 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1373 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1137 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1068 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment </src><tgt><\|wait\|></tgt>` | 1487 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1256 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1531 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1477 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change can </src><tgt><\|wait\|></tgt>` | 1282 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 774 |
| 9 | `<src>in the United States. </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>happen in the United States. </src><tgt>19세 개정안의 의미와 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 그 역사를 탐구하는 것입니다.</tgt>` | 2997 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1077 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meaning of the amendment </src><tgt><\|wait\|></tgt>` | 1713 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of course I'm </src><tgt><\|wait\|></tgt>` | 1885 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>Maryed. </src><tgt><\|wait\|></tgt>` | 1448 |

---

### Test Example 28 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1123 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 986 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，不是</src><tgt><\|wait\|></tgt>` | 1487 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>一定要</src><tgt><\|wait\|></tgt>` | 1218 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>造成了，所以呢，</src><tgt><\|wait\|></tgt>` | 1302 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 991 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>有什么</src><tgt><\|wait\|></tgt>` | 1060 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>一些遗迹啊，</src><tgt><\|wait\|></tgt>` | 1676 |
| 9 | `<src>也不可能是</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、</tgt>` | `<src>跟风景</src><tgt>皆さんにお伝えしたいのは、このローマは必ずしもそうしたものではありません。ですから、今、何か遺跡や景色が</tgt>` | 2091 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 1408 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>视线就演变出来。</src><tgt><\|wait\|></tgt>` | 1841 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 916 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | 1575 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>各位的朋友呢，</src><tgt><\|wait\|></tgt>` | 1391 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 806 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>rubber band, </src><tgt><\|wait\|></tgt>` | 1104 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1456 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1329 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1551 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets </src><tgt><\|wait\|></tgt>` | 1679 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other </src><tgt><\|wait\|></tgt>` | 1648 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, like </src><tgt><\|wait\|></tgt>` | 1670 |
| 9 | `<src>like heat or light, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light. </src><tgt>고무줄처럼 늘어난 화학 결합도 에너지를 저장합니다. 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 형태의 에너지로 변환됩니다.</tgt>` | 3725 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt><\|wait\|></tgt>` | 999 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make different bonds. </src><tgt><\|wait\|></tgt>` | 1593 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1485 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它到了一个</src><tgt><\|wait\|></tgt>` | 800 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>尖头，</src><tgt><\|wait\|></tgt>` | 1058 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1411 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了尖头之后，</src><tgt><\|wait\|></tgt>` | 1280 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1540 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1467 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>抓住，</src><tgt><\|wait\|></tgt>` | 933 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想着</src><tgt><\|wait\|></tgt>` | 1098 |
| 9 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。</tgt>` | `<src>哎，那我再去操作</src><tgt>尖頭に到達したら、必ず掴んでください。そうしないと、操作を</tgt>` | 2040 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦。</src><tgt><\|wait\|></tgt>` | 1415 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1775 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么呢？</src><tgt><\|wait\|></tgt>` | 930 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>这么讲，因为呢，</src><tgt><\|wait\|></tgt>` | 1720 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1495 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这章的部分</src><tgt><\|wait\|></tgt>` | 778 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1075 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1195 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>带调的人，但是他是</src><tgt><\|wait\|></tgt>` | 1278 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的。</src><tgt><\|wait\|></tgt>` | 747 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这通常</src><tgt><\|wait\|></tgt>` | 1142 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>好吗？这样</src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>一个状况，需要去特别</src><tgt><\|wait\|></tgt>` | 1825 |
| 9 | `<src>特别注意，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>的注意是</src><tgt>이 장의 일부는 ' 조절하는 사람 '을 보여줍니다. 하지만 그는 역방향적입니다. 보통 이런 상황에서는 특별히 주의해야 할 점이 있습니다.</tgt>` | 3054 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1007 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 1468 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>与他调不到</src><tgt><\|wait\|></tgt>` | 1895 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1169 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>呢？</src><tgt><\|wait\|></tgt>` | 938 |

---

### Test Example 32 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 948 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1095 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>符合广播条，</src><tgt><\|wait\|></tgt>` | 1474 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1296 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开道，</src><tgt><\|wait\|></tgt>` | 1607 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1636 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1671 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来整段，</src><tgt><\|wait\|></tgt>` | 1742 |
| 9 | `<src>一下敲腿，</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>以下敲腿</src><tgt>Everything was normal at the time, in line with the broadcast rules. So, I insisted on not opening the door. The duration was about twelve days. I kept knocking,</tgt>` | 3126 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt><\|wait\|></tgt>` | 1131 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1759 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1417 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>一会打开。</src><tgt><\|wait\|></tgt>` | 845 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1021 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1010 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1472 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1341 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1486 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1744 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1705 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>and it's like oh, </src><tgt><\|wait\|></tgt>` | 1720 |
| 9 | `<src>is this word </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>あるいは、何かを書く必要がある場合、テキストを書く場合、スペルが全くわからないことに気づくかもしれません。すると、「あ、この単語は</tgt>` | 2871 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>starts with a double p. </src><tgt><\|wait\|></tgt>` | 1375 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1723 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>Double m. I don't know </src><tgt><\|wait\|></tgt>` | 1537 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 771 |

---

### Test Example 34 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 </src><tgt><\|wait\|></tgt>` | 737 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니 뭐니 </src><tgt><\|wait\|></tgt>` | 925 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1309 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1262 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하는 </src><tgt><\|wait\|></tgt>` | 592 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1454 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그때 로 </src><tgt><\|wait\|></tgt>` | 1688 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 1712 |
| 9 | `<src><\|wait\|></src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>また、ここで異邦人としていられる時に、言葉を話せない偶像へと連れて行かれて、</tgt>` | 2016 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 1468 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희에게 </src><tgt><\|wait\|></tgt>` | 1785 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1014 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt><\|wait\|></tgt>` | 1477 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>영으로 말하는 자는 </src><tgt><\|wait\|></tgt>` | 1434 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 806 |

---

### Test Example 35 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 986 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个财运可以说是</src><tgt><\|wait\|></tgt>` | 1101 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不好的，但是</src><tgt><\|wait\|></tgt>` | 1420 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较赚钱的部分</src><tgt><\|wait\|></tgt>` | 1301 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1440 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面的业绩</src><tgt><\|wait\|></tgt>` | 1669 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>和销售的红利</src><tgt><\|wait\|></tgt>` | 1535 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>以及收入的提升</src><tgt><\|wait\|></tgt>` | 544 |
| 9 | `<src>提升。如果是在</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>呢，</src><tgt>財運に関しては、とても悪いと言えるでしょう。ただ、稼げる部分というのは、事業の業績や販売による利益、そして収入の増加です。</tgt>` | 2775 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>如果是在投资理财方面呢，</src><tgt><\|wait\|></tgt>` | 1296 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月也是</src><tgt><\|wait\|></tgt>` | 1484 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>不好，只是</src><tgt><\|wait\|></tgt>` | 1796 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>相对而言说，</src><tgt><\|wait\|></tgt>` | 1344 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就算</src><tgt><\|wait\|></tgt>` | 754 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>入了那么一点。</src><tgt><\|wait\|></tgt>` | 514 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is </src><tgt><\|wait\|></tgt>` | 1179 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 1000 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1440 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1256 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1568 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 1670 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1466 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>um. </src><tgt><\|wait\|></tgt>` | 598 |
| 9 | `<src>I'm going to go into. </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>これから動き出す人たち、そのうち10人くらいは本当に重要です。えーと、</tgt>` | 2676 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one </src><tgt><\|wait\|></tgt>` | 921 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>minute videos </src><tgt><\|wait\|></tgt>` | 1702 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>at the fall this video. </src><tgt><\|wait\|></tgt>` | 2021 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage of each one </src><tgt><\|wait\|></tgt>` | 1280 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 986 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 1040 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>呃，</src><tgt><\|wait\|></tgt>` | 1026 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HTM이라고 하는 </src><tgt><\|wait\|></tgt>` | 1478 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1557 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | 1698 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>있는 </src><tgt><\|wait\|></tgt>` | 1574 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 어노에 </src><tgt><\|wait\|></tgt>` | 1201 |
| 9 | `<src>문법 에 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>문법 의 </src><tgt>呃，计算机，包括人，都能理解的计算机，</tgt>` | 830 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>학계. 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1660 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 1888 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 2068 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 1195 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1111 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1087 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1082 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>十二手とか</src><tgt><\|wait\|></tgt>` | 1062 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>言った。おそらく</src><tgt><\|wait\|></tgt>` | 1460 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>十秒で</src><tgt><\|wait\|></tgt>` | 1276 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1426 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt><\|wait\|></tgt>` | 1161 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 849 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt><\|wait\|></tgt>` | 1546 |
| 9 | `<src>ね。</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。</tgt>` | `<src><\|wait\|></src><tgt>他说十二手之类的。大概十秒，一秒左右吧。</tgt>` | 1787 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1563 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1147 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十二手</src><tgt><\|wait\|></tgt>` | 1300 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1826 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1222 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 1053 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 1057 |

---

### Test Example 39 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 821 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150개 가 </src><tgt><\|wait\|></tgt>` | 1121 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중화 벌써 1000만으로 </src><tgt><\|wait\|></tgt>` | 1917 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 817 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1470 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 1663 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 기업 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1764 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 에서 </src><tgt><\|wait\|></tgt>` | 1684 |
| 9 | `<src>걷게 되는데 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>이렇게 되는데 </src><tgt>そのうち150社が中国で1000万社に達していました。とても小さな企業でした。一般的に、小さな企業は成長するか、あるいは海外でそうなるのですが、</tgt>` | 3644 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이번 에 </src><tgt><\|wait\|></tgt>` | 1145 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성기 없던 것은 </src><tgt><\|wait\|></tgt>` | 1490 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 폐업도 하지 않은 </src><tgt><\|wait\|></tgt>` | 1888 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1173 |

---

### Test Example 40 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1173 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세인보라 </src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1459 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 서름이 </src><tgt><\|wait\|></tgt>` | 1258 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차리 돋은 </src><tgt><\|wait\|></tgt>` | 1588 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1609 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>한들어서 </src><tgt><\|wait\|></tgt>` | 1444 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 634 |
| 9 | `<src>귀신 이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>기신이 </src><tgt>目を閉じて、セインボラを振るんだ。今はまだ、まだ目が出ていないから、一緒に遊ぼうってことだよ。</tgt>` | 2731 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>많이 굴릴 거고 </src><tgt><\|wait\|></tgt>` | 1128 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>기신이 많이 </src><tgt><\|wait\|></tgt>` | 1634 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>치켜세우라고 </src><tgt><\|wait\|></tgt>` | 1879 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러주다니까 </src><tgt><\|wait\|></tgt>` | 1486 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 마음 에. </src><tgt><\|wait\|></tgt>` | 852 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 1082 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1057 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>濡らせてやる。</src><tgt><\|wait\|></tgt>` | 1146 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1437 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1269 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き知ってみる。</src><tgt><\|wait\|></tgt>` | 1526 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1442 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 847 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1241 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>ふれを気勢。</src><tgt>그럼 젖게 해줄게. 나는 한 번 젖어보자. 이미 한계는 넘어서 버린 기세야.</tgt>` | 2921 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 922 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1737 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなデイを</src><tgt><\|wait\|></tgt>` | 1930 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる。</src><tgt><\|wait\|></tgt>` | 1109 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt><\|wait\|></tgt>` | 1073 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい階族線を見た。</src><tgt><\|wait\|></tgt>` | 570 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>とかない。</src><tgt><\|wait\|></tgt>` | 866 |

---

### Test Example 42 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1034 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>There was such </src><tgt><\|wait\|></tgt>` | 1458 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>interest before, </src><tgt><\|wait\|></tgt>` | 1323 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1542 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>net future TC </src><tgt><\|wait\|></tgt>` | 1668 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>there. </src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>So this is just </src><tgt><\|wait\|></tgt>` | 1710 |
| 9 | `<src>one another place </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个</tgt>` | `<src>one another place </src><tgt>没什么新鲜事。之前确实有那么大的兴趣，netfutureTC。所以这只是</tgt>` | 2173 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1786 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1893 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1064 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1067 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>would like to be </src><tgt><\|wait\|></tgt>` | 592 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 933 |

---

### Test Example 43 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感知</src><tgt><\|wait\|></tgt>` | 1109 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1399 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>对手的感情真实意图的。</src><tgt><\|wait\|></tgt>` | 1332 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1424 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1448 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 960 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>听到人们这样说：</src><tgt><\|wait\|></tgt>` | 1230 |
| 9 | `<src>这样说：“</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や真意を察知すること。よく、人々がこう言います。</tgt>` | 1925 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1461 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又在</src><tgt><\|wait\|></tgt>` | 1796 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>躲藏了。</src><tgt><\|wait\|></tgt>` | 1047 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1435 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1458 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 840 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 948 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 771 |

---

### Test Example 44 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 842 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1401 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1272 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 666 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 퀀텀 앤트예요. </src><tgt><\|wait\|></tgt>` | 1644 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이게 컨설턴트여야 </src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>되고 A라는 </src><tgt><\|wait\|></tgt>` | 1460 |
| 9 | `<src>A라는 사람 이 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>사람 이 </src><tgt>ですから、もちろんこういうケースもあります。AさんとBさんがお互いにクォンタム・エージェントです。これがコンサルタントで、Aさんが</tgt>` | 2931 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1132 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 1633 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람이 </src><tgt><\|wait\|></tgt>` | 1837 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로 사이트 </src><tgt><\|wait\|></tgt>` | 1482 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>스크립트에서 </src><tgt><\|wait\|></tgt>` | 850 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>이 엑스파일까지 </src><tgt><\|wait\|></tgt>` | 1112 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까 </src><tgt><\|wait\|></tgt>` | 888 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1055 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1485 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1258 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1579 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1649 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1505 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat and </src><tgt><\|wait\|></tgt>` | 657 |
| 9 | `<src>block and because the </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>the block, and because </src><tgt>活動、そして自分自身で基準を定義することです。なぜなら、あなたは完全に正しいのですが、現実は、私たちが新しい猫であり、ブロックであるからです。そして</tgt>` | 2861 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt><\|wait\|></tgt>` | 1140 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1397 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>20 years ago. </src><tgt><\|wait\|></tgt>` | 1903 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>We are being held to </src><tgt><\|wait\|></tgt>` | 1455 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>our standard </src><tgt><\|wait\|></tgt>` | 791 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 1098 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is being held to higher standard. </src><tgt><\|wait\|></tgt>` | 913 |

---

### Test Example 46 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1126 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어차피 보면 </src><tgt><\|wait\|></tgt>` | 1125 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1498 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1288 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1520 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1699 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1627 |
| 9 | `<src><\|wait\|></src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>어 </src><tgt>反正，他就是那个和20岁同龄的弟弟，也是家人一样的弟弟。所以</tgt>` | 1979 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>재인 엄마 는 </src><tgt><\|wait\|></tgt>` | 1850 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1321 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1083 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1485 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 829 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내놓고 </src><tgt><\|wait\|></tgt>` | 961 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 899 |

---

### Test Example 47 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1135 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. How far </src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually </src><tgt><\|wait\|></tgt>` | 1402 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>go in your education? </src><tgt><\|wait\|></tgt>` | 1594 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>Did you graduate from high school? </src><tgt><\|wait\|></tgt>` | 1827 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1663 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1578 |
| 9 | `<src>to college, </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>학력 수준. 실제로 교육을 얼마나 받았나요? 고등학교를 졸업했나요? 그건 한 단계의 학력입니다. 대학에 갔나요?</tgt>` | 3249 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And so, did you graduate? </src><tgt><\|wait\|></tgt>` | 1084 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | 1857 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. </src><tgt><\|wait\|></tgt>` | 1540 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now. </src><tgt><\|wait\|></tgt>` | 931 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you </src><tgt><\|wait\|></tgt>` | 790 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 845 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 해매입니다. </src><tgt><\|wait\|></tgt>` | 1181 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1453 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 온 거로 </src><tgt><\|wait\|></tgt>` | 1283 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1478 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>가는 거는 </src><tgt><\|wait\|></tgt>` | 1450 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1309 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 876 |
| 9 | `<src><\|wait\|></src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国</tgt>` | `<src>외국 에게 나가 는 것도 장려 리요. </src><tgt>进去的时候非常迷茫。因为我开车过来，然后走路去，那更是难说，去江南区的话，更是鼓励外国人去。</tgt>` | 3101 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙기 는 거. </src><tgt><\|wait\|></tgt>` | 1645 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1821 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1416 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>뭐 바요. 그거 는 </src><tgt><\|wait\|></tgt>` | 881 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>난인 것 같아요. </src><tgt><\|wait\|></tgt>` | 1038 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね</src><tgt><\|wait\|></tgt>` | 1115 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1118 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>と違ってですね</src><tgt><\|wait\|></tgt>` | 1424 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1259 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1744 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルの書いてあと</src><tgt><\|wait\|></tgt>` | 1826 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>これやつはPython</src><tgt><\|wait\|></tgt>` | 1604 |
| 9 | `<src>にそこから</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>コードなんそっから生成される</src><tgt>This, unlike the visual development environment, is a visual Python development environment. This is also a visual flow graph. And this one is generated from Python code.</tgt>` | 3408 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>やつでそれが</src><tgt><\|wait\|></tgt>` | 810 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1836 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1467 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>ことに</src><tgt><\|wait\|></tgt>` | 750 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているからですね。</src><tgt><\|wait\|></tgt>` | 1040 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 772 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ</src><tgt><\|wait\|></tgt>` | 477 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 782 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1060 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1492 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 1284 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1574 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 1606 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>이력 60에 </src><tgt><\|wait\|></tgt>` | 1714 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FP 파이프를 </src><tgt><\|wait\|></tgt>` | 1775 |
| 9 | `<src>128비트로 낮춘 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>それについて多くの人が分析をしています。このロクジャの分析を見ると、ソニーが</tgt>` | 2448 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것을 로 포인트 한다. </src><tgt><\|wait\|></tgt>` | 1777 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 1858 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1447 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 942 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>CS가 </src><tgt><\|wait\|></tgt>` | 927 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>여기도 없다. </src><tgt><\|wait\|></tgt>` | 847 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 612 |

---

### Test Example 51 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 절수가 </src><tgt><\|wait\|></tgt>` | 933 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승 하는 </src><tgt><\|wait\|></tgt>` | 1073 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1487 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1500 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>어 큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1908 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 1520 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가변 온 </src><tgt><\|wait\|></tgt>` | 1661 |
| 9 | `<src>종목 들이 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>종목 들이 </src><tgt>If the stock price is now showing an upward trend, these large- cap stocks will likely see a significant rise. But first, we need to look at these variable- cap stocks</tgt>` | 3303 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 983 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1880 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1358 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>요소 1초기 가변 온 </src><tgt><\|wait\|></tgt>` | 956 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>종목 을 </src><tgt><\|wait\|></tgt>` | 962 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 912 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 669 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1060 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1126 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1401 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>be able to move media objects </src><tgt><\|wait\|></tgt>` | 1298 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1464 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1462 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1062 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the situation </src><tgt><\|wait\|></tgt>` | 1107 |
| 9 | `<src>a situation </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果</tgt>` | `<src>where you </src><tgt>另外，你将无法在资源之间移动媒体对象。所以，如果你遇到这种情况，</tgt>` | 1901 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1567 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1849 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular </src><tgt><\|wait\|></tgt>` | 2018 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>resource, let us know. </src><tgt><\|wait\|></tgt>` | 1008 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>Now, and we can see about </src><tgt><\|wait\|></tgt>` | 1347 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>moving those media </src><tgt><\|wait\|></tgt>` | 1037 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>files and then making sure </src><tgt><\|wait\|></tgt>` | 498 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get back up </src><tgt><\|wait\|></tgt>` | 704 |
| 18 | `<src>properly. </src><tgt>你发现自己给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 617 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>for all </src><tgt><\|wait\|></tgt>` | 761 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the source </src><tgt><\|wait\|></tgt>` | 1068 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>that is recognized. </src><tgt><\|wait\|></tgt>` | 1458 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>But when we </src><tgt><\|wait\|></tgt>` | 1243 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1214 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>study it, </src><tgt><\|wait\|></tgt>` | 948 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>the source of the love </src><tgt><\|wait\|></tgt>` | 1367 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>we also </src><tgt><\|wait\|></tgt>` | 1536 |
| 9 | `<src>同时进入恨。</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>can also enter </src><tgt>모든 출처를 인정합니다. 하지만 우리가 그것을 연구할 때, 그 사랑의 출처도</tgt>` | 2068 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1471 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>in our own time </src><tgt><\|wait\|></tgt>` | 1843 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>as well. </src><tgt><\|wait\|></tgt>` | 1222 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>It comes to the end. </src><tgt><\|wait\|></tgt>` | 1349 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>It becomes </src><tgt><\|wait\|></tgt>` | 1537 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the source </src><tgt><\|wait\|></tgt>` | 694 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>that we have. </src><tgt><\|wait\|></tgt>` | 964 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>It continues </src><tgt><\|wait\|></tgt>` | 848 |
| 18 | `<src>继续在移动。</src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다. 그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>to evolve. </src><tgt>우리 자신의 시간 속에서도 찾을 수 있습니다. 결국 그것은 우리가 가진 출처가 됩니다. 그리고 계속해서 진화합니다.</tgt>` | 995 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1294 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1043 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1439 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1232 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the AHR field </src><tgt><\|wait\|></tgt>` | 1545 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1668 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1433 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 638 |
| 9 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>最初のセクションで、AHRフィールドが非常に重要であるという点について、少しズレていました。</tgt>` | 2239 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, which is obviously </src><tgt><\|wait\|></tgt>` | 1159 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1901 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1942 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1240 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1114 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these data </src><tgt><\|wait\|></tgt>` | 1059 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>sources that we can </src><tgt><\|wait\|></tgt>` | 465 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from. There's nothing </src><tgt><\|wait\|></tgt>` | 834 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt>バリアントデータベースは、私が大好きです。つまり、これらのデータソースに含めるべきフィールドについて合意できていない場合、そこから引き出すことはできませんよね？</tgt>` | 991 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 314 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1143 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 868 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, and </src><tgt><\|wait\|></tgt>` | 1140 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>the Supreme Court </src><tgt><\|wait\|></tgt>` | 923 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1005 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I don't I don't </src><tgt><\|wait\|></tgt>` | 1763 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>have the courts want to be </src><tgt><\|wait\|></tgt>` | 1670 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1564 |
| 9 | `<src>the the vanguard of social </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为</tgt>` | `<src>the vanguard of </src><tgt>有意义的个人权利，而最高法院最后才介入，而不是作为引领者。我并不认为法院应该</tgt>` | 2183 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1308 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1851 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1258 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1267 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 1433 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 876 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 934 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 874 |
| 18 | `<src>So you have some </src><tgt>法院现在想成为社会变革的先锋，它们更倾向于反映已经形成的共识。所以，</tgt>` | `<src>You have </src><tgt>成为社会变革的先锋。但它们反映的是已经形成的共识。所以，</tgt>` | 868 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 329 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 302 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 317 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 890 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>and it warns Jesus </src><tgt><\|wait\|></tgt>` | 1045 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>of hunger. </src><tgt><\|wait\|></tgt>` | 1393 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1227 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1579 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1698 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry, </src><tgt><\|wait\|></tgt>` | 1795 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1679 |
| 9 | `<src>to Jesus," Hey, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, say, </src><tgt>ある時、イエスは飢えについて警告します。彼は、40日間飢えのまま荒野にいることを知っています。それでイエスに言います。「</tgt>` | 3544 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>if you're the son of God, prove it. </src><tgt><\|wait\|></tgt>` | 1100 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1415 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>Turn these stones to bread. </src><tgt><\|wait\|></tgt>` | 1439 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 801 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with that? </src><tgt><\|wait\|></tgt>` | 1040 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>The temptation. </src><tgt><\|wait\|></tgt>` | 867 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 625 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 428 |
| 18 | `<src>by bread alone. </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？人はパンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>「もしあなたが神の子なら、証明してください。この石をパンに変えなさい。」イエスはそれに対してどう対処したのでしょうか？誘惑に打ち勝ったのです。いや、ヨハネはパンで導いた。一人で。</tgt>` | 935 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1037 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1054 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1424 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | 1344 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>了一个是克汀，</src><tgt><\|wait\|></tgt>` | 1572 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>的部分，</src><tgt><\|wait\|></tgt>` | 1616 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>克汀一般</src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 1699 |
| 9 | `<src>我们</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가</tgt>` | `<src>我们</src><tgt>그럼 사진을 한번 볼까요? 사진 부분에는 ' 크틴 ' 이 있는데, 크틴은 보통</tgt>` | 2206 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>在修饰的地方，</src><tgt><\|wait\|></tgt>` | 1848 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1902 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分。</src><tgt><\|wait\|></tgt>` | 1244 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它会反映的是</src><tgt><\|wait\|></tgt>` | 1085 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1105 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 803 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好的</src><tgt><\|wait\|></tgt>` | 483 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>做一下来修习，</src><tgt><\|wait\|></tgt>` | 448 |
| 18 | `<src>我们可以看到这边是</src><tgt>쉬는 곳이잖아요. 그래서 이 신체 부위도 여러분이 자신에게 시간을 내서 편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可以看到</src><tgt>우리가 수련해야 하는 부분이에요. 그래서 이건 신체 부분이에요. 이건 여러분이 스스로 시간을 들여서 수련할 수 있는 부분이에요. 여기 보시면</tgt>` | 684 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是仿佛一人的嘛。</src><tgt><\|wait\|></tgt>` | 439 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 311 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 352 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 789 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1104 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1462 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1529 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | 1774 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1610 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is something </src><tgt><\|wait\|></tgt>` | 1697 |
| 9 | `<src>something of a </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は</tgt>` | `<src>of a contradiction. </src><tgt>彼らは全く珍しく、世界を完全に変革する存在です。その個性は矛盾をはらんでいます。</tgt>` | 2464 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1584 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're extroverted, </src><tgt><\|wait\|></tgt>` | 1935 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1320 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 939 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1101 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 782 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like it gets straight to the </src><tgt><\|wait\|></tgt>` | 668 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 329 |
| 18 | `<src>They also love to </src><tgt>矛盾しています。外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 308 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate, </src><tgt>外向的ですが、無意味な会話も嫌います。そしてすぐに本題に入ります。彼らは議論の相手を演じるのが大好きです。</tgt>` | 736 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>but they're </src><tgt><\|wait\|></tgt>` | 380 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy about </src><tgt><\|wait\|></tgt>` | 353 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>a debate. </src><tgt><\|wait\|></tgt>` | 306 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 295 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.P. Stansfield </src><tgt><\|wait\|></tgt>` | 393 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>or. </src><tgt><\|wait\|></tgt>` | 337 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 의 이준석은 </src><tgt><\|wait\|></tgt>` | 984 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무 를 거부 한 </src><tgt><\|wait\|></tgt>` | 1116 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1358 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1281 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1586 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1642 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1646 |
| 9 | `<src>윤석열 후보 가 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt>Lee Jun- seok previously claimed he was refusing political duties to nominate his candidate, and even boasted about it. But now, Yoon Suk- yeol's campaign</tgt>` | 2985 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김정은을 </src><tgt><\|wait\|></tgt>` | 1347 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제간 순간 </src><tgt><\|wait\|></tgt>` | 1752 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 1512 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 816 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 1063 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기 를 품은 </src><tgt><\|wait\|></tgt>` | 881 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 662 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 344 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>is determined to attack Yoon Suk- yeol, even after hearing about Kim Jong- un. He's showing a fierce determination to do so.</tgt>` | 718 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 320 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 227 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석 청상 납권 </src><tgt><\|wait\|></tgt>` | 360 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 306 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 </src><tgt><\|wait\|></tgt>` | 322 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 얼마나 </src><tgt><\|wait\|></tgt>` | 328 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재 입니까? </src><tgt><\|wait\|></tgt>` | 350 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1032 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今作って</src><tgt><\|wait\|></tgt>` | 1134 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>みたいです。なので</src><tgt><\|wait\|></tgt>` | 1461 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 1228 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>このホテルを</src><tgt><\|wait\|></tgt>` | 1242 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>朝食が</src><tgt><\|wait\|></tgt>` | 1058 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1096 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になっている</src><tgt><\|wait\|></tgt>` | 1617 |
| 9 | `<src>予定になってるので</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>Well, it looks like they're making something after the meal. So, they're planning to use this hotel for breakfast.</tgt>` | 2410 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1117 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここ五郎ドストンホテル</src><tgt><\|wait\|></tgt>` | 1854 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まっていな</src><tgt><\|wait\|></tgt>` | 1173 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>いっていただく方はですね</src><tgt><\|wait\|></tgt>` | 1437 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt><\|wait\|></tgt>` | 1495 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 774 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 914 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います</src><tgt><\|wait\|></tgt>` | 822 |
| 18 | `<src>のホテルからですね釜山</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt><\|wait\|></tgt>` | 639 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt>So, if you're thinking of staying at the Go-ro-do-ston Hotel, we'd like to consider it. And I think it's a good idea. From this hotel, you can also</tgt>` | 880 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 382 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 353 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかんないかそんなレベル</src><tgt><\|wait\|></tgt>` | 390 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>でのね立地の</src><tgt><\|wait\|></tgt>` | 329 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>いいねまあホテル</src><tgt><\|wait\|></tgt>` | 357 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 267 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 341 |
| 27 | `<src>ご検討なさってみて</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good. If you'd like,</tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 203 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください</src><tgt>walkable, so the location is pretty good. So please consider it.</tgt>` | 243 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それではね</src><tgt><\|wait\|></tgt>` | 186 |
