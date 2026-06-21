# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9874
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.1192
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.0000
  - TGT_RELEASE_TOTAL: 494
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1273.9020
  - PROCESS_TIME_MS_P50: 1389.1240
  - PROCESS_TIME_MS_P95: 1809.0060
  - PROCESS_TIME_MS_MAX: 8264.5550

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1097 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>的宿舍里，</src><tgt><\|wait\|></tgt>` | 824 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个房间</src><tgt><\|wait\|></tgt>` | 1088 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>要很大，</src><tgt><\|wait\|></tgt>` | 1088 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 560 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 1441 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1560 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>下课人。</src><tgt><\|wait\|></tgt>` | 1540 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在宿舍里</src><tgt><\|wait\|></tgt>` | 850 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1517 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 1420 |

---

### Test Example 2 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长</src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>需要做的是</src><tgt><\|wait\|></tgt>` | 813 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1089 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | 1104 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 642 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 1406 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | 1566 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>心瘾</src><tgt><\|wait\|></tgt>` | 1514 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>影响</src><tgt><\|wait\|></tgt>` | 1121 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | 1298 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>长大。</src><tgt><\|wait\|></tgt>` | 1381 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要</src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>气数</src><tgt><\|wait\|></tgt>` | 805 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src>是容易的，但是</src><tgt><\|wait\|></tgt>` | 1134 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有</src><tgt><\|wait\|></tgt>` | 1382 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1068 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>师傅</src><tgt><\|wait\|></tgt>` | 656 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>除了</src><tgt><\|wait\|></tgt>` | 1573 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>中见，所以</src><tgt><\|wait\|></tgt>` | 1624 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>气场反</src><tgt><\|wait\|></tgt>` | 1752 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 1583 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>师傅</src><tgt><\|wait\|></tgt>` | 644 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 867 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>아 칼 </src><tgt><\|wait\|></tgt>` | 1032 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>봉심이 칼 </src><tgt><\|wait\|></tgt>` | 1414 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>봉심이 가 </src><tgt><\|wait\|></tgt>` | 1578 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>석회 </src><tgt><\|wait\|></tgt>` | 1298 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>석회 는 건데요. </src><tgt><\|wait\|></tgt>` | 620 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1648 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>아 진짜 이거 </src><tgt><\|wait\|></tgt>` | 1817 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>행으로 </src><tgt><\|wait\|></tgt>` | 1460 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 죽기 </src><tgt><\|wait\|></tgt>` | 1332 |

---

### Test Example 5 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거</src><tgt><\|wait\|></tgt>` | 900 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이럴지</src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>너무</src><tgt><\|wait\|></tgt>` | 1052 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좋아요</src><tgt><\|wait\|></tgt>` | 1406 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>근데</src><tgt><\|wait\|></tgt>` | 1588 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 거</src><tgt><\|wait\|></tgt>` | 1393 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>거린데</src><tgt><\|wait\|></tgt>` | 530 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>꿈일 필요</src><tgt><\|wait\|></tgt>` | 1779 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>있고</src><tgt><\|wait\|></tgt>` | 1736 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>나만</src><tgt><\|wait\|></tgt>` | 1479 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>보살이</src><tgt><\|wait\|></tgt>` | 1339 |

---

### Test Example 6 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 850 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 799 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely happy </src><tgt><\|wait\|></tgt>` | 1043 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>people. This is </src><tgt><\|wait\|></tgt>` | 1365 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>tip of the stem, </src><tgt><\|wait\|></tgt>` | 1321 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>research. Looking </src><tgt><\|wait\|></tgt>` | 605 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>at 10% </src><tgt><\|wait\|></tgt>` | 1554 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1828 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>people out. </src><tgt><\|wait\|></tgt>` | 1715 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>People that </src><tgt><\|wait\|></tgt>` | 1530 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1380 |

---

### Test Example 7 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>模拟这个情况，</src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 749 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>遇到问题，</src><tgt><\|wait\|></tgt>` | 1062 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就是感谢的</src><tgt><\|wait\|></tgt>` | 1508 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回复主管，</src><tgt><\|wait\|></tgt>` | 1517 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1580 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>这个状况，</src><tgt><\|wait\|></tgt>` | 1520 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1326 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>怎么把它</src><tgt><\|wait\|></tgt>` | 1050 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>强起来，</src><tgt><\|wait\|></tgt>` | 1433 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>整天</src><tgt><\|wait\|></tgt>` | 1446 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 891 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Apple </src><tgt><\|wait\|></tgt>` | 787 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>초밥 </src><tgt><\|wait\|></tgt>` | 1043 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>치키고 </src><tgt><\|wait\|></tgt>` | 1432 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>자신의 모로 조깅 </src><tgt><\|wait\|></tgt>` | 994 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 978 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1753 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박찬과 </src><tgt><\|wait\|></tgt>` | 1824 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | 1606 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>있답니다. </src><tgt><\|wait\|></tgt>` | 1552 |

---

### Test Example 9 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 761 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | 802 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>中まだ1年</src><tgt><\|wait\|></tgt>` | 1098 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>生ですからね。</src><tgt><\|wait\|></tgt>` | 1390 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>はい、その時点で</src><tgt><\|wait\|></tgt>` | 1611 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>資格を</src><tgt><\|wait\|></tgt>` | 409 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1584 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>退職してあげると</src><tgt><\|wait\|></tgt>` | 1892 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>10年経っても</src><tgt><\|wait\|></tgt>` | 1566 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>大丈夫だ。</src><tgt><\|wait\|></tgt>` | 1569 |

---

### Test Example 10 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘纱完以后</src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 917 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 1042 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能力也</src><tgt><\|wait\|></tgt>` | 1386 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>刷了，然后就</src><tgt><\|wait\|></tgt>` | 1594 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>去填入在一个</src><tgt><\|wait\|></tgt>` | 1649 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src>相对的</src><tgt><\|wait\|></tgt>` | 1718 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>低能量的运行状况</src><tgt><\|wait\|></tgt>` | 1790 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>排开。</src><tgt><\|wait\|></tgt>` | 1526 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1261 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>的</src><tgt><\|wait\|></tgt>` | 1286 |

---

### Test Example 11 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 888 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>ような感じで</src><tgt><\|wait\|></tgt>` | 1028 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>オーサーロカタが</src><tgt><\|wait\|></tgt>` | 1408 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>やっぱり多いですね。</src><tgt><\|wait\|></tgt>` | 1384 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | 784 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ引っ越したい方</src><tgt><\|wait\|></tgt>` | 1324 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1662 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>いいですね。</src><tgt><\|wait\|></tgt>` | 1723 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>でもっと本音で</src><tgt><\|wait\|></tgt>` | 1670 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>喋る</src><tgt><\|wait\|></tgt>` | 1351 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>方が強いので</src><tgt><\|wait\|></tgt>` | 1423 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>待って、</src><tgt><\|wait\|></tgt>` | 1070 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>この辺りから</src><tgt><\|wait\|></tgt>` | 969 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので</src><tgt><\|wait\|></tgt>` | 950 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>ご</src><tgt><\|wait\|></tgt>` | 1343 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>方法</src><tgt><\|wait\|></tgt>` | 1419 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン</src><tgt><\|wait\|></tgt>` | 724 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1258 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt><\|wait\|></tgt>` | 1857 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>などという人の</src><tgt><\|wait\|></tgt>` | 1555 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>絵は</src><tgt><\|wait\|></tgt>` | 1444 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>田舎の</src><tgt><\|wait\|></tgt>` | 1461 |

---

### Test Example 13 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단에 있는 </src><tgt><\|wait\|></tgt>` | 1210 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>육성들은 </src><tgt><\|wait\|></tgt>` | 905 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 957 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능이 높지 </src><tgt><\|wait\|></tgt>` | 1475 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1518 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1764 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>사람들이 </src><tgt><\|wait\|></tgt>` | 1711 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었기 때문입니다. </src><tgt><\|wait\|></tgt>` | 1897 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>사람들입니다. </src><tgt><\|wait\|></tgt>` | 1547 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실을 </src><tgt><\|wait\|></tgt>` | 1516 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 </src><tgt><\|wait\|></tgt>` | 1506 |

---

### Test Example 14 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 674 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我的</src><tgt><\|wait\|></tgt>` | 865 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1052 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>鬼岛，让我</src><tgt><\|wait\|></tgt>` | 1446 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>能够享受它</src><tgt><\|wait\|></tgt>` | 1564 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>下的</src><tgt><\|wait\|></tgt>` | 1448 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>时间，在</src><tgt><\|wait\|></tgt>` | 492 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>这个日子</src><tgt><\|wait\|></tgt>` | 1725 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>过去，我当时</src><tgt><\|wait\|></tgt>` | 1845 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>被一招</src><tgt><\|wait\|></tgt>` | 1470 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>小小的诱惑</src><tgt><\|wait\|></tgt>` | 1757 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1484 |

---

### Test Example 15 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 838 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>saying, </src><tgt><\|wait\|></tgt>` | 867 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1120 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 1316 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>attention start? </src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>What is it? Is it a </src><tgt><\|wait\|></tgt>` | 1742 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>day? </src><tgt><\|wait\|></tgt>` | 1701 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it time is in your chest? </src><tgt><\|wait\|></tgt>` | 2046 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>I have a sob, </src><tgt><\|wait\|></tgt>` | 1546 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>lament which are you used </src><tgt><\|wait\|></tgt>` | 1802 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>saying. </src><tgt><\|wait\|></tgt>` | 1471 |

---

### Test Example 16 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 854 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>먼지레 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 948 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>해 가지고 내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1225 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>아스다. 다른 </src><tgt><\|wait\|></tgt>` | 1542 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>잔 때문에 </src><tgt><\|wait\|></tgt>` | 1648 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>달래 자라. 내가 </src><tgt><\|wait\|></tgt>` | 1914 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그런 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 2011 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>중요한 게 </src><tgt><\|wait\|></tgt>` | 1429 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1930 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1367 |

---

### Test Example 17 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 822 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>A E E が</src><tgt><\|wait\|></tgt>` | 934 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>あんてですね。いる</src><tgt><\|wait\|></tgt>` | 1156 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>な場面で</src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>清掃活動</src><tgt><\|wait\|></tgt>` | 1484 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>行う時に</src><tgt><\|wait\|></tgt>` | 1583 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>A E の</src><tgt><\|wait\|></tgt>` | 1553 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>欄を調べたことで、</src><tgt><\|wait\|></tgt>` | 1782 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>あの清掃活動</src><tgt><\|wait\|></tgt>` | 1413 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>を保証する</src><tgt><\|wait\|></tgt>` | 731 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>清掃で</src><tgt><\|wait\|></tgt>` | 1896 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方も</src><tgt><\|wait\|></tgt>` | 1405 |

---

### Test Example 18 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1068 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>lastly, </src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat, </src><tgt><\|wait\|></tgt>` | 1087 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>learners to repeat </src><tgt><\|wait\|></tgt>` | 1436 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>find you're good at </src><tgt><\|wait\|></tgt>` | 1620 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1706 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good at </src><tgt><\|wait\|></tgt>` | 1895 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>ya, get to people </src><tgt><\|wait\|></tgt>` | 1959 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1498 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1793 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>tell next time, </src><tgt><\|wait\|></tgt>` | 1530 |

---

### Test Example 19 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 738 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 860 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1190 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有这种</src><tgt><\|wait\|></tgt>` | 1348 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>某种人性</src><tgt><\|wait\|></tgt>` | 1568 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 1614 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>从那天</src><tgt><\|wait\|></tgt>` | 1586 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>夜里开始的</src><tgt><\|wait\|></tgt>` | 1810 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1618 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 794 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思欲</src><tgt><\|wait\|></tgt>` | 1820 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>连篇</src><tgt><\|wait\|></tgt>` | 1428 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 956 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>以为</src><tgt><\|wait\|></tgt>` | 796 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1056 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src>我</src><tgt><\|wait\|></tgt>` | 1385 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>可以坚持</src><tgt><\|wait\|></tgt>` | 1393 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>打开，</src><tgt><\|wait\|></tgt>` | 613 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>期限大概</src><tgt><\|wait\|></tgt>` | 1397 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>有准医生来</src><tgt><\|wait\|></tgt>` | 1739 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>审段，</src><tgt><\|wait\|></tgt>` | 1738 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下</src><tgt><\|wait\|></tgt>` | 1553 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>提腿</src><tgt><\|wait\|></tgt>` | 1208 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1392 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>他们都可以</src><tgt><\|wait\|></tgt>` | 1406 |

---

### Test Example 21 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Chun-Hwa-Teroo. Hi, </src><tgt><\|wait\|></tgt>` | 1584 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I'm currently studying </src><tgt><\|wait\|></tgt>` | 524 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a BA in </src><tgt><\|wait\|></tgt>` | 1184 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance and a </src><tgt><\|wait\|></tgt>` | 1597 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>major of psychology. </src><tgt><\|wait\|></tgt>` | 1628 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1641 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 1741 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>you're in </src><tgt><\|wait\|></tgt>` | 1587 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>the future, </src><tgt><\|wait\|></tgt>` | 1276 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I want to go into corporate </src><tgt><\|wait\|></tgt>` | 1518 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1426 |

---

### Test Example 22 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber</src><tgt><\|wait\|></tgt>` | 899 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>band, chemical</src><tgt><\|wait\|></tgt>` | 810 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>bands also store</src><tgt><\|wait\|></tgt>` | 1045 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. And when those</src><tgt><\|wait\|></tgt>` | 1513 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>bands are broken,</src><tgt><\|wait\|></tgt>` | 1539 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy gets</src><tgt><\|wait\|></tgt>` | 1705 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other</src><tgt><\|wait\|></tgt>` | 1723 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, like</src><tgt><\|wait\|></tgt>` | 1839 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light.</src><tgt><\|wait\|></tgt>` | 1553 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets you</src><tgt><\|wait\|></tgt>` | 1392 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make different bonds</src><tgt><\|wait\|></tgt>` | 1474 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |

---

### Test Example 23 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1184 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 862 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 1108 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>uh </src><tgt><\|wait\|></tgt>` | 1360 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1529 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tell us to use </src><tgt><\|wait\|></tgt>` | 1584 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1415 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 659 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 1769 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>values. So </src><tgt><\|wait\|></tgt>` | 1530 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>game.dot </src><tgt><\|wait\|></tgt>` | 1452 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>board array. </src><tgt><\|wait\|></tgt>` | 1450 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1278 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1103 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>です。ギア</src><tgt><\|wait\|></tgt>` | 873 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1193 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 1383 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>のでギア</src><tgt><\|wait\|></tgt>` | 1585 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>の先に</src><tgt><\|wait\|></tgt>` | 1501 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1141 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが付いて</src><tgt><\|wait\|></tgt>` | 1291 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>いるっていうこと</src><tgt><\|wait\|></tgt>` | 1435 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1544 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1427 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイ分解</src><tgt><\|wait\|></tgt>` | 1154 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1156 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the nineteenth amendment </src><tgt><\|wait\|></tgt>` | 851 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 1031 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>to explore </src><tgt><\|wait\|></tgt>` | 1366 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1581 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help political </src><tgt><\|wait\|></tgt>` | 1480 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 486 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt><\|wait\|></tgt>` | 1751 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>United States. </src><tgt><\|wait\|></tgt>` | 1822 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 1465 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 1710 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>of the amendment, </src><tgt><\|wait\|></tgt>` | 1522 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>of course, I'm </src><tgt><\|wait\|></tgt>` | 1305 |

---

### Test Example 26 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 909 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこ で </src><tgt><\|wait\|></tgt>` | 812 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>てん けい </src><tgt><\|wait\|></tgt>` | 1201 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>と せる 7GB </src><tgt><\|wait\|></tgt>` | 1436 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>が あり まし た ね 。 </src><tgt><\|wait\|></tgt>` | 1538 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で </src><tgt><\|wait\|></tgt>` | 1551 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ハ セイ </src><tgt><\|wait\|></tgt>` | 1630 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>の 仕組み </src><tgt><\|wait\|></tgt>` | 1806 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は </src><tgt><\|wait\|></tgt>` | 1535 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 764 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ボコン </src><tgt><\|wait\|></tgt>` | 1693 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>7GB </src><tgt><\|wait\|></tgt>` | 1414 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>です 。 </src><tgt><\|wait\|></tgt>` | 1390 |

---

### Test Example 27 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 931 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 803 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>二季时，</src><tgt><\|wait\|></tgt>` | 1082 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会服</src><tgt><\|wait\|></tgt>` | 1401 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>在这一季</src><tgt><\|wait\|></tgt>` | 1564 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼大的牛们，</src><tgt><\|wait\|></tgt>` | 1640 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1593 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 1804 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>沟通好是几年，</src><tgt><\|wait\|></tgt>` | 1625 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 786 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信</src><tgt><\|wait\|></tgt>` | 1710 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>好拼分的</src><tgt><\|wait\|></tgt>` | 1459 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>心膀反而</src><tgt><\|wait\|></tgt>` | 1570 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라더니</src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>일거투는</src><tgt><\|wait\|></tgt>` | 939 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진</src><tgt><\|wait\|></tgt>` | 932 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>유니셜링과</src><tgt><\|wait\|></tgt>` | 1441 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>이거진 유산</src><tgt><\|wait\|></tgt>` | 1564 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>한 정도가</src><tgt><\|wait\|></tgt>` | 1641 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히</src><tgt><\|wait\|></tgt>` | 1587 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>아주 당분</src><tgt><\|wait\|></tgt>` | 1786 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>모니레라이다</src><tgt><\|wait\|></tgt>` | 1581 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>길게 갈 정도에</src><tgt><\|wait\|></tgt>` | 1363 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제</src><tgt><\|wait\|></tgt>` | 1399 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거에다가</src><tgt><\|wait\|></tgt>` | 1475 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아니면</src><tgt><\|wait\|></tgt>` | 1425 |

---

### Test Example 29 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 824 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>甜头，</src><tgt><\|wait\|></tgt>` | 912 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1009 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>得到了甜头之后</src><tgt><\|wait\|></tgt>` | 1422 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>亲你乌比</src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先</src><tgt><\|wait\|></tgt>` | 1509 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>手作，</src><tgt><\|wait\|></tgt>` | 531 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想，</src><tgt><\|wait\|></tgt>` | 1564 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我在去操作一下</src><tgt><\|wait\|></tgt>` | 1833 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>去哦。</src><tgt><\|wait\|></tgt>` | 1454 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1471 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1384 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢</src><tgt><\|wait\|></tgt>` | 1240 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src>呢</src><tgt><\|wait\|></tgt>` | 1403 |

---

### Test Example 30 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 1045 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在</src><tgt><\|wait\|></tgt>` | 795 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>这个罗马呢</src><tgt><\|wait\|></tgt>` | 1096 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是</src><tgt><\|wait\|></tgt>` | 1390 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>年前造成的</src><tgt><\|wait\|></tgt>` | 1569 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>所以呢</src><tgt><\|wait\|></tgt>` | 1463 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>现在</src><tgt><\|wait\|></tgt>` | 481 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>除了你的一些</src><tgt><\|wait\|></tgt>` | 1732 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>天气啊跟风水</src><tgt><\|wait\|></tgt>` | 1918 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也更不可能是</src><tgt><\|wait\|></tgt>` | 1540 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间就</src><tgt><\|wait\|></tgt>` | 1686 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 1513 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>的实例</src><tgt><\|wait\|></tgt>` | 1111 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>会建议</src><tgt><\|wait\|></tgt>` | 1331 |

---

### Test Example 31 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 782 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150원 계기가 </src><tgt><\|wait\|></tgt>` | 1164 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>중앙에 </src><tgt><\|wait\|></tgt>` | 849 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>중앙에 </src><tgt><\|wait\|></tgt>` | 1408 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>중소기업들이 </src><tgt><\|wait\|></tgt>` | 1584 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1610 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>일반적으로는 </src><tgt><\|wait\|></tgt>` | 1654 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>성장 하거나 </src><tgt><\|wait\|></tgt>` | 1809 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>혹은 해외 회계에 </src><tgt><\|wait\|></tgt>` | 1771 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>거의 적게 되는데 </src><tgt><\|wait\|></tgt>` | 1703 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>해외 송기 없으면 </src><tgt><\|wait\|></tgt>` | 1521 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>성장도 </src><tgt><\|wait\|></tgt>` | 1138 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>폐업 하지 않는 현상들이 </src><tgt><\|wait\|></tgt>` | 1621 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src>帝王的</src><tgt><\|wait\|></tgt>` | 753 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>部分我们</src><tgt><\|wait\|></tgt>` | 857 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>开看到的是</src><tgt><\|wait\|></tgt>` | 1047 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>个戴庙的人，但是</src><tgt><\|wait\|></tgt>` | 1560 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>他是属于</src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src>这一通场</src><tgt><\|wait\|></tgt>` | 1609 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>场怎么样</src><tgt><\|wait\|></tgt>` | 1546 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>这样一个状况</src><tgt><\|wait\|></tgt>` | 1772 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>就特别注意是</src><tgt><\|wait\|></tgt>` | 1633 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 641 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到与他</src><tgt><\|wait\|></tgt>` | 1824 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>掉不到与他</src><tgt><\|wait\|></tgt>` | 1525 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的意事</src><tgt><\|wait\|></tgt>` | 1340 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1004 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 948 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>if you have to produce </src><tgt><\|wait\|></tgt>` | 1061 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 963 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1386 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1563 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1692 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1870 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>which is like, </src><tgt><\|wait\|></tgt>` | 1848 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>oh, is this word </src><tgt><\|wait\|></tgt>` | 1614 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a double P? </src><tgt><\|wait\|></tgt>` | 1789 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1468 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>Double M? I don't know. </src><tgt><\|wait\|></tgt>` | 1582 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1009 |

---

### Test Example 34 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 811 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>eighty-</src><tgt><\|wait\|></tgt>` | 863 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>seven-mile-one, </src><tgt><\|wait\|></tgt>` | 1227 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>which is also </src><tgt><\|wait\|></tgt>` | 1320 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a mile, </src><tgt><\|wait\|></tgt>` | 1537 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>and a mile, </src><tgt><\|wait\|></tgt>` | 1571 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and a mile, </src><tgt><\|wait\|></tgt>` | 1691 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>the computer </src><tgt><\|wait\|></tgt>` | 1756 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>of the </src><tgt><\|wait\|></tgt>` | 1570 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>computer, </src><tgt><\|wait\|></tgt>` | 926 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>we have to write </src><tgt><\|wait\|></tgt>` | 1660 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1359 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>computer, </src><tgt><\|wait\|></tgt>` | 1331 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 984 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>program. </src><tgt><\|wait\|></tgt>` | 1003 |

---

### Test Example 35 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>村せてやる</src><tgt><\|wait\|></tgt>` | 825 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>あれ</src><tgt><\|wait\|></tgt>` | 1010 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1138 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>ひき手</src><tgt><\|wait\|></tgt>` | 620 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よ見てる</src><tgt><\|wait\|></tgt>` | 1412 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1553 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1532 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不れる不気味</src><tgt><\|wait\|></tgt>` | 1760 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>う</src><tgt><\|wait\|></tgt>` | 613 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長根のデイコウやってる</src><tgt><\|wait\|></tgt>` | 1943 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>な</src><tgt><\|wait\|></tgt>` | 1413 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>もうこれこんなに</src><tgt><\|wait\|></tgt>` | 1347 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい快族線を見た</src><tgt><\|wait\|></tgt>` | 1278 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>ことがない</src><tgt><\|wait\|></tgt>` | 1040 |

---

### Test Example 36 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 956 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手</src><tgt><\|wait\|></tgt>` | 871 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>手とか</src><tgt><\|wait\|></tgt>` | 1036 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>手とか</src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1362 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 699 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>1秒に</src><tgt><\|wait\|></tgt>` | 1366 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>約</src><tgt><\|wait\|></tgt>` | 1606 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>1秒間</src><tgt><\|wait\|></tgt>` | 1754 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1566 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>なんか</src><tgt><\|wait\|></tgt>` | 1162 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1451 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>12日で</src><tgt><\|wait\|></tgt>` | 1428 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1419 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 828 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 1006 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 986 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>觉得餐饮可以</src><tgt><\|wait\|></tgt>` | 914 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>说吃很不错，但是</src><tgt><\|wait\|></tgt>` | 1127 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较讲正菜的部分</src><tgt><\|wait\|></tgt>` | 1345 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 1468 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>在西餐方面的</src><tgt><\|wait\|></tgt>` | 1632 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩增长</src><tgt><\|wait\|></tgt>` | 1614 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>所带来的</src><tgt><\|wait\|></tgt>` | 1745 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>收入的提升，</src><tgt><\|wait\|></tgt>` | 1622 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>如果是在投资领域</src><tgt><\|wait\|></tgt>` | 978 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这一方面，</src><tgt><\|wait\|></tgt>` | 1617 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>这个月也是不错，</src><tgt><\|wait\|></tgt>` | 1553 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>只是相对来说</src><tgt><\|wait\|></tgt>` | 1498 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>觉得</src><tgt><\|wait\|></tgt>` | 738 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>做了那么一点点</src><tgt><\|wait\|></tgt>` | 1014 |

---

### Test Example 38 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1195 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 빌 </src><tgt><\|wait\|></tgt>` | 859 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>거야. </src><tgt><\|wait\|></tgt>` | 1054 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 소름이 돋는 </src><tgt><\|wait\|></tgt>` | 1518 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>그 차리 돋는 </src><tgt><\|wait\|></tgt>` | 1520 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>게 마음이야. </src><tgt><\|wait\|></tgt>` | 1567 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>이걸 흔들어서 </src><tgt><\|wait\|></tgt>` | 1536 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1590 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 805 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>오물리 꼴리고 </src><tgt><\|wait\|></tgt>` | 1554 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>기신이 오물리 꼴리고 </src><tgt><\|wait\|></tgt>` | 2028 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>지치라고 </src><tgt><\|wait\|></tgt>` | 1488 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>지르라고 지르라고 지르라고 지르라고 </src><tgt><\|wait\|></tgt>` | 1837 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 755 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>판만 봐. </src><tgt><\|wait\|></tgt>` | 844 |

---

### Test Example 39 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>there's </src><tgt><\|wait\|></tgt>` | 908 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>such </src><tgt><\|wait\|></tgt>` | 924 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>instances before. </src><tgt><\|wait\|></tgt>` | 1396 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1611 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>Net Future TC. </src><tgt><\|wait\|></tgt>` | 1716 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1606 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>this is just </src><tgt><\|wait\|></tgt>` | 1745 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>one another place. </src><tgt><\|wait\|></tgt>` | 1591 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>Look at </src><tgt><\|wait\|></tgt>` | 1096 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 1471 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>devoted </src><tgt><\|wait\|></tgt>` | 1389 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1528 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>who know </src><tgt><\|wait\|></tgt>` | 813 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>bagreposh should be aware of that. </src><tgt><\|wait\|></tgt>` | 1139 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>또 이도 </src><tgt><\|wait\|></tgt>` | 842 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알고 있나요? </src><tgt><\|wait\|></tgt>` | 1047 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1041 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1336 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src>말 못 하는 </src><tgt><\|wait\|></tgt>` | 1496 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>무상에게로 </src><tgt><\|wait\|></tgt>` | 1720 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>이 되는 그대로 </src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 1781 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1538 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 1371 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>너 의에게 </src><tgt><\|wait\|></tgt>` | 1405 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1389 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나 님의 영어 로 </src><tgt><\|wait\|></tgt>` | 1499 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자 는 </src><tgt><\|wait\|></tgt>` | 887 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 764 |

---

### Test Example 41 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 1074 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 858 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1057 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>20대들을 </src><tgt><\|wait\|></tgt>` | 1361 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1217 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 681 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>그렇다고 </src><tgt><\|wait\|></tgt>` | 1537 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1887 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1820 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>어, 제인 거 보다는 </src><tgt><\|wait\|></tgt>` | 1619 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 자기 스스로 </src><tgt><\|wait\|></tgt>` | 1738 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>수술을 </src><tgt><\|wait\|></tgt>` | 1507 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1072 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거. </src><tgt><\|wait\|></tgt>` | 1336 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>넣고. </src><tgt><\|wait\|></tgt>` | 615 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 848 |

---

### Test Example 42 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>で、これはですね、</src><tgt><\|wait\|></tgt>` | 1161 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1045 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていう開発環境</src><tgt><\|wait\|></tgt>` | 849 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、ビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1436 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>なんです。で、</src><tgt><\|wait\|></tgt>` | 1549 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1524 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフでビジュアルを</src><tgt><\|wait\|></tgt>` | 1581 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとは</src><tgt><\|wait\|></tgt>` | 1761 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード</src><tgt><\|wait\|></tgt>` | 1488 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>を生成する。それが</src><tgt><\|wait\|></tgt>` | 651 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1856 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理を</src><tgt><\|wait\|></tgt>` | 1473 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>行うという</src><tgt><\|wait\|></tgt>` | 1374 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ところになっているから</src><tgt><\|wait\|></tgt>` | 1118 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 1026 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 752 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational</src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>engagement. How far</src><tgt><\|wait\|></tgt>` | 883 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually</src><tgt><\|wait\|></tgt>` | 1109 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your</src><tgt><\|wait\|></tgt>` | 1511 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>education? Did you graduate</src><tgt><\|wait\|></tgt>` | 1596 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>from high school?</src><tgt><\|wait\|></tgt>` | 1617 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of</src><tgt><\|wait\|></tgt>` | 1894 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>engagement. Did you</src><tgt><\|wait\|></tgt>` | 1840 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>go to college, and</src><tgt><\|wait\|></tgt>` | 1511 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>so did you graduate?</src><tgt><\|wait\|></tgt>` | 1603 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of</src><tgt><\|wait\|></tgt>` | 1604 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>engagement.</src><tgt><\|wait\|></tgt>` | 1005 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it for now.</src><tgt><\|wait\|></tgt>` | 1740 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>I'll see you</src><tgt><\|wait\|></tgt>` | 1061 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online.</src><tgt><\|wait\|></tgt>` | 743 |

---

### Test Example 44 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>드러가면 </src><tgt><\|wait\|></tgt>` | 1234 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 헤맨니다. </src><tgt><\|wait\|></tgt>` | 1225 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>아예 운전 을 </src><tgt><\|wait\|></tgt>` | 809 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>거로 </src><tgt><\|wait\|></tgt>` | 1318 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>거로 다니고 </src><tgt><\|wait\|></tgt>` | 1504 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>가는 에 뭐 </src><tgt><\|wait\|></tgt>` | 1579 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>강북으로 가면 </src><tgt><\|wait\|></tgt>` | 1526 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>말 할 것 또 </src><tgt><\|wait\|></tgt>` | 1343 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가도 </src><tgt><\|wait\|></tgt>` | 1186 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장려 리요. </src><tgt><\|wait\|></tgt>` | 1447 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1674 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>괜히 에요. </src><tgt><\|wait\|></tgt>` | 1537 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1380 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1216 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>노발요. </src><tgt><\|wait\|></tgt>` | 1041 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그거는 </src><tgt><\|wait\|></tgt>` | 778 |

---

### Test Example 45 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 986 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 801 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>针对</src><tgt><\|wait\|></tgt>` | 1063 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>对手的</src><tgt><\|wait\|></tgt>` | 1068 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 677 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>攻击</src><tgt><\|wait\|></tgt>` | 1389 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 1593 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>经常会</src><tgt><\|wait\|></tgt>` | 1530 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>对人们</src><tgt><\|wait\|></tgt>` | 1323 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>这样说吧，你们看。</src><tgt><\|wait\|></tgt>` | 1283 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人又</src><tgt><\|wait\|></tgt>` | 1210 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>在躲黄了。</src><tgt><\|wait\|></tgt>` | 1775 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1465 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 1192 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1515 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 1047 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 783 |

---

### Test Example 46 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who is</src><tgt><\|wait\|></tgt>` | 1201 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>getting going needs</src><tgt><\|wait\|></tgt>` | 855 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>to get</src><tgt><\|wait\|></tgt>` | 950 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1494 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and a ten of them that</src><tgt><\|wait\|></tgt>` | 1627 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>you're really important</src><tgt><\|wait\|></tgt>` | 1642 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1835 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to</src><tgt><\|wait\|></tgt>` | 1775 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>um, I'm going to go and do</src><tgt><\|wait\|></tgt>` | 1721 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one</src><tgt><\|wait\|></tgt>` | 2014 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>video, it's</src><tgt><\|wait\|></tgt>` | 1534 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>all this video</src><tgt><\|wait\|></tgt>` | 1551 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one, </src><tgt><\|wait\|></tgt>` | 777 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>and a little more</src><tgt><\|wait\|></tgt>` | 1042 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, but</src><tgt><\|wait\|></tgt>` | 758 |

---

### Test Example 47 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Ah, </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>activity, then </src><tgt><\|wait\|></tgt>` | 850 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>self-defining </src><tgt><\|wait\|></tgt>` | 1060 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>what we think </src><tgt><\|wait\|></tgt>` | 1419 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>standard is because </src><tgt><\|wait\|></tgt>` | 1559 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src>you're absolutely correct, </src><tgt><\|wait\|></tgt>` | 1648 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1547 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1760 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>we're the new kid block, and because </src><tgt><\|wait\|></tgt>` | 1696 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have changed, </src><tgt><\|wait\|></tgt>` | 1035 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>since 2020. </src><tgt><\|wait\|></tgt>` | 1776 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>We're </src><tgt><\|wait\|></tgt>` | 1392 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>being held to </src><tgt><\|wait\|></tgt>` | 1491 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>our standard because </src><tgt><\|wait\|></tgt>` | 784 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>everything at this point </src><tgt><\|wait\|></tgt>` | 931 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is a higher standard, </src><tgt><\|wait\|></tgt>` | 770 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>축가 절수가 </src><tgt><\|wait\|></tgt>` | 1020 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승하는 </src><tgt><\|wait\|></tgt>` | 861 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>그름을 보인 다음에 </src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이러한 </src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>대형주도 </src><tgt><\|wait\|></tgt>` | 1515 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1792 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>어 먼저 </src><tgt><\|wait\|></tgt>` | 1671 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt><\|wait\|></tgt>` | 2021 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt><\|wait\|></tgt>` | 1409 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장을 </src><tgt><\|wait\|></tgt>` | 1509 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도하면서 움직이기 때문에 </src><tgt><\|wait\|></tgt>` | 1590 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1130 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>주식 초기에 </src><tgt><\|wait\|></tgt>` | 1401 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목을 </src><tgt><\|wait\|></tgt>` | 964 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>어 눈여겨 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 937 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 499 |

---

### Test Example 49 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계소 </src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 이런 경우들로 </src><tgt><\|wait\|></tgt>` | 957 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1112 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>저희 A라는 사람과 </src><tgt><\|wait\|></tgt>` | 1453 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>기란 사람이 </src><tgt><\|wait\|></tgt>` | 1520 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 </src><tgt><\|wait\|></tgt>` | 1575 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요. </src><tgt><\|wait\|></tgt>` | 1854 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>그리고 A라는 </src><tgt><\|wait\|></tgt>` | 1770 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>사람이 </src><tgt><\|wait\|></tgt>` | 1532 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드를 </src><tgt><\|wait\|></tgt>` | 1453 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>설쳤을 때 </src><tgt><\|wait\|></tgt>` | 1462 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt><\|wait\|></tgt>` | 1312 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실패를 </src><tgt><\|wait\|></tgt>` | 1407 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로사이트스 T에서 </src><tgt><\|wait\|></tgt>` | 1054 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>엑스파이까지 </src><tgt><\|wait\|></tgt>` | 816 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염이 될까? </src><tgt><\|wait\|></tgt>` | 804 |

---

### Test Example 50 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 855 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 752 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>subtle suggestion </src><tgt><\|wait\|></tgt>` | 1109 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 1329 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>we all </src><tgt><\|wait\|></tgt>` | 1581 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>have a tendency to </src><tgt><\|wait\|></tgt>` | 1416 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>love each other, </src><tgt><\|wait\|></tgt>` | 550 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src>but we also </src><tgt><\|wait\|></tgt>` | 1735 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>tend to enter into </src><tgt><\|wait\|></tgt>` | 1822 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a relationship </src><tgt><\|wait\|></tgt>` | 1419 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>that is </src><tgt><\|wait\|></tgt>` | 1320 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>the time we love </src><tgt><\|wait\|></tgt>` | 1465 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>each other. </src><tgt><\|wait\|></tgt>` | 1360 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>Then it becomes </src><tgt><\|wait\|></tgt>` | 1407 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 710 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 869 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 746 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>will continue to </src><tgt><\|wait\|></tgt>` | 629 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 805 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>말하는 사람들이 </src><tgt><\|wait\|></tgt>` | 918 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1114 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 1346 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>이 로쿠자열 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1690 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>손이가 </src><tgt><\|wait\|></tgt>` | 1510 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>유리 룩트 에 에프피 파이프 </src><tgt><\|wait\|></tgt>` | 2011 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>를 </src><tgt><\|wait\|></tgt>` | 1720 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128 비트 로 </src><tgt><\|wait\|></tgt>` | 1613 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나치 로 포인트 </src><tgt><\|wait\|></tgt>` | 1988 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>한다. </src><tgt><\|wait\|></tgt>` | 1406 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈 </src><tgt><\|wait\|></tgt>` | 1576 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>에서도 없는 </src><tgt><\|wait\|></tgt>` | 880 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1116 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>에스이도 </src><tgt><\|wait\|></tgt>` | 764 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>없다. </src><tgt><\|wait\|></tgt>` | 600 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 951 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 1028 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1052 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1488 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1552 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src>though if </src><tgt><\|wait\|></tgt>` | 585 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into a situation </src><tgt><\|wait\|></tgt>` | 1517 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>where you </src><tgt><\|wait\|></tgt>` | 1741 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1580 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 1683 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 1460 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>to put in the list. Now, </src><tgt><\|wait\|></tgt>` | 1332 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1484 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 1063 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 774 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>to get backed up </src><tgt><\|wait\|></tgt>` | 632 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt><\|wait\|></tgt>` | 541 |

---

### Test Example 53 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 882 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>knows Jesus </src><tgt><\|wait\|></tgt>` | 874 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1033 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1377 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1525 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>for he's been </src><tgt><\|wait\|></tgt>` | 1618 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 1629 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>and is hungry. And so </src><tgt><\|wait\|></tgt>` | 1856 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>he says, "If </src><tgt><\|wait\|></tgt>` | 1637 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>the Son of God </src><tgt><\|wait\|></tgt>` | 1292 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>proved, turn </src><tgt><\|wait\|></tgt>` | 1408 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 1482 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did </src><tgt><\|wait\|></tgt>` | 1410 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>Jesus deal with that? </src><tgt><\|wait\|></tgt>` | 986 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 763 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 723 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>genuinely </src><tgt><\|wait\|></tgt>` | 616 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>led by </src><tgt><\|wait\|></tgt>` | 518 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1339 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in here for a mile on the first </src><tgt><\|wait\|></tgt>` | 1409 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>section about </src><tgt><\|wait\|></tgt>` | 498 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1306 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1569 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1556 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>importance versus </src><tgt><\|wait\|></tgt>` | 874 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1052 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 1651 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt><\|wait\|></tgt>` | 1556 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1290 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1474 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1486 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 1422 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1122 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 671 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from. </src><tgt><\|wait\|></tgt>` | 903 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, </src><tgt><\|wait\|></tgt>` | 445 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>right? </src><tgt><\|wait\|></tgt>` | 480 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>individual </src><tgt><\|wait\|></tgt>` | 794 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>right, and </src><tgt><\|wait\|></tgt>` | 1095 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>Supreme Court </src><tgt><\|wait\|></tgt>` | 1073 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 681 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And </src><tgt><\|wait\|></tgt>` | 1403 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>I thought the courts </src><tgt><\|wait\|></tgt>` | 1571 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>want to be the </src><tgt><\|wait\|></tgt>` | 1669 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>vanard of social change, </src><tgt><\|wait\|></tgt>` | 1895 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>uh </src><tgt><\|wait\|></tgt>` | 1544 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 1278 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they </src><tgt><\|wait\|></tgt>` | 1444 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src>rather reflect </src><tgt><\|wait\|></tgt>` | 1430 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1428 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 867 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 849 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 758 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>you have </src><tgt><\|wait\|></tgt>` | 595 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 521 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 330 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 347 |

---

### Test Example 56 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>T-shirts, and so on, </src><tgt><\|wait\|></tgt>` | 1389 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>that, </src><tgt><\|wait\|></tgt>` | 587 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>you know, </src><tgt><\|wait\|></tgt>` | 1055 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>you'll need to have ready, </src><tgt><\|wait\|></tgt>` | 1546 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>so that you can easily </src><tgt><\|wait\|></tgt>` | 1533 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>do that, so please </src><tgt><\|wait\|></tgt>` | 1634 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>do that. </src><tgt><\|wait\|></tgt>` | 1636 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>As a contact, </src><tgt><\|wait\|></tgt>` | 1811 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>we've been, </src><tgt><\|wait\|></tgt>` | 1715 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>for example, </src><tgt><\|wait\|></tgt>` | 1437 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>we have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who have a lot of people who` | 8265 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>so please wait for a moment. </src><tgt><\|wait\|></tgt>` | 385 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 954 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1051 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1557 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客听的部分，</src><tgt><\|wait\|></tgt>` | 1680 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>客听一般</src><tgt><\|wait\|></tgt>` | 1717 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 1667 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src>我们再</src><tgt><\|wait\|></tgt>` | 1547 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt><\|wait\|></tgt>` | 1181 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1451 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分。</src><tgt><\|wait\|></tgt>` | 1465 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>它会反映的是</src><tgt><\|wait\|></tgt>` | 1547 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>需要给</src><tgt><\|wait\|></tgt>` | 758 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 956 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地做。</src><tgt><\|wait\|></tgt>` | 794 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>下来休息，</src><tgt><\|wait\|></tgt>` | 616 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可我们看到这边是</src><tgt><\|wait\|></tgt>` | 529 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>双人吗？</src><tgt><\|wait\|></tgt>` | 388 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，所以</src><tgt><\|wait\|></tgt>` | 382 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>是说</src><tgt><\|wait\|></tgt>` | 352 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 831 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 853 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1051 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1426 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize </src><tgt><\|wait\|></tgt>` | 1554 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1570 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1535 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 943 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>of a contradiction. </src><tgt><\|wait\|></tgt>` | 1571 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 1352 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>they're extroverted, </src><tgt><\|wait\|></tgt>` | 1735 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>they also </src><tgt><\|wait\|></tgt>` | 1389 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1076 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 1409 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 649 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it gets straight to the </src><tgt><\|wait\|></tgt>` | 928 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 772 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 538 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>to play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 639 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 261 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 375 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 377 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Ean </src><tgt><\|wait\|></tgt>` | 292 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>TP stands </src><tgt><\|wait\|></tgt>` | 298 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>for </src><tgt><\|wait\|></tgt>` | 314 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전의 이준석은</src><tgt><\|wait\|></tgt>` | 1240 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 601 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>정무를 거부한 명분</src><tgt><\|wait\|></tgt>` | 1123 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>이후를 위해서 하면서</src><tgt><\|wait\|></tgt>` | 1347 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후후의 당수를 위해서</src><tgt><\|wait\|></tgt>` | 1589 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>하면서</src><tgt><\|wait\|></tgt>` | 1509 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 냈지만</src><tgt><\|wait\|></tgt>` | 1850 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>이제는</src><tgt><\|wait\|></tgt>` | 1680 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보가</src><tgt><\|wait\|></tgt>` | 1683 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김치를 제관 순간</src><tgt><\|wait\|></tgt>` | 1455 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>이준석</src><tgt><\|wait\|></tgt>` | 1426 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>드러내 놓고</src><tgt><\|wait\|></tgt>` | 1285 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보</src><tgt><\|wait\|></tgt>` | 1471 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는</src><tgt><\|wait\|></tgt>` | 985 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼를 품은</src><tgt><\|wait\|></tgt>` | 802 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격성을</src><tgt><\|wait\|></tgt>` | 678 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이기로</src><tgt><\|wait\|></tgt>` | 486 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 것</src><tgt><\|wait\|></tgt>` | 533 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>입니다.</src><tgt><\|wait\|></tgt>` | 324 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>김세발 이준석</src><tgt><\|wait\|></tgt>` | 388 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>청산 납권</src><tgt><\|wait\|></tgt>` | 361 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 321 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이</src><tgt><\|wait\|></tgt>` | 337 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격에 얼마나</src><tgt><\|wait\|></tgt>` | 334 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>큰 호재 됩니까?</src><tgt><\|wait\|></tgt>` | 340 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 797 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいです。</src><tgt><\|wait\|></tgt>` | 1122 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1135 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 620 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ホテル</src><tgt><\|wait\|></tgt>` | 1361 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>の朝食が</src><tgt><\|wait\|></tgt>` | 1664 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所になってる</src><tgt><\|wait\|></tgt>` | 1756 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になってる</src><tgt><\|wait\|></tgt>` | 1704 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1512 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1168 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>このドストンホテル</src><tgt><\|wait\|></tgt>` | 1522 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>泊まってみたい方</src><tgt><\|wait\|></tgt>` | 1439 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>はですね</src><tgt><\|wait\|></tgt>` | 1461 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>この夏</src><tgt><\|wait\|></tgt>` | 738 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>いいじゃないか。</src><tgt><\|wait\|></tgt>` | 1031 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>と、はい、思います。</src><tgt><\|wait\|></tgt>` | 798 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>このホテルからですね</src><tgt><\|wait\|></tgt>` | 625 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>バス3駅も</src><tgt><\|wait\|></tgt>` | 572 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 314 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>1分かかるか</src><tgt><\|wait\|></tgt>` | 388 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かからないか</src><tgt><\|wait\|></tgt>` | 351 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなね、立地の</src><tgt><\|wait\|></tgt>` | 332 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>いいね、まあ</src><tgt><\|wait\|></tgt>` | 309 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | 356 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 286 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 206 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。</src><tgt><\|wait\|></tgt>` | 187 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>それでは</src><tgt><\|wait\|></tgt>` | 175 |
