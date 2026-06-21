# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9457
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.4437
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 0.6990
  - TGT_RELEASE_TOTAL: 495
  - TGT_WAIT_ACCURACY: 0.7380
  - TGT_WAIT_TOTAL: 374
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1357.0480
  - PROCESS_TIME_MS_P50: 1295.5320
  - PROCESS_TIME_MS_P95: 2250.9140
  - PROCESS_TIME_MS_MAX: 3211.9710

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt>从一开始，</tgt>` | `<src>最初から</src><tgt>从一开始</tgt>` | 755 |
| 2 | `<src>あの特に</src><tgt>尤其是</tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 988 |
| 3 | `<src>これなんかまだ</src><tgt>这一棵</tgt>` | `<src>特に仲まだ</src><tgt><\|wait\|></tgt>` | 926 |
| 4 | `<src>一年生ですからね。</src><tgt>现在还只是一年生。</tgt>` | `<src>一年生ですからね。</src><tgt>就是因为我们是一年级，所以</tgt>` | 1754 |
| 5 | `<src>この時点で</src><tgt>在这个阶段</tgt>` | `<src>あの時点で</src><tgt>那时候</tgt>` | 1098 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう密告</src><tgt><\|wait\|></tgt>` | 1164 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 1617 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数して</src><tgt><\|wait\|></tgt>` | 1099 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>あげると</src><tgt><\|wait\|></tgt>` | 1518 |
| 10 | `<src>十年経っても</src><tgt>十年后也不会</tgt>` | `<src>10年経っても</src><tgt><\|wait\|></tgt>` | 1075 |
| 11 | `<src>大した。</src><tgt>有什么大……</tgt>` | `<src>大した</src><tgt><\|wait\|></tgt>` | 1959 |

---

### Test Example 2 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1061 |
| 2 | `<src>抛洒完以后呢，</src><tgt>放出が終わると、</tgt>` | `<src>淘沙完以后呢，</src><tgt>砂を掘り終わった後、</tgt>` | 1658 |
| 3 | `<src>内部的压力减轻，</src><tgt>内部の圧力が軽くなり、</tgt>` | `<src>内部的压力</src><tgt>内部の圧力が</tgt>` | 889 |
| 4 | `<src>能量也衰弱了，</src><tgt>エネルギーも弱まります。</tgt>` | `<src>能量也</src><tgt>エネルギーも</tgt>` | 1219 |
| 5 | `<src>然后</src><tgt>そして、</tgt>` | `<src>衰弱了，</src><tgt>弱まり、</tgt>` | 1374 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>然后就停留在</src><tgt><\|wait\|></tgt>` | 1173 |
| 7 | `<src>相对的低</src><tgt>比較的</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1489 |
| 8 | `<src>能量的运行</src><tgt>低エネルギーの</tgt>` | `<src>一个相对的低能量的</src><tgt><\|wait\|></tgt>` | 1041 |
| 9 | `<src>状态，</src><tgt>状態にとどまります。</tgt>` | `<src>运行状态。</src><tgt>相対的に低いエネルギーの稼働状態に留まります。</tgt>` | 1685 |
| 10 | `<src>这就是所谓的</src><tgt>これが、いわゆる</tgt>` | `<src>这就是</src><tgt>これが</tgt>` | 2174 |
| 11 | `<src>抑郁状态。</src><tgt>抑うつ状態です。</tgt>` | `<src>所谓的异于状态。</src><tgt>いわゆる異状態です。</tgt>` | 1562 |

---

### Test Example 3 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>为什么</src><tgt><\|wait\|></tgt>` | 1160 |
| 2 | `<src>挖一点松子儿里</src><tgt>Add some pine nuts;</tgt>` | `<src>在松子这里呢？</src><tgt>Why is it at the pine nut?</tgt>` | 1281 |
| 3 | `<src>边，这个油性也很大。</src><tgt>they're quite oily.</tgt>` | `<src>这个油量很大，</src><tgt>The oil content is very high,</tgt>` | 1666 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1389 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt>and then,</tgt>` | 968 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放点</src><tgt><\|wait\|></tgt>` | 1325 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>核桃仁，</src><tgt>I'm adding some walnuts,</tgt>` | 1686 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1636 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>感觉</src><tgt><\|wait\|></tgt>` | 679 |
| 10 | `<src>这种核桃</src><tgt>this kind of</tgt>` | `<src>这些</src><tgt><\|wait\|></tgt>` | 2291 |
| 11 | `<src>仁儿。</src><tgt>walnut kernels.</tgt>` | `<src>核桃仁。</src><tgt>and these walnuts.</tgt>` | 1761 |

---

### Test Example 4 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>要气熟是容易的，</src><tgt>呼吸を数えるのは</tgt>` | `<src>要气数是容易的，</src><tgt>気数を気にするのは簡単です。</tgt>` | 1657 |
| 3 | `<src>但是</src><tgt>簡単ですが、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 776 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有</src><tgt>でも、</tgt>` | 1333 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一个师傅指导</src><tgt>師匠が</tgt>` | 1266 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 977 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如何处于中间，</src><tgt>どういう時に</tgt>` | 1803 |
| 8 | `<src>所以</src><tgt>だからこそ、</tgt>` | `<src>所以</src><tgt>中間にいるべきか、</tgt>` | 959 |
| 9 | `<src>虚阿凡</src><tgt>シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>それを指導してくれないと、反省が必要になります。</tgt>` | 1766 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2349 |
| 11 | `<src>一个师父。</src><tgt>師匠になる必要があるのです。</tgt>` | `<src>要成为一个师傅，</src><tgt>師匠になるには、</tgt>` | 1785 |

---

### Test Example 5 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>다른 </src><tgt><\|wait\|></tgt>` | 924 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>산줄에 </src><tgt><\|wait\|></tgt>` | 1154 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>죽여달라고 해가지고 </src><tgt><\|wait\|></tgt>` | 1450 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt>came in here to do it.</tgt>` | `<src>내가 죽이기로 하도 </src><tgt><\|wait\|></tgt>` | 1822 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔치 </src><tgt><\|wait\|></tgt>` | 1003 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>메이 죽여달라고 </src><tgt><\|wait\|></tgt>` | 2037 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>해자. 내가 </src><tgt><\|wait\|></tgt>` | 1134 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 있는 </src><tgt><\|wait\|></tgt>` | 1752 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>줄은 </src><tgt><\|wait\|></tgt>` | 1602 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt>Did you think I wasn't listening? Huh?</tgt>` | `<src>야. </src><tgt><\|wait\|></tgt>` | 1622 |
| 11 | `<src>내가 가. </src><tgt>I'm going.</tgt>` | `<src>내가 </src><tgt><\|wait\|></tgt>` | 1265 |

---

### Test Example 6 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt>大致是</tgt>` | `<src>大体</src><tgt>大概</tgt>` | 1022 |
| 2 | `<src>このあたりから</src><tgt>从这一带</tgt>` | `<src>このあたりから</src><tgt>从这附近</tgt>` | 837 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始まった</src><tgt><\|wait\|></tgt>` | 1067 |
| 4 | `<src>もので、</src><tgt>开始的，</tgt>` | `<src>もので、</src><tgt>开始的，</tgt>` | 1234 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ご法</src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ごうぎゃん</src><tgt><\|wait\|></tgt>` | 1061 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1870 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザムの</src><tgt><\|wait\|></tgt>` | 1201 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1606 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の</src><tgt><\|wait\|></tgt>` | 1132 |
| 11 | `<src>は、田舎の</src><tgt>画，连乡下的</tgt>` | `<src>絵、</src><tgt><\|wait\|></tgt>` | 1917 |
| 12 | `<src>中学生でも。</src><tgt>中学生都……</tgt>` | `<src>田舎の中学生でも</src><tgt><\|wait\|></tgt>` | 1749 |

---

### Test Example 7 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>家长需要</src><tgt><\|wait\|></tgt>` | 1114 |
| 2 | `<src>家长需要做的是，</src><tgt>What parents need to do is this:</tgt>` | `<src>做的是</src><tgt>Parents need to</tgt>` | 1140 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1179 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深沉的爱交</src><tgt><\|wait\|></tgt>` | 1996 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>水，</src><tgt>use our deep love to</tgt>` | 1041 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>十分</src><tgt><\|wait\|></tgt>` | 1581 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>刻入</src><tgt><\|wait\|></tgt>` | 1342 |
| 8 | `<src>孩子心理营养，</src><tgt>give children enough psychological nourishment,</tgt>` | `<src>孩子心里，</src><tgt>imprint it in their hearts,</tgt>` | 1665 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>令人</src><tgt><\|wait\|></tgt>` | 832 |
| 10 | `<src>并耐心等待孩子</src><tgt>and wait patiently for</tgt>` | `<src>耐心等</src><tgt><\|wait\|></tgt>` | 2227 |
| 11 | `<src>慢慢长大。</src><tgt>them to grow slowly.</tgt>` | `<src>孩子慢慢长大。</src><tgt>and patiently wait for their child to grow up.</tgt>` | 1958 |

---

### Test Example 8 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt>嗯，</tgt>` | `<src>あとなんか</src><tgt>还有，</tgt>` | 1175 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>ちょっと距離が離れてくる</src><tgt><\|wait\|></tgt>` | 1254 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>感觉距离会慢慢拉开，</tgt>` | `<src>みたいな感じで</src><tgt><\|wait\|></tgt>` | 1111 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt>确实</tgt>` | `<src>大将が</src><tgt><\|wait\|></tgt>` | 1580 |
| 5 | `<src>多いですね。</src><tgt>很多人这么说。</tgt>` | `<src>こういですね</src><tgt><\|wait\|></tgt>` | 1238 |
| 6 | `<src>開業したい方って</src><tgt>想创业的人</tgt>` | `<src>会話したい方って</src><tgt><\|wait\|></tgt>` | 1063 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すぐ行き来しき다가 </src><tgt><\|wait\|></tgt>` | 1791 |
| 8 | `<src>自己意識高いし、</src><tgt>自我意识都很强，而且</tgt>` | `<src>シー</src><tgt><\|wait\|></tgt>` | 674 |
| 9 | `<src>自分で</src><tgt><\|wait\|></tgt>` | `<src>喋り始めると</src><tgt><\|wait\|></tgt>` | 1636 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と分かっていると</src><tgt><\|wait\|></tgt>` | 1982 |
| 11 | `<src>傾向が強いので、</src><tgt>倾向于自己全部投资，</tgt>` | `<src>評価が強ので</src><tgt><\|wait\|></tgt>` | 1379 |
| 12 | `<src>なので。</src><tgt>所以……</tgt>` | `<src>なので</src><tgt><\|wait\|></tgt>` | 1258 |

---

### Test Example 9 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>面对</src><tgt><\|wait\|></tgt>` | 872 |
| 2 | `<src>面对这个情况，我们就是</src><tgt>In this situation,</tgt>` | `<src>这种情况，</src><tgt>When faced with this situation,</tgt>` | 1111 |
| 3 | `<src>遇到问题</src><tgt>when we encounter a problem,</tgt>` | `<src>我们就是遇到问题</src><tgt><\|wait\|></tgt>` | 1103 |
| 4 | `<src>就赶紧的回报主管，</src><tgt>we should</tgt>` | `<src>就赶紧的</src><tgt><\|wait\|></tgt>` | 1369 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>汇报主管，或是通知对方</src><tgt><\|wait\|></tgt>` | 1223 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们笑这个状况，</src><tgt>we just quickly report it to our supervisor or let them know about the situation.</tgt>` | 2298 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1231 |
| 8 | `<src>什么都把它扛下来，</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself</tgt>` | `<src>什么都把它扛下来，</src><tgt>Don't think you have to handle everything yourself.</tgt>` | 1851 |
| 9 | `<src>独立承担。</src><tgt>or handle it alone.</tgt>` | `<src>扛得不力沉担。</src><tgt>If you can't carry it, don't take on the burden.</tgt>` | 2026 |
| 10 | `<src>整体而言，</src><tgt>Overall,</tgt>` | `<src>责任而已，</src><tgt>It's just your responsibility.</tgt>` | 1778 |
| 11 | `<src>事业运就属凶。</src><tgt>your career prospects are quite poor.</tgt>` | `<src>所以就属上。</src><tgt>So just take it.</tgt>` | 1048 |

---

### Test Example 10 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 885 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 을 켜 버리 고 </src><tgt>I'm turning on Apple</tgt>` | 1845 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1418 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 999 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>모든 것을 </src><tgt><\|wait\|></tgt>` | 1845 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>죽이 는 </src><tgt><\|wait\|></tgt>` | 1186 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1589 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>백화상과 </src><tgt><\|wait\|></tgt>` | 958 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들인 </src><tgt><\|wait\|></tgt>` | 2265 |
| 11 | `<src>같은 세대 들입니다. </src><tgt>They are the same generation as him.</tgt>` | `<src>것입니다. </src><tgt>and killing all of his own family and friends.</tgt>` | 1764 |

---

### Test Example 11 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt>I'm having</tgt>` | `<src>자 저는 </src><tgt>Well, I'm</tgt>` | 1050 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용심이 </src><tgt><\|wait\|></tgt>` | 1148 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1160 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src>칼 용심이 </src><tgt><\|wait\|></tgt>` | 1693 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>어설프 용심이 가 </src><tgt><\|wait\|></tgt>` | 1354 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1758 |
| 7 | `<src>섞여 있는 건데요. </src><tgt>it's a mix of rice noodles and ongsimi.</tgt>` | `<src>섞이 는 건데요. 야 </src><tgt>a bit of a sword spirit, a clumsy sword spirit, they get mixed up.</tgt>` | 2142 |
| 8 | `<src>야, </src><tgt>Man,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 9 | `<src>진짜 이거 </src><tgt>this is</tgt>` | `<src>진짜 이거 </src><tgt><\|wait\|></tgt>` | 2362 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt>seriously killer for a hangover,</tgt>` | `<src>행동 으로 </src><tgt><\|wait\|></tgt>` | 1271 |
| 11 | `<src>진짜. </src><tgt>for real.</tgt>` | `<src>조금 주기가 되는 </src><tgt><\|wait\|></tgt>` | 1043 |

---

### Test Example 12 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명단 에 있는 </src><tgt><\|wait\|></tgt>` | 1190 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>직성들은 </src><tgt>Those on the list</tgt>` | 1206 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1109 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1692 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt>actually weren't that intelligent,</tgt>` | 1306 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1767 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>직성들이 </src><tgt><\|wait\|></tgt>` | 1251 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>있었기 때문 입니다. </src><tgt>so they were just randomly selected.</tgt>` | 1802 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1122 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1917 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐던 교사 들은 </src><tgt>The teachers who didn't know the truth</tgt>` | 1954 |

---

### Test Example 13 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt>これはすごく</tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 960 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이걸 너무 </src><tgt><\|wait\|></tgt>` | 1094 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>低俗なことかもしれないけど、</tgt>` | `<src>지어야 를 </src><tgt><\|wait\|></tgt>` | 909 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>할 수 있지만 진짜 보살 도요 </src><tgt>これをあまり必要としないといけないけど、本当に菩薩様は</tgt>` | 2513 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt>本当の菩薩道なんだよね。いや、</tgt>` | `<src>아니 </src><tgt>違うよ。</tgt>` | 802 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>자기 의 보살 인데 꾸밀 필요 가 </src><tgt>自分の菩薩様なのに、飾る必要は</tgt>` | 2542 |
| 7 | `<src>뭐 있고 </src><tgt>ある？</tgt>` | `<src>보이 고 </src><tgt>ないし、</tgt>` | 908 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt>他人に菩薩に見せる必要なんて</tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1485 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？宇宙が</tgt>` | `<src>보살 로 보일 필요 가 </src><tgt>私だけ菩薩様に見える必要は</tgt>` | 2456 |
| 10 | `<src>지금 나한테 </src><tgt>今、私に</tgt>` | `<src>없어요 우주 가 </src><tgt>ない。宇宙が</tgt>` | 1513 |
| 11 | `<src>보살 이라는데. </src><tgt>菩薩だと言ってるんだから。</tgt>` | `<src>있다 보살 이란데. </src><tgt>菩薩様がいるんだ。</tgt>` | 1066 |

---

### Test Example 14 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Did varying </src><tgt><\|wait\|></tgt>` | 847 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>important research </src><tgt><\|wait\|></tgt>` | 1142 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1186 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. </src><tgt>非常に幸せな人々の研究を様々な角度から行いました。</tgt>` | 2415 |
| 5 | `<src>This is tip of the stem </src><tgt>これは</tgt>` | `<src>This is tip of the stem. </src><tgt>これが茎の先端です。</tgt>` | 1802 |
| 6 | `<src>research, </src><tgt>最先端の研究です。</tgt>` | `<src>Research looking at </src><tgt><\|wait\|></tgt>` | 1489 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>10% </src><tgt><\|wait\|></tgt>` | 788 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1518 |
| 9 | `<src>of the happiest people </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>最も幸せな人々の10%を</tgt>` | 2486 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. </src><tgt>調査したものです。</tgt>` | 1484 |
| 11 | `<src>people that we can learn from. </src><tgt>彼らから学べることを探っています。</tgt>` | `<src>People that we can learn from. </src><tgt>私たちが学ぶべき人たちです。</tgt>` | 1095 |

---

### Test Example 15 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1136 |
| 2 | `<src>And lastly, </src><tgt>最后，</tgt>` | `<src>And lastly, </src><tgt>最后，</tgt>` | 1151 |
| 3 | `<src>is repeat. </src><tgt>要重复。</tgt>` | `<src>is repeat. </src><tgt>重复一下。</tgt>` | 1166 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt>学会不断重复。</tgt>` | `<src>Learned that you repeat </src><tgt>你学到</tgt>` | 1725 |
| 5 | `<src>Find what you're good at </src><tgt>找到你的长处，</tgt>` | `<src>five or you're good at </src><tgt>重复五次，</tgt>` | 1424 |
| 6 | `<src>and do more of it. </src><tgt>多做那些事。</tgt>` | `<src>and do more of it </src><tgt>就</tgt>` | 1793 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and what you </src><tgt>就多做几次，</tgt>` | 1292 |
| 8 | `<src>And what you're not good at, </src><tgt>至于你的短处，</tgt>` | `<src>not good at, </src><tgt>就多做那些你不太擅长的，</tgt>` | 1884 |
| 9 | `<src>get the people around you to help you with. </src><tgt>找身边的人帮你。</tgt>` | `<src>get the people around you to help you with </src><tgt>让周围的人</tgt>` | 2388 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1792 |
| 11 | `<src>And until next time. </src><tgt>下次再见。</tgt>` | `<src>and tell next time </src><tgt>帮你，</tgt>` | 981 |

---

### Test Example 16 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt>你的身体</tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 786 |
| 2 | `<src>doing? </src><tgt>在做什么？</tgt>` | `<src>doing? </src><tgt>你的身体在做什么？</tgt>` | 1193 |
| 3 | `<src>Drop into </src><tgt>感受一下</tgt>` | `<src>Drop pin to your body. </src><tgt>把针头按到你的身体上。</tgt>` | 1946 |
| 4 | `<src>your body. </src><tgt>你的身体。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1506 |
| 5 | `<src>Where does the tension </src><tgt>紧张感从哪里</tgt>` | `<src>Where does the tension </src><tgt>紧张感</tgt>` | 1117 |
| 6 | `<src>start? What is it? </src><tgt>开始？是什么样的？</tgt>` | `<src>start? What is it? </src><tgt>从哪里开始？是什么？</tgt>` | 2423 |
| 7 | `<src>Is it a headache? </src><tgt>是头痛吗？</tgt>` | `<src>Is it a head? </src><tgt>是头吗？</tgt>` | 1373 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt>还是胸口紧绷？</tgt>` | `<src>Is it tension in your chest? </src><tgt>是胸部紧张吗？</tgt>` | 1060 |
| 9 | `<src>I ask them what </src><tgt>我问他们，</tgt>` | `<src>Or is it </src><tgt>还是</tgt>` | 2251 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>your lap, which are you </src><tgt><\|wait\|></tgt>` | 1780 |
| 11 | `<src>language are you using? </src><tgt>你在用什么语言？</tgt>` | `<src>using? </src><tgt>你的膝盖？你用的是哪个？</tgt>` | 1434 |

---

### Test Example 17 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt>이것이</tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1105 |
| 2 | `<src>です。</src><tgt>기어입니다.</tgt>` | `<src>ギアです。</src><tgt>이게 기어입니다.</tgt>` | 849 |
| 3 | `<src>ギアが</src><tgt>기어가</tgt>` | `<src>ギアが</src><tgt><\|wait\|></tgt>` | 1081 |
| 4 | `<src>緩むと芯が</src><tgt>느슨해지면 심이</tgt>` | `<src>緩むと、</src><tgt>기어가 풀리면</tgt>` | 1593 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えなくなって</src><tgt>신호가</tgt>` | 1295 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>しまうので、</src><tgt>꺼지기 때문에</tgt>` | 1297 |
| 7 | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | `<src>ギアの先に</src><tgt>기어 끝에</tgt>` | 1645 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src>逆ネジの</src><tgt><\|wait\|></tgt>` | 997 |
| 9 | `<src>ナットが</src><tgt>역나사 너트가</tgt>` | `<src>ナットが</src><tgt><\|wait\|></tgt>` | 1539 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>ついているっていうこと</src><tgt><\|wait\|></tgt>` | 1397 |
| 11 | `<src>ね。</src><tgt>달려 있는 거죠.</tgt>` | `<src>ですね。</src><tgt>역나사 너트가 붙어 있는 거죠.</tgt>` | 2223 |
| 12 | `<src>はい、</src><tgt>네,</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1127 |
| 13 | `<src>分解完了。</src><tgt>분해 완료.</tgt>` | `<src>ハイ分解完了。</src><tgt>하이 분해 완료.</tgt>` | 1898 |

---

### Test Example 18 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt>맞습니다.</tgt>` | `<src>そうです。</src><tgt>그렇습니다.</tgt>` | 897 |
| 2 | `<src>そこで</src><tgt>거기</tgt>` | `<src>そこで</src><tgt>그곳에서</tgt>` | 1102 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>think</src><tgt><\|wait\|></tgt>` | 865 |
| 4 | `<src>テキという設備寺が</src><tgt>' 테키' 라는 접미사가</tgt>` | `<src>という設定が</src><tgt>think라는 설정이</tgt>` | 1415 |
| 5 | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | `<src>ありましたね。</src><tgt>있었죠.</tgt>` | 1338 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt>그리고</tgt>` | 978 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1866 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井教授の仕組み</src><tgt>나가이 교수님의</tgt>` | 1215 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>작동 방식은</tgt>` | 1470 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>五個。</src><tgt>다섯 가지입니다.</tgt>` | 1610 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1705 |
| 12 | `<src>設備寺、五比</src><tgt>어근, 접미사, 어미로</tgt>` | `<src>設定が</src><tgt>설정은</tgt>` | 1415 |
| 13 | `<src>です。</src><tgt>이루어져 있습니다.</tgt>` | `<src>五つ。</src><tgt>다섯 가지입니다.</tgt>` | 1939 |

---

### Test Example 19 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt>好的，</tgt>` | `<src>All right. </src><tgt>好的。</tgt>` | 1123 |
| 2 | `<src>and then </src><tgt>然后</tgt>` | `<src>And then, </src><tgt>然后，</tgt>` | 807 |
| 3 | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>在这些例子之后，</tgt>` | 1159 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1356 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1423 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1233 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1725 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 996 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1587 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. </src><tgt>实际上使用这些值。</tgt>` | 1597 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1630 |
| 12 | `<src>this game dot scored array. </src><tgt>这个game.scored数组。</tgt>` | `<src>So this game.board array </src><tgt>所以这个game.board数组</tgt>` | 1668 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1828 |

---

### Test Example 20 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 837 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt>If you're a female high school student</tgt>` | 1564 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相怪的人之间</src><tgt><\|wait\|></tgt>` | 1095 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1369 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>有着某种心理，</src><tgt>have a certain psychological attraction to someone who looks strange,</tgt>` | 1475 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt><\|wait\|></tgt>` | 2026 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1034 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从天而降</src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的？</src><tgt>could it be a heavenly descent?</tgt>` | 1612 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1721 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思维</src><tgt><\|wait\|></tgt>` | 1399 |
| 12 | `<src>连篇。</src><tgt>drifted.</tgt>` | `<src>连篇。</src><tgt>Yang Zi's thoughts are continuous.</tgt>` | 2058 |

---

### Test Example 21 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなど</src><tgt><\|wait\|></tgt>` | 1125 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>があの</src><tgt><\|wait\|></tgt>` | 1137 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただくという</src><tgt><\|wait\|></tgt>` | 1136 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>ようなものも用意して</src><tgt><\|wait\|></tgt>` | 1430 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>おりますので、ぜひ</src><tgt>We have items like T- shirts available, so please</tgt>` | 1769 |
| 6 | `<src>ぜひご参加ください。</src><tgt>so please be sure to join us.</tgt>` | `<src>ご参加ください。</src><tgt>feel free to join us.</tgt>` | 1983 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1034 |
| 8 | `<src>以上になりまして、</src><tgt>That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt>That's all for the contact information.</tgt>` | 1738 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1402 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>えっと</src><tgt><\|wait\|></tgt>` | 1637 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>何種類か</src><tgt><\|wait\|></tgt>` | 1605 |
| 12 | `<src>もう少々お待ちください。</src><tgt>so please wait just a moment.</tgt>` | `<src>ありますので、少々お待ちください。</src><tgt>We have a few different types, so please wait a moment.</tgt>` | 2168 |

---

### Test Example 22 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 867 |
| 2 | `<src>映画でですね、</src><tgt>For the ' ei' (ray),</tgt>` | `<src>AAがですね</src><tgt>Um, A. A.</tgt>` | 1171 |
| 3 | `<src>いろんな場面で</src><tgt>in various situations,</tgt>` | `<src>いろんな場面で</src><tgt>In various situations,</tgt>` | 1160 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>生生刻画かどうかって</src><tgt><\|wait\|></tgt>` | 1866 |
| 5 | `<src>調べるときに、</src><tgt>when checking whether they are inhabiting an area,</tgt>` | `<src>いう時に</src><tgt>when you're thinking about whether to use live drawing,</tgt>` | 1347 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>you investigate their eggs.</tgt>` | `<src>まあAAの</src><tgt><\|wait\|></tgt>` | 1933 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ランクを調べて</src><tgt><\|wait\|></tgt>` | 1092 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>ということであの生生刻画かどうかって</src><tgt>and then checking the A. A. rank,</tgt>` | 2033 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>生生で</src><tgt><\|wait\|></tgt>` | 2362 |
| 10 | `<src>ことを保証する</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>行うこと保証するといった</src><tgt>and then guaranteeing that live drawing</tgt>` | 1881 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>わけを使うことを定められました。</src><tgt>is used.</tgt>` | 1524 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 704 |

---

### Test Example 23 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Like a stretched </src><tgt><\|wait\|></tgt>` | 889 |
| 2 | `<src>Like a stretched rubber band, </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>rubber band, </src><tgt>고무줄처럼</tgt>` | 1199 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt>화학 결합도</tgt>` | 1441 |
| 4 | `<src>also store energy, </src><tgt>화학 결합도 에너지를 저장합니다.</tgt>` | `<src>energy. </src><tgt>에너지를 저장합니다.</tgt>` | 1497 |
| 5 | `<src>and when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | `<src>And when those bonds are broken, </src><tgt>이 결합이 끊어지면</tgt>` | 1390 |
| 6 | `<src>that potential energy </src><tgt>잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>그 잠재 에너지가</tgt>` | 2272 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted </src><tgt><\|wait\|></tgt>` | 855 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>to other types of energy, </src><tgt>다른 종류의 에너지로</tgt>` | 1750 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>like heat or light. </src><tgt>변환됩니다. 예를 들어 열이나 빛 같은 것들이죠.</tgt>` | 2880 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets used </src><tgt>또는</tgt>` | 1504 |
| 11 | `<src>or gets used to make </src><tgt>또는</tgt>` | `<src>to make </src><tgt><\|wait\|></tgt>` | 1393 |
| 12 | `<src>different bonds. </src><tgt>새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>다른 결합을 만드는 데 사용됩니다.</tgt>` | 925 |

---

### Test Example 24 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 745 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1145 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活的一个轨道，</src><tgt>제 삶의 궤도로 돌아가게 해 주세요.</tgt>` | 2079 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>好，</src><tgt>좋아요,</tgt>` | 1283 |
| 5 | `<src>让我能够哈，</src><tgt>돌아가고 싶어요.</tgt>` | `<src>让我能够好自在</src><tgt><\|wait\|></tgt>` | 962 |
| 6 | `<src>在他下班的时候，</src><tgt>그 사람이 퇴근했을 때</tgt>` | `<src>的那一发生的时候，</src><tgt>편안하게 지낼 수 있는 그 순간을</tgt>` | 2770 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做日航</src><tgt><\|wait\|></tgt>` | 1262 |
| 8 | `<src>热饭给他吃。真的，</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>日航的</src><tgt><\|wait\|></tgt>` | 951 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>时候，</src><tgt>다이칸야마를</tgt>` | 2482 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时被他做制服</src><tgt>입고</tgt>` | 1870 |
| 11 | `<src>小小的愿望</src><tgt>그 작은 소망 하나뿐이었어요.</tgt>` | `<src>一个小小的小小的一段往好，</src><tgt>그때 그 옷을 입고</tgt>` | 2033 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 603 |

---

### Test Example 25 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 953 |
| 2 | `<src>一切正常，</src><tgt>I was perfectly fine at the time,</tgt>` | `<src>一切正常，</src><tgt>Everything was normal back then.</tgt>` | 1157 |
| 3 | `<src>活蹦乱跳，</src><tgt>jumping around,</tgt>` | `<src>胡波乱跳，</src><tgt>I was just jumping around,</tgt>` | 1441 |
| 4 | `<src>所以</src><tgt>so I</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1461 |
| 5 | `<src>坚持不开刀。</src><tgt>insisted on not having surgery.</tgt>` | `<src>所以坚持不开刀，</src><tgt>so I insisted on not cutting in.</tgt>` | 1433 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>切肩大概</src><tgt><\|wait\|></tgt>` | 1870 |
| 7 | `<src>大概有十位医生</src><tgt>About ten doctors</tgt>` | `<src>有十二生</src><tgt><\|wait\|></tgt>` | 1138 |
| 8 | `<src>来诊断，</src><tgt>came to examine me during that period.</tgt>` | `<src>来剪断，</src><tgt>I had about twelve cuts to make to my shoulders,</tgt>` | 1968 |
| 9 | `<src>一下敲腿，</src><tgt><\|wait\|></tgt>` | `<src>以下敲腿</src><tgt><\|wait\|></tgt>` | 2118 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一打提腿，</src><tgt>and I had to kick and lift my legs</tgt>` | 2033 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt>without any problems.</tgt>` | 783 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 1554 |
| 13 | `<src>都很疑惑的离开。</src><tgt>They all left feeling very puzzled.</tgt>` | `<src>疑惑的离开。</src><tgt>They all left looking confused.</tgt>` | 1383 |

---

### Test Example 26 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt>제 이름은</tgt>` | `<src>My name is </src><tgt>제 이름은</tgt>` | 971 |
| 2 | `<src>Kerenath Dettig. </src><tgt>케레나스 데티그입니다.</tgt>` | `<src>Chunhatteru. </src><tgt>춘하테루입니다.</tgt>` | 1312 |
| 3 | `<src>I am currently </src><tgt>저는 현재</tgt>` | `<src>I am currently studying </src><tgt><\|wait\|></tgt>` | 1129 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a B.A. in </src><tgt><\|wait\|></tgt>` | 1944 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Business Finance </src><tgt><\|wait\|></tgt>` | 935 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a B.S. in </src><tgt><\|wait\|></tgt>` | 1999 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Psychology. </src><tgt>현재 경영학 학사 학위와 심리학 학사 학위를</tgt>` | 1588 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>Yeah, here at Yale. </src><tgt>Yale에서 공부하고 있어요.</tgt>` | 1627 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2377 |
| 10 | `<src>and in the future, I want to go into </src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src>And in the future, I want to go into </src><tgt>그리고 앞으로는</tgt>` | 2016 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1960 |
| 12 | `<src>corporate consultancy. </src><tgt>기업 컨설팅 쪽으로 가고 싶습니다.</tgt>` | `<src>corporate consultancy. </src><tgt>기업 컨설팅 분야로 가고 싶어요.</tgt>` | 1485 |

---

### Test Example 27 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>바나듐 이라는 </src><tgt><\|wait\|></tgt>` | 926 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt>Things like vanadium</tgt>` | `<src>이런 것들은 </src><tgt>These things, like vanadium,</tgt>` | 1256 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>거진 유실 이 일어날 수가 </src><tgt>can be lost</tgt>` | 1691 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 경우 인 경우 를 </src><tgt><\|wait\|></tgt>` | 1104 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>굉장히 </src><tgt><\|wait\|></tgt>` | 1843 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>아주 </src><tgt><\|wait\|></tgt>` | 1090 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당연히 미네랄 이다 </src><tgt><\|wait\|></tgt>` | 1763 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이기 때문 에 </src><tgt><\|wait\|></tgt>` | 1187 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1794 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>그런 거죠. 이제 </src><tgt>because they are minerals, they can be lost. So, that's what it is. Now,</tgt>` | 2407 |
| 12 | `<src>그거 에다가 </src><tgt>And on top of that,</tgt>` | `<src>그거 에다가 </src><tgt>add that to</tgt>` | 1409 |
| 13 | `<src>아연. </src><tgt>there's zinc.</tgt>` | `<src>아견. </src><tgt>the ' ah '.</tgt>` | 1409 |

---

### Test Example 28 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt>2つ目は、</tgt>` | `<src>第二个</src><tgt>2つ目は</tgt>` | 906 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>就是进入</src><tgt><\|wait\|></tgt>` | 1156 |
| 3 | `<src>选择二级市场，哎，</src><tgt>二次市場を選ぶことです。つまり、</tgt>` | `<src>二极相，</src><tgt>二極相に入ることです。</tgt>` | 1545 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1369 |
| 5 | `<src>在一级一线</src><tgt>最前線で</tgt>` | `<src>复在一级一线</src><tgt>1つ目の線と</tgt>` | 1296 |
| 6 | `<src>拼杀的大牛们，</src><tgt>戦っている大物たちをサポートするのです。</tgt>` | `<src>拼上的大牛们。</src><tgt>2つ目の線で構成された大きな牛たちです。</tgt>` | 2354 |
| 7 | `<src>比如说，呃，</src><tgt>例えば、</tgt>` | `<src>比如说，</src><tgt>例えば、</tgt>` | 935 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1577 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>在做微信号重仓好事</src><tgt>微信号の</tgt>` | 1544 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>几年你会发现，</src><tgt>重倉の好い時期に</tgt>` | 2204 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信号平分的</src><tgt>微信号を</tgt>` | 1052 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1878 |
| 13 | `<src>火了。</src><tgt>人気を集めていることに気づきます。</tgt>` | `<src>新棒反而活了。</src><tgt>均等に分配すると、むしろ活力が湧いてくることがあります。</tgt>` | 1604 |

---

### Test Example 29 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt>それか、</tgt>` | `<src>Well, </src><tgt>ええと、</tgt>` | 976 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>if you have to produce </src><tgt>もし</tgt>` | 1173 |
| 3 | `<src>something written, </src><tgt>何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>何か書く必要があるなら、</tgt>` | 1397 |
| 4 | `<src>write a text, </src><tgt>テキストを作るときに、</tgt>` | `<src>write a text, </src><tgt>テキストを書く、</tgt>` | 1703 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize </src><tgt>その時に</tgt>` | 927 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>that you don't even know </src><tgt>そもそも</tgt>` | 1371 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1655 |
| 8 | `<src>the words. Like, oh, </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、</tgt>` | `<src>the words. </src><tgt>スペルがわからないことに気づくかもしれません。</tgt>` | 1677 |
| 9 | `<src>is this word </src><tgt>この単語って、</tgt>` | `<src>Like, oh, is this word </src><tgt>「あ、この単語は</tgt>` | 1107 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>started with </src><tgt><\|wait\|></tgt>` | 2137 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a double p, </src><tgt>「ダブルPで始まるの？」</tgt>` | 1809 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double l. I don't know </src><tgt>「ダブルL。わからない」</tgt>` | 2078 |
| 13 | `<src>know. </src><tgt>分かんないんですよね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1489 |

---

### Test Example 30 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>扎了一个</src><tgt><\|wait\|></tgt>` | 786 |
| 2 | `<src>达到了一个甜头，那</src><tgt>うまくいったなと</tgt>` | `<src>腱头，</src><tgt>腱を一本刺して、</tgt>` | 1287 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>那如果你</src><tgt>その後に</tgt>` | 1010 |
| 4 | `<src>达到了甜头之后，</src><tgt>思ったらね。その時は</tgt>` | `<src>达到了腱头之后，</src><tgt>腱を刺した後に</tgt>` | 1999 |
| 5 | `<src>请你务必就要</src><tgt>必ず利益を</tgt>` | `<src>请务必</src><tgt>必ず</tgt>` | 902 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>坐腰先</src><tgt>腰を</tgt>` | 1023 |
| 7 | `<src>先守住，</src><tgt>確保してください。</tgt>` | `<src>守住，</src><tgt>守って、</tgt>` | 1468 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，</src><tgt>「あ、</tgt>` | 1165 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那我</src><tgt>作業しなきゃ」なんて</tgt>` | 1571 |
| 10 | `<src>继续操作下去哦。</src><tgt>「もっといけるはずだ」なんて思わないで。</tgt>` | `<src>再去操作下去了。</src><tgt>なんて考えないでください。</tgt>` | 2559 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1808 |
| 12 | `<src>为什么会这么讲？</src><tgt>なぜそう言うかというと、</tgt>` | `<src>为什么</src><tgt>なぜなら、</tgt>` | 1148 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>我们这么讲？因为呢，</src><tgt>私たちはこう言うんです。なぜなら、</tgt>` | 1232 |
| 14 | `<src>因为呢。</src><tgt>それはですね。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1456 |

---

### Test Example 31 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1149 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1148 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment </src><tgt>19차 수정헌법의</tgt>` | 1658 |
| 4 | `<src>and to explore its </src><tgt>살펴보고,</tgt>` | `<src>and to explore its </src><tgt>의 의미와</tgt>` | 1502 |
| 5 | `<src>history as a guide </src><tgt>그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>history as a guide </src><tgt>역사를 살펴보겠습니다.</tgt>` | 1099 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1750 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to how political change </src><tgt>정치적 변화가</tgt>` | 1387 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>can happen </src><tgt>어떻게 일어날 수 있는지</tgt>` | 1755 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>미국에서 어떻게 일어날 수 있는지에 대한 지침서입니다.</tgt>` | 2641 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1731 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings of </src><tgt><\|wait\|></tgt>` | 1060 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>이 수정헌법의 의미는 물론</tgt>` | 1419 |
| 13 | `<src>myriad. </src><tgt>무수히 많습니다.</tgt>` | `<src>I'm Mary. </src><tgt>마리입니다.</tgt>` | 1529 |

---

### Test Example 32 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt>そのうち</tgt>` | `<src>그중 에서 </src><tgt>その中で</tgt>` | 791 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt>150万社が、従業員数</tgt>` | `<src>150개가 </src><tgt>150個が</tgt>` | 1233 |
| 3 | `<src>10명 미만 으로 </src><tgt>10人未満の</tgt>` | `<src>증오 못해서 위험 이만으로 </src><tgt>憎悪で</tgt>` | 1571 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt>非常に小さな</tgt>` | `<src>아주 작은 기업 들만 </src><tgt>危険で、とても小さな企業だけが</tgt>` | 1928 |
| 5 | `<src>많았습니다. </src><tgt>企業でした。</tgt>` | `<src>남았습니다. </src><tgt>残りました。</tgt>` | 1086 |
| 6 | `<src>일반 적으로는 </src><tgt>一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>一般的には</tgt>` | 1874 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt>小規模な企業は成長するか</tgt>` | `<src>작은 업체 들은 </src><tgt>小さな企業は</tgt>` | 1122 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt>廃業するかの道を</tgt>` | `<src>성장 하거나 혹은 </src><tgt>成長するか、あるいは</tgt>` | 1622 |
| 9 | `<src>걷게 되는데 </src><tgt>歩むものですが、</tgt>` | `<src>해화법에 그껴도 되는데 </src><tgt>解体法に縛られてもいいのですが、</tgt>` | 2670 |
| 10 | `<src>일본 의 소기업들은 </src><tgt>日本の小企業は</tgt>` | `<src>이거 는 </src><tgt>これは</tgt>` | 1610 |
| 11 | `<src>성장 도 폐업 도 </src><tgt>成長も廃業も</tgt>` | `<src>소기업 들은 </src><tgt>中小企業は</tgt>` | 1225 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>しないという現象を</tgt>` | `<src>성장 도 폐업 도 하지 않는 </src><tgt>成長も廃業もしない</tgt>` | 1222 |
| 13 | `<src>보이 게 된 거죠. </src><tgt>見せるようになったのです。</tgt>` | `<src>현상 들로 보이 게 된 거죠. </src><tgt>現象になっているんです。</tgt>` | 1764 |

---

### Test Example 33 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt>没什么新鲜的。</tgt>` | `<src>Nothing new, </src><tgt>没什么新鲜事，</tgt>` | 997 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1146 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>there's </src><tgt><\|wait\|></tgt>` | 1159 |
| 4 | `<src>such interfaces before, </src><tgt>以前就有过这样的接口，</tgt>` | `<src>such instances </src><tgt><\|wait\|></tgt>` | 1457 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>before. </src><tgt>以前发生过很多类似的情况。</tgt>` | 1409 |
| 6 | `<src>netfilter, TC. </src><tgt>比如netfilter和 TC。</tgt>` | `<src>Next filter, </src><tgt>下一个过滤器，</tgt>` | 1222 |
| 7 | `<src>Yeah, so </src><tgt>所以</tgt>` | `<src>TC. </src><tgt>TC。</tgt>` | 1212 |
| 8 | `<src>this is just </src><tgt>这只是</tgt>` | `<src>That's just </src><tgt>这只是</tgt>` | 1017 |
| 9 | `<src>one another place </src><tgt>另一个</tgt>` | `<src>one another </src><tgt><\|wait\|></tgt>` | 1547 |
| 10 | `<src>to look at. </src><tgt>需要关注的地方。</tgt>` | `<src>place to look at. </src><tgt>另一个地方看。</tgt>` | 1638 |
| 11 | `<src>But </src><tgt>但</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1706 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1256 |
| 13 | `<src>developers or engineers </src><tgt>开发人员或</tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1636 |
| 14 | `<src>working on BugRepo </src><tgt>在BugRepo工作的工程师</tgt>` | `<src>working on Bug Repos </src><tgt><\|wait\|></tgt>` | 651 |
| 15 | `<src>should be aware of that. </src><tgt>应该意识到这一点。</tgt>` | `<src>should be aware of that. </src><tgt>但开发或工程师在BugRepos上工作的人应该知道这一点。</tgt>` | 1931 |

---

### Test Example 34 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt>皆さん、</tgt>` | 1053 |
| 2 | `<src>要提醒大家，</src><tgt>皆さんに言っておきたいんですが、</tgt>` | `<src>在这</src><tgt><\|wait\|></tgt>` | 1119 |
| 3 | `<src>在这个罗马呢</src><tgt>ローマは</tgt>` | `<src>个罗马呢，</src><tgt>このローマでは、</tgt>` | 1218 |
| 4 | `<src>不是一天造成的，</src><tgt>一日にして成らずと言いますよね。</tgt>` | `<src>不是意味着</src><tgt><\|wait\|></tgt>` | 1454 |
| 5 | `<src>所以呢，</src><tgt>だから、</tgt>` | `<src>造成了，所以呢，</src><tgt>そうなるわけではありません。ですから、</tgt>` | 1650 |
| 6 | `<src>你现在</src><tgt>今皆さんが</tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1702 |
| 7 | `<src>所面临的一些</src><tgt>直面している</tgt>` | `<src>有什么</src><tgt><\|wait\|></tgt>` | 1156 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>你的一些</src><tgt><\|wait\|></tgt>` | 1617 |
| 9 | `<src>也不可能是</src><tgt>危機やリスクも、</tgt>` | `<src>业力跟风性</src><tgt><\|wait\|></tgt>` | 965 |
| 10 | `<src>一夕之间就</src><tgt>一朝一夕で</tgt>` | `<src>也不可能是</src><tgt><\|wait\|></tgt>` | 2199 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>一夜之间就</src><tgt><\|wait\|></tgt>` | 1702 |
| 12 | `<src>演变出来的，</src><tgt>生まれたわけじゃありません。</tgt>` | `<src>演变出来的。</src><tgt>今、皆さんが持っている業力や風性も、一夜にして変化するものではありません。</tgt>` | 2130 |
| 13 | `<src>因此会建议</src><tgt>そこで、</tgt>` | `<src>因此，</src><tgt>ですから、</tgt>` | 1390 |
| 14 | `<src>属鸡的朋友呢。</src><tgt>酉年生まれの皆さんには…</tgt>` | `<src>会建议属鸡的朋友呢，</src><tgt>鶏年生まれの皆さんは、</tgt>` | 1282 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt>이 부분에서는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 840 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分，</src><tgt>이 부분은</tgt>` | 1228 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是一个</src><tgt><\|wait\|></tgt>` | 1226 |
| 4 | `<src>的人，但是</src><tgt>낚시하는 사람을 볼 수 있는데요,</tgt>` | `<src>戴雪的人，但是</src><tgt>눈을 덮은 사람을 보고 있습니다.</tgt>` | 2235 |
| 5 | `<src>它是属于逆向的，</src><tgt>이게 역방향이에요.</tgt>` | `<src>他是属于</src><tgt><\|wait\|></tgt>` | 1080 |
| 6 | `<src>所以</src><tgt>그래서</tgt>` | `<src>逆向的，</src><tgt>하지만 역방향입니다.</tgt>` | 2065 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt>보통 이런 상황을</tgt>` | `<src>这通场吗这样的一个状况</src><tgt><\|wait\|></tgt>` | 1049 |
| 8 | `<src>时候，就要去</src><tgt>만나게 되면,</tgt>` | `<src>需要去</src><tgt><\|wait\|></tgt>` | 1446 |
| 9 | `<src>特别注意，</src><tgt><\|wait\|></tgt>` | `<src>特别的注意是</src><tgt>이런 상황은 특별히 주의해야 합니다.</tgt>` | 2473 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1799 |
| 11 | `<src>钓到鱼，</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요.</tgt>` | `<src>得到</src><tgt><\|wait\|></tgt>` | 894 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡지 못한다는</tgt>` | `<src>与他跳不到</src><tgt><\|wait\|></tgt>` | 1498 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>与你的意识</src><tgt><\|wait\|></tgt>` | 1398 |
| 14 | `<src>的意思哦。</src><tgt>뜻이거든요.</tgt>` | `<src>了。</src><tgt>그가 당신의 의식에 닿지 못할 수도 있습니다.</tgt>` | 1239 |

---

### Test Example 36 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt>目を閉じて。</tgt>` | `<src>눈 감고 </src><tgt>目を閉じて</tgt>` | 1173 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>새로 </src><tgt><\|wait\|></tgt>` | 911 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>私が祈るから。</tgt>` | `<src>밝을 거야. </src><tgt>新しい光が差し込むんだ。</tgt>` | 1202 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 </src><tgt><\|wait\|></tgt>` | 1174 |
| 5 | `<src>닭살이 돋든 </src><tgt>鳥肌が立ったり</tgt>` | `<src>서름이 </src><tgt><\|wait\|></tgt>` | 1436 |
| 6 | `<src>느낌 이 오면 </src><tgt>何かを感じたりしたら、</tgt>` | `<src>돋은 자태 로 </src><tgt>今、</tgt>` | 1118 |
| 7 | `<src>이걸 흔들 어서 </src><tgt>これを振って。</tgt>` | `<src>네 길을 </src><tgt>その光に照らされて、</tgt>` | 2202 |
| 8 | `<src>같이 놀자는 거야. </src><tgt>一緒に遊ぼうって合図だから。</tgt>` | `<src>흔들 어서 같이 놀자는 거야. </src><tgt>一緒に遊ぼうよ。</tgt>` | 1284 |
| 9 | `<src>귀신 이 오면 </src><tgt>霊が来たら</tgt>` | `<src>귀신 이 </src><tgt><\|wait\|></tgt>` | 1142 |
| 10 | `<src>물릴 거고 </src><tgt>噛みつかれるし、</tgt>` | `<src>너무 많이 </src><tgt><\|wait\|></tgt>` | 1952 |
| 11 | `<src>신이 오면 </src><tgt>神様が来たら</tgt>` | `<src>불릴 거고, 네 눈이 </src><tgt>お化けがすごくたくさん出てきて、</tgt>` | 2223 |
| 12 | `<src>너 지켜 주라고 </src><tgt>守ってくれるように</tgt>` | `<src>더 치켜 올라가 고 </src><tgt>君の目がもっと</tgt>` | 1222 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt>突いてくれるから、</tgt>` | `<src>찔러 주다 보니까 </src><tgt>見つめられて、</tgt>` | 1267 |
| 14 | `<src>편안 한 마음 에 </src><tgt>安心して</tgt>` | `<src>편안 한 마음 에 </src><tgt>気持ちが</tgt>` | 1504 |
| 15 | `<src>눈 감아. </src><tgt>目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>楽になるように目を閉じて。</tgt>` | 1118 |

---

### Test Example 37 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>実は</src><tgt>其实</tgt>` | 961 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一二手とか</src><tgt><\|wait\|></tgt>` | 807 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですかね</src><tgt>一二手之类的</tgt>` | 1106 |
| 4 | `<src>十秒で。</src><tgt>差不多十秒。</tgt>` | `<src>と恐らく十秒で</src><tgt>大概十秒</tgt>` | 1506 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1349 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>まあ一秒に</src><tgt><\|wait\|></tgt>` | 1209 |
| 7 | `<src>一定強ぐらいの</src><tgt>一秒一手多一点</tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 1772 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>せつなんですかね</src><tgt><\|wait\|></tgt>` | 1113 |
| 9 | `<src>ね。</src><tgt>这样算。</tgt>` | `<src>ね。</src><tgt>一秒左右，</tgt>` | 1521 |
| 10 | `<src>でなんか</src><tgt>然后</tgt>` | `<src>でなんか</src><tgt>大概一秒</tgt>` | 1857 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>恐らく</src><tgt><\|wait\|></tgt>` | 1361 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一</src><tgt><\|wait\|></tgt>` | 1399 |
| 13 | `<src>十一二手で</src><tgt>十一二手的时候，</tgt>` | `<src>二で</src><tgt><\|wait\|></tgt>` | 1890 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 603 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>見合うまとかが</src><tgt><\|wait\|></tgt>` | 1478 |
| 16 | `<src>あるから。</src><tgt>会有宫马什么的。</tgt>` | `<src>だから。</src><tgt>大概十一二，所以……</tgt>` | 891 |

---

### Test Example 38 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt>あなたがたも</tgt>` | `<src>너희 도 </src><tgt>あなたたちも</tgt>` | 862 |
| 2 | `<src>알거니와 너희 가 </src><tgt>知っているとおり、あなたがたが</tgt>` | `<src>알거니와 </src><tgt>知っているでしょう。</tgt>` | 1208 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>여기 가 </src><tgt>ここが</tgt>` | 1066 |
| 4 | `<src>있을 때에 </src><tgt>異邦人だった時、</tgt>` | `<src>이방인 으로 있을 때에 </src><tgt>異邦人として</tgt>` | 1880 |
| 5 | `<src>말 못하 는 </src><tgt>ものを言わない</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1080 |
| 6 | `<src>우상에게로 </src><tgt>偶像に</tgt>` | `<src>말 못하는 우상 에게로 </src><tgt>言葉を</tgt>` | 1434 |
| 7 | `<src>끄는 그대로 </src><tgt>引かれるままに</tgt>` | `<src>그는 그대로 </src><tgt>捧げている</tgt>` | 1560 |
| 8 | `<src>끌려 갔느니라. </src><tgt>連れて行かれました。</tgt>` | `<src>끌려 갔느니라. </src><tgt>その偶像にそのまま連れて行かれるのです。</tgt>` | 1786 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 10 | `<src>그러므로 내가 </src><tgt>ですから、</tgt>` | `<src>그러므로 </src><tgt>ですから、</tgt>` | 2091 |
| 11 | `<src>너희 에게 </src><tgt>あなたがたに</tgt>` | `<src>내가 너희에게 </src><tgt>私があなたたちに</tgt>` | 1704 |
| 12 | `<src>알리 노니 </src><tgt>教えます。</tgt>` | `<src>알리 노니 </src><tgt>知らせるのです。</tgt>` | 1981 |
| 13 | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | `<src>하나님 의 영으로 </src><tgt>神の霊によって</tgt>` | 965 |
| 14 | `<src>말하는 자는. </src><tgt>語る者は、</tgt>` | `<src>말하는 자는 </src><tgt>語る者は</tgt>` | 1121 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 876 |

---

### Test Example 39 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt>金運ですが、</tgt>` | `<src>在财运方面，</src><tgt>財運についてですが、</tgt>` | 1031 |
| 2 | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | `<src>这个月财运可以说是</src><tgt>今月は</tgt>` | 1225 |
| 3 | `<src>很不错的，但是</src><tgt>かなり良いです。ただ、</tgt>` | `<src>还不错的，但是</src><tgt>かなり良いですよ。ただ、</tgt>` | 1480 |
| 4 | `<src>比较偏向正财的部分，</src><tgt>どちらかというと本業の収入、</tgt>` | `<src>比较占正财的部分</src><tgt>正財の</tgt>` | 1609 |
| 5 | `<src>也就是</src><tgt>つまり</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 945 |
| 6 | `<src>在事业方面的</src><tgt>仕事の</tgt>` | `<src>一直是在事业方面的</src><tgt>部分が、</tgt>` | 1793 |
| 7 | `<src>业绩成长所带来的红利</src><tgt>業績成長による</tgt>` | `<src>业绩增长所带来的</src><tgt>仕事の業績向上による</tgt>` | 1425 |
| 8 | `<src>与收入的</src><tgt>ボーナスや昇給の運気が</tgt>` | `<src>流动收入的</src><tgt>収入の</tgt>` | 1529 |
| 9 | `<src>提升。如果是在</src><tgt>強めです。</tgt>` | `<src>提升。如果</src><tgt>増加です。もし</tgt>` | 1060 |
| 10 | `<src>投资理财方面呢，</src><tgt>投資や資産運用についても、</tgt>` | `<src>在投资理财方面，</src><tgt>投資や資産運用に関しては、</tgt>` | 2528 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt>今月は</tgt>` | 1262 |
| 12 | `<src>也是不错，只是</src><tgt>悪くはないんですが、</tgt>` | `<src>也是不错，只是</src><tgt>悪くないですが、</tgt>` | 1994 |
| 13 | `<src>相对正财来说就</src><tgt>本業の収入に比べると</tgt>` | `<src>相对正财来说，</src><tgt>正財に比べると</tgt>` | 1450 |
| 14 | `<src>稍微弱了那么一点。</src><tgt>少し弱めですね。</tgt>` | `<src>就稍微弱了</src><tgt>少し弱いです。</tgt>` | 1068 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>那么一点。</src><tgt>少しだけですね。</tgt>` | 387 |

---

### Test Example 40 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt>それは</tgt>` | `<src>That someone who </src><tgt>それは、</tgt>` | 1089 |
| 2 | `<src>just getting going </src><tgt>始めたばかりの人が</tgt>` | `<src>is just getting going </src><tgt>ただ</tgt>` | 1131 |
| 3 | `<src>needs to get, </src><tgt>手に入れるべき</tgt>` | `<src>needs to get </src><tgt>始める必要がある人</tgt>` | 1181 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1495 |
| 5 | `<src>and I have ten of them </src><tgt>もので、</tgt>` | `<src>and I have ten of them </src><tgt>と、その人が10人いると、</tgt>` | 1723 |
| 6 | `<src>that I think are </src><tgt>私にとって</tgt>` | `<src>that you're </src><tgt><\|wait\|></tgt>` | 2123 |
| 7 | `<src>really important. </src><tgt>本当に重要だと思うのが10個あります。</tgt>` | `<src>really important. </src><tgt>本当に重要だということですね。</tgt>` | 1107 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1536 |
| 9 | `<src>I'm going to go into. </src><tgt>それについてお話ししていきます。</tgt>` | `<src>I'm going to go and do </src><tgt>では、</tgt>` | 1897 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>I have about </src><tgt><\|wait\|></tgt>` | 1453 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>one minute videos </src><tgt>1分程度の動画を</tgt>` | 1366 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>about this video. </src><tgt>作ります。</tgt>` | 1928 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The coverage </src><tgt><\|wait\|></tgt>` | 1328 |
| 14 | `<src>that cover each one </src><tgt>それぞれを</tgt>` | `<src>each one </src><tgt>各動画で</tgt>` | 934 |
| 15 | `<src>in a little more detail, but. </src><tgt>もう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>in a little more detail, </src><tgt>少し詳しく</tgt>` | 711 |

---

### Test Example 41 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 827 |
| 2 | `<src>HTML이라고 </src><tgt>HTML</tgt>` | `<src>呃，</src><tgt>呃，</tgt>` | 1116 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Hterm이라고 하는 </src><tgt><\|wait\|></tgt>` | 1213 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>컴피터도 </src><tgt><\|wait\|></tgt>` | 1700 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt>Hterm这个计算机</tgt>` | 1306 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>사람 도 </src><tgt>也能理解，</tgt>` | 1627 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1333 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>컴퓨터 어 </src><tgt><\|wait\|></tgt>` | 1626 |
| 9 | `<src>문법 에 </src><tgt><\|wait\|></tgt>` | `<src>언어 의 문법 을 </src><tgt><\|wait\|></tgt>` | 902 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>알게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 2349 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 1681 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt><\|wait\|></tgt>` | 1944 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt>编写代码</tgt>` | `<src>그것 들을 </src><tgt><\|wait\|></tgt>` | 510 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1590 |
| 15 | `<src>필요 합니다. </src><tgt>就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要理解计算机语言的语法，然后编写程序来编写这些东西。</tgt>` | 1122 |

---

### Test Example 42 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>어떻게 보면 </src><tgt>怎么说呢，</tgt>` | `<src>어치 보면 </src><tgt>你看，</tgt>` | 932 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1102 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1373 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1373 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 같은 </src><tgt><\|wait\|></tgt>` | 1399 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>동생 이잖아. </src><tgt>他就是和你一起经历20岁的人，也是家人一样，</tgt>` | 2229 |
| 8 | `<src>그러니까 </src><tgt>所以</tgt>` | `<src>그러니까 </src><tgt>所以</tgt>` | 1549 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 746 |
| 10 | `<src>책임감 보다는 </src><tgt>比起责任感，</tgt>` | `<src>재생 한 거라는 </src><tgt><\|wait\|></tgt>` | 2346 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1702 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 1129 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1182 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 1471 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내놓고 </src><tgt><\|wait\|></tgt>` | 972 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>생각 했습니다. </src><tgt>我当时觉得，因为他也是我们一起经历20岁的人，所以他自己应该会多想一些。</tgt>` | 1004 |

---

### Test Example 43 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt>一进去就会</tgt>` | `<src>들어감에 </src><tgt><\|wait\|></tgt>` | 1163 |
| 2 | `<src>엄청 헤맵니다. </src><tgt>晕头转向。</tgt>` | `<src>엄청 해매 입니다. </src><tgt>进入的时候非常困惑。</tgt>` | 1314 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | 1109 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>하고 </src><tgt><\|wait\|></tgt>` | 1363 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 걸어 다니 고 </src><tgt><\|wait\|></tgt>` | 1434 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그러면 </src><tgt>开车、走路，</tgt>` | 1133 |
| 7 | `<src>강북 을 가면 </src><tgt>去江北</tgt>` | `<src>뭐 강북 으로 </src><tgt><\|wait\|></tgt>` | 1569 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt>就不用说了，去外国</tgt>` | `<src>가면 말을 할 것도 </src><tgt><\|wait\|></tgt>` | 959 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>왜구 에게 나가 는 것도 </src><tgt><\|wait\|></tgt>` | 1589 |
| 10 | `<src>또 장렬이에요. </src><tgt>就更惨了。</tgt>` | `<src>장려 리요. </src><tgt>去江南区的话，去外围也算是鼓励。</tgt>` | 2596 |
| 11 | `<src>좀 창피 하네요. </src><tgt>真有点丢人。</tgt>` | `<src>좀 치안 이 </src><tgt><\|wait\|></tgt>` | 1732 |
| 12 | `<src>대신 에 </src><tgt>不过，</tgt>` | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | 1220 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 열심히 </src><tgt><\|wait\|></tgt>` | 1026 |
| 14 | `<src>열심히 물어봐요. </src><tgt>我会努力去问路。</tgt>` | `<src>모여 봐요. </src><tgt>比起治安，不如大家努力聚在一起。</tgt>` | 1731 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>这一点倒是做得还行。</tgt>` | `<src>그거 는 된 것 같아요. </src><tgt>我觉得这样应该没问题。</tgt>` | 1032 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 788 |

---

### Test Example 44 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt>그렇다면</tgt>` | 1092 |
| 2 | `<src>もう眠らせてやれ。</src><tgt>그럼 이제 잠들게 해줘.</tgt>` | `<src>もう蒸らせてやれ。</src><tgt>그냥 쪄버려.</tgt>` | 1319 |
| 3 | `<src>俺は</src><tgt>난</tgt>` | `<src>俺は</src><tgt><\|wait\|></tgt>` | 1057 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1577 |
| 5 | `<src>今奇跡を見てる。</src><tgt>지금 기적을 보고 있어.</tgt>` | `<src>火勢を見ている。</src><tgt>나는 불길을 보고 있어.</tgt>` | 1422 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1758 |
| 7 | `<src>もう限界なんか</src><tgt>이미</tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1255 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 1608 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈火勢気勢。</src><tgt>이 불길은 이미 한계를 넘어선 불길이야.</tgt>` | 1391 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1890 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1556 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt><\|wait\|></tgt>` | 1856 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やっている。</src><tgt>오랫동안 불을 지펴왔어.</tgt>` | 500 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなに</src><tgt>나는 이렇게</tgt>` | 1608 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt>이렇게 대단한 해적선은</tgt>` | `<src>すごい海賊線を</src><tgt><\|wait\|></tgt>` | 949 |
| 16 | `<src>見たことがない。</src><tgt>처음 봤다.</tgt>` | `<src>見たことがない。</src><tgt>대단한 해적선을 본 적이 없어.</tgt>` | 953 |

---

### Test Example 45 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1088 |
| 2 | `<src>Educational attainment. </src><tgt>교육 수준.</tgt>` | `<src>Educational attainment. </src><tgt>학력 수준.</tgt>` | 1163 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1226 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1515 |
| 5 | `<src>actually go in your education? Did you </src><tgt>실제로 어디까지 교육을 받으셨나요?</tgt>` | `<src>in your education? </src><tgt>실제로 교육을 얼마나 받았나요?</tgt>` | 1475 |
| 6 | `<src>graduate from high school? </src><tgt>고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>고등학교를 졸업했나요?</tgt>` | 2436 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level of </src><tgt><\|wait\|></tgt>` | 1038 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt>그게 한 단계입니다.</tgt>` | `<src>attainment. </src><tgt>그게 한 단계의 학력 수준입니다.</tgt>` | 1701 |
| 9 | `<src>to college, </src><tgt>대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>대학에 다녔나요?</tgt>` | 2522 |
| 10 | `<src>and if so, did you graduate? </src><tgt>그렇다면 졸업하셨나요?</tgt>` | `<src>And if so, </src><tgt>만약 그렇다면,</tgt>` | 1766 |
| 11 | `<src>That's another level of </src><tgt>그게 또 다른 단계입니다.</tgt>` | `<src>did you graduate? </src><tgt>졸업했나요?</tgt>` | 2011 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>That's another level of attainment. </src><tgt>그게 또 다른 학력 수준입니다.</tgt>` | 1508 |
| 13 | `<src>So that's it for </src><tgt>그럼</tgt>` | `<src>So that's it </src><tgt>그게</tgt>` | 964 |
| 14 | `<src>now. I'll see you </src><tgt>오늘은 여기까지 하겠습니다.</tgt>` | `<src>for now. I'll see you </src><tgt>지금까지입니다. 그럼</tgt>` | 713 |
| 15 | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>온라인에서 뵙겠습니다.</tgt>` | 622 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt>だから、</tgt>` | 1042 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt>もちろん、こうしたケースも</tgt>` | `<src>뭐 물론 이제 </src><tgt>もちろん、</tgt>` | 831 |
| 3 | `<src>있습니다. </src><tgt>あります。</tgt>` | `<src>이런 경우 들도 있습니다. </src><tgt>こういうケースもあります。</tgt>` | 1216 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | `<src>저희 가 A라는 사람 과 </src><tgt>Aさんと</tgt>` | 1605 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt>Bさんはお互いに</tgt>` | `<src>B라는 사람 이 </src><tgt>Bさんが</tgt>` | 1162 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨턴트 예요. </src><tgt>お互いにコンテンツを</tgt>` | 1827 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이게 컨턴트 예요. </src><tgt>持っているんです。まあ、これがコンテンツなんです。</tgt>` | 1909 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt>模擬ハッキングのコンサルタントです。例えば、</tgt>` | `<src>그리고 </src><tgt>そして、</tgt>` | 1490 |
| 9 | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>Aさんが</tgt>` | 923 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt>何らかの悪性コードを</tgt>` | `<src>어떤 악성 코드 를 </src><tgt>悪意のあるコードを</tgt>` | 2662 |
| 11 | `<src>뿌렸 을 때 </src><tgt>配布したとします。その場合、</tgt>` | `<src>줬을 때 </src><tgt>渡したとき、</tgt>` | 1433 |
| 12 | `<src>B라는 사람 이 </src><tgt>Bさんは</tgt>` | `<src>비라는 사람이 </src><tgt>Bさんが</tgt>` | 1926 |
| 13 | `<src>실제 </src><tgt>実際の</tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1275 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt>クロスサイトスクリプティングから</tgt>` | `<src>크로 사이트 스크립트 에서 </src><tgt>実際にクロスサイトスクリプトで</tgt>` | 1395 |
| 15 | `<src>EX 파일 까지 </src><tgt>EXEファイルまで</tgt>` | `<src>예시 파일 까지 </src><tgt>例のファイルまで</tgt>` | 505 |
| 16 | `<src>감염 이 될까. </src><tgt>感染してしまうのか、というケースです。</tgt>` | `<src>감염 이 될까 </src><tgt>感染するかもしれない</tgt>` | 591 |

---

### Test Example 47 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt>This is,</tgt>` | 1071 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1204 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>と言だったりして、</src><tgt>well, it's a visual development environment,</tgt>` | 1959 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython</src><tgt><\|wait\|></tgt>` | 1502 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt>it's a visual Python development environment.</tgt>` | `<src>開発環境なんですね。</src><tgt>a visual Python development environment.</tgt>` | 1233 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのも</src><tgt>That's because</tgt>` | 1717 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフビジュアルに</src><tgt><\|wait\|></tgt>` | 1106 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>書いてあとそれとは</src><tgt><\|wait\|></tgt>` | 1589 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコードを</src><tgt><\|wait\|></tgt>` | 1600 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成させて、それが</src><tgt><\|wait\|></tgt>` | 2153 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1039 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt><\|wait\|></tgt>` | 1824 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>ことに</src><tgt><\|wait\|></tgt>` | 1332 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なっているので。</src><tgt>you write a flow graph in Visual, then generate Python code from that, and that code executes to perform signal processing.</tgt>` | 1507 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 781 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はいじゃあ</src><tgt>Okay,</tgt>` | 643 |

---

### Test Example 48 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1091 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉</src><tgt><\|wait\|></tgt>` | 1190 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt><\|wait\|></tgt>` | 1181 |
| 4 | `<src>真实意图的，</src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>或真实意图的。</src><tgt>相手の感情や本心を見抜こうとすること。</tgt>` | 2324 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1086 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt>多くの場合、</tgt>` | 1727 |
| 7 | `<src>很多时候经常</src><tgt>するとき、</tgt>` | `<src>好经常会</src><tgt><\|wait\|></tgt>` | 1124 |
| 8 | `<src>会听到人们</src><tgt>よく耳にするのが</tgt>` | `<src>听到人们这样说：</src><tgt>よく</tgt>` | 1554 |
| 9 | `<src>这样说：“</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1402 |
| 10 | `<src>你们看，</src><tgt>「ほら、</tgt>` | `<src>你们看，</src><tgt>「見て、</tgt>` | 1699 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt>この人は</tgt>` | 1470 |
| 12 | `<src>又在说谎了，</src><tgt>また嘘をついている。</tgt>` | `<src>又在说谎了。</src><tgt>また嘘をついているよ」って言われるんです。</tgt>` | 2051 |
| 13 | `<src>他的眼睛</src><tgt>目が</tgt>` | `<src>他的眼睛</src><tgt>彼の目は</tgt>` | 965 |
| 14 | `<src>已经说明了一切。”</src><tgt>すべてを物語っているよ」という言葉です。</tgt>` | `<src>已经说明了一切。</src><tgt>すべてを物語っている。</tgt>` | 1253 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 784 |
| 16 | `<src>也就是说。</src><tgt>つまり…</tgt>` | `<src>也就是说，</src><tgt>つまり、</tgt>` | 750 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt>言っていること。</tgt>` | 642 |

---

### Test Example 49 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, </src><tgt>活動、</tgt>` | 1094 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>then self-defining </src><tgt><\|wait\|></tgt>` | 1156 |
| 4 | `<src>the standard is because you're </src><tgt>基準であるかを自己定義するよりも、あなたが</tgt>` | `<src>what we think that standard is, </src><tgt>そして自分にとっての基準を定義する。</tgt>` | 2228 |
| 5 | `<src>absolutely correct, </src><tgt>完全に正しいのです。</tgt>` | `<src>because you're absolutely correct. </src><tgt>その基準は絶対に正しい。</tgt>` | 1064 |
| 6 | `<src>but the reality </src><tgt>しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1975 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>But the reality is that </src><tgt>しかし、現実は</tgt>` | 1220 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new cat </src><tgt>、私たちが</tgt>` | 1699 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>in the box, and because </src><tgt>箱の中の新しい猫だから、</tgt>` | 2647 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt>基準が</tgt>` | 1675 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1152 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>changed from twenty years ago, </src><tgt>20年前に変わってから、</tgt>` | 1241 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt>私たちは</tgt>` | 1544 |
| 14 | `<src>a higher standard because </src><tgt>より高い基準を求められています。なぜなら、</tgt>` | `<src>a higher standard </src><tgt>より高い基準を</tgt>` | 966 |
| 15 | `<src>everything at this point is being </src><tgt>今はすべてが</tgt>` | `<src>because everything at this point </src><tgt>守らなければならないんです。なぜなら、今の</tgt>` | 979 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められているからです。</tgt>` | `<src>is being held to </src><tgt>すべてが</tgt>` | 708 |

---

### Test Example 50 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt>そしてこれについて</tgt>` | `<src>그리고 이에 대해 </src><tgt>そして、これについて</tgt>` | 801 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt>多くの人々が分析を</tgt>` | `<src>많은 사람 들이 </src><tgt>多くの人が</tgt>` | 1144 |
| 3 | `<src>내놓 았습니다. </src><tgt>出しています。</tgt>` | `<src>분석 을 해놓았습니다. </src><tgt>分析をしています。</tgt>` | 1485 |
| 4 | `<src>여기 로쿠자 의 </src><tgt>こちらの</tgt>` | `<src>여기 </src><tgt>ここで</tgt>` | 1016 |
| 5 | `<src>분석 을 보시면 </src><tgt>ロクザの分析を見ると、</tgt>` | `<src>이 로쿠자 의 분석 을 보시면 </src><tgt>ロクジャの分析を見ると、</tgt>` | 1786 |
| 6 | `<src>소니가 </src><tgt>ソニーが</tgt>` | `<src>소니 가 </src><tgt>ソニーが</tgt>` | 1967 |
| 7 | `<src>26비트 FP </src><tgt>26ビット</tgt>` | `<src>이력 칩에 </src><tgt>イエロクチップに</tgt>` | 1312 |
| 8 | `<src>파이프 를 </src><tgt>FPパイプを</tgt>` | `<src>FDP 파이프 를 </src><tgt>FDPパイプを</tgt>` | 1713 |
| 9 | `<src>128비트로 낮춘 </src><tgt>128ビットに下げた</tgt>` | `<src>128비트 로 </src><tgt>128ビットに</tgt>` | 2580 |
| 10 | `<src>것으로 보인다. </src><tgt>ようです。</tgt>` | `<src>나충가서 로 보인 다. </src><tgt>ナッシュが</tgt>` | 1893 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1906 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>엑스박스 시리즈, </src><tgt>Xboxシリーズ、</tgt>` | 1079 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>엑스에서도 없는 </src><tgt>Xboxにもない</tgt>` | 1140 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시, </src><tgt>インフィニットキャッシュ、</tgt>` | 876 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>S가 여기 도 없다. </src><tgt>Sもありません。</tgt>` | 742 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 702 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt>프로이트가</tgt>` | `<src>Fourth, </src><tgt>넷째,</tgt>` | 776 |
| 2 | `<src>首次觉知到</src><tgt>처음으로</tgt>` | `<src>the author </src><tgt><\|wait\|></tgt>` | 913 |
| 3 | `<src>那个现象：</src><tgt>그 현상을 알아차렸습니다.</tgt>` | `<src>should have understood that </src><tgt>저자는</tgt>` | 1011 |
| 4 | `<src>每当我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1360 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>me and we </src><tgt><\|wait\|></tgt>` | 1436 |
| 6 | `<src>处于爱之中，</src><tgt>사랑 속에</tgt>` | `<src>are in love </src><tgt><\|wait\|></tgt>` | 1090 |
| 7 | `<src>所谓的爱，</src><tgt>있을 때—소위</tgt>` | `<src>with each other. </src><tgt>우리 서로 사랑하고 있다는 걸 이해했어야 합니다.</tgt>` | 2458 |
| 8 | `<src>我们也</src><tgt>사랑이라 부르는 것—우리는</tgt>` | `<src>我们</src><tgt><\|wait\|></tgt>` | 1151 |
| 9 | `<src>同时进入恨。</src><tgt>동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>也同时进入恨。</src><tgt>우리도 동시에 서로를 미워하고 있습니다.</tgt>` | 1268 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2328 |
| 11 | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | `<src>在早上的时候，</src><tgt>아침에는</tgt>` | 1801 |
| 12 | `<src>它是爱；</src><tgt>그것이 사랑이지만,</tgt>` | `<src>他是不爱。</src><tgt>그는 사랑하지 않습니다.</tgt>` | 1655 |
| 13 | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | `<src>到了晚上，</src><tgt>밤이 되면</tgt>` | 595 |
| 14 | `<src>它就变成恨。</src><tgt>미움으로 변합니다.</tgt>` | `<src>他就变成恨。</src><tgt>그는 미워하게 됩니다.</tgt>` | 1553 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1021 |
| 16 | `<src>那个钟摆</src><tgt>그 시계추는</tgt>` | `<src>那个钟摆。</src><tgt>그 시계추처럼요.</tgt>` | 714 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 365 |
| 18 | `<src>继续在移动。</src><tgt>계속 움직이고 있습니다.</tgt>` | `<src>继续在移动。</src><tgt>계속 움직입니다.</tgt>` | 713 |

---

### Test Example 52 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 </src><tgt><\|wait\|></tgt>` | 959 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>인증 하는 </src><tgt><\|wait\|></tgt>` | 1144 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>흐름 을 보인다면 </src><tgt>If the stock index is showing an upward trend,</tgt>` | 1992 |
| 4 | `<src>이런 대형주 도 </src><tgt>these large- cap stocks</tgt>` | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | 1520 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1107 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>will see significant gains.</tgt>` | `<src>큰 폭의 상승 을 </src><tgt><\|wait\|></tgt>` | 2029 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 </src><tgt>then these large- cap stocks will likely rise sharply.</tgt>` | 1129 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt><\|wait\|></tgt>` | 1485 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | 2118 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 1285 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 </src><tgt><\|wait\|></tgt>` | 1141 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>움직이 기 때문 에 </src><tgt>However, since lighter stocks usually lead the market first,</tgt>` | 2150 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시 총이 </src><tgt><\|wait\|></tgt>` | 1677 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 959 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt><\|wait\|></tgt>` | 818 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt>you should keep an eye on those lighter stocks.</tgt>` | 828 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1046 |
| 2 | `<src>Also, </src><tgt>另外，</tgt>` | `<src>Also, </src><tgt>另外，</tgt>` | 1087 |
| 3 | `<src>you will not be able to </src><tgt>你没法</tgt>` | `<src>you will not be able to move </src><tgt><\|wait\|></tgt>` | 1188 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>meedia objects </src><tgt><\|wait\|></tgt>` | 1496 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1260 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources </src><tgt><\|wait\|></tgt>` | 971 |
| 7 | `<src>So, if </src><tgt>所以，如果</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1659 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>though if you get into </src><tgt><\|wait\|></tgt>` | 1116 |
| 9 | `<src>a situation </src><tgt><\|wait\|></tgt>` | `<src>a situation </src><tgt><\|wait\|></tgt>` | 1486 |
| 10 | `<src>where you realize </src><tgt>你发现自己</tgt>` | `<src>where you realize you've added </src><tgt><\|wait\|></tgt>` | 2022 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1316 |
| 12 | `<src>files to a particular resource, </src><tgt>给某个资源加错了媒体文件，就</tgt>` | `<src>the wrong media files </src><tgt><\|wait\|></tgt>` | 1349 |
| 13 | `<src>you need to let us know, </src><tgt>告诉我们一声。</tgt>` | `<src>to a particular resource, </src><tgt><\|wait\|></tgt>` | 1983 |
| 14 | `<src>and we can see about </src><tgt>我们可以帮你想想办法</tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1425 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 995 |
| 16 | `<src>moving those media files and then making sure they </src><tgt>把那些媒体文件移过去，然后确保它们</tgt>` | `<src>giving those media files </src><tgt><\|wait\|></tgt>` | 499 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>and then making sure </src><tgt><\|wait\|></tgt>` | 783 |
| 18 | `<src>properly. </src><tgt>都备份好。</tgt>` | `<src>they get backed up properly. </src><tgt>你也不能在资源之间移动媒体对象。不过，如果你发现把错误的媒体文件添加到了某个资源中，我们可以查看这些媒体文件，并确保它们被正确备份。</tgt>` | 1319 |

---

### Test Example 54 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt>ある時、</tgt>` | `<src>And at one point, </src><tgt>ある時点で、</tgt>` | 833 |
| 2 | `<src>he knows Jesus </src><tgt>彼はイエスが</tgt>` | `<src>he knows Jesus </src><tgt>彼は</tgt>` | 1071 |
| 3 | `<src>is hungry. </src><tgt>空腹だと知っています。</tgt>` | `<src>is hungry, </src><tgt>イエスが飢えていることを知っていました。</tgt>` | 1561 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt>そして、</tgt>` | 1244 |
| 5 | `<src>he's been without food, </src><tgt>食べ物をとらずに</tgt>` | `<src>he's going to </src><tgt>イエスが</tgt>` | 1328 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt>荒野に</tgt>` | 1405 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。</tgt>` | `<src>for forty days </src><tgt>40日間いることを知っていました。</tgt>` | 1633 |
| 8 | `<src>And so he says </src><tgt>で、彼は</tgt>` | `<src>that he's hungry, </src><tgt>そして、</tgt>` | 1637 |
| 9 | `<src>to Jesus," Hey, </src><tgt>イエスに言うんです。「おい、</tgt>` | `<src>and so he says to Jesus, </src><tgt>イエスが飢えていることを知っていたので、イエスにこう言いました。</tgt>` | 1466 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt>お前が神の子なら、証明してみろよ。</tgt>` | `<src>If you're the Son of God, prove it </src><tgt>「もしあなたが神の子なら、</tgt>` | 3212 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1079 |
| 12 | `<src>Turn these stones to bread." </src><tgt>この石をパンに変えてみろ」。</tgt>` | `<src>turn these stones to bread. </src><tgt>この石をパンに変えてみせなさい。」</tgt>` | 1470 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did </src><tgt>どうして</tgt>` | 1442 |
| 14 | `<src>How did Jesus deal with that </src><tgt>イエスは</tgt>` | `<src>Jesus deal with that </src><tgt>イエスは</tgt>` | 1077 |
| 15 | `<src>temptation? </src><tgt>その誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>その誘惑に立ち向かったのでしょうか。</tgt>` | 902 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 666 |
| 17 | `<src>Man shall not live </src><tgt>人は</tgt>` | `<src>Man, Jonathan </src><tgt>いや、</tgt>` | 397 |
| 18 | `<src>by bread alone. </src><tgt>パンだけで生きるものではない。</tgt>` | `<src>lead by bread alone. </src><tgt>ヨナタンはパンだけで導いたんです。</tgt>` | 508 |

---

### Test Example 55 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt>少し</tgt>` | 1260 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in the wrong mile </src><tgt><\|wait\|></tgt>` | 1206 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>in the first section </src><tgt>最初のセクションで</tgt>` | 1343 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1455 |
| 5 | `<src>about the EHR fields </src><tgt>EHRフィールドの</tgt>` | `<src>about the AHR field </src><tgt>AHRの</tgt>` | 1260 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1480 |
| 7 | `<src>being of critical importance </src><tgt>決定的な重要性と、</tgt>` | `<src>being of critical importance </src><tgt>重要性について、少しズレていました。</tgt>` | 1617 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1567 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 873 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt>バリアントデータベースと</tgt>` | 2326 |
| 11 | `<src>which is obviously one of my loves. </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>which is obviously one of my loves. </src><tgt>バリアントデータベースは、もちろん大好きです。</tgt>` | 2043 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that </src><tgt>それは</tgt>` | 1689 |
| 13 | `<src>Is that if we don't agree </src><tgt>つまり、</tgt>` | `<src>if we don't agree </src><tgt>、</tgt>` | 1298 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>upon the fields </src><tgt><\|wait\|></tgt>` | 958 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>that need to be in </src><tgt><\|wait\|></tgt>` | 751 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>these data sources </src><tgt>これらのデータソースに</tgt>` | 775 |
| 17 | `<src>draw from, </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、</tgt>` | `<src>that we can draw from? </src><tgt>必要なフィールドについて合意できなければ、</tgt>` | 788 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>There's nothing to draw from, right? </src><tgt>それから引き出すものがないですよね？</tgt>` | 597 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 437 |

---

### Test Example 56 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt>그럼</tgt>` | `<src>那我们看一下</src><tgt>자, 그럼</tgt>` | 1011 |
| 2 | `<src>它的图片哦，</src><tgt>사진을 한번 볼까요?</tgt>` | `<src>它的图片哦，</src><tgt>그림을 한번 볼까요?</tgt>` | 1293 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1094 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt>사진 부분을 보면</tgt>` | `<src>图片的部分呢，</src><tgt>그림 부분은</tgt>` | 1890 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到</src><tgt><\|wait\|></tgt>` | 992 |
| 6 | `<src>的部分。</src><tgt>거실 공간이 보이네요.</tgt>` | `<src>一个是克汀的部分，</src><tgt>크레틴 부분,</tgt>` | 1634 |
| 7 | `<src>那客厅一般</src><tgt>거실은 보통</tgt>` | `<src>克汀一般</src><tgt>크레틴은 보통</tgt>` | 1378 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>都是属于</src><tgt><\|wait\|></tgt>` | 1600 |
| 9 | `<src>我们</src><tgt>우리가</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 761 |
| 10 | `<src>在休息的地方，</src><tgt>쉬는 곳이잖아요.</tgt>` | `<src>我们在吸收</src><tgt><\|wait\|></tgt>` | 2330 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>的地方，</src><tgt>우리가 흡수하는 곳에</tgt>` | 1821 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>그래서</tgt>` | `<src>所以呢，</src><tgt>있으니까요.</tgt>` | 1401 |
| 13 | `<src>也会反映的是</src><tgt>이 신체 부위도</tgt>` | `<src>这是身体的部分会反应的是</src><tgt>그러니까 우리 몸의 부분은</tgt>` | 948 |
| 14 | `<src>你需要给自己</src><tgt>여러분이 자신에게</tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1598 |
| 15 | `<src>一点时间，</src><tgt>시간을 내서</tgt>` | `<src>自己一点时间</src><tgt><\|wait\|></tgt>` | 927 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>可以好好的做</src><tgt><\|wait\|></tgt>` | 851 |
| 17 | `<src>坐下来休息。可是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데</tgt>` | `<src>下来吸收，</src><tgt>흡수할 시간을 좀 줘야 해요.</tgt>` | 632 |
| 18 | `<src>我们可以看到这边是</src><tgt>여기는</tgt>` | `<src>可我们可以看到</src><tgt>그리고</tgt>` | 444 |
| 19 | `<src>空无一人的嘛，</src><tgt>아무도 없네요.</tgt>` | `<src>这边是双五一人的嘛。</src><tgt>여기서 551인 사람이 보이죠?</tgt>` | 572 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt>자,</tgt>` | 298 |
| 21 | `<src>所以是说。</src><tgt>그래서 말인데...</tgt>` | `<src>说一些</src><tgt><\|wait\|></tgt>` | 382 |

---

### Test Example 57 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1167 |
| 2 | `<src>Meaningful individual </src><tgt>有意义的</tgt>` | `<src>Meaningful </src><tgt><\|wait\|></tgt>` | 832 |
| 3 | `<src>right, </src><tgt>个人权利，</tgt>` | `<src>individual write </src><tgt><\|wait\|></tgt>` | 1084 |
| 4 | `<src>and the Supreme Court </src><tgt>而最高法院</tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1388 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1431 |
| 6 | `<src>last, not leading. </src><tgt>是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. And I don't know </src><tgt>有意义的个人写作，最高法院最后才出现，而不是领导者。</tgt>` | 2465 |
| 7 | `<src>And I don't think the courts want to be </src><tgt>我不认为</tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1426 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1628 |
| 9 | `<src>the the vanguard of social </src><tgt><\|wait\|></tgt>` | `<src>the vanguard of </src><tgt><\|wait\|></tgt>` | 1179 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt>我不知道法院是否想成为社会变革的先锋。</tgt>` | 2697 |
| 11 | `<src>these days, </src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src>These days, </src><tgt>如今，</tgt>` | 908 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>but they rather </src><tgt>但他们更倾向于</tgt>` | 1892 |
| 13 | `<src>but they rather reflect </src><tgt>它们更倾向于</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1184 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>reflect the consensus </src><tgt><\|wait\|></tgt>` | 959 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that's already </src><tgt><\|wait\|></tgt>` | 814 |
| 16 | `<src>that's already emerged. </src><tgt>反映已经形成的共识。</tgt>` | `<src>emerged. </src><tgt>反映已经形成的共识。</tgt>` | 816 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So. </src><tgt>所以。</tgt>` | 576 |
| 18 | `<src>So you have some </src><tgt>所以，</tgt>` | `<src>You have </src><tgt><\|wait\|></tgt>` | 413 |
| 19 | `<src>federal judges </src><tgt>有些联邦法官……</tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 439 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 416 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt>你有一些联邦法官，他们……</tgt>` | 431 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt>こうした人々は</tgt>` | `<src>These people are </src><tgt>この人たちは</tgt>` | 857 |
| 2 | `<src>completely rare, </src><tgt>非常に稀です。</tgt>` | `<src>completely rare, </src><tgt>完全に</tgt>` | 1104 |
| 3 | `<src>and they often </src><tgt>そして、</tgt>` | `<src>and they often </src><tgt>珍しく、</tgt>` | 1168 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up </src><tgt><\|wait\|></tgt>` | 1399 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1265 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するよう、よく現れます。</tgt>` | 1905 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1409 |
| 8 | `<src>Their personality is </src><tgt>彼らの性格は</tgt>` | `<src>The personality is </src><tgt>その性格は</tgt>` | 1436 |
| 9 | `<src>something of a </src><tgt><\|wait\|></tgt>` | `<src>something of a contradiction. </src><tgt>矛盾をはらんでいます。</tgt>` | 858 |
| 10 | `<src>contradiction. </src><tgt>矛盾しています。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2357 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>Well, they're </src><tgt>まあ、</tgt>` | 1777 |
| 12 | `<src>extroverted, </src><tgt>外交的である一方、</tgt>` | `<src>extroverted. </src><tgt>外向的です。</tgt>` | 1247 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>They also hate </src><tgt>また</tgt>` | 1064 |
| 14 | `<src>meaningless conversations </src><tgt>無意味な会話は嫌います。</tgt>` | `<src>meaningless conversations. </src><tgt>無意味な会話も嫌います。</tgt>` | 1591 |
| 15 | `<src>and like to </src><tgt>そして、</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1017 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like to get straight to the </src><tgt>そして</tgt>` | 797 |
| 17 | `<src>get straight to the point. </src><tgt>要点を突くのを好みます。</tgt>` | `<src>point. </src><tgt>要点をまっすぐ言うのが好きです。</tgt>` | 510 |
| 18 | `<src>They also love to </src><tgt>また、</tgt>` | `<src>They also love </src><tgt>彼らは</tgt>` | 464 |
| 19 | `<src>play </src><tgt>あえて</tgt>` | `<src>to play </src><tgt><\|wait\|></tgt>` | 490 |
| 20 | `<src>the devil's advocate, and they </src><tgt>悪魔の代弁者を演じることを好み、</tgt>` | `<src>the devil's advocate, </src><tgt>悪魔の代弁者になるのも好きで、</tgt>` | 505 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and never shy away </src><tgt>決して</tgt>` | 332 |
| 22 | `<src>never shy away from a debate. </src><tgt>議論を避けることはありません。</tgt>` | `<src>from a debate. </src><tgt>議論を避けることはありません。</tgt>` | 334 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 360 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>E.T.P. </src><tgt>E.T.P.は</tgt>` | 403 |
| 25 | `<src>ENTP stands for </src><tgt>ENTPとは</tgt>` | `<src>stands for. </src><tgt>「</tgt>` | 320 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>이전 의 이준석은 </src><tgt>Lee Jun- seok used to</tgt>` | 1069 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>정무 를 </src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>거부 한 명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1664 |
| 4 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake—</tgt>` | `<src>위해서 하면서 </src><tgt><\|wait\|></tgt>` | 1402 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선을 </src><tgt><\|wait\|></tgt>` | 1156 |
| 6 | `<src>위해서 라면서 </src><tgt>for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1980 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1188 |
| 8 | `<src>냈지만 이제 는 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>냈지만 </src><tgt><\|wait\|></tgt>` | 1538 |
| 9 | `<src>윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | `<src>이제 는 윤석열 후보 가 </src><tgt><\|wait\|></tgt>` | 1251 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 2034 |
| 11 | `<src>제거 한 순간 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in,</tgt>` | `<src>제거 한 순간, </src><tgt><\|wait\|></tgt>` | 1537 |
| 12 | `<src>이준석은 </src><tgt>Lee Jun -seok</tgt>` | `<src>이준석 은 들은 해놓고 </src><tgt><\|wait\|></tgt>` | 2035 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1507 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리겠다는 </src><tgt><\|wait\|></tgt>` | 1095 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>도끼 를 품은 </src><tgt><\|wait\|></tgt>` | 824 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>공격 성을 </src><tgt><\|wait\|></tgt>` | 377 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 587 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 486 |
| 19 | `<src>것입니다. </src><tgt>And then there's</tgt>` | `<src>작정 한 것입니다. </src><tgt>He was quite eager to win the election, even going to great lengths to make it look like he was just doing it for the candidate. But now that Yoon Suk- yeol has removed Kim Jong- in, Lee Jun- seok has put his foot down, ready to attack Yoon Suk- yeol.</tgt>` | 1146 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 382 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석 청상납건 </src><tgt><\|wait\|></tgt>` | 370 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 359 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 345 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기 </src><tgt><\|wait\|></tgt>` | 284 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재 입니까? </src><tgt>Lee Jun- seok's ' Cheong- sang- nap' scandal— how much of a boon is that for the Democratic Party?</tgt>` | 625 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>でまあ</src><tgt>So, well,</tgt>` | 1081 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後の</src><tgt><\|wait\|></tgt>` | 1124 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>今作ってみたいな</src><tgt><\|wait\|></tgt>` | 1173 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>です。なので</src><tgt>I want to make something after dinner. So,</tgt>` | 2110 |
| 5 | `<src>ゴールドストーンホテル</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>ここのねゴルフスロホテル</src><tgt><\|wait\|></tgt>` | 1113 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も朝食が</src><tgt><\|wait\|></tgt>` | 2031 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1080 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1529 |
| 9 | `<src>予定になってるので</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>I'm planning to go to the Golf Suro Hotel here, and it's a place where you can have breakfast.</tgt>` | 2767 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt>So, going forward,</tgt>` | 1783 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 1234 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたいな</src><tgt><\|wait\|></tgt>` | 1083 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>という方はですね</src><tgt>if you're thinking of staying at the Golf Suro Hotel,</tgt>` | 1794 |
| 14 | `<src>検討なさってみて</src><tgt>thinking about staying here in the future,</tgt>` | `<src>検討なさって</src><tgt><\|wait\|></tgt>` | 896 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見てもまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 849 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと</src><tgt><\|wait\|></tgt>` | 596 |
| 17 | `<src>なとはい思いますここ</src><tgt>it might be worth considering.</tgt>` | `<src>思います。</src><tgt>I think it's a good option.</tgt>` | 504 |
| 18 | `<src>のホテルからですね釜山</src><tgt>From this hotel,</tgt>` | `<src>ここホテルからですね</src><tgt>From here,</tgt>` | 426 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 416 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 386 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一本かかる</src><tgt><\|wait\|></tgt>` | 208 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないか</src><tgt><\|wait\|></tgt>` | 343 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 321 |
| 24 | `<src>立地のいいねまあ</src><tgt>so the location is really good.</tgt>` | `<src>立地ねまあホテル</src><tgt><\|wait\|></tgt>` | 381 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 345 |
| 26 | `<src>よかったらですね</src><tgt>If you'd like,</tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 308 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさって</src><tgt><\|wait\|></tgt>` | 335 |
| 28 | `<src>ください</src><tgt>please consider it.</tgt>` | `<src>みてください。それでは</src><tgt>it's just a one- mile walk to Busan Station from the hotel. It's a really well- located hotel, so please consider it. Well,</tgt>` | 447 |
| 29 | `<src>それではですね今回は。</src><tgt>So, for this time...</tgt>` | `<src>ね今回は</src><tgt>this time,</tgt>` | 202 |
