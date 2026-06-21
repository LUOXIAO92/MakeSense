# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9206
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5563
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 29
  - TARGET_METRICS_FILTERED_TURN_COUNT: 420
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 31
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 140
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 309
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1327.2850
  - PROCESS_TIME_MS_P50: 1280.0630
  - PROCESS_TIME_MS_P95: 2081.9200
  - PROCESS_TIME_MS_MAX: 3363.7530

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 800 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1103 |
| 3 | `<src>これなんかまだ</src><tgt>从一开始，尤其是这一棵</tgt>` | `<src>特に今まだ</src><tgt>从一开始，</tgt>` | 912 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>1年生ですからね。</src><tgt><\|wait\|></tgt>` | 1178 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 795 |
| 6 | `<src>こう短く</src><tgt>现在还只是一年生。在这个阶段</tgt>` | `<src>こう密告</src><tgt>特别是现在才一年级。在这个阶段，</tgt>` | 1758 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>選挙を</src><tgt><\|wait\|></tgt>` | 983 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>こう対数している</src><tgt><\|wait\|></tgt>` | 1729 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>如果能把剪枝持续做好的话，</tgt>` | `<src>と</src><tgt>如果把密告和选举对数化，</tgt>` | 834 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>1年経っても</src><tgt><\|wait\|></tgt>` | 1763 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>対数だ。</src><tgt><\|wait\|></tgt>` | 1291 |

---

### Test Example 2 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>乖的宠仔点，</src><tgt><\|wait\|></tgt>` | 1421 |
| 3 | `<src>边，这个油性也很大。</src><tgt>Add some pine nuts; they're quite oily.</tgt>` | `<src>这个友谊很大，</src><tgt>The sweet little darling, this friendship is so big,</tgt>` | 1516 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 831 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 1444 |
| 6 | `<src>呢，我再放一点</src><tgt>Then, I'll add</tgt>` | `<src>我在放假</src><tgt>and I'm on vacation</tgt>` | 1282 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>跟陶儿，</src><tgt><\|wait\|></tgt>` | 1504 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 872 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>some walnut kernels—</tgt>` | `<src>在礼迪</src><tgt>with Tao'er, at</tgt>` | 2138 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>的这种</src><tgt><\|wait\|></tgt>` | 1324 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>喝陶儿。</src><tgt><\|wait\|></tgt>` | 1843 |

---

### Test Example 3 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1121 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1325 |
| 3 | `<src><\|wait\|></src><tgt>What parents need to do is this:</tgt>` | `<src><\|wait\|></src><tgt>What parents need to do is</tgt>` | 1073 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | 1364 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>爱浇水，</src><tgt><\|wait\|></tgt>` | 1460 |
| 6 | `<src>施肥，</src><tgt>water and fertilize with our deep love,</tgt>` | `<src>施肥，</src><tgt>use our deep love to water and fertilize</tgt>` | 1340 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1644 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>给子孩子心里营养，</src><tgt><\|wait\|></tgt>` | 825 |
| 9 | `<src><\|wait\|></src><tgt>give children enough psychological nourishment,</tgt>` | `<src><\|wait\|></src><tgt>to nourish their children's hearts</tgt>` | 2196 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>给那孩子</src><tgt><\|wait\|></tgt>` | 1195 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | 1971 |

---

### Test Example 4 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1299 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>극성들은 </src><tgt><\|wait\|></tgt>` | 1190 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt>The people in the auspicious spots</tgt>` | 988 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 </src><tgt><\|wait\|></tgt>` | 1439 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>않았고 </src><tgt><\|wait\|></tgt>` | 1834 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위 로 뽑힌 </src><tgt>actually weren't that intelligent.</tgt>` | 1247 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>극성들이 </src><tgt><\|wait\|></tgt>` | 1677 |
| 8 | `<src>때문 입니다. </src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src>어떤 분입니다. </src><tgt><\|wait\|></tgt>` | 729 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>They were just randomly selected.</tgt>` | 1978 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 </src><tgt><\|wait\|></tgt>` | 1180 |
| 11 | `<src>교사 들은. </src><tgt>The teachers, who didn't know the truth...</tgt>` | `<src>몰랐 던 교수 하들은 </src><tgt><\|wait\|></tgt>` | 2075 |

---

### Test Example 5 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1076 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>淘沙玩一放，那</src><tgt><\|wait\|></tgt>` | 1453 |
| 3 | `<src>内部的压力减轻，</src><tgt>放出が終わると、内部の圧力が軽くなり、</tgt>` | `<src>内部的压力</src><tgt>砂を洗って遊んだ後、内部の圧力が</tgt>` | 1525 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也</src><tgt><\|wait\|></tgt>` | 747 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>衰弱了，然后</src><tgt><\|wait\|></tgt>` | 1807 |
| 6 | `<src>就停留在一个</src><tgt>エネルギーも弱まります。そして、</tgt>` | `<src>就停留在</src><tgt>弱まり、</tgt>` | 1017 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>一个相对的</src><tgt><\|wait\|></tgt>` | 1641 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>低能量的</src><tgt><\|wait\|></tgt>` | 867 |
| 9 | `<src>状态，</src><tgt>比較的低エネルギーの状態にとどまります。</tgt>` | `<src>运行状态。</src><tgt>比較的低エネルギーな運行状態に留まってしまいます。</tgt>` | 2448 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 910 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>逆流状态。</src><tgt><\|wait\|></tgt>` | 2004 |

---

### Test Example 6 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | 1083 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 884 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただいている</src><tgt>The T- shirts and other items you've received</tgt>` | 1229 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも用意しております</src><tgt><\|wait\|></tgt>` | 1193 |
| 5 | `<src>用意しておりますので</src><tgt>We have prepared things like T- shirts that you can get,</tgt>` | `<src>ので</src><tgt><\|wait\|></tgt>` | 666 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt>are also available, so please feel free to join us.</tgt>` | 2082 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 776 |
| 8 | `<src>以上になりまして、</src><tgt>so please be sure to join us. That's all for the announcements,</tgt>` | `<src>以上になります</src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src>えっと</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt>That concludes my message.</tgt>` | 779 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>ご不明な点が</src><tgt><\|wait\|></tgt>` | 1846 |
| 11 | `<src>ランチの案内がありますので</src><tgt>and we have some info about lunch,</tgt>` | `<src>ありましたら、</src><tgt><\|wait\|></tgt>` | 1365 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>お申し出ください。</src><tgt>If you have any questions, please let me know.</tgt>` | 2195 |

---

### Test Example 7 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1063 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>始めた</src><tgt>大致是从这一带</tgt>` | `<src><\|wait\|></src><tgt>通常从这里开始，</tgt>` | 943 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>始めたもので、</src><tgt><\|wait\|></tgt>` | 1198 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴホ</src><tgt><\|wait\|></tgt>` | 665 |
| 6 | `<src>ゴーギャン、</src><tgt>开始的，</tgt>` | `<src>ゴギョアン</src><tgt>就是这样开始的，</tgt>` | 1825 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1079 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>生産の</src><tgt><\|wait\|></tgt>` | 1611 |
| 9 | `<src>ルナールなど</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>生产</tgt>` | 620 |
| 10 | `<src>という人の絵</src><tgt>像梵高、高更、塞尚、雷诺阿他们的</tgt>` | `<src>ルナールなどという人の絵</src><tgt><\|wait\|></tgt>` | 2200 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1211 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>は田舎の中学生でも</src><tgt>卢纳尔（Lunal）等人的画，连乡村中学生</tgt>` | 2229 |

---

### Test Example 8 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=8 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 912 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src>Aptitude </src><tgt><\|wait\|></tgt>` | 1283 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>축발시키고 </src><tgt>I'm Aptitude, and I'm</tgt>` | 1482 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 942 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 1836 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>부모 를 죽인 </src><tgt>excommunicating those who killed their parents.</tgt>` | 1406 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>캐리나 </src><tgt><\|wait\|></tgt>` | 1694 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1878 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt>Park Han- sang</tgt>` | 1479 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1182 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>입니다. </src><tgt><\|wait\|></tgt>` | 1454 |

---

### Test Example 9 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 978 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔을 </src><tgt><\|wait\|></tgt>` | 1261 |
| 3 | `<src>해가지고 내가 </src><tgt>Someone asked me to kill them, so I</tgt>` | `<src>주게 달라 이거 주고 내가 </src><tgt>He gave me another glass,</tgt>` | 1006 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>주길 넣고 들어왔 수도다. </src><tgt><\|wait\|></tgt>` | 1471 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔쯤에 </src><tgt><\|wait\|></tgt>` | 1663 |
| 6 | `<src>죽여 달라 </src><tgt>came in here to do it.</tgt>` | `<src>주게 달라 </src><tgt>and I might have put it in and come back.</tgt>` | 1242 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>했잖아. 내가 </src><tgt><\|wait\|></tgt>` | 1702 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>큰 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 839 |
| 9 | `<src><\|wait\|></src><tgt>Didn't they ask you to kill them in the other room?</tgt>` | `<src>있는 줄 알아냈나. 내가 </src><tgt>I said I'd give it to another glass. Did I figure it out without hearing a word?</tgt>` | 3088 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1748 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>아, 내가 </src><tgt><\|wait\|></tgt>` | 648 |

---

### Test Example 10 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 </src><tgt><\|wait\|></tgt>` | 909 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1117 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt>これはすごく低俗なことかもしれないけど、</tgt>` | `<src>좋아요 하실 수 있지만 </src><tgt>これは、とても気に入っていただけるかもしれませんが、</tgt>` | 1241 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1419 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 자기 고 </src><tgt><\|wait\|></tgt>` | 1485 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt>本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんて</tgt>` | `<src>세렌드 꿈일 </src><tgt>本当に菩薩様が</tgt>` | 1287 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>피라고 보이 고 </src><tgt><\|wait\|></tgt>` | 1697 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 689 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>ある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보살 로 보이 려고 보이 세 우주 가 </src><tgt>見ているわけではなく、自分の菩薩様に見せようとしているだけです。宇宙が</tgt>` | 3364 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 이라는 </src><tgt><\|wait\|></tgt>` | 1669 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>거든요. </src><tgt><\|wait\|></tgt>` | 831 |

---

### Test Example 11 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1138 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1112 |
| 3 | `<src>is repeat. </src><tgt>最后，要重复。</tgt>` | `<src>is repeat. </src><tgt>最后，重复。</tgt>` | 910 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to dance, </src><tgt><\|wait\|></tgt>` | 1207 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>and repeat five times. If you're good at </src><tgt><\|wait\|></tgt>` | 1530 |
| 6 | `<src>and do more of it. </src><tgt>学会不断重复。找到你的长处，多做那些事。</tgt>` | `<src>it, do more of it </src><tgt>学会跳舞，重复五次。如果你跳得好，</tgt>` | 1744 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and repeat. And what you're not </src><tgt><\|wait\|></tgt>` | 1796 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>good at, </src><tgt><\|wait\|></tgt>` | 830 |
| 9 | `<src>get the people around you to help you with. </src><tgt>至于你的短处，找身边的人帮你。</tgt>` | `<src>get the people around you to help you with. </src><tgt>就多做几次。如果你跳得不好，就请周围的人来帮你。</tgt>` | 3079 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1200 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time, </src><tgt><\|wait\|></tgt>` | 1356 |

---

### Test Example 12 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>要气鼠是容易的，</src><tgt><\|wait\|></tgt>` | 1496 |
| 3 | `<src>但是</src><tgt>呼吸を数えるのは簡単ですが、</tgt>` | `<src><\|wait\|></src><tgt>鼠を追い払うのは簡単です。</tgt>` | 1117 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>但是只有一个</src><tgt><\|wait\|></tgt>` | 1081 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>师傅指导到</src><tgt><\|wait\|></tgt>` | 1841 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>しかし、</tgt>` | 1118 |
| 7 | `<src>处于中间，</src><tgt>中間に留まる方法を知っているのは師匠だけです。</tgt>` | `<src>如波出于终前，</src><tgt><\|wait\|></tgt>` | 1974 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1532 |
| 9 | `<src>虚阿凡</src><tgt><\|wait\|></tgt>` | `<src>需要反。</src><tgt>師匠の指導が波の出た終前までしかありません。ですから、反転させる必要があります。</tgt>` | 2055 |
| 10 | `<src>要成为</src><tgt>だからこそ、シュ・アファンは</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1328 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>要成为一个师傅，</src><tgt><\|wait\|></tgt>` | 1263 |

---

### Test Example 13 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1014 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，</src><tgt><\|wait\|></tgt>` | 1343 |
| 3 | `<src>遇到问题</src><tgt>In this situation, when we encounter a problem,</tgt>` | `<src>我们就是遇到问题</src><tgt>When faced with this situation,</tgt>` | 1028 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回答</src><tgt><\|wait\|></tgt>` | 1263 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>主管，或是通知对方</src><tgt><\|wait\|></tgt>` | 1685 |
| 6 | `<src>我们现有这个状况，</src><tgt>we should</tgt>` | `<src>我们笑这个状况，</src><tgt>we should quickly report it to our supervisor or notify the other party.</tgt>` | 1469 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1749 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>不要想自己什么</src><tgt><\|wait\|></tgt>` | 1875 |
| 9 | `<src>独立承担。</src><tgt>immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>都把它扛下来，</src><tgt>Don't think you have to handle everything yourself.</tgt>` | 1792 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>不离成本。整体而言，</src><tgt><\|wait\|></tgt>` | 2056 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>是应该做Solution。</src><tgt><\|wait\|></tgt>` | 489 |

---

### Test Example 14 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | 988 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>용신 이 </src><tgt><\|wait\|></tgt>` | 1222 |
| 3 | `<src><\|wait\|></src><tgt>I'm having</tgt>` | `<src><\|wait\|></src><tgt>Ah, I'm a Yongshin,</tgt>` | 1073 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>아 칼 용신이 </src><tgt><\|wait\|></tgt>` | 1403 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>그래서 우리 용신 이가 </src><tgt><\|wait\|></tgt>` | 1763 |
| 6 | `<src><\|wait\|></src><tgt>the ongsimi and kal- ongsimi—</tgt>` | `<src><\|wait\|></src><tgt>a Kal Yongshin. So, our Yongshin</tgt>` | 1234 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. 야 </src><tgt><\|wait\|></tgt>` | 1972 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1987 |
| 9 | `<src>진짜 이거 </src><tgt>it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>is mixed in. Wow, this is really</tgt>` | 1837 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해당 으로도 </src><tgt><\|wait\|></tgt>` | 2029 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금 주기 만 한 작업 </src><tgt><\|wait\|></tgt>` | 1282 |

---

### Test Example 15 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 871 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1184 |
| 3 | `<src>Drop into </src><tgt>你的身体在做什么？感受一下</tgt>` | `<src>doing? Drop into your body </src><tgt>你的身体在做什么？</tgt>` | 987 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1338 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>where does the tension </src><tgt><\|wait\|></tgt>` | 1471 |
| 6 | `<src>start? What is it? </src><tgt>你的身体。紧张感从哪里开始？是什么样的？</tgt>` | `<src>start? What is it? Is it a </src><tgt>进入你的身体，紧张感从哪里开始？是什么？</tgt>` | 1808 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>head? Is it a </src><tgt><\|wait\|></tgt>` | 1773 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>tension in your chest? </src><tgt><\|wait\|></tgt>` | 1885 |
| 9 | `<src>I ask them what </src><tgt>是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I ask the body </src><tgt>是头部的紧张吗？是胸部的紧张吗？</tgt>` | 1965 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>limb that you </src><tgt><\|wait\|></tgt>` | 1992 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>use. </src><tgt><\|wait\|></tgt>` | 1321 |

---

### Test Example 16 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 896 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1368 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>非常に重要な</tgt>` | 876 |
| 4 | `<src>on extremely happy people. </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。</tgt>` | `<src>on extremely happy people. This is </src><tgt><\|wait\|></tgt>` | 1466 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>tip of the stem </src><tgt><\|wait\|></tgt>` | 1551 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>research. Looking at </src><tgt>極めて幸せな人々に関する研究を行いました。これは、この研究の先端です。</tgt>` | 1673 |
| 7 | `<src>looking at the ten percent </src><tgt>これは最先端の研究です。</tgt>` | `<src>a 10% </src><tgt><\|wait\|></tgt>` | 1723 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1926 |
| 9 | `<src>of the happiest people </src><tgt><\|wait\|></tgt>` | `<src>of the happiest people </src><tgt>最も幸せな人々の10%を</tgt>` | 1845 |
| 10 | `<src>out there, </src><tgt>最も幸福な上位10％の人々に注目し、</tgt>` | `<src>out there, people who live </src><tgt><\|wait\|></tgt>` | 2057 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>we can learn from. </src><tgt><\|wait\|></tgt>` | 1374 |

---

### Test Example 17 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1351 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt>If a high school girl</tgt>` | 1183 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1080 |
| 5 | `<src>之间有着某种联系，</src><tgt>Was there some kind of connection between the high school girl and the odd- looking person?</tgt>` | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | 1858 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会是</src><tgt>has some connection with someone with a strange appearance, could it be</tgt>` | 1913 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1183 |
| 8 | `<src>从那天夜里开始的？</src><tgt>Could it have started that night?</tgt>` | `<src>从那天夜里</src><tgt><\|wait\|></tgt>` | 1724 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>开始的？</src><tgt>something that started that night?</tgt>` | 1269 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 857 |
| 11 | `<src>杨子思绪</src><tgt>Yang Zi's thoughts</tgt>` | `<src>杨子思疑</src><tgt><\|wait\|></tgt>` | 2021 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇。</src><tgt>Yang Zisi was suspicious from that night on.</tgt>` | 1498 |

---

### Test Example 18 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1124 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>だんだんちょっと距離が</src><tgt><\|wait\|></tgt>` | 968 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt>嗯，感觉距离会慢慢拉开，</tgt>` | `<src>離れてくるみたいな感じで</src><tgt>嗯，感觉距离在慢慢拉开，</tgt>` | 1354 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>おしゃれとか</src><tgt><\|wait\|></tgt>` | 1032 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>タタタが</src><tgt><\|wait\|></tgt>` | 972 |
| 6 | `<src>開業したい方って</src><tgt>确实很多人这么说。想创业的人</tgt>` | `<src>いっぱいでですね、海遊したい方って</src><tgt>像“时尚”或者“Tatatata”这种风格的人，</tgt>` | 2199 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい行き来行き来したが</src><tgt><\|wait\|></tgt>` | 1549 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>し、</src><tgt><\|wait\|></tgt>` | 880 |
| 9 | `<src>自分で</src><tgt>自我意识都很强，而且</tgt>` | `<src>行き来する</src><tgt>他们会非常频繁地来来回来，</tgt>` | 2436 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と友達と</src><tgt><\|wait\|></tgt>` | 1180 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>シャグ共々強いので。</src><tgt><\|wait\|></tgt>` | 2099 |
| 12 | `<src>なので。</src><tgt>倾向于自己全部投资，所以……</tgt>` | `<src>なので</src><tgt>和朋友们一起玩，所以</tgt>` | 1551 |

---

### Test Example 19 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 868 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>让我回到</src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>我生活的一个</src><tgt>제 삶의</tgt>` | 848 |
| 4 | `<src>的一个轨道哈，</src><tgt>제 삶의 궤도로</tgt>` | `<src>轨道哈，</src><tgt><\|wait\|></tgt>` | 1163 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够</src><tgt><\|wait\|></tgt>` | 811 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>好好的站它下面的时候，</src><tgt>궤도로 돌아가게 해 주세요. 제 삶의 궤도에 잘 서 있을 수 있도록</tgt>` | 2468 |
| 7 | `<src>在做热汤</src><tgt>돌아가고 싶어요. 그 사람이 퇴근했을 때</tgt>` | `<src>在做热棒</src><tgt><\|wait\|></tgt>` | 1563 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热棒的环节</src><tgt><\|wait\|></tgt>` | 828 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之中，</src><tgt>열 빵을 굽는 과정에서</tgt>` | 2113 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt>따뜻한 국과 밥을 차려줄 수 있도록요. 정말, 그때 너무 슬펐어요. 그저</tgt>` | `<src>我当时被掏出</src><tgt><\|wait\|></tgt>` | 1468 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>一个小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 2083 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>작은 소망 하나가 떠올랐어요.</tgt>` | 1779 |

---

### Test Example 20 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1246 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1277 |
| 3 | `<src>after these examples, </src><tgt>好的，然后在这些例子之后，</tgt>` | `<src>after these examples, </src><tgt>好的。然后，在这些例子之后，</tgt>` | 1333 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1073 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1275 |
| 6 | `<src>tells us to use </src><tgt>说明告诉我们</tgt>` | `<src>tells us to use </src><tgt>指令告诉我们</tgt>` | 1351 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1151 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1144 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>实际上</tgt>` | 1190 |
| 10 | `<src>these values. So </src><tgt>要使用这些值。也就是</tgt>` | `<src>these values. So, </src><tgt><\|wait\|></tgt>` | 1459 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1173 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot sort array </src><tgt>要使用这些值。所以，这个game.sort数组</tgt>` | 2236 |
| 13 | `<src><\|wait\|></src><tgt>这个game.scored数组。</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1809 |

---

### Test Example 21 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そう</src><tgt><\|wait\|></tgt>` | 895 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>です。そこで</src><tgt><\|wait\|></tgt>` | 1151 |
| 3 | `<src><\|wait\|></src><tgt>맞습니다. 거기</tgt>` | `<src>テイクという</src><tgt>그렇습니다. 거기서</tgt>` | 1101 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>ストレージが</src><tgt><\|wait\|></tgt>` | 1268 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>入りましたね。</src><tgt><\|wait\|></tgt>` | 841 |
| 6 | `<src>で、</src><tgt>' 테키' 라는 접미사가 있었죠.</tgt>` | `<src>で、</src><tgt>테이크라는 저장 장치가 들어왔네요. 그리고</tgt>` | 1514 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 962 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井氏の仕組み</src><tgt><\|wait\|></tgt>` | 1846 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>は</src><tgt>나가이 씨의 시스템은</tgt>` | 1884 |
| 10 | `<src>は五経、</src><tgt>파생 형용사의 구조는</tgt>` | `<src>ウォコン</src><tgt><\|wait\|></tgt>` | 1426 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1098 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>ストレージを</src><tgt>워콘 저장 장치를</tgt>` | 1638 |
| 13 | `<src>です。</src><tgt>어근, 접미사, 어미로 이루어져 있습니다.</tgt>` | `<src>使います。</src><tgt><\|wait\|></tgt>` | 1798 |

---

### Test Example 22 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1118 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>ギアです。</src><tgt><\|wait\|></tgt>` | 878 |
| 3 | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | `<src>ギアが</src><tgt>이것이 기어입니다. 기어가</tgt>` | 1176 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと、</src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>信号が消えて</src><tgt><\|wait\|></tgt>` | 916 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt>느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서</tgt>` | `<src>できなくなってしまうので、</src><tgt>느슨해지면 신호가 꺼져서</tgt>` | 1974 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 758 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1743 |
| 9 | `<src>ナットが</src><tgt>기어 끝에 역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>작동하지 않게 되기 때문에, 기어 끝에 역나사 너트가</tgt>` | 2037 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1612 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1171 |
| 12 | `<src>はい、</src><tgt>달려 있는 거죠. 네,</tgt>` | `<src><\|wait\|></src><tgt>달려 있다는 뜻입니다.</tgt>` | 1326 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイ分解完了。</src><tgt><\|wait\|></tgt>` | 1812 |

---

### Test Example 23 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kiran Patel, </src><tgt><\|wait\|></tgt>` | 1278 |
| 3 | `<src>I am currently </src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재</tgt>` | `<src>I am currently studying </src><tgt>제 이름은 키란 파텔입니다. 현재</tgt>` | 1479 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>in a business </src><tgt><\|wait\|></tgt>` | 951 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>finance and a </src><tgt><\|wait\|></tgt>` | 1689 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>batch of psychology </src><tgt>경영학과 심리학을</tgt>` | 1063 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1553 |
| 8 | `<src>here at the ANU, </src><tgt>호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src>here at Yale. </src><tgt><\|wait\|></tgt>` | 812 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And in the </src><tgt>Yale에서 공부하고 있습니다. 그리고</tgt>` | 2225 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>future, I want to go </src><tgt><\|wait\|></tgt>` | 1449 |
| 11 | `<src><\|wait\|></src><tgt>밟고 있고요, 앞으로는</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2060 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src>into corporate consultancy. </src><tgt>미래에는 기업 컨설팅 분야로 진출하고 싶습니다.</tgt>` | 1972 |

---

### Test Example 24 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 834 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>AAアンデスに</src><tgt><\|wait\|></tgt>` | 1154 |
| 3 | `<src>いろんな場面で</src><tgt>For the ' ei' (ray), in various situations,</tgt>` | `<src>世論の場面で</src><tgt>In the public sphere of the Andes,</tgt>` | 1191 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>AA制服かどうか</src><tgt><\|wait\|></tgt>` | 1351 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>の場面でいるときに</src><tgt><\|wait\|></tgt>` | 1454 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt>when checking whether they are inhabiting an area, you investigate their eggs.</tgt>` | `<src>AAの乱高下を</src><tgt>when they are in the role of the AA uniform,</tgt>` | 1590 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>調べて、あの</src><tgt><\|wait\|></tgt>` | 1702 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>そのAA制服かどうか</src><tgt><\|wait\|></tgt>` | 779 |
| 9 | `<src>保証する、生息である</src><tgt>This guarantees their presence—</tgt>` | `<src>を調べる</src><tgt>they investigate the fluctuations of the AA uniform— that is, whether they are actually wearing the AA uniform—</tgt>` | 2988 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>制服であることを保証する</src><tgt><\|wait\|></tgt>` | 1267 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような使い方を</src><tgt><\|wait\|></tgt>` | 1299 |
| 12 | `<src>使い方をされます。</src><tgt>it ensures they are indeed inhabiting the area.</tgt>` | `<src>されています。</src><tgt>and they use it to confirm that they are indeed wearing the uniform.</tgt>` | 1926 |

---

### Test Example 25 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 997 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 </src><tgt><\|wait\|></tgt>` | 1464 |
| 3 | `<src>인슐린과 </src><tgt>Things like vanadium</tgt>` | `<src>거진 인슐린과 </src><tgt>Vanadium and these things</tgt>` | 1057 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1064 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1960 |
| 6 | `<src>일어날 정도 로 </src><tgt>have an effect almost like insulin— to the point where</tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1180 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1743 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 897 |
| 9 | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | `<src>이렇게 </src><tgt><\|wait\|></tgt>` | 1409 |
| 10 | `<src>이야기 할 정도 의 </src><tgt>you could call them diabetes minerals.</tgt>` | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | 1477 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. </src><tgt>are so similar to insulin that they are called ' diabetes minerals '.</tgt>` | 2160 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>이제 그 후에다가 </src><tgt><\|wait\|></tgt>` | 1413 |
| 13 | `<src>아연. </src><tgt>And on top of that, there's zinc.</tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 800 |

---

### Test Example 26 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 970 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 947 |
| 3 | `<src>在这个罗马呢</src><tgt>皆さんに言っておきたいんですが、ローマは</tgt>` | `<src>在这个罗马呢，</src><tgt>皆さんに注意していただきたいのですが、このローマでは、</tgt>` | 1396 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | 1354 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 1286 |
| 6 | `<src>你现在</src><tgt>一日にして成らずと言いますよね。だから、今皆さんが</tgt>` | `<src><\|wait\|></src><tgt>一日にしてできたものではないので、</tgt>` | 1522 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>你现在所面临的一些</src><tgt><\|wait\|></tgt>` | 1443 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>危机啊</src><tgt><\|wait\|></tgt>` | 951 |
| 9 | `<src>也不可能是</src><tgt>直面している危機やリスクも、</tgt>` | `<src>跟风险，</src><tgt>今直面している危機やリスクは、</tgt>` | 2125 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你</src><tgt><\|wait\|></tgt>` | 1362 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>之前就眼见出来</src><tgt><\|wait\|></tgt>` | 1749 |
| 12 | `<src>演变出来的，</src><tgt>一朝一夕で生まれたわけじゃありません。</tgt>` | `<src><\|wait\|></src><tgt>以前に</tgt>` | 616 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的经济会见</src><tgt><\|wait\|></tgt>` | 1814 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>输出的朋友呢。</src><tgt><\|wait\|></tgt>` | 924 |

---

### Test Example 27 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1162 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1109 |
| 3 | `<src>the 19th Amendment, </src><tgt>수정헌법 제19조의 의미를</tgt>` | `<src>the 19th Amendment </src><tgt>19차 수정헌법의</tgt>` | 1187 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1364 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1452 |
| 6 | `<src>to how political </src><tgt>살펴보고, 그 역사를 탐구하는 것입니다. 이는</tgt>` | `<src>to how political </src><tgt>의미와 그 역사를 탐구해 보겠습니다. 정치적</tgt>` | 1580 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1712 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 718 |
| 9 | `<src>in the United States. </src><tgt>미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>변화가 미국에서 어떻게 일어날 수 있는지에 대한 지침서로서 말이죠.</tgt>` | 3040 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1057 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1455 |
| 12 | `<src>of the amendment, of course, are </src><tgt>이 수정헌법의 의미는 물론</tgt>` | `<src>the amendment, of course, </src><tgt>물론</tgt>` | 1862 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>I'm Mary. </src><tgt><\|wait\|></tgt>` | 1279 |

---

### Test Example 28 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 955 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1386 |
| 3 | `<src>chemical bonds </src><tgt>팽팽하게 당겨진 고무줄처럼</tgt>` | `<src>chemical bonds also store </src><tgt>고무줄처럼 화학 결합도</tgt>` | 1294 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 982 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1905 |
| 6 | `<src>that potential energy </src><tgt>화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는</tgt>` | `<src>that potential energy </src><tgt>에너지를 저장합니다. 그 결합이 끊어지면,</tgt>` | 1927 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1093 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 2028 |
| 9 | `<src>like heat or light, </src><tgt>열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light. </src><tgt>그 위치 에너지는 열이나 빛 같은 다른 에너지로 변환됩니다.</tgt>` | 1965 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1946 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>Or gets used to make </src><tgt><\|wait\|></tgt>` | 1852 |
| 12 | `<src>different bonds. </src><tgt>또는 새로운 결합을 만드는 데 사용됩니다.</tgt>` | `<src>different bonds. </src><tgt>또는 다른 결합을 만드는 데 사용됩니다.</tgt>` | 1335 |

---

### Test Example 29 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个</src><tgt><\|wait\|></tgt>` | 905 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1211 |
| 3 | `<src>选择二级市场，哎，</src><tgt>2つ目は、二次市場を選ぶことです。つまり、</tgt>` | `<src>就是进入二级市场，</src><tgt>2つ目は、</tgt>` | 1043 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1301 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>在一级一级线</src><tgt><\|wait\|></tgt>` | 1016 |
| 6 | `<src>拼杀的大牛们，</src><tgt>最前線で戦っている大物たちをサポートするのです。</tgt>` | `<src>喷射的大牛们，</src><tgt>二级市場への参入です。1階1階線で噴出した大牛たちです。</tgt>` | 1921 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1509 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 880 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>在做微信公众号几年的你会</src><tgt>例えば、WeChat公式アカウントを何年も運営していると、</tgt>` | 3067 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 986 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>发件给微信公众号投放的</src><tgt><\|wait\|></tgt>` | 1828 |
| 12 | `<src>的新榜反而</src><tgt>その評価を行う「新榜」の方が逆に</tgt>` | `<src>新绑粉丝</src><tgt>WeChat公式アカウントに送った</tgt>` | 1864 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>反薅完了。</src><tgt><\|wait\|></tgt>` | 1217 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you have </src><tgt><\|wait\|></tgt>` | 1078 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>to produce </src><tgt><\|wait\|></tgt>` | 1078 |
| 3 | `<src>something written, </src><tgt>それか、何か文章を書かなきゃいけないとき、</tgt>` | `<src>something written, </src><tgt>あるいは、何かを書き出す必要がある場合、</tgt>` | 1087 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1391 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1313 |
| 6 | `<src>you don't even know how </src><tgt>テキストを作るときに、</tgt>` | `<src>you don't even know </src><tgt>テキストを書く際に、</tgt>` | 1483 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>how to spell </src><tgt><\|wait\|></tgt>` | 1338 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, is </src><tgt><\|wait\|></tgt>` | 1058 |
| 9 | `<src>is this word </src><tgt>単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>this word </src><tgt>単語のスペルが全くわからないことに気づくかもしれません。「ああ、この単語は</tgt>` | 3050 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with </src><tgt><\|wait\|></tgt>` | 971 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>a double p, </src><tgt><\|wait\|></tgt>` | 1761 |
| 12 | `<src>p, double lam? I don't </src><tgt>pが二つ重なるんだっけ？lも二つ重なるんだっけ？って。自分でも</tgt>` | `<src>double lam. I don't know. </src><tgt>ダブルP、ダブルLで綴られているんだ。わからないな」</tgt>` | 1984 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1313 |

---

### Test Example 31 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>10</src><tgt><\|wait\|></tgt>` | 969 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>見てとか</src><tgt><\|wait\|></tgt>` | 976 |
| 3 | `<src>じゃないですか。おそらく</src><tgt>大概十一二手吧。</tgt>` | `<src>ですかとかを</src><tgt>比如“10”或者“看”之类的，</tgt>` | 1322 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく10秒</src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>でまあ</src><tgt><\|wait\|></tgt>` | 973 |
| 6 | `<src>一秒に</src><tgt>差不多十秒。</tgt>` | `<src>1秒に</src><tgt>大概是10秒，</tgt>` | 1137 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>言って今日ぐらいの</src><tgt><\|wait\|></tgt>` | 1165 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね</src><tgt><\|wait\|></tgt>` | 1792 |
| 9 | `<src>ね。</src><tgt>一秒一手多一点这样算。</tgt>` | `<src>と</src><tgt>也就是1秒，</tgt>` | 1421 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>いうなんか</src><tgt><\|wait\|></tgt>` | 917 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらく</src><tgt><\|wait\|></tgt>` | 1247 |
| 12 | `<src><\|wait\|></src><tgt>然后</tgt>` | `<src>12</src><tgt>大概是今天左右的时间吧，</tgt>` | 1551 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src>見てで</src><tgt><\|wait\|></tgt>` | 896 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 1634 |
| 15 | `<src>宮馬とかが</src><tgt>十一二手的时候，</tgt>` | `<src>見合うまとかが</src><tgt>比如“12”或者“看”之类的，</tgt>` | 893 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>から。</src><tgt><\|wait\|></tgt>` | 828 |

---

### Test Example 32 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1003 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>我当时已婚正常，</src><tgt><\|wait\|></tgt>` | 1417 |
| 3 | `<src>活蹦乱跳，</src><tgt>I was perfectly fine at the time, jumping around,</tgt>` | `<src>毫无妨乱跳。</src><tgt>I was already married and it was normal, no harm in jumping.</tgt>` | 1747 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 917 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不开刀，</src><tgt><\|wait\|></tgt>` | 1563 |
| 6 | `<src>期间</src><tgt>so I insisted on not having surgery.</tgt>` | `<src>切肩大概</src><tgt>So I insisted on not cutting it open.</tgt>` | 1395 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>有十万医生</src><tgt><\|wait\|></tgt>` | 1600 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来审断，</src><tgt><\|wait\|></tgt>` | 1897 |
| 9 | `<src>一下敲腿，</src><tgt>About ten doctors came to examine me during that period.</tgt>` | `<src>一刹敲腿，</src><tgt>About a million doctors came to examine the shoulder. With a single tap of the leg,</tgt>` | 2085 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>一刹抬腿，</src><tgt><\|wait\|></tgt>` | 1981 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | 1525 |
| 12 | `<src>他们</src><tgt>They would tap my leg, lift my leg— everything was fine.</tgt>` | `<src>他们都很</src><tgt>a single lift of the leg, there was no problem at all. They were all</tgt>` | 1140 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>询问的离开。</src><tgt><\|wait\|></tgt>` | 832 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 900 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150배가 종업원 수가 </src><tgt><\|wait\|></tgt>` | 1470 |
| 3 | `<src>10명 미만 으로 </src><tgt>そのうち150万社が、従業員数10人未満の</tgt>` | `<src>100만 미만 으로 </src><tgt>そのうち150倍の従業員数が100万未満に</tgt>` | 1677 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1200 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1211 |
| 6 | `<src>일반 적으로는 </src><tgt>非常に小さな企業でした。一般的に</tgt>` | `<src>일반 적으로는 </src><tgt>なっていた。つまり、非常に小さな企業が多かった。一般的に、</tgt>` | 2090 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 </src><tgt><\|wait\|></tgt>` | 1104 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>성장 하거나 혹은 </src><tgt><\|wait\|></tgt>` | 1939 |
| 9 | `<src>걷게 되는데 </src><tgt>小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>폐업 했을 것이라 그런데 </src><tgt>中小企業は成長するか、あるいは廃業したはずだ。しかし、</tgt>` | 1950 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>이번 에 소기업 들은 </src><tgt><\|wait\|></tgt>` | 1918 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1546 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt>日本の小企業は成長も廃業もしないという現象を</tgt>` | `<src>폐업 도 하지 않을 </src><tgt>今回中小企業は成長も廃業もせず、</tgt>` | 978 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들이 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1046 |

---

### Test Example 34 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 1051 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们看到的是</src><tgt><\|wait\|></tgt>` | 1181 |
| 3 | `<src>一个在钓鱼</src><tgt>이 부분에서는</tgt>` | `<src><\|wait\|></src><tgt>이 부분은</tgt>` | 888 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>一个戴雪的人，但是</src><tgt><\|wait\|></tgt>` | 1444 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1932 |
| 6 | `<src>所以</src><tgt>낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서</tgt>` | `<src><\|wait\|></src><tgt>눈을 가린 사람을 보여주는데, 이건 역방향입니다.</tgt>` | 2085 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>所以通场佛嘛，</src><tgt><\|wait\|></tgt>` | 1089 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>这样的一个状况</src><tgt><\|wait\|></tgt>` | 1915 |
| 9 | `<src>特别注意，</src><tgt>보통 이런 상황을 만나게 되면,</tgt>` | `<src>需要去特别注意的是</src><tgt>그래서 통장불의 경우, 이런 상황은 특별히 주의해야 합니다.</tgt>` | 1916 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>他能不能</src><tgt><\|wait\|></tgt>` | 1914 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>能够得到</src><tgt><\|wait\|></tgt>` | 1402 |
| 12 | `<src>它钓不到鱼</src><tgt>물고기를 잡을 수 있는지 없는지 특별히 주의해서 봐야 해요. 물고기를 잡지 못한다는</tgt>` | `<src>于他去掉</src><tgt>그가</tgt>` | 713 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>于这个</src><tgt><\|wait\|></tgt>` | 1234 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>意识了。</src><tgt><\|wait\|></tgt>` | 1061 |

---

### Test Example 35 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 874 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>达到了一个甜头，</src><tgt><\|wait\|></tgt>` | 1351 |
| 3 | `<src>如果你</src><tgt>うまくいったなと</tgt>` | `<src>那如果你</src><tgt>良い兆しが訪れました。もし</tgt>` | 1185 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1121 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1822 |
| 6 | `<src><\|wait\|></src><tgt>思ったらね。その時は必ず利益を</tgt>` | `<src><\|wait\|></src><tgt>良い兆しを得たなら、</tgt>` | 1239 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1777 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说：“哎，那我</src><tgt><\|wait\|></tgt>` | 1587 |
| 9 | `<src><\|wait\|></src><tgt>確保してください。</tgt>` | `<src>再继续操作</src><tgt>必ず守り抜いてください。そうして「まあ、</tgt>` | 1750 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦，</src><tgt><\|wait\|></tgt>` | 969 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1746 |
| 12 | `<src>为什么会这么讲？</src><tgt>「もっといけるはずだ」なんて思わないで。なぜそう言うかというと、</tgt>` | `<src>为什么会这么讲？”</src><tgt>そのあとで操作を続ける」なんて考えないでください。なぜそんな言い方をするのか？」</tgt>` | 2118 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1329 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | 1110 |

---

### Test Example 36 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1220 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src>needs to get, </src><tgt>それは始めたばかりの人が手に入れるべき</tgt>` | `<src>needs to get </src><tgt>今まさに動き出そうとしている人、</tgt>` | 1084 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1364 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1664 |
| 6 | `<src>that I think are </src><tgt>もので、私にとって</tgt>` | `<src>that you really </src><tgt>本当に</tgt>` | 991 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src>might want to </src><tgt><\|wait\|></tgt>` | 1001 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1375 |
| 9 | `<src>I'm going to go into. </src><tgt>本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>um I'm going to go </src><tgt>知っておくといいと思う10人います。えー、</tgt>` | 2531 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>ind here </src><tgt><\|wait\|></tgt>` | 1164 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>about one minute videos </src><tgt><\|wait\|></tgt>` | 1901 |
| 12 | `<src>that follow this video </src><tgt>この動画の後に、</tgt>` | `<src>that follow this video </src><tgt>この動画の後に</tgt>` | 580 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | 1884 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src>in a little more </src><tgt><\|wait\|></tgt>` | 1279 |
| 15 | `<src>in a little more detail, but. </src><tgt>それぞれをもう少し詳しく説明する約1分の動画があるんですけど、</tgt>` | `<src>detail, </src><tgt>1分程度の動画をいくつか紹介します。それぞれもう少し詳しく解説します。</tgt>` | 1225 |

---

### Test Example 37 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 944 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니화. </src><tgt><\|wait\|></tgt>` | 1351 |
| 3 | `<src>이방인으로 </src><tgt>あなたがたも知っているとおり、あなたがたが</tgt>` | `<src>너희 가 </src><tgt>あなたたちも知っているでしょう。あなたたちが</tgt>` | 1332 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>이방인 으로 있을 때에 </src><tgt><\|wait\|></tgt>` | 985 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1540 |
| 6 | `<src>우상에게로 </src><tgt>異邦人だった時、ものを言わない偶像に</tgt>` | `<src>말 못하 는 우선 에게로 </src><tgt>異邦人としている時に、話せない優先に</tgt>` | 1542 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1744 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>그는 그대로 </src><tgt><\|wait\|></tgt>` | 1341 |
| 9 | `<src><\|wait\|></src><tgt>引かれるままに連れて行かれました。</tgt>` | `<src>걸려 갔느니라. </src><tgt>そのまま取り残されてしまったのです。</tgt>` | 1893 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 </src><tgt><\|wait\|></tgt>` | 827 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>내가 너희 에게 </src><tgt><\|wait\|></tgt>` | 1950 |
| 12 | `<src>알리 노니 </src><tgt>ですから、あなたがたに教えます。</tgt>` | `<src>알리 노니 </src><tgt>ですから、私があなたたちに知らせるのです。</tgt>` | 1864 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 </src><tgt><\|wait\|></tgt>` | 831 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>영으로 말하는 자는 </src><tgt><\|wait\|></tgt>` | 907 |
| 15 | `<src><\|wait\|></src><tgt>神の霊によって語る者は、</tgt>` | `<src><\|wait\|></src><tgt>神の霊で語る者は、</tgt>` | 1128 |

---

### Test Example 38 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new, </src><tgt><\|wait\|></tgt>` | 1059 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1300 |
| 3 | `<src><\|wait\|></src><tgt>没什么新鲜的。</tgt>` | `<src>there are such </src><tgt>没什么新鲜事，</tgt>` | 971 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>instances before </src><tgt><\|wait\|></tgt>` | 1300 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1414 |
| 6 | `<src>netfilter, TC. </src><tgt>以前就有过这样的接口，比如netfilter和 TC。</tgt>` | `<src>netfilterTC, </src><tgt>netfilterTC这种实例以前就存在了，</tgt>` | 1491 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1648 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src>and so this is just </src><tgt><\|wait\|></tgt>` | 883 |
| 9 | `<src>one another place </src><tgt>所以这只是另一个</tgt>` | `<src>one another place </src><tgt>所以这只是</tgt>` | 1830 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>for a hook, </src><tgt><\|wait\|></tgt>` | 1432 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1894 |
| 12 | `<src><\|wait\|></src><tgt>需要关注的地方。但</tgt>` | `<src>but the </src><tgt>一个钩子的地方，但</tgt>` | 582 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 1863 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>who's working on Bugrep should be </src><tgt><\|wait\|></tgt>` | 1531 |
| 15 | `<src>should be aware of that. </src><tgt>开发人员或在BugRepo工作的工程师应该意识到这一点。</tgt>` | `<src>aware of that. </src><tgt>Bugrep的开发者或工程师应该知道这一点。</tgt>` | 1306 |

---

### Test Example 39 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1109 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 1081 |
| 3 | `<src>가장 20대를 </src><tgt>怎么说呢，</tgt>` | `<src>가장 20대를 </src><tgt>嗯，从某种意义上说，</tgt>` | 1226 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1334 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>이 동생 이자 </src><tgt><\|wait\|></tgt>` | 1158 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그렇 도 가족 </src><tgt>这个弟弟，他和我一起过了二十岁，也是</tgt>` | 1542 |
| 7 | `<src>같은 동생 이잖아 </src><tgt>他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。</tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1319 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1080 |
| 9 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt>家人一样的弟弟。所以，</tgt>` | 1943 |
| 10 | `<src>책임감 보다는 </src><tgt>所以比起责任感，</tgt>` | `<src>재생 감 보다는 </src><tgt><\|wait\|></tgt>` | 1566 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1200 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt>嗯，比起再生感，</tgt>` | 1353 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1839 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>좀 많은 거 </src><tgt><\|wait\|></tgt>` | 1241 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>잘 넣어 놓고 </src><tgt>我更想自己多加点，</tgt>` | 996 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt>我更希望他能自己放下一些包袱，过得幸福就好。</tgt>` | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | 736 |

---

### Test Example 40 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1052 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运</src><tgt><\|wait\|></tgt>` | 1327 |
| 3 | `<src>很不错的，但是</src><tgt>金運ですが、今月はかなり良いです。ただ、</tgt>` | `<src>可以说是还不多的，</src><tgt>金運については、今月はあまり良くないと言えるでしょう。</tgt>` | 1749 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src>但是比较稳定</src><tgt><\|wait\|></tgt>` | 820 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>的部分。</src><tgt><\|wait\|></tgt>` | 1280 |
| 6 | `<src>在事业方面的</src><tgt>どちらかというと本業の収入、つまり仕事の</tgt>` | `<src>也就是在事业方面的</src><tgt>ただ、安定している部分もあります。つまり、</tgt>` | 1332 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>业绩增长</src><tgt><\|wait\|></tgt>` | 1604 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>所带来的红利，</src><tgt><\|wait\|></tgt>` | 920 |
| 9 | `<src>提升。如果是在</src><tgt>業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>也就是提升。如果</src><tgt>仕事の業績向上による恩恵、つまり昇進です。もし</tgt>` | 2820 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>在投资理财方面，</src><tgt><\|wait\|></tgt>` | 1170 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月</src><tgt><\|wait\|></tgt>` | 1489 |
| 12 | `<src>也是不错，只是</src><tgt>投資や資産運用についても、悪くはないんですが、</tgt>` | `<src>也是不错的，</src><tgt>投資や資産運用に関しては、今月も良い</tgt>` | 1865 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>只是相对整体来说，</src><tgt><\|wait\|></tgt>` | 1270 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>就稍微弱了</src><tgt><\|wait\|></tgt>` | 526 |
| 15 | `<src><\|wait\|></src><tgt>本業の収入に比べると少し弱めですね。</tgt>` | `<src>那么一点。</src><tgt>と言えますが、全体としては少し弱めです。</tgt>` | 1256 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1062 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1149 |
| 3 | `<src>How far did you </src><tgt>교육 수준.</tgt>` | `<src>How far did you </src><tgt>학력. 당신은</tgt>` | 1104 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1177 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? </src><tgt><\|wait\|></tgt>` | 933 |
| 6 | `<src>graduate from high school? </src><tgt>실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요?</tgt>` | `<src>Did you graduate from high school? </src><tgt>실제로 학업을 얼마나 마쳤나요? 고등학교를 졸업했나요?</tgt>` | 2042 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 1316 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 995 |
| 9 | `<src>to college, </src><tgt>그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>Did you go to college? </src><tgt>그것은 학력의 한 단계입니다. 대학에 다녔나요?</tgt>` | 2853 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>And if so, did you </src><tgt><\|wait\|></tgt>` | 995 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>graduate? </src><tgt><\|wait\|></tgt>` | 2025 |
| 12 | `<src>attainment. </src><tgt>그렇다면 졸업하셨나요? 그게 또 다른 단계입니다.</tgt>` | `<src>That's another level of attainment. </src><tgt>만약 그렇다면, 졸업했나요? 그것은 또 다른 학력 단계입니다.</tgt>` | 2054 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1315 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 1172 |
| 15 | `<src>online. </src><tgt>그럼 오늘은 여기까지 하겠습니다. 온라인에서 뵙겠습니다.</tgt>` | `<src>online. </src><tgt>그게 전부입니다. 온라인에서 뵙겠습니다.</tgt>` | 885 |

---

### Test Example 42 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったら</src><tgt><\|wait\|></tgt>` | 1069 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>もう寝かせているね。</src><tgt><\|wait\|></tgt>` | 1158 |
| 3 | `<src>俺は</src><tgt>그럼 이제 잠들게 해줘. 난</tgt>` | `<src>俺は</src><tgt>그럼 이미 잠들었겠지. 나는</tgt>` | 1177 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>今</src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>血記事を見ている。</src><tgt><\|wait\|></tgt>` | 1242 |
| 6 | `<src><\|wait\|></src><tgt>지금 기적을 보고 있어.</tgt>` | `<src><\|wait\|></src><tgt>지금 혈기( 血記事) 를 보고 있어.</tgt>` | 1558 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1331 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>超に超えている</src><tgt><\|wait\|></tgt>` | 1069 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>不烈記事を</src><tgt>이제 한계는 아득히 초월한 불렬기( 不烈記事) 를</tgt>` | 3098 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 909 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1780 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>ふなでいくを</src><tgt>오래도록</tgt>` | 1599 |
| 13 | `<src>が、</src><tgt>오랫동안 배를 만들어왔지만,</tgt>` | `<src>やっているんだ。</src><tgt><\|wait\|></tgt>` | 542 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺はこんなにすごい</src><tgt><\|wait\|></tgt>` | 1389 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>海賊船を見た</src><tgt>나아가는 중이야. 나는 이렇게 대단한 해적선을</tgt>` | 1500 |
| 16 | `<src>見たことがない。</src><tgt>이렇게 대단한 해적선은 처음 봤다.</tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 524 |

---

### Test Example 43 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | 1135 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1175 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt>If the stock index shows an upward trend,</tgt>` | `<src>상승 하는 흐름 을 보인 다면 </src><tgt>If the stock index is showing an upward trend,</tgt>` | 1805 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이러 면 대형 주도 </src><tgt><\|wait\|></tgt>` | 1345 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1119 |
| 6 | `<src>상승 을 하겠지만 </src><tgt>these large- cap stocks will see significant gains.</tgt>` | `<src>또 큰 폭의 상승 을 </src><tgt>it suggests that large- cap stocks</tgt>` | 1501 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>하겠지만 </src><tgt><\|wait\|></tgt>` | 1456 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt><\|wait\|></tgt>` | 1553 |
| 9 | `<src>종목 들이 </src><tgt><\|wait\|></tgt>` | `<src>종목 들이 </src><tgt>will also rise sharply. However, it's</tgt>` | 1720 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 시장 을 </src><tgt><\|wait\|></tgt>` | 980 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>주도 하면서 움직이 기 </src><tgt><\|wait\|></tgt>` | 1801 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt>But since lighter stocks tend to lead the market first,</tgt>` | `<src>때문 에 </src><tgt>driven by lighter stocks leading the market first,</tgt>` | 1879 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 리 초의 </src><tgt><\|wait\|></tgt>` | 1285 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 1031 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨 봐야 </src><tgt>you should always keep an eye on those lighter stocks</tgt>` | 909 |
| 16 | `<src>같습니다. </src><tgt>I think we should always keep an eye on those small- cap names.</tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 409 |

---

### Test Example 44 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=6 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1015 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity, then self </src><tgt><\|wait\|></tgt>` | 1268 |
| 3 | `<src>self-defining what we think </src><tgt>私たちが何が</tgt>` | `<src>defining what we think </src><tgt>活動、そして</tgt>` | 938 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, </src><tgt><\|wait\|></tgt>` | 1181 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>because you're absolutely correct </src><tgt><\|wait\|></tgt>` | 1139 |
| 6 | `<src>but the reality </src><tgt>基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src><\|wait\|></src><tgt>自分自身で基準を定義することです。なぜなら、</tgt>` | 1543 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>but the reality is that </src><tgt><\|wait\|></tgt>` | 853 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on </src><tgt><\|wait\|></tgt>` | 1763 |
| 9 | `<src>block and because the </src><tgt><\|wait\|></tgt>` | `<src>the block, and because </src><tgt>あなたは完全に正しい。しかし、現実は、私たちが新しい子だからです。そして、</tgt>` | 3079 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>the standards have </src><tgt><\|wait\|></tgt>` | 766 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from </src><tgt><\|wait\|></tgt>` | 1992 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>twenty years ago, </src><tgt>20年前に基準が変わってから、</tgt>` | 1678 |
| 13 | `<src>we are being held to </src><tgt>私たちは新参者であり、20年前と基準が変わっているため、</tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 633 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard </src><tgt><\|wait\|></tgt>` | 1254 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>because everything at this point </src><tgt>私たちはより高い基準を求められている。なぜなら、今の状況では、</tgt>` | 1312 |
| 16 | `<src>held to a higher standard. </src><tgt>より高い基準を求められています。なぜなら、今はすべてがより高い基準を求められているからです。</tgt>` | `<src>is being held to higher </src><tgt><\|wait\|></tgt>` | 778 |

---

### Test Example 45 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 920 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src>어 H 1개월 </src><tgt><\|wait\|></tgt>` | 1372 |
| 3 | `<src><\|wait\|></src><tgt>HTML</tgt>` | `<src><\|wait\|></src><tgt>嗯，</tgt>` | 810 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src>이라고 하는 컴퓨터 도 </src><tgt><\|wait\|></tgt>` | 1414 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1870 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt>是一种</tgt>` | `<src>사람 도 </src><tgt>计算机也理解为H1个月，</tgt>` | 1230 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1838 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | 2033 |
| 9 | `<src>문법 에 </src><tgt>计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src><\|wait\|></src><tgt>人类也理解为计算机语言，</tgt>` | 1717 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>문법 이 맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 2109 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 </src><tgt><\|wait\|></tgt>` | 1156 |
| 12 | `<src>되는데 </src><tgt>我们需要按照它的语法来编写代码，而</tgt>` | `<src>작성 해야 되는데 </src><tgt>语法也正确。我们现在需要编写代码，</tgt>` | 1450 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1015 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1132 |
| 15 | `<src>필요 합니다. </src><tgt>编写代码就需要专门的程序。</tgt>` | `<src>필요 합니다. </src><tgt>需要一个程序来编写这些代码。</tgt>` | 938 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1056 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 937 |
| 3 | `<src>있습니다. </src><tgt>もちろん、こうしたケースもあります。</tgt>` | `<src>이런 경우 들이 있습니다. 저희 가 </src><tgt>ですから、もちろんこういうケースもあります。私たちが</tgt>` | 1406 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 </src><tgt><\|wait\|></tgt>` | 1352 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | 1365 |
| 6 | `<src>컨설턴트예요, </src><tgt>AさんとBさんはお互いに</tgt>` | `<src>서로 컨설턴트 예요. </src><tgt>AさんとBさんがコンサルタントで、お互いに</tgt>` | 1911 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>뭐 이렇게 </src><tgt><\|wait\|></tgt>` | 1692 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>컨설턴트 여야 되고 </src><tgt><\|wait\|></tgt>` | 1693 |
| 9 | `<src>A라는 사람 이 </src><tgt>模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>コンサルタントで、Aさんが</tgt>` | 1594 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1010 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>줬을 때 </src><tgt><\|wait\|></tgt>` | 1722 |
| 12 | `<src>B라는 사람 이 </src><tgt>何らかの悪性コードを配布したとします。その場合、Bさんは</tgt>` | `<src>B라는 사람 이 </src><tgt>悪意のあるコードを渡したときに、Bさんが</tgt>` | 2013 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 </src><tgt><\|wait\|></tgt>` | 1251 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>크로스 사이트 크리티 에서 </src><tgt><\|wait\|></tgt>` | 1082 |
| 15 | `<src>EX 파일 까지 </src><tgt>実際のクロスサイトスクリプティングからEXEファイルまで</tgt>` | `<src>예기할 사이 까지 </src><tgt>実際にクロスサイトクリティカルを</tgt>` | 746 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 529 |

---

### Test Example 47 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1162 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>색인 번호 를 </src><tgt><\|wait\|></tgt>` | 1157 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt>目を閉じて。私が祈るから。</tgt>` | `<src>빌 거야. </src><tgt>目を閉じて、色番号を</tgt>` | 1138 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>이제 서름이 돋든 </src><tgt><\|wait\|></tgt>` | 1386 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>가짜 이 돋든 </src><tgt><\|wait\|></tgt>` | 1285 |
| 6 | `<src>느낌 이 오면 </src><tgt>鳥肌が立ったり何かを感じたりしたら、</tgt>` | `<src>느낌 이 오면 </src><tgt>選ぶんだ。今、鳥肌が立ったり、偽物が立ったりする感じがしたら、</tgt>` | 2174 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1630 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1791 |
| 9 | `<src>귀신 이 오면 </src><tgt>これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>귀신 이 </src><tgt>それを振って一緒に遊ぼうってこと。</tgt>` | 1525 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>너무 많이 </src><tgt><\|wait\|></tgt>` | 1054 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>풀릴 거고, 시시니하면 </src><tgt><\|wait\|></tgt>` | 1767 |
| 12 | `<src>너 지켜 주라고 </src><tgt>噛みつかれるし、神様が来たら守ってくれるように</tgt>` | `<src>너 지켜 주라고 </src><tgt>お化けが多すぎて、</tgt>` | 1902 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주라고 그러니까 </src><tgt><\|wait\|></tgt>` | 1377 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 1102 |
| 15 | `<src>눈 감아. </src><tgt>突いてくれるから、安心して目を閉じて。</tgt>` | `<src>눈 감아. </src><tgt>「お前を守れ」って刺してくれって言ってるから、リラックスして目を閉じて。</tgt>` | 1441 |

---

### Test Example 48 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=7 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1182 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1328 |
| 3 | `<src>というだけじゃなくて</src><tgt>This isn't just a visual development environment;</tgt>` | `<src>っていう出じゃなくて、</src><tgt>So, this isn't a visual development environment,</tgt>` | 1560 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 745 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1919 |
| 6 | `<src>というのもフローリフを</src><tgt>it's a visual Python development environment.</tgt>` | `<src>というのも、</src><tgt>but a Visual Python development environment.</tgt>` | 1269 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>フローグラフのビジュアルの書いて</src><tgt><\|wait\|></tgt>` | 1755 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>後、それは</src><tgt><\|wait\|></tgt>` | 1870 |
| 9 | `<src>にそこから</src><tgt><\|wait\|></tgt>` | `<src>Pythonコード、</src><tgt>That's because you write the visual flow graph, and then it generates</tgt>` | 1977 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>そっから生成されるっていう、それが</src><tgt><\|wait\|></tgt>` | 2112 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで信号処理</src><tgt><\|wait\|></tgt>` | 1800 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>が行われるっていう</src><tgt>Python code from it, which is then executed to perform signal processing.</tgt>` | 875 |
| 13 | `<src>構造になっているからです。</src><tgt>That's because after you visually create a flowchart, Python code is generated from it, and that code is then executed to perform signal processing. So that's the structure.</tgt>` | `<src>機能になっているから</src><tgt><\|wait\|></tgt>` | 779 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>です。</src><tgt><\|wait\|></tgt>` | 1034 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>That's why it's called</tgt>` | 954 |
| 16 | `<src>じゃあ。</src><tgt>Alright, then.</tgt>` | `<src>はい。じゃあ、</src><tgt><\|wait\|></tgt>` | 750 |

---

### Test Example 49 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1094 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩和感觉</src><tgt><\|wait\|></tgt>` | 1268 |
| 3 | `<src>的感情或</src><tgt>相手の感情や</tgt>` | `<src>对手的感情</src><tgt>相手の感情を</tgt>` | 995 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>或真挚意图的，</src><tgt><\|wait\|></tgt>` | 1476 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1805 |
| 6 | `<src><\|wait\|></src><tgt>本当の意図を察したり推し量ったり</tgt>` | `<src>很多是</src><tgt>推し量ったり感じ取ったりする。多くの場合、</tgt>` | 1598 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1502 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>好经常会听到</src><tgt><\|wait\|></tgt>` | 1869 |
| 9 | `<src>这样说：“</src><tgt>するとき、よく耳にするのが</tgt>` | `<src>人们这样说：“</src><tgt>人々はよく</tgt>` | 1439 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 1086 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1554 |
| 12 | `<src>又在说谎了，</src><tgt>「ほら、また嘘をついている。</tgt>` | `<src>又在作谎了。”</src><tgt>「見て、この人はまた嘘をついている」と言う。</tgt>` | 2020 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1202 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛已经说明了一切。</src><tgt><\|wait\|></tgt>` | 969 |
| 15 | `<src><\|wait\|></src><tgt>目がすべてを物語っているよ」という言葉です。</tgt>` | `<src><\|wait\|></src><tgt>彼の目はすべてを物語っている。</tgt>` | 674 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是说，</src><tgt><\|wait\|></tgt>` | 670 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说：“</src><tgt><\|wait\|></tgt>` | 698 |

---

### Test Example 50 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1308 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1199 |
| 3 | `<src>운전 을 </src><tgt>一进去就会晕头转向。</tgt>` | `<src>엄청 헤맵니다. </src><tgt>进入的时候非常艰难。</tgt>` | 980 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>운전 을 하고 </src><tgt><\|wait\|></tgt>` | 1399 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1417 |
| 6 | `<src>공간 에 뭐 </src><tgt>不管是开车还是走路，</tgt>` | `<src>걸어 걸어 다니 고 아니면 </src><tgt>开车、走路，或者</tgt>` | 1442 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>막굴을 가면 </src><tgt><\|wait\|></tgt>` | 1695 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 864 |
| 9 | `<src><\|wait\|></src><tgt>去江北就不用说了，去外国</tgt>` | `<src>외국 에 나가 는 것도 </src><tgt>在丛林里乱窜，那更是难说，</tgt>` | 2800 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬 이요. </src><tgt><\|wait\|></tgt>` | 988 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>좀 챙기 네요. </src><tgt><\|wait\|></tgt>` | 1816 |
| 12 | `<src>대신 에 </src><tgt>就更惨了。真有点丢人。不过，</tgt>` | `<src>대신 에 이제 </src><tgt>出国也是一场灾难。得好好照顾一下。不过，</tgt>` | 2018 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1232 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>열심히 모아 봐요. </src><tgt><\|wait\|></tgt>` | 1201 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt>我会努力去问路。这一点倒是做得还行。</tgt>` | `<src>그거 는 다행 이긴 것 같아요. </src><tgt>不如努力攒钱吧。这应该会比较好。我觉得</tgt>` | 1141 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>예. </src><tgt><\|wait\|></tgt>` | 580 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=4 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 875 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1288 |
| 3 | `<src>내놓 았습니다. </src><tgt>そしてこれについて多くの人々が分析を出しています。</tgt>` | `<src>분석 을 내놓 았습니다. </src><tgt>これについて多くの人が分析を提示しました。</tgt>` | 1616 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 </src><tgt><\|wait\|></tgt>` | 708 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>로쿠자 내부 색을 보시면 </src><tgt><\|wait\|></tgt>` | 1949 |
| 6 | `<src>소니가 </src><tgt>こちらのロクザの分析を見ると、ソニーが</tgt>` | `<src>소니가 </src><tgt>ここでロクジャの内部色を見ると、ソニーが</tgt>` | 1715 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>UHD 60 </src><tgt><\|wait\|></tgt>` | 1311 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>HzF 패널 을 </src><tgt><\|wait\|></tgt>` | 1793 |
| 9 | `<src>128비트로 낮춘 </src><tgt>26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128bit로 </src><tgt>UHD60HzFパネルを128bitで</tgt>` | 1918 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것을 보여 줍니다. </src><tgt><\|wait\|></tgt>` | 2068 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 616 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt>ようです。</tgt>` | `<src>X 박스 시리즈 X에서도 없는 </src><tgt>下げていることがわかります。XボックスシリーズXにもない</tgt>` | 2107 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 904 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 1092 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt>インフィニットキャッシュL3は、XboxSeriesXにもなく、ここにもありません。</tgt>` | `<src>LCD가 여기 도 없다. </src><tgt>インフィニットキャッシュLCDはありません。</tgt>` | 970 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 737 |

---

### Test Example 52 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 914 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>フロア1の所</src><tgt><\|wait\|></tgt>` | 1368 |
| 3 | `<src>那个现象：</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다.</tgt>` | `<src>知っていたが、</src><tgt>1층에 대해 알고 있었지만,</tgt>` | 1153 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1083 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>毎晩</src><tgt><\|wait\|></tgt>` | 1588 |
| 6 | `<src>处于爱之中，</src><tgt>우리가 사랑 속에</tgt>` | `<src>我知知心中</src><tgt>매일 밤 내 마음속에</tgt>` | 1228 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>所谓の愛</src><tgt><\|wait\|></tgt>` | 1683 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 773 |
| 9 | `<src>同时进入恨。</src><tgt>있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>がもはや魂に</src><tgt>그 소위 사랑이</tgt>` | 2212 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1209 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>入った際、</src><tgt><\|wait\|></tgt>` | 2061 |
| 12 | `<src>它是爱；</src><tgt>아침에는 그것이 사랑이지만,</tgt>` | `<src>他は愛、</src><tgt>영혼에 들어갈 때, 그는 사랑을</tgt>` | 1367 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>倒れおわん上。</src><tgt><\|wait\|></tgt>` | 1008 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>他</src><tgt><\|wait\|></tgt>` | 1179 |
| 15 | `<src><\|wait\|></src><tgt>밤이 되면 미움으로 변합니다.</tgt>` | `<src>就變成恨。</src><tgt>뒤집어 버립니다. 그는 사랑을 증오로 바꿉니다.</tgt>` | 1256 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>那个重白，</src><tgt><\|wait\|></tgt>` | 860 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 701 |
| 18 | `<src>继续在移动。</src><tgt>그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>继续在一道。</src><tgt>그 ' 중백' 은 계속해서 한 줄기...</tgt>` | 601 |

---

### Test Example 53 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1049 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>Also, you will not </src><tgt><\|wait\|></tgt>` | 1382 |
| 3 | `<src>you will not be able to </src><tgt>另外，你没法</tgt>` | `<src><\|wait\|></src><tgt>另外，</tgt>` | 874 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>be able to move media objects </src><tgt><\|wait\|></tgt>` | 1477 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1671 |
| 6 | `<src>between the resources. </src><tgt>在资源之间移动媒体对象。</tgt>` | `<src>between the resources. </src><tgt>你无法在资源之间移动媒体对象。</tgt>` | 1204 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if you </src><tgt><\|wait\|></tgt>` | 1748 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>get into a </src><tgt><\|wait\|></tgt>` | 717 |
| 9 | `<src>a situation </src><tgt>所以，如果</tgt>` | `<src>situation where you </src><tgt>所以，如果你遇到</tgt>` | 1880 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 1541 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 2013 |
| 12 | `<src>files to a particular resource, </src><tgt>你发现自己给某个资源加错了媒体文件，就</tgt>` | `<src>files to a particular resource, </src><tgt>情况，发现把错误的媒体文件添加到了某个资源中，</tgt>` | 1959 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know. </src><tgt><\|wait\|></tgt>` | 1318 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>Now, and we can see about </src><tgt><\|wait\|></tgt>` | 883 |
| 15 | `<src><\|wait\|></src><tgt>告诉我们一声。我们可以帮你想想办法</tgt>` | `<src><\|wait\|></src><tgt>请告诉我们。我们</tgt>` | 687 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>moving those media files and then making sure </src><tgt><\|wait\|></tgt>` | 861 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 649 |
| 18 | `<src>properly. </src><tgt>把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>they get backed up properly. </src><tgt>可以帮您移动这些媒体文件，并确保它们正确备份。</tgt>` | 769 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1376 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 1078 |
| 3 | `<src>in the first section </src><tgt>最初のセクションでは少し葛藤していました。</tgt>` | `<src>on the first section about </src><tgt>最初のセクションについて、少し混乱していました。</tgt>` | 1096 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>the AHR field </src><tgt><\|wait\|></tgt>` | 1234 |
| 6 | `<src><\|wait\|></src><tgt>EHRフィールドの</tgt>` | `<src><\|wait\|></src><tgt>AHR分野の</tgt>` | 1401 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | 1039 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1339 |
| 9 | `<src><\|wait\|></src><tgt>決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>重要性について、</tgt>` | 1549 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, which is obviously </src><tgt><\|wait\|></tgt>` | 1361 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>one of my loves. </src><tgt><\|wait\|></tgt>` | 1009 |
| 12 | `<src><\|wait\|></src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。</tgt>` | `<src>Is that if </src><tgt>バリアントデータベースとの比較について。これは私の好きな分野の一つです。もし</tgt>` | 2303 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1868 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 1371 |
| 15 | `<src>to be in these </src><tgt>つまり、</tgt>` | `<src>to be in these </src><tgt>これらの</tgt>` | 1094 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 928 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, there's nothing </src><tgt><\|wait\|></tgt>` | 779 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>to draw from, right? </src><tgt>データソースに含めるべき分野について合意できなければ、そこからデータを取得できるものはない、ということになりますよね？</tgt>` | 946 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 432 |

---

### Test Example 55 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1276 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful, </src><tgt><\|wait\|></tgt>` | 1164 |
| 3 | `<src>right, </src><tgt>有意义的个人权利，</tgt>` | `<src>individual right, </src><tgt>有意义的、个人的权利，</tgt>` | 1052 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1373 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1282 |
| 6 | `<src>last, not leading. </src><tgt>而最高法院是最后才介入的，不是引领者。</tgt>` | `<src>last, not leading. And I don't know </src><tgt>最高法院最后才出现，而不是引领。我不知道</tgt>` | 1910 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>if the courts want to be </src><tgt><\|wait\|></tgt>` | 1845 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1517 |
| 9 | `<src>the the vanguard of social </src><tgt>我不认为</tgt>` | `<src>the the vanguard of </src><tgt>法院是否想成为</tgt>` | 1253 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change. </src><tgt><\|wait\|></tgt>` | 1043 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>These days, </src><tgt><\|wait\|></tgt>` | 2010 |
| 12 | `<src><\|wait\|></src><tgt>法院现在想成为社会变革的先锋，</tgt>` | `<src><\|wait\|></src><tgt>社会变革的先锋。如今，</tgt>` | 606 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | 1670 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1328 |
| 15 | `<src><\|wait\|></src><tgt>它们更倾向于</tgt>` | `<src>the consensus that's already </src><tgt>它们更多反映的是</tgt>` | 1116 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>emerged. </src><tgt><\|wait\|></tgt>` | 883 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 647 |
| 18 | `<src>So you have some </src><tgt>反映已经形成的共识。所以，</tgt>` | `<src>you have </src><tgt>已经形成的共识。</tgt>` | 396 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>some federal judges </src><tgt><\|wait\|></tgt>` | 329 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 374 |
| 21 | `<src>who. </src><tgt>有些联邦法官……</tgt>` | `<src>who. </src><tgt>所以，你有一些联邦法官……</tgt>` | 467 |

---

### Test Example 56 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point </src><tgt><\|wait\|></tgt>` | 903 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>in his Jesus </src><tgt><\|wait\|></tgt>` | 1287 |
| 3 | `<src>is hungry. </src><tgt>ある時、彼はイエスが空腹だと知っています。</tgt>` | `<src>as a hungry, </src><tgt>ある時、イエスが飢えを</tgt>` | 1379 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>he knows that </src><tgt><\|wait\|></tgt>` | 943 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1845 |
| 6 | `<src><\|wait\|></src><tgt>食べ物をとらずに</tgt>` | `<src>be in the wilderness </src><tgt>知っていた。彼は、</tgt>` | 1275 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days that he's hungry, </src><tgt><\|wait\|></tgt>` | 1861 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he says to </src><tgt><\|wait\|></tgt>` | 1841 |
| 9 | `<src>to Jesus," Hey, </src><tgt>荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus, hey, if you're </src><tgt>40日間飢えのまま荒野にいるだろうと。だからイエスに言ったんだ。「おい、</tgt>` | 2511 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | 1767 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1756 |
| 12 | `<src>Turn these stones to bread." </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。</tgt>` | `<src>Turn these stones to bread. </src><tgt>神の御子なら証明してみろ。この石をパンに変えろ」。</tgt>` | 1656 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 1025 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that </src><tgt><\|wait\|></tgt>` | 893 |
| 15 | `<src>temptation? </src><tgt>イエスはその誘惑にどう対処したんでしょう？</tgt>` | `<src>temptation? </src><tgt>彼はその誘惑にどう対処したのだろうか？</tgt>` | 851 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 430 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Man Jonathan led by </src><tgt><\|wait\|></tgt>` | 397 |
| 18 | `<src>by bread alone. </src><tgt>人はパンだけで生きるものではない。</tgt>` | `<src>barrel alone. </src><tgt>男、ヨナタンは樽を背負って一人で進んだ。</tgt>` | 606 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1008 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片呢，</src><tgt><\|wait\|></tgt>` | 1266 |
| 3 | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | `<src><\|wait\|></src><tgt>그럼 사진을 한번 볼까요?</tgt>` | 978 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的不普遍呢，</src><tgt><\|wait\|></tgt>` | 1371 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1459 |
| 6 | `<src>的部分。</src><tgt>사진 부분을 보면 거실 공간이 보이네요.</tgt>` | `<src>客梯的部分。</src><tgt>사진의 보편적인 부분은 계단 부분입니다.</tgt>` | 1489 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1627 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src>那客梯一般都是</src><tgt><\|wait\|></tgt>` | 894 |
| 9 | `<src>我们</src><tgt>거실은 보통 우리가</tgt>` | `<src>属于我们</src><tgt>계단은 보통</tgt>` | 1830 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1372 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在休息的地方，所以呢，</src><tgt><\|wait\|></tgt>` | 1843 |
| 12 | `<src>所以呢，这身体的部分</src><tgt>쉬는 곳이잖아요. 그래서</tgt>` | `<src>是身体的部分</src><tgt>휴식 공간에 속하죠. 그래서</tgt>` | 709 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，会反映的是</src><tgt><\|wait\|></tgt>` | 1873 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给</src><tgt><\|wait\|></tgt>` | 1235 |
| 15 | `<src>一点时间，</src><tgt>이 신체 부위도 여러분이 자신에게 시간을 내서</tgt>` | `<src>自己一点时间</src><tgt>신체 부분은</tgt>` | 1153 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 849 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>可以好好地坐下来休息</src><tgt><\|wait\|></tgt>` | 675 |
| 18 | `<src>我们可以看到这边是</src><tgt>편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>的时候我们可以看到</src><tgt>자신을 위해 잠시 앉아서 쉴 때</tgt>` | 609 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>这边是存放一人的嘛，</src><tgt><\|wait\|></tgt>` | 386 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>好，</src><tgt><\|wait\|></tgt>` | 427 |
| 21 | `<src>所以是说。</src><tgt>아무도 없네요. 그래서 말인데...</tgt>` | `<src>所以是说。</src><tgt>보관할 수 있는 공간이라는 걸 보여줍니다. 자, 그래서 말이죠.</tgt>` | 507 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 2 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 936 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1198 |
| 3 | `<src>and they often </src><tgt>こうした人々は非常に稀です。そして、</tgt>` | `<src><\|wait\|></src><tgt>これらの人々は非常に稀で、</tgt>` | 1072 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>and they often show up </src><tgt><\|wait\|></tgt>` | 1375 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1689 |
| 6 | `<src>completely revolutionize the world. </src><tgt>世界を根本から変えるような存在であることがよくあります。</tgt>` | `<src>to completely revolutionize the world. </src><tgt>世界を完全に変革するよう、しばしば現れます。</tgt>` | 1468 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1726 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>The personality is </src><tgt><\|wait\|></tgt>` | 1306 |
| 9 | `<src>something of a </src><tgt>彼らの性格は</tgt>` | `<src>something of a contradiction. </src><tgt>その性格は矛盾をはらんでいます。</tgt>` | 1887 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 826 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>While they're </src><tgt><\|wait\|></tgt>` | 1973 |
| 12 | `<src>extroverted, </src><tgt>矛盾しています。外交的である一方、</tgt>` | `<src>extroverted, </src><tgt>外向的である一方で、</tgt>` | 1850 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1288 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations, </src><tgt><\|wait\|></tgt>` | 539 |
| 15 | `<src>and like to </src><tgt>無意味な会話は嫌います。そして、</tgt>` | `<src><\|wait\|></src><tgt>無意味な会話を嫌い、</tgt>` | 1188 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>and like to get straight to </src><tgt><\|wait\|></tgt>` | 747 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>the point. </src><tgt><\|wait\|></tgt>` | 666 |
| 18 | `<src>They also love to </src><tgt>要点を突くのを好みます。また、</tgt>` | `<src>They also love to </src><tgt>要点を直接言いたいタイプです。また、</tgt>` | 712 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 449 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 433 |
| 21 | `<src><\|wait\|></src><tgt>あえて悪魔の代弁者を演じることを好み、</tgt>` | `<src><\|wait\|></src><tgt>悪魔の代弁者になるのも好きです。</tgt>` | 372 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>and never shy away from a debate. </src><tgt><\|wait\|></tgt>` | 412 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 251 |
| 24 | `<src><\|wait\|></src><tgt>議論を避けることはありません。</tgt>` | `<src>E.T.P. stands for </src><tgt>議論を避けることはありません。E.T.P.は</tgt>` | 567 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>for. </src><tgt><\|wait\|></tgt>` | 219 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=5 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 </src><tgt><\|wait\|></tgt>` | 973 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 정부 를 </src><tgt><\|wait\|></tgt>` | 1381 |
| 3 | `<src>명분 이 후보 를 </src><tgt>Previously, Lee Jun- seok</tgt>` | `<src>거부 한 명분 이 후보 를 </src><tgt>Lee Jun- seok</tgt>` | 1328 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 943 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1924 |
| 6 | `<src>위해서 라면서 </src><tgt>claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election—</tgt>` | `<src>위해서 라면서 </src><tgt>had previously</tgt>` | 1140 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1821 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1992 |
| 9 | `<src>윤석열 후보 가 </src><tgt>and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt>made quite a show of support for the candidate, claiming he was running for the sake of the candidate's victory. But now, Yoon Suk- yeol</tgt>` | 2842 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 1256 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1826 |
| 12 | `<src>이준석은 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok</tgt>` | `<src>이준석은 들은 해 놓고 </src><tgt>has taken down Kim Jong- in. Lee Jun- seok</tgt>` | 1567 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 </src><tgt><\|wait\|></tgt>` | 1092 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | 934 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>독기 를 </src><tgt><\|wait\|></tgt>` | 710 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>뿜은 공격 성을 </src><tgt><\|wait\|></tgt>` | 527 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 420 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 436 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>작정 한 것입니다. </src><tgt>is now determined to attack Yoon Suk- yeol with the same venom he showed when he was talking about the candidate's victory.</tgt>` | 597 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 315 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt>And then there's the sex bribery scandal involving Lee Jun-seok, broken by Garo Sero Institute—</tgt>` | `<src>이준석의 성상 랍권 </src><tgt><\|wait\|></tgt>` | 364 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt>Lee Jun- seok's ' Heart- Valued' status</tgt>` | 452 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 289 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 </src><tgt><\|wait\|></tgt>` | 307 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt>what a huge boon that is for the Democratic Party to attack with, right?</tgt>` | `<src>얼마나 큰 호재입니까? </src><tgt>is a huge boon for the Democratic Party's attack.</tgt>` | 438 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 2 wait windows before each target release.
- TGT_METRICS: filtered (max_empty_window=3 > requested_window=2)

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1075 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後ね今</src><tgt><\|wait\|></tgt>` | 1122 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいです。なので</src><tgt>I'd like to make something after a meal now. So,</tgt>` | 1549 |
| 4 | `<src>みたいですなのでここのね</src><tgt>Well, it seems they're building a dining area right now,</tgt>` | `<src>ここで</src><tgt><\|wait\|></tgt>` | 988 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>このホテル</src><tgt><\|wait\|></tgt>` | 1315 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>の朝食が</src><tgt>the breakfast at this hotel</tgt>` | 1391 |
| 7 | `<src>朝食が食べれる場所</src><tgt>so this Gold Stone Hotel</tgt>` | `<src>食べれる場所</src><tgt><\|wait\|></tgt>` | 1051 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 1269 |
| 9 | `<src>予定になってるので</src><tgt><\|wait\|></tgt>` | `<src>予定になっているので</src><tgt>is supposed to be a place where you can eat breakfast. So,</tgt>` | 2630 |
| 10 | `<src>今後ねここ</src><tgt>is also planning to have breakfast available.</tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 1125 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここゴルドストンホテル</src><tgt><\|wait\|></tgt>` | 2054 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | 609 |
| 13 | `<src>なっていう方はですね</src><tgt>So, for anyone</tgt>` | `<src>なという方はですね</src><tgt>if you're thinking of staying at the Goldston Hotel here in the future,</tgt>` | 2132 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討なさ</src><tgt><\|wait\|></tgt>` | 867 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>てもってみてもまあいいんじゃない</src><tgt><\|wait\|></tgt>` | 1106 |
| 16 | `<src><\|wait\|></src><tgt>thinking about staying here in the future,</tgt>` | `<src>かなと</src><tgt>you might want to consider it, I think it's a good option.</tgt>` | 1047 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>思います。ここ</src><tgt><\|wait\|></tgt>` | 654 |
| 18 | `<src>のホテルからですね釜山</src><tgt><\|wait\|></tgt>` | `<src>のホテルからですね</src><tgt><\|wait\|></tgt>` | 522 |
| 19 | `<src>駅ももう</src><tgt>it might be worth considering. From this hotel,</tgt>` | `<src>プサン駅も</src><tgt>From this hotel,</tgt>` | 417 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 442 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分かかる</src><tgt><\|wait\|></tgt>` | 295 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt>it's less than a minute's walk to Busan Station,</tgt>` | `<src>かかんないか</src><tgt>you can walk to Busan Station in about a minute.</tgt>` | 338 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 300 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のねまあ</src><tgt><\|wait\|></tgt>` | 277 |
| 25 | `<src>ホテルになってますので</src><tgt>so the location is really good.</tgt>` | `<src>ホテルになってますので</src><tgt>It's in a really convenient location.</tgt>` | 441 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>翌ったらですね</src><tgt><\|wait\|></tgt>` | 322 |
| 27 | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>ご検討なさってみて</src><tgt><\|wait\|></tgt>` | 334 |
| 28 | `<src>ください</src><tgt>If you'd like, please consider it.</tgt>` | `<src>くださいそれでは</src><tgt>So please give it some thought. Well,</tgt>` | 326 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は</src><tgt><\|wait\|></tgt>` | 198 |
