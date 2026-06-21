# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9903
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9139
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
  - PROCESS_TIME_MS_AVG: 1305.7810
  - PROCESS_TIME_MS_P50: 1332.4480
  - PROCESS_TIME_MS_P95: 2227.2910
  - PROCESS_TIME_MS_MAX: 3391.0050

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1815 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1213 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1438 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 636 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1499 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 399 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 1427 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 1454 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 689 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2322 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1251 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1800 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1388 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1021 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 740 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1320 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 617 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 1702 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1819 |
| 9 | `<src>虚阿凡</src>` | `<src>虚阿凡</src>` | 929 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2148 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 857 |

---

### Test Example 3 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1688 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 726 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 780 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1461 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 491 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1578 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1531 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1976 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1092 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2200 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 718 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1565 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 810 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 862 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1454 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 721 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1246 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1712 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1835 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1133 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 2201 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 722 |

---

### Test Example 5 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2001 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿里</src>` | 1297 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>边，这个油性也很大。</src>` | 1665 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 266 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1783 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 1567 |
| 7 | `<src>儿核桃</src>` | `<src>儿核桃</src>` | 336 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1777 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>仁儿，</src>` | 1537 |
| 10 | `<src>这种核桃</src>` | `<src>对，这种核桃</src>` | 2021 |
| 11 | `<src>仁儿。</src>` | `<src>仁。</src>` | 927 |

---

### Test Example 6 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2071 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 841 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 699 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1498 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1108 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 884 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1656 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1914 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1908 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모르 았 던 </src>` | 1701 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1159 |

---

### Test Example 7 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1664 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 1090 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 1459 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 710 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1779 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1390 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>부모 를 죽인 페르 나 </src>` | 467 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1891 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 2528 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1042 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 1191 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1705 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1199 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 477 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1576 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1806 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 1549 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1315 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 866 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 2632 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 997 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运就属凶。</src>` | 1183 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1775 |
| 2 | `<src>옹심이, </src>` | `<src>옹심이, </src>` | 988 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 721 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 옹심이, 쌀국수하고 </src>` | 1607 |
| 5 | `<src>옹심이가 </src>` | `<src>옹심이가 </src>` | 1791 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1511 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 1464 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 683 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 2227 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해장으로도 조금 죽입니다, </src>` | 1460 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 1183 |

---

### Test Example 10 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1760 |
| 2 | `<src><\|wait\|></src>` | `<src>의 좋아요를 </src>` | 871 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>눌 수 있지만 </src>` | 789 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1596 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 1536 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 근데 꾸밀 필요 가 </src>` | 528 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 </src>` | 1500 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>남한 테 보살 로 보일 필요 가 </src>` | 1961 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요 우주 가 </src>` | 2766 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 보살 이라는 </src>` | 996 |
| 11 | `<src>보살 이라는데. </src>` | `<src>거예요. </src>` | 1662 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1649 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1101 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1332 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 832 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1895 |
| 6 | `<src>research, </src>` | `<src>research, </src>` | 1543 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 1858 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 387 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 2819 |
| 10 | `<src>out there, </src>` | `<src>out there, </src>` | 775 |
| 11 | `<src>people that we can learn from. </src>` | `<src>people that we can learn from. </src>` | 1749 |

---

### Test Example 12 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1924 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1188 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1214 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 824 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1830 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1524 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1467 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 738 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2777 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 965 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1861 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2114 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 729 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1669 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 726 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1738 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 576 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 1156 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 1937 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 906 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 2403 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 816 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1675 |

---

### Test Example 14 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 1901 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 762 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 867 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1493 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 764 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1244 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1570 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1931 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 877 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2263 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 818 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1914 |

---

### Test Example 15 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1839 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 827 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 815 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1453 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 355 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1712 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1574 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1953 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1387 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2047 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1028 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1858 |

---

### Test Example 16 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1922 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 966 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 701 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1561 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1766 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 905 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 926 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1973 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 3391 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 988 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1916 |

---

### Test Example 17 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1674 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1278 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1114 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 828 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1786 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1508 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 334 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1865 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 2358 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1225 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1151 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1713 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1636 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1072 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1688 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 464 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1794 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1504 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 337 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1845 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2591 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1033 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1167 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1674 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1542 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 823 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 854 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1455 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1062 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 953 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1719 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 1907 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2329 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，只有这么一个</src>` | 1420 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望</src>` | 1480 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1335 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1734 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 823 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 885 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 1376 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 368 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 1612 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 1566 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 1245 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 964 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 2772 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 893 |
| 12 | `<src>他们</src>` | `<src>他们</src>` | 1188 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1655 |

---

### Test Example 21 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1693 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 882 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级市场，哎，</src>` | 1683 |
| 4 | `<src>服务</src>` | `<src>服务</src>` | 578 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 931 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1123 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，呃，</src>` | 1503 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1787 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你会</src>` | 459 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 2520 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信公众号评分</src>` | 1042 |
| 12 | `<src>的新榜反而</src>` | `<src>的新榜反而</src>` | 1393 |
| 13 | `<src>火了。</src>` | `<src>火了。</src>` | 1443 |

---

### Test Example 22 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1734 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1406 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1376 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 537 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1780 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1703 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1961 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 2784 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 954 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 1637 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1362 |

---

### Test Example 23 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1664 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 727 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 913 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1637 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1354 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 549 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1551 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 1954 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 974 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 2347 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 595 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 1942 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1516 |

---

### Test Example 24 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1745 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Dettig. </src>` | 1386 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 1251 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 602 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1873 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 1595 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1866 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 713 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2465 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 1022 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1736 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1573 |

---

### Test Example 25 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 1933 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 778 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 862 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1553 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1411 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 604 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1622 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1873 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1240 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 2285 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 775 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1818 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 1323 |

---

### Test Example 26 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 1987 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 855 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 811 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1414 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 857 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1179 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1676 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1878 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1440 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 2061 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 936 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 1966 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1225 |

---

### Test Example 27 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1843 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1061 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 604 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1421 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 734 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1228 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1526 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，跟风险</src>` | 551 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 1575 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 2371 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1232 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1206 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1690 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1417 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1667 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1609 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1502 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 438 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1602 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1535 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1681 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 454 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2393 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 1188 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1214 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1641 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1450 |

---

### Test Example 29 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1948 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 957 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1811 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 496 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1836 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1602 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1872 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 545 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2716 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 709 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1510 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1434 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1371 |

---

### Test Example 30 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1639 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 804 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 882 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1644 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1809 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1740 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1884 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 2863 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 990 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1517 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1300 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1493 |

---

### Test Example 31 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1929 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 918 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1324 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 820 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1796 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1640 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1884 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 730 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 2421 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 831 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1659 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 1802 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1070 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1759 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 963 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1441 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 691 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1553 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 380 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1687 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1853 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1744 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 1818 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1045 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1880 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1320 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1053 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1747 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 853 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 797 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1464 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 763 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1239 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 1582 |
| 8 | `<src>this is just </src>` | `<src>this is just </src>` | 1854 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 375 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 2775 |
| 11 | `<src>But </src>` | `<src>But </src>` | 761 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1194 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1595 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1446 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1096 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1702 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1180 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 382 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1484 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1533 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 466 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1675 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1980 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2616 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 1037 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1303 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1570 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1528 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 955 |

---

### Test Example 35 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2016 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 840 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 1447 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 749 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1565 |
| 6 | `<src>that I think are </src>` | `<src>that I think are </src>` | 448 |
| 7 | `<src>really important. </src>` | `<src>really important. </src>` | 1545 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1890 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1070 |
| 10 | `<src>I have about </src>` | `<src>I have about </src>` | 2286 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 618 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 1693 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1722 |
| 14 | `<src>that cover each one </src>` | `<src>that cover each one </src>` | 1143 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1153 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1603 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1586 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1662 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1864 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1489 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 775 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 1469 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 3127 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 711 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1858 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 폐업 도 </src>` | 1657 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>하지 않는 현상 들을 </src>` | 1184 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1022 |

---

### Test Example 37 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 1960 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 780 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 1784 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 752 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>닭살이 돋든 </src>` | 1712 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1003 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 856 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1834 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1745 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1756 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 1089 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1896 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1290 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1213 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 825 |

---

### Test Example 38 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1830 |
| 2 | `<src>十一二手とか</src>` | `<src>十一二手とか</src>` | 952 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>じゃないですか。おそらく</src>` | 1444 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 691 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 724 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1271 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 1614 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 1874 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 808 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2304 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 790 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1568 |
| 13 | `<src>十一二手で</src>` | `<src>十一二手で</src>` | 1319 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1392 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1004 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 773 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1857 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1170 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1347 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 642 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1699 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 443 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 1430 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1813 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1443 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2207 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1047 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1819 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1403 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1125 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 829 |

---

### Test Example 40 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1591 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 824 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 865 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 1571 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1782 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 1581 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1250 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 957 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 2500 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1128 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1282 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1578 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 1570 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 1024 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 868 |

---

### Test Example 41 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1767 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1280 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1379 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 499 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1750 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1558 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 682 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 1524 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2644 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1025 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1249 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1603 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1545 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1019 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 878 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1879 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 945 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 721 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1408 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 1383 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 679 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1562 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 2028 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 2789 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 993 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1672 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1285 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1478 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1159 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1005 |

---

### Test Example 43 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1847 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 913 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 804 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1425 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今奇跡を見てる。</src>` | 495 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1492 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1517 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 991 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えてる船の奇跡よ。</src>` | 1341 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2772 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 850 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 2121 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1422 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1240 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊船を見た</src>` | 999 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 873 |

---

### Test Example 44 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1877 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 907 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 1890 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 327 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1701 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1505 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 331 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 1875 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 2162 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1233 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 961 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 2011 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1181 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목을 </src>` | 1219 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1027 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 729 |

---

### Test Example 45 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1875 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 751 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 961 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1424 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 343 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1655 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아 </src>` | 1719 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1889 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1631 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1937 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 1022 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1801 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1127 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1061 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 985 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 978 |

---

### Test Example 46 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1789 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 858 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1677 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 751 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 1710 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1004 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 818 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1965 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 2636 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 910 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1134 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1706 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1236 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1059 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 1028 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 819 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1833 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1098 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1332 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 837 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1733 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 420 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 1429 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们</src>` | 1793 |
| 9 | `<src>这样说：“</src>` | `<src>这样说：“</src>` | 980 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2239 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 705 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1733 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1624 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1172 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1029 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 1018 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 369 |

---

### Test Example 48 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 1981 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1286 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1233 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 716 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 1919 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 1501 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 1620 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 나가 면 </src>` | 634 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2651 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이에요. </src>` | 966 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 창피 하네요. </src>` | 1651 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 </src>` | 1297 |
| 13 | `<src>이제 </src>` | `<src>이제 </src>` | 1365 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>열심히 물어봐요. </src>` | 1030 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 1244 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 609 |

---

### Test Example 49 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1953 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1082 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1338 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 723 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1884 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1709 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 1874 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 2574 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 1046 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1040 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1780 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1247 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1041 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 945 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 801 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 576 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1561 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1215 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1448 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 625 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1792 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1751 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 1849 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1245 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 2432 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 1144 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1720 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1264 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1079 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 960 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 805 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 548 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 뭐 </src>` | 1862 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 이런 경우 들도 </src>` | 1114 |
| 3 | `<src>있습니다. </src>` | `<src>있습니다. </src>` | 1342 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 846 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 서로 </src>` | 1850 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>컨설턴트예요, </src>` | 1673 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1834 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>모이 킹 컨설턴트여가지고 </src>` | 1498 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 2074 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1102 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>뿌렸 을 때 </src>` | 1894 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1404 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1025 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스쿠티에서 </src>` | 986 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일 까지 </src>` | 667 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 669 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1804 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 793 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1616 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 698 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1066 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 935 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1505 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1455 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 696 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2320 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1388 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1663 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1461 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1358 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1043 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 1221 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 568 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 381 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 1724 |
| 2 | `<src>首次觉知到</src>` | `<src>首次觉知到</src>` | 963 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象：</src>` | 1346 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 727 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 1112 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 821 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱之中，所谓的爱，</src>` | 1761 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1853 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨。</src>` | 2165 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1330 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 1047 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 1845 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1173 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1129 |
| 15 | `<src><\|wait\|></src>` | `<src>那个</src>` | 868 |
| 16 | `<src>那个钟摆</src>` | `<src>钟摆，</src>` | 954 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在移动。</src>` | 622 |
| 18 | `<src>继续在移动。</src>` | `<src><\|wait\|></src>` | 374 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2136 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 733 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 815 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1415 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 400 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1611 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1512 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 655 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1489 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 2327 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 1398 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1504 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 1511 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 1473 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1038 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 978 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 301 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 772 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 214 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1767 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 910 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1339 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 732 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1536 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 482 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 1711 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1842 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 2476 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 1359 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1665 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1692 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1145 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 1128 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 988 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 566 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 392 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone. </src>` | 343 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1995 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 873 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 782 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1453 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 896 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1141 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1734 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1854 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 2018 |
| 10 | `<src>change </src>` | `<src>change </src>` | 1224 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 617 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1789 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1705 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1004 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1115 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 1012 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 566 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 388 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 315 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 279 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 351 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1760 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 974 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 711 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1575 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1811 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1483 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 341 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1823 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1524 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1958 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 972 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 2043 |
| 13 | `<src>也会反映的是</src>` | `<src>也会反映的是</src>` | 1220 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1041 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间，</src>` | 934 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 828 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息。可是</src>` | 616 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>我们可以看到这边是</src>` | 389 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 378 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 212 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 322 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1759 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 840 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 721 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1414 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 849 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1166 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1563 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1947 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 928 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 2299 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 724 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1650 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1526 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1210 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 1013 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 937 |
| 17 | `<src>get straight to the point. </src>` | `<src>get straight to the point. </src>` | 415 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 572 |
| 19 | `<src>play </src>` | `<src>play </src>` | 305 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 441 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 205 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 337 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 198 |
| 24 | `<src><\|wait\|></src>` | `<src>ENTP stands for </src>` | 255 |
| 25 | `<src>ENTP stands for </src>` | `<src>Extraverted, Intuitive,</src>` | 287 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1868 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1194 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1474 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 399 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1735 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1301 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 560 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1801 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1120 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2313 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 884 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1877 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1336 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | 1491 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 821 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 765 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 588 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 352 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 353 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 이준석의 </src>` | 245 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src><\|wait\|></src>` | 323 |
| 22 | `<src><\|wait\|></src>` | `<src>성상 랍건 </src>` | 261 |
| 23 | `<src>민주당 이 </src>` | `<src><\|wait\|></src>` | 234 |
| 24 | `<src><\|wait\|></src>` | `<src>민주당 의 공격 적의 </src>` | 313 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 239 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1825 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 727 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 911 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいですなのでここのね</src>` | 1577 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 1317 |
| 6 | `<src>も</src>` | `<src>も</src>` | 579 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1625 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1484 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 591 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 2541 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 1138 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1189 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね</src>` | 1672 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1445 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 1052 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 807 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>なとはい思いますここ</src>` | 705 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね釜</src>` | 623 |
| 19 | `<src>駅ももう</src>` | `<src>山駅ももう</src>` | 331 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 256 |
| 21 | `<src>歩いて一分</src>` | `<src>歩いて一分</src>` | 256 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないかそんな</src>` | 389 |
| 23 | `<src>レベルのね</src>` | `<src>レベルのね</src>` | 225 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 255 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 281 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 217 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 146 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 130 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではですね今回は。</src>` | 150 |
