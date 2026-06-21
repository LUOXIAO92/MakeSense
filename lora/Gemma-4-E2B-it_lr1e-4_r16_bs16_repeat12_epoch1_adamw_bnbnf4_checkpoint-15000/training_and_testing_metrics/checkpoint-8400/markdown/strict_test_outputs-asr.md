# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9749
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.7815
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
  - PROCESS_TIME_MS_AVG: 1443.6270
  - PROCESS_TIME_MS_P50: 1504.9810
  - PROCESS_TIME_MS_P95: 2546.7760
  - PROCESS_TIME_MS_MAX: 3102.2170

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1695 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 798 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 1096 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生ですからね。</src>` | 1862 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 918 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1343 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1546 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1572 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 532 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 1111 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1961 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1976 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 979 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1166 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 1576 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1158 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1106 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 1561 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 1840 |
| 9 | `<src>虚阿凡</src>` | `<src>虚阿凡</src>` | 492 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 2393 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 1524 |

---

### Test Example 3 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2169 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 793 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1152 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1761 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 807 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 1508 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 1578 |
| 8 | `<src>때문 입니다. </src>` | `<src>었기 때문 입니다. </src>` | 1868 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1044 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모르 았 던 </src>` | 2468 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1849 |

---

### Test Example 4 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1734 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 763 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 1005 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1885 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 393 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1951 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1647 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1929 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1345 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2166 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1854 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1992 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 918 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 2277 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 760 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1935 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1552 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 303 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 1791 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1636 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2382 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1897 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1934 |
| 2 | `<src>옹심이, </src>` | `<src>보궁 님이 </src>` | 798 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1028 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼, 우심심했. </src>` | 1981 |
| 5 | `<src>옹심이가 </src>` | `<src>어 솔 궁심이 가 </src>` | 1073 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1187 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이는 건데요. </src>` | 1619 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1826 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1987 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해방 으로 </src>` | 2240 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 </src>` | 2157 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2098 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 891 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2175 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 878 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1978 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 1539 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 870 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 1233 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2583 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 1637 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 2202 |

---

### Test Example 8 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2090 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 809 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 1070 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1885 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1777 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 574 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1566 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1945 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2577 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1591 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 2547 |

---

### Test Example 9 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2188 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿里</src>` | 896 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>边，这个油性也很大。</src>` | 2508 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 446 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2002 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 1378 |
| 7 | `<src>儿核桃</src>` | `<src>儿核桃</src>` | 500 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1816 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>仁儿，仁儿，</src>` | 2829 |
| 10 | `<src>这种核桃</src>` | `<src>这种核桃</src>` | 1504 |
| 11 | `<src>仁儿。</src>` | `<src>仁儿。</src>` | 2552 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1882 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 904 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1233 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1792 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1967 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况。</src>` | 1595 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1248 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 886 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 1858 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 2255 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运就属凶。</src>` | 2795 |

---

### Test Example 11 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2210 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 756 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 2270 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 865 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1921 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1038 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 678 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 1843 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 933 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 2228 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 1397 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 2621 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1812 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 866 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1418 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1580 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 2014 |
| 6 | `<src>research, </src>` | `<src>research. </src>` | 708 |
| 7 | `<src>looking at the ten percent </src>` | `<src>Looking at ten percent </src>` | 1160 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1822 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 2648 |
| 10 | `<src>out there, </src>` | `<src>out there, people with </src>` | 1672 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 2744 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1888 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 942 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 죽이 리 </src>` | 2583 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>못하 도록 두루 와서도 </src>` | 483 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다니 는 잔찜의 </src>` | 1977 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1547 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐 내가 </src>` | 1968 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1338 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐 </src>` | 2482 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src><\|wait\|></src>` | 1570 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가 </src>` | 1772 |

---

### Test Example 14 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1901 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Datt리고, </src>` | 1036 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 2042 |
| 4 | `<src><\|wait\|></src>` | `<src>studying IT </src>` | 774 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>Business Finance </src>` | 1787 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 454 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1537 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 1930 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1531 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 2655 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2254 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 724 |

---

### Test Example 15 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1795 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 927 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1250 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1608 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1884 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 422 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1594 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1861 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1640 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2385 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1986 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1203 |

---

### Test Example 16 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1857 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 899 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 2397 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 660 |
| 5 | `<src>자신 의 </src>` | `<src><\|wait\|></src>` | 1953 |
| 6 | `<src><\|wait\|></src>` | `<src>자신 의 메모 를 </src>` | 1638 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>죽인 대로 나 </src>` | 1851 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 510 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 2658 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1378 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 2802 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1800 |
| 2 | `<src>映画でですね、</src>` | `<src>映画出てですね、</src>` | 776 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1026 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 2030 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1217 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1100 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1560 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1935 |
| 9 | `<src>保証する、生息である</src>` | `<src>小する、生息では</src>` | 1585 |
| 10 | `<src>ことを保証する</src>` | `<src>あること保証する</src>` | 2417 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1849 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1316 |

---

### Test Example 18 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1900 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 842 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 2266 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 672 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1240 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 951 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 1609 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 1853 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 504 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 2658 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1314 |
| 12 | `<src>他们</src>` | `<src>他们</src>` | 2333 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 563 |

---

### Test Example 19 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2006 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 801 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 977 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1913 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 377 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1919 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1566 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1959 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1880 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 2356 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 2413 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 647 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1780 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 823 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 2259 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 700 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 947 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1261 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1565 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1988 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1737 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2430 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子</src>` | 2059 |
| 12 | `<src>连篇。</src>` | `<src>思绪连篇。</src>` | 1014 |

---

### Test Example 21 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2098 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 748 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 1044 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1929 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1117 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1194 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1508 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 1919 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 2740 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1600 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 2517 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 511 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1654 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 794 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 1062 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1917 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 720 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1591 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1629 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 1940 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2283 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，只有这么一个</src>` | 2023 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望</src>` | 2695 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 523 |

---

### Test Example 23 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1822 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 766 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1014 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 2007 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1581 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 657 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1567 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 1903 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1042 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 2230 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1233 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 2685 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 966 |

---

### Test Example 24 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1942 |
| 2 | `<src><\|wait\|></src>` | `<src>의 좋아요 를 </src>` | 824 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>눌러 줄 수는 있지만 </src>` | 2245 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 889 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 1951 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보세요 등 꾸밀 필요 가 </src>` | 1630 |
| 7 | `<src>뭐 있고 </src>` | `<src>없고 나와 </src>` | 1925 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>지금 보살 로 보일 필요 가 </src>` | 3102 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>없어요 우주 가 </src>` | 1394 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 </src>` | 2652 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는데. </src>` | 1356 |

---

### Test Example 25 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1739 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1160 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 2260 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 569 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1907 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1560 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 519 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1688 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 1165 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 2295 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 1631 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 </src>` | 1988 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1568 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2108 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 766 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1007 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1970 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 331 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 1977 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1561 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1914 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 2659 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついている</src>` | 1607 |
| 11 | `<src>ね。</src>` | `<src>っていうことですね。</src>` | 2560 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 495 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキ完了。</src>` | 1497 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1962 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 790 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1335 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1578 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1573 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 795 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1481 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 1927 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1109 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2289 |
| 11 | `<src><\|wait\|></src>` | `<src>p, </src>` | 1152 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double lam? I don't </src>` | 2678 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1661 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2138 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 811 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 2476 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 634 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1926 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1268 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 599 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1807 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 2458 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1745 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 2250 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 807 |
| 13 | `<src>myriad. </src>` | `<src>are myriad. </src>` | 1610 |

---

### Test Example 29 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1849 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 836 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级市场，</src>` | 1365 |
| 4 | `<src>服务</src>` | `<src><\|wait\|></src>` | 1589 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1019 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1289 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说</src>` | 1511 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1889 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你会</src>` | 1760 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 2278 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信公众号屏蔽的</src>` | 1944 |
| 12 | `<src>的新榜反而</src>` | `<src>新房</src>` | 1306 |
| 13 | `<src>火了。</src>` | `<src>反而是火了。</src>` | 1678 |

---

### Test Example 30 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2176 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 800 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 1456 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1479 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1139 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1170 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1604 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1834 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1596 |
| 10 | `<src>these values. So </src>` | `<src>these values. So, </src>` | 2607 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2067 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game.config array </src>` | 1023 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1642 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1859 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1336 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1834 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 유사 한 </src>` | 769 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>작용 이 </src>` | 1932 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 굉장히 </src>` | 1567 |
| 7 | `<src>굉장히 아주 </src>` | `<src>바로 </src>` | 650 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1524 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 이제 까지 </src>` | 2372 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>알죠. </src>` | 1750 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2688 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 381 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1635 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1719 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 923 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1075 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1771 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 840 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1389 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1566 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，</src>` | 1861 |
| 9 | `<src><\|wait\|></src>` | `<src>那我再继续操作</src>` | 504 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦，</src>` | 2471 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1505 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 2713 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 595 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1338 |

---

### Test Example 33 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2006 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 853 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 1413 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 1505 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1003 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1220 |
| 7 | `<src>所面临的一些</src>` | `<src><\|wait\|></src>` | 1539 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>所面临的一些压力啊</src>` | 1915 |
| 9 | `<src>也不可能是</src>` | `<src>跟风景</src>` | 1064 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是</src>` | 1909 |
| 11 | `<src><\|wait\|></src>` | `<src>一夕之间就</src>` | 1484 |
| 12 | `<src>演变出来的，</src>` | `<src>眼便出来</src>` | 2687 |
| 13 | `<src>因此会建议</src>` | `<src>的，因此会建议</src>` | 1116 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1275 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1834 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 781 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1338 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1568 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1257 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 962 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1639 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1856 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 2084 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2255 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 2354 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 667 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1509 |
| 14 | `<src>的意思哦。</src>` | `<src>的意事哦。</src>` | 1191 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1905 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 799 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1069 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1861 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 720 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1600 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 1532 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 1826 |
| 9 | `<src>one another place </src>` | `<src>this is just one another place </src>` | 500 |
| 10 | `<src>to look at. </src>` | `<src>where you </src>` | 2392 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 1515 |
| 12 | `<src><\|wait\|></src>` | `<src>could develop </src>` | 2418 |
| 13 | `<src>developers or engineers </src>` | `<src><\|wait\|></src>` | 588 |
| 14 | `<src>working on BugRepo </src>` | `<src>operators, and engineers working on BugRepo </src>` | 1783 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1350 |

---

### Test Example 36 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1718 |
| 2 | `<src>HTML이라고 </src>` | `<src><\|wait\|></src>` | 760 |
| 3 | `<src><\|wait\|></src>` | `<src>HTML 이라고 하는 </src>` | 1002 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴퓨터 도 이해 할 수 </src>` | 2026 |
| 5 | `<src><\|wait\|></src>` | `<src>있고 </src>` | 861 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 이해 할 수 </src>` | 1440 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1549 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 1871 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1056 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 2308 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1184 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 2618 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 1069 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 1077 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1220 |

---

### Test Example 37 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2026 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ</src>` | 821 |
| 3 | `<src>俺は</src>` | `<src><\|wait\|></src>` | 1096 |
| 4 | `<src><\|wait\|></src>` | `<src>俺は</src>` | 1806 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>奇跡を見てる</src>` | 369 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1889 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1597 |
| 8 | `<src><\|wait\|></src>` | `<src>遠い超えている</src>` | 1583 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不二の奇跡</src>` | 498 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1248 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 2072 |
| 12 | `<src>船大工をやってる</src>` | `<src>中野大工をやってる</src>` | 1433 |
| 13 | `<src>が、</src>` | `<src><\|wait\|></src>` | 2283 |
| 14 | `<src>俺は</src>` | `<src>が俺はこんなにすごい</src>` | 1436 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>階族線を見た</src>` | 1101 |
| 16 | `<src>見たことがない。</src>` | `<src>ことがない。</src>` | 873 |

---

### Test Example 38 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2024 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 809 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1479 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1480 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 1879 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 467 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1539 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 1982 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 1317 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2635 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 2185 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 939 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1407 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1283 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 825 |

---

### Test Example 39 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2176 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 845 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>색모를 빌 거야. </src>` | 2457 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 </src>` | 546 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>소름 이 돋는 차림 도 </src>` | 2070 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>뜯는데 기분 이 </src>` | 1595 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>엄이야. 이걸 </src>` | 1474 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>한들 어서 같이 놀자는 거야. </src>` | 707 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1319 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 2401 |
| 11 | `<src>신이 오면 </src>` | `<src>새니 오면 </src>` | 1782 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1511 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1478 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1196 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 872 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1787 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니 모아 </src>` | 939 |
| 3 | `<src>이방인으로 </src>` | `<src>너희 가 이방인으로 </src>` | 2491 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 537 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1979 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1554 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그는 그대로 </src>` | 1215 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 960 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2345 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1789 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 2430 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 569 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1534 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1185 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 878 |

---

### Test Example 41 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1938 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 852 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 2173 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正财的部分</src>` | 872 |
| 5 | `<src>也就是</src>` | `<src><\|wait\|></src>` | 1936 |
| 6 | `<src>在事业方面的</src>` | `<src>也就是在事业方面的</src>` | 1362 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 504 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1804 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1465 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 2568 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1867 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1307 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对于正财来说就</src>` | 1660 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1200 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1072 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2053 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 768 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1019 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1940 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 497 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1774 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아 </src>` | 1584 |
| 8 | `<src>그러니까 </src>` | `<src>그려니까 </src>` | 1355 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 649 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 가능 도는 </src>` | 2466 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 1771 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 2354 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 623 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 것을 </src>` | 1682 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1182 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1145 |

---

### Test Example 43 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who just </src>` | 2096 |
| 2 | `<src>just getting going </src>` | `<src>getting going </src>` | 763 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 1186 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1729 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1011 |
| 6 | `<src>that I think are </src>` | `<src>that are really </src>` | 1269 |
| 7 | `<src>really important. </src>` | `<src>important. </src>` | 1539 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1932 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into </src>` | 2410 |
| 10 | `<src>I have about </src>` | `<src>I have about one </src>` | 1897 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 2214 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 784 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1658 |
| 14 | `<src>that cover each one </src>` | `<src>that cover each one </src>` | 1182 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, </src>` | 1275 |

---

### Test Example 44 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>図</src>` | 1928 |
| 2 | `<src>十一二手とか</src>` | `<src>1、2、とか</src>` | 868 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>ですね。おそらく</src>` | 1352 |
| 4 | `<src>十秒で。</src>` | `<src>10秒で。</src>` | 1597 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 886 |
| 6 | `<src>一秒に</src>` | `<src>1秒に</src>` | 1329 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>1秒ぐらいの</src>` | 1571 |
| 8 | `<src>計算ですか</src>` | `<src>設定なのか</src>` | 1902 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 1771 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2368 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1867 |
| 12 | `<src><\|wait\|></src>` | `<src>1、2、</src>` | 1278 |
| 13 | `<src>十一二手で</src>` | `<src>2で</src>` | 1453 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1110 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 914 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 775 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2044 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 885 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 2153 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 709 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1866 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 464 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 1640 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 1891 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 2450 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1678 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 2460 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 605 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1578 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1285 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 954 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 352 |

---

### Test Example 46 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2146 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 913 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1367 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1485 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>할 것, 거러 거러 다 </src>` | 1553 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>이용 하기가 하면 </src>` | 737 |
| 7 | `<src>강북 을 가면 </src>` | `<src>막고 들어감 </src>` | 1669 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 </src>` | 1835 |
| 9 | `<src><\|wait\|></src>` | `<src>나가 는 것도 </src>` | 1258 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장렬이에요. </src>` | 2197 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 창피 하네요. </src>` | 1854 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1867 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1516 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>못하 고 말아요. </src>` | 1267 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 1080 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 423 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1940 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 831 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 2372 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 782 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 1912 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1355 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 499 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1926 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1334 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 2207 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1877 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1678 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1678 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1151 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 967 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 467 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1707 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 938 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 2268 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 765 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1985 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1533 |
| 7 | `<src>26비트 FP </src>` | `<src>268F </src>` | 1215 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 879 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트 로 </src>` | 1411 |
| 10 | `<src>것으로 보인다. </src>` | `<src>나충수가로 보인다. </src>` | 2521 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1701 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1518 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1678 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1222 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 1265 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 402 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2042 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 883 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1371 |
| 4 | `<src>真实意图的，</src>` | `<src>真实力土的，</src>` | 1584 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1779 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 386 |
| 7 | `<src>很多时候经常</src>` | `<src>好经常</src>` | 1540 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们这样说：</src>` | 1927 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1262 |
| 10 | `<src>你们看，</src>` | `<src>你看，</src>` | 1955 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1189 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 2742 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 824 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1136 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1205 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 1076 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 645 |

---

### Test Example 50 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1919 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 770 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 2588 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 570 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1934 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 1549 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 713 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 1411 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 2179 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1950 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 2411 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 704 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1614 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1327 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 1146 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 627 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 뭐 </src>` | 2041 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 이런 경우 들도 </src>` | 940 |
| 3 | `<src>있습니다. </src>` | `<src>있습니다. </src>` | 1362 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 1672 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 서로 </src>` | 2002 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>컨설턴트예요, 뭐 </src>` | 1621 |
| 7 | `<src><\|wait\|></src>` | `<src>B가 컨설턴트여야 </src>` | 1847 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>되고 A라는 </src>` | 685 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 2277 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1579 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>뿌렸 을 때 </src>` | 2656 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 855 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1121 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스쿠티에서 </src>` | 1358 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일 까지 </src>` | 981 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 642 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 1796 |
| 2 | `<src>首次觉知到</src>` | `<src>首次觉知到</src>` | 813 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象：</src>` | 1428 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1471 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 1094 |
| 6 | `<src>处于爱之中，</src>` | `<src>爱之中，</src>` | 1196 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 1549 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1871 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨。</src>` | 2931 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1481 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 2567 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 354 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1450 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1243 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 832 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆</src>` | 698 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 622 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 562 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1990 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 794 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 2277 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 764 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1677 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 547 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1559 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1842 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1162 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2181 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1257 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2644 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1532 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1243 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 797 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 831 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 532 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 584 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2233 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 732 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 1222 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1739 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 750 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1515 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 1567 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 1547 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 461 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 1084 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2663 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1654 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree upon </src>` | 1815 |
| 14 | `<src>upon the fields that need </src>` | `<src>the fields that need </src>` | 1333 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1172 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 890 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 779 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 734 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 544 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1787 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 766 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1350 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1581 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 2117 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1168 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 747 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1821 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 1711 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 2664 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2656 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1060 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1052 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 1324 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 919 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 651 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 561 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone. </src>` | 370 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2179 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 808 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 1070 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1851 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 680 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't know </src>` | 1705 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1647 |
| 8 | `<src><\|wait\|></src>` | `<src>the the van </src>` | 1780 |
| 9 | `<src>the the vanguard of social </src>` | `<src><\|wait\|></src>` | 1100 |
| 10 | `<src>change </src>` | `<src>ard of social change. </src>` | 2292 |
| 11 | `<src>these days, </src>` | `<src>These days, </src>` | 1050 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2636 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 872 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1200 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1272 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 1032 |
| 17 | `<src><\|wait\|></src>` | `<src>So, </src>` | 639 |
| 18 | `<src>So you have some </src>` | `<src>you have some </src>` | 517 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 370 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 342 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 202 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1937 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 860 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1418 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1680 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1941 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1237 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 599 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1783 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 1238 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 2170 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1215 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 2585 |
| 13 | `<src>也会反映的是</src>` | `<src>它反映的是</src>` | 1460 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1100 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间，</src>` | 903 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的做</src>` | 810 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>一下洗去，</src>` | 650 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 605 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛。</src>` | 331 |
| 20 | `<src>啊，</src>` | `<src><\|wait\|></src>` | 333 |
| 21 | `<src>所以是说。</src>` | `<src>好所以是说。</src>` | 319 |

---

### Test Example 58 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1884 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 876 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 2257 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 782 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1952 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1555 |
| 7 | `<src>제법 생색까지 </src>` | `<src><\|wait\|></src>` | 1088 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>제법 생색까지 냈지만 이제 는 </src>` | 1256 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2600 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1481 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 2689 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 508 |
| 13 | `<src><\|wait\|></src>` | `<src>드러내 놓고 윤석열 </src>` | 1486 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>후보 를 떨어뜨리 겠다는 </src>` | 1349 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 1002 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 683 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 487 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 283 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 227 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 288 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건 </src>` | 357 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 228 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 280 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 316 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까? </src>` | 304 |

---

### Test Example 59 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1805 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 816 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1442 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1475 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1150 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1166 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1585 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1856 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1056 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 2029 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1376 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 2674 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1080 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1291 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 1048 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 888 |
| 17 | `<src>get straight to the point. </src>` | `<src>get straight to the point. </src>` | 716 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 572 |
| 19 | `<src>play </src>` | `<src>play </src>` | 303 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 435 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 260 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 283 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 244 |
| 24 | `<src><\|wait\|></src>` | `<src>ENTP stands for </src>` | 302 |
| 25 | `<src>ENTP stands for </src>` | `<src>Extraverted, Intuitive,</src>` | 334 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1997 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 761 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 987 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいですなのでここのね</src>` | 1987 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 393 |
| 6 | `<src>も</src>` | `<src>も</src>` | 1831 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1574 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 1207 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 891 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 1586 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 2580 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 2252 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね</src>` | 779 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1671 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 1362 |
| 16 | `<src><\|wait\|></src>` | `<src>なとはい</src>` | 1089 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思いますここ</src>` | 626 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね釜山</src>` | 200 |
| 19 | `<src>駅ももう</src>` | `<src>駅ももう</src>` | 496 |
| 20 | `<src><\|wait\|></src>` | `<src>歩いて</src>` | 331 |
| 21 | `<src>歩いて一分</src>` | `<src>一分かかる</src>` | 338 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかんないかな</src>` | 313 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 275 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>リッチのねまあホテル</src>` | 300 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 292 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 276 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 183 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 133 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではですね今回は。</src>` | 145 |
