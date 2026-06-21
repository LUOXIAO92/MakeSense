# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9442
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.6225
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
  - PROCESS_TIME_MS_AVG: 1428.4870
  - PROCESS_TIME_MS_P50: 1304.0060
  - PROCESS_TIME_MS_P95: 2465.6280
  - PROCESS_TIME_MS_MAX: 3769.0360

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要做</src>` | 2195 |
| 2 | `<src>家长需要做的是，</src>` | `<src>的是，</src>` | 903 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 862 |
| 4 | `<src>用我们深深的</src>` | `<src>用我们深深的</src>` | 1279 |
| 5 | `<src>爱浇水、</src>` | `<src>爱浇水，</src>` | 817 |
| 6 | `<src>施肥，</src>` | `<src>所以</src>` | 1507 |
| 7 | `<src>给足</src>` | `<src>给足</src>` | 1313 |
| 8 | `<src>孩子心理营养，</src>` | `<src>孩子心灵营养，</src>` | 2044 |
| 9 | `<src><\|wait\|></src>` | `<src>给耐心</src>` | 342 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>等他</src>` | 1662 |
| 11 | `<src>慢慢长大。</src>` | `<src>慢慢长大。</src>` | 2165 |

---

### Test Example 2 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>아, 저는 </src>` | 2065 |
| 2 | `<src>옹심이, </src>` | `<src>용신이 </src>` | 986 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 896 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>아 칼 용신이 </src>` | 1409 |
| 5 | `<src>옹심이가 </src>` | `<src>어 혹설 용신이 가 </src>` | 683 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1739 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이는 건데요. 야, </src>` | 1442 |
| 8 | `<src>야, </src>` | `<src><\|wait\|></src>` | 1706 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 512 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해킹으로 </src>` | 3229 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 맞는 것 </src>` | 694 |

---

### Test Example 3 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1741 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 852 |
| 3 | `<src>これなんかまだ</src>` | `<src>これなんかまだ</src>` | 882 |
| 4 | `<src>一年生ですからね。</src>` | `<src>一年生ですからね。</src>` | 1204 |
| 5 | `<src>この時点で</src>` | `<src>この時点で</src>` | 826 |
| 6 | `<src>こう短く</src>` | `<src>こう短く</src>` | 1649 |
| 7 | `<src>剪定を</src>` | `<src>剪定を</src>` | 1387 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2056 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>こうタイズしてってあげると</src>` | 580 |
| 10 | `<src>十年経っても</src>` | `<src>十年経っても</src>` | 3219 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1025 |

---

### Test Example 4 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1864 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src><\|wait\|></src>` | 899 |
| 3 | `<src>촉발 시키고 </src>` | `<src>Abbot Jr. tucking his shirt in </src>` | 1341 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1274 |
| 5 | `<src>자신 의 </src>` | `<src>and his </src>` | 1338 |
| 6 | `<src><\|wait\|></src>` | `<src>bedroom jug </src>` | 885 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>in Helena </src>` | 1238 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1956 |
| 9 | `<src>박한상과 </src>` | `<src>park bench with </src>` | 1354 |
| 10 | `<src><\|wait\|></src>` | `<src>four other teenagers </src>` | 2449 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>sitting. </src>` | 1051 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2055 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>抛洒完以后呢，</src>` | 1226 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1135 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了，</src>` | 1260 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1611 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在一个</src>` | 1467 |
| 7 | `<src>相对的低</src>` | `<src><\|wait\|></src>` | 1945 |
| 8 | `<src>能量的运行</src>` | `<src>相对的低能量的</src>` | 456 |
| 9 | `<src>状态，</src>` | `<src>运行状态，</src>` | 1488 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 2179 |
| 11 | `<src>抑郁状态。</src>` | `<src>抑郁状态。</src>` | 1361 |

---

### Test Example 6 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1926 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>面对这个情况，我们就是</src>` | 1312 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 626 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1648 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1625 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们现有</src>` | 1408 |
| 7 | `<src>不要想自己</src>` | `<src>这个状况，不要想自己</src>` | 1719 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 703 |
| 9 | `<src>独立承担。</src>` | `<src>不理成担，</src>` | 1530 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言</src>` | 2169 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是给就是署凶。</src>` | 1435 |

---

### Test Example 7 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>乖的</src>` | 2260 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>忪子儿身边，</src>` | 948 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个友谊很大，</src>` | 974 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1014 |
| 5 | `<src><\|wait\|></src>` | `<src>那我要</src>` | 833 |
| 6 | `<src>呢，我再放一点</src>` | `<src>再拜个阿姨，</src>` | 1950 |
| 7 | `<src>儿核桃</src>` | `<src>和陶儿</src>` | 1250 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1968 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>认识一下儿，</src>` | 1657 |
| 10 | `<src>这种核桃</src>` | `<src><\|wait\|></src>` | 2193 |
| 11 | `<src>仁儿。</src>` | `<src>这种喝陶人。</src>` | 1472 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명당에 있는 </src>` | 2333 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성들은 </src>` | 994 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 801 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1424 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 582 |
| 6 | `<src>무작위로 </src>` | `<src>무작위로 뽑힌 </src>` | 2022 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성들이 </src>` | 1170 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1890 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2087 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 모르 았 던 </src>` | 1868 |
| 11 | `<src>교사 들은. </src>` | `<src>교사 들은. </src>` | 1892 |

---

### Test Example 9 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2039 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>要器速是容易的，</src>` | 1434 |
| 3 | `<src>但是</src>` | `<src><\|wait\|></src>` | 634 |
| 4 | `<src>只有一个师父</src>` | `<src>但是</src>` | 1127 |
| 5 | `<src><\|wait\|></src>` | `<src>只有一个师傅指导到</src>` | 689 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1815 |
| 7 | `<src>处于中间，</src>` | `<src>如波[]>` | 1136 |
| 8 | `<src>所以</src>` | `<src>处于中间，所以</src>` | 2137 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反</src>` | 2103 |
| 10 | `<src>要成为</src>` | `<src>要成为一个</src>` | 1834 |
| 11 | `<src>一个师父。</src>` | `<src>师傅，</src>` | 2046 |

---

### Test Example 10 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2205 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 997 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 810 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to rinse and repeat. </src>` | 1512 |
| 5 | `<src>Find what you're good at </src>` | `<src>Find what you're good at </src>` | 648 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 2085 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1034 |
| 8 | `<src>And what you're not good at, </src>` | `<src>And what you're not good at, </src>` | 1972 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get the people around you to help you with. </src>` | 1900 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1919 |
| 11 | `<src>And until next time. </src>` | `<src>And until next time. </src>` | 2230 |

---

### Test Example 11 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1859 |
| 2 | `<src>Did very important research </src>` | `<src>Did very important research </src>` | 1131 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 938 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people. </src>` | 1438 |
| 5 | `<src>This is tip of the stem </src>` | `<src>This is tip of the stem </src>` | 1462 |
| 6 | `<src>research, </src>` | `<src>research, </src>` | 766 |
| 7 | `<src>looking at the ten percent </src>` | `<src>looking at the ten percent </src>` | 1370 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1812 |
| 9 | `<src>of the happiest people </src>` | `<src>of the happiest people </src>` | 3591 |
| 10 | `<src>out there, </src>` | `<src>out there—people with </src>` | 432 |
| 11 | `<src>people that we can learn from. </src>` | `<src>whom we can learn from. </src>` | 2466 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1848 |
| 2 | `<src>doing? </src>` | `<src><\|wait\|></src>` | 998 |
| 3 | `<src>Drop into </src>` | `<src>doing? Drop into </src>` | 855 |
| 4 | `<src>your body. </src>` | `<src>your body. </src>` | 1388 |
| 5 | `<src>Where does the tension </src>` | `<src>Where does the tension </src>` | 656 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 2062 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a headache? </src>` | 1117 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tightness in your chest? </src>` | 1869 |
| 9 | `<src>I ask them what </src>` | `<src>I ask them," Well, </src>` | 3621 |
| 10 | `<src><\|wait\|></src>` | `<src>and for which are you used </src>` | 1183 |
| 11 | `<src>language are you using? </src>` | `<src>say?" </src>` | 2220 |

---

### Test Example 13 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>まあだんだんちょっと</src>` | 2448 |
| 2 | `<src>距離が</src>` | `<src>距離が</src>` | 814 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 946 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>大将が</src>` | 1252 |
| 5 | `<src>多いですね。</src>` | `<src>あるからったがですね</src>` | 693 |
| 6 | `<src>開業したい方って</src>` | `<src>海遊してぃ方って</src>` | 2172 |
| 7 | `<src>すごい</src>` | `<src>すごい勢い動こしい</src>` | 1157 |
| 8 | `<src>自己意識高いし、</src>` | `<src>とか、</src>` | 1618 |
| 9 | `<src>自分で</src>` | `<src>でいうじゃで</src>` | 562 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>普通に遊ぶとシャ&#96;&#96;&#96;</src>` | 3346 |
| 11 | `<src>傾向が強いので、</src>` | `<src>結構強いので</src>` | 1246 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 2256 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2352 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 931 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 922 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1247 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 682 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1954 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1188 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 1758 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 310 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 1318 |
| 11 | `<src><\|wait\|></src>` | `<src>So this </src>` | 2289 |
| 12 | `<src>this game dot scored array. </src>` | `<src>game.sort array. </src>` | 1145 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2526 |

---

### Test Example 15 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1875 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src><\|wait\|></src>` | 1001 |
| 3 | `<src>chemical bonds </src>` | `<src>rubber band, </src>` | 873 |
| 4 | `<src>also store energy, </src>` | `<src>chemical bonds also store energy. And when those </src>` | 1708 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1645 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1443 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted to </src>` | 1538 |
| 8 | `<src>other types of energy, </src>` | `<src>other types of energy, like </src>` | 796 |
| 9 | `<src>like heat or light, </src>` | `<src>heat or light. </src>` | 1727 |
| 10 | `<src><\|wait\|></src>` | `<src>Or, </src>` | 2039 |
| 11 | `<src>or gets used to make </src>` | `<src>gets used to make </src>` | 1440 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 2338 |

---

### Test Example 16 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1831 |
| 2 | `<src>如果在女高中生</src>` | `<src>如果在女高中生</src>` | 1112 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相古怪的人</src>` | 1307 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1047 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>之间有着某种联系，</src>` | 1033 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 1323 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1183 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从那天夜里开始的？</src>` | 2015 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1739 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2131 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思绪</src>` | 1734 |
| 12 | `<src>连篇。</src>` | `<src>连篇。</src>` | 2089 |

---

### Test Example 17 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 너무 </src>` | 2009 |
| 2 | `<src><\|wait\|></src>` | `<src>인 것 </src>` | 937 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저열한 일일 수 있지만 </src>` | 1135 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 1546 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 1629 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 프로 </src>` | 1723 |
| 7 | `<src>뭐 있고 </src>` | `<src>하고 있고 </src>` | 1876 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 더 보살 로 </src>` | 563 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>보일 프로 하고 있어요 </src>` | 3313 |
| 10 | `<src>지금 나한테 </src>` | `<src>우주 가 지금 나한테 </src>` | 1399 |
| 11 | `<src>보살 이라는데. </src>` | `<src>보살 이라는 거. </src>` | 2718 |

---

### Test Example 18 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src>让我</src>` | 1700 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 876 |
| 3 | `<src>回到我生活</src>` | `<src>回到我生活</src>` | 877 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>的一个轨道哈，</src>` | 1143 |
| 5 | `<src>让我能够哈，</src>` | `<src>让我能够哈，</src>` | 898 |
| 6 | `<src>在他下班的时候，</src>` | `<src>在他下班的时候，</src>` | 1840 |
| 7 | `<src>在做热汤</src>` | `<src>在做热汤</src>` | 1368 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>热饭给大家吃。真的，</src>` | 2086 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1504 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>我当时悲痛的时候，就吃一碗粥</src>` | 2392 |
| 11 | `<src>小小的愿望</src>` | `<src>吃一碗小小的慰问</src>` | 1815 |
| 12 | `<src>哈。</src>` | `<src>哈。</src>` | 2204 |

---

### Test Example 19 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1960 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>다른 잔찜에 </src>` | 1000 |
| 3 | `<src>해가지고 내가 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 1229 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>주길 넣고 들어왔 수다. </src>` | 1477 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜에 </src>` | 1686 |
| 6 | `<src>죽여 달라 </src>` | `<src>주겨 달라 해가지고 내가 </src>` | 1560 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>안 되냐? 내가 </src>` | 2040 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 </src>` | 3418 |
| 9 | `<src><\|wait\|></src>` | `<src>있는 줄 알았느냐? </src>` | 600 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>응. </src>` | 1745 |
| 11 | `<src>내가 가. </src>` | `<src>내가 가. </src>` | 2275 |

---

### Test Example 20 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1850 |
| 2 | `<src>映画でですね、</src>` | `<src>えええ関係ですね。</src>` | 924 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 855 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>円生速度がどうか</src>` | 1345 |
| 5 | `<src>調べるときに、</src>` | `<src>っていう場合において、</src>` | 828 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>まあえの卵光</src>` | 1933 |
| 7 | `<src>ことで、あの</src>` | `<src>調べることね、</src>` | 1276 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>あのその円生速度どうか</src>` | 1903 |
| 9 | `<src>保証する、生息である</src>` | `<src>っていう相関する相関で</src>` | 2321 |
| 10 | `<src>ことを保証する</src>` | `<src>いうことを保証する</src>` | 1626 |
| 11 | `<src>といったような</src>` | `<src>といったような</src>` | 1892 |
| 12 | `<src>使い方をされます。</src>` | `<src>使い方をされます。</src>` | 2243 |

---

### Test Example 21 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツ</src>` | 2154 |
| 2 | `<src>あの</src>` | `<src>などが</src>` | 798 |
| 3 | `<src>いただもらえる</src>` | `<src>あの</src>` | 901 |
| 4 | `<src>といったようなものも</src>` | `<src>いただいたものといったようなものも用意しております</src>` | 1234 |
| 5 | `<src>用意しておりますので</src>` | `<src>ので、ぜひ</src>` | 879 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご査袋ください。</src>` | 1800 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 1265 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になりまして、</src>` | 2115 |
| 9 | `<src>えっと</src>` | `<src>えっと</src>` | 2622 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1386 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>ランチの案内がありますので、</src>` | 2804 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>もう少々お待ちください。</src>` | 1448 |

---

### Test Example 22 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2097 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 898 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 824 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1115 |
| 5 | `<src>ゴッホ、</src>` | `<src>ゴッホ、</src>` | 880 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン、</src>` | 1732 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1419 |
| 8 | `<src>セザンヌ、</src>` | `<src>セザンヌ、</src>` | 2141 |
| 9 | `<src>ルナールなど</src>` | `<src>ルナールなど</src>` | 1945 |
| 10 | `<src>という人の絵</src>` | `<src>という人の絵</src>` | 1975 |
| 11 | `<src>は、田舎の</src>` | `<src>は、田舎の</src>` | 2750 |
| 12 | `<src>中学生でも。</src>` | `<src>中学生でも。</src>` | 1564 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1963 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Kiran Patel. </src>` | 1134 |
| 3 | `<src>I am currently </src>` | `<src>I am currently </src>` | 824 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1385 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>studying a Bachelor of Finance </src>` | 656 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a Bachelor of Psychology </src>` | 1932 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1181 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at the ANU, </src>` | 1904 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2739 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>and in the future, I want to go into </src>` | 1233 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2780 |
| 12 | `<src>corporate consultancy. </src>` | `<src>corporate consultancy. </src>` | 1453 |

---

### Test Example 24 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1915 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 853 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>选择二十几小时，</src>` | 954 |
| 4 | `<src>服务</src>` | `<src><\|wait\|></src>` | 1122 |
| 5 | `<src>在一级一线</src>` | `<src>ให服在一集一线</src>` | 979 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>平常的大牛们，</src>` | 1834 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说</src>` | 1124 |
| 8 | `<src><\|wait\|></src>` | `<src>呃，</src>` | 1994 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>在做维向沟通</src>` | 574 |
| 10 | `<src>发现</src>` | `<src>好事几点你会发现，</src>` | 3322 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维向沟通</src>` | 1119 |
| 12 | `<src>的新榜反而</src>` | `<src>平凡的新棒</src>` | 2395 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 995 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1972 |
| 2 | `<src>一切正常，</src>` | `<src><\|wait\|></src>` | 904 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>一切正常，</src>` | 858 |
| 4 | `<src>所以</src>` | `<src>活蹦乱跳，所以</src>` | 1465 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开刀。</src>` | 699 |
| 6 | `<src>期间</src>` | `<src>期间大概有</src>` | 1679 |
| 7 | `<src>大概有十位医生</src>` | `<src>十位医生来</src>` | 1387 |
| 8 | `<src>来诊断，</src>` | `<src>审断，</src>` | 1947 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 1636 |
| 10 | `<src>一下提腿，</src>` | `<src>一站立腿，</src>` | 2240 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 1547 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 2244 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>疑惑的离开。</src>` | 701 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これがギア</src>` | 2207 |
| 2 | `<src>です。</src>` | `<src><\|wait\|></src>` | 898 |
| 3 | `<src>ギアが</src>` | `<src>です。ギアが</src>` | 909 |
| 4 | `<src>緩むと芯が</src>` | `<src>緩むと芯が</src>` | 1281 |
| 5 | `<src><\|wait\|></src>` | `<src>上げ下げできなくなってしまう</src>` | 840 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1662 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1283 |
| 8 | `<src>役ねじの</src>` | `<src><\|wait\|></src>` | 2051 |
| 9 | `<src>ナットが</src>` | `<src>逆ネジのナットが</src>` | 1638 |
| 10 | `<src>ついているっていうことです</src>` | `<src>ついているっていうこと</src>` | 2237 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1560 |
| 12 | `<src>はい、</src>` | `<src><\|wait\|></src>` | 2235 |
| 13 | `<src>分解完了。</src>` | `<src>ハイブンブレーキを。</src>` | 773 |

---

### Test Example 27 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1878 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 806 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 918 |
| 4 | `<src>テキという設備寺が</src>` | `<src>テキという設備寺が</src>` | 1239 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 842 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1632 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1389 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井慶義氏の仕組み</src>` | 2248 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1195 |
| 10 | `<src>は五経、</src>` | `<src>は五経、</src>` | 2512 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1203 |
| 12 | `<src>設備寺、五比</src>` | `<src>設備寺、五比</src>` | 2766 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 664 |

---

### Test Example 28 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2321 |
| 2 | `<src>The meaning of </src>` | `<src><\|wait\|></src>` | 1007 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>the 19th Amendment </src>` | 1231 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1151 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1013 |
| 6 | `<src>to how political </src>` | `<src>to how political </src>` | 1210 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1252 |
| 8 | `<src>change can happen </src>` | `<src>change can happen </src>` | 1923 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1402 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2426 |
| 11 | `<src>The meanings </src>` | `<src>The meanings </src>` | 1040 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>of the amendment, of course, are </src>` | 2968 |
| 13 | `<src>myriad. </src>` | `<src>myriad. </src>` | 772 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Or, or if you </src>` | 2180 |
| 2 | `<src>have to produce </src>` | `<src>have to produce </src>` | 923 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 829 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1396 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 572 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know how </src>` | 2031 |
| 7 | `<src>to spell </src>` | `<src>to spell </src>` | 1074 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the words. Like, oh, </src>` | 2017 |
| 9 | `<src>is this word </src>` | `<src>is this word </src>` | 1609 |
| 10 | `<src>spelled with a double </src>` | `<src>spelled with a double </src>` | 2262 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1649 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>p, double lam? I don't </src>` | 2583 |
| 13 | `<src>know. </src>` | `<src>know. </src>` | 1025 |

---

### Test Example 30 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1882 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>바나듐이라든가 이것 들은 </src>` | 1669 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 윤수릉과 </src>` | 1174 |
| 4 | `<src>이제 거진 </src>` | `<src>이제 </src>` | 776 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>거진 유사 찬 자긍 진을 </src>` | 1803 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>보통 에게 </src>` | 1348 |
| 7 | `<src>굉장히 아주 </src>` | `<src>굉장히 아주 </src>` | 1919 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연 업 미네랄이다 </src>` | 626 |
| 9 | `<src>이렇게 </src>` | `<src>이렇게 </src>` | 2934 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>이야기 할 정도 의 </src>` | 692 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. 이제 </src>` | 2558 |
| 12 | `<src>그거 에다가 </src>` | `<src>그거 에다가 </src>` | 1757 |
| 13 | `<src>아연. </src>` | `<src>아연. </src>` | 1073 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分呢，</src>` | 2009 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们可以看到的是</src>` | 924 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个在钓鱼</src>` | 1102 |
| 4 | `<src>的人，但是</src>` | `<src>的人，但是</src>` | 1258 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 835 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1121 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>通常逢到这样的一个状况的</src>` | 1550 |
| 8 | `<src>时候，就要去</src>` | `<src>时候，就要去</src>` | 1981 |
| 9 | `<src>特别注意，</src>` | `<src>特别注意，</src>` | 1337 |
| 10 | `<src>是它能不能够</src>` | `<src>是它能不能够</src>` | 2443 |
| 11 | `<src>钓到鱼，</src>` | `<src>钓到鱼，</src>` | 1179 |
| 12 | `<src>它钓不到鱼</src>` | `<src>它钓不到鱼</src>` | 2528 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 809 |
| 14 | `<src>的意思哦。</src>` | `<src>的意思哦。</src>` | 1220 |

---

### Test Example 32 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2180 |
| 2 | `<src>要提醒大家，</src>` | `<src><\|wait\|></src>` | 1016 |
| 3 | `<src>在这个罗马呢</src>` | `<src>在这个罗马呢，</src>` | 1093 |
| 4 | `<src>不是一天造成的，</src>` | `<src><\|wait\|></src>` | 1259 |
| 5 | `<src>所以呢，</src>` | `<src>不是一天造成的，所以呢，</src>` | 894 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 1193 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1275 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊、</src>` | 2085 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 3333 |
| 10 | `<src>一夕之间就</src>` | `<src>也不可能是你一时之间</src>` | 678 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1788 |
| 12 | `<src>演变出来的，</src>` | `<src>就显现出来</src>` | 2299 |
| 13 | `<src>因此会建议</src>` | `<src>的。因此，</src>` | 937 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>会建议属鸡的朋友呢。</src>` | 1067 |

---

### Test Example 33 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1785 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>达到了一个甜头，那</src>` | 1309 |
| 3 | `<src>如果你</src>` | `<src>如果你</src>` | 579 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>达到了甜头之后，</src>` | 1441 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必就要</src>` | 801 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1583 |
| 7 | `<src>先守住，</src>` | `<src>先守住，</src>` | 1256 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想说，哎，那我再</src>` | 2082 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1698 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>继续操作下去哦。</src>` | 2203 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3011 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1289 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1060 |
| 14 | `<src>因为呢。</src>` | `<src>因为呢。</src>` | 1130 |

---

### Test Example 34 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1781 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>150만 개가 종업원 수 </src>` | 1679 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>100명 미만 으로 </src>` | 1332 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 894 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 1659 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1403 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 성장 하거나 </src>` | 2087 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>혹은 폐업 할 길을 </src>` | 3349 |
| 9 | `<src>걷게 되는데 </src>` | `<src>걷게 되는데 </src>` | 577 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>일본 의 소기업들은 </src>` | 1949 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>성장 도 </src>` | 2201 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>폐업 도 하지 않는 </src>` | 1117 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들만 보이 게 된 거죠. </src>` | 1253 |

---

### Test Example 35 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new. </src>` | 1998 |
| 2 | `<src>There were </src>` | `<src>There were </src>` | 912 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 859 |
| 4 | `<src>such interfaces before, </src>` | `<src>such interfaces before, </src>` | 1273 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 816 |
| 6 | `<src>netfilter, TC. </src>` | `<src>netfilter, TC. </src>` | 1830 |
| 7 | `<src>Yeah, so </src>` | `<src>Yeah, so </src>` | 1259 |
| 8 | `<src>this is just </src>` | `<src><\|wait\|></src>` | 1925 |
| 9 | `<src>one another place </src>` | `<src>this is just one </src>` | 509 |
| 10 | `<src>to look at. </src>` | `<src>other place to look at. </src>` | 3317 |
| 11 | `<src>But </src>` | `<src>But </src>` | 987 |
| 12 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2345 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1188 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on BugRepo </src>` | 1201 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 1117 |

---

### Test Example 36 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1856 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 너희 가 </src>` | 1428 |
| 3 | `<src>이방인으로 </src>` | `<src>이방인으로 </src>` | 779 |
| 4 | `<src>있을 때에 </src>` | `<src>있을 때에 </src>` | 1281 |
| 5 | `<src>말 못하 는 </src>` | `<src><\|wait\|></src>` | 1243 |
| 6 | `<src>우상에게로 </src>` | `<src>말 못하 는 우상에게로 </src>` | 1641 |
| 7 | `<src>끄는 그대로 </src>` | `<src><\|wait\|></src>` | 715 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>그대로 돌려갖는 </src>` | 1910 |
| 9 | `<src><\|wait\|></src>` | `<src>그러니 라. </src>` | 1163 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2537 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 1211 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 2659 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님의 영으로 </src>` | 770 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는. </src>` | 1278 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1213 |

---

### Test Example 37 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2100 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. </src>` | 940 |
| 3 | `<src>How far did you </src>` | `<src>How far did you </src>` | 883 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 1097 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? Did you </src>` | 980 |
| 6 | `<src>graduate from high school? </src>` | `<src>graduate from high school? </src>` | 1953 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level </src>` | 1283 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>of attainment. Did you </src>` | 1863 |
| 9 | `<src>to college, </src>` | `<src>go to college and </src>` | 1458 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>so, did you graduate? </src>` | 2332 |
| 11 | `<src>That's another level of </src>` | `<src>That's another level </src>` | 1455 |
| 12 | `<src>attainment. </src>` | `<src>of attainment. </src>` | 2330 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 779 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. I'll see you </src>` | 1328 |
| 15 | `<src>online. </src>` | `<src>online. </src>` | 1189 |

---

### Test Example 38 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who's </src>` | 2336 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 918 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get, </src>` | 958 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1273 |
| 5 | `<src>and I have ten of them </src>` | `<src>and I have ten of them </src>` | 801 |
| 6 | `<src>that I think are </src>` | `<src>that I really </src>` | 1589 |
| 7 | `<src>really important. </src>` | `<src>important </src>` | 1215 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1979 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go </src>` | 1612 |
| 10 | `<src>I have about </src>` | `<src>into. I have about one </src>` | 2345 |
| 11 | `<src>one minute videos </src>` | `<src>minute of videos </src>` | 1601 |
| 12 | `<src>that follow this video </src>` | `<src>that follow this video </src>` | 2350 |
| 13 | `<src><\|wait\|></src>` | `<src>that cover each one, </src>` | 809 |
| 14 | `<src>that cover each one </src>` | `<src>and a little more </src>` | 1094 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>detail, </src>` | 1313 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 2140 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1133 |
| 3 | `<src>很不错的，但是</src>` | `<src>很不错的，但是</src>` | 884 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src><\|wait\|></src>` | 1263 |
| 5 | `<src>也就是</src>` | `<src>比较偏正财的部分，也就是</src>` | 1509 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面的</src>` | 850 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>业绩成长所带来的红利，</src>` | 1388 |
| 8 | `<src>与收入的</src>` | `<src><\|wait\|></src>` | 1695 |
| 9 | `<src>提升。如果是在</src>` | `<src>收入的提升。</src>` | 1845 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>如果涉及到投资理财方面</src>` | 2198 |
| 11 | `<src>这个月</src>` | `<src>这个月，也是</src>` | 2334 |
| 12 | `<src>也是不错，只是</src>` | `<src>不错，</src>` | 1802 |
| 13 | `<src>相对正财来说就</src>` | `<src>只是相对正财来说，</src>` | 1134 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了</src>` | 1223 |
| 15 | `<src><\|wait\|></src>` | `<src>那么一点。</src>` | 899 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 2180 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어, 어찌 보면 </src>` | 1245 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1215 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1048 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>동생 이자 </src>` | 1686 |
| 6 | `<src>그래도 가족 </src>` | `<src>그래도 가족 </src>` | 1340 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>같은 동생 이잖아. </src>` | 758 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 1558 |
| 9 | `<src><\|wait\|></src>` | `<src>어, </src>` | 507 |
| 10 | `<src>책임감 보다는 </src>` | `<src>제인감보다는 </src>` | 3302 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 684 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 2733 |
| 13 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1176 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>좀 많은 것 </src>` | 1204 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려놓 고 </src>` | 1061 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>행복 했으면 좋겠다. </src>` | 1210 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったら</src>` | 2117 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>もう眠らせてやれ。</src>` | 973 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 805 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1115 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>今基地を見ている。</src>` | 902 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1631 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1409 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2052 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>遠い超えてる船を起せ球。</src>` | 700 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 3140 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 1020 |
| 12 | `<src>船大工をやってる</src>` | `<src>船大工をやってる</src>` | 2754 |
| 13 | `<src>が、</src>` | `<src>が、</src>` | 795 |
| 14 | `<src>俺は</src>` | `<src>俺は</src>` | 1248 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>こんなにすごい海賊船を</src>` | 1222 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 1008 |

---

### Test Example 42 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2057 |
| 2 | `<src>十一二手とか</src>` | `<src>十一・二日とか</src>` | 1218 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 846 |
| 4 | `<src>十秒で。</src>` | `<src>十秒で。</src>` | 1269 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 576 |
| 6 | `<src>一秒に</src>` | `<src>一秒に</src>` | 1813 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>一定強ぐらいの</src>` | 1256 |
| 8 | `<src>計算ですか</src>` | `<src>してたんですかね。</src>` | 1952 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 1651 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 2180 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 1656 |
| 12 | `<src><\|wait\|></src>` | `<src>十一・二日</src>` | 2319 |
| 13 | `<src>十一二手で</src>` | `<src><\|wait\|></src>` | 769 |
| 14 | `<src>あの</src>` | `<src>であの</src>` | 1133 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮内馬とかが</src>` | 1204 |
| 16 | `<src>あるから。</src>` | `<src>あるから。</src>` | 966 |

---

### Test Example 43 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수 가 </src>` | 2106 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 939 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 1310 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 배형주도 </src>` | 1179 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1555 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 1527 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 1833 |
| 8 | `<src>이 가벼운 </src>` | `<src>이 가벼운 </src>` | 547 |
| 9 | `<src>종목 들이 </src>` | `<src>종목 들이 </src>` | 1495 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2200 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 움직이 기 때문 에 </src>` | 1896 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>항상 </src>` | 2201 |
| 13 | `<src>요 시총이 </src>` | `<src>요 시총이 </src>` | 766 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1114 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨봐야 </src>` | 1384 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 1007 |

---

### Test Example 44 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계서 </src>` | 2134 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1049 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1311 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 1152 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1463 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트예요. 뭐 </src>` | 1551 |
| 7 | `<src><\|wait\|></src>` | `<src>이게 컨설턴트여야 </src>` | 1718 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>되고 A라는 </src>` | 740 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1444 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2391 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 1614 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>비란 사람 이 </src>` | 2425 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 672 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스사이트 스킷에서 </src>` | 1245 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>EX 파일까지 </src>` | 1385 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 1166 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2194 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1210 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>というだけじゃなくて、</src>` | 1022 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1134 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>ビジュアルPython開発環境なんですね。</src>` | 894 |
| 6 | `<src>というのもフローリフを</src>` | `<src>そういうのも</src>` | 1193 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフビジュアルに書いた後、</src>` | 1563 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>それあいではPythonコード</src>` | 1874 |
| 9 | `<src>にそこから</src>` | `<src>にそれがそこから</src>` | 1740 |
| 10 | `<src>生成されて、それが</src>` | `<src>生成されて、それが</src>` | 2150 |
| 11 | `<src>実行されることで</src>` | `<src>実行されることで</src>` | 1655 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>信号処理が行われるという</src>` | 2329 |
| 13 | `<src>構造になっているからです。</src>` | `<src>構造になっているからです。</src>` | 784 |
| 14 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1191 |
| 15 | `<src>はい。</src>` | `<src>はい。</src>` | 1392 |
| 16 | `<src>じゃあ。</src>` | `<src>じゃあ、</src>` | 1113 |

---

### Test Example 46 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대해 </src>` | 1777 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1097 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 내놓았습니다. </src>` | 1431 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 로쿠자 의 </src>` | 1061 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>분석 을 보시면 </src>` | 1604 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1423 |
| 7 | `<src>26비트 FP </src>` | `<src>26비트 FP </src>` | 1591 |
| 8 | `<src>파이프 를 </src>` | `<src>파이프 를 </src>` | 757 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비트로 </src>` | 3408 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 </src>` | 535 |
| 11 | `<src><\|wait\|></src>` | `<src>보인다. </src>` | 1715 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>Xbox Series X에서도 없는 </src>` | 2329 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 823 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>CS </src>` | 1051 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>가 여기 도 없다. </src>` | 1409 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1111 |

---

### Test Example 47 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어감 에는 </src>` | 2343 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src><\|wait\|></src>` | 1015 |
| 3 | `<src>운전 을 </src>` | `<src>엄청 헤맨다. </src>` | 1230 |
| 4 | `<src><\|wait\|></src>` | `<src>운전 을 할 건 </src>` | 1245 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src><\|wait\|></src>` | 1473 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>거로 거르 다 이용 안 가네. 뭐 </src>` | 1636 |
| 7 | `<src>강북 을 가면 </src>` | `<src>강북 으로 가면 </src>` | 1792 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 565 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 </src>` | 1685 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>장렬이에요. 좀 </src>` | 2201 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 1902 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 2279 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1082 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모바일 을 그거 는 </src>` | 1102 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>안 된 것 같아요. </src>` | 1043 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1039 |

---

### Test Example 48 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1833 |
| 2 | `<src>HTML이라고 </src>` | `<src>어 Hielmel </src>` | 1094 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 941 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>이라고 하는 컴피 터도 이해 할 수 </src>` | 1600 |
| 5 | `<src><\|wait\|></src>` | `<src>있고 </src>` | 1618 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 이해 할 수 </src>` | 1553 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2074 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>있는 컴퓨터 어 어noise? </src>` | 3769 |
| 9 | `<src>문법 에 </src>` | `<src><\|wait\|></src>` | 1082 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>문법 을 알겠 네 우리 가 이제 </src>` | 2970 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>코드 를 작성 해야 </src>` | 771 |
| 12 | `<src>되는데 </src>` | `<src>되는데 </src>` | 1133 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 코드 를 </src>` | 1215 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1071 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 553 |

---

### Test Example 49 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 간 코 </src>` | 2274 |
| 2 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 921 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>생활 빌 거야, </src>` | 891 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 에 서름이 돋든 </src>` | 1777 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>가시 리 돋든 </src>` | 1623 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>느낌 이 뭐냐면 </src>` | 1565 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 흔들 어서 </src>` | 2188 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>같이 놀자는 거야. </src>` | 3531 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>귀신 이 오면 </src>` | 418 |
| 10 | `<src>물릴 거고 </src>` | `<src>물릴 거고 </src>` | 1936 |
| 11 | `<src>신이 오면 </src>` | `<src>시눈 이 오면 </src>` | 2384 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>너 지켜 주라고 </src>` | 1129 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 줄 거 아니 까. </src>` | 1179 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1148 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 간다. </src>` | 773 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2049 |
| 2 | `<src>Activity than </src>` | `<src>Activity than </src>` | 911 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1018 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is because you're </src>` | 1655 |
| 5 | `<src>absolutely correct, </src>` | `<src>absolutely correct, </src>` | 1641 |
| 6 | `<src>but the reality </src>` | `<src>but the reality </src>` | 1459 |
| 7 | `<src>is is that </src>` | `<src>is is that </src>` | 1884 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new kid on the </src>` | 723 |
| 9 | `<src>block and because the </src>` | `<src>block and because the </src>` | 3317 |
| 10 | `<src>standards have </src>` | `<src>standards have </src>` | 620 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from 20 </src>` | 2820 |
| 12 | `<src>years ago, </src>` | `<src>years ago, </src>` | 1192 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1345 |
| 14 | `<src>a higher standard because </src>` | `<src>a higher standard because </src>` | 1150 |
| 15 | `<src>everything at this point is being </src>` | `<src>everything at this point is being </src>` | 1167 |
| 16 | `<src>held to a higher standard. </src>` | `<src>held to a higher standard. </src>` | 552 |

---

### Test Example 51 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2112 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩或感知对手</src>` | 1197 |
| 3 | `<src>的感情或</src>` | `<src>的感情或</src>` | 856 |
| 4 | `<src>真实意图的，</src>` | `<src>真实意图的，</src>` | 1532 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1613 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1423 |
| 7 | `<src>很多时候经常</src>` | `<src>很多时候经常</src>` | 582 |
| 8 | `<src>会听到人们</src>` | `<src>会听到人们这样说：</src>` | 1784 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1884 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 1995 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 2778 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在说谎了，</src>` | 1609 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1201 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1083 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1148 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 715 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 520 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src><\|wait\|></src>` | 1795 |
| 2 | `<src>首次觉知到</src>` | `<src>佛罗伊的所指</src>` | 1326 |
| 3 | `<src>那个现象：</src>` | `<src>觉得到了那个现象，</src>` | 1025 |
| 4 | `<src>每当我们</src>` | `<src><\|wait\|></src>` | 1132 |
| 5 | `<src><\|wait\|></src>` | `<src>每当我们处于</src>` | 1478 |
| 6 | `<src>处于爱之中，</src>` | `<src>爱之中，</src>` | 881 |
| 7 | `<src>所谓的爱，</src>` | `<src>所谓的爱，</src>` | 1181 |
| 8 | `<src>我们也</src>` | `<src><\|wait\|></src>` | 1913 |
| 9 | `<src>同时进入恨。</src>` | `<src>我们也同时进入恨，</src>` | 1725 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2135 |
| 11 | `<src>在早上的时候，</src>` | `<src>在早上</src>` | 1445 |
| 12 | `<src>它是爱；</src>` | `<src>的时候它是爱，</src>` | 2461 |
| 13 | `<src>到了晚上，</src>` | `<src>到了晚上，</src>` | 690 |
| 14 | `<src>它就变成恨。</src>` | `<src>它就变成</src>` | 1231 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1234 |
| 16 | `<src>那个钟摆</src>` | `<src>恨那个钟摆，</src>` | 1072 |
| 17 | `<src><\|wait\|></src>` | `<src>继续在</src>` | 507 |
| 18 | `<src>继续在移动。</src>` | `<src>一动一动。</src>` | 646 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was </src>` | 2272 |
| 2 | `<src>in turmoil </src>` | `<src>a bit under a mile </src>` | 1040 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 886 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1171 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR </src>` | 820 |
| 6 | `<src><\|wait\|></src>` | `<src>fields being of </src>` | 1541 |
| 7 | `<src>being of critical importance </src>` | `<src>critical importance </src>` | 1348 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 1852 |
| 9 | `<src><\|wait\|></src>` | `<src>variant database </src>` | 441 |
| 10 | `<src>databases, </src>` | `<src>is which is </src>` | 1095 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>obviously one of my loves, </src>` | 2598 |
| 12 | `<src><\|wait\|></src>` | `<src>is that if </src>` | 1259 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree </src>` | 2669 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 663 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in these data </src>` | 1383 |
| 16 | `<src>data sources that we can </src>` | `<src>sources, </src>` | 1157 |
| 17 | `<src>draw from, </src>` | `<src>that we can draw from, </src>` | 1290 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 345 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 550 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point, </src>` | 1966 |
| 2 | `<src>he knows Jesus </src>` | `<src>he knows Jesus </src>` | 946 |
| 3 | `<src>is hungry. </src>` | `<src>is hungry. </src>` | 931 |
| 4 | `<src>He knows that </src>` | `<src>He knows that </src>` | 1275 |
| 5 | `<src>he's been without food, </src>` | `<src>he's been without food, </src>` | 968 |
| 6 | `<src><\|wait\|></src>` | `<src>been in the wilderness </src>` | 1520 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>forty days, that he's hungry. </src>` | 1534 |
| 8 | `<src>And so he says </src>` | `<src>And so he says </src>` | 1587 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>to Jesus," Hey, if you're Jesus, </src>` | 1819 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it." </src>` | 2218 |
| 11 | `<src><\|wait\|></src>` | `<src>Turn these </src>` | 1569 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>stones to bread." </src>` | 2326 |
| 13 | `<src><\|wait\|></src>` | `<src>How did Jesus </src>` | 766 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>deal with that </src>` | 1098 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 1384 |
| 16 | `<src><\|wait\|></src>` | `<src>Man </src>` | 1065 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan </src>` | 252 |
| 18 | `<src>by bread alone. </src>` | `<src>led by bread alone. </src>` | 660 |

---

### Test Example 55 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2052 |
| 2 | `<src>Also, </src>` | `<src>Also, </src>` | 920 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to </src>` | 1020 |
| 4 | `<src>move media objects </src>` | `<src>move media objects </src>` | 1405 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 631 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources. </src>` | 1869 |
| 7 | `<src>So, if </src>` | `<src>So, if </src>` | 1177 |
| 8 | `<src>you get into </src>` | `<src>you get into </src>` | 1873 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 2095 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 1905 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong media </src>` | 1767 |
| 12 | `<src>files to a particular resource, </src>` | `<src>files to a particular resource, </src>` | 2349 |
| 13 | `<src>you need to let us know, </src>` | `<src>you need to let us know, </src>` | 1190 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1137 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1007 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>moving those media files and then making sure they </src>` | 1110 |
| 17 | `<src>get backed up </src>` | `<src>get backed up </src>` | 569 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 355 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2313 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful individual </src>` | 906 |
| 3 | `<src>right, </src>` | `<src>right, </src>` | 800 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1176 |
| 5 | `<src>came along </src>` | `<src>came along </src>` | 784 |
| 6 | `<src>last, not leading. </src>` | `<src>last, not leading. And I don't </src>` | 2377 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>think the courts want to be </src>` | 1145 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1678 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1251 |
| 10 | `<src>change </src>` | `<src>social change </src>` | 2479 |
| 11 | `<src>these days, </src>` | `<src>these days. </src>` | 371 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1888 |
| 13 | `<src>but they rather reflect </src>` | `<src><\|wait\|></src>` | 2200 |
| 14 | `<src>the consensus </src>` | `<src>reflect the consensus </src>` | 929 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1181 |
| 16 | `<src>that's already emerged. </src>` | `<src>that's already emerged. </src>` | 1150 |
| 17 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1063 |
| 18 | `<src>So you have some </src>` | `<src>So you have some </src>` | 529 |
| 19 | `<src>federal judges </src>` | `<src>federal judges </src>` | 203 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 294 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 355 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 2014 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1138 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 812 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，我们可以看到</src>` | 1549 |
| 5 | `<src>的一个是客厅</src>` | `<src>的一个是客厅</src>` | 1121 |
| 6 | `<src>的部分。</src>` | `<src>的部分，</src>` | 1097 |
| 7 | `<src>那客厅一般</src>` | `<src><\|wait\|></src>` | 1245 |
| 8 | `<src>都是属于</src>` | `<src>它客厅一般都是</src>` | 2011 |
| 9 | `<src>我们</src>` | `<src>属于我们要</src>` | 1674 |
| 10 | `<src>在休息的地方，</src>` | `<src><\|wait\|></src>` | 2146 |
| 11 | `<src><\|wait\|></src>` | `<src>休息的地方。所以呢，</src>` | 1539 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这身体的部分</src>` | 2362 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，会反映的是</src>` | 708 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 1203 |
| 15 | `<src>一点时间，</src>` | `<src><\|wait\|></src>` | 1111 |
| 16 | `<src>可以好好的</src>` | `<src>一点时间可以</src>` | 1087 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>好好地坐下来休息。可是</src>` | 709 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>如果我们看到</src>` | 566 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>这边是荒芜一人的嘛，</src>` | 380 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 332 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 305 |

---

### Test Example 58 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 에 이준석은 </src>` | 2249 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>당무 를 거부 한 </src>` | 1060 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 907 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1158 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선 을 </src>` | 1664 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1215 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 803 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 1767 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 1977 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 1995 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1800 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 </src>` | 2363 |
| 13 | `<src><\|wait\|></src>` | `<src>들러내 놓고 </src>` | 984 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>윤석열 후보 를 </src>` | 1219 |
| 15 | `<src><\|wait\|></src>` | `<src>떨어뜨리 겠다는 뚝기 를 </src>` | 1239 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>뿜은 공격 성을 </src>` | 922 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로 </src>` | 580 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 361 |
| 19 | `<src>것입니다. </src>` | `<src>것 같습니다. </src>` | 217 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 193 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상납 건 </src>` | 335 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 250 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 275 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 하기에 얼마나 </src>` | 319 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재입니까. </src>` | 307 |

---

### Test Example 59 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1845 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1008 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 875 |
| 4 | `<src>show up to </src>` | `<src>show up to </src>` | 1175 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 835 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>completely revolutionize the world </src>` | 1940 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1173 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1910 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 2411 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 1639 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 2308 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1948 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1234 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations </src>` | 1021 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 872 |
| 16 | `<src><\|wait\|></src>` | `<src>and like to get straight to the </src>` | 1081 |
| 17 | `<src>get straight to the point. </src>` | `<src>point. </src>` | 624 |
| 18 | `<src>They also love to </src>` | `<src>They also love to </src>` | 349 |
| 19 | `<src>play </src>` | `<src>play the devil's advocate </src>` | 407 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and then they </src>` | 282 |
| 21 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 292 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>never shy away from a debate </src>` | 297 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 311 |
| 24 | `<src><\|wait\|></src>` | `<src>and see </src>` | 255 |
| 25 | `<src>ENTP stands for </src>` | `<src>VP stands for </src>` | 206 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>で、まあ</src>` | 2237 |
| 2 | `<src>食堂ね</src>` | `<src>食後の今</src>` | 1021 |
| 3 | `<src>今作ってる</src>` | `<src>作ってるみたいなものだ</src>` | 1091 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>ので、ここのね</src>` | 1376 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>これこれホノルル</src>` | 1785 |
| 6 | `<src>も</src>` | `<src>ホテルも</src>` | 1304 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>朝食が食べれる場所</src>` | 1811 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 545 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になってるので、</src>` | 1374 |
| 10 | `<src>今後ねここ</src>` | `<src>今後ね</src>` | 2297 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 1213 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいなって</src>` | 2521 |
| 13 | `<src>なっていう方はですね</src>` | `<src>いう方はですね、</src>` | 776 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさ</src>` | 1009 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>て見てみると、まあいいじゃないか</src>` | 1269 |
| 16 | `<src><\|wait\|></src>` | `<src>なと、はい。</src>` | 1190 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>と思います。ここの</src>` | 771 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ホテルからですね、</src>` | 508 |
| 19 | `<src>駅ももう</src>` | `<src>부산駅も</src>` | 264 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 190 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 347 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 320 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルのね</src>` | 287 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいね、まあ</src>` | 296 |
| 25 | `<src>ホテルになってますので</src>` | `<src>ホテルなってますので、</src>` | 344 |
| 26 | `<src>よかったらですね</src>` | `<src>行ったらですね、</src>` | 271 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 199 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 161 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね、今回は。</src>` | 146 |
