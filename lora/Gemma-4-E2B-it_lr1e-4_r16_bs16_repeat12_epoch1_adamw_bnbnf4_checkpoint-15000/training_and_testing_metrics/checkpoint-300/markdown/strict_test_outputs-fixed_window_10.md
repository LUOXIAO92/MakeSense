# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9988
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9791
  - SRC_RELEASE_TOTAL: 717
  - SRC_WAIT_ACCURACY: 0.1192
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.0000
  - TGT_RELEASE_TOTAL: 63
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 805
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1222.0840
  - PROCESS_TIME_MS_P50: 1145.0050
  - PROCESS_TIME_MS_P95: 2007.4200
  - PROCESS_TIME_MS_MAX: 11613.0730

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>做的是</src><tgt><\|wait\|></tgt>` | 808 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 960 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>生生的爱胶水</src><tgt><\|wait\|></tgt>` | 1108 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 626 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>湿气</src><tgt><\|wait\|></tgt>` | 965 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>去阻止孩子</src><tgt><\|wait\|></tgt>` | 1725 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>心瘾</src><tgt><\|wait\|></tgt>` | 1181 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>影响</src><tgt><\|wait\|></tgt>` | 1313 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>你的孩子慢慢</src><tgt><\|wait\|></tgt>` | 1815 |
| 11 | `<src>慢慢长大。</src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment, and wait patiently for them to grow slowly.</tgt>` | `<src>长大。</src><tgt><\|wait\|></tgt>` | 744 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>的宿舍里，</src><tgt><\|wait\|></tgt>` | 822 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个房间</src><tgt><\|wait\|></tgt>` | 1001 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>要很大，</src><tgt><\|wait\|></tgt>` | 1084 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1191 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在</src><tgt><\|wait\|></tgt>` | 690 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>放假</src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>下课人。</src><tgt><\|wait\|></tgt>` | 1184 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>在宿舍里</src><tgt><\|wait\|></tgt>` | 1272 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 1838 |
| 11 | `<src>仁儿。</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels— this kind of walnut kernels.</tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 1319 |

---

### Test Example 3 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거</src><tgt><\|wait\|></tgt>` | 879 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이럴지</src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>너무</src><tgt><\|wait\|></tgt>` | 1005 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좋아요</src><tgt><\|wait\|></tgt>` | 988 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>근데</src><tgt><\|wait\|></tgt>` | 1350 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 거</src><tgt><\|wait\|></tgt>` | 1242 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>거린데</src><tgt><\|wait\|></tgt>` | 1468 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>꿈일 필요</src><tgt><\|wait\|></tgt>` | 1466 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>있고</src><tgt><\|wait\|></tgt>` | 719 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>나만</src><tgt><\|wait\|></tgt>` | 1615 |
| 11 | `<src>보살 이라는데. </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が今、私に菩薩だと言ってるんだから。</tgt>` | `<src>보살이</src><tgt><\|wait\|></tgt>` | 2005 |

---

### Test Example 4 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初</src><tgt><\|wait\|></tgt>` | 649 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 824 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>あの、特に</src><tgt><\|wait\|></tgt>` | 1000 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>中まだ1年生</src><tgt><\|wait\|></tgt>` | 1108 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>ですからね。はい、</src><tgt><\|wait\|></tgt>` | 1380 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>その時点で</src><tgt><\|wait\|></tgt>` | 1244 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>こう</src><tgt><\|wait\|></tgt>` | 1422 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>積極</src><tgt><\|wait\|></tgt>` | 1322 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>に</src><tgt><\|wait\|></tgt>` | 717 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>ついてをこう</src><tgt><\|wait\|></tgt>` | 1796 |
| 11 | `<src>大した。</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，十年后也不会有什么大……</tgt>` | `<src>耐述</src><tgt><\|wait\|></tgt>` | 2002 |

---

### Test Example 5 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>明天这个情况</src><tgt><\|wait\|></tgt>` | 863 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>我们就是</src><tgt><\|wait\|></tgt>` | 881 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1050 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就是感谢的</src><tgt><\|wait\|></tgt>` | 993 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>回报主管</src><tgt><\|wait\|></tgt>` | 1330 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>就是通知对方</src><tgt><\|wait\|></tgt>` | 1311 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>一下这个状况，</src><tgt><\|wait\|></tgt>` | 1387 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1463 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>怎么把它</src><tgt><\|wait\|></tgt>` | 941 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>扛下来，</src><tgt><\|wait\|></tgt>` | 1472 |
| 11 | `<src>事业运就属凶。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone. Overall, your career prospects are quite poor.</tgt>` | `<src>整天是</src><tgt><\|wait\|></tgt>` | 2519 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 933 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>봉심이 </src><tgt><\|wait\|></tgt>` | 908 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>아 칼 </src><tgt><\|wait\|></tgt>` | 1004 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>봉심이 칼 </src><tgt><\|wait\|></tgt>` | 1072 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>봉심이 가 </src><tgt><\|wait\|></tgt>` | 1483 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>석커 </src><tgt><\|wait\|></tgt>` | 1583 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>되는 건데요. </src><tgt><\|wait\|></tgt>` | 1272 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야 </src><tgt><\|wait\|></tgt>` | 1272 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>아 진짜 </src><tgt><\|wait\|></tgt>` | 1718 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>이게 </src><tgt><\|wait\|></tgt>` | 672 |
| 11 | `<src>진짜. </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is seriously killer for a hangover, for real.</tgt>` | `<src>형으로 </src><tgt><\|wait\|></tgt>` | 2518 |

---

### Test Example 7 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要</src><tgt><\|wait\|></tgt>` | 901 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>气守</src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>是容易的，但是</src><tgt><\|wait\|></tgt>` | 1350 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有</src><tgt><\|wait\|></tgt>` | 706 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 1357 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>师父</src><tgt><\|wait\|></tgt>` | 1473 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>只出于</src><tgt><\|wait\|></tgt>` | 1369 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>中见，所以</src><tgt><\|wait\|></tgt>` | 1497 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>师父还</src><tgt><\|wait\|></tgt>` | 1823 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 1088 |
| 11 | `<src>一个师父。</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは師匠になる必要があるのです。</tgt>` | `<src>师父。</src><tgt><\|wait\|></tgt>` | 2020 |

---

### Test Example 8 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>淘纱完以后</src><tgt><\|wait\|></tgt>` | 966 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>那内部的</src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>的液体检清</src><tgt><\|wait\|></tgt>` | 1137 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 911 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>刷了，然后就</src><tgt><\|wait\|></tgt>` | 1413 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>去填充在</src><tgt><\|wait\|></tgt>` | 1591 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1248 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的运行状态</src><tgt><\|wait\|></tgt>` | 1515 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>状态。</src><tgt><\|wait\|></tgt>` | 1822 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 1321 |
| 11 | `<src>抑郁状态。</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。これが、いわゆる抑うつ状態です。</tgt>` | `<src>的</src><tgt><\|wait\|></tgt>` | 1734 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 818 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 896 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>apple, </src><tgt><\|wait\|></tgt>` | 1075 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>축 썰기 고. </src><tgt><\|wait\|></tgt>` | 1147 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1372 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>자신의 모로 조깅 </src><tgt><\|wait\|></tgt>` | 2047 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>헤르나 </src><tgt><\|wait\|></tgt>` | 1423 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>박 </src><tgt><\|wait\|></tgt>` | 768 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>상과 </src><tgt><\|wait\|></tgt>` | 1828 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대들이 </src><tgt><\|wait\|></tgt>` | 1446 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents. They are the same generation as him.</tgt>` | `<src>있답니다. </src><tgt><\|wait\|></tgt>` | 1696 |

---

### Test Example 10 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying</src><tgt><\|wait\|></tgt>` | 795 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research</src><tgt><\|wait\|></tgt>` | 893 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on extremely happy</src><tgt><\|wait\|></tgt>` | 1028 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>people. This is</src><tgt><\|wait\|></tgt>` | 1048 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem, </src><tgt><\|wait\|></tgt>` | 1528 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking </src><tgt><\|wait\|></tgt>` | 1769 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>at 10% </src><tgt><\|wait\|></tgt>` | 1429 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt><\|wait\|></tgt>` | 1088 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people out </src><tgt><\|wait\|></tgt>` | 1782 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>there. People </src><tgt><\|wait\|></tgt>` | 1231 |
| 11 | `<src>people that we can learn from. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、彼らから学べることを探っています。</tgt>` | `<src>that we can learn from. </src><tgt><\|wait\|></tgt>` | 1994 |

---

### Test Example 11 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 785 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>あの、いただく</src><tgt><\|wait\|></tgt>` | 1053 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>というようなものも用意しております。</src><tgt><\|wait\|></tgt>` | 1149 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>のでぜひ</src><tgt><\|wait\|></tgt>` | 1318 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ご参加ください。</src><tgt><\|wait\|></tgt>` | 1395 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1289 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になります。</src><tgt><\|wait\|></tgt>` | 1470 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>えっと、</src><tgt><\|wait\|></tgt>` | 941 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>連絡</src><tgt><\|wait\|></tgt>` | 1336 |
| 11 | `<src>ランチの案内がありますので</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements, and we have some info about lunch,</tgt>` | `<src>の連絡網がありますので、</src><tgt><\|wait\|></tgt>` | 1929 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1259 |

---

### Test Example 12 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>待って、</src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>この辺りから</src><tgt><\|wait\|></tgt>` | 851 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めたもので</src><tgt><\|wait\|></tgt>` | 1014 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>ご</src><tgt><\|wait\|></tgt>` | 1006 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>方法</src><tgt><\|wait\|></tgt>` | 1216 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン</src><tgt><\|wait\|></tgt>` | 974 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1331 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ</src><tgt><\|wait\|></tgt>` | 1566 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナール</src><tgt><\|wait\|></tgt>` | 907 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>ナルトという人の</src><tgt><\|wait\|></tgt>` | 1895 |
| 11 | `<src>は、田舎の</src><tgt>大致是从这一带开始的，像梵高、高更、塞尚、雷诺阿他们的画，连乡下的</tgt>` | `<src>絵は</src><tgt><\|wait\|></tgt>` | 2194 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>田舎の</src><tgt><\|wait\|></tgt>` | 970 |

---

### Test Example 13 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단에 있는 </src><tgt><\|wait\|></tgt>` | 1100 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>육성들은 </src><tgt><\|wait\|></tgt>` | 901 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1048 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능이 높지 </src><tgt><\|wait\|></tgt>` | 1129 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1391 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 2130 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>사람들이 </src><tgt><\|wait\|></tgt>` | 1201 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>있었기 때문입니다. </src><tgt><\|wait\|></tgt>` | 1051 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1872 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사시를 </src><tgt><\|wait\|></tgt>` | 2348 |
| 11 | `<src>교사 들은. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random. The teachers, who didn't know the truth...</tgt>` | `<src>모을 랐던 </src><tgt><\|wait\|></tgt>` | 978 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 844 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>먼지레 죽여 달라고 </src><tgt><\|wait\|></tgt>` | 972 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해 가지고 내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 1511 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>내가 죽이 줘 </src><tgt><\|wait\|></tgt>` | 660 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>아스다. 다른 </src><tgt><\|wait\|></tgt>` | 1429 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>잔 때문에 </src><tgt><\|wait\|></tgt>` | 1712 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>달래 자라. 내가 </src><tgt><\|wait\|></tgt>` | 1579 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>죽은 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1141 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>중요한 게 </src><tgt><\|wait\|></tgt>` | 1868 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아. </src><tgt><\|wait\|></tgt>` | 2420 |
| 11 | `<src>내가 가. </src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room? Did you think I wasn't listening? Huh? I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 866 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>lastly, </src><tgt><\|wait\|></tgt>` | 838 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat, </src><tgt><\|wait\|></tgt>` | 1026 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>learners to repeat </src><tgt><\|wait\|></tgt>` | 1105 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>find out you're good at </src><tgt><\|wait\|></tgt>` | 1562 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 2040 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And well, you're not good </src><tgt><\|wait\|></tgt>` | 1674 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>yet, get to people </src><tgt><\|wait\|></tgt>` | 825 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1861 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 2432 |
| 11 | `<src>And until next time. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。下次再见。</tgt>` | `<src>tell next time, </src><tgt><\|wait\|></tgt>` | 1099 |

---

### Test Example 16 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 705 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>saying, </src><tgt><\|wait\|></tgt>` | 855 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>drop pin to your body. </src><tgt><\|wait\|></tgt>` | 1280 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>Where does </src><tgt><\|wait\|></tgt>` | 802 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>attention start? </src><tgt><\|wait\|></tgt>` | 1385 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>What is it? Is it a </src><tgt><\|wait\|></tgt>` | 1893 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>day? </src><tgt><\|wait\|></tgt>` | 1076 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it time is in your chest? </src><tgt><\|wait\|></tgt>` | 1521 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>I have a sob. </src><tgt><\|wait\|></tgt>` | 2013 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I think you are using </src><tgt><\|wait\|></tgt>` | 2456 |
| 11 | `<src>language are you using? </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，你在用什么语言？</tgt>` | `<src>singing. </src><tgt><\|wait\|></tgt>` | 1247 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>アドワンさん</src><tgt><\|wait\|></tgt>` | 1071 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 876 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>ような感じで</src><tgt><\|wait\|></tgt>` | 978 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>オーサーロカタが</src><tgt><\|wait\|></tgt>` | 1168 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>やっぱり多いですね。</src><tgt><\|wait\|></tgt>` | 1328 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | 1478 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ引っ越したい方</src><tgt><\|wait\|></tgt>` | 1469 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 1314 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>いいですね。</src><tgt><\|wait\|></tgt>` | 1448 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>でもっと本音で</src><tgt><\|wait\|></tgt>` | 871 |
| 11 | `<src>傾向が強いので、</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且倾向于自己全部投资，</tgt>` | `<src>喋る</src><tgt><\|wait\|></tgt>` | 2474 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>方が強いので</src><tgt><\|wait\|></tgt>` | 1409 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 727 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>在女高中生</src><tgt><\|wait\|></tgt>` | 960 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相不怪的人之间</src><tgt><\|wait\|></tgt>` | 1518 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>有这种</src><tgt><\|wait\|></tgt>` | 534 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>宝贝心</src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>系，难道</src><tgt><\|wait\|></tgt>` | 1540 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>会是</src><tgt><\|wait\|></tgt>` | 1309 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天</src><tgt><\|wait\|></tgt>` | 1428 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的。</src><tgt><\|wait\|></tgt>` | 1575 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 744 |
| 11 | `<src>杨子思绪</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night? Yang Zi's thoughts</tgt>` | `<src>杨子思</src><tgt><\|wait\|></tgt>` | 2594 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>说了两遍，</src><tgt><\|wait\|></tgt>` | 1343 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 644 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>回到我的</src><tgt><\|wait\|></tgt>` | 815 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>生活在一个</src><tgt><\|wait\|></tgt>` | 1001 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>鬼岛，让我</src><tgt><\|wait\|></tgt>` | 1123 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>能够享受它</src><tgt><\|wait\|></tgt>` | 1388 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>下的状态的时候，</src><tgt><\|wait\|></tgt>` | 1442 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在座日</src><tgt><\|wait\|></tgt>` | 1312 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>康乐园</src><tgt><\|wait\|></tgt>` | 1465 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的园，我当时</src><tgt><\|wait\|></tgt>` | 1647 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>被一招</src><tgt><\|wait\|></tgt>` | 741 |
| 11 | `<src>小小的愿望</src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저 그 작은 소망 하나뿐이었어요.</tgt>` | `<src>小小的诱惑</src><tgt><\|wait\|></tgt>` | 2635 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1321 |

---

### Test Example 20 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right, </src><tgt><\|wait\|></tgt>` | 1084 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>and then after </src><tgt><\|wait\|></tgt>` | 786 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>these examples, </src><tgt><\|wait\|></tgt>` | 985 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1074 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1039 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tell us to use </src><tgt><\|wait\|></tgt>` | 672 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1613 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1048 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 1385 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>values. So </src><tgt><\|wait\|></tgt>` | 1826 |
| 11 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们要使用这些值。也就是</tgt>` | `<src>game.dot </src><tgt><\|wait\|></tgt>` | 787 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>board array, </src><tgt><\|wait\|></tgt>` | 2379 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1287 |

---

### Test Example 21 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 794 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>A E E が</src><tgt><\|wait\|></tgt>` | 961 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>あんてですね。いる</src><tgt><\|wait\|></tgt>` | 1249 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>な場面で</src><tgt><\|wait\|></tgt>` | 857 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>清掃活動</src><tgt><\|wait\|></tgt>` | 1409 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>行う時に</src><tgt><\|wait\|></tgt>` | 1514 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>A E の</src><tgt><\|wait\|></tgt>` | 1254 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>欄を調べたことで</src><tgt><\|wait\|></tgt>` | 1518 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>清掃活動</src><tgt><\|wait\|></tgt>` | 1819 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>を清掃で</src><tgt><\|wait\|></tgt>` | 1321 |
| 11 | `<src>といったような</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>保証されていった</src><tgt><\|wait\|></tgt>` | 1827 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方を</src><tgt><\|wait\|></tgt>` | 1497 |

---

### Test Example 22 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber</src><tgt><\|wait\|></tgt>` | 821 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>band, chemical</src><tgt><\|wait\|></tgt>` | 815 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>bands also store</src><tgt><\|wait\|></tgt>` | 1060 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those</src><tgt><\|wait\|></tgt>` | 1073 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bands are broken,</src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy gets</src><tgt><\|wait\|></tgt>` | 1657 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>converted to other</src><tgt><\|wait\|></tgt>` | 1305 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>types of energy, like</src><tgt><\|wait\|></tgt>` | 1511 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>heat or light.</src><tgt><\|wait\|></tgt>` | 1793 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets you</src><tgt><\|wait\|></tgt>` | 1300 |
| 11 | `<src>or gets used to make </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다. 또는</tgt>` | `<src>to make different</src><tgt><\|wait\|></tgt>` | 1827 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>bands</src><tgt><\|wait\|></tgt>` | 1494 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name's </src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Chun-Hwa, and </src><tgt><\|wait\|></tgt>` | 905 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I'm currently studying </src><tgt><\|wait\|></tgt>` | 1313 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a BA in </src><tgt><\|wait\|></tgt>` | 775 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance, and </src><tgt><\|wait\|></tgt>` | 1467 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>a major of psychology. </src><tgt><\|wait\|></tgt>` | 1990 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1352 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>I hear </src><tgt><\|wait\|></tgt>` | 891 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>you're in </src><tgt><\|wait\|></tgt>` | 1906 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>the future, </src><tgt><\|wait\|></tgt>` | 1515 |
| 11 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을 밟고 있고요, 앞으로는</tgt>` | `<src>I want to go into corporate </src><tgt><\|wait\|></tgt>` | 1757 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>consultancy. </src><tgt><\|wait\|></tgt>` | 1413 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>以为</src><tgt><\|wait\|></tgt>` | 835 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1066 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>我</src><tgt><\|wait\|></tgt>` | 986 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>可以坚持</src><tgt><\|wait\|></tgt>` | 1352 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>打开，期限大概</src><tgt><\|wait\|></tgt>` | 1253 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十二生来</src><tgt><\|wait\|></tgt>` | 1468 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来选择，</src><tgt><\|wait\|></tgt>` | 1480 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下</src><tgt><\|wait\|></tgt>` | 758 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>敲腿、</src><tgt><\|wait\|></tgt>` | 1652 |
| 11 | `<src>都没有问题。</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>以下打腿</src><tgt><\|wait\|></tgt>` | 2473 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 1092 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>我都可以打开。</src><tgt><\|wait\|></tgt>` | 998 |

---

### Test Example 25 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1058 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the nineteenth amendment </src><tgt><\|wait\|></tgt>` | 909 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 963 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>to explore </src><tgt><\|wait\|></tgt>` | 1030 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1398 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to help </src><tgt><\|wait\|></tgt>` | 1442 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>political change </src><tgt><\|wait\|></tgt>` | 1321 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt><\|wait\|></tgt>` | 1456 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | 1615 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning </src><tgt><\|wait\|></tgt>` | 723 |
| 11 | `<src>The meanings </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>of the amendment </src><tgt><\|wait\|></tgt>` | 2483 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, </src><tgt><\|wait\|></tgt>` | 1237 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>of course, I'm </src><tgt><\|wait\|></tgt>` | 951 |

---

### Test Example 26 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これがギア</src><tgt><\|wait\|></tgt>` | 1055 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>です。ギア</src><tgt><\|wait\|></tgt>` | 816 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが緩むと</src><tgt><\|wait\|></tgt>` | 1182 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>信号が</src><tgt><\|wait\|></tgt>` | 964 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>消えなくなってしまう</src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>のでギア</src><tgt><\|wait\|></tgt>` | 1485 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>の先に</src><tgt><\|wait\|></tgt>` | 1305 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 1479 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが付いて</src><tgt><\|wait\|></tgt>` | 1617 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>いるっていうこと</src><tgt><\|wait\|></tgt>` | 785 |
| 11 | `<src>ね。</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가 달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 2449 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src>はい、</src><tgt><\|wait\|></tgt>` | 1357 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解を</src><tgt><\|wait\|></tgt>` | 1045 |

---

### Test Example 27 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 851 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>进入到</src><tgt><\|wait\|></tgt>` | 906 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>二季时，</src><tgt><\|wait\|></tgt>` | 1279 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src>会服</src><tgt><\|wait\|></tgt>` | 811 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在这一季</src><tgt><\|wait\|></tgt>` | 1375 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼大的牛们，</src><tgt><\|wait\|></tgt>` | 1793 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 1118 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做微信</src><tgt><\|wait\|></tgt>` | 1404 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好是几年，</src><tgt><\|wait\|></tgt>` | 1888 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1286 |
| 11 | `<src>给微信公众号评分</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>给微信</src><tgt><\|wait\|></tgt>` | 1750 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>好拼分的</src><tgt><\|wait\|></tgt>` | 1442 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>心膀反而</src><tgt><\|wait\|></tgt>` | 1041 |

---

### Test Example 28 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 841 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>so this </src><tgt><\|wait\|></tgt>` | 801 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>so here </src><tgt><\|wait\|></tgt>` | 1027 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>you have to </src><tgt><\|wait\|></tgt>` | 1085 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>gotten 7.8 GB, </src><tgt><\|wait\|></tgt>` | 1574 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>you know? </src><tgt><\|wait\|></tgt>` | 1682 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And </src><tgt><\|wait\|></tgt>` | 1113 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>the way </src><tgt><\|wait\|></tgt>` | 1375 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1813 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>shikumi </src><tgt><\|wait\|></tgt>` | 765 |
| 11 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠. 파생 형용사의 구조는</tgt>` | `<src>wa </src><tgt><\|wait\|></tgt>` | 2263 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>kon </src><tgt><\|wait\|></tgt>` | 1302 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>7.8 GB. </src><tgt><\|wait\|></tgt>` | 1296 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家</src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在</src><tgt><\|wait\|></tgt>` | 775 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>这个罗马呢</src><tgt><\|wait\|></tgt>` | 966 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是</src><tgt><\|wait\|></tgt>` | 1004 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>年前造成的</src><tgt><\|wait\|></tgt>` | 380 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>所以呢</src><tgt><\|wait\|></tgt>` | 1311 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>现在</src><tgt><\|wait\|></tgt>` | 1412 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>除了你的一些</src><tgt><\|wait\|></tgt>` | 1373 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>鸡鸭跟凤</src><tgt><\|wait\|></tgt>` | 1465 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>鸡也不可能是</src><tgt><\|wait\|></tgt>` | 1875 |
| 11 | `<src><\|wait\|></src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、一朝一夕で</tgt>` | `<src>之间就</src><tgt><\|wait\|></tgt>` | 1370 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>演变出来</src><tgt><\|wait\|></tgt>` | 1761 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的实例</src><tgt><\|wait\|></tgt>` | 1462 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>会建议叔叔</src><tgt><\|wait\|></tgt>` | 1120 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>帝王的</src><tgt><\|wait\|></tgt>` | 738 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>部分我们看到的是</src><tgt><\|wait\|></tgt>` | 927 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个</src><tgt><\|wait\|></tgt>` | 953 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>帝王的人，但是</src><tgt><\|wait\|></tgt>` | 1103 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>他是属于</src><tgt><\|wait\|></tgt>` | 1328 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>这一种</src><tgt><\|wait\|></tgt>` | 1269 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>场景</src><tgt><\|wait\|></tgt>` | 1379 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>会像这样一个状况</src><tgt><\|wait\|></tgt>` | 1488 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特殊地注意是</src><tgt><\|wait\|></tgt>` | 891 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1437 |
| 11 | `<src>钓到鱼，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면, 물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到与他</src><tgt><\|wait\|></tgt>` | 2015 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>掉不到与他</src><tgt><\|wait\|></tgt>` | 1139 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的意识</src><tgt><\|wait\|></tgt>` | 1380 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1095 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>他到了一个</src><tgt><\|wait\|></tgt>` | 697 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>甜头，</src><tgt><\|wait\|></tgt>` | 932 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 1045 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>得到了甜头之后</src><tgt><\|wait\|></tgt>` | 1007 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>亲你乌比</src><tgt><\|wait\|></tgt>` | 1466 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就要先手</src><tgt><\|wait\|></tgt>` | 1618 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>组，</src><tgt><\|wait\|></tgt>` | 1155 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想，</src><tgt><\|wait\|></tgt>` | 1440 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在去操作下</src><tgt><\|wait\|></tgt>` | 1823 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>去哦。</src><tgt><\|wait\|></tgt>` | 885 |
| 11 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。「もっといけるはずだ」なんて思わないで。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2234 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1275 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>呢</src><tgt><\|wait\|></tgt>` | 956 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>呢</src><tgt><\|wait\|></tgt>` | 881 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중에서 </src><tgt><\|wait\|></tgt>` | 741 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150원 계기가 </src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>중앙에 </src><tgt><\|wait\|></tgt>` | 1049 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>중앙에 </src><tgt><\|wait\|></tgt>` | 998 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>중소기업들이 </src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1595 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>일반적으로는 </src><tgt><\|wait\|></tgt>` | 1298 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 </src><tgt><\|wait\|></tgt>` | 1469 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>혹은 해외 회계에 </src><tgt><\|wait\|></tgt>` | 2003 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>거의 적게 되는데 </src><tgt><\|wait\|></tgt>` | 2313 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、日本の小企業は成長も廃業も</tgt>` | `<src>해외 송기 없으면 </src><tgt><\|wait\|></tgt>` | 1074 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>성장도 </src><tgt><\|wait\|></tgt>` | 1268 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>폐업 하지 않는 현상들이 </src><tgt><\|wait\|></tgt>` | 1354 |

---

### Test Example 33 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Well, </src><tgt><\|wait\|></tgt>` | 892 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>if you have to produce </src><tgt><\|wait\|></tgt>` | 933 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 980 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt><\|wait\|></tgt>` | 1938 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell the word </src><tgt><\|wait\|></tgt>` | 1573 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>which is like, </src><tgt><\|wait\|></tgt>` | 906 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>oh, is this word </src><tgt><\|wait\|></tgt>` | 1895 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>start with a double P? </src><tgt><\|wait\|></tgt>` | 2331 |
| 11 | `<src><\|wait\|></src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 878 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>Double M? I don't know. </src><tgt><\|wait\|></tgt>` | 1695 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1090 |

---

### Test Example 34 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐이라더니</src><tgt><\|wait\|></tgt>` | 857 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>일거투는</src><tgt><\|wait\|></tgt>` | 887 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진</src><tgt><\|wait\|></tgt>` | 1115 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>유니술림과</src><tgt><\|wait\|></tgt>` | 1058 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>이거진 유산한</src><tgt><\|wait\|></tgt>` | 1482 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>궁전이라</src><tgt><\|wait\|></tgt>` | 1802 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히</src><tgt><\|wait\|></tgt>` | 1170 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>아주 당분</src><tgt><\|wait\|></tgt>` | 1296 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>모네랄이다</src><tgt><\|wait\|></tgt>` | 1907 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>길게</src><tgt><\|wait\|></tgt>` | 2283 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where you could call them diabetes minerals.</tgt>` | `<src>길게</src><tgt><\|wait\|></tgt>` | 874 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그런거죠. 이제</src><tgt><\|wait\|></tgt>` | 1526 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>그거에다가</src><tgt><\|wait\|></tgt>` | 1331 |

---

### Test Example 35 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>由于</src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二二手</src><tgt><\|wait\|></tgt>` | 823 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>とかだと</src><tgt><\|wait\|></tgt>` | 1002 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1074 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>10秒で</src><tgt><\|wait\|></tgt>` | 1277 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>ま1秒に</src><tgt><\|wait\|></tgt>` | 1113 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>1秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1285 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せつあんすかね。</src><tgt><\|wait\|></tgt>` | 1638 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 794 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1750 |
| 11 | `<src>おそらく</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。然后</tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1717 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>11二</src><tgt><\|wait\|></tgt>` | 1379 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1404 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1064 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 816 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから</src><tgt><\|wait\|></tgt>` | 737 |

---

### Test Example 36 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>세모라 빌 </src><tgt><\|wait\|></tgt>` | 810 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>거야. </src><tgt><\|wait\|></tgt>` | 968 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 소름이 </src><tgt><\|wait\|></tgt>` | 1102 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋은 차례 </src><tgt><\|wait\|></tgt>` | 738 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>돋은 데 </src><tgt><\|wait\|></tgt>` | 914 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>기미 움이야. </src><tgt><\|wait\|></tgt>` | 1896 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들어서 </src><tgt><\|wait\|></tgt>` | 1459 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1027 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>기신이 </src><tgt><\|wait\|></tgt>` | 1858 |
| 11 | `<src>신이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら噛みつかれるし、神様が来たら</tgt>` | `<src>움빌 일 거고 </src><tgt><\|wait\|></tgt>` | 2039 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>기신이 어 치켜 </src><tgt><\|wait\|></tgt>` | 1165 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>라고 짓 으라니까 </src><tgt><\|wait\|></tgt>` | 1662 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>피난 방해. </src><tgt><\|wait\|></tgt>` | 1211 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>아, 눈 감아. </src><tgt><\|wait\|></tgt>` | 1128 |

---

### Test Example 37 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在餐饮方面</src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>觉得餐饮可以</src><tgt><\|wait\|></tgt>` | 887 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>说吃很不错，但是</src><tgt><\|wait\|></tgt>` | 1452 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>比较讲正菜的部分</src><tgt><\|wait\|></tgt>` | 747 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>也是在</src><tgt><\|wait\|></tgt>` | 1318 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>西餐方面</src><tgt><\|wait\|></tgt>` | 1624 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长</src><tgt><\|wait\|></tgt>` | 1273 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>的收入的提升</src><tgt><\|wait\|></tgt>` | 1460 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>如果</src><tgt><\|wait\|></tgt>` | 1753 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>在投资领域</src><tgt><\|wait\|></tgt>` | 1211 |
| 11 | `<src>这个月</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。投資や資産運用についても、</tgt>` | `<src>在投资领域</src><tgt><\|wait\|></tgt>` | 1892 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>这个月也是不错，</src><tgt><\|wait\|></tgt>` | 1557 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对来说</src><tgt><\|wait\|></tgt>` | 1098 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>觉得</src><tgt><\|wait\|></tgt>` | 682 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>做了那么一点点</src><tgt><\|wait\|></tgt>` | 947 |

---

### Test Example 38 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 897 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 901 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there's such </src><tgt><\|wait\|></tgt>` | 1259 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>instances before </src><tgt><\|wait\|></tgt>` | 803 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1460 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>net future TC. </src><tgt><\|wait\|></tgt>` | 1716 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1180 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so this is just </src><tgt><\|wait\|></tgt>` | 1519 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>one another place </src><tgt><\|wait\|></tgt>` | 1875 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>ruched </src><tgt><\|wait\|></tgt>` | 1707 |
| 11 | `<src>But </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个需要关注的地方。但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1362 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but </src><tgt><\|wait\|></tgt>` | 1400 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>devops or engineers </src><tgt><\|wait\|></tgt>` | 1119 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>with no bagrepols should be </src><tgt><\|wait\|></tgt>` | 997 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>aware of that. </src><tgt><\|wait\|></tgt>` | 659 |

---

### Test Example 39 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 982 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>村せてやる</src><tgt><\|wait\|></tgt>` | 946 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>あれ</src><tgt><\|wait\|></tgt>` | 1020 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1012 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>ひき手</src><tgt><\|wait\|></tgt>` | 1371 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よ見てる</src><tgt><\|wait\|></tgt>` | 1480 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1420 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超えてる</src><tgt><\|wait\|></tgt>` | 1398 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不れる不気味</src><tgt><\|wait\|></tgt>` | 1883 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 956 |
| 11 | `<src>長年</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>う</src><tgt><\|wait\|></tgt>` | 2098 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>長年の大工</src><tgt><\|wait\|></tgt>` | 1338 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってる</src><tgt><\|wait\|></tgt>` | 1037 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>が</src><tgt><\|wait\|></tgt>` | 802 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>こんなに</src><tgt><\|wait\|></tgt>` | 982 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>すごい快族線を見た。</src><tgt><\|wait\|></tgt>` | 768 |

---

### Test Example 40 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 1044 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 805 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1039 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어, </src><tgt><\|wait\|></tgt>` | 1067 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>20대들을 </src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1286 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1444 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그렇고 </src><tgt><\|wait\|></tgt>` | 1454 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1020 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>어, 제인 거라는 </src><tgt><\|wait\|></tgt>` | 1421 |
| 11 | `<src>조금 </src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以比起责任感，</tgt>` | `<src>저쪽은 </src><tgt><\|wait\|></tgt>` | 2603 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1324 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 972 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거. </src><tgt><\|wait\|></tgt>` | 949 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>넣고. </src><tgt><\|wait\|></tgt>` | 1001 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했으면 </src><tgt><\|wait\|></tgt>` | 843 |

---

### Test Example 41 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1060 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 헤맨 </src><tgt><\|wait\|></tgt>` | 951 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1044 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1025 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>거로 다니고 </src><tgt><\|wait\|></tgt>` | 1439 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>가는 데 </src><tgt><\|wait\|></tgt>` | 1414 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 </src><tgt><\|wait\|></tgt>` | 1256 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>갈 거면 </src><tgt><\|wait\|></tgt>` | 1485 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가도 </src><tgt><\|wait\|></tgt>` | 1629 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장려 리요. </src><tgt><\|wait\|></tgt>` | 821 |
| 11 | `<src>좀 창피 하네요. </src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国就更惨了。真有点丢人。</tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 2393 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>괜히 아니요. </src><tgt><\|wait\|></tgt>` | 1397 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>에 대신에 이제 </src><tgt><\|wait\|></tgt>` | 1170 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 768 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>노배요. </src><tgt><\|wait\|></tgt>` | 1047 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그거는 </src><tgt><\|wait\|></tgt>` | 888 |

---

### Test Example 42 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Educational</src><tgt><\|wait\|></tgt>` | 951 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment. How far</src><tgt><\|wait\|></tgt>` | 835 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>did you actually</src><tgt><\|wait\|></tgt>` | 1062 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>go in your</src><tgt><\|wait\|></tgt>` | 1043 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>education? Did you</src><tgt><\|wait\|></tgt>` | 1396 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school?</src><tgt><\|wait\|></tgt>` | 1474 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of</src><tgt><\|wait\|></tgt>` | 1500 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>attainment. Did you</src><tgt><\|wait\|></tgt>` | 1503 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>go to college, and</src><tgt><\|wait\|></tgt>` | 1958 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>so, did you graduate</src><tgt><\|wait\|></tgt>` | 2425 |
| 11 | `<src>That's another level of </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요? 그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>that's another level of</src><tgt><\|wait\|></tgt>` | 1042 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>attainment.</src><tgt><\|wait\|></tgt>` | 1121 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it for now.</src><tgt><\|wait\|></tgt>` | 1438 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>I'll see you</src><tgt><\|wait\|></tgt>` | 1081 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online.</src><tgt><\|wait\|></tgt>` | 864 |

---

### Test Example 43 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who is</src><tgt><\|wait\|></tgt>` | 1026 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going needs</src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>to get</src><tgt><\|wait\|></tgt>` | 1056 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1001 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and a ten of them that</src><tgt><\|wait\|></tgt>` | 1537 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>you're really important</src><tgt><\|wait\|></tgt>` | 1992 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1344 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to</src><tgt><\|wait\|></tgt>` | 906 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>um, I'm going to go and do</src><tgt><\|wait\|></tgt>` | 2107 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about one</src><tgt><\|wait\|></tgt>` | 2417 |
| 11 | `<src>one minute videos </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>videos, it's</src><tgt><\|wait\|></tgt>` | 1015 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>all this video</src><tgt><\|wait\|></tgt>` | 1134 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one, </src><tgt><\|wait\|></tgt>` | 1364 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>and a little more</src><tgt><\|wait\|></tgt>` | 1026 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>detail, but</src><tgt><\|wait\|></tgt>` | 899 |

---

### Test Example 44 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>で、これはですね、</src><tgt><\|wait\|></tgt>` | 979 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 837 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていう開発環境</src><tgt><\|wait\|></tgt>` | 1069 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>で、ビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1179 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>なんです。で、</src><tgt><\|wait\|></tgt>` | 1408 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>こういうのも</src><tgt><\|wait\|></tgt>` | 1756 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフでビジュアルを</src><tgt><\|wait\|></tgt>` | 1571 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとは</src><tgt><\|wait\|></tgt>` | 947 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード</src><tgt><\|wait\|></tgt>` | 1853 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>を生成する。それが</src><tgt><\|wait\|></tgt>` | 1810 |
| 11 | `<src>実行されることで</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1355 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理を</src><tgt><\|wait\|></tgt>` | 1486 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>行うことになる</src><tgt><\|wait\|></tgt>` | 1176 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>から</src><tgt><\|wait\|></tgt>` | 629 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 769 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 883 |

---

### Test Example 45 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>또 이도 </src><tgt><\|wait\|></tgt>` | 800 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알고 있나요? </src><tgt><\|wait\|></tgt>` | 899 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 이방인으로 </src><tgt><\|wait\|></tgt>` | 1451 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 736 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못 하는 </src><tgt><\|wait\|></tgt>` | 1387 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>무상에게로 </src><tgt><\|wait\|></tgt>` | 1901 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>이 되는 그대로 </src><tgt><\|wait\|></tgt>` | 1305 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>끌려 갔느라 </src><tgt><\|wait\|></tgt>` | 1141 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1793 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그럼 으로 내가 </src><tgt><\|wait\|></tgt>` | 1694 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。ですから、あなたがたに</tgt>` | `<src>너 의에게 </src><tgt><\|wait\|></tgt>` | 1475 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1593 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나 님의 영어 로 </src><tgt><\|wait\|></tgt>` | 1355 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자 는 </src><tgt><\|wait\|></tgt>` | 1097 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 895 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>传闻</src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>和</src><tgt><\|wait\|></tgt>` | 825 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>针对</src><tgt><\|wait\|></tgt>` | 991 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>对手的</src><tgt><\|wait\|></tgt>` | 1075 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1379 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>感染或</src><tgt><\|wait\|></tgt>` | 1238 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>真实</src><tgt><\|wait\|></tgt>` | 1359 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>指引，很多时候</src><tgt><\|wait\|></tgt>` | 1355 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>会</src><tgt><\|wait\|></tgt>` | 682 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1846 |
| 11 | `<src>这个人</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが「ほら、</tgt>` | `<src>这个人又</src><tgt><\|wait\|></tgt>` | 1510 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>在躲黄了。</src><tgt><\|wait\|></tgt>` | 1560 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1486 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经</src><tgt><\|wait\|></tgt>` | 1175 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说明了一切。</src><tgt><\|wait\|></tgt>` | 724 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 747 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 833 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>축가 절수가 </src><tgt><\|wait\|></tgt>` | 880 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이제 상승하는 </src><tgt><\|wait\|></tgt>` | 873 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>그름을 보인 다음에 </src><tgt><\|wait\|></tgt>` | 1452 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러한 </src><tgt><\|wait\|></tgt>` | 664 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src>대형주도 </src><tgt><\|wait\|></tgt>` | 1449 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승을 하겠지만 </src><tgt><\|wait\|></tgt>` | 2060 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>어 먼저 </src><tgt><\|wait\|></tgt>` | 1288 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>이 가벼운 종목 </src><tgt><\|wait\|></tgt>` | 1043 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>들이 </src><tgt><\|wait\|></tgt>` | 1697 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>이 먼저 시장을 </src><tgt><\|wait\|></tgt>` | 1295 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>주도하면서 움직이기 때문에 </src><tgt><\|wait\|></tgt>` | 1922 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src>항상 </src><tgt><\|wait\|></tgt>` | 1435 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>주식 초기에 </src><tgt><\|wait\|></tgt>` | 1241 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목을 </src><tgt><\|wait\|></tgt>` | 884 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>어 눈여겨 봐야 될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 732 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 723 |

---

### Test Example 48 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>계소 </src><tgt><\|wait\|></tgt>` | 1001 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 이런 경우들 </src><tgt><\|wait\|></tgt>` | 956 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1113 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>저희 A라는 사람과 </src><tgt><\|wait\|></tgt>` | 1062 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>기란 사람이 </src><tgt><\|wait\|></tgt>` | 1374 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 </src><tgt><\|wait\|></tgt>` | 1576 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>컨설턴트예요. </src><tgt><\|wait\|></tgt>` | 1637 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>그리고 A라는 </src><tgt><\|wait\|></tgt>` | 1088 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>사람이 </src><tgt><\|wait\|></tgt>` | 1840 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드를 </src><tgt><\|wait\|></tgt>` | 1531 |
| 11 | `<src>뿌렸 을 때 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが何らかの悪性コードを配布したとします。その場合、</tgt>` | `<src>설쳤을 때 </src><tgt><\|wait\|></tgt>` | 1623 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비라는 사람이 </src><tgt><\|wait\|></tgt>` | 1445 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실패를 </src><tgt><\|wait\|></tgt>` | 1149 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로사이트스 T에서 </src><tgt><\|wait\|></tgt>` | 977 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>엑스파이까지 </src><tgt><\|wait\|></tgt>` | 650 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염이 될까? </src><tgt><\|wait\|></tgt>` | 921 |

---

### Test Example 49 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>Oh, </src><tgt><\|wait\|></tgt>` | 738 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>eighty-</src><tgt><\|wait\|></tgt>` | 852 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>seven-mile-one-</src><tgt><\|wait\|></tgt>` | 1328 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>as-one-</src><tgt><\|wait\|></tgt>` | 932 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>two-mile-one-</src><tgt><\|wait\|></tgt>` | 1482 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>two-mile-one-two-</src><tgt><\|wait\|></tgt>` | 2248 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>as-two-mile-one-two-</src><tgt><\|wait\|></tgt>` | 1575 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>is-the-</src><tgt><\|wait\|></tgt>` | 793 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>computer-</src><tgt><\|wait\|></tgt>` | 1542 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>or-another-type-of-computer. </src><tgt><\|wait\|></tgt>` | 2678 |
| 11 | `<src>코드 를 작성 해야 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>We need to write down </src><tgt><\|wait\|></tgt>` | 1422 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>the computer- </src><tgt><\|wait\|></tgt>` | 1144 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>types, but </src><tgt><\|wait\|></tgt>` | 792 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>we need to write down the computer- </src><tgt><\|wait\|></tgt>` | 1152 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>types, but we need to write down the </src><tgt><\|wait\|></tgt>` | 1101 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Activity </src><tgt><\|wait\|></tgt>` | 891 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>then self </src><tgt><\|wait\|></tgt>` | 866 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>defining what we think </src><tgt><\|wait\|></tgt>` | 1072 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>standard is because </src><tgt><\|wait\|></tgt>` | 1054 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1470 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1630 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1207 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new </src><tgt><\|wait\|></tgt>` | 1571 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>kid block and because </src><tgt><\|wait\|></tgt>` | 1890 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have changed </src><tgt><\|wait\|></tgt>` | 1817 |
| 11 | `<src>changed from 20 </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>since 20 </src><tgt><\|wait\|></tgt>` | 1363 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 1496 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held </src><tgt><\|wait\|></tgt>` | 1362 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>to our standard because </src><tgt><\|wait\|></tgt>` | 982 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>everything at this point </src><tgt><\|wait\|></tgt>` | 943 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>is a higher standard </src><tgt><\|wait\|></tgt>` | 559 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, you will not </src><tgt><\|wait\|></tgt>` | 958 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>be able to move </src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>media objects </src><tgt><\|wait\|></tgt>` | 806 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>between the </src><tgt><\|wait\|></tgt>` | 1333 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>resources </src><tgt><\|wait\|></tgt>` | 1415 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>though if </src><tgt><\|wait\|></tgt>` | 1321 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into a situation </src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>where you </src><tgt><\|wait\|></tgt>` | 1813 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 886 |
| 11 | `<src>you've added the wrong media </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果你发现自己</tgt>` | `<src>the wrong media file </src><tgt><\|wait\|></tgt>` | 2305 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>to a particular resource </src><tgt><\|wait\|></tgt>` | 1547 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>to put in the list. Now, </src><tgt><\|wait\|></tgt>` | 1189 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 981 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 649 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 873 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>to get backed up properly. </src><tgt><\|wait\|></tgt>` | 499 |
| 18 | `<src>properly. </src><tgt><\|wait\|></tgt>` | `<src>Wait. </src><tgt><\|wait\|></tgt>` | 462 |

---

### Test Example 52 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 733 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>knows Jesus </src><tgt><\|wait\|></tgt>` | 826 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1063 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1027 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>for he's been </src><tgt><\|wait\|></tgt>` | 1490 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>in the wilderness </src><tgt><\|wait\|></tgt>` | 1366 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and is hungry. And so </src><tgt><\|wait\|></tgt>` | 1589 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>he says, "If </src><tgt><\|wait\|></tgt>` | 1888 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>this is the son of God, </src><tgt><\|wait\|></tgt>` | 1601 |
| 11 | `<src><\|wait\|></src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>prove it. Turn </src><tgt><\|wait\|></tgt>` | 1568 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 1601 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did Jesus </src><tgt><\|wait\|></tgt>` | 1307 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>deal with that </src><tgt><\|wait\|></tgt>` | 983 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 872 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 466 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 261 |
| 18 | `<src>by bread alone. </src><tgt><\|wait\|></tgt>` | `<src>chances are he'd be </src><tgt><\|wait\|></tgt>` | 647 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src>For all the </src><tgt><\|wait\|></tgt>` | 755 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 730 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>subtlety, you've got to </src><tgt><\|wait\|></tgt>` | 1011 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src>get that feeling, but </src><tgt><\|wait\|></tgt>` | 1145 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>we're all </src><tgt><\|wait\|></tgt>` | 1395 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src>in the midst of </src><tgt><\|wait\|></tgt>` | 1486 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>love, </src><tgt><\|wait\|></tgt>` | 1377 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src>we're all </src><tgt><\|wait\|></tgt>` | 1485 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>going to enter </src><tgt><\|wait\|></tgt>` | 1843 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 953 |
| 11 | `<src>在早上的时候，</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다. 아침에는</tgt>` | `<src>night, </src><tgt><\|wait\|></tgt>` | 2145 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>we're all going to enter the night, </src><tgt><\|wait\|></tgt>` | 1818 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>and we're all going to </src><tgt><\|wait\|></tgt>` | 1379 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>turn into </src><tgt><\|wait\|></tgt>` | 979 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that </src><tgt><\|wait\|></tgt>` | 888 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>night </src><tgt><\|wait\|></tgt>` | 541 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>night, </src><tgt><\|wait\|></tgt>` | 500 |
| 18 | `<src>继续在移动。</src><tgt><\|wait\|></tgt>` | `<src>we'll </src><tgt><\|wait\|></tgt>` | 415 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1175 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in here for a mile on the first </src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>section about </src><tgt><\|wait\|></tgt>` | 978 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 970 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>AHR field </src><tgt><\|wait\|></tgt>` | 1366 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>being of critical </src><tgt><\|wait\|></tgt>` | 1253 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>importance versus </src><tgt><\|wait\|></tgt>` | 1437 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1456 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>variant database </src><tgt><\|wait\|></tgt>` | 662 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>is which is obviously </src><tgt><\|wait\|></tgt>` | 1793 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 2519 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1410 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1124 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 888 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1002 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt><\|wait\|></tgt>` | 884 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from. </src><tgt><\|wait\|></tgt>` | 577 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt><\|wait\|></tgt>` | `<src>There's nothing to draw from, </src><tgt><\|wait\|></tgt>` | 653 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>right? </src><tgt><\|wait\|></tgt>` | 427 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 1102 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 789 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, and </src><tgt><\|wait\|></tgt>` | 994 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>Supreme Court came </src><tgt><\|wait\|></tgt>` | 1088 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>along last, </src><tgt><\|wait\|></tgt>` | 1222 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>not leading. And I </src><tgt><\|wait\|></tgt>` | 1178 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>thought the courts want to be </src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the </src><tgt><\|wait\|></tgt>` | 1099 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>vanard of social change </src><tgt><\|wait\|></tgt>` | 1030 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>change. </src><tgt><\|wait\|></tgt>` | 1790 |
| 11 | `<src>these days, </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为法院现在想成为社会变革的先锋，</tgt>` | `<src>Ah, these days. </src><tgt><\|wait\|></tgt>` | 1463 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But they rather </src><tgt><\|wait\|></tgt>` | 1600 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect the </src><tgt><\|wait\|></tgt>` | 1485 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>consensus </src><tgt><\|wait\|></tgt>` | 1068 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 719 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 867 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 894 |
| 18 | `<src>So you have some </src><tgt><\|wait\|></tgt>` | `<src>you have </src><tgt><\|wait\|></tgt>` | 499 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 507 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 386 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who </src><tgt><\|wait\|></tgt>` | 382 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 903 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1114 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的部分呢，</src><tgt><\|wait\|></tgt>` | 980 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1450 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>客听的部分，</src><tgt><\|wait\|></tgt>` | 1781 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>客听一般</src><tgt><\|wait\|></tgt>` | 1184 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>是属于</src><tgt><\|wait\|></tgt>` | 1238 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>我们再</src><tgt><\|wait\|></tgt>` | 1795 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>休息的地方，</src><tgt><\|wait\|></tgt>` | 880 |
| 11 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가 쉬는 곳이잖아요.</tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 2239 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>这是身体的部分。</src><tgt><\|wait\|></tgt>` | 1341 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>它会反映的是</src><tgt><\|wait\|></tgt>` | 1149 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>需要给</src><tgt><\|wait\|></tgt>` | 706 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 1026 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好地做。</src><tgt><\|wait\|></tgt>` | 915 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>下来休息，</src><tgt><\|wait\|></tgt>` | 548 |
| 18 | `<src>我们可以看到这边是</src><tgt><\|wait\|></tgt>` | `<src>可我们看到这边是</src><tgt><\|wait\|></tgt>` | 597 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>双人吗？</src><tgt><\|wait\|></tgt>` | 456 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，所以</src><tgt><\|wait\|></tgt>` | 380 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>是说</src><tgt><\|wait\|></tgt>` | 360 |

---

### Test Example 57 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 693 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>말하는 사람들이 </src><tgt><\|wait\|></tgt>` | 895 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석을 해 놓았습니다. </src><tgt><\|wait\|></tgt>` | 1551 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 649 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>에 대한 분석을 보시면 </src><tgt><\|wait\|></tgt>` | 1446 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니 가 </src><tgt><\|wait\|></tgt>` | 1847 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>유력 룩트 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에 에` | 11613 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>FFP 파이프 를 </src><tgt><\|wait\|></tgt>` | 923 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128 비트 로 </src><tgt><\|wait\|></tgt>` | 416 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>나 줘 로 보인다. </src><tgt><\|wait\|></tgt>` | 588 |
| 11 | `<src><\|wait\|></src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げたようです。</tgt>` | `<src>엑스박스 시리즈 </src><tgt><\|wait\|></tgt>` | 425 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 368 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 383 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>에 S2 </src><tgt><\|wait\|></tgt>` | 339 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>가 여기도 없다. </src><tgt><\|wait\|></tgt>` | 362 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 336 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 793 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare. </src><tgt><\|wait\|></tgt>` | 892 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>And they often </src><tgt><\|wait\|></tgt>` | 1265 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 848 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize </src><tgt><\|wait\|></tgt>` | 1338 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>the world. </src><tgt><\|wait\|></tgt>` | 1600 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The personality </src><tgt><\|wait\|></tgt>` | 1252 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>is something </src><tgt><\|wait\|></tgt>` | 1372 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>of a contradiction. </src><tgt><\|wait\|></tgt>` | 1826 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 623 |
| 11 | `<src>While they're </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は矛盾しています。</tgt>` | `<src>Well, they're extroverted, </src><tgt><\|wait\|></tgt>` | 2707 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>they also </src><tgt><\|wait\|></tgt>` | 1462 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>hate meaningless </src><tgt><\|wait\|></tgt>` | 1107 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>conversations. </src><tgt><\|wait\|></tgt>` | 787 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src>And like </src><tgt><\|wait\|></tgt>` | 829 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>it gets straight to the </src><tgt><\|wait\|></tgt>` | 917 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>point. </src><tgt><\|wait\|></tgt>` | 439 |
| 18 | `<src>They also love to </src><tgt><\|wait\|></tgt>` | `<src>They also love </src><tgt><\|wait\|></tgt>` | 511 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>to play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 416 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and </src><tgt><\|wait\|></tgt>` | 312 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 365 |
| 22 | `<src>never shy away from a debate. </src><tgt>外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、あえて悪魔の代弁者を演じることを好み、議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 345 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Ean </src><tgt><\|wait\|></tgt>` | 355 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>TP stands </src><tgt><\|wait\|></tgt>` | 352 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for </src><tgt><\|wait\|></tgt>` | 263 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전의 이준석은</src><tgt><\|wait\|></tgt>` | 987 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 742 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>정무를 거부한 명분이 후불을 위해서</src><tgt><\|wait\|></tgt>` | 1789 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>하면서 후불을</src><tgt><\|wait\|></tgt>` | 405 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>위해서라는</src><tgt><\|wait\|></tgt>` | 1367 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>생각을 위해서</src><tgt><\|wait\|></tgt>` | 2007 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>세보생색까지 냈지만</src><tgt><\|wait\|></tgt>` | 1694 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>이제는</src><tgt><\|wait\|></tgt>` | 779 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보가</src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김경기를 재관 순간</src><tgt><\|wait\|></tgt>` | 2476 |
| 11 | `<src>제거 한 순간 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now, the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>이준석</src><tgt><\|wait\|></tgt>` | 1247 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>등르내 놓고</src><tgt><\|wait\|></tgt>` | 891 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보</src><tgt><\|wait\|></tgt>` | 1296 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는</src><tgt><\|wait\|></tgt>` | 1013 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼를 품은</src><tgt><\|wait\|></tgt>` | 898 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격성을</src><tgt><\|wait\|></tgt>` | 551 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이기로</src><tgt><\|wait\|></tgt>` | 521 |
| 18 | `<src>보이 기로 작정 한 </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것</src><tgt><\|wait\|></tgt>` | 425 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다.</src><tgt><\|wait\|></tgt>` | 375 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>김세발 이준석</src><tgt><\|wait\|></tgt>` | 396 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>청상 납권</src><tgt><\|wait\|></tgt>` | 320 |
| 22 | `<src><\|wait\|></src><tgt>Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down. And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 362 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당이 공격</src><tgt><\|wait\|></tgt>` | 369 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하기에 얼마나</src><tgt><\|wait\|></tgt>` | 281 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재입니까?</src><tgt><\|wait\|></tgt>` | 264 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 10.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 792 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいです。</src><tgt><\|wait\|></tgt>` | 904 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 999 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここのね</src><tgt><\|wait\|></tgt>` | 470 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>ホテル</src><tgt><\|wait\|></tgt>` | 1242 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>の朝食が</src><tgt><\|wait\|></tgt>` | 1701 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所になってる</src><tgt><\|wait\|></tgt>` | 1380 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってる</src><tgt><\|wait\|></tgt>` | 1294 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 1749 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1076 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>このドストンホテル</src><tgt><\|wait\|></tgt>` | 2085 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい方</src><tgt><\|wait\|></tgt>` | 1561 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>はですね</src><tgt><\|wait\|></tgt>` | 1117 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | 842 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>まあいいんじゃないかと</src><tgt><\|wait\|></tgt>` | 777 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 803 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>このホテルからですね</src><tgt><\|wait\|></tgt>` | 547 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>アップ3駅も</src><tgt><\|wait\|></tgt>` | 586 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう</src><tgt><\|wait\|></tgt>` | 431 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>歩いて</src><tgt><\|wait\|></tgt>` | 382 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel, it's less than a minute's walk to Busan Station,</tgt>` | `<src>1分かかるか</src><tgt><\|wait\|></tgt>` | 388 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなね</src><tgt><\|wait\|></tgt>` | 345 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のね</src><tgt><\|wait\|></tgt>` | 356 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>まあホテルなってますので</src><tgt><\|wait\|></tgt>` | 374 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 252 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 217 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。</src><tgt><\|wait\|></tgt>` | 175 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>それでは</src><tgt><\|wait\|></tgt>` | 175 |
