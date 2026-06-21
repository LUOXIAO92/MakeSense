# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 0.9977
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9581
  - SRC_RELEASE_TOTAL: 716
  - SRC_WAIT_ACCURACY: 0.4040
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 47
  - TARGET_METRICS_FILTERED_TURN_COUNT: 683
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 13
  - TGT_RELEASE_ACCURACY: 0.9884
  - TGT_RELEASE_TOTAL: 86
  - TGT_WAIT_ACCURACY: 0.9796
  - TGT_WAIT_TOTAL: 98
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1428.1660
  - PROCESS_TIME_MS_P50: 1447.1540
  - PROCESS_TIME_MS_P95: 2127.5160
  - PROCESS_TIME_MS_MAX: 9145.3350

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 783 |
| 2 | `<src>あの特に</src><tgt>从一开始，尤其是</tgt>` | `<src>あの特に</src><tgt>从一开始，</tgt>` | 965 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>子供がまだ</src><tgt><\|wait\|></tgt>` | 1419 |
| 4 | `<src>一年生ですからね。</src><tgt>这一棵现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>孩子还是小学一年级呢。</tgt>` | 1297 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>あの時点で</src><tgt><\|wait\|></tgt>` | 1245 |
| 6 | `<src>こう短く</src><tgt>在这个阶段</tgt>` | `<src>こう身近く</src><tgt>就在那个时候，</tgt>` | 1642 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>算定を</src><tgt><\|wait\|></tgt>` | 1061 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対図して</src><tgt>我们算出了</tgt>` | 1783 |
| 9 | `<src>こうタイズしてってあげると</src><tgt><\|wait\|></tgt>` | `<src>なげると</src><tgt><\|wait\|></tgt>` | 1723 |
| 10 | `<src>十年経っても</src><tgt>如果能把剪枝持续做好的话，十年后也不会</tgt>` | `<src>十年経っても</src><tgt>十年后</tgt>` | 1799 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 624 |

---

### Test Example 2 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying important </src><tgt><\|wait\|></tgt>` | 1011 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>research </src><tgt>重要な研究を</tgt>` | 930 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>on </src><tgt><\|wait\|></tgt>` | 1343 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>extremely happy people. This is </src><tgt>極度に幸せな人々について行いました。</tgt>` | 1489 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1713 |
| 6 | `<src>research, </src><tgt>これは最先端の研究です。</tgt>` | `<src>research. Looking at </src><tgt>これは研究の序章です。</tgt>` | 1408 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 868 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>of the happiest </src><tgt>最も幸せな</tgt>` | 1605 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>people </src><tgt><\|wait\|></tgt>` | 1647 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, people that </src><tgt>人々を10%見ると、</tgt>` | 1860 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 624 |

---

### Test Example 3 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1157 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气鼠是容易的，</src><tgt>「気鼠」は簡単です。</tgt>` | 1886 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 823 |
| 4 | `<src>只有一个师父</src><tgt>簡単ですが、</tgt>` | `<src>只有一个师傅</src><tgt>でも、</tgt>` | 1309 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>指道：“</src><tgt><\|wait\|></tgt>` | 1611 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如波出</src><tgt>師匠が</tgt>` | 1288 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>于中年，</src><tgt><\|wait\|></tgt>` | 799 |
| 8 | `<src>所以</src><tgt>中間に留まる方法を知っているのは師匠だけです。だからこそ、</tgt>` | `<src>所以</src><tgt>「波出」を中年と指し示しました。だから</tgt>` | 2282 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt><\|wait\|></tgt>` | 1140 |
| 10 | `<src>要成为</src><tgt>シュ・アファンは</tgt>` | `<src>要成为</src><tgt>反転が必要なんです。</tgt>` | 2120 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>一个师傅，</src><tgt><\|wait\|></tgt>` | 1995 |

---

### Test Example 4 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>淘洗が終わった後、</tgt>` | 1702 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的冶力检验</src><tgt><\|wait\|></tgt>` | 1045 |
| 4 | `<src>能量也衰弱了，</src><tgt>内部の圧力が軽くなり、エネルギーも弱まります。</tgt>` | `<src>能量也衰弱了。</src><tgt>内部の冶力検査エネルギーも弱まります。</tgt>` | 2448 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 1180 |
| 6 | `<src>就停留在一个</src><tgt>そして、</tgt>` | `<src>就停留在</src><tgt>そして、</tgt>` | 790 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1682 |
| 8 | `<src>能量的运行</src><tgt>比較的低エネルギーの</tgt>` | `<src>低能量的</src><tgt>比較的低いエネルギーの</tgt>` | 1597 |
| 9 | `<src>状态，</src><tgt><\|wait\|></tgt>` | `<src>运行状态，</src><tgt><\|wait\|></tgt>` | 815 |
| 10 | `<src>这就是所谓的</src><tgt>状態にとどまります。これが、いわゆる</tgt>` | `<src>这就是所谓的</src><tgt>運転状態に留まります。これが</tgt>` | 2011 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>倚虚状态。</src><tgt><\|wait\|></tgt>` | 1986 |

---

### Test Example 5 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1208 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>家长需要做的是，</src><tgt>What parents need to do is</tgt>` | 1401 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1335 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱</src><tgt>use our deep love</tgt>` | 1873 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>浇水，</src><tgt><\|wait\|></tgt>` | 1315 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>to water and fertilize</tgt>` | 1332 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1713 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>培育孩子心灵营养，</src><tgt>their children's spiritual nourishment.</tgt>` | 1809 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 578 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>冷心等等，</src><tgt>And also to cultivate their hearts and minds.</tgt>` | 1973 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>让孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 2004 |

---

### Test Example 6 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 1025 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Abbotol. </src><tgt>I am Abbotol.</tgt>` | 1313 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt><\|wait\|></tgt>` | 1355 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>I'll banish you,</tgt>` | 1722 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1404 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt>I'll kill your own parents,</tgt>` | 1436 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>녀르나 </src><tgt><\|wait\|></tgt>` | 1784 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and you'll</tgt>` | 1792 |
| 9 | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | `<src>박한상과 </src><tgt><\|wait\|></tgt>` | 601 |
| 10 | `<src><\|wait\|></src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>같은 세대 들은 </src><tgt>be just like Park Han- sang and the same generation,</tgt>` | 1995 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>됩니다. </src><tgt><\|wait\|></tgt>` | 1892 |

---

### Test Example 7 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1389 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>怪在嵩子寺里边，</src><tgt>It's strange that it's inside Songzi Temple.</tgt>` | 2214 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个游行也很大，</src><tgt><\|wait\|></tgt>` | 1269 |
| 4 | `<src>然后</src><tgt>they're quite oily.</tgt>` | `<src><\|wait\|></src><tgt>The procession is also huge.</tgt>` | 1591 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 1405 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt>And I'm on vacation</tgt>` | 1069 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和陶渊临，</src><tgt><\|wait\|></tgt>` | 1830 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>and I'm spending time with Tao Yuanming.</tgt>` | 1847 |
| 9 | `<src>仁儿，仁儿里边</src><tgt><\|wait\|></tgt>` | `<src>这里呀，</src><tgt><\|wait\|></tgt>` | 1721 |
| 10 | `<src>这种核桃</src><tgt>some walnut kernels— this kind of</tgt>` | `<src><\|wait\|></src><tgt>Here,</tgt>` | 736 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>这种和陶渊。</src><tgt><\|wait\|></tgt>` | 1712 |

---

### Test Example 8 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对这个</src><tgt><\|wait\|></tgt>` | 1042 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>情况，我们就是</src><tgt>Facing this situation,</tgt>` | 1211 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1405 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>when we encounter a problem, we should</tgt>` | `<src>就赶紧的回报主管，</src><tgt>we just quickly report it to our supervisor.</tgt>` | 2211 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方</src><tgt><\|wait\|></tgt>` | 1419 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们学校这个状况，</src><tgt>Or we notify the school about the situation.</tgt>` | 1073 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想</src><tgt><\|wait\|></tgt>` | 1823 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>自己什么都把它扛下来，</src><tgt>Don't try to handle everything yourself.</tgt>` | 2040 |
| 9 | `<src>独立承担。</src><tgt><\|wait\|></tgt>` | `<src>不理承担。</src><tgt><\|wait\|></tgt>` | 1764 |
| 10 | `<src>整体而言，</src><tgt>or handle it alone. Overall,</tgt>` | `<src>整体而言，</src><tgt>Overall,</tgt>` | 775 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业属顺。</src><tgt><\|wait\|></tgt>` | 1670 |

---

### Test Example 9 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>자 저는 </src><tgt><\|wait\|></tgt>` | 1095 |
| 2 | `<src>옹심이, </src><tgt>I'm having</tgt>` | `<src>용심이 </src><tgt>I'm</tgt>` | 1075 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1599 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt>a sword- minded person,</tgt>` | 1417 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설프 용심이가 </src><tgt><\|wait\|></tgt>` | 1781 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>a clumsy sword- minded person,</tgt>` | 1356 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1963 |
| 8 | `<src>야, </src><tgt>it's a mix of rice noodles and ongsimi. Man,</tgt>` | `<src><\|wait\|></src><tgt>they're mixed together. Wow,</tgt>` | 1938 |
| 9 | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 1843 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>this is seriously killer for a hangover,</tgt>` | `<src>해형으로 </src><tgt>this is really</tgt>` | 618 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 쥐기 맞는 것 </src><tgt><\|wait\|></tgt>` | 1954 |

---

### Test Example 10 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1339 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt>The people in the auspicious spots</tgt>` | 1213 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1405 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt>actually don't have high intelligence.</tgt>` | 2074 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1412 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt>They were just randomly selected</tgt>` | 1129 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1743 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt>and are just some people.</tgt>` | 1877 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 556 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1820 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>몰랐던 교수 아들은 </src><tgt>The professor son who didn't know the truth</tgt>` | 2260 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1230 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 992 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1482 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>要重复。学会不断重复。</tgt>` | `<src>Learn to rinse and repeat. </src><tgt>重复。学会重复。重复。</tgt>` | 1376 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1746 |
| 6 | `<src>and do more of it. </src><tgt>找到你的长处，多做那些事。</tgt>` | `<src>and do more of it. </src><tgt>找到你擅长的地方，多做一些。</tgt>` | 1662 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And what you're not good </src><tgt><\|wait\|></tgt>` | 1885 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>at, get to people </src><tgt>你不太擅长的，</tgt>` | 1967 |
| 9 | `<src>get the people around you to help you with. </src><tgt><\|wait\|></tgt>` | `<src>around you to help you with </src><tgt><\|wait\|></tgt>` | 1971 |
| 10 | `<src><\|wait\|></src><tgt>找身边的人帮你。</tgt>` | `<src><\|wait\|></src><tgt>找身边的人帮忙，</tgt>` | 1780 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>it, and and tell the next time </src><tgt><\|wait\|></tgt>` | 710 |

---

### Test Example 12 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 932 |
| 2 | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1128 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into your body. </src><tgt><\|wait\|></tgt>` | 1469 |
| 4 | `<src>your body. </src><tgt>感受一下你的身体。</tgt>` | `<src>Where does </src><tgt>进入你的身体。你</tgt>` | 1589 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>the tension </src><tgt><\|wait\|></tgt>` | 1390 |
| 6 | `<src>start? What is it? </src><tgt>紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>的紧张感从哪里开始？是什么？</tgt>` | 1643 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1929 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？还是胸口紧绷？</tgt>` | `<src>Is it a tightness in your chest? </src><tgt>是头痛吗？胸口紧吗？</tgt>` | 2007 |
| 9 | `<src>I ask them what </src><tgt><\|wait\|></tgt>` | `<src>Or is it </src><tgt><\|wait\|></tgt>` | 1867 |
| 10 | `<src><\|wait\|></src><tgt>我问他们，</tgt>` | `<src>a lump in your </src><tgt>还是</tgt>` | 1954 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>using? </src><tgt><\|wait\|></tgt>` | 938 |

---

### Test Example 13 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうですよ。</src><tgt><\|wait\|></tgt>` | 968 |
| 2 | `<src>そこで</src><tgt>맞습니다. 거기</tgt>` | `<src>そこで</src><tgt>맞아요. 거기서</tgt>` | 865 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>天国</src><tgt><\|wait\|></tgt>` | 1450 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>という施設</src><tgt>천국이라는 시설이</tgt>` | 1213 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>がありましたね。</src><tgt><\|wait\|></tgt>` | 1133 |
| 6 | `<src>で、</src><tgt>있었죠.</tgt>` | `<src>で、</src><tgt>있었죠. 그런데</tgt>` | 1530 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1040 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井英雄氏の仕組み</src><tgt>나가이 히데오 씨의</tgt>` | 1841 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt><\|wait\|></tgt>` | 1494 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>冒険</src><tgt>시스템은</tgt>` | 751 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1985 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>施設</src><tgt>모험 시설</tgt>` | 1951 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ゴビース。</src><tgt><\|wait\|></tgt>` | 1733 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1123 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 를 </src><tgt>I'll</tgt>` | 1181 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>주겨 달라 해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1525 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>Someone asked me to kill them, so I came in here to do it.</tgt>` | `<src>주길 수 있도록 </src><tgt>give you another party invitation,</tgt>` | 1841 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>하도노 아스다. 다른 잔치 </src><tgt><\|wait\|></tgt>` | 1955 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>미 주겨 달라 해잔 </src><tgt>but I'm not sure if I can.</tgt>` | 1578 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>안 되나. 내가 </src><tgt><\|wait\|></tgt>` | 1451 |
| 8 | `<src>그 소리 안 듣고 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt>I don't think I can give you another party invitation either.</tgt>` | 1858 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>주자 는 거야. </src><tgt><\|wait\|></tgt>` | 1870 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src><\|wait\|></src><tgt>I'm just saying I'm not listening to you.</tgt>` | 2204 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1611 |

---

### Test Example 15 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1371 |
| 2 | `<src>and then </src><tgt>好的，然后</tgt>` | `<src>And then, </src><tgt>好的。然后，</tgt>` | 1088 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1533 |
| 4 | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | `<src><\|wait\|></src><tgt>在这些例子之后，</tgt>` | 1506 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1480 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1489 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1001 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt>实际上</tgt>` | 1132 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1771 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>要使用这些值。</tgt>` | 1745 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So this </src><tgt><\|wait\|></tgt>` | 647 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>game dot sort array. </src><tgt>所以这是game.sort数组。</tgt>` | 2073 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1676 |

---

### Test Example 16 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt>제가</tgt>` | 886 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个轨道，</src><tgt><\|wait\|></tgt>` | 1689 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>好，</src><tgt>제 삶의 궤도로 돌아가게 해 주세요.</tgt>` | 1983 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 1257 |
| 6 | `<src>在他下班的时候，</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>好自在的时光，</src><tgt>편안한 시간을</tgt>` | 1329 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1707 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>热饭一样的，</src><tgt>보내 주세요. 뜨거운 국처럼 따뜻한 밥처럼,</tgt>` | 2158 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是说</src><tgt><\|wait\|></tgt>` | 1762 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时被他这样子</src><tgt>그때 그분이 저를</tgt>` | 810 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>这么一个小小的小小的一个愿望</src><tgt><\|wait\|></tgt>` | 1877 |
| 12 | `<src>哈。</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>哈。</src><tgt>이렇게 바라보게 해 주세요.</tgt>` | 1667 |

---

### Test Example 17 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1311 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt>T- shirts and things like that</tgt>` | 1306 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただいている</src><tgt><\|wait\|></tgt>` | 1308 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>と言ったようなものも</src><tgt>that you've received</tgt>` | 1899 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1310 |
| 6 | `<src>ぜひご参加ください。</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us.</tgt>` | `<src>ぜひご参考ください。</src><tgt>are also available, so please do take a look.</tgt>` | 1473 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1799 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>That's all for the contact</tgt>` | 1909 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>て、えっと</src><tgt><\|wait\|></tgt>` | 1766 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こちら</src><tgt>I have,</tgt>` | 616 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>の案内があります</src><tgt><\|wait\|></tgt>` | 1905 |
| 12 | `<src>もう少々お待ちください。</src><tgt>and we have some info about lunch, so please wait just a moment.</tgt>` | `<src>ので、もう少しお待ちください。</src><tgt>so please wait a little longer for the information here.</tgt>` | 1858 |

---

### Test Example 18 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1156 |
| 2 | `<src>このあたりから</src><tgt>大致是从这一带</tgt>` | `<src>このあたりから</src><tgt>大概从这个地方开始，</tgt>` | 1289 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 1414 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>我才开始的，</tgt>` | 1394 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴゴ号、</src><tgt><\|wait\|></tgt>` | 1653 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt>比如“ゴゴ号”、“ゴー根”</tgt>` | 1578 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1818 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザム、</src><tgt>和“セザム”，</tgt>` | 1964 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | 1867 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>という人の絵</src><tgt>还有</tgt>` | 574 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、</src><tgt><\|wait\|></tgt>` | 1877 |
| 12 | `<src>中学生でも。</src><tgt>画，连乡下的中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt>像“ルナ尔”这些人的画，</tgt>` | 1845 |

---

### Test Example 19 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>またまたちょっと</src><tgt><\|wait\|></tgt>` | 1289 |
| 2 | `<src>距離が</src><tgt>嗯，</tgt>` | `<src>距離が離れてくる</src><tgt>又又有点</tgt>` | 1138 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1544 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>感觉距离会慢慢拉开，确实</tgt>` | `<src>大将が</src><tgt>像距离拉开了一点，大将</tgt>` | 1672 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>ある方多いですね。</src><tgt><\|wait\|></tgt>` | 1526 |
| 6 | `<src>開業したい方って</src><tgt>很多人这么说。想创业的人</tgt>` | `<src>海遊したい方って</src><tgt>好像很多人都想去海游。</tgt>` | 1444 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行き来しきたり</src><tgt><\|wait\|></tgt>` | 1992 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>し、</src><tgt>他们会来来回地往返，</tgt>` | 1943 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>ジュウジュウって</src><tgt><\|wait\|></tgt>` | 1904 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>音立てて</src><tgt>发出“啾啾”的声音，</tgt>` | 2018 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>シャグが強いので</src><tgt><\|wait\|></tgt>` | 1546 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt>因为“シャグ”很强，所以</tgt>` | 633 |

---

### Test Example 20 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1111 |
| 2 | `<src>Kerenath Dettig. </src><tgt>제 이름은 케레나스 데티그입니다.</tgt>` | `<src>Shiranami Teru. </src><tgt>제 이름은 시라나미 테루입니다.</tgt>` | 2009 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 794 |
| 4 | `<src><\|wait\|></src><tgt>저는 현재</tgt>` | `<src><\|wait\|></src><tgt>현재</tgt>` | 1179 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>a business background, </src><tgt><\|wait\|></tgt>` | 1660 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>finance, and a bachelor of </src><tgt>경영학을 전공하고 있습니다. 경영학, 금융학, 그리고</tgt>` | 1877 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>psychology. </src><tgt><\|wait\|></tgt>` | 1714 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Here at Yaenju, </src><tgt>심리학 학사 학위를 받았습니다. 여기 야엔주에서는</tgt>` | 2001 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and in the </src><tgt><\|wait\|></tgt>` | 1964 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>future, I want to go into </src><tgt>앞으로</tgt>` | 2024 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1636 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 728 |

---

### Test Example 21 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1219 |
| 2 | `<src>です。</src><tgt>이것이 기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 824 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1507 |
| 4 | `<src>緩むと芯が</src><tgt>기어가 느슨해지면 심이</tgt>` | `<src>ゆるむと</src><tgt>기어가 맞물리면</tgt>` | 1240 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えて</src><tgt><\|wait\|></tgt>` | 1401 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>신호가 꺼져서</tgt>` | 1690 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1108 |
| 8 | `<src>役ねじの</src><tgt>기어 끝에</tgt>` | `<src>ヤクネジの</src><tgt>안 되니까, 기어 앞쪽에</tgt>` | 2249 |
| 9 | `<src>ナットが</src><tgt><\|wait\|></tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1289 |
| 10 | `<src>ついているっていうことです</src><tgt>역나사 너트가</tgt>` | `<src>付いている</src><tgt>나사 머리가</tgt>` | 2012 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>っていうことですね。</src><tgt><\|wait\|></tgt>` | 1977 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>달려 있는 거죠.</tgt>` | 1716 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキを。</src><tgt><\|wait\|></tgt>` | 723 |

---

### Test Example 22 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 949 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a female high school student</tgt>` | 1909 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1024 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之间有着某种</src><tgt>have a connection with someone who's a bit weird,</tgt>` | 2235 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>联系，</src><tgt><\|wait\|></tgt>` | 1293 |
| 6 | `<src>难道会是</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>难道会是</src><tgt> is it</tgt>` | 885 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1861 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天涯里开始的？</src><tgt>something that started back in Tianya?</tgt>` | 1975 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2040 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1971 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt>Yangzi's thoughts</tgt>` | 1769 |
| 12 | `<src>连篇。</src><tgt>Yang Zi's thoughts drifted.</tgt>` | `<src>连篇。</src><tgt><\|wait\|></tgt>` | 1229 |

---

### Test Example 23 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 958 |
| 2 | `<src><\|wait\|></src><tgt>2つ目は、</tgt>` | `<src>就是问子二</src><tgt>2つ目は、</tgt>` | 982 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>师堂，</src><tgt><\|wait\|></tgt>` | 1425 |
| 4 | `<src>服务</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>还服务</src><tgt>師堂の質問です。また、</tgt>` | 1291 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | 1376 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>拼杀的大牛们。</src><tgt>一級一线で戦う大牛たちへのサービスも含まれます。</tgt>` | 1795 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说，</src><tgt><\|wait\|></tgt>` | 840 |
| 8 | `<src><\|wait\|></src><tgt>例えば、</tgt>` | `<src>在做维信</src><tgt>例えば、</tgt>` | 1725 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt><\|wait\|></tgt>` | `<src>沟通好事几年前，</src><tgt><\|wait\|></tgt>` | 1796 |
| 10 | `<src>发现</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>你会发现</src><tgt>維信コミュニケーションを始めたのが何年前か</tgt>` | 2068 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给维信沟通好平分子的</src><tgt><\|wait\|></tgt>` | 2066 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新绑</src><tgt>思い出せますか？維信コミュニケーションで</tgt>` | 1835 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反而活了。</src><tgt><\|wait\|></tgt>` | 1385 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1155 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>我当时已很正常，</src><tgt>I was already quite normal at the time.</tgt>` | 1848 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 900 |
| 4 | `<src>所以</src><tgt>jumping around, so I</tgt>` | `<src>所以</src><tgt>So I</tgt>` | 1169 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>坚持不开档，</src><tgt><\|wait\|></tgt>` | 1678 |
| 6 | `<src>期间</src><tgt>insisted on not having surgery.</tgt>` | `<src>期间大概有</src><tgt>didn't keep the door locked. During that time,</tgt>` | 1630 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十名医生</src><tgt><\|wait\|></tgt>` | 1766 |
| 8 | `<src>来诊断，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>来诊段，</src><tgt>about ten doctors came to treat me,</tgt>` | 1993 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下挑腿</src><tgt><\|wait\|></tgt>` | 1756 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿，</src><tgt>and they had to pull on my legs and lift them up.</tgt>` | 942 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1688 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>It wasn't a problem at all.</tgt>` | 1748 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑的离开。</src><tgt><\|wait\|></tgt>` | 1454 |

---

### Test Example 25 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 947 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAアンデスに</src><tgt>Um, in the A A Andes,</tgt>` | 1650 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>そのあたりで</src><tgt><\|wait\|></tgt>` | 1117 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt>in various situations,</tgt>` | `<src>生生捕獲を</src><tgt>we're doing</tgt>` | 1835 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>考えてる時に</src><tgt><\|wait\|></tgt>` | 1316 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>まあAAの</src><tgt>some live capture research,</tgt>` | 1328 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>乱行調べということであの</src><tgt><\|wait\|></tgt>` | 1815 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生生捕獲を</src><tgt>and we're looking into the A A</tgt>` | 2062 |
| 9 | `<src>保証する、生息である</src><tgt><\|wait\|></tgt>` | `<src>考えてる生生で</src><tgt><\|wait\|></tgt>` | 1974 |
| 10 | `<src>ことを保証する</src><tgt>This guarantees their presence— it ensures they are indeed inhabiting the area.</tgt>` | `<src>捕獲すること保証するということでいったん</src><tgt>live capture we're doing. So, we're confirming that we're doing live capture.</tgt>` | 2450 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>その使い方を</src><tgt><\|wait\|></tgt>` | 1646 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>されています。</src><tgt>That's how we're using it.</tgt>` | 1557 |

---

### Test Example 26 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1313 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>the 19th </src><tgt>19세기</tgt>` | 1108 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>Amendment, </src><tgt><\|wait\|></tgt>` | 1514 |
| 4 | `<src>and to explore its </src><tgt>수정헌법 제19조의 의미를 살펴보고,</tgt>` | `<src>and to explore its </src><tgt>수정안의 의미와</tgt>` | 1668 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>to how political </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>역사적 맥락을 살펴보겠습니다.</tgt>` | 1423 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>change can </src><tgt><\|wait\|></tgt>` | 1669 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>happen in the </src><tgt>정치적 변화가</tgt>` | 1670 |
| 9 | `<src>in the United States. </src><tgt><\|wait\|></tgt>` | `<src>United States. </src><tgt><\|wait\|></tgt>` | 688 |
| 10 | `<src><\|wait\|></src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src><\|wait\|></src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침서로서 말이죠.</tgt>` | 2158 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1933 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 1730 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Meredith. </src><tgt><\|wait\|></tgt>` | 1775 |

---

### Test Example 27 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼 늘어난</tgt>` | 1559 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | 1104 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>also store energy. And when those </src><tgt>화학 결합도 에너지를 저장합니다. 그리고</tgt>` | 2824 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1216 |
| 6 | `<src>that potential energy </src><tgt>이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 결합이 끊어지면, 그 잠재 에너지가</tgt>` | 1822 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 941 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, </src><tgt>다른 종류의 에너지로</tgt>` | 1735 |
| 9 | `<src>like heat or light, </src><tgt><\|wait\|></tgt>` | `<src>like heat or light. </src><tgt><\|wait\|></tgt>` | 2042 |
| 10 | `<src><\|wait\|></src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>Or gets used </src><tgt>변환됩니다. 예를 들어 열이나 빛 같은 거죠.</tgt>` | 2218 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 1638 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용되기도 합니다.</tgt>` | 1858 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or or if you have </src><tgt><\|wait\|></tgt>` | 1201 |
| 2 | `<src>have to produce </src><tgt>それか、</tgt>` | `<src>to produce </src><tgt>あるいは、</tgt>` | 912 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1610 |
| 4 | `<src>write a text, </src><tgt>何か文章を書かなきゃいけないとき、テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>何かを書き出す必要がある場合、テキストを</tgt>` | 2090 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1412 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know </src><tgt>書くとき、</tgt>` | 1124 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1755 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. It's like, oh, is </src><tgt>スペルが全くわからないことに気づくかもしれません。「あ、</tgt>` | 2251 |
| 9 | `<src>is this word </src><tgt><\|wait\|></tgt>` | `<src>this word </src><tgt><\|wait\|></tgt>` | 1857 |
| 10 | `<src>spelled with a double </src><tgt>この単語って、</tgt>` | `<src>spelled with a double </src><tgt>この単語、</tgt>` | 2040 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1669 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>p, double l, I don't know. </src><tgt>doublep、doublel、わからない」って感じですね。</tgt>` | 920 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1254 |

---

### Test Example 29 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1233 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在这个</src><tgt>皆さんにお伝えしたいのですが、</tgt>` | 1061 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，</src><tgt><\|wait\|></tgt>` | 1522 |
| 4 | `<src>不是一天造成的，</src><tgt>ローマは一日にして成らずと言いますよね。</tgt>` | `<src>不是一天造成的，</src><tgt>このローマは一日にしてできたものではなく、</tgt>` | 2225 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1415 |
| 6 | `<src>你现在</src><tgt>だから、今皆さんが</tgt>` | `<src>你现在</src><tgt>ですから、</tgt>` | 845 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 805 |
| 8 | `<src>危机啊，跟风险</src><tgt>直面している</tgt>` | `<src>遗迹啊</src><tgt>今あなたが直面している遺産や</tgt>` | 1863 |
| 9 | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | `<src>跟风景，</src><tgt><\|wait\|></tgt>` | 1400 |
| 10 | `<src>一夕之间就</src><tgt>危機やリスクも、一朝一夕で</tgt>` | `<src>也不可能是你</src><tgt>風景も、</tgt>` | 1921 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夜之间就</src><tgt><\|wait\|></tgt>` | 2005 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的。</src><tgt>一晩で変化したものではありません。</tgt>` | 1715 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>因此，</src><tgt><\|wait\|></tgt>` | 507 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>そこで、酉年生まれの皆さんには…</tgt>` | `<src>会见习属期的朋友呢，</src><tgt>ですから、見習属の皆さん、</tgt>` | 1740 |

---

### Test Example 30 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>二十</src><tgt><\|wait\|></tgt>` | 1077 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>二日とか</src><tgt>二十二号</tgt>` | 820 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>でした。恐らく</src><tgt><\|wait\|></tgt>` | 1530 |
| 4 | `<src>十秒で。</src><tgt>大概十一二手吧。差不多十秒。</tgt>` | `<src>十秒で</src><tgt>左右吧。大概十秒</tgt>` | 1245 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1093 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一秒に</src><tgt>一秒</tgt>` | 1270 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1310 |
| 8 | `<src>計算ですか</src><tgt>一秒一手多一点</tgt>` | `<src>時間ですかね。</src><tgt>左右的时间吧。</tgt>` | 1784 |
| 9 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1555 |
| 10 | `<src>でなんか</src><tgt>这样算。然后</tgt>` | `<src>でなんか</src><tgt>然后</tgt>` | 735 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐ろしく</src><tgt><\|wait\|></tgt>` | 1878 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一日</src><tgt>十一号</tgt>` | 1946 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>で</src><tgt><\|wait\|></tgt>` | 1042 |
| 14 | `<src>あの</src><tgt>十一二手的时候，</tgt>` | `<src>あの</src><tgt>那个，</tgt>` | 1051 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | 1442 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>因为宫马什么的。</tgt>` | 464 |

---

### Test Example 31 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1041 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt>Vanadium and these things</tgt>` | 1887 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 1000일인가 </src><tgt><\|wait\|></tgt>` | 1415 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt>are about 1,000</tgt>` | 1501 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>거진 600일 정도 </src><tgt><\|wait\|></tgt>` | 1698 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>오긴 하지, </src><tgt>or maybe 600, right?</tgt>` | 1368 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1417 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연 업 미네랄이다 </src><tgt>They're definitely minerals.</tgt>` | 1889 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1807 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt>They're the kind of minerals you'd talk about</tgt>` | 2148 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 1746 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>about that. And then, on top of that,</tgt>` | 1563 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 586 |

---

### Test Example 32 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 938 |
| 2 | `<src>我们可以看到的是</src><tgt>이 부분에서는</tgt>` | `<src>最长的部分呢？</src><tgt>가장 긴 부분은요?</tgt>` | 1577 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是一个</src><tgt><\|wait\|></tgt>` | 1132 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴雪的人，但是他是</src><tgt>우리가 보는 건 눈을 쓴 사람인데, 그 사람이</tgt>` | 2799 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>属于逆向的，</src><tgt><\|wait\|></tgt>` | 1262 |
| 6 | `<src>所以</src><tgt>이게 역방향이에요. 그래서</tgt>` | `<src>所以</src><tgt>역방향에 속하니까</tgt>` | 965 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通场我们这样的一个状况</src><tgt><\|wait\|></tgt>` | 1819 |
| 8 | `<src>时候，就要去</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>的需要去</src><tgt>이런 상황에서는</tgt>` | 1588 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别的注意是</src><tgt><\|wait\|></tgt>` | 1856 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt>그 사람이</tgt>` | 1276 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>能够得到</src><tgt><\|wait\|></tgt>` | 1135 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>与他吊不到</src><tgt>그에게</tgt>` | 1692 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1769 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>哦。</src><tgt>당신의 의식을</tgt>` | 1087 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>There were </src><tgt>没什么新鲜的。</tgt>` | `<src><\|wait\|></src><tgt>没什么新鲜事，</tgt>` | 1182 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there were </src><tgt><\|wait\|></tgt>` | 1404 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances before </src><tgt>以前也有过这样的情况，</tgt>` | 1652 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1447 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>netFilterTC, </src><tgt>就是netFilterTC，</tgt>` | 1448 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>and so </src><tgt><\|wait\|></tgt>` | 1675 |
| 8 | `<src>this is just </src><tgt>所以这只是</tgt>` | `<src><\|wait\|></src><tgt>所以</tgt>` | 1383 |
| 9 | `<src>one another place </src><tgt><\|wait\|></tgt>` | `<src>this is just one another place </src><tgt><\|wait\|></tgt>` | 978 |
| 10 | `<src>to look at. </src><tgt>另一个需要关注的地方。</tgt>` | `<src>where we </src><tgt>这只是另一个地方，</tgt>` | 1892 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1961 |
| 12 | `<src><\|wait\|></src><tgt>但</tgt>` | `<src>bad developed </src><tgt>我们</tgt>` | 840 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>this </src><tgt><\|wait\|></tgt>` | 1268 |
| 14 | `<src>working on BugRepo </src><tgt>开发人员或在BugRepo工作的工程师</tgt>` | `<src>plugin, and this plugin </src><tgt>开发了这个插件，这个插件</tgt>` | 1768 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be available. </src><tgt><\|wait\|></tgt>` | 1145 |

---

### Test Example 34 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | 1343 |
| 2 | `<src>just getting going </src><tgt>それは始めたばかりの人が</tgt>` | `<src>just getting going </src><tgt>今まさに</tgt>` | 971 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get </src><tgt><\|wait\|></tgt>` | 1552 |
| 4 | `<src><\|wait\|></src><tgt>手に入れるべき</tgt>` | `<src><\|wait\|></src><tgt>スタートを切ろうとしている人、</tgt>` | 1528 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1712 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that you're really </src><tgt>本当に</tgt>` | 1292 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>important. </src><tgt><\|wait\|></tgt>` | 1292 |
| 8 | `<src><\|wait\|></src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src><\|wait\|></src><tgt>大事な人たちが10人います。</tgt>` | 1457 |
| 9 | `<src>I'm going to go into. </src><tgt><\|wait\|></tgt>` | `<src>I'm going to go into </src><tgt><\|wait\|></tgt>` | 1305 |
| 10 | `<src>I have about </src><tgt>それについてお話ししていきます。</tgt>` | `<src><\|wait\|></src><tgt>そのうちの1人について</tgt>` | 1914 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>I have about one minute videos </src><tgt><\|wait\|></tgt>` | 1979 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video. </src><tgt>1分程度の動画を1つ紹介します。</tgt>` | 1815 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>They cover each one </src><tgt><\|wait\|></tgt>` | 922 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src><\|wait\|></src><tgt>それぞれの動画は、</tgt>` | 1177 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>in a little more detail, </src><tgt><\|wait\|></tgt>` | 1436 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 925 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，XJML</src><tgt>呃，</tgt>` | 1213 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 </src><tgt><\|wait\|></tgt>` | 1418 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피트어도 </src><tgt>XJML</tgt>` | 1508 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1669 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>这个Compit，</tgt>` | 1293 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1552 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴피트 어 언어 의 </src><tgt>也是可以理解的，</tgt>` | 1565 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 927 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 에 맞게 우리 가 이제 </src><tgt>符合Compit语言的语法，</tgt>` | 2247 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1903 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>我们现在需要编写代码，</tgt>` | 1829 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1381 |
| 14 | `<src>프로그램 이 </src><tgt>编写代码</tgt>` | `<src>작성 하는 프로그램 이 </src><tgt>编写这些代码的程序</tgt>` | 624 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 1367 |

---

### Test Example 36 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 883 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>そのうち150万社が、従業員数</tgt>` | `<src>백오십만 개가 중고 번에서 </src><tgt>そのうち150万個は中古販売で</tgt>` | 2251 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>1천 미만 으로 </src><tgt><\|wait\|></tgt>` | 1248 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>10人未満の非常に小さな</tgt>` | `<src>4, 500여 개 기업 들이 </src><tgt>1000個未満で450個程度の企業が</tgt>` | 2493 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1169 |
| 6 | `<src>일반 적으로는 </src><tgt>企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>多くありました。一般的には</tgt>` | 1717 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1607 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>小規模な企業は成長するか廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>中小企業は成長するか、あるいは</tgt>` | 958 |
| 9 | `<src>걷게 되는데 </src><tgt><\|wait\|></tgt>` | `<src>폐업 해 길게 되는데 </src><tgt><\|wait\|></tgt>` | 1922 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>歩むものですが、日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>廃業して長引くことが多いのですが、これは</tgt>` | 2137 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>소기업 들은 </src><tgt><\|wait\|></tgt>` | 1642 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>成長も廃業もしないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>中小企業は成長も廃業もしない</tgt>` | 1852 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1543 |

---

### Test Example 37 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1207 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어디 를 보면 </src><tgt>呃，</tgt>` | 824 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1680 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 이런 </src><tgt>看，</tgt>` | 1090 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>존생이 자, 그래도 </src><tgt><\|wait\|></tgt>` | 1696 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>가족 같은 </src><tgt>那些和20岁一起长大的朋友，</tgt>` | 1397 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1155 |
| 8 | `<src>그러니까 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src>그러니까 </src><tgt>就像是亲弟弟一样。所以</tgt>` | 1820 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1486 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 감보 단은 </src><tgt>再生感宝</tgt>` | 1967 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1344 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt>自己</tgt>` | 959 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1583 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt>多一点，</tgt>` | 1168 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>잘 넣어 놓고 </src><tgt><\|wait\|></tgt>` | 946 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>생각 했습니다. </src><tgt>我多加了一些，觉得会更亲切。</tgt>` | 1646 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 983 |
| 2 | `<src>알거니와 너희 가 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>알거니와, </src><tgt>あなたたちも知っているでしょう、</tgt>` | 1805 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>너희 가 </src><tgt><\|wait\|></tgt>` | 907 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인으로 있을 때에 </src><tgt>異邦人としている時に</tgt>` | 2349 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1406 |
| 6 | `<src>우상에게로 </src><tgt>ものを言わない偶像に</tgt>` | `<src>말 못 하는 우선에게로 </src><tgt>言葉を</tgt>` | 1122 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그대로 </src><tgt><\|wait\|></tgt>` | 1645 |
| 8 | `<src>끌려 갔느니라. </src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>그려 갔느니라. </src><tgt>伝えるべき優先にそのまま描いていったのです。</tgt>` | 1977 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1855 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 내가 </src><tgt>ですから、私が</tgt>` | 1958 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | 676 |
| 12 | `<src>알리 노니 </src><tgt>あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>あなたたちに知らせるのです。</tgt>` | 1556 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt><\|wait\|></tgt>` | 1630 |
| 14 | `<src>말하는 자는. </src><tgt>神の霊によって語る者は、</tgt>` | `<src>영으로 </src><tgt>神の霊によって</tgt>` | 1119 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 824 |

---

### Test Example 39 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 902 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>砸到了一个铁头，</src><tgt>鉄の塊にぶつかって、</tgt>` | 1903 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt><\|wait\|></tgt>` | 802 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>打到了铁头之后，</src><tgt>もし鉄の塊にぶつかったら、</tgt>` | 2672 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必</src><tgt><\|wait\|></tgt>` | 1141 |
| 6 | `<src><\|wait\|></src><tgt>必ず利益を</tgt>` | `<src>抓前</src><tgt>必ず</tgt>` | 974 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>手阻，</src><tgt><\|wait\|></tgt>` | 1740 |
| 8 | `<src>不要想说，哎，那我再</src><tgt>確保してください。</tgt>` | `<src>不要想说哎，</src><tgt>前手をガードしてください。そうすると、</tgt>` | 1952 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我再去操作</src><tgt><\|wait\|></tgt>` | 2035 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>下去哦。</src><tgt>「あ、また操作しなきゃ」なんて思わないようにしてください。</tgt>` | 2319 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1597 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？</src><tgt>なぜそんなことを言うのか？</tgt>` | 1802 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1219 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt>それはですね、</tgt>` | 726 |

---

### Test Example 40 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어 가면 </src><tgt><\|wait\|></tgt>` | 1272 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>进去之后会迷路。</tgt>` | 1529 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1226 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하려고 은 </src><tgt>想开车</tgt>` | 1251 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>걸어 걸어다니 고 </src><tgt><\|wait\|></tgt>` | 1873 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>있으면 </src><tgt>却只能走走停停，</tgt>` | 1373 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 을 가면 </src><tgt><\|wait\|></tgt>` | 1724 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>去江北就不用说了，去外国</tgt>` | `<src>말할 것도 없고 </src><tgt>更别提去江北了，</tgt>` | 1957 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>외국 에 나가 면 또 장렬이에요. </src><tgt><\|wait\|></tgt>` | 1058 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>좀 </src><tgt>出国的话就真的惨了。</tgt>` | 1369 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>신기 하네요. </src><tgt><\|wait\|></tgt>` | 2013 |
| 12 | `<src>대신 에 </src><tgt>真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>挺神奇的。不如现在</tgt>` | 1791 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1268 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>무뤄봐요. 그거 는 </src><tgt>努力做个“无聊”吧。那</tgt>` | 831 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>안 된 것 같아요. </src><tgt><\|wait\|></tgt>` | 1370 |
| 16 | `<src><\|wait\|></src><tgt>这一点倒是做得还行。</tgt>` | `<src><\|wait\|></src><tgt>好像没戏。</tgt>` | 670 |

---

### Test Example 41 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1192 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう蒸らせてやるよ。</src><tgt>그럼 그냥 쪄 죽여버리겠어.</tgt>` | 2007 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 812 |
| 4 | `<src><\|wait\|></src><tgt>난</tgt>` | `<src>今</src><tgt>나는 지금</tgt>` | 1209 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き地を見ている。</src><tgt><\|wait\|></tgt>` | 1678 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>그 지도를 보고 있어.</tgt>` | 1488 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1134 |
| 8 | `<src><\|wait\|></src><tgt>이미</tgt>` | `<src>超に超えている</src><tgt>한계가</tgt>` | 1240 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt><\|wait\|></tgt>` | `<src>不烈火勢力よ。</src><tgt><\|wait\|></tgt>` | 1672 |
| 10 | `<src><\|wait\|></src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src><\|wait\|></src><tgt>아주, 아주, 아주 넘어서 버린 불멸의 세력이야.</tgt>` | 2252 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1865 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船団大攻を</src><tgt>오랜 기간 동안</tgt>` | 1711 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src>やってるだろ。</src><tgt><\|wait\|></tgt>` | 1413 |
| 14 | `<src>俺は</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>俺はこんなに</src><tgt>선단 대공을 치고 있었잖아.</tgt>` | 743 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>すごい海賊船を</src><tgt><\|wait\|></tgt>` | 1369 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>나는 이렇게 대단한 해적선을 본 적이 없어.</tgt>` | 1012 |

---

### Test Example 42 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1216 |
| 2 | `<src>这个月财运可以说是</src><tgt>金運ですが、今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>金運についてですが、今月は</tgt>` | 1778 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>还不错的，但是</src><tgt><\|wait\|></tgt>` | 856 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>かなり良いです。ただ、どちらかというと本業の収入、</tgt>` | `<src>比较偏向正财</src><tgt>悪くないですね。ただ、</tgt>` | 2069 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分。也就是说，</src><tgt><\|wait\|></tgt>` | 1518 |
| 6 | `<src>在事业方面的</src><tgt>つまり仕事の</tgt>` | `<src>在事业方面</src><tgt>正月の運気は少し弱いかもしれません。つまり、仕事運は</tgt>` | 1154 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长</src><tgt><\|wait\|></tgt>` | 1746 |
| 8 | `<src>与收入的</src><tgt>業績成長によるボーナスや昇給の運気が</tgt>` | `<src>带来的红利</src><tgt>業績アップによる恩恵や</tgt>` | 1904 |
| 9 | `<src>提升。如果是在</src><tgt><\|wait\|></tgt>` | `<src>和收入的提升。如果</src><tgt><\|wait\|></tgt>` | 2022 |
| 10 | `<src>投资理财方面呢，</src><tgt>強めです。投資や資産運用についても、</tgt>` | `<src>在投资理财方面，</src><tgt>収入アップによる恩恵です。投資や資産運用に関しては、</tgt>` | 2221 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1532 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错的，</src><tgt>今月も悪くないですね。</tgt>` | 1389 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对正财来说，</src><tgt><\|wait\|></tgt>` | 712 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>ただ、正月の運気と比べると、少し</tgt>` | 1681 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt><\|wait\|></tgt>` | 841 |

---

### Test Example 43 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1225 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1062 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1563 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt>실제로</tgt>` | 1292 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 1658 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | 2028 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1882 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. </src><tgt>그게 한 단계의 학력 수준입니다.</tgt>` | 1735 |
| 9 | `<src>to college, </src><tgt><\|wait\|></tgt>` | `<src>Did you go to college? </src><tgt><\|wait\|></tgt>` | 2049 |
| 10 | `<src>and if so, did you graduate? </src><tgt>대학에 진학하셨나요? 그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, </src><tgt>대학까지 가셨나요? 만약 그렇다면,</tgt>` | 2130 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>did you graduate? </src><tgt><\|wait\|></tgt>` | 1694 |
| 12 | `<src>attainment. </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of attainment. </src><tgt>졸업하셨나요? 그게 또 다른 단계의 학력 수준입니다.</tgt>` | 1856 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1126 |
| 14 | `<src>now. I'll see you </src><tgt>그럼 오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>지금은 여기까지입니다. 곧</tgt>` | 1193 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 444 |

---

### Test Example 44 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>ですから、もちろん</tgt>` | 832 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1878 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>あります。Aさんと</tgt>` | `<src>A라는 사람 과 </src><tgt>このようなケースはあります。Aさんとは</tgt>` | 1979 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1529 |
| 6 | `<src>컨설턴트예요, </src><tgt>Bさんはお互いに</tgt>` | `<src>서로 콘텐츠 예요. </src><tgt>Bさんとコンテンツを共有しています。</tgt>` | 1138 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 콘텐츠 예요 </src><tgt><\|wait\|></tgt>` | 1993 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>이렇게 되고 </src><tgt>このようにコンテンツを共有しています。</tgt>` | 1781 |
| 9 | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1820 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>Aさんが何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>Aさんが悪意のあるコードを</tgt>` | 843 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1726 |
| 12 | `<src>B라는 사람 이 </src><tgt>配布したとします。その場合、Bさんは</tgt>` | `<src>비라는 사람 이 </src><tgt>送ったとき、Bさんが</tgt>` | 1729 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1730 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>実際のクロスサイトスクリプティングから</tgt>` | `<src>크로스 사이트 크리티에서 </src><tgt>クロスサイトクリティカルから</tgt>` | 1248 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>JSP까지 </src><tgt><\|wait\|></tgt>` | 787 |
| 16 | `<src>감염 이 될까. </src><tgt>EXEファイルまで感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까. </src><tgt>JSPまで感染してしまうのか。</tgt>` | 863 |

---

### Test Example 45 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>そしてこれについて多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>そして、これについて多くの人が</tgt>` | 1419 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 해놓았습니다. </src><tgt><\|wait\|></tgt>` | 1282 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>出しています。こちらの</tgt>` | `<src>여기 </src><tgt>分析をしています。ここで</tgt>` | 1543 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>이 로쿠 자의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1981 |
| 6 | `<src>소니가 </src><tgt>ロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>このロクジャの分析を見ると、ソニーが</tgt>` | 1109 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>UHD에 </src><tgt><\|wait\|></tgt>` | 1838 |
| 8 | `<src>파이프 를 </src><tgt>26ビットFPパイプを</tgt>` | `<src>FP 파이프 를 </src><tgt>UHDFPファームを</tgt>` | 1925 |
| 9 | `<src>128비트로 낮춘 </src><tgt><\|wait\|></tgt>` | `<src>128비트 로 </src><tgt><\|wait\|></tgt>` | 1955 |
| 10 | `<src>것으로 보인다. </src><tgt>128ビットに下げたようです。</tgt>` | `<src>나중 가서 </src><tgt>128ビットに後から</tgt>` | 2007 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>로 보인 다. </src><tgt><\|wait\|></tgt>` | 1439 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스 박스 시리즈, </src><tgt>見せるようです。Xboxシリーズ、</tgt>` | 767 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt><\|wait\|></tgt>` | 1627 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>XboxにもないInfinityCache、</tgt>` | 1314 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>L시가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 934 |
| 16 | `<src><\|wait\|></src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src><\|wait\|></src><tgt>LSiもここにはありません。</tgt>` | 606 |

---

### Test Example 46 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1217 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt>推し量る</tgt>` | 1325 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1334 |
| 4 | `<src>真实意图的，</src><tgt>相手の感情や本当の意図を察したり推し量ったり</tgt>` | `<src>或真挚意图的，</src><tgt>相手の感情や真意を察知する。</tgt>` | 2630 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1232 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1032 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 8 | `<src>会听到人们</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>后经场会提到</src><tgt>後世の場では</tgt>` | 1906 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src>人们这样说：“</src><tgt><\|wait\|></tgt>` | 1941 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 2005 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1677 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了。”</src><tgt>この人はまた嘘をついているよ」と言う。</tgt>` | 651 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1512 |
| 14 | `<src>已经说明了一切。”</src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>彼の目はすべてを物語っている。</tgt>` | 1287 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 713 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是</src><tgt>つまり、</tgt>` | 657 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说：“</src><tgt><\|wait\|></tgt>` | 698 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1293 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt>So, this is</tgt>` | 1362 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>っていうやつでやって、</src><tgt><\|wait\|></tgt>` | 1252 |
| 4 | `<src><\|wait\|></src><tgt>This isn't just a visual development environment;</tgt>` | `<src>ビジュアルパイソン</src><tgt>a visual development environment. We use it to</tgt>` | 2265 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1528 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのも</src><tgt>develop with Visual Python.</tgt>` | 1105 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルに書いて</src><tgt><\|wait\|></tgt>` | 1961 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>あとそれは</src><tgt>The reason is that</tgt>` | 1603 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードがそっから生成される</src><tgt><\|wait\|></tgt>` | 2140 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>ってやつ、それが</src><tgt>the visual flow graph is written in Visual, and the Python code is generated from it.</tgt>` | 2414 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1494 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>When it runs, signal processing happens.</tgt>` | 1703 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>こういうことになっているから</src><tgt><\|wait\|></tgt>` | 1118 |
| 14 | `<src><\|wait\|></src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>です。</src><tgt>That's how it works.</tgt>` | 806 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 776 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay,</tgt>` | 693 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1189 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>The stock index</tgt>` | 952 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 1633 |
| 4 | `<src>이런 대형주 도 </src><tgt>If the stock index shows an upward trend, these large- cap stocks</tgt>` | `<src>이러 면 대형 주도 </src><tgt>is rising, then</tgt>` | 2112 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1408 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>어 큰 폭의 상승 을 </src><tgt>the large- cap stocks</tgt>` | 1001 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 먼저 </src><tgt><\|wait\|></tgt>` | 1860 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 </src><tgt>will see a sharp rise, but first</tgt>` | 2061 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 2071 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt>the light- cap stocks</tgt>` | 2045 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | 1817 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 </src><tgt>lead the market, so</tgt>` | 1749 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1099 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt>the market cap of the light- cap stocks</tgt>` | 1109 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈으로 봐야 </src><tgt><\|wait\|></tgt>` | 593 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>will always be the one to watch.</tgt>` | 880 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then </src><tgt>活動、それから</tgt>` | 1215 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1481 |
| 4 | `<src>the standard is because you're </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>the standard is, because you're </src><tgt>自分たちで「標準」って何だと思うかを定義するんです。だって、</tgt>` | 2881 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | 1259 |
| 6 | `<src>but the reality </src><tgt>完全に正しいのです。しかし現実には、</tgt>` | `<src>but the reality </src><tgt>その考えは完全に正しい。でも、</tgt>` | 1058 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is that </src><tgt><\|wait\|></tgt>` | 1438 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>現実には、</tgt>` | 1857 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>on the block, and because </src><tgt><\|wait\|></tgt>` | 2105 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>私たちが新しいカタカナの登場人物だから。そして、</tgt>` | 2279 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1573 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前に変わった基準が</tgt>` | 1740 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1162 |
| 14 | `<src>a higher standard because </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、より高い基準を求められています。なぜなら、</tgt>` | `<src>our own standard </src><tgt>私たちの基準に</tgt>` | 790 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt><\|wait\|></tgt>` | 832 |
| 16 | `<src>held to a higher standard. </src><tgt>今はすべてがより高い基準を求められているからです。</tgt>` | `<src>is being held to higher </src><tgt>より高い基準が</tgt>` | 883 |

---

### Test Example 50 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 1142 |
| 2 | `<src><\|wait\|></src><tgt>これはすごく</tgt>` | `<src>이거 이 저 </src><tgt>これ、これ、これ、</tgt>` | 1562 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>일할 수 있지만 </src><tgt><\|wait\|></tgt>` | 1137 |
| 4 | `<src><\|wait\|></src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>진짜 보살 도요 </src><tgt>これ、これ、これ、</tgt>` | 2264 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 가 </src><tgt><\|wait\|></tgt>` | 1516 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>보살 인데 꿈일 </src><tgt>これ、これ、これ、</tgt>` | 1242 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 보이 고 </src><tgt><\|wait\|></tgt>` | 1659 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>ある？他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt>これ、これ、これ、</tgt>` | 1748 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt><\|wait\|></tgt>` | `<src>보살 로 보이 려고 </src><tgt><\|wait\|></tgt>` | 2064 |
| 10 | `<src>지금 나한테 </src><tgt>ある？宇宙が今、私に</tgt>` | `<src>보이 서 우주 가 지지 않아. 이때 보살 이라는 </src><tgt>これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ、これ` | 9145 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 492 |

---

### Test Example 51 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1166 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 923 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1701 |
| 4 | `<src>move media objects </src><tgt>你没法</tgt>` | `<src>move media objects </src><tgt>您将无法</tgt>` | 1328 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1632 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt>在资源之间移动媒体对象，</tgt>` | 1576 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>so if </src><tgt><\|wait\|></tgt>` | 1681 |
| 8 | `<src>you get into </src><tgt>所以，如果</tgt>` | `<src>you get into </src><tgt>所以如果</tgt>` | 1289 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation where you </src><tgt><\|wait\|></tgt>` | 1033 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>realize you've added </src><tgt>您发现</tgt>` | 1935 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 2004 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>将错误的媒体文件添加到了某个资源中，</tgt>` | 2011 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know. </src><tgt><\|wait\|></tgt>` | 1746 |
| 14 | `<src>and we can see about </src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src>Now, and we can see about </src><tgt>请务必通知我们。我们</tgt>` | 1112 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 840 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>moving those media files and then making sure </src><tgt>可以帮您移动这些媒体文件，并确保</tgt>` | 1083 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>they get backed up </src><tgt><\|wait\|></tgt>` | 655 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>properly. </src><tgt>它们得到正确备份。</tgt>` | 524 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>首次觉知到</src><tgt>프로이트가 처음으로</tgt>` | `<src>FourthE的阻止决策</src><tgt>FourthE의</tgt>` | 1322 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>到的那个现象，</src><tgt><\|wait\|></tgt>` | 1366 |
| 4 | `<src>每当我们</src><tgt>그 현상을 알아차렸습니다. 우리가</tgt>` | `<src>美登们</src><tgt>차단 결정 현상에 대해, 미등들은</tgt>` | 2397 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1412 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>处于艾知中</src><tgt>A지</tgt>` | 1113 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所位的艾。</src><tgt><\|wait\|></tgt>` | 1716 |
| 8 | `<src>我们也</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는</tgt>` | `<src>我们</src><tgt>중의 A에 위치해 있습니다. 우리는</tgt>` | 1828 |
| 9 | `<src>同时进入恨。</src><tgt><\|wait\|></tgt>` | `<src>也同时</src><tgt><\|wait\|></tgt>` | 2076 |
| 10 | `<src><\|wait\|></src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>进入恨，</src><tgt>동시에 H에 진입합니다.</tgt>` | 2033 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>在掌上的时候，</src><tgt><\|wait\|></tgt>` | 1721 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>它是在艾。</src><tgt>손바닥에 닿으면 A에 있습니다.</tgt>` | 1528 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 579 |
| 14 | `<src>它就变成恨。</src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>它就变成恨。</src><tgt>밤이 되면 H로 바뀝니다.</tgt>` | 1628 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 848 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆。</src><tgt>그 시계추 말입니다.</tgt>` | 713 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续</src><tgt><\|wait\|></tgt>` | 536 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>在移动。</src><tgt>계속 움직입니다.</tgt>` | 368 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1494 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt>私は</tgt>` | 868 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>on the first section about </src><tgt><\|wait\|></tgt>` | 1658 |
| 4 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src><\|wait\|></src><tgt>最初のセクションについて少し混乱していました。</tgt>` | 1665 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>the AHR field </src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src>being of </src><tgt>AHRの</tgt>` | 1099 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>critical importance </src><tgt><\|wait\|></tgt>` | 737 |
| 8 | `<src>versus variant </src><tgt>決定的な重要性と、</tgt>` | `<src>versus </src><tgt>重要性について、</tgt>` | 1622 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1756 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt>バリアントデータベースとの対比についてです。</tgt>` | 1930 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously to my loves. </src><tgt><\|wait\|></tgt>` | 1020 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt>それは、私の愛する人たちにとって明らかです。もし</tgt>` | 1654 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree </src><tgt><\|wait\|></tgt>` | 1565 |
| 14 | `<src>upon the fields that need </src><tgt>つまり、</tgt>` | `<src>upon the fields </src><tgt>フィールドについて合意できなければ、</tgt>` | 1670 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in these </src><tgt><\|wait\|></tgt>` | 1122 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources </src><tgt>これらのデータソースに</tgt>` | 824 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>that we can draw from, </src><tgt><\|wait\|></tgt>` | 839 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>アクセスできるフィールドがなければ、それから何も引き出せませんよね？</tgt>` | 1174 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 461 |

---

### Test Example 54 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1294 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful, </src><tgt>有意义的、</tgt>` | 818 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>individual right, </src><tgt><\|wait\|></tgt>` | 1517 |
| 4 | `<src>and the Supreme Court </src><tgt>个人权利，而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt>个人权利，</tgt>` | 1213 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along last, </src><tgt><\|wait\|></tgt>` | 1250 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>not leading. And I don't know </src><tgt>最高法院最后才介入，而不是主导。我不知道</tgt>` | 2074 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1006 |
| 8 | `<src><\|wait\|></src><tgt>我不认为</tgt>` | `<src>the the van </src><tgt>法院是否想</tgt>` | 1611 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>ard of </src><tgt><\|wait\|></tgt>` | 1658 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>成为社会变革的先锋。</tgt>` | 1967 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days. </src><tgt><\|wait\|></tgt>` | 1627 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>But they rather </src><tgt>但现在，他们更倾向于</tgt>` | 852 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>reflect </src><tgt><\|wait\|></tgt>` | 1630 |
| 14 | `<src>the consensus </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt>反映</tgt>` | 1283 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the consensus that's already </src><tgt><\|wait\|></tgt>` | 659 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>已经形成的共识。</tgt>` | 1371 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt><\|wait\|></tgt>` | 638 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt>所以，</tgt>` | 582 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 698 |
| 20 | `<src><\|wait\|></src><tgt>有些联邦法官……</tgt>` | `<src><\|wait\|></src><tgt>你有一些联邦法官，</tgt>` | 540 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 391 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 977 |
| 2 | `<src>he knows Jesus </src><tgt>ある時、彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>ある時、彼は</tgt>` | 1124 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is a son of Henry, </src><tgt><\|wait\|></tgt>` | 1475 |
| 4 | `<src>He knows that </src><tgt>空腹だと知っています。</tgt>` | `<src>he knows that </src><tgt>イエスがヘンリーの息子だと知っていました。</tgt>` | 2279 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's Jude Powell's </src><tgt><\|wait\|></tgt>` | 1563 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>son of the wilderness </src><tgt>そして、彼はユダ・パウエルが</tgt>` | 1426 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>sermon today is that he's Henry. </src><tgt><\|wait\|></tgt>` | 2263 |
| 8 | `<src>And so he says </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼は</tgt>` | `<src>And so he says to </src><tgt>今日説教でヘンリーの息子だと述べていることを知っていました。だから彼は</tgt>` | 1570 |
| 9 | `<src>to Jesus," Hey, </src><tgt><\|wait\|></tgt>` | `<src>Jesus, say, </src><tgt><\|wait\|></tgt>` | 1506 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>イエスに言うんです。「おい、お前が神の子なら、証明してみろよ。</tgt>` | `<src>if you're a son of God, </src><tgt>イエスに言ったのです。「もしあなたが神の息子なら、</tgt>` | 2597 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>prove it. </src><tgt><\|wait\|></tgt>` | 1293 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread. </src><tgt>証明してみせなさい。この石をパンに変えなさい。</tgt>` | 1830 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1304 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>just deal with that </src><tgt>彼はどうやって</tgt>` | 681 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>temptation? </src><tgt><\|wait\|></tgt>` | 710 |
| 16 | `<src><\|wait\|></src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>Man, </src><tgt>その誘惑に立ち向かったのか？いやはや、</tgt>` | 895 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by </src><tgt><\|wait\|></tgt>` | 470 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>a brother alone. </src><tgt>ジョナタンは兄を一人で導いた。</tgt>` | 530 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1147 |
| 2 | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그럼 사진을 한번 볼게요.</tgt>` | 1442 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1227 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>사진 부분은</tgt>` | 1467 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1575 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>客订的部分，</src><tgt>고객 주문 부분이에요.</tgt>` | 1449 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>但客订一般</src><tgt><\|wait\|></tgt>` | 1728 |
| 8 | `<src>都是属于</src><tgt>거실은 보통</tgt>` | `<src>都是</src><tgt>보통은</tgt>` | 1552 |
| 9 | `<src>我们</src><tgt><\|wait\|></tgt>` | `<src>属于我们要</src><tgt><\|wait\|></tgt>` | 804 |
| 10 | `<src>在休息的地方，</src><tgt>우리가 쉬는 곳이잖아요.</tgt>` | `<src>休息的地方，</src><tgt>쉬는 시간이에요.</tgt>` | 1956 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1946 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>这是身体的部分</src><tgt>그래서 이건</tgt>` | 1671 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 596 |
| 14 | `<src>你需要给自己</src><tgt>이 신체 부위도 여러분이 자신에게</tgt>` | `<src>你需要给自己</src><tgt>자기 자신에게</tgt>` | 1522 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间</src><tgt><\|wait\|></tgt>` | 1096 |
| 16 | `<src>可以好好的</src><tgt>시간을 내서</tgt>` | `<src>可以好好地</src><tgt>충분한 시간을</tgt>` | 807 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>坐下来休息，</src><tgt><\|wait\|></tgt>` | 798 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可由我们可以看到</src><tgt>앉아서 쉴 수 있는 시간이에요. 그리고</tgt>` | 924 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是存放一人的嘛。</src><tgt><\|wait\|></tgt>` | 538 |
| 20 | `<src>啊，</src><tgt>아무도 없네요.</tgt>` | `<src>好，</src><tgt>여기는 한 사람을 위한 공간이에요. 자,</tgt>` | 459 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>说说。</src><tgt><\|wait\|></tgt>` | 330 |

---

### Test Example 57 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1385 |
| 2 | `<src><\|wait\|></src><tgt>目を閉じて。</tgt>` | `<src>색인 번호 를 </src><tgt>目を閉じて、</tgt>` | 1443 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>빌 거야. </src><tgt><\|wait\|></tgt>` | 1234 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt>私が祈るから。</tgt>` | `<src>옛날 서름이 </src><tgt>色番号を借りるんだ。</tgt>` | 1897 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>돋든 차리 돋든 </src><tgt><\|wait\|></tgt>` | 1914 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>昔の書物でも、何かの手がかりでも、何か感じ取れたら、</tgt>` | 2166 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1233 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>これを振って。一緒に遊ぼうって合図だから。</tgt>` | `<src>같이 놀자는 거야. </src><tgt>それを振って一緒に遊ぼうってことなんだ。</tgt>` | 1362 |
| 9 | `<src>귀신 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 1759 |
| 10 | `<src>물릴 거고 </src><tgt>霊が来たら噛みつかれるし、</tgt>` | `<src>너무 많이 올릴 거고 </src><tgt>お化けがすごくたくさん出てくるし、</tgt>` | 2128 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>시녀 님이야 </src><tgt><\|wait\|></tgt>` | 1757 |
| 12 | `<src>너 지켜 주라고 </src><tgt>神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘さん、お化けの娘` | 6716 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>안 그러니까 </src><tgt>だから守ってって言ってるんだから、</tgt>` | 347 |
| 14 | `<src>편안 한 마음 에 </src><tgt>突いてくれるから、安心して</tgt>` | `<src>편안 마음 에 </src><tgt><\|wait\|></tgt>` | 351 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt>リラックスして目を閉じて。</tgt>` | 332 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=2 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 953 |
| 2 | `<src>completely rare, </src><tgt>こうした人々は非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>これらの人々は全く珍しく、</tgt>` | 1448 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1233 |
| 4 | `<src>show up to </src><tgt>そして、</tgt>` | `<src>grow up </src><tgt>多くの場合</tgt>` | 1264 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1621 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革する。</tgt>` | 1593 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1697 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 1584 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt><\|wait\|></tgt>` | 832 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt>矛盾をはらんでいる。</tgt>` | 1986 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 2008 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的ではあるが、</tgt>` | 1808 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1334 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations </src><tgt>無意味な会話を</tgt>` | 659 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1371 |
| 16 | `<src><\|wait\|></src><tgt>そして、</tgt>` | `<src>and like to get straight to </src><tgt>嫌い、</tgt>` | 788 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 516 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>要点にすぐ入ることを好む。</tgt>` | 858 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 482 |
| 20 | `<src>the devil's advocate, and they </src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src>play the devil's advocate, </src><tgt>彼らはまた、悪魔の代弁者も演じるのが好きで、</tgt>` | 716 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt><\|wait\|></tgt>` | 356 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることは決してない。</tgt>` | 404 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 313 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. </src><tgt><\|wait\|></tgt>` | 355 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt>E.T.P.は、</tgt>` | 436 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 992 |
| 2 | `<src>당무 를 거부 한 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이준석은 정부 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | 1879 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 </src><tgt><\|wait\|></tgt>` | 856 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>명분 이 후보 를 위세 삼으면서 </src><tgt>used the excuse of rejecting the government to promote his candidacy,</tgt>` | 2798 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당슬을 </src><tgt><\|wait\|></tgt>` | 1475 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위세 삼으면서 </src><tgt>and then used the candidate's party support</tgt>` | 1240 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제보 생색까지 </src><tgt><\|wait\|></tgt>` | 1313 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 이제 는 </src><tgt>to his advantage, even making a show of it. But now</tgt>` | 1709 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1945 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt>Yoon Suk- yeol</tgt>` | 2048 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1645 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 들은 해놓고 </src><tgt>removed Kim Jong- in, Lee Jun- seok</tgt>` | 1607 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 </src><tgt><\|wait\|></tgt>` | 563 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>후보 를 떨어뜨리 겠다는 </src><tgt>said he would drop Yoon Suk- yeol</tgt>` | 1676 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기를 품은 </src><tgt><\|wait\|></tgt>` | 838 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt>and was filled with malice,</tgt>` | 699 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 561 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt>ready to attack</tgt>` | 475 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt><\|wait\|></tgt>` | 369 |
| 20 | `<src><\|wait\|></src><tgt>And then there's</tgt>` | `<src>가슴 발 </src><tgt>at any moment.</tgt>` | 348 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 </src><tgt><\|wait\|></tgt>` | 359 |
| 22 | `<src><\|wait\|></src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>성상 납건. </src><tgt>Lee Jun- seok's ' chest- high- ground' case.</tgt>` | 436 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 351 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 에 얼마나 </src><tgt>How much</tgt>` | 330 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재입니까? </src><tgt><\|wait\|></tgt>` | 302 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Tolerance window size is 1.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=1)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>で、まあ</src><tgt><\|wait\|></tgt>` | 1261 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の今</src><tgt>So, after the meal,</tgt>` | 1196 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので、</src><tgt><\|wait\|></tgt>` | 1492 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>でここのね</src><tgt>I want to try making something now. So,</tgt>` | 2271 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ホルモン温泉ホテル</src><tgt><\|wait\|></tgt>` | 1524 |
| 6 | `<src>も</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>も焼魚が</src><tgt>the Horumon Onsen Hotel's grilled fish</tgt>` | 1387 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt>is a place where you can eat it.</tgt>` | 1752 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になってるので、</src><tgt><\|wait\|></tgt>` | 1976 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt>So, I'm planning to</tgt>` | 1988 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1719 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt>stay at the Goldston Hotel</tgt>` | 587 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>なっていう方はですね、</src><tgt><\|wait\|></tgt>` | 1557 |
| 14 | `<src>検討なさってみて</src><tgt>So, for anyone thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt>in the future. If you're thinking about it,</tgt>` | 1545 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見て、まあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 849 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと、はい、</src><tgt>and you think, ' Hmm, that sounds good, yes,</tgt>` | 792 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。</src><tgt><\|wait\|></tgt>` | 424 |
| 18 | `<src>のホテルからですね釜山</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>ここのホテルからですね。</src><tgt>I think so. From this hotel...</tgt>` | 555 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 379 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt>you can walk to Busan Station</tgt>` | 401 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本</src><tgt><\|wait\|></tgt>` | 293 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかるかかかんないか</src><tgt>in about a minute or so,</tgt>` | 379 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 303 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地のいいね、まあホテル</src><tgt>it's a really convenient location.</tgt>` | 390 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>になってますので、</src><tgt><\|wait\|></tgt>` | 288 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt>So if you're interested,</tgt>` | 271 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 198 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>ください。それでは</src><tgt>please give it some thought. Well then,</tgt>` | 220 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね、今回は。</src><tgt><\|wait\|></tgt>` | 191 |
