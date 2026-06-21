# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9694
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.3245
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
  - PROCESS_TIME_MS_AVG: 1422.2900
  - PROCESS_TIME_MS_P50: 1438.7310
  - PROCESS_TIME_MS_P95: 2508.6040
  - PROCESS_TIME_MS_MAX: 3267.8980

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>我的</src>` | 2180 |
| 2 | `<src>挖一点松子儿里</src>` | `<src>送纸的地方，</src>` | 890 |
| 3 | `<src>边，这个油性也很大。</src>` | `<src>这个友邻也很大，</src>` | 1124 |
| 4 | `<src>然后</src>` | `<src>然后</src>` | 1043 |
| 5 | `<src><\|wait\|></src>` | `<src>呢，</src>` | 1570 |
| 6 | `<src>呢，我再放一点</src>` | `<src>我在放个</src>` | 418 |
| 7 | `<src>儿核桃</src>` | `<src>热汤儿，</src>` | 1397 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 588 |
| 9 | `<src>仁儿，仁儿里边</src>` | `<src>在礼器，</src>` | 2435 |
| 10 | `<src>这种核桃</src>` | `<src>这种热汤儿</src>` | 1486 |
| 11 | `<src>仁儿。</src>` | `<src>啊。</src>` | 1805 |

---

### Test Example 2 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要切肤，</src>` | 2034 |
| 2 | `<src>要气熟是容易的，</src>` | `<src>是容易的。</src>` | 1147 |
| 3 | `<src>但是</src>` | `<src>但是</src>` | 661 |
| 4 | `<src>只有一个师父</src>` | `<src>只有</src>` | 1124 |
| 5 | `<src><\|wait\|></src>` | `<src>一个师傅指导</src>` | 411 |
| 6 | `<src>知道如何</src>` | `<src><\|wait\|></src>` | 1516 |
| 7 | `<src>处于中间，</src>` | `<src>如何处于中间，</src>` | 1711 |
| 8 | `<src>所以</src>` | `<src>所以</src>` | 2243 |
| 9 | `<src>虚阿凡</src>` | `<src>需要反。</src>` | 781 |
| 10 | `<src>要成为</src>` | `<src>要成为</src>` | 1867 |
| 11 | `<src>一个师父。</src>` | `<src>一个师傅，</src>` | 2622 |

---

### Test Example 3 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2052 |
| 2 | `<src>抛洒完以后呢，</src>` | `<src>淘沙完以后呢，</src>` | 1650 |
| 3 | `<src>内部的压力减轻，</src>` | `<src>内部的压力减轻，</src>` | 1088 |
| 4 | `<src>能量也衰弱了，</src>` | `<src>能量也衰弱了。</src>` | 425 |
| 5 | `<src>然后</src>` | `<src>然后</src>` | 1660 |
| 6 | `<src>就停留在一个</src>` | `<src>就停留在</src>` | 921 |
| 7 | `<src>相对的低</src>` | `<src>一个相对的</src>` | 872 |
| 8 | `<src>能量的运行</src>` | `<src>低能量的</src>` | 2558 |
| 9 | `<src>状态，</src>` | `<src>运行状态。</src>` | 674 |
| 10 | `<src>这就是所谓的</src>` | `<src>这就是所谓的</src>` | 1843 |
| 11 | `<src>抑郁状态。</src>` | `<src>蚁居状态。</src>` | 2550 |

---

### Test Example 4 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src>` | `<src>자 저는 </src>` | 1985 |
| 2 | `<src>옹심이, </src>` | `<src>용심이 </src>` | 1081 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 864 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src>` | `<src>칼 용심이 </src>` | 1127 |
| 5 | `<src>옹심이가 </src>` | `<src>어설프 용심이가 </src>` | 1900 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1482 |
| 7 | `<src>섞여 있는 건데요. </src>` | `<src>섞이 는 건데요. </src>` | 1191 |
| 8 | `<src>야, </src>` | `<src>야 </src>` | 1674 |
| 9 | `<src>진짜 이거 </src>` | `<src>진짜 이거 </src>` | 1463 |
| 10 | `<src>해장으로도 조금 죽입니다, </src>` | `<src>해행으로 </src>` | 1618 |
| 11 | `<src>진짜. </src>` | `<src>조금 주기 만 되는 </src>` | 2177 |

---

### Test Example 5 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src>` | `<src>また</src>` | 2155 |
| 2 | `<src>距離が</src>` | `<src>またちょっと距離が</src>` | 876 |
| 3 | `<src>離れてくるみたいな感じ、</src>` | `<src>離れてくるみたいな感じで</src>` | 1091 |
| 4 | `<src>オシャレる方がやっぱ</src>` | `<src>大社から</src>` | 1093 |
| 5 | `<src>多いですね。</src>` | `<src>タタカにパオイですね。</src>` | 1859 |
| 6 | `<src>開業したい方って</src>` | `<src>解消したい方って</src>` | 900 |
| 7 | `<src>すごい</src>` | `<src>すぐパオイ行き来して다가</src>` | 908 |
| 8 | `<src>自己意識高いし、</src>` | `<src>シー</src>` | 1501 |
| 9 | `<src>自分で</src>` | `<src>で見てみて</src>` | 1445 |
| 10 | `<src>全部ちょっと次の投資</src>` | `<src>とこも変なとこで</src>` | 1616 |
| 11 | `<src>傾向が強いので、</src>` | `<src>シャゴが強いので</src>` | 2754 |
| 12 | `<src>なので。</src>` | `<src>なので</src>` | 641 |

---

### Test Example 6 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>面对这个情况，</src>` | 1919 |
| 2 | `<src>面对这个情况，我们就是</src>` | `<src>我们就是</src>` | 1148 |
| 3 | `<src>遇到问题</src>` | `<src>遇到问题</src>` | 783 |
| 4 | `<src>就赶紧的回报主管，</src>` | `<src>就赶紧的回报主管，</src>` | 1169 |
| 5 | `<src>或是通知对方，</src>` | `<src>或是通知对方</src>` | 1742 |
| 6 | `<src>我们现有这个状况，</src>` | `<src>我们学校</src>` | 1504 |
| 7 | `<src>不要想自己</src>` | `<src>这个状况，不要想自己</src>` | 648 |
| 8 | `<src>什么都把它扛下来，</src>` | `<src>什么都把它扛下来，</src>` | 2502 |
| 9 | `<src>独立承担。</src>` | `<src>你無理承担。</src>` | 1390 |
| 10 | `<src>整体而言，</src>` | `<src>整体而言，</src>` | 2340 |
| 11 | `<src>事业运就属凶。</src>` | `<src>是应该做手术。</src>` | 1384 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src>` | `<src>大抵</src>` | 2075 |
| 2 | `<src>このあたりから</src>` | `<src>このあたりから</src>` | 946 |
| 3 | `<src>始めた</src>` | `<src>始めた</src>` | 899 |
| 4 | `<src>もので、</src>` | `<src>もので、</src>` | 1147 |
| 5 | `<src>ゴッホ、</src>` | `<src>方法</src>` | 369 |
| 6 | `<src>ゴーギャン、</src>` | `<src>ゴーギャン</src>` | 1551 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1535 |
| 8 | `<src>セザンヌ、</src>` | `<src>生産の</src>` | 915 |
| 9 | `<src>ルナールなど</src>` | `<src><\|wait\|></src>` | 2068 |
| 10 | `<src>という人の絵</src>` | `<src>ルナールなどの</src>` | 1501 |
| 11 | `<src>は、田舎の</src>` | `<src>絵は</src>` | 2134 |
| 12 | `<src>中学生でも。</src>` | `<src>田舎の中学生でも</src>` | 1637 |

---

### Test Example 8 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>명단 에 있는 </src>` | 2185 |
| 2 | `<src>명단 에 있는 학생 들은 </src>` | `<src>극성 들은 </src>` | 1188 |
| 3 | `<src>실제로 </src>` | `<src>실제로 </src>` | 795 |
| 4 | `<src>지능 이 높지 않았고 </src>` | `<src>지능 이 높지 </src>` | 1131 |
| 5 | `<src><\|wait\|></src>` | `<src>않았고 </src>` | 1767 |
| 6 | `<src>무작위로 </src>` | `<src>무작위 로 뽑힌 </src>` | 1665 |
| 7 | `<src>뽑힌 학생 들이었기 </src>` | `<src>극성 들이 </src>` | 1517 |
| 8 | `<src>때문 입니다. </src>` | `<src>어떤 분입니다. </src>` | 1632 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1766 |
| 10 | `<src>사실 을 몰랐 던 </src>` | `<src>사실 을 </src>` | 2401 |
| 11 | `<src>교사 들은. </src>` | `<src>몰랐 던 교사 들은 </src>` | 867 |

---

### Test Example 9 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>如果</src>` | 1738 |
| 2 | `<src>如果在女高中生</src>` | `<src>在女高中生</src>` | 973 |
| 3 | `<src>与长相古怪的人</src>` | `<src>与长相不怪的人之间</src>` | 1262 |
| 4 | `<src><\|wait\|></src>` | `<src>有着某种</src>` | 917 |
| 5 | `<src>之间有着某种联系，</src>` | `<src>心理，</src>` | 1754 |
| 6 | `<src>难道会是</src>` | `<src>难道会是</src>` | 778 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 990 |
| 8 | `<src>从那天夜里开始的？</src>` | `<src>从天黎明</src>` | 2222 |
| 9 | `<src><\|wait\|></src>` | `<src>开始的？</src>` | 823 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1817 |
| 11 | `<src>杨子思绪</src>` | `<src>杨子思</src>` | 2644 |
| 12 | `<src>连篇。</src>` | `<src>与天篇。</src>` | 640 |

---

### Test Example 10 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>家长需要</src>` | 2162 |
| 2 | `<src>家长需要做的是，</src>` | `<src>做的是，</src>` | 1171 |
| 3 | `<src><\|wait\|></src>` | `<src>用我们</src>` | 786 |
| 4 | `<src>用我们深深的</src>` | `<src><\|wait\|></src>` | 1108 |
| 5 | `<src>爱浇水、</src>` | `<src>深深的爱浇水，</src>` | 1891 |
| 6 | `<src>施肥，</src>` | `<src>所以</src>` | 1589 |
| 7 | `<src>给足</src>` | `<src>可以</src>` | 1344 |
| 8 | `<src>孩子心理营养，</src>` | `<src>住孩子心里，</src>` | 1754 |
| 9 | `<src><\|wait\|></src>` | `<src>营养，</src>` | 1980 |
| 10 | `<src>并耐心等待孩子</src>` | `<src>跟耐心等</src>` | 2597 |
| 11 | `<src>慢慢长大。</src>` | `<src>他孩子慢慢长大。</src>` | 616 |

---

### Test Example 11 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>I am </src>` | 1846 |
| 2 | `<src>아이 엠 애플 을 </src>` | `<src>Abbot, </src>` | 944 |
| 3 | `<src>촉발 시키고 </src>` | `<src>축발시키고 </src>` | 990 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1127 |
| 5 | `<src>자신 의 </src>` | `<src>자신 의 </src>` | 1846 |
| 6 | `<src><\|wait\|></src>` | `<src>부모 를 죽인 </src>` | 1755 |
| 7 | `<src>부모 를 죽인 페르 나 </src>` | `<src>헤르나 </src>` | 2481 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 598 |
| 9 | `<src>박한상과 </src>` | `<src>박한상과 </src>` | 1886 |
| 10 | `<src><\|wait\|></src>` | `<src>같은 세대 들은 </src>` | 2653 |
| 11 | `<src>같은 세대 들입니다. </src>` | `<src>입니다. </src>` | 853 |

---

### Test Example 12 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src>` | `<src>あの</src>` | 1817 |
| 2 | `<src>映画でですね、</src>` | `<src>Aがですね</src>` | 870 |
| 3 | `<src>いろんな場面で</src>` | `<src>いろんな場面で</src>` | 1013 |
| 4 | `<src>映画生息かどうかっていうのを</src>` | `<src>A制服かどうか</src>` | 1182 |
| 5 | `<src>調べるときに、</src>` | `<src>メディアでいう時にまあ</src>` | 1824 |
| 6 | `<src>まあ映画の卵を調べる</src>` | `<src>Aの乱攻を</src>` | 1039 |
| 7 | `<src>ことで、あの</src>` | `<src>調べて、</src>` | 666 |
| 8 | `<src>その生息かどうかっていうのを</src>` | `<src>あのその制服かどうか</src>` | 1735 |
| 9 | `<src>保証する、生息である</src>` | `<src>を調べる、</src>` | 1376 |
| 10 | `<src>ことを保証する</src>` | `<src>制服であること保証する</src>` | 1992 |
| 11 | `<src>といったような</src>` | `<src>といったような使い方を</src>` | 2614 |
| 12 | `<src>使い方をされます。</src>` | `<src>されます。</src>` | 860 |

---

### Test Example 13 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>다른 </src>` | 1872 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src>` | `<src>산줄에 </src>` | 895 |
| 3 | `<src>해가지고 내가 </src>` | `<src>죽여 달라 이거 주고 내가 </src>` | 1145 |
| 4 | `<src>죽이 려고 들어왔 수다. </src>` | `<src>죽이 려고 들어왔 수도다. </src>` | 1279 |
| 5 | `<src>다른 잔찜에 </src>` | `<src>다른 잔찜이 </src>` | 1663 |
| 6 | `<src>죽여 달라 </src>` | `<src>죽여 달라 </src>` | 1650 |
| 7 | `<src>해지 않았느냐? 내가 </src>` | `<src>해달 거냐? 내가 </src>` | 2545 |
| 8 | `<src>그 소리 안 듣고 </src>` | `<src>그 소리 안 듣고 있는 </src>` | 765 |
| 9 | `<src><\|wait\|></src>` | `<src>줄은 아니야. </src>` | 2108 |
| 10 | `<src>있는 줄 알았느냐? 응? </src>` | `<src>어? </src>` | 2344 |
| 11 | `<src>내가 가. </src>` | `<src>내가 </src>` | 957 |

---

### Test Example 14 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src>` | `<src>最初から</src>` | 1749 |
| 2 | `<src>あの特に</src>` | `<src>あの特に</src>` | 1033 |
| 3 | `<src>これなんかまだ</src>` | `<src>子供がまだ</src>` | 920 |
| 4 | `<src>一年生ですからね。</src>` | `<src>1年生ですからね。</src>` | 1132 |
| 5 | `<src>この時点で</src>` | `<src>その時点で</src>` | 1760 |
| 6 | `<src>こう短く</src>` | `<src>こう二次額</src>` | 1714 |
| 7 | `<src>剪定を</src>` | `<src>選択を</src>` | 1820 |
| 8 | `<src><\|wait\|></src>` | `<src>こう対図して</src>` | 1261 |
| 9 | `<src>こうタイズしてってあげると</src>` | `<src>なげると</src>` | 2039 |
| 10 | `<src>十年経っても</src>` | `<src>1年経っても</src>` | 2626 |
| 11 | `<src>大した。</src>` | `<src>大した。</src>` | 1057 |

---

### Test Example 15 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src>` | `<src>Tシャツなどが</src>` | 2156 |
| 2 | `<src>あの</src>` | `<src>あの</src>` | 866 |
| 3 | `<src>いただもらえる</src>` | `<src>いただくという</src>` | 963 |
| 4 | `<src>といったようなものも</src>` | `<src>といったようなものも用意しております</src>` | 1259 |
| 5 | `<src>用意しておりますので</src>` | `<src>のでぜひ</src>` | 1772 |
| 6 | `<src>ぜひご参加ください。</src>` | `<src>ご参加ください。</src>` | 1559 |
| 7 | `<src>ご連絡としては</src>` | `<src>ご連絡としては</src>` | 904 |
| 8 | `<src>以上になりまして、</src>` | `<src>以上になります</src>` | 1909 |
| 9 | `<src>えっと</src>` | `<src>ので、</src>` | 931 |
| 10 | `<src><\|wait\|></src>` | `<src>またのご連絡</src>` | 1920 |
| 11 | `<src>ランチの案内がありますので</src>` | `<src>を楽しみにお待ち</src>` | 2359 |
| 12 | `<src>もう少々お待ちください。</src>` | `<src>ください。</src>` | 1190 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Did varying </src>` | 1842 |
| 2 | `<src>Did very important research </src>` | `<src>research </src>` | 920 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 923 |
| 4 | `<src>on extremely happy people. </src>` | `<src>on extremely happy people? This is </src>` | 1271 |
| 5 | `<src>This is tip of the stem </src>` | `<src>tip of the stem </src>` | 1805 |
| 6 | `<src>research, </src>` | `<src>research. Looking at </src>` | 1677 |
| 7 | `<src>looking at the ten percent </src>` | `<src>a 10% </src>` | 2640 |
| 8 | `<src><\|wait\|></src>` | `<src>of the happiest </src>` | 1464 |
| 9 | `<src>of the happiest people </src>` | `<src>people </src>` | 1484 |
| 10 | `<src>out there, </src>` | `<src>out there, people that </src>` | 2370 |
| 11 | `<src>people that we can learn from. </src>` | `<src>we can learn from. </src>` | 1557 |

---

### Test Example 17 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src>` | `<src>What is your body </src>` | 1744 |
| 2 | `<src>doing? </src>` | `<src>doing? </src>` | 1002 |
| 3 | `<src>Drop into </src>` | `<src>Drop pin to your body. </src>` | 1135 |
| 4 | `<src>your body. </src>` | `<src>Where does </src>` | 901 |
| 5 | `<src>Where does the tension </src>` | `<src>the tension </src>` | 1789 |
| 6 | `<src>start? What is it? </src>` | `<src>start? What is it? </src>` | 1700 |
| 7 | `<src>Is it a headache? </src>` | `<src>Is it a head? </src>` | 2731 |
| 8 | `<src>Is it a tightness in your chest? </src>` | `<src>Is it a tension in your chest? </src>` | 1753 |
| 9 | `<src>I ask them what </src>` | `<src>Or is the body </src>` | 2575 |
| 10 | `<src><\|wait\|></src>` | `<src>landing page </src>` | 937 |
| 11 | `<src>language are you using? </src>` | `<src>you are using? </src>` | 1594 |

---

### Test Example 18 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2170 |
| 2 | `<src>And lastly, </src>` | `<src>And lastly, </src>` | 1174 |
| 3 | `<src>is repeat. </src>` | `<src>is repeat. </src>` | 791 |
| 4 | `<src>Learn to rinse and repeat. </src>` | `<src>Learn to dance, </src>` | 1125 |
| 5 | `<src>Find what you're good at </src>` | `<src>repeat five times, and you're good at </src>` | 1905 |
| 6 | `<src>and do more of it. </src>` | `<src>and do more of it. </src>` | 1662 |
| 7 | `<src><\|wait\|></src>` | `<src>And while you're not </src>` | 2548 |
| 8 | `<src>And what you're not good at, </src>` | `<src>good at it, </src>` | 1193 |
| 9 | `<src>get the people around you to help you with. </src>` | `<src>get to people around you to help you with </src>` | 2171 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1990 |
| 11 | `<src>And until next time. </src>` | `<src>it, and in telling next time </src>` | 1672 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src>` | `<src>이거 </src>` | 1952 |
| 2 | `<src><\|wait\|></src>` | `<src>이거 너무 </src>` | 1338 |
| 3 | `<src>저열한 일일 수 있지만 </src>` | `<src>저열한 데일 수 있지만 </src>` | 1473 |
| 4 | `<src><\|wait\|></src>` | `<src>진짜 보살 도요 </src>` | 485 |
| 5 | `<src>진짜 보살 도요. 아니 </src>` | `<src>아니 자기 가 </src>` | 1631 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src>` | `<src>보살 인데 꿈일 </src>` | 1683 |
| 7 | `<src>뭐 있고 </src>` | `<src>피라고 보이 고 </src>` | 2591 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src>` | `<src>나만 </src>` | 533 |
| 9 | `<src>뭐 있어요. 우주 가 </src>` | `<src>이 보살 로 보이 려고 </src>` | 1652 |
| 10 | `<src>지금 나한테 </src>` | `<src>보이 세 우주 가진다. 근데 보살 이란 </src>` | 3268 |
| 11 | `<src>보살 이라는데. </src>` | `<src><\|wait\|></src>` | 1778 |

---

### Test Example 20 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src>` | `<src>そうです。</src>` | 1880 |
| 2 | `<src>そこで</src>` | `<src>そこで</src>` | 875 |
| 3 | `<src><\|wait\|></src>` | `<src>天啓</src>` | 963 |
| 4 | `<src>テキという設備寺が</src>` | `<src>という設定が</src>` | 1159 |
| 5 | `<src>ありましたね。</src>` | `<src>ありましたね。</src>` | 492 |
| 6 | `<src>で、</src>` | `<src>で、</src>` | 1380 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1567 |
| 8 | `<src>長井慶義氏の仕組み</src>` | `<src>長井家氏の仕組み</src>` | 1235 |
| 9 | `<src><\|wait\|></src>` | `<src>は</src>` | 1744 |
| 10 | `<src>は五経、</src>` | `<src>五本、</src>` | 1380 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1913 |
| 12 | `<src>設備寺、五比</src>` | `<src>設定が五本</src>` | 1970 |
| 13 | `<src>です。</src>` | `<src>です。</src>` | 1887 |

---

### Test Example 21 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src>` | `<src><\|wait\|></src>` | 1751 |
| 2 | `<src><\|wait\|></src>` | `<src>让我回到</src>` | 1008 |
| 3 | `<src>回到我生活</src>` | `<src>我生活的一个</src>` | 867 |
| 4 | `<src>的一个轨道哈，</src>` | `<src>轨道哈，让我</src>` | 1137 |
| 5 | `<src>让我能够哈，</src>` | `<src>能够好好的</src>` | 1846 |
| 6 | `<src>在他下班的时候，</src>` | `<src>站在那边</src>` | 1452 |
| 7 | `<src>在做热汤</src>` | `<src>的时候，在座日</src>` | 489 |
| 8 | `<src>热饭给他吃。真的，</src>` | `<src>堂热闹的，所以</src>` | 2564 |
| 9 | `<src><\|wait\|></src>` | `<src>们我当时</src>` | 1374 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src>` | `<src>背对着我，</src>` | 1921 |
| 11 | `<src>小小的愿望</src>` | `<src>这么一个小小的小小的一个愿望哈，</src>` | 2024 |
| 12 | `<src>哈。</src>` | `<src><\|wait\|></src>` | 2024 |

---

### Test Example 22 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Like a stretched </src>` | 1844 |
| 2 | `<src>Like a stretched rubber band, </src>` | `<src>rubber band, </src>` | 1319 |
| 3 | `<src>chemical bonds </src>` | `<src>chemical bonds </src>` | 750 |
| 4 | `<src>also store energy, </src>` | `<src>also store energy. And when those </src>` | 1065 |
| 5 | `<src>and when those bonds are broken, </src>` | `<src>bonds are broken, </src>` | 1809 |
| 6 | `<src>that potential energy </src>` | `<src>that potential energy </src>` | 1655 |
| 7 | `<src>gets converted to </src>` | `<src>gets converted </src>` | 2511 |
| 8 | `<src>other types of energy, </src>` | `<src>to other types of energy, </src>` | 778 |
| 9 | `<src>like heat or light, </src>` | `<src>like heat or light. </src>` | 2201 |
| 10 | `<src><\|wait\|></src>` | `<src>Or </src>` | 2244 |
| 11 | `<src>or gets used to make </src>` | `<src>gets used to make </src>` | 1136 |
| 12 | `<src>different bonds. </src>` | `<src>different bonds. </src>` | 1685 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src>` | `<src>My name is </src>` | 1946 |
| 2 | `<src>Kerenath Dettig. </src>` | `<src>Chunawataru. </src>` | 1409 |
| 3 | `<src>I am currently </src>` | `<src>I am currently studying </src>` | 1036 |
| 4 | `<src><\|wait\|></src>` | `<src>in a business </src>` | 633 |
| 5 | `<src>studying a Bachelor of Finance </src>` | `<src>and finance </src>` | 1758 |
| 6 | `<src>and a Bachelor of Psychology </src>` | `<src>and a brother of psychology. </src>` | 1756 |
| 7 | `<src><\|wait\|></src>` | `<src>He </src>` | 2509 |
| 8 | `<src>here at the ANU, </src>` | `<src>here at Ian's </src>` | 746 |
| 9 | `<src><\|wait\|></src>` | `<src>and in the </src>` | 1980 |
| 10 | `<src>and in the future, I want to go into </src>` | `<src>future, I want to go into </src>` | 2606 |
| 11 | `<src><\|wait\|></src>` | `<src>corporate consultancy. </src>` | 1408 |
| 12 | `<src>corporate consultancy. </src>` | `<src><\|wait\|></src>` | 1684 |

---

### Test Example 24 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src>` | `<src>これが</src>` | 2141 |
| 2 | `<src>です。</src>` | `<src>ギアです。</src>` | 869 |
| 3 | `<src>ギアが</src>` | `<src>ギアが</src>` | 1003 |
| 4 | `<src>緩むと芯が</src>` | `<src>ユルむと、</src>` | 1187 |
| 5 | `<src><\|wait\|></src>` | `<src>信号が消えなくなってしまう</src>` | 1857 |
| 6 | `<src>上げ下げできなくなってしまうので、</src>` | `<src>ので、</src>` | 1574 |
| 7 | `<src>ギアの先に</src>` | `<src>ギアの先に</src>` | 1180 |
| 8 | `<src>役ねじの</src>` | `<src>逆ネジの</src>` | 1867 |
| 9 | `<src>ナットが</src>` | `<src>ナットが</src>` | 1417 |
| 10 | `<src>ついているっていうことです</src>` | `<src>付いているっていうこと</src>` | 2262 |
| 11 | `<src>ね。</src>` | `<src>ですね。</src>` | 1296 |
| 12 | `<src>はい、</src>` | `<src>はい、</src>` | 1410 |
| 13 | `<src>分解完了。</src>` | `<src>分解を</src>` | 1679 |

---

### Test Example 25 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src>` | `<src>第二个就是</src>` | 1902 |
| 2 | `<src><\|wait\|></src>` | `<src>进入到</src>` | 1048 |
| 3 | `<src>选择二级市场，哎，</src>` | `<src>二classList，</src>` | 870 |
| 4 | `<src>服务</src>` | `<src>并服务</src>` | 1085 |
| 5 | `<src>在一级一线</src>` | `<src>在一级一线</src>` | 1715 |
| 6 | `<src>拼杀的大牛们，</src>` | `<src>拼杀的大牛们。</src>` | 299 |
| 7 | `<src>比如说，呃，</src>` | `<src>比如说，</src>` | 1433 |
| 8 | `<src><\|wait\|></src>` | `<src>在做</src>` | 1056 |
| 9 | `<src>在做微信公众号十几年，你会</src>` | `<src>维信运动好事几年前，</src>` | 2176 |
| 10 | `<src>发现</src>` | `<src>你会发现</src>` | 1933 |
| 11 | `<src>给微信公众号评分</src>` | `<src>给维信运动和平分的</src>` | 2790 |
| 12 | `<src>的新榜反而</src>` | `<src>新棒</src>` | 1578 |
| 13 | `<src>火了。</src>` | `<src>反而活了。</src>` | 1727 |

---

### Test Example 26 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>要提醒大家，</src>` | 2102 |
| 2 | `<src>要提醒大家，</src>` | `<src>在这个</src>` | 874 |
| 3 | `<src>在这个罗马呢</src>` | `<src>罗马呢，</src>` | 920 |
| 4 | `<src>不是一天造成的，</src>` | `<src>不是意味着</src>` | 1139 |
| 5 | `<src>所以呢，</src>` | `<src>造成了，所以呢，</src>` | 1593 |
| 6 | `<src>你现在</src>` | `<src>你现在</src>` | 401 |
| 7 | `<src>所面临的一些</src>` | `<src>所面临的一些</src>` | 1463 |
| 8 | `<src>危机啊，跟风险</src>` | `<src>危机啊</src>` | 1181 |
| 9 | `<src>也不可能是</src>` | `<src>跟风险</src>` | 1786 |
| 10 | `<src>一夕之间就</src>` | `<src>也可能是</src>` | 1362 |
| 11 | `<src><\|wait\|></src>` | `<src>你事业即将</src>` | 1713 |
| 12 | `<src>演变出来的，</src>` | `<src>变坏的</src>` | 2073 |
| 13 | `<src>因此会建议</src>` | `<src>，因此会建议</src>` | 1547 |
| 14 | `<src>属鸡的朋友呢。</src>` | `<src>属鸡的朋友呢，</src>` | 1702 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>The meaning of </src>` | 2185 |
| 2 | `<src>The meaning of </src>` | `<src>the 19th </src>` | 1432 |
| 3 | `<src>the 19th Amendment, </src>` | `<src>Amendment </src>` | 635 |
| 4 | `<src>and to explore its </src>` | `<src>and to explore its </src>` | 1053 |
| 5 | `<src>history as a guide </src>` | `<src>history as a guide </src>` | 1792 |
| 6 | `<src>to how political </src>` | `<src>to how </src>` | 1502 |
| 7 | `<src><\|wait\|></src>` | `<src>political change </src>` | 1084 |
| 8 | `<src>change can happen </src>` | `<src>can happen </src>` | 1796 |
| 9 | `<src>in the United States. </src>` | `<src>in the United States. </src>` | 1606 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2142 |
| 11 | `<src>The meanings </src>` | `<src>The meanings of </src>` | 1569 |
| 12 | `<src>of the amendment, of course, are </src>` | `<src>the amendment, of course, </src>` | 1687 |
| 13 | `<src>myriad. </src>` | `<src>are Miriam. </src>` | 1505 |

---

### Test Example 28 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src>` | `<src>All right. </src>` | 2230 |
| 2 | `<src>and then </src>` | `<src>And then, </src>` | 1169 |
| 3 | `<src>after these examples, </src>` | `<src>after these examples, </src>` | 883 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1012 |
| 5 | `<src>the instruction </src>` | `<src>the instruction </src>` | 1781 |
| 6 | `<src>tells us to use </src>` | `<src>tells us to use </src>` | 1781 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2197 |
| 8 | `<src>actually </src>` | `<src>actually </src>` | 695 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1390 |
| 10 | `<src>these values. So </src>` | `<src>these values. </src>` | 2447 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1244 |
| 12 | `<src>this game dot scored array. </src>` | `<src>So this game.board </src>` | 1795 |
| 13 | `<src><\|wait\|></src>` | `<src>array. </src>` | 1677 |

---

### Test Example 29 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>바나듐이라는 </src>` | 1912 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src>` | `<src>얘르 거들은 </src>` | 1274 |
| 3 | `<src>인슐린과 </src>` | `<src>거진 유실 이 일어났 으려나 </src>` | 1659 |
| 4 | `<src>이제 거진 </src>` | `<src>또 </src>` | 1564 |
| 5 | `<src>유사 한 작용 이 </src>` | `<src>거진 유산 자형이 </src>` | 456 |
| 6 | `<src>일어날 정도 로 </src>` | `<src>나올 정도 로 굉장히 </src>` | 1578 |
| 7 | `<src>굉장히 아주 </src>` | `<src>아주 </src>` | 1586 |
| 8 | `<src>당뇨 미네랄이다 </src>` | `<src>당연 업 미네랄이다 </src>` | 1532 |
| 9 | `<src>이렇게 </src>` | `<src>이기적인 </src>` | 1634 |
| 10 | `<src>이야기 할 정도 의 </src>` | `<src>게일 자형에 </src>` | 2784 |
| 11 | `<src>이제 그런 거죠. 이제 </src>` | `<src>이제 그런 거죠. </src>` | 596 |
| 12 | `<src>그거 에다가 </src>` | `<src>이제 그 후에다가 </src>` | 2081 |
| 13 | `<src>아연. </src>` | `<src>아견. </src>` | 1453 |

---

### Test Example 30 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src>` | `<src>我当时</src>` | 1943 |
| 2 | `<src>一切正常，</src>` | `<src>已婚正常，</src>` | 1210 |
| 3 | `<src>活蹦乱跳，</src>` | `<src>我父母乱跳，</src>` | 1101 |
| 4 | `<src>所以</src>` | `<src>所以</src>` | 748 |
| 5 | `<src>坚持不开刀。</src>` | `<src>坚持不开档，</src>` | 1805 |
| 6 | `<src>期间</src>` | `<src>期限大概有</src>` | 1765 |
| 7 | `<src>大概有十位医生</src>` | `<src>十二个月</src>` | 2237 |
| 8 | `<src>来诊断，</src>` | `<src>这段，</src>` | 790 |
| 9 | `<src>一下敲腿，</src>` | `<src>以下敲腿</src>` | 2038 |
| 10 | `<src>一下提腿，</src>` | `<src>以下提腿，</src>` | 2660 |
| 11 | `<src>都没有问题。</src>` | `<src>都没有问题。</src>` | 953 |
| 12 | `<src>他们</src>` | `<src>他们都很</src>` | 1780 |
| 13 | `<src>都很疑惑的离开。</src>` | `<src>依乎我的离开。</src>` | 1447 |

---

### Test Example 31 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src>` | `<src>这一张的部分</src>` | 1800 |
| 2 | `<src>我们可以看到的是</src>` | `<src>我们看到的是</src>` | 1334 |
| 3 | `<src>一个在钓鱼</src>` | `<src>一个</src>` | 752 |
| 4 | `<src>的人，但是</src>` | `<src>在跳舞的人，但是</src>` | 1053 |
| 5 | `<src>它是属于逆向的，</src>` | `<src>它是属于逆向的，</src>` | 1835 |
| 6 | `<src>所以</src>` | `<src>所以</src>` | 1384 |
| 7 | `<src>通常逢到这样的一个状况的</src>` | `<src>同样的话，</src>` | 504 |
| 8 | `<src>时候，就要去</src>` | `<src>这样的一个状况</src>` | 2379 |
| 9 | `<src>特别注意，</src>` | `<src>需要去特别注意的是</src>` | 1309 |
| 10 | `<src>是它能不能够</src>` | `<src>他能不能</src>` | 1628 |
| 11 | `<src>钓到鱼，</src>` | `<src>能够得到</src>` | 2243 |
| 12 | `<src>它钓不到鱼</src>` | `<src>与他跳</src>` | 1178 |
| 13 | `<src><\|wait\|></src>` | `<src>不到与你的意识</src>` | 1769 |
| 14 | `<src>的意思哦。</src>` | `<src>哦。</src>` | 1154 |

---

### Test Example 32 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src>` | `<src>Well, or if you have </src>` | 2010 |
| 2 | `<src>have to produce </src>` | `<src>to produce </src>` | 987 |
| 3 | `<src>something written, </src>` | `<src>something written, </src>` | 862 |
| 4 | `<src>write a text, </src>` | `<src>write a text, </src>` | 1141 |
| 5 | `<src>you realize that </src>` | `<src>you realize that </src>` | 1796 |
| 6 | `<src>you don't even know how </src>` | `<src>you don't even know </src>` | 1761 |
| 7 | `<src>to spell </src>` | `<src>how to spell </src>` | 2596 |
| 8 | `<src>the words. Like, oh, </src>` | `<src>the word. </src>` | 1439 |
| 9 | `<src>is this word </src>` | `<src>Like, oh, is this word </src>` | 1846 |
| 10 | `<src>spelled with a double </src>` | `<src>started with </src>` | 1947 |
| 11 | `<src><\|wait\|></src>` | `<src>a double p, </src>` | 1544 |
| 12 | `<src>p, double lam? I don't </src>` | `<src>double l? I don't know. </src>` | 1942 |
| 13 | `<src>know. </src>` | `<src><\|wait\|></src>` | 988 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src>` | `<src>그중 에서 </src>` | 1782 |
| 2 | `<src>150만 개가 종업원 수 </src>` | `<src>백 오십만 개가 중화 볼 수 </src>` | 1786 |
| 3 | `<src>10명 미만 으로 </src>` | `<src>100명 미만 으로 </src>` | 1211 |
| 4 | `<src>아주 작은 기업 들이 </src>` | `<src>아주 작은 기업 들이 </src>` | 1823 |
| 5 | `<src>많았습니다. </src>` | `<src>많았습니다. </src>` | 799 |
| 6 | `<src>일반 적으로는 </src>` | `<src>일반 적으로는 </src>` | 1011 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src>` | `<src>작은 업체 들은 </src>` | 2596 |
| 8 | `<src>혹은 폐업 할 길을 </src>` | `<src>성장 하거나 혹은 </src>` | 1536 |
| 9 | `<src>걷게 되는데 </src>` | `<src>폐업 해 길게 되는데 </src>` | 2384 |
| 10 | `<src>일본 의 소기업들은 </src>` | `<src>이거 는 </src>` | 1442 |
| 11 | `<src>성장 도 폐업 도 </src>` | `<src>소기업 들은 </src>` | 1600 |
| 12 | `<src>하지 않는 현상 들을 </src>` | `<src>성장 도 폐업 도 하지 않는 </src>` | 1955 |
| 13 | `<src>보이 게 된 거죠. </src>` | `<src>현상 들을 보이 게 된 거죠. </src>` | 1335 |

---

### Test Example 34 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src>` | `<src>在财运方面，</src>` | 1948 |
| 2 | `<src>这个月财运可以说是</src>` | `<src>这个月财运可以说是</src>` | 1623 |
| 3 | `<src>很不错的，但是</src>` | `<src>还不错的，但是</src>` | 984 |
| 4 | `<src>比较偏向正财的部分，</src>` | `<src>比较偏正财</src>` | 488 |
| 5 | `<src>也就是</src>` | `<src>的部分。也就是</src>` | 1749 |
| 6 | `<src>在事业方面的</src>` | `<src>在事业方面</src>` | 1504 |
| 7 | `<src>业绩成长所带来的红利</src>` | `<src>的业绩增长</src>` | 515 |
| 8 | `<src>与收入的</src>` | `<src>所带来的荣誉</src>` | 2322 |
| 9 | `<src>提升。如果是在</src>` | `<src>与收入的提升。如果</src>` | 751 |
| 10 | `<src>投资理财方面呢，</src>` | `<src>在投资领域方面</src>` | 2115 |
| 11 | `<src>这个月</src>` | `<src>这个月</src>` | 2306 |
| 12 | `<src>也是不错，只是</src>` | `<src>也是不错的，只是</src>` | 1200 |
| 13 | `<src>相对正财来说就</src>` | `<src>相对整体来说，</src>` | 1735 |
| 14 | `<src>稍微弱了那么一点。</src>` | `<src>就稍微弱了</src>` | 1322 |
| 15 | `<src><\|wait\|></src>` | `<src>那么一点。</src>` | 995 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>砸到</src>` | 1728 |
| 2 | `<src>达到了一个甜头，那</src>` | `<src>一个铁头，</src>` | 1456 |
| 3 | `<src>如果你</src>` | `<src>那如果你</src>` | 730 |
| 4 | `<src>达到了甜头之后，</src>` | `<src>打到了铁头之后，</src>` | 967 |
| 5 | `<src>请你务必就要</src>` | `<src>请你务必</src>` | 1786 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1626 |
| 7 | `<src>先守住，</src>` | `<src>坐腰先守，</src>` | 2638 |
| 8 | `<src>不要想说，哎，那我再</src>` | `<src>不要想着哎，那我</src>` | 697 |
| 9 | `<src><\|wait\|></src>` | `<src>再继续操作</src>` | 1979 |
| 10 | `<src>继续操作下去哦。</src>` | `<src>下去哦。</src>` | 2477 |
| 11 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1136 |
| 12 | `<src>为什么会这么讲？</src>` | `<src>为什么会这么讲？</src>` | 1807 |
| 13 | `<src><\|wait\|></src>` | `<src>因为呢，</src>` | 1278 |
| 14 | `<src>因为呢。</src>` | `<src><\|wait\|></src>` | 1105 |

---

### Test Example 36 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src>` | `<src>Nothing new </src>` | 1927 |
| 2 | `<src>There were </src>` | `<src><\|wait\|></src>` | 1064 |
| 3 | `<src><\|wait\|></src>` | `<src>there. </src>` | 862 |
| 4 | `<src>such interfaces before, </src>` | `<src>Such instances before </src>` | 1101 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1744 |
| 6 | `<src>netfilter, TC. </src>` | `<src>net future TC </src>` | 247 |
| 7 | `<src>Yeah, so </src>` | `<src>here. </src>` | 1536 |
| 8 | `<src>this is just </src>` | `<src>So this is just </src>` | 2711 |
| 9 | `<src>one another place </src>` | `<src>one another place </src>` | 1043 |
| 10 | `<src>to look at. </src>` | `<src>to look at. </src>` | 1887 |
| 11 | `<src>But </src>` | `<src><\|wait\|></src>` | 2261 |
| 12 | `<src><\|wait\|></src>` | `<src>But </src>` | 1204 |
| 13 | `<src>developers or engineers </src>` | `<src>developers or engineers </src>` | 1800 |
| 14 | `<src>working on BugRepo </src>` | `<src>working on Bug Repositories </src>` | 1346 |
| 15 | `<src>should be aware of that. </src>` | `<src>should be aware of that. </src>` | 983 |

---

### Test Example 37 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src>` | `<src>That someone who </src>` | 2134 |
| 2 | `<src>just getting going </src>` | `<src>just getting going </src>` | 1308 |
| 3 | `<src>needs to get, </src>` | `<src>needs to get </src>` | 864 |
| 4 | `<src><\|wait\|></src>` | `<src>and </src>` | 853 |
| 5 | `<src>and I have ten of them </src>` | `<src>like ten of them </src>` | 1801 |
| 6 | `<src>that I think are </src>` | `<src>that are </src>` | 1596 |
| 7 | `<src>really important. </src>` | `<src>really important </src>` | 906 |
| 8 | `<src><\|wait\|></src>` | `<src>to </src>` | 1883 |
| 9 | `<src>I'm going to go into. </src>` | `<src>I'm going to go </src>` | 1479 |
| 10 | `<src>I have about </src>` | `<src>into I have about one </src>` | 1669 |
| 11 | `<src>one minute videos </src>` | `<src>minute videos </src>` | 2073 |
| 12 | `<src>that follow this video </src>` | `<src>at all for this video. </src>` | 1571 |
| 13 | `<src><\|wait\|></src>` | `<src>It'll cover each one. </src>` | 1898 |
| 14 | `<src>that cover each one </src>` | `<src>You know, </src>` | 1058 |
| 15 | `<src>in a little more detail, but. </src>` | `<src>a little more detail, </src>` | 1179 |

---

### Test Example 38 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src>어 </src>` | 2117 |
| 2 | `<src>어떻게 보면 </src>` | `<src>어디 를 보면 </src>` | 972 |
| 3 | `<src>가장 20대를 </src>` | `<src>가장 20대를 </src>` | 1157 |
| 4 | `<src><\|wait\|></src>` | `<src>함께 한 </src>` | 1021 |
| 5 | `<src>함께 한 동생 이자 </src>` | `<src>이 동생 이자 </src>` | 1848 |
| 6 | `<src>그래도 가족 </src>` | `<src>그렇 고 같은 </src>` | 1427 |
| 7 | `<src>같은 동생 이잖아 </src>` | `<src>동생 이잖아. </src>` | 605 |
| 8 | `<src>그러니까 </src>` | `<src>그러니까 </src>` | 2227 |
| 9 | `<src><\|wait\|></src>` | `<src>어 </src>` | 511 |
| 10 | `<src>책임감 보다는 </src>` | `<src>재생 한 거다는 </src>` | 1515 |
| 11 | `<src>조금 </src>` | `<src>조금 자기 스스로 </src>` | 2636 |
| 12 | `<src>자기 스스로 </src>` | `<src><\|wait\|></src>` | 796 |
| 13 | `<src><\|wait\|></src>` | `<src>좀 </src>` | 1737 |
| 14 | `<src>좀 많은 것을 </src>` | `<src>많은 거 </src>` | 1697 |
| 15 | `<src>내려놓 고 </src>` | `<src>내려 놓고 </src>` | 953 |
| 16 | `<src>행복 했으면 좋겠다. </src>` | `<src>생각 했습니다. </src>` | 1374 |

---

### Test Example 39 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>10 </src>` | 2015 |
| 2 | `<src>十一二手とか</src>` | `<src>12手とか</src>` | 1210 |
| 3 | `<src>じゃないですか。おそらく</src>` | `<src>でした。おそらく</src>` | 882 |
| 4 | `<src>十秒で。</src>` | `<src>10秒で</src>` | 1039 |
| 5 | `<src>まあ</src>` | `<src>まあ</src>` | 1720 |
| 6 | `<src>一秒に</src>` | `<src>1秒に</src>` | 628 |
| 7 | `<src>一定強ぐらいの</src>` | `<src>行って今日ぐらいの</src>` | 1180 |
| 8 | `<src>計算ですか</src>` | `<src>時間ですかね。</src>` | 2545 |
| 9 | `<src>ね。</src>` | `<src><\|wait\|></src>` | 704 |
| 10 | `<src>でなんか</src>` | `<src>でなんか</src>` | 1953 |
| 11 | `<src>おそらく</src>` | `<src>おそらく</src>` | 2389 |
| 12 | `<src><\|wait\|></src>` | `<src>11手</src>` | 879 |
| 13 | `<src>十一二手で</src>` | `<src>で</src>` | 1788 |
| 14 | `<src>あの</src>` | `<src>あの</src>` | 1421 |
| 15 | `<src>宮馬とかが</src>` | `<src>宮馬とかが</src>` | 1192 |
| 16 | `<src>あるから。</src>` | `<src>だから。</src>` | 1000 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src>` | `<src>너희 도 </src>` | 1871 |
| 2 | `<src>알거니와 너희 가 </src>` | `<src>알거니와 </src>` | 1283 |
| 3 | `<src>이방인으로 </src>` | `<src>여기 가 </src>` | 752 |
| 4 | `<src>있을 때에 </src>` | `<src>이방인 으로 있을 때에 </src>` | 1094 |
| 5 | `<src>말 못하 는 </src>` | `<src>말 못하 는 </src>` | 1755 |
| 6 | `<src>우상에게로 </src>` | `<src>우상 에게로 </src>` | 1507 |
| 7 | `<src>끄는 그대로 </src>` | `<src>그랬 는 그대로 </src>` | 1456 |
| 8 | `<src>끌려 갔느니라. </src>` | `<src>걸려 갔느니라. </src>` | 1783 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1625 |
| 10 | `<src>그러므로 내가 </src>` | `<src>그러므로 내가 </src>` | 2552 |
| 11 | `<src>너희 에게 </src>` | `<src>너희 에게 </src>` | 799 |
| 12 | `<src>알리 노니 </src>` | `<src>알리 노니 </src>` | 1967 |
| 13 | `<src>하나님 의 영으로 </src>` | `<src>하나님 의 영으로 </src>` | 1697 |
| 14 | `<src>말하는 자는. </src>` | `<src>말하는 자는 </src>` | 1182 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1049 |

---

### Test Example 41 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src>` | `<src>눈 감고 </src>` | 2246 |
| 2 | `<src><\|wait\|></src>` | `<src>새 영화 를 </src>` | 1031 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src>` | `<src>빌 거야. </src>` | 922 |
| 4 | `<src>니한테 소름 이 돋든 </src>` | `<src>옛날 서름이 </src>` | 1130 |
| 5 | `<src>닭살이 돋든 </src>` | `<src>돋든 자차 리 돋든 </src>` | 1883 |
| 6 | `<src>느낌 이 오면 </src>` | `<src>내 기분 이 너무야. </src>` | 1563 |
| 7 | `<src>이걸 흔들 어서 </src>` | `<src>이걸 </src>` | 1224 |
| 8 | `<src>같이 놀자는 거야. </src>` | `<src>한들어서 같이 놀자는 거야. </src>` | 1931 |
| 9 | `<src>귀신 이 오면 </src>` | `<src>기신이 너무 </src>` | 1592 |
| 10 | `<src>물릴 거고 </src>` | `<src>불릴 거고 </src>` | 2439 |
| 11 | `<src>신이 오면 </src>` | `<src>기신이 너무 </src>` | 908 |
| 12 | `<src>너 지켜 주라고 </src>` | `<src>지켜 주라고 </src>` | 1776 |
| 13 | `<src>찔러 줄 거니 까 </src>` | `<src>찔러 주다 보니까 </src>` | 1757 |
| 14 | `<src>편안 한 마음 에 </src>` | `<src>편안 한 마음 에 </src>` | 1305 |
| 15 | `<src>눈 감아. </src>` | `<src>눈 감음. </src>` | 1110 |

---

### Test Example 42 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src>` | `<src>들어 가면 </src>` | 2188 |
| 2 | `<src>엄청 헤맵니다. </src>` | `<src>엄청 헤맵니다. </src>` | 1346 |
| 3 | `<src>운전 을 </src>` | `<src>운전 을 </src>` | 839 |
| 4 | `<src><\|wait\|></src>` | `<src>하려고 </src>` | 871 |
| 5 | `<src>하건 걸어 걸어다니 </src>` | `<src>걸어 걸어다니 고 </src>` | 1913 |
| 6 | `<src>공간 에 뭐 </src>` | `<src>있거나 </src>` | 1396 |
| 7 | `<src>강북 을 가면 </src>` | `<src>뭐 강북 으로 가면 </src>` | 489 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src>` | `<src>말할 것도 없고 </src>` | 2390 |
| 9 | `<src><\|wait\|></src>` | `<src>외국 에 나가 면 또 장렬이에요. </src>` | 951 |
| 10 | `<src>또 장렬이에요. </src>` | `<src>좀 </src>` | 1782 |
| 11 | `<src>좀 창피 하네요. </src>` | `<src>신기 하네요. </src>` | 2461 |
| 12 | `<src>대신 에 </src>` | `<src>대신 에 이제 </src>` | 1353 |
| 13 | `<src>이제 </src>` | `<src>열심히 </src>` | 1672 |
| 14 | `<src>열심히 물어봐요. </src>` | `<src>모여 봐요. 그거 는 </src>` | 1458 |
| 15 | `<src>그거 는 다인 것 같아요. </src>` | `<src>잘한 것 같아요. </src>` | 1169 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 732 |

---

### Test Example 43 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src>` | `<src><\|wait\|></src>` | 1840 |
| 2 | `<src>HTML이라고 </src>` | `<src>H Tielmel </src>` | 1269 |
| 3 | `<src><\|wait\|></src>` | `<src>이라고 하는 </src>` | 751 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src>` | `<src>컴피 터도 </src>` | 1034 |
| 5 | `<src><\|wait\|></src>` | `<src>이해 할 수 있고 </src>` | 1848 |
| 6 | `<src>있고 사람 도 이해 할 수 </src>` | `<src>사람 도 </src>` | 1615 |
| 7 | `<src><\|wait\|></src>` | `<src>이해 할 수 있는 </src>` | 2641 |
| 8 | `<src>있는 컴퓨터 언어 의 </src>` | `<src>컴퓨터 언어 의 </src>` | 1548 |
| 9 | `<src>문법 에 </src>` | `<src>문법 의 </src>` | 1727 |
| 10 | `<src>맞게 우리 가 이제 </src>` | `<src>말 이렇게 우리 가 이제 </src>` | 2137 |
| 11 | `<src>코드 를 작성 해야 </src>` | `<src>조건 을 </src>` | 1571 |
| 12 | `<src>되는데 </src>` | `<src>작성해야 되는데 </src>` | 1726 |
| 13 | `<src>그 코드 를 작성 하는 </src>` | `<src>그 조건 을 </src>` | 1057 |
| 14 | `<src>프로그램 이 </src>` | `<src>작성 하는 프로그램 이 </src>` | 1302 |
| 15 | `<src>필요 합니다. </src>` | `<src>필요 합니다. </src>` | 537 |

---

### Test Example 44 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2097 |
| 2 | `<src>Educational attainment. </src>` | `<src>Educational attainment. How far </src>` | 1431 |
| 3 | `<src>How far did you </src>` | `<src>did you </src>` | 748 |
| 4 | `<src><\|wait\|></src>` | `<src>actually go </src>` | 894 |
| 5 | `<src>actually go in your education? Did you </src>` | `<src>in your education? </src>` | 1854 |
| 6 | `<src>graduate from high school? </src>` | `<src>Did you graduate from high school? </src>` | 1700 |
| 7 | `<src><\|wait\|></src>` | `<src>That's one level of </src>` | 2578 |
| 8 | `<src>That's one level of attainment. Did you go </src>` | `<src>attainment. </src>` | 1548 |
| 9 | `<src>to college, </src>` | `<src>Did you go to college? </src>` | 1927 |
| 10 | `<src>and if so, did you graduate? </src>` | `<src>And so, </src>` | 1860 |
| 11 | `<src>That's another level of </src>` | `<src>did you graduate? </src>` | 1443 |
| 12 | `<src>attainment. </src>` | `<src>That's another level of attainment. </src>` | 1811 |
| 13 | `<src>So that's it for </src>` | `<src>So that's it </src>` | 1174 |
| 14 | `<src>now. I'll see you </src>` | `<src>for now. </src>` | 1167 |
| 15 | `<src>online. </src>` | `<src>I'll see you online. </src>` | 725 |

---

### Test Example 45 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2006 |
| 2 | `<src>Activity than </src>` | `<src>Activity, then </src>` | 1163 |
| 3 | `<src>self-defining what we think </src>` | `<src>self-defining what we think </src>` | 1119 |
| 4 | `<src>the standard is because you're </src>` | `<src>the standard is, </src>` | 821 |
| 5 | `<src>absolutely correct, </src>` | `<src>because you're absolutely correct. </src>` | 1864 |
| 6 | `<src>but the reality </src>` | `<src><\|wait\|></src>` | 1449 |
| 7 | `<src>is is that </src>` | `<src>But the reality is that </src>` | 1348 |
| 8 | `<src>because we're the new kid on the </src>` | `<src>because we're the new cat </src>` | 1909 |
| 9 | `<src>block and because the </src>` | `<src>on the block, and because </src>` | 1766 |
| 10 | `<src>standards have </src>` | `<src>the standards have </src>` | 2526 |
| 11 | `<src>changed from 20 </src>` | `<src>changed from </src>` | 662 |
| 12 | `<src>years ago, </src>` | `<src>twenty years ago, </src>` | 1934 |
| 13 | `<src>we are being held to </src>` | `<src>we are being held to </src>` | 1676 |
| 14 | `<src>a higher standard because </src>` | `<src>higher standards </src>` | 1149 |
| 15 | `<src>everything at this point is being </src>` | `<src>because everything at this point </src>` | 1186 |
| 16 | `<src>held to a higher standard. </src>` | `<src>is being held to higher </src>` | 286 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src>` | `<src>계속 </src>` | 2119 |
| 2 | `<src>물론 이제 이런 경우 들도 </src>` | `<src>뭐 물론 이제 </src>` | 1328 |
| 3 | `<src>있습니다. </src>` | `<src>이런 경우 들 있습니다. 저희 가 </src>` | 1478 |
| 4 | `<src>저희 가 A라는 사람 과 </src>` | `<src>A라는 사람 과 </src>` | 376 |
| 5 | `<src>B라는 사람 이 서로 </src>` | `<src>B라는 사람 이 </src>` | 1736 |
| 6 | `<src>컨설턴트예요, </src>` | `<src>서로 컨설턴트 예요. </src>` | 1763 |
| 7 | `<src><\|wait\|></src>` | `<src>B가 컨설턴트 이 </src>` | 2294 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src>` | `<src>되고 A라는 </src>` | 721 |
| 9 | `<src>A라는 사람 이 </src>` | `<src>사람 이 </src>` | 1470 |
| 10 | `<src>어떤 악성 코드 를 </src>` | `<src>어떤 악성 코드 를 </src>` | 2832 |
| 11 | `<src>뿌렸 을 때 </src>` | `<src>주었을 때 </src>` | 687 |
| 12 | `<src>B라는 사람 이 </src>` | `<src>B라는 사람 이 </src>` | 1922 |
| 13 | `<src>실제 </src>` | `<src>실제 </src>` | 1575 |
| 14 | `<src>크로스사이트 스쿠티에서 </src>` | `<src>크로스 사이트 크리티 에서 </src>` | 1351 |
| 15 | `<src>EX 파일 까지 </src>` | `<src>X 사이 까지 </src>` | 1119 |
| 16 | `<src>감염 이 될까. </src>` | `<src>감염 이 될까. </src>` | 470 |

---

### Test Example 47 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src>` | `<src>だったらもう</src>` | 2148 |
| 2 | `<src>もう眠らせてやれ。</src>` | `<src>村せてやるね。</src>` | 1435 |
| 3 | `<src>俺は</src>` | `<src>俺は</src>` | 743 |
| 4 | `<src><\|wait\|></src>` | `<src>今、</src>` | 901 |
| 5 | `<src>今奇跡を見てる。</src>` | `<src>ひき手を見ている。</src>` | 1863 |
| 6 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1673 |
| 7 | `<src>もう限界なんか</src>` | `<src>もう限界なんか</src>` | 1896 |
| 8 | `<src><\|wait\|></src>` | `<src>超に超えている</src>` | 1132 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src>` | `<src>不烈火勢気よ。</src>` | 1834 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2643 |
| 11 | `<src>長年</src>` | `<src>長年</src>` | 636 |
| 12 | `<src>船大工をやってる</src>` | `<src>ふなでいくを</src>` | 2301 |
| 13 | `<src>が、</src>` | `<src>やってるんだ。</src>` | 1420 |
| 14 | `<src>俺は</src>` | `<src>俺はこんなにすごい</src>` | 1190 |
| 15 | `<src>こんなにすごい海賊船を</src>` | `<src>海賊線を</src>` | 1006 |
| 16 | `<src>見たことがない。</src>` | `<src>見たことがない。</src>` | 544 |

---

### Test Example 48 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src>` | `<src>주가 지수가 </src>` | 1922 |
| 2 | `<src><\|wait\|></src>` | `<src>이제 상승 하는 </src>` | 1291 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src>` | `<src>흐름 을 보인 다면 </src>` | 1422 |
| 4 | `<src>이런 대형주 도 </src>` | `<src>이런 대형 주도 </src>` | 515 |
| 5 | `<src>큰 폭의 </src>` | `<src><\|wait\|></src>` | 1633 |
| 6 | `<src>상승 을 하겠지만 </src>` | `<src>큰 폭의 상승 을 하겠지만 </src>` | 1768 |
| 7 | `<src>먼저 </src>` | `<src>먼저 </src>` | 2303 |
| 8 | `<src>이 가벼운 </src>` | `<src><\|wait\|></src>` | 731 |
| 9 | `<src>종목 들이 </src>` | `<src>이 가벼운 종목 들이 </src>` | 2157 |
| 10 | `<src>먼저 </src>` | `<src>먼저 시장 을 </src>` | 2543 |
| 11 | `<src>시장 을 주도 하면서 </src>` | `<src>주도 하면서 </src>` | 1180 |
| 12 | `<src>움직이 기 때문 에 항상 </src>` | `<src>움직이기 때문 에 </src>` | 1744 |
| 13 | `<src>요 시총이 </src>` | `<src>항상 요 시총이 </src>` | 1393 |
| 14 | `<src>가벼운 종목 을 </src>` | `<src>가벼운 종목 을 </src>` | 1026 |
| 15 | `<src>눈여겨 봐야 될 것 </src>` | `<src>눈여겨 봐야 </src>` | 1009 |
| 16 | `<src>같습니다. </src>` | `<src>될 것 같습니다. </src>` | 667 |

---

### Test Example 49 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src>` | `<src>그리고 이에 대 </src>` | 1757 |
| 2 | `<src>많은 사람 들이 분석 을 </src>` | `<src>많은 사람 들이 </src>` | 1404 |
| 3 | `<src>내놓 았습니다. </src>` | `<src>분석 을 해놨습니다. </src>` | 1356 |
| 4 | `<src>여기 로쿠자 의 </src>` | `<src>여기 </src>` | 328 |
| 5 | `<src>분석 을 보시면 </src>` | `<src>로쿠 자의 분석 을 보시면 </src>` | 1850 |
| 6 | `<src>소니가 </src>` | `<src>소니가 </src>` | 1451 |
| 7 | `<src>26비트 FP </src>` | `<src>이력 60, </src>` | 1199 |
| 8 | `<src>파이프 를 </src>` | `<src>FP 파이 프를 </src>` | 1992 |
| 9 | `<src>128비트로 낮춘 </src>` | `<src>128비 트로 </src>` | 2197 |
| 10 | `<src>것으로 보인다. </src>` | `<src>낮춘 것을 보입니다. </src>` | 2617 |
| 11 | `<src><\|wait\|></src>` | `<src>엑스 박스 </src>` | 1187 |
| 12 | `<src>Xbox Series X에서도 없는 </src>` | `<src>시리즈, X에서도 없는 </src>` | 1841 |
| 13 | `<src><\|wait\|></src>` | `<src>인피니트 캐시 </src>` | 1355 |
| 14 | `<src>인피니트 캐시 </src>` | `<src>C, S가 </src>` | 961 |
| 15 | `<src>L3가 여기 도 없다. </src>` | `<src>여기도 없다. </src>` | 1029 |
| 16 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 676 |

---

### Test Example 50 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src>` | `<src>でこれはですね、</src>` | 2117 |
| 2 | `<src>あのビジュアル開発環境</src>` | `<src>あのビジュアル開発環境</src>` | 1382 |
| 3 | `<src>というだけじゃなくて</src>` | `<src>っていうだけじゃなくて、</src>` | 1204 |
| 4 | `<src><\|wait\|></src>` | `<src>ビジュアルパイソン</src>` | 493 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src>` | `<src>開発環境なんですね。</src>` | 1771 |
| 6 | `<src>というのもフローリフを</src>` | `<src>というのも、</src>` | 1549 |
| 7 | `<src>ビジュアルに書いた後、</src>` | `<src>フローグラフのビジュアルの書いて</src>` | 1439 |
| 8 | `<src>それあいさつはPythonコード</src>` | `<src>後、とりあえずは</src>` | 1776 |
| 9 | `<src>にそこから</src>` | `<src>パイソンコード、そっから生成される</src>` | 2327 |
| 10 | `<src>生成されて、それが</src>` | `<src>やつ、それが実行される</src>` | 2454 |
| 11 | `<src>実行されることで</src>` | `<src>ということで信号処理</src>` | 1192 |
| 12 | `<src>信号処理が行われるという</src>` | `<src>が行われるっていう</src>` | 1814 |
| 13 | `<src>構造になっているからです。</src>` | `<src>ことをしている</src>` | 1200 |
| 14 | `<src><\|wait\|></src>` | `<src>からである。</src>` | 1008 |
| 15 | `<src>はい。</src>` | `<src><\|wait\|></src>` | 1065 |
| 16 | `<src>じゃあ。</src>` | `<src>はい。じゃあ、</src>` | 760 |

---

### Test Example 51 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src>` | `<src>For all of the </src>` | 1818 |
| 2 | `<src>首次觉知到</src>` | `<src>shortrices, </src>` | 1131 |
| 3 | `<src>那个现象：</src>` | `<src>we've just concluded </src>` | 994 |
| 4 | `<src>每当我们</src>` | `<src>that we </src>` | 902 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1830 |
| 6 | `<src>处于爱之中，</src>` | `<src>in our hearts </src>` | 1510 |
| 7 | `<src>所谓的爱，</src>` | `<src>love </src>` | 799 |
| 8 | `<src>我们也</src>` | `<src>is also </src>` | 2031 |
| 9 | `<src>同时进入恨。</src>` | `<src>the time to enter </src>` | 1462 |
| 10 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1589 |
| 11 | `<src>在早上的时候，</src>` | `<src>into a new stage </src>` | 2169 |
| 12 | `<src>它是爱；</src>` | `<src>of love. </src>` | 1159 |
| 13 | `<src>到了晚上，</src>` | `<src>Love has reached its peak. </src>` | 1926 |
| 14 | `<src>它就变成恨。</src>` | `<src>It has become </src>` | 1248 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 870 |
| 16 | `<src>那个钟摆</src>` | `<src>the most perfect. </src>` | 1023 |
| 17 | `<src><\|wait\|></src>` | `<src>It continues </src>` | 674 |
| 18 | `<src>继续在移动。</src>` | `<src>to evolve. </src>` | 328 |

---

### Test Example 52 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2091 |
| 2 | `<src>揣摩或感知对手</src>` | `<src>揣摩和感觉</src>` | 1171 |
| 3 | `<src>的感情或</src>` | `<src>对手的感情</src>` | 892 |
| 4 | `<src>真实意图的，</src>` | `<src>或真挚意图的。</src>` | 1069 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1750 |
| 6 | `<src><\|wait\|></src>` | `<src>很多是</src>` | 1661 |
| 7 | `<src>很多时候经常</src>` | `<src><\|wait\|></src>` | 2516 |
| 8 | `<src>会听到人们</src>` | `<src>后经常会听到人们这样说：“</src>` | 778 |
| 9 | `<src>这样说：“</src>` | `<src><\|wait\|></src>` | 1955 |
| 10 | `<src>你们看，</src>` | `<src>你们看，</src>` | 2519 |
| 11 | `<src>这个人</src>` | `<src>这个人</src>` | 968 |
| 12 | `<src>又在说谎了，</src>` | `<src>又在作谎了。”</src>` | 1987 |
| 13 | `<src>他的眼睛</src>` | `<src>他的眼睛</src>` | 1206 |
| 14 | `<src>已经说明了一切。”</src>` | `<src>已经说明了一切。</src>` | 1166 |
| 15 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1078 |
| 16 | `<src>也就是说。</src>` | `<src>也就是说，</src>` | 683 |
| 17 | `<src><\|wait\|></src>` | `<src>说。</src>` | 481 |

---

### Test Example 53 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src>` | `<src>I was a bit </src>` | 2293 |
| 2 | `<src>in turmoil </src>` | `<src>in turmoil </src>` | 1007 |
| 3 | `<src>in the first section </src>` | `<src>on the first section </src>` | 923 |
| 4 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1080 |
| 5 | `<src>about the EHR fields </src>` | `<src>about the EHR </src>` | 1788 |
| 6 | `<src><\|wait\|></src>` | `<src>field being of </src>` | 791 |
| 7 | `<src>being of critical importance </src>` | `<src>critical importance </src>` | 948 |
| 8 | `<src>versus variant </src>` | `<src>versus </src>` | 1315 |
| 9 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1728 |
| 10 | `<src>databases, </src>` | `<src>variant databases, </src>` | 1423 |
| 11 | `<src>which is obviously one of my loves. </src>` | `<src>which is obviously one of my loves. </src>` | 3069 |
| 12 | `<src><\|wait\|></src>` | `<src>Is that if </src>` | 553 |
| 13 | `<src>Is that if we don't agree </src>` | `<src>we don't agree </src>` | 1650 |
| 14 | `<src>upon the fields that need </src>` | `<src>upon the fields </src>` | 1763 |
| 15 | `<src>to be in these </src>` | `<src>that need to be in </src>` | 1043 |
| 16 | `<src>data sources that we can </src>` | `<src>these data sources </src>` | 1295 |
| 17 | `<src>draw from, </src>` | `<src>that we can draw from, </src>` | 442 |
| 18 | `<src>there's nothing to draw from, right? </src>` | `<src>there's nothing to draw from, right? </src>` | 771 |
| 19 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 420 |

---

### Test Example 54 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src>Um, </src>` | 1998 |
| 2 | `<src>Also, </src>` | `<src>also, </src>` | 943 |
| 3 | `<src>you will not be able to </src>` | `<src>you will not be able to move </src>` | 1255 |
| 4 | `<src>move media objects </src>` | `<src>media objects </src>` | 919 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1789 |
| 6 | `<src>between the resources. </src>` | `<src>between the resources </src>` | 1664 |
| 7 | `<src>So, if </src>` | `<src>though, </src>` | 1976 |
| 8 | `<src>you get into </src>` | `<src>if you get into </src>` | 1149 |
| 9 | `<src>a situation </src>` | `<src>a situation </src>` | 1788 |
| 10 | `<src>where you realize </src>` | `<src>where you realize </src>` | 2530 |
| 11 | `<src>you've added the wrong media </src>` | `<src>you've added the wrong </src>` | 736 |
| 12 | `<src>files to a particular resource, </src>` | `<src>media files </src>` | 2022 |
| 13 | `<src>you need to let us know, </src>` | `<src>to a particular resource, </src>` | 1687 |
| 14 | `<src>and we can see about </src>` | `<src>and we can see about </src>` | 1217 |
| 15 | `<src><\|wait\|></src>` | `<src>uploading those </src>` | 1068 |
| 16 | `<src>moving those media files and then making sure they </src>` | `<src>media files and then making sure </src>` | 710 |
| 17 | `<src>get backed up </src>` | `<src>they get backed up </src>` | 510 |
| 18 | `<src>properly. </src>` | `<src>properly. </src>` | 223 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src>` | `<src>And at one point </src>` | 1799 |
| 2 | `<src>he knows Jesus </src>` | `<src>in Noah's Genesis </src>` | 1505 |
| 3 | `<src>is hungry. </src>` | `<src>a hungry, </src>` | 742 |
| 4 | `<src>He knows that </src>` | `<src>in Noah's </src>` | 826 |
| 5 | `<src>he's been without food, </src>` | `<src>that he's been told that </src>` | 1864 |
| 6 | `<src><\|wait\|></src>` | `<src>forbids the wilderness </src>` | 1669 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src>` | `<src>spurtiday is hungry, </src>` | 2077 |
| 8 | `<src>And so he says </src>` | `<src>and so he says to </src>` | 963 |
| 9 | `<src>to Jesus," Hey, </src>` | `<src>Jesus, </src>` | 1500 |
| 10 | `<src>if you're the Son of God, prove it. </src>` | `<src>if you're the Son of God, prove it </src>` | 3217 |
| 11 | `<src><\|wait\|></src>` | `<src>by turn </src>` | 1575 |
| 12 | `<src>Turn these stones to bread." </src>` | `<src>these stones to bread. </src>` | 1802 |
| 13 | `<src><\|wait\|></src>` | `<src>How did </src>` | 1014 |
| 14 | `<src>How did Jesus deal with that </src>` | `<src>Jesus deal with that </src>` | 1052 |
| 15 | `<src>temptation? </src>` | `<src>temptation? </src>` | 945 |
| 16 | `<src><\|wait\|></src>` | `<src>Man </src>` | 681 |
| 17 | `<src>Man shall not live </src>` | `<src>Jonathan led by </src>` | 574 |
| 18 | `<src>by bread alone. </src>` | `<src>a brother alone. </src>` | 429 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 2242 |
| 2 | `<src>Meaningful individual </src>` | `<src>Meaningful, </src>` | 1054 |
| 3 | `<src>right, </src>` | `<src>individual right, </src>` | 921 |
| 4 | `<src>and the Supreme Court </src>` | `<src>and the Supreme Court </src>` | 1143 |
| 5 | `<src>came along </src>` | `<src>came along last, </src>` | 1793 |
| 6 | `<src>last, not leading. </src>` | `<src>not leading. And I don't know </src>` | 1653 |
| 7 | `<src>And I don't think the courts want to be </src>` | `<src>if the courts want to be </src>` | 1836 |
| 8 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1220 |
| 9 | `<src>the the vanguard of social </src>` | `<src>the the vanguard of </src>` | 1458 |
| 10 | `<src>change </src>` | `<src>social change. </src>` | 2410 |
| 11 | `<src>these days, </src>` | `<src>These days. </src>` | 1141 |
| 12 | `<src><\|wait\|></src>` | `<src>But they rather </src>` | 1798 |
| 13 | `<src>but they rather reflect </src>` | `<src>reflect </src>` | 1658 |
| 14 | `<src>the consensus </src>` | `<src>the consensus </src>` | 1071 |
| 15 | `<src><\|wait\|></src>` | `<src>that's already </src>` | 1353 |
| 16 | `<src>that's already emerged. </src>` | `<src>emerged. </src>` | 330 |
| 17 | `<src><\|wait\|></src>` | `<src>So. </src>` | 634 |
| 18 | `<src>So you have some </src>` | `<src>You have </src>` | 549 |
| 19 | `<src>federal judges </src>` | `<src>some federal judges </src>` | 307 |
| 20 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 216 |
| 21 | `<src>who. </src>` | `<src>who. </src>` | 403 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src>` | `<src>那我们看一下</src>` | 1994 |
| 2 | `<src>它的图片哦，</src>` | `<src>它的图片哦，</src>` | 1309 |
| 3 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 854 |
| 4 | `<src>图片的部分呢，我们可以看到</src>` | `<src>图片的部分呢，</src>` | 930 |
| 5 | `<src>的一个是客厅</src>` | `<src>我们可以看到的一个是</src>` | 1817 |
| 6 | `<src>的部分。</src>` | `<src>客厅的部分，</src>` | 1676 |
| 7 | `<src>那客厅一般</src>` | `<src>那客厅一般</src>` | 1803 |
| 8 | `<src>都是属于</src>` | `<src>都是</src>` | 1076 |
| 9 | `<src>我们</src>` | `<src>属于我们</src>` | 1322 |
| 10 | `<src>在休息的地方，</src>` | `<src>休息的地方，</src>` | 1993 |
| 11 | `<src><\|wait\|></src>` | `<src>所以呢，</src>` | 1828 |
| 12 | `<src>所以呢，这身体的部分</src>` | `<src>这是身体的部分</src>` | 1580 |
| 13 | `<src>也会反映的是</src>` | `<src>呢，会反映的是</src>` | 1703 |
| 14 | `<src>你需要给自己</src>` | `<src>你需要给自己</src>` | 974 |
| 15 | `<src>一点时间，</src>` | `<src>一点时间</src>` | 878 |
| 16 | `<src>可以好好的</src>` | `<src>可以好好的</src>` | 984 |
| 17 | `<src>坐下来休息。可是</src>` | `<src>坐下来休息，</src>` | 724 |
| 18 | `<src>我们可以看到这边是</src>` | `<src>可我们可以看到这边是</src>` | 575 |
| 19 | `<src>空无一人的嘛，</src>` | `<src>空无一人的吗？</src>` | 334 |
| 20 | `<src>啊，</src>` | `<src>好，</src>` | 180 |
| 21 | `<src>所以是说。</src>` | `<src>所以是说。</src>` | 397 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src>` | `<src>These people are </src>` | 1818 |
| 2 | `<src>completely rare, </src>` | `<src>completely rare, </src>` | 1316 |
| 3 | `<src>and they often </src>` | `<src>and they often </src>` | 861 |
| 4 | `<src>show up to </src>` | `<src>show up </src>` | 906 |
| 5 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1801 |
| 6 | `<src>completely revolutionize the world. </src>` | `<src>to completely revolutionize the world. </src>` | 1654 |
| 7 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 1356 |
| 8 | `<src>Their personality is </src>` | `<src>The personality is </src>` | 1736 |
| 9 | `<src>something of a </src>` | `<src>something of a contradiction. </src>` | 1562 |
| 10 | `<src>contradiction. </src>` | `<src><\|wait\|></src>` | 2422 |
| 11 | `<src>While they're </src>` | `<src>While they're </src>` | 1030 |
| 12 | `<src>extroverted, </src>` | `<src>extroverted, </src>` | 1929 |
| 13 | `<src>they also hate </src>` | `<src>they also hate </src>` | 1579 |
| 14 | `<src>meaningless conversations </src>` | `<src>meaningless conversations. </src>` | 1175 |
| 15 | `<src>and like to </src>` | `<src><\|wait\|></src>` | 1128 |
| 16 | `<src><\|wait\|></src>` | `<src>And like it </src>` | 373 |
| 17 | `<src>get straight to the point. </src>` | `<src>gets straight to the point. </src>` | 691 |
| 18 | `<src>They also love to </src>` | `<src>They also love </src>` | 524 |
| 19 | `<src>play </src>` | `<src>to play the devil's advocate </src>` | 464 |
| 20 | `<src>the devil's advocate, and they </src>` | `<src>and they </src>` | 431 |
| 21 | `<src><\|wait\|></src>` | `<src>never shy away </src>` | 201 |
| 22 | `<src>never shy away from a debate. </src>` | `<src>from a debate. </src>` | 187 |
| 23 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 252 |
| 24 | `<src><\|wait\|></src>` | `<src>E.T.P. stands for </src>` | 330 |
| 25 | `<src>ENTP stands for </src>` | `<src>for. </src>` | 267 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src>` | `<src>이전 의 이준석은 </src>` | 1909 |
| 2 | `<src>당무 를 거부 한 </src>` | `<src>강물 을 거부 한 </src>` | 1492 |
| 3 | `<src>명분 이 후보 를 </src>` | `<src>명분 이 후보 를 </src>` | 1198 |
| 4 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 418 |
| 5 | `<src>후보 의 당선 을 </src>` | `<src>후보 의 당선을 </src>` | 1776 |
| 6 | `<src>위해서 라면서 </src>` | `<src>위해서 라면서 </src>` | 1694 |
| 7 | `<src>제법 생색까지 </src>` | `<src>제법 생색까지 </src>` | 2558 |
| 8 | `<src>냈지만 이제 는 </src>` | `<src>냈지만 이제 는 </src>` | 691 |
| 9 | `<src>윤석열 후보 가 </src>` | `<src>윤석열 후보 가 </src>` | 2195 |
| 10 | `<src>김종인 을 </src>` | `<src>김종인 을 </src>` | 2370 |
| 11 | `<src>제거 한 순간 </src>` | `<src>제거 한 순간 </src>` | 1175 |
| 12 | `<src>이준석은 </src>` | `<src>이준석은 들은 해놓고. </src>` | 2082 |
| 13 | `<src><\|wait\|></src>` | `<src>윤석열 후보 </src>` | 1099 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src>` | `<src>를 떨어뜨리겠다는 </src>` | 945 |
| 15 | `<src><\|wait\|></src>` | `<src>듯기를 품은 </src>` | 1019 |
| 16 | `<src>독기를 품은 공격 성을 </src>` | `<src>공격 성을 </src>` | 716 |
| 17 | `<src><\|wait\|></src>` | `<src>보이 기로. </src>` | 571 |
| 18 | `<src>보이 기로 작정 한 </src>` | `<src>작정 한 </src>` | 424 |
| 19 | `<src>것입니다. </src>` | `<src>것입니다. </src>` | 301 |
| 20 | `<src><\|wait\|></src>` | `<src>가슴 발 </src>` | 267 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src>` | `<src>이준석의 성상 납권. </src>` | 300 |
| 22 | `<src><\|wait\|></src>` | `<src><\|wait\|></src>` | 225 |
| 23 | `<src>민주당 이 </src>` | `<src>민주당 이 </src>` | 286 |
| 24 | `<src><\|wait\|></src>` | `<src>공격 학이 얼마나 </src>` | 320 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src>` | `<src>큰 호재 입니까? </src>` | 307 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional transcriptionist. Transcribe what you hear.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src>` | `<src>まあ</src>` | 2054 |
| 2 | `<src>食堂ね</src>` | `<src>食堂ね今作って</src>` | 971 |
| 3 | `<src>今作ってる</src>` | `<src>見たいです。なので</src>` | 1048 |
| 4 | `<src>みたいですなのでここのね</src>` | `<src>ここで</src>` | 1050 |
| 5 | `<src>ゴールドストーンホテル</src>` | `<src>このホテル</src>` | 1605 |
| 6 | `<src>も</src>` | `<src>の朝食が</src>` | 380 |
| 7 | `<src>朝食が食べれる場所</src>` | `<src>食べれる場所</src>` | 1599 |
| 8 | `<src>になってる</src>` | `<src>になってる</src>` | 2036 |
| 9 | `<src>予定になってるので</src>` | `<src>予定になっている</src>` | 996 |
| 10 | `<src>今後ねここ</src>` | `<src>ので今後ね</src>` | 1702 |
| 11 | `<src>ゴールドストーンホテルを</src>` | `<src>ここゴルドストンホテル</src>` | 2799 |
| 12 | `<src>泊まってみたい</src>` | `<src>泊まってみたいな</src>` | 683 |
| 13 | `<src>なっていう方はですね</src>` | `<src>っていう方はですね</src>` | 2152 |
| 14 | `<src>検討なさってみて</src>` | `<src>検討なさ</src>` | 1498 |
| 15 | `<src>もまあいいんじゃないか</src>` | `<src>ても見てまあいいんじゃない</src>` | 1179 |
| 16 | `<src><\|wait\|></src>` | `<src>なと。はい。</src>` | 1067 |
| 17 | `<src>なとはい思いますここ</src>` | `<src>思います。ここ</src>` | 672 |
| 18 | `<src>のホテルからですね釜山</src>` | `<src>ホテルからですね</src>` | 508 |
| 19 | `<src>駅ももう</src>` | `<src>プサン駅も</src>` | 265 |
| 20 | `<src><\|wait\|></src>` | `<src>もう歩いて</src>` | 319 |
| 21 | `<src>歩いて一分</src>` | `<src>一本</src>` | 361 |
| 22 | `<src>かかるかかかんないかそんな</src>` | `<src>かかるかかかんないか</src>` | 254 |
| 23 | `<src>レベルのね</src>` | `<src>そんなレベルでのね</src>` | 219 |
| 24 | `<src>立地のいいねまあ</src>` | `<src>立地のいいねまあホテル</src>` | 284 |
| 25 | `<src>ホテルになってますので</src>` | `<src>になってますので</src>` | 287 |
| 26 | `<src>よかったらですね</src>` | `<src>よかったらですね</src>` | 311 |
| 27 | `<src>ご検討なさってみて</src>` | `<src>ご検討なさってみて</src>` | 298 |
| 28 | `<src>ください</src>` | `<src>ください。それでは</src>` | 151 |
| 29 | `<src>それではですね今回は。</src>` | `<src>ね今回は。</src>` | 138 |
