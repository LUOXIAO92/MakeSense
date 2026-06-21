# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9944
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.9338
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
  - PROCESS_TIME_MS_AVG: 1346.3370
  - PROCESS_TIME_MS_P50: 1400.8800
  - PROCESS_TIME_MS_P95: 1974.4360
  - PROCESS_TIME_MS_MAX: 2539.9490

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1795 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要气熟是容易的，</src>` | 1538 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 1279 |
| 4 | `<src>只有一个师父</src>` | `<src>只有一个师父</src>` | 980 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 433 |
| 6 | `<src>知道如何</src>` | `<src>知道如何</src>` | 1341 |
| 7 | `<src>处于中间，</src>` | `<src>处于中间，</src>` | 2121 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 430 |
| 9 | `<src>虚阿凡</src>` | `<src>虚阿凡</src>` | 1314 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 1564 |
| 11 | `<src>一个师父。</src>` | `<src>一个师父。</src>` | 1928 |

---

### Test Example 2 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1582 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1383 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 363 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1198 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 1140 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1400 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 918 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1701 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 1469 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 1531 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1922 |

---

### Test Example 3 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 1847 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 1388 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 289 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1190 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 1166 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1259 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 366 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 1228 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1346 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1425 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 1726 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1696 |

---

### Test Example 4 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1690 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1441 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1229 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 457 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1085 |
| 6 | `<src>research, </src>` | `<src>research, </src>` | 1360 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 2009 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 578 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 1401 |
| 10 | `<src>out there, </src>` | `<src>out there, </src>` | 1674 |
| 11 | `<src>people that we can learn from. </src>` | `<src>people that we can learn from. </src>` | 1888 |

---

### Test Example 5 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 1990 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>학생 들은 </src>` | 1393 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 1343 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 않았고 </src>` | 1207 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1064 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 596 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>학생 들이 </src>` | 2035 |
| 8 | `<src>때문 입니다. </src>` | `<src>었기 때문 입니다. </src>` | 540 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1777 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모를 랐던 </src>` | 1977 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1824 |

---

### Test Example 6 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1933 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1420 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 915 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 724 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 1191 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1385 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2354 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 280 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 2138 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1719 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 1779 |

---

### Test Example 7 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 1790 |
| 2 | `<src><\|wait\|></src>` | `<src>의지 를 </src>` | 1409 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>내일 수 있지만 </src>` | 1356 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 655 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기가 </src>` | 800 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꾸밀 필요 가 </src>` | 1422 |
| 7 | `<src>뭐 있고 </src>` | `<src>뭐 있고 </src>` | 1738 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>남한 테 보살 로 보일 필요 가 </src>` | 874 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>뭐 있어요. 우주 가 </src>` | 2172 |
| 10 | `<src>지금 나한테 </src>` | `<src>지금 나한테 </src>` | 1836 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는데. </src>` | 1656 |

---

### Test Example 8 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1911 |
| 2 | `<src>家长需要做的是，</src>` | `<src>家长需要做的是，</src>` | 1505 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1345 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1187 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水、</src>` | 1385 |
| 6 | `<src>施肥，</src>` | `<src>施肥，</src>` | 642 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1966 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心理营养，</src>` | 890 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1575 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>并耐心等待孩子</src>` | 1896 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 1548 |

---

### Test Example 9 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1997 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>挖一点松子儿里</src>` | 1530 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>边，这个油性也很大。</src>` | 1470 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1048 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1372 |
| 6 | `<src>呢，我再放一点</src>` | `<src>呢，我再放一点</src>` | 739 |
| 7 | `<src>儿核桃</src>` | `<src>儿核桃</src>` | 1879 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 925 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>仁儿，仁儿里边</src>` | 1748 |
| 10 | `<src>这种核桃</src>` | `<src>这种核桃</src>` | 1951 |
| 11 | `<src>仁儿。</src>` | `<src>仁儿。</src>` | 1369 |

---

### Test Example 10 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1717 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1531 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 1302 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1201 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方，</src>` | 1389 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有这个状况，</src>` | 920 |
| 7 | `<src>不要想自己</src>` | `<src>不要想自己</src>` | 1715 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 1166 |
| 9 | `<src>独立承担。</src>` | `<src>独立承担。</src>` | 1561 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 1929 |
| 11 | `<src>事业运就属凶。</src>` | `<src>事业运就属凶。</src>` | 1501 |

---

### Test Example 11 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1627 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1358 |
| 3 | `<src>Drop into </src>` | `<src>Drop into </src>` | 571 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 919 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 1180 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1513 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 2444 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1114 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them what </src>` | 1668 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1938 |
| 11 | `<src>language are you using? </src>` | `<src>language are you using? </src>` | 1653 |

---

### Test Example 12 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2010 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 1374 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じ、</src>` | 1015 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>オシャレる方がやっぱ</src>` | 635 |
| 5 | `<src>多いですね。</src>` | `<src>多いですね。</src>` | 1044 |
| 6 | `<src>開業したい方って</src>` | `<src>開業したい方って</src>` | 1418 |
| 7 | `<src>すごい</src>` | `<src>すごい</src>` | 906 |
| 8 | `<src>自己意識高いし、</src>` | `<src>自己意識高いし、</src>` | 1692 |
| 9 | `<src>自分で</src>` | `<src>自分で</src>` | 1294 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>全部ちょっと次の投資</src>` | 1581 |
| 11 | `<src>傾向が強いので、</src>` | `<src>傾向が強いので、</src>` | 1897 |
| 12 | `<src>なので。</src>` | `<src>なので。</src>` | 1529 |

---

### Test Example 13 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1744 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>아이 엠 애플 을 </src>` | 1458 |
| 3 | `<src>촉발 시키고 </src>` | `<src>촉발 시키고 </src>` | 1429 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1166 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1395 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 896 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>부모 를 죽인 페르 나 </src>` | 1798 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1615 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1817 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1509 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>같은 세대 들입니다. </src>` | 1906 |

---

### Test Example 14 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1689 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>Like a stretched rubber band, </src>` | 1518 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 1295 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy, </src>` | 1150 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>and when those bonds are broken, </src>` | 1191 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 432 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 974 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, </src>` | 1617 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light, </src>` | 1468 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1714 |
| 11 | `<src>or gets used to make </src>` | `<src>or gets used to make </src>` | 1742 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 2065 |

---

### Test Example 15 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아 저는 </src>` | 1788 |
| 2 | `<src>옹심이, </src>` | `<src>옹심이, </src>` | 1451 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1421 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 옹심이, 쌀국수하고 </src>` | 1377 |
| 5 | `<src>옹심이가 </src>` | `<src>옹심이가 </src>` | 1372 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2201 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞여 있는 건데요. </src>` | 458 |
| 8 | `<src>야, </src>` | `<src>야, </src>` | 1673 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1792 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해장으로도 조금 죽입니다, </src>` | 1724 |
| 11 | `<src>진짜. </src>` | `<src>진짜. </src>` | 1778 |

---

### Test Example 16 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1857 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1507 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1391 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1322 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1287 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1853 |
| 7 | `<src>相对的低</src>` | `<src>相对的低</src>` | 804 |
| 8 | `<src>能量的运行</src>` | `<src>能量的运行</src>` | 2092 |
| 9 | `<src>状态，</src>` | `<src>状态，</src>` | 1664 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1710 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1719 |

---

### Test Example 17 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1546 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1251 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 356 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1353 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 1312 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1408 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1867 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给他吃。真的，</src>` | 742 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1690 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，只有这么一个</src>` | 2013 |
| 11 | `<src>小小的愿望</src>` | `<src>小小的愿望</src>` | 1852 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 1575 |

---

### Test Example 18 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1758 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 죽여 달라 </src>` | 1543 |
| 3 | `<src>해가지고 내가 </src>` | `<src>해가지고 내가 </src>` | 1358 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수다. </src>` | 1397 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1279 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 994 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해지 않았느냐? 내가 </src>` | 1658 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 1767 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1778 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>있는 줄 알았느냐? 응? </src>` | 1929 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 1700 |

---

### Test Example 19 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1661 |
| 2 | `<src>映画でですね、</src>` | `<src>映画でですね、</src>` | 1239 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 369 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>映画生息かどうかっていうのを</src>` | 1493 |
| 5 | `<src>調べるときに、</src>` | `<src>調べるときに、</src>` | 1182 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあ映画の卵を調べる</src>` | 1411 |
| 7 | `<src>ことで、あの</src>` | `<src>ことで、あの</src>` | 1517 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>その生息かどうかっていうのを</src>` | 1078 |
| 9 | `<src>保証する、生息である</src>` | `<src>保証する、生息である</src>` | 2094 |
| 10 | `<src>ことを保証する</src>` | `<src>ことを保証する</src>` | 1769 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1683 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 1769 |

---

### Test Example 20 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 1934 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 1354 |
| 3 | `<src>いただもらえる</src>` | `<src>いただもらえる</src>` | 389 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも</src>` | 1157 |
| 5 | `<src>用意しておりますので</src>` | `<src>用意しておりますので</src>` | 1196 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ぜひご参加ください。</src>` | 1461 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 2437 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 824 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 1474 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1737 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので</src>` | 1751 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1914 |

---

### Test Example 21 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right, </src>` | 1990 |
| 2 | `<src>and then </src>` | `<src>and then </src>` | 1380 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 829 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 685 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1152 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1443 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 910 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1621 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 997 |
| 10 | `<src>these values. So </src>` | `<src>these values. So </src>` | 1594 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1834 |
| 12 | `<src>this game dot scored array. </src>` | `<src>this game dot scored array. </src>` | 1556 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1767 |

---

### Test Example 22 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1754 |
| 2 | `<src>一切正常，</src>` | `<src>一切正常，</src>` | 1428 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>活蹦乱跳，</src>` | 966 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 554 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 1173 |
| 6 | `<src>期间</src>` | `<src>期间</src>` | 1363 |
| 7 | `<src>大概有十位医生</src>` | `<src>大概有十位医生</src>` | 955 |
| 8 | `<src>来诊断，</src>` | `<src>来诊断，</src>` | 1663 |
| 9 | `<src>一下敲腿，</src>` | `<src>一下敲腿，</src>` | 1163 |
| 10 | `<src>一下提腿，</src>` | `<src>一下提腿，</src>` | 1740 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1833 |
| 12 | `<src>他们</src>` | `<src>他们</src>` | 1581 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>都很疑惑的离开。</src>` | 1628 |

---

### Test Example 23 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1647 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1444 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1393 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1209 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1399 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 849 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1757 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 1358 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1562 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1832 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1666 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 1564 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 1929 |
| 2 | `<src>です。</src>` | `<src>です。</src>` | 1243 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 334 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1368 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1150 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>上げ下げできなくなってしまうので、</src>` | 1507 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 981 |
| 8 | `<src>役ねじの</src>` | `<src>役ねじの</src>` | 1566 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1399 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうことです</src>` | 1555 |
| 11 | `<src>ね。</src>` | `<src>ね。</src>` | 1816 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1589 |
| 13 | `<src>分解完了。</src>` | `<src>分解完了。</src>` | 1607 |

---

### Test Example 25 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1688 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 1247 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 360 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1372 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 1118 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1374 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 550 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2140 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1340 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 1580 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1957 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 1578 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1535 |

---

### Test Example 26 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1751 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1403 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二级市场，哎，</src>` | 1414 |
| 4 | `<src>服务</src>` | `<src>服务</src>` | 1065 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 316 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们，</src>` | 1406 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，呃，</src>` | 1183 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1384 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做微信公众号十几年，你会</src>` | 1871 |
| 10 | `<src>发现</src>` | `<src>发现</src>` | 1716 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给微信公众号评分</src>` | 1685 |
| 12 | `<src>的新榜反而</src>` | `<src>的新榜反而</src>` | 1818 |
| 13 | `<src>火了。</src>` | `<src>火了。</src>` | 1272 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 1806 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 1389 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 1350 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 654 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 822 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 1391 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1945 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 667 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1503 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 1870 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1612 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 2189 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1208 |

---

### Test Example 28 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1758 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kerenath Dettig. </src>` | 1536 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 1355 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1193 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 1501 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 2207 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 410 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 1944 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1717 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 1957 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1769 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1219 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1735 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 거진 </src>` | 1523 |
| 3 | `<src>인슐린과 </src>` | `<src>인슐린과 </src>` | 1336 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 거진 </src>` | 1194 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>유사 한 작용 이 </src>` | 1530 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>일어날 정도 로 </src>` | 1177 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1375 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당뇨 미네랄이다 </src>` | 1490 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 1509 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 1891 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 1819 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1583 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1124 |

---

### Test Example 30 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1657 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1514 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>10명 미만 으로 </src>` | 1458 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1250 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1331 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1090 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 1557 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 1634 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 1751 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1612 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 폐업 도 </src>` | 2086 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>하지 않는 현상 들을 </src>` | 1378 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>보이 게 된 거죠. </src>` | 1220 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1835 |
| 2 | `<src>要提醒大家，</src>` | `<src>要提醒大家，</src>` | 1458 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢</src>` | 972 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是一天造成的，</src>` | 630 |
| 5 | `<src>所以呢，</src>` | `<src>所以呢，</src>` | 1216 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1275 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 971 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊，跟风险</src>` | 1682 |
| 9 | `<src>也不可能是</src>` | `<src>也不可能是</src>` | 2049 |
| 10 | `<src>一夕之间就</src>` | `<src>一夕之间就</src>` | 1790 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1758 |
| 12 | `<src>演变出来的，</src>` | `<src>演变出来的，</src>` | 1756 |
| 13 | `<src>因此会建议</src>` | `<src>因此会建议</src>` | 1259 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢。</src>` | 1106 |

---

### Test Example 32 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1962 |
| 2 | `<src>The meaning of </src>` | `<src>The meaning of </src>` | 1411 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment, </src>` | 1506 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1311 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1368 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 2390 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 761 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1567 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1807 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1716 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1692 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 1420 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 1483 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 1699 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 1373 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 952 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 640 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1203 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1319 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 2540 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1057 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1649 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 1971 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1674 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 1676 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1043 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1608 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1597 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1506 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 1316 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1171 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 1063 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 564 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 2441 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 1369 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1577 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 1926 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1650 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1643 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1008 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1547 |

---

### Test Example 35 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1840 |
| 2 | `<src>十一二手とか</src>` | `<src>十一二手とか</src>` | 1405 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>じゃないですか。おそらく</src>` | 1199 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 443 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1016 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1371 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 894 |
| 8 | `<src>計算ですか</src>` | `<src>計算ですか</src>` | 1696 |
| 9 | `<src>ね。</src>` | `<src>ね。</src>` | 852 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1547 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1698 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1689 |
| 13 | `<src>十一二手で</src>` | `<src>十一二手で</src>` | 1785 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1155 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1130 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 920 |

---

### Test Example 36 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 1985 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1438 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>선생 이 뭐라 빌 거야. </src>` | 1334 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>니한테 소름 이 돋든 </src>` | 1015 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>닭살이 돋든 </src>` | 443 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 오면 </src>` | 1374 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 1144 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 1465 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 1525 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1726 |
| 11 | `<src>신이 오면 </src>` | `<src>신이 오면 </src>` | 1655 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1861 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거니 까 </src>` | 1566 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1154 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감아. </src>` | 1134 |

---

### Test Example 37 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1590 |
| 2 | `<src>HTML이라고 </src>` | `<src>HTML이라고 </src>` | 1225 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 373 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>하는 컴퓨터 도 이해 할 수 </src>` | 1381 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1171 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>있고 사람 도 이해 할 수 </src>` | 1506 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1113 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 언어 의 </src>` | 1504 |
| 9 | `<src>문법 에 </src>` | `<src>문법 에 </src>` | 1509 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>맞게 우리 가 이제 </src>` | 1860 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 1531 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1758 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 작성 하는 </src>` | 1657 |
| 14 | `<src>프로그램 이 </src>` | `<src>프로그램 이 </src>` | 1154 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 1140 |

---

### Test Example 38 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1783 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 1389 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1010 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 630 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1158 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1349 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 2466 |
| 8 | `<src>this is just </src>` | `<src>this is just </src>` | 1284 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1673 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 1938 |
| 11 | `<src>But </src>` | `<src>But </src>` | 1561 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1620 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 989 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1691 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 595 |

---

### Test Example 39 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 1933 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1383 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 1424 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1163 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 1413 |
| 6 | `<src>that I think are </src>` | `<src>that I think are </src>` | 542 |
| 7 | `<src>really important. </src>` | `<src>really important. </src>` | 2085 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1021 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go into. </src>` | 1738 |
| 10 | `<src>I have about </src>` | `<src>I have about </src>` | 1938 |
| 11 | `<src>one minute videos </src>` | `<src>one minute videos </src>` | 1540 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 1720 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1052 |
| 14 | `<src>that cover each one </src>` | `<src>that cover each one </src>` | 1708 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>in a little more detail, but. </src>` | 625 |

---

### Test Example 40 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1886 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 1420 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 1182 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 439 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>actually go in your education? Did you </src>` | 1250 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1323 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2368 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>That's one level of attainment. Did you go </src>` | 1072 |
| 9 | `<src>to college, </src>` | `<src>to college, </src>` | 1557 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>and if so, did you graduate? </src>` | 2122 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level of </src>` | 1669 |
| 12 | `<src>attainment. </src>` | `<src>attainment. </src>` | 1601 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it for </src>` | 1136 |
| 14 | `<src>now. I'll see you </src>` | `<src>now. I'll see you </src>` | 1660 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 790 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 1867 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 1407 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 360 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1162 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今奇跡を見てる。</src>` | 1354 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1314 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 999 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1541 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えてる船の奇跡よ。</src>` | 1466 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1526 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1914 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 1715 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 1576 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 936 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい海賊船を</src>` | 1620 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 775 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 1890 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어떻게 보면 </src>` | 1254 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 482 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1205 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>함께 한 동생 이자 </src>` | 1364 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1307 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아 </src>` | 1941 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 688 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 10 | `<src>책임감 보다는 </src>` | `<src>책임감 보다는 </src>` | 1860 |
| 11 | `<src>조금 </src>` | `<src>조금 </src>` | 1669 |
| 12 | `<src>자기 스스로 </src>` | `<src>자기 스스로 </src>` | 1622 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1231 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것을 </src>` | 1150 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1117 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 895 |

---

### Test Example 43 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1666 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1547 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 1355 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1188 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1426 |
| 6 | `<src>우상에게로 </src>` | `<src>우상에게로 </src>` | 1007 |
| 7 | `<src>끄는 그대로 </src>` | `<src>끄는 그대로 </src>` | 1576 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>끌려 갔느니라. </src>` | 1459 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1586 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 1883 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1626 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1589 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1124 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1466 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 930 |

---

### Test Example 44 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1777 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1457 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 1391 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏向正财的部分，</src>` | 1355 |
| 5 | `<src>也就是</src>` | `<src>也就是</src>` | 1291 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 2266 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利</src>` | 454 |
| 8 | `<src>与收入的</src>` | `<src>与收入的</src>` | 1811 |
| 9 | `<src>提升。如果是在</src>` | `<src>提升。如果是在</src>` | 1815 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>投资理财方面呢，</src>` | 1825 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 1707 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错，只是</src>` | 1285 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对正财来说就</src>` | 1207 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>稍微弱了那么一点。</src>` | 1039 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1245 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 1879 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1466 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて</src>` | 1387 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1223 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 1445 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのもフローリフを</src>` | 1103 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>ビジュアルに書いた後、</src>` | 1569 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいさつはPythonコード</src>` | 1708 |
| 9 | `<src>にそこから</src>` | `<src>にそこから</src>` | 1691 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 1618 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1960 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 1360 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 1154 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1091 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 647 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ。</src>` | 796 |

---

### Test Example 46 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 이제 </src>` | 1772 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1386 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>상승 하는 흐름 을 보인다 면 </src>` | 1413 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형주 도 </src>` | 1199 |
| 5 | `<src>큰 폭의 </src>` | `<src>큰 폭의 </src>` | 1374 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>상승 을 하겠지만 </src>` | 674 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1923 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 874 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1583 |
| 10 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1817 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>시장 을 주도 하면서 </src>` | 1636 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이 기 때문 에 항상 </src>` | 1921 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 1210 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1690 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 될 것 </src>` | 506 |
| 16 | `<src>같습니다. </src>` | `<src>같습니다. </src>` | 1000 |

---

### Test Example 47 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1863 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1488 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 1357 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1209 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1366 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 828 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 1796 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们</src>` | 1078 |
| 9 | `<src>这样说：“</src>` | `<src>这样说：“</src>` | 1562 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1853 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 1380 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1859 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1187 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。”</src>` | 1625 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 337 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说。</src>` | 822 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 628 |

---

### Test Example 48 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1608 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 분석 을 </src>` | 1530 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>내놓 았습니다. </src>` | 1366 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1179 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1407 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 893 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 1712 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 1322 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 낮춘 </src>` | 1690 |
| 10 | `<src>것으로 보인다. </src>` | `<src>것으로 보인다. </src>` | 1939 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1661 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 1661 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1064 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>인피니트 캐시 </src>` | 1405 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>L3가 여기 도 없다. </src>` | 918 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 623 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1791 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 1411 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1402 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1183 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 953 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 631 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 2449 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 1200 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 1647 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 1850 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 1494 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1720 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1159 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1692 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 688 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 921 |

---

### Test Example 50 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어가 면 </src>` | 1953 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1546 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 1315 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1207 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>하건 걸어 걸어다니 </src>` | 1467 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>공간 에 뭐 </src>` | 1192 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 을 가면 </src>` | 1473 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 외국 에 나가 면 </src>` | 1747 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1809 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>또 장렬이에요. </src>` | 1701 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>좀 창피 하네요. </src>` | 1953 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 </src>` | 1192 |
| 13 | `<src>이제 </src>` | `<src>이제 </src>` | 1119 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>열심히 물어봐요. </src>` | 1241 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>그거 는 다인 것 같아요. </src>` | 1298 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 629 |

---

### Test Example 51 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>그래서 뭐 </src>` | 1879 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>물론 이제 이런 경우 들도 </src>` | 1561 |
| 3 | `<src>있습니다. </src>` | `<src>있습니다. </src>` | 1312 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>저희 가 A라는 사람 과 </src>` | 1260 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 서로 </src>` | 1438 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>컨설턴트예요, </src>` | 2467 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 818 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>모이 킹 컨설턴트여가지고 </src>` | 1880 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>A라는 사람 이 </src>` | 1950 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 1501 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>뿌렸 을 때 </src>` | 1692 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1196 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1680 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스쿠티에서 </src>` | 457 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일 까지 </src>` | 1046 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 644 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>弗洛伊德</src>` | 1675 |
| 2 | `<src>首次觉知到</src>` | `<src>首次觉知到</src>` | 1401 |
| 3 | `<src>那个现象：</src>` | `<src>那个现象：</src>` | 1361 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1085 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 340 |
| 6 | `<src>处于爱之中，</src>` | `<src><\|wait\|></src>` | 1330 |
| 7 | `<src>所谓的爱，</src>` | `<src>爱之中，所有</src>` | 1157 |
| 8 | `<src>我们也</src>` | `<src>的爱，我们</src>` | 1455 |
| 9 | `<src>同时进入恨。</src>` | `<src>也同时进入恨。</src>` | 1437 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1652 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上的时候，</src>` | 1792 |
| 12 | `<src>它是爱；</src>` | `<src>它是爱；</src>` | 1696 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 1625 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成恨。</src>` | 1211 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1211 |
| 16 | `<src>那个钟摆</src>` | `<src>那个钟摆</src>` | 809 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 754 |
| 18 | `<src>继续在移动。</src>` | `<src>继续在移动。</src>` | 539 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Um, </src>` | 1798 |
| 2 | `<src>Also, </src>` | `<src>also, </src>` | 1388 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 477 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1050 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1209 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1431 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1262 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1375 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1377 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 1525 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1974 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 1759 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1733 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1180 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1094 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 817 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 753 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 536 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1667 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 1383 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 1406 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1190 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 1412 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 821 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>been in the wilderness forty days, that he's hungry. </src>` | 1994 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 2081 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, </src>` | 1959 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it. </src>` | 1826 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1667 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>Turn these stones to bread." </src>` | 1203 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1607 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>How did Jesus deal with that </src>` | 347 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 881 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 542 |
| 17 | `<src>Man shall not live </src>` | `<src>Man shall not live </src>` | 560 |
| 18 | `<src>by bread alone. </src>` | `<src>by bread alone. </src>` | 425 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2055 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1364 |
| 3 | `<src>in the first section </src>` | `<src>in the first section </src>` | 931 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 669 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR fields </src>` | 1267 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1246 |
| 7 | `<src>being of critical importance </src>` | `<src>being of critical importance </src>` | 997 |
| 8 | `<src>versus variant </src>` | `<src>versus variant </src>` | 1552 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1066 |
| 10 | `<src>databases, </src>` | `<src>databases, </src>` | 1551 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 2123 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1612 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>Is that if we don't agree </src>` | 1796 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields that need </src>` | 951 |
| 15 | `<src>to be in these </src>` | `<src>to be in these </src>` | 1625 |
| 16 | `<src>data sources that we can </src>` | `<src>data sources that we can </src>` | 683 |
| 17 | `<src>draw from, </src>` | `<src>draw from, </src>` | 828 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 659 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 442 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1807 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1429 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1076 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 568 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1150 |
| 6 | `<src>的部分。</src>` | `<src>的部分。</src>` | 1274 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 909 |
| 8 | `<src>都是属于</src>` | `<src>都是属于</src>` | 1641 |
| 9 | `<src>我们</src>` | `<src>我们</src>` | 856 |
| 10 | `<src>在休息的地方，</src>` | `<src>在休息的地方，</src>` | 1645 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1819 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>所以呢，这身体的部分</src>` | 1570 |
| 13 | `<src>也会反映的是</src>` | `<src>也会反映的是</src>` | 1755 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1268 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间，</src>` | 1377 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 589 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息。可是</src>` | 1236 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>我们可以看到这边是</src>` | 349 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的嘛，</src>` | 433 |
| 20 | `<src>啊，</src>` | `<src>啊，</src>` | 406 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 347 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2022 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 1419 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 895 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 674 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 1064 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. </src>` | 1418 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>And I don't think the courts want to be </src>` | 1189 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1433 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of social </src>` | 1450 |
| 10 | `<src>change </src>` | `<src>change </src>` | 1545 |
| 11 | `<src>these days, </src>` | `<src>these days, </src>` | 1913 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1624 |
| 13 | `<src>but they rather reflect </src>` | `<src>but they rather reflect </src>` | 1651 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1072 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1422 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 736 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 850 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 543 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 394 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 196 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 212 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1652 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1437 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 1401 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1145 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 470 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world. </src>` | 1188 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2396 |
| 8 | `<src>Their personality is </src>` | `<src>Their personality is </src>` | 1096 |
| 9 | `<src>something of a </src>` | `<src>something of a </src>` | 1499 |
| 10 | `<src>contradiction. </src>` | `<src>contradiction. </src>` | 1779 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1552 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1824 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1182 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 947 |
| 15 | `<src>and like to </src>` | `<src>and like to </src>` | 1018 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1244 |
| 17 | `<src>get straight to the point. </src>` | `<src>get straight to the point. </src>` | 502 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 273 |
| 19 | `<src>play </src>` | `<src>play </src>` | 396 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>the devil's advocate, and they </src>` | 389 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 233 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate. </src>` | 271 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 262 |
| 24 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 242 |
| 25 | `<src>ENTP stands for </src>` | `<src>ENTP stands for </src>` | 202 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 1741 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1487 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1370 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1187 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1493 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1299 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 1349 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 2045 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1819 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1718 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1783 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 1283 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1031 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | 1169 |
| 15 | `<src><\|wait\|></src>` | `<src>독기를 품은 </src>` | 1155 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 528 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 203 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src><\|wait\|></src>` | 424 |
| 19 | `<src>것입니다. </src>` | `<src>작정 한 것입니다. </src>` | 347 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 이준석의 </src>` | 263 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src><\|wait\|></src>` | 202 |
| 22 | `<src><\|wait\|></src>` | `<src>성상 낯큰 </src>` | 301 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 265 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 </src>` | 230 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>얼마나 큰 호재입니까? </src>` | 260 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 1839 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね</src>` | 1304 |
| 3 | `<src>今作ってる</src>` | `<src>今作ってる</src>` | 340 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>みたいですなのでここのね</src>` | 1411 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>ゴールドストーンホテル</src>` | 1251 |
| 6 | `<src>も</src>` | `<src>も</src>` | 1254 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 2072 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 592 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので</src>` | 1840 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ねここ</src>` | 1805 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ゴールドストーンホテルを</src>` | 1723 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたい</src>` | 1773 |
| 13 | `<src>なっていう方はですね</src>` | `<src>なっていう方はですね</src>` | 1308 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさってみて</src>` | 1167 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>もまあいいんじゃないか</src>` | 1126 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1144 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>なとはい思いますここ</src>` | 363 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>のホテルからですね釜山</src>` | 524 |
| 19 | `<src>駅ももう</src>` | `<src>駅ももう</src>` | 449 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 335 |
| 21 | `<src>歩いて一分</src>` | `<src>歩いて一分</src>` | 250 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないかそんな</src>` | 261 |
| 23 | `<src>レベルのね</src>` | `<src>レベルのね</src>` | 255 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあ</src>` | 289 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルになってますので</src>` | 229 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 213 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 150 |
| 28 | `<src>ください</src>` | `<src>ください</src>` | 127 |
| 29 | `<src>それではですね今回は。</src>` | `<src>それではですね今回は。</src>` | 133 |
