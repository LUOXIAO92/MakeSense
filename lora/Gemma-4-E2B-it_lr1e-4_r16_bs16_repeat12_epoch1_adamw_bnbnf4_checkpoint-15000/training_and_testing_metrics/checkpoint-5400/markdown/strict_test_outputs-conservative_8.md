# OpenAI-Compatible Runtime Strict Test

Test Metrics
  - STEP: 0
  - TOTAL_AVAILABLE_TEST_ROWS: 60
  - SELECTED_TEST_ROWS: 60
  - PROTOCOL_ADHERENCE_RATE: 1.0000
  - RECORD_COUNT: 60
  - SRC_RELEASE_ACCURACY: 0.9513
  - SRC_RELEASE_TOTAL: 718
  - SRC_WAIT_ACCURACY: 0.5762
  - SRC_WAIT_TOTAL: 151
  - TARGET_METRICS_FILTERED_RECORD_COUNT: 0
  - TARGET_METRICS_FILTERED_TURN_COUNT: 0
  - TARGET_METRICS_INCLUDED_RECORD_COUNT: 60
  - TGT_RELEASE_ACCURACY: 1.0000
  - TGT_RELEASE_TOTAL: 70
  - TGT_WAIT_ACCURACY: 1.0000
  - TGT_WAIT_TOTAL: 799
  - TURN_COUNT: 869

Timing Metrics
  - PROCESS_TIME_MS_COUNT: 869
  - PROCESS_TIME_MS_AVG: 1379.2180
  - PROCESS_TIME_MS_P50: 1370.4980
  - PROCESS_TIME_MS_P95: 2227.8180
  - PROCESS_TIME_MS_MAX: 3196.2980

---

- model_name: `gemma-4-E2B-it-lora`
- base_url: `http://127.0.0.1:18000/v1`
- concurrency: `90`
- splits: `test`
- constrained_decoding: `False`

---

### Test Example 1 / 60
- UID: ZH_W0NbyT5Ak-A_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要气($_314)！</src><tgt><\|wait\|></tgt>` | 1114 |
| 2 | `<src>要气熟是容易的，</src><tgt><\|wait\|></tgt>` | `<src>是容易的，</src><tgt><\|wait\|></tgt>` | 1044 |
| 3 | `<src>但是</src><tgt><\|wait\|></tgt>` | `<src>但是</src><tgt><\|wait\|></tgt>` | 1185 |
| 4 | `<src>只有一个师父</src><tgt><\|wait\|></tgt>` | `<src>只有一个师傅</src><tgt><\|wait\|></tgt>` | 1245 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>知道，</src><tgt><\|wait\|></tgt>` | 1324 |
| 6 | `<src>知道如何</src><tgt><\|wait\|></tgt>` | `<src>如何除于</src><tgt><\|wait\|></tgt>` | 1562 |
| 7 | `<src>处于中间，</src><tgt><\|wait\|></tgt>` | `<src>终间，</src><tgt><\|wait\|></tgt>` | 1489 |
| 8 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1498 |
| 9 | `<src>虚阿凡</src><tgt>呼吸を数えるのは簡単ですが、中間に留まる方法を知っているのは師匠だけです。だからこそ、シュ・アファンは</tgt>` | `<src>需要反。</src><tgt>気は易しい。でも師匠が一人しか知らない。どうやって終間を離れるか。だから、反転が必要だ。</tgt>` | 1974 |
| 10 | `<src>要成为</src><tgt><\|wait\|></tgt>` | `<src>要成为一个</src><tgt><\|wait\|></tgt>` | 440 |
| 11 | `<src>一个师父。</src><tgt><\|wait\|></tgt>` | `<src>师傅。</src><tgt><\|wait\|></tgt>` | 1070 |

---

### Test Example 2 / 60
- UID: ZH_B00021_S00118_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1067 |
| 2 | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | `<src>抛洒完以后呢，</src><tgt><\|wait\|></tgt>` | 1113 |
| 3 | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | `<src>内部的压力减轻，</src><tgt><\|wait\|></tgt>` | 1626 |
| 4 | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | `<src>能量也衰弱了，</src><tgt><\|wait\|></tgt>` | 1539 |
| 5 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src>然后</src><tgt><\|wait\|></tgt>` | 751 |
| 6 | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | `<src>就停留在一个</src><tgt><\|wait\|></tgt>` | 1456 |
| 7 | `<src>相对的低</src><tgt><\|wait\|></tgt>` | `<src>相对的低</src><tgt><\|wait\|></tgt>` | 1504 |
| 8 | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | `<src>能量的运行</src><tgt><\|wait\|></tgt>` | 1693 |
| 9 | `<src>状态，</src><tgt>放出が終わると、内部の圧力が軽くなり、エネルギーも弱まります。そして、比較的低エネルギーの状態にとどまります。</tgt>` | `<src>状态，</src><tgt>撒き散らした後、内部の圧力が軽減し、エネルギーも衰弱します。そして、比較的低いエネルギーの運行状態に留まります。</tgt>` | 1869 |
| 10 | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | `<src>这就是所谓的</src><tgt><\|wait\|></tgt>` | 549 |
| 11 | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | `<src>抑郁状态。</src><tgt><\|wait\|></tgt>` | 977 |

---

### Test Example 3 / 60
- UID: JA_48elNGI2sVo_W000267
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Tシャツなどが</src><tgt><\|wait\|></tgt>` | `<src>Tシャツ</src><tgt><\|wait\|></tgt>` | 1170 |
| 2 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>などがあの</src><tgt><\|wait\|></tgt>` | 1030 |
| 3 | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | `<src>いただもらえる</src><tgt><\|wait\|></tgt>` | 1070 |
| 4 | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | `<src>といったようなものも</src><tgt><\|wait\|></tgt>` | 1356 |
| 5 | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | `<src>用意しておりますので</src><tgt><\|wait\|></tgt>` | 1424 |
| 6 | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | `<src>ぜひご参加ください。</src><tgt><\|wait\|></tgt>` | 1578 |
| 7 | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | `<src>ご連絡としては</src><tgt><\|wait\|></tgt>` | 1470 |
| 8 | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | `<src>以上になりまして、</src><tgt><\|wait\|></tgt>` | 1549 |
| 9 | `<src>えっと</src><tgt>We have prepared things like T- shirts that you can get, so please be sure to join us. That's all for the announcements,</tgt>` | `<src>えっと</src><tgt>We have things like T- shirts available, so please feel free to join. That's all for the contact information.</tgt>` | 1541 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>よろしくお願いします。</src><tgt><\|wait\|></tgt>` | 725 |
| 11 | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | `<src>ランチの案内がありますので</src><tgt><\|wait\|></tgt>` | 1059 |
| 12 | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | `<src>もう少々お待ちください。</src><tgt><\|wait\|></tgt>` | 1946 |

---

### Test Example 4 / 60
- UID: JA_B00001_S00577_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>大抵</src><tgt><\|wait\|></tgt>` | `<src>大抵</src><tgt><\|wait\|></tgt>` | 1098 |
| 2 | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | `<src>このあたりから</src><tgt><\|wait\|></tgt>` | 1049 |
| 3 | `<src>始めた</src><tgt><\|wait\|></tgt>` | `<src>始めた</src><tgt><\|wait\|></tgt>` | 949 |
| 4 | `<src>もので、</src><tgt><\|wait\|></tgt>` | `<src>もので、</src><tgt><\|wait\|></tgt>` | 1379 |
| 5 | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | `<src>ゴッホ、</src><tgt><\|wait\|></tgt>` | 1501 |
| 6 | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | `<src>ゴーギャン、</src><tgt><\|wait\|></tgt>` | 1542 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 443 |
| 8 | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | `<src>セザンヌ、</src><tgt><\|wait\|></tgt>` | 1499 |
| 9 | `<src>ルナールなど</src><tgt>大致是从这一带开始的，</tgt>` | `<src>ルナールなど</src><tgt>大概是从这里开始的，</tgt>` | 1657 |
| 10 | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | `<src>という人の絵</src><tgt><\|wait\|></tgt>` | 1744 |
| 11 | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | `<src>は、田舎の</src><tgt><\|wait\|></tgt>` | 1161 |
| 12 | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | `<src>中学生でも。</src><tgt><\|wait\|></tgt>` | 1961 |

---

### Test Example 5 / 60
- UID: JA_A7kJ7PmPk8g_W000017
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>最初から</src><tgt><\|wait\|></tgt>` | `<src>最初から</src><tgt><\|wait\|></tgt>` | 826 |
| 2 | `<src>あの特に</src><tgt><\|wait\|></tgt>` | `<src>あの特に</src><tgt><\|wait\|></tgt>` | 1030 |
| 3 | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | `<src>これなんかまだ</src><tgt><\|wait\|></tgt>` | 1551 |
| 4 | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | `<src>一年生ですからね。</src><tgt><\|wait\|></tgt>` | 1342 |
| 5 | `<src>この時点で</src><tgt><\|wait\|></tgt>` | `<src>この時点で</src><tgt><\|wait\|></tgt>` | 1028 |
| 6 | `<src>こう短く</src><tgt><\|wait\|></tgt>` | `<src>こう短く</src><tgt><\|wait\|></tgt>` | 1491 |
| 7 | `<src>剪定を</src><tgt><\|wait\|></tgt>` | `<src>剪定を</src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1824 |
| 9 | `<src>こうタイズしてってあげると</src><tgt>从一开始，尤其是这一棵现在还只是一年生。在这个阶段如果能把剪枝持续做好的话，</tgt>` | `<src>こうタイズしてってあげると</src><tgt>从一开始，特别是现在才一年级，对吧。这个时候剪短枝条，收紧一点，</tgt>` | 2228 |
| 10 | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | `<src>十年経っても</src><tgt><\|wait\|></tgt>` | 1023 |
| 11 | `<src>大した。</src><tgt><\|wait\|></tgt>` | `<src>大した。</src><tgt><\|wait\|></tgt>` | 2074 |

---

### Test Example 6 / 60
- UID: KO_B00001_S08422_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>아 저는 </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 1050 |
| 2 | `<src>옹심이, </src><tgt><\|wait\|></tgt>` | `<src>저는 용심히 </src><tgt><\|wait\|></tgt>` | 1079 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1185 |
| 4 | `<src>칼 옹심이, 쌀국수하고 </src><tgt><\|wait\|></tgt>` | `<src>칼 용심히 </src><tgt><\|wait\|></tgt>` | 1413 |
| 5 | `<src>옹심이가 </src><tgt><\|wait\|></tgt>` | `<src>쇠술 용심히가 </src><tgt><\|wait\|></tgt>` | 1237 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1551 |
| 7 | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | `<src>섞여 있는 건데요. </src><tgt><\|wait\|></tgt>` | 1528 |
| 8 | `<src>야, </src><tgt><\|wait\|></tgt>` | `<src>야, </src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src>진짜 이거 </src><tgt>I'm having the ongsimi and kal- ongsimi— it's a mix of rice noodles and ongsimi. Man, this is</tgt>` | `<src>진짜 이거 </src><tgt>Ah, it's a mix of ' yongsimi ' (용심히), ' kal yongsimi ' (칼 용심히), and ' so-sul yongsimi ' (쇠술 용심히). Wow,</tgt>` | 2214 |
| 10 | `<src>해장으로도 조금 죽입니다, </src><tgt><\|wait\|></tgt>` | `<src>해당 으로 </src><tgt><\|wait\|></tgt>` | 1142 |
| 11 | `<src>진짜. </src><tgt><\|wait\|></tgt>` | `<src>조금씩 입니다, 저. </src><tgt><\|wait\|></tgt>` | 2188 |

---

### Test Example 7 / 60
- UID: KO_B00002_S08662_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>명당에 있는 </src><tgt><\|wait\|></tgt>` | 1254 |
| 2 | `<src>명단 에 있는 학생 들은 </src><tgt><\|wait\|></tgt>` | `<src>학생 들은 </src><tgt><\|wait\|></tgt>` | 1075 |
| 3 | `<src>실제로 </src><tgt><\|wait\|></tgt>` | `<src>실제로 </src><tgt><\|wait\|></tgt>` | 1405 |
| 4 | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | `<src>지능 이 높지 않았고 </src><tgt><\|wait\|></tgt>` | 1646 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 940 |
| 6 | `<src>무작위로 </src><tgt><\|wait\|></tgt>` | `<src>무작위로 뽑힌 </src><tgt><\|wait\|></tgt>` | 1543 |
| 7 | `<src>뽑힌 학생 들이었기 </src><tgt><\|wait\|></tgt>` | `<src>학생 들이 </src><tgt><\|wait\|></tgt>` | 1571 |
| 8 | `<src>때문 입니다. </src><tgt><\|wait\|></tgt>` | `<src>어떤 분입니다. </src><tgt><\|wait\|></tgt>` | 1734 |
| 9 | `<src><\|wait\|></src><tgt>Because the students on the list weren't actually highly intelligent. They were chosen at random.</tgt>` | `<src><\|wait\|></src><tgt>The students in the auspicious positions were actually not that intelligent. They were just randomly selected.</tgt>` | 2135 |
| 10 | `<src>사실 을 몰랐 던 </src><tgt><\|wait\|></tgt>` | `<src>사실 을 모를 랐던 </src><tgt><\|wait\|></tgt>` | 1118 |
| 11 | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | `<src>교사 들은. </src><tgt><\|wait\|></tgt>` | 2209 |

---

### Test Example 8 / 60
- UID: ZH_B00041_S00155_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1173 |
| 2 | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | `<src>家长需要做的是，</src><tgt><\|wait\|></tgt>` | 1106 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>用我们</src><tgt><\|wait\|></tgt>` | 1417 |
| 4 | `<src>用我们深深的</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1307 |
| 5 | `<src>爱浇水、</src><tgt><\|wait\|></tgt>` | `<src>深深的爱浇水，</src><tgt><\|wait\|></tgt>` | 1261 |
| 6 | `<src>施肥，</src><tgt><\|wait\|></tgt>` | `<src>施肥，</src><tgt><\|wait\|></tgt>` | 1456 |
| 7 | `<src>给足</src><tgt><\|wait\|></tgt>` | `<src>给足</src><tgt><\|wait\|></tgt>` | 1454 |
| 8 | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | `<src>孩子心理营养，</src><tgt><\|wait\|></tgt>` | 1827 |
| 9 | `<src><\|wait\|></src><tgt>What parents need to do is this: water and fertilize with our deep love, give children enough psychological nourishment,</tgt>` | `<src><\|wait\|></src><tgt>What parents need to do is water our children with deep love, fertilize them with care, and provide them with the psychological nourishment they need.</tgt>` | 2417 |
| 10 | `<src>并耐心等待孩子</src><tgt><\|wait\|></tgt>` | `<src>给耐心等等</src><tgt><\|wait\|></tgt>` | 987 |
| 11 | `<src>慢慢长大。</src><tgt><\|wait\|></tgt>` | `<src>孩子慢慢长大。</src><tgt><\|wait\|></tgt>` | 2184 |

---

### Test Example 9 / 60
- UID: KO_Djg2xNdyFCU_W000010
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>I am </src><tgt><\|wait\|></tgt>` | 928 |
| 2 | `<src>아이 엠 애플 을 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1082 |
| 3 | `<src>촉발 시키고 </src><tgt><\|wait\|></tgt>` | `<src>애플 을 켜 봤을 때 </src><tgt><\|wait\|></tgt>` | 1960 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1222 |
| 5 | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | `<src>자신 의 </src><tgt><\|wait\|></tgt>` | 938 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>페마를 </src><tgt><\|wait\|></tgt>` | 1357 |
| 7 | `<src>부모 를 죽인 페르 나 </src><tgt><\|wait\|></tgt>` | `<src>죽인 게 아니 낫나. </src><tgt><\|wait\|></tgt>` | 1746 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1620 |
| 9 | `<src>박한상과 </src><tgt>Park Han- sang is the degenerate who triggered the IMF crisis and killed his own parents.</tgt>` | `<src>박한상과 </src><tgt>When I turned on my Apple, I thought, ' I didn't kill my own demon. ' Park Han- sang</tgt>` | 2431 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>같은 세대 들이 </src><tgt><\|wait\|></tgt>` | 1112 |
| 11 | `<src>같은 세대 들입니다. </src><tgt><\|wait\|></tgt>` | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | 1982 |

---

### Test Example 10 / 60
- UID: EN_nUuwxonVyYE_W000054
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>What is your body </src><tgt><\|wait\|></tgt>` | `<src>What is your body </src><tgt><\|wait\|></tgt>` | 828 |
| 2 | `<src>doing? </src><tgt><\|wait\|></tgt>` | `<src>doing? </src><tgt><\|wait\|></tgt>` | 1003 |
| 3 | `<src>Drop into </src><tgt><\|wait\|></tgt>` | `<src>Drop into </src><tgt><\|wait\|></tgt>` | 1546 |
| 4 | `<src>your body. </src><tgt><\|wait\|></tgt>` | `<src>your body. </src><tgt><\|wait\|></tgt>` | 1240 |
| 5 | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | `<src>Where does the tension </src><tgt><\|wait\|></tgt>` | 1168 |
| 6 | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | `<src>start? What is it? </src><tgt><\|wait\|></tgt>` | 1631 |
| 7 | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | `<src>Is it a headache? </src><tgt><\|wait\|></tgt>` | 1591 |
| 8 | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | `<src>Is it a tightness in your chest? </src><tgt><\|wait\|></tgt>` | 1744 |
| 9 | `<src>I ask them what </src><tgt>你的身体在做什么？感受一下你的身体。紧张感从哪里开始？是什么样的？是头痛吗？还是胸口紧绷？我问他们，</tgt>` | `<src>I ask </src><tgt>你的身体在做什么？进入你的身体。紧张感从哪里开始？是什么？是头痛吗？是胸闷吗？</tgt>` | 2625 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>the more language </src><tgt><\|wait\|></tgt>` | 1726 |
| 11 | `<src>language are you using? </src><tgt><\|wait\|></tgt>` | `<src>you use. </src><tgt><\|wait\|></tgt>` | 1208 |

---

### Test Example 11 / 60
- UID: ZH_3X_Q9-mIhJI_W000026
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1294 |
| 2 | `<src>挖一点松子儿里</src><tgt><\|wait\|></tgt>` | `<src>怪在嵩邸字里边，</src><tgt><\|wait\|></tgt>` | 1242 |
| 3 | `<src>边，这个油性也很大。</src><tgt><\|wait\|></tgt>` | `<src>这个要因也很大。</src><tgt><\|wait\|></tgt>` | 1675 |
| 4 | `<src>然后</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1224 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>然后呢，</src><tgt><\|wait\|></tgt>` | 934 |
| 6 | `<src>呢，我再放一点</src><tgt><\|wait\|></tgt>` | `<src>我在排课</src><tgt><\|wait\|></tgt>` | 1444 |
| 7 | `<src>儿核桃</src><tgt><\|wait\|></tgt>` | `<src>和谈人，</src><tgt><\|wait\|></tgt>` | 1493 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1794 |
| 9 | `<src>仁儿，仁儿里边</src><tgt>Add some pine nuts; they're quite oily. Then, I'll add some walnut kernels—</tgt>` | `<src>感觉是这样。</src><tgt>It's because of the situation at Songdi, and that's a big factor. Then, I was scheduling meetings and negotiating with the people, and I feel it's like that.</tgt>` | 2919 |
| 10 | `<src>这种核桃</src><tgt><\|wait\|></tgt>` | `<src>这种</src><tgt><\|wait\|></tgt>` | 1707 |
| 11 | `<src>仁儿。</src><tgt><\|wait\|></tgt>` | `<src>和谈人。</src><tgt><\|wait\|></tgt>` | 1171 |

---

### Test Example 12 / 60
- UID: EN_B00016_S00042_W000165
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 945 |
| 2 | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | `<src>Did very important research </src><tgt><\|wait\|></tgt>` | 1083 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1392 |
| 4 | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | `<src>on extremely happy people. </src><tgt><\|wait\|></tgt>` | 1432 |
| 5 | `<src>This is tip of the stem </src><tgt><\|wait\|></tgt>` | `<src>This is Tip the Stem. </src><tgt><\|wait\|></tgt>` | 1247 |
| 6 | `<src>research, </src><tgt><\|wait\|></tgt>` | `<src>Research. </src><tgt><\|wait\|></tgt>` | 1346 |
| 7 | `<src>looking at the ten percent </src><tgt><\|wait\|></tgt>` | `<src>Looking at 10% </src><tgt><\|wait\|></tgt>` | 1669 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1675 |
| 9 | `<src>of the happiest people </src><tgt>極めて幸福な人々に関する非常に重要な研究を行いました。これは最先端の研究です。最も幸福な上位10％の人々に注目し、</tgt>` | `<src>of the happiest people </src><tgt>非常に幸せな人たちに関する重要な研究を行いました。これは「Tip the Stem」という研究です。10%の最も幸せな人たちを</tgt>` | 2716 |
| 10 | `<src>out there, </src><tgt><\|wait\|></tgt>` | `<src>out there. </src><tgt><\|wait\|></tgt>` | 1852 |
| 11 | `<src>people that we can learn from. </src><tgt><\|wait\|></tgt>` | `<src>People that we can learn from. </src><tgt><\|wait\|></tgt>` | 1340 |

---

### Test Example 13 / 60
- UID: EN_nOtTM2Tg_DY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1213 |
| 2 | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | `<src>And lastly, </src><tgt><\|wait\|></tgt>` | 1081 |
| 3 | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | `<src>is repeat. </src><tgt><\|wait\|></tgt>` | 1620 |
| 4 | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | `<src>Learn to rinse and repeat. </src><tgt><\|wait\|></tgt>` | 1540 |
| 5 | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | `<src>Find what you're good at </src><tgt><\|wait\|></tgt>` | 1422 |
| 6 | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | `<src>and do more of it. </src><tgt><\|wait\|></tgt>` | 1007 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1517 |
| 8 | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | `<src>And what you're not good at, </src><tgt><\|wait\|></tgt>` | 1780 |
| 9 | `<src>get the people around you to help you with. </src><tgt>最后，要重复。学会不断重复。找到你的长处，多做那些事。至于你的短处，找身边的人帮你。</tgt>` | `<src>get the people around you to help you with. </src><tgt>最后，是重复。学会重复练习。找到你擅长的事情，多做一些。而你不擅长的事情，请身边的人帮忙。</tgt>` | 2915 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1949 |
| 11 | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | `<src>And until next time. </src><tgt><\|wait\|></tgt>` | 1356 |

---

### Test Example 14 / 60
- UID: KO_B00003_S00166_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1019 |
| 2 | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 죽여 달라 </src><tgt><\|wait\|></tgt>` | 1233 |
| 3 | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | `<src>해가지고 내가 </src><tgt><\|wait\|></tgt>` | 1682 |
| 4 | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | `<src>죽이 려고 들어왔 수다. </src><tgt><\|wait\|></tgt>` | 1704 |
| 5 | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | `<src>다른 잔찜에 </src><tgt><\|wait\|></tgt>` | 1385 |
| 6 | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | `<src>죽여 달라 </src><tgt><\|wait\|></tgt>` | 634 |
| 7 | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | `<src>해지 않았느냐? 내가 </src><tgt><\|wait\|></tgt>` | 1673 |
| 8 | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | `<src>그 소리 안 듣고 </src><tgt><\|wait\|></tgt>` | 1633 |
| 9 | `<src><\|wait\|></src><tgt>Someone asked me to kill them, so I came in here to do it. Didn't they ask you to kill them in the other room?</tgt>` | `<src>있는 줄 알았느냐? </src><tgt>You asked me to be killed by another method, so I came here to kill you. Didn't you ask to be killed by another method? Did you think I wasn't listening to that?</tgt>` | 3016 |
| 10 | `<src>있는 줄 알았느냐? 응? </src><tgt><\|wait\|></tgt>` | `<src>아, </src><tgt><\|wait\|></tgt>` | 2015 |
| 11 | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | `<src>내가 가. </src><tgt><\|wait\|></tgt>` | 1873 |

---

### Test Example 15 / 60
- UID: ZH_P0j1n-htgFu_W000014
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 967 |
| 2 | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | `<src>面对这个情况，我们就是</src><tgt><\|wait\|></tgt>` | 1236 |
| 3 | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | `<src>遇到问题</src><tgt><\|wait\|></tgt>` | 1449 |
| 4 | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | `<src>就赶紧的回报主管，</src><tgt><\|wait\|></tgt>` | 1646 |
| 5 | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | `<src>或是通知对方，</src><tgt><\|wait\|></tgt>` | 1073 |
| 6 | `<src>我们现有这个状况，</src><tgt><\|wait\|></tgt>` | `<src>我们现有的这个状况。</src><tgt><\|wait\|></tgt>` | 1221 |
| 7 | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | `<src>不要想自己</src><tgt><\|wait\|></tgt>` | 1474 |
| 8 | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | `<src>什么都把它扛下来，</src><tgt><\|wait\|></tgt>` | 1796 |
| 9 | `<src>独立承担。</src><tgt>In this situation, when we encounter a problem, we should immediately report it to our supervisor or notify the other party about our current status. Don't try to take everything on yourself or handle it alone.</tgt>` | `<src>独立承担。</src><tgt>When facing this situation, if we run into a problem, we should quickly report it to our supervisor or let them know about the current situation. Don't think you have to handle everything on your own.</tgt>` | 3029 |
| 10 | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | `<src>整体而言，</src><tgt><\|wait\|></tgt>` | 2043 |
| 11 | `<src>事业运就属凶。</src><tgt><\|wait\|></tgt>` | `<src>事业是相互署，</src><tgt><\|wait\|></tgt>` | 1896 |

---

### Test Example 16 / 60
- UID: JA_Xv3zO_K9SuU_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>そうです。</src><tgt><\|wait\|></tgt>` | `<src>そうです。</src><tgt><\|wait\|></tgt>` | 946 |
| 2 | `<src>そこで</src><tgt><\|wait\|></tgt>` | `<src>そこで</src><tgt><\|wait\|></tgt>` | 865 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1073 |
| 4 | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | `<src>テキという設備寺が</src><tgt><\|wait\|></tgt>` | 1520 |
| 5 | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | `<src>ありましたね。</src><tgt><\|wait\|></tgt>` | 1405 |
| 6 | `<src>で、</src><tgt><\|wait\|></tgt>` | `<src>で、</src><tgt><\|wait\|></tgt>` | 1535 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 592 |
| 8 | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | `<src>長井慶義氏の仕組み</src><tgt><\|wait\|></tgt>` | 1488 |
| 9 | `<src><\|wait\|></src><tgt>맞습니다. 거기 ' 테키' 라는 접미사가 있었죠.</tgt>` | `<src><\|wait\|></src><tgt>맞아요. 거기에는 테키라는 설비가 있었죠. 그리고</tgt>` | 1628 |
| 10 | `<src>は五経、</src><tgt><\|wait\|></tgt>` | `<src>は五コン、</src><tgt><\|wait\|></tgt>` | 1660 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1135 |
| 12 | `<src>設備寺、五比</src><tgt><\|wait\|></tgt>` | `<src>設備寺、五ビル、</src><tgt><\|wait\|></tgt>` | 2193 |
| 13 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src>す。</src><tgt><\|wait\|></tgt>` | 1891 |

---

### Test Example 17 / 60
- UID: JA_6YxG4VtOq3M_W000012
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | `<src>まあだんだんちょっと</src><tgt><\|wait\|></tgt>` | 1263 |
| 2 | `<src>距離が</src><tgt><\|wait\|></tgt>` | `<src>距離が</src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>離れてくるみたいな感じ、</src><tgt><\|wait\|></tgt>` | `<src>離れてくるみたいな感じで、</src><tgt><\|wait\|></tgt>` | 1848 |
| 4 | `<src>オシャレる方がやっぱ</src><tgt><\|wait\|></tgt>` | `<src>大将が、</src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>多いですね。</src><tgt><\|wait\|></tgt>` | `<src>大将が覚えてる方多いですね。</src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>開業したい方って</src><tgt><\|wait\|></tgt>` | `<src>海老押したい方って</src><tgt><\|wait\|></tgt>` | 888 |
| 7 | `<src>すごい</src><tgt><\|wait\|></tgt>` | `<src>すごい覚え越しきた</src><tgt><\|wait\|></tgt>` | 1552 |
| 8 | `<src>自己意識高いし、</src><tgt><\|wait\|></tgt>` | `<src>し、</src><tgt><\|wait\|></tgt>` | 1647 |
| 9 | `<src>自分で</src><tgt>嗯，感觉距离会慢慢拉开，确实很多人这么说。想创业的人自我意识都很强，而且</tgt>` | `<src>読み始めて</src><tgt>嗯，距离慢慢拉远，大将好像记住了很多人。想押虾的人，</tgt>` | 2022 |
| 10 | `<src>全部ちょっと次の投資</src><tgt><\|wait\|></tgt>` | `<src>と思ったり、</src><tgt><\|wait\|></tgt>` | 1154 |
| 11 | `<src>傾向が強いので、</src><tgt><\|wait\|></tgt>` | `<src>覚悟が強いので、</src><tgt><\|wait\|></tgt>` | 2193 |
| 12 | `<src>なので。</src><tgt><\|wait\|></tgt>` | `<src>なので。</src><tgt><\|wait\|></tgt>` | 1805 |

---

### Test Example 18 / 60
- UID: ZH_B00041_S00105_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 879 |
| 2 | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | `<src>如果在女高中生</src><tgt><\|wait\|></tgt>` | 1098 |
| 3 | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | `<src>与长相古怪的人</src><tgt><\|wait\|></tgt>` | 1817 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1214 |
| 5 | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | `<src>之间有着某种联系，</src><tgt><\|wait\|></tgt>` | 1161 |
| 6 | `<src>难道会是</src><tgt><\|wait\|></tgt>` | `<src>难道会使</src><tgt><\|wait\|></tgt>` | 1251 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1447 |
| 8 | `<src>从那天夜里开始的？</src><tgt><\|wait\|></tgt>` | `<src>从那天夜里开始的</src><tgt><\|wait\|></tgt>` | 1868 |
| 9 | `<src><\|wait\|></src><tgt>Was there some kind of connection between the high school girl and the odd- looking person? Could it have started that night?</tgt>` | `<src><\|wait\|></src><tgt>If there is some connection between a high school girl and someone with a strange appearance, could it be that</tgt>` | 2200 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1078 |
| 11 | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | `<src>杨子思绪</src><tgt><\|wait\|></tgt>` | 2252 |
| 12 | `<src>连篇。</src><tgt><\|wait\|></tgt>` | `<src>连篇？</src><tgt><\|wait\|></tgt>` | 1730 |

---

### Test Example 19 / 60
- UID: KO_GSM-N2PFBuE_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | `<src>이거 너무 </src><tgt><\|wait\|></tgt>` | 1059 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1072 |
| 3 | `<src>저열한 일일 수 있지만 </src><tgt><\|wait\|></tgt>` | `<src>저열한 일일 수도 있지만 </src><tgt><\|wait\|></tgt>` | 1825 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>진짜 보살 도요 </src><tgt><\|wait\|></tgt>` | 1525 |
| 5 | `<src>진짜 보살 도요. 아니 </src><tgt><\|wait\|></tgt>` | `<src>아니 </src><tgt><\|wait\|></tgt>` | 862 |
| 6 | `<src>자기 가 보살 인데 꾸밀 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>자기 가 보살 인데 꿈일 프로 </src><tgt><\|wait\|></tgt>` | 1422 |
| 7 | `<src>뭐 있고 </src><tgt><\|wait\|></tgt>` | `<src>아보이 고 </src><tgt><\|wait\|></tgt>` | 1510 |
| 8 | `<src>남한 테 보살 로 보일 필요 가 </src><tgt><\|wait\|></tgt>` | `<src>나만 </src><tgt><\|wait\|></tgt>` | 1698 |
| 9 | `<src>뭐 있어요. 우주 가 </src><tgt>これはすごく低俗なことかもしれないけど、本当の菩薩道なんだよね。いや、自分が菩薩なのに着飾る必要なんてある？他人に菩薩に見せる必要なんてある？宇宙が</tgt>` | `<src>보살 로 보일 프로 보이 서 </src><tgt>これはあまりにも低俗なことかもしれません。でも、本当に菩薩様です。いや、自分は菩薩なのに、夢の中の菩薩に見えるのは私だけ</tgt>` | 3005 |
| 10 | `<src>지금 나한테 </src><tgt><\|wait\|></tgt>` | `<src>우주 가 지금 나한테 </src><tgt><\|wait\|></tgt>` | 2208 |
| 11 | `<src>보살 이라는데. </src><tgt><\|wait\|></tgt>` | `<src>보살 이라는 거지. </src><tgt><\|wait\|></tgt>` | 1979 |

---

### Test Example 20 / 60
- UID: ZH_ShY5gaBM9MI_W000011
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>我当时</src><tgt><\|wait\|></tgt>` | `<src>我当时</src><tgt><\|wait\|></tgt>` | 1004 |
| 2 | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | `<src>一切正常，</src><tgt><\|wait\|></tgt>` | 1084 |
| 3 | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | `<src>活蹦乱跳，</src><tgt><\|wait\|></tgt>` | 1286 |
| 4 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1370 |
| 5 | `<src>坚持不开刀。</src><tgt><\|wait\|></tgt>` | `<src>所以坚持不起来，</src><tgt><\|wait\|></tgt>` | 1202 |
| 6 | `<src>期间</src><tgt><\|wait\|></tgt>` | `<src>期间大概有</src><tgt><\|wait\|></tgt>` | 1531 |
| 7 | `<src>大概有十位医生</src><tgt><\|wait\|></tgt>` | `<src>十位医生</src><tgt><\|wait\|></tgt>` | 1508 |
| 8 | `<src>来诊断，</src><tgt><\|wait\|></tgt>` | `<src>来审断，</src><tgt><\|wait\|></tgt>` | 1693 |
| 9 | `<src>一下敲腿，</src><tgt>I was perfectly fine at the time, jumping around, so I insisted on not having surgery. About ten doctors came to examine me during that period.</tgt>` | `<src>以下挑腿、</src><tgt>I was perfectly fine back then, full of energy, so I couldn't keep going. About ten doctors came to examine me. I had</tgt>` | 1886 |
| 10 | `<src>一下提腿，</src><tgt><\|wait\|></tgt>` | `<src>以下提腿、</src><tgt><\|wait\|></tgt>` | 686 |
| 11 | `<src>都没有问题。</src><tgt><\|wait\|></tgt>` | `<src>都没有问题，</src><tgt><\|wait\|></tgt>` | 999 |
| 12 | `<src>他们</src><tgt><\|wait\|></tgt>` | `<src>他们都很</src><tgt><\|wait\|></tgt>` | 2205 |
| 13 | `<src>都很疑惑的离开。</src><tgt><\|wait\|></tgt>` | `<src>疑惑不解来。</src><tgt><\|wait\|></tgt>` | 1753 |

---

### Test Example 21 / 60
- UID: EN_n_COVPwr54I_W000006
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>My name is </src><tgt><\|wait\|></tgt>` | `<src>My name is </src><tgt><\|wait\|></tgt>` | 1021 |
| 2 | `<src>Kerenath Dettig. </src><tgt><\|wait\|></tgt>` | `<src>Kiran Patel. </src><tgt><\|wait\|></tgt>` | 1089 |
| 3 | `<src>I am currently </src><tgt><\|wait\|></tgt>` | `<src>I am currently </src><tgt><\|wait\|></tgt>` | 1485 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>studying IEEE Baxter </src><tgt><\|wait\|></tgt>` | 1339 |
| 5 | `<src>studying a Bachelor of Finance </src><tgt><\|wait\|></tgt>` | `<src>Finance </src><tgt><\|wait\|></tgt>` | 996 |
| 6 | `<src>and a Bachelor of Psychology </src><tgt><\|wait\|></tgt>` | `<src>and a Ph.D. of Psychology. </src><tgt><\|wait\|></tgt>` | 1714 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1466 |
| 8 | `<src>here at the ANU, </src><tgt><\|wait\|></tgt>` | `<src>Here at the IEEE N </src><tgt><\|wait\|></tgt>` | 1766 |
| 9 | `<src><\|wait\|></src><tgt>제 이름은 케레나스 데티그입니다. 저는 현재 호주국립대학교( ANU) 에서 금융학과 심리학 학사 과정을</tgt>` | `<src><\|wait\|></src><tgt>제 이름은 키란 파텔입니다. 현재 IEEE 금융과 심리학 박사 과정을 밟고 있습니다. IEEE</tgt>` | 2292 |
| 10 | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | `<src>and in the future, I want to go into </src><tgt><\|wait\|></tgt>` | 1205 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | 2061 |
| 12 | `<src>corporate consultancy. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1744 |

---

### Test Example 22 / 60
- UID: EN_B00016_S00472_W000046
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>All right, </src><tgt><\|wait\|></tgt>` | `<src>All right. </src><tgt><\|wait\|></tgt>` | 1248 |
| 2 | `<src>and then </src><tgt><\|wait\|></tgt>` | `<src>And then, </src><tgt><\|wait\|></tgt>` | 1107 |
| 3 | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | `<src>after these examples, </src><tgt><\|wait\|></tgt>` | 1406 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1314 |
| 5 | `<src>the instruction </src><tgt><\|wait\|></tgt>` | `<src>the instruction </src><tgt><\|wait\|></tgt>` | 1108 |
| 6 | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | `<src>tells us to use </src><tgt><\|wait\|></tgt>` | 1620 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1468 |
| 8 | `<src>actually </src><tgt><\|wait\|></tgt>` | `<src>actually </src><tgt><\|wait\|></tgt>` | 1787 |
| 9 | `<src><\|wait\|></src><tgt>好的，然后在这些例子之后，说明告诉我们</tgt>` | `<src><\|wait\|></src><tgt>好的。然后，在这些例子之后，说明书告诉我们，实际上</tgt>` | 1864 |
| 10 | `<src>these values. So </src><tgt><\|wait\|></tgt>` | `<src>these values. So </src><tgt><\|wait\|></tgt>` | 940 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1683 |
| 12 | `<src>this game dot scored array. </src><tgt><\|wait\|></tgt>` | `<src>this game dot scored array, </src><tgt><\|wait\|></tgt>` | 1315 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1712 |

---

### Test Example 23 / 60
- UID: JA_055Z9Ti9z9Y_W000045
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>これがギア</src><tgt><\|wait\|></tgt>` | `<src>これが</src><tgt><\|wait\|></tgt>` | 1196 |
| 2 | `<src>です。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 861 |
| 3 | `<src>ギアが</src><tgt><\|wait\|></tgt>` | `<src>ギアです。ギアが</src><tgt><\|wait\|></tgt>` | 1114 |
| 4 | `<src>緩むと芯が</src><tgt><\|wait\|></tgt>` | `<src>緩むと、シンガーが</src><tgt><\|wait\|></tgt>` | 1736 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>上げ下げできなくなってしまう</src><tgt><\|wait\|></tgt>` | 1237 |
| 6 | `<src>上げ下げできなくなってしまうので、</src><tgt><\|wait\|></tgt>` | `<src>ので、</src><tgt><\|wait\|></tgt>` | 1531 |
| 7 | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | `<src>ギアの先に</src><tgt><\|wait\|></tgt>` | 1479 |
| 8 | `<src>役ねじの</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1539 |
| 9 | `<src>ナットが</src><tgt>이것이 기어입니다. 기어가 느슨해지면 심이 올라가거나 내려가지 않게 됩니다. 그래서 기어 끝에 역나사 너트가</tgt>` | `<src>逆ネジのナットが</src><tgt>이것이 기어입니다. 기어가 헐거워지면 싱거가 위아래로 움직이지 않게 되니까, 기어 끝에 역나사 너트가</tgt>` | 2275 |
| 10 | `<src>ついているっていうことです</src><tgt><\|wait\|></tgt>` | `<src>付いているっていうこと</src><tgt><\|wait\|></tgt>` | 1056 |
| 11 | `<src>ね。</src><tgt><\|wait\|></tgt>` | `<src>ですね。</src><tgt><\|wait\|></tgt>` | 1762 |
| 12 | `<src>はい、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1141 |
| 13 | `<src>分解完了。</src><tgt><\|wait\|></tgt>` | `<src>ハイブンブレーキを。</src><tgt><\|wait\|></tgt>` | 1646 |

---

### Test Example 24 / 60
- UID: EN_B00016_S01082_W000024
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 935 |
| 2 | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | `<src>Like a stretched rubber band, </src><tgt><\|wait\|></tgt>` | 1194 |
| 3 | `<src>chemical bonds </src><tgt><\|wait\|></tgt>` | `<src>chemical bonds also store </src><tgt><\|wait\|></tgt>` | 1695 |
| 4 | `<src>also store energy, </src><tgt><\|wait\|></tgt>` | `<src>energy. And when those </src><tgt><\|wait\|></tgt>` | 1430 |
| 5 | `<src>and when those bonds are broken, </src><tgt><\|wait\|></tgt>` | `<src>bonds are broken, </src><tgt><\|wait\|></tgt>` | 1200 |
| 6 | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | `<src>that potential energy </src><tgt><\|wait\|></tgt>` | 1064 |
| 7 | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | `<src>gets converted to </src><tgt><\|wait\|></tgt>` | 1393 |
| 8 | `<src>other types of energy, </src><tgt><\|wait\|></tgt>` | `<src>other types of energy, like </src><tgt><\|wait\|></tgt>` | 1867 |
| 9 | `<src>like heat or light, </src><tgt>팽팽하게 당겨진 고무줄처럼 화학 결합도 에너지를 저장합니다. 이 결합이 끊어지면 잠재된 에너지는 열이나 빛과 같은 다른 형태의 에너지로 전환됩니다.</tgt>` | `<src>heat or light. </src><tgt>늘어난 고무줄처럼 화학 결합도 에너지를 저장합니다. 그리고 그 결합이 끊어지면, 그 잠재 에너지는 열이나 빛 같은 다른 에너지 형태로 변환됩니다.</tgt>` | 3084 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Or gets </src><tgt><\|wait\|></tgt>` | 1946 |
| 11 | `<src>or gets used to make </src><tgt><\|wait\|></tgt>` | `<src>used to make </src><tgt><\|wait\|></tgt>` | 1291 |
| 12 | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | `<src>different bonds. </src><tgt><\|wait\|></tgt>` | 1139 |

---

### Test Example 25 / 60
- UID: JA_7sVJ5Fmygak_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>あの</src><tgt><\|wait\|></tgt>` | 921 |
| 2 | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | `<src>映画でですね、</src><tgt><\|wait\|></tgt>` | 1089 |
| 3 | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | `<src>いろんな場面で</src><tgt><\|wait\|></tgt>` | 1643 |
| 4 | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>映画生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1829 |
| 5 | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | `<src>調べるときに、</src><tgt><\|wait\|></tgt>` | 1362 |
| 6 | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | `<src>まあ映画の卵を調べる</src><tgt><\|wait\|></tgt>` | 833 |
| 7 | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | `<src>ことで、あの</src><tgt><\|wait\|></tgt>` | 1496 |
| 8 | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | `<src>その生息かどうかっていうのを</src><tgt><\|wait\|></tgt>` | 1756 |
| 9 | `<src>保証する、生息である</src><tgt>For the ' ei' (ray), in various situations, when checking whether they are inhabiting an area, you investigate their eggs. This guarantees their presence—</tgt>` | `<src>保証する、生息である</src><tgt>In movies, when you're checking if a movie is actually living in a certain area, you can use things like checking for movie eggs to confirm that it's</tgt>` | 2829 |
| 10 | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | `<src>ことを保証する</src><tgt><\|wait\|></tgt>` | 1973 |
| 11 | `<src>といったような</src><tgt><\|wait\|></tgt>` | `<src>といったような</src><tgt><\|wait\|></tgt>` | 989 |
| 12 | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | `<src>使い方をされます。</src><tgt><\|wait\|></tgt>` | 1565 |

---

### Test Example 26 / 60
- UID: ZH_UJBZXO0vtl8_W000084
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | `<src>这一张的部分呢，</src><tgt><\|wait\|></tgt>` | 917 |
| 2 | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的是</src><tgt><\|wait\|></tgt>` | 1039 |
| 3 | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | `<src>一个在钓鱼</src><tgt><\|wait\|></tgt>` | 1514 |
| 4 | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | `<src>的人，但是</src><tgt><\|wait\|></tgt>` | 1232 |
| 5 | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | `<src>它是属于逆向的，</src><tgt><\|wait\|></tgt>` | 1253 |
| 6 | `<src>所以</src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 1365 |
| 7 | `<src>通常逢到这样的一个状况的</src><tgt><\|wait\|></tgt>` | `<src>通常我们这样一个状况</src><tgt><\|wait\|></tgt>` | 1481 |
| 8 | `<src>时候，就要去</src><tgt><\|wait\|></tgt>` | `<src>的视频就要去</src><tgt><\|wait\|></tgt>` | 1630 |
| 9 | `<src>特别注意，</src><tgt>이 부분에서는 낚시하는 사람을 볼 수 있는데요, 이게 역방향이에요. 그래서 보통 이런 상황을 만나게 되면,</tgt>` | `<src>特别注意，</src><tgt>이 부분은 낚시를 하는 사람인데, 역방향으로 되어 있어요. 그래서 이런 상황의 영상은 특히 주의해야 해요.</tgt>` | 1855 |
| 10 | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | `<src>是它能不能够</src><tgt><\|wait\|></tgt>` | 475 |
| 11 | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | `<src>钓到鱼，</src><tgt><\|wait\|></tgt>` | 1166 |
| 12 | `<src>它钓不到鱼</src><tgt><\|wait\|></tgt>` | `<src>它钓不到鱼，</src><tgt><\|wait\|></tgt>` | 2155 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>它也</src><tgt><\|wait\|></tgt>` | 1837 |
| 14 | `<src>的意思哦。</src><tgt><\|wait\|></tgt>` | `<src>意思了。</src><tgt><\|wait\|></tgt>` | 828 |

---

### Test Example 27 / 60
- UID: ZH_ShY5gaBM9MI_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>让我</src><tgt><\|wait\|></tgt>` | `<src>让我</src><tgt><\|wait\|></tgt>` | 791 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1099 |
| 3 | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | `<src>回到我生活</src><tgt><\|wait\|></tgt>` | 1603 |
| 4 | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | `<src>的一个轨道哈，</src><tgt><\|wait\|></tgt>` | 1449 |
| 5 | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | `<src>让我能够哈，</src><tgt><\|wait\|></tgt>` | 1043 |
| 6 | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | `<src>在他下班的时候，</src><tgt><\|wait\|></tgt>` | 1430 |
| 7 | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | `<src>在做热汤</src><tgt><\|wait\|></tgt>` | 1564 |
| 8 | `<src>热饭给他吃。真的，</src><tgt><\|wait\|></tgt>` | `<src>热饭给他吃，</src><tgt><\|wait\|></tgt>` | 1719 |
| 9 | `<src><\|wait\|></src><tgt>제 삶의 궤도로 돌아가고 싶어요. 그 사람이 퇴근했을 때 따뜻한 국과 밥을 차려줄 수 있도록요. 정말,</tgt>` | `<src>就这么了。</src><tgt>제 삶의 궤도로 돌아가게 해 주세요. 퇴근하고 오실 때 따뜻한 국이나 밥을 끓여 드리는 것, 그게 다예요.</tgt>` | 3028 |
| 10 | `<src>我当时悲痛的时候，只有这么一个</src><tgt><\|wait\|></tgt>` | `<src>我只是备餐的时候，</src><tgt><\|wait\|></tgt>` | 2142 |
| 11 | `<src>小小的愿望</src><tgt><\|wait\|></tgt>` | `<src>就一个小小的愿望哈，</src><tgt><\|wait\|></tgt>` | 2018 |
| 12 | `<src>哈。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1274 |

---

### Test Example 28 / 60
- UID: KO_E5GX5U4qdXY_W000004
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 965 |
| 2 | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | `<src>바나듐이라든가 이것 들은 거진 </src><tgt><\|wait\|></tgt>` | 1559 |
| 3 | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | `<src>인슐린과 </src><tgt><\|wait\|></tgt>` | 1324 |
| 4 | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | `<src>이제 거진 </src><tgt><\|wait\|></tgt>` | 1234 |
| 5 | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | `<src>유사 한 작용 이 </src><tgt><\|wait\|></tgt>` | 1271 |
| 6 | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | `<src>일어날 정도 로 </src><tgt><\|wait\|></tgt>` | 1233 |
| 7 | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | `<src>굉장히 아주 </src><tgt><\|wait\|></tgt>` | 1452 |
| 8 | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | `<src>당뇨 미네랄이다 </src><tgt><\|wait\|></tgt>` | 1811 |
| 9 | `<src>이렇게 </src><tgt>Things like vanadium have an effect almost like insulin— to the point where</tgt>` | `<src>기계 가 </src><tgt>Vadium and these things are almost as effective as insulin. They are, in a sense, diabetes minerals.</tgt>` | 2210 |
| 10 | `<src>이야기 할 정도 의 </src><tgt><\|wait\|></tgt>` | `<src>열 정도 의 </src><tgt><\|wait\|></tgt>` | 1009 |
| 11 | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | `<src>이제 그런 거죠. 이제 </src><tgt><\|wait\|></tgt>` | 2286 |
| 12 | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | `<src>그거 에다가 </src><tgt><\|wait\|></tgt>` | 1762 |
| 13 | `<src>아연. </src><tgt><\|wait\|></tgt>` | `<src>아연. </src><tgt><\|wait\|></tgt>` | 1434 |

---

### Test Example 29 / 60
- UID: ZH_P3DbOZsH800_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | `<src>第二个就是</src><tgt><\|wait\|></tgt>` | 972 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1083 |
| 3 | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | `<src>选择二级市场，哎，</src><tgt><\|wait\|></tgt>` | 1959 |
| 4 | `<src>服务</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1218 |
| 5 | `<src>在一级一线</src><tgt><\|wait\|></tgt>` | `<src>如果在一级一项</src><tgt><\|wait\|></tgt>` | 938 |
| 6 | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | `<src>拼杀的大牛们，</src><tgt><\|wait\|></tgt>` | 1453 |
| 7 | `<src>比如说，呃，</src><tgt><\|wait\|></tgt>` | `<src>比如说</src><tgt><\|wait\|></tgt>` | 1369 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>在做</src><tgt><\|wait\|></tgt>` | 1787 |
| 9 | `<src>在做微信公众号十几年，你会</src><tgt>2つ目は、二次市場を選ぶことです。つまり、最前線で戦っている大物たちをサポートするのです。例えば、微信公式アカウントを十数年やっています。すると、</tgt>` | `<src>微信公众号十几年，</src><tgt>2つ目は、セカンダリーマーケットを選ぶことです。ああ、もしプライマリーマーケットで激しい競争をしている大口トレーダーがいれば、例えばWeChat公式アカウントを10年以上運営している人なら、</tgt>` | 2941 |
| 10 | `<src>发现</src><tgt><\|wait\|></tgt>` | `<src>你会发现</src><tgt><\|wait\|></tgt>` | 1795 |
| 11 | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | `<src>给微信公众号评分</src><tgt><\|wait\|></tgt>` | 1233 |
| 12 | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | `<src>的新榜反而</src><tgt><\|wait\|></tgt>` | 1568 |
| 13 | `<src>火了。</src><tgt><\|wait\|></tgt>` | `<src>火了。</src><tgt><\|wait\|></tgt>` | 1450 |

---

### Test Example 30 / 60
- UID: EN_B00016_S01462_W000036
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | `<src>Or, or if you </src><tgt><\|wait\|></tgt>` | 1063 |
| 2 | `<src>have to produce </src><tgt><\|wait\|></tgt>` | `<src>have to produce </src><tgt><\|wait\|></tgt>` | 1055 |
| 3 | `<src>something written, </src><tgt><\|wait\|></tgt>` | `<src>something written, </src><tgt><\|wait\|></tgt>` | 1404 |
| 4 | `<src>write a text, </src><tgt><\|wait\|></tgt>` | `<src>write a text, </src><tgt><\|wait\|></tgt>` | 1327 |
| 5 | `<src>you realize that </src><tgt><\|wait\|></tgt>` | `<src>you realize that </src><tgt><\|wait\|></tgt>` | 1106 |
| 6 | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | `<src>you don't even know how </src><tgt><\|wait\|></tgt>` | 1627 |
| 7 | `<src>to spell </src><tgt><\|wait\|></tgt>` | `<src>to spell </src><tgt><\|wait\|></tgt>` | 1435 |
| 8 | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | `<src>the words. Like, oh, </src><tgt><\|wait\|></tgt>` | 1932 |
| 9 | `<src>is this word </src><tgt>それか、何か文章を書かなきゃいけないとき、テキストを作るときに、単語の綴りさえ分からないってことに気づくんですよ。例えば、あれ、この単語って、</tgt>` | `<src>is this word </src><tgt>あるいは、あるいは何か文章を書く必要があるとき、文字を書くとき、そもそも単語の綴りさえ分からなくて、「あ、この単語は</tgt>` | 2857 |
| 10 | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | `<src>spelled with a double </src><tgt><\|wait\|></tgt>` | 1998 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>p, </src><tgt><\|wait\|></tgt>` | 977 |
| 12 | `<src>p, double lam? I don't </src><tgt><\|wait\|></tgt>` | `<src>double l, and I don't </src><tgt><\|wait\|></tgt>` | 1668 |
| 13 | `<src>know. </src><tgt><\|wait\|></tgt>` | `<src>know. </src><tgt><\|wait\|></tgt>` | 1531 |

---

### Test Example 31 / 60
- UID: ZH_RuIL-xmPqIY_W000179
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | 1109 |
| 2 | `<src>要提醒大家，</src><tgt><\|wait\|></tgt>` | `<src>在这个</src><tgt><\|wait\|></tgt>` | 1055 |
| 3 | `<src>在这个罗马呢</src><tgt><\|wait\|></tgt>` | `<src>罗马呢，</src><tgt><\|wait\|></tgt>` | 1650 |
| 4 | `<src>不是一天造成的，</src><tgt><\|wait\|></tgt>` | `<src>不是意味着造成了</src><tgt><\|wait\|></tgt>` | 1437 |
| 5 | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | `<src>所以呢，</src><tgt><\|wait\|></tgt>` | 934 |
| 6 | `<src>你现在</src><tgt><\|wait\|></tgt>` | `<src>你现在</src><tgt><\|wait\|></tgt>` | 1379 |
| 7 | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | `<src>所面临的一些</src><tgt><\|wait\|></tgt>` | 1530 |
| 8 | `<src>危机啊，跟风险</src><tgt><\|wait\|></tgt>` | `<src>遗迹啊、</src><tgt><\|wait\|></tgt>` | 1839 |
| 9 | `<src>也不可能是</src><tgt>皆さんに言っておきたいんですが、ローマは一日にして成らずと言いますよね。だから、今皆さんが直面している危機やリスクも、</tgt>` | `<src>跟风景，</src><tgt>皆さんに注意していただきたいのですが、このローマは、</tgt>` | 1917 |
| 10 | `<src>一夕之间就</src><tgt><\|wait\|></tgt>` | `<src>也不可能是你历史之间</src><tgt><\|wait\|></tgt>` | 1207 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1973 |
| 12 | `<src>演变出来的，</src><tgt><\|wait\|></tgt>` | `<src>就演变出来</src><tgt><\|wait\|></tgt>` | 1710 |
| 13 | `<src>因此会建议</src><tgt><\|wait\|></tgt>` | `<src>的因此会建议</src><tgt><\|wait\|></tgt>` | 778 |
| 14 | `<src>属鸡的朋友呢。</src><tgt><\|wait\|></tgt>` | `<src>优质的朋友呢。</src><tgt><\|wait\|></tgt>` | 1552 |

---

### Test Example 32 / 60
- UID: EN_nd3VSjWd148_W000003
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1225 |
| 2 | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | `<src>The meaning of </src><tgt><\|wait\|></tgt>` | 1058 |
| 3 | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | `<src>the 19th Amendment, </src><tgt><\|wait\|></tgt>` | 2074 |
| 4 | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | `<src>and to explore its </src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | `<src>history as a guide </src><tgt><\|wait\|></tgt>` | 1246 |
| 6 | `<src>to how political </src><tgt><\|wait\|></tgt>` | `<src>to how political </src><tgt><\|wait\|></tgt>` | 848 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>change can happen </src><tgt><\|wait\|></tgt>` | `<src>change can happen </src><tgt><\|wait\|></tgt>` | 1748 |
| 9 | `<src>in the United States. </src><tgt>수정헌법 제19조의 의미를 살펴보고, 그 역사를 탐구하는 것입니다. 이는 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침이 됩니다.</tgt>` | `<src>in the United States. </src><tgt>제19조 수정헌법의 의미를 살펴보고, 미국에서 정치적 변화가 어떻게 일어날 수 있는지에 대한 지침서로서 그 역사를 탐구해 보겠습니다.</tgt>` | 2998 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2003 |
| 11 | `<src>The meanings </src><tgt><\|wait\|></tgt>` | `<src>The meanings </src><tgt><\|wait\|></tgt>` | 1904 |
| 12 | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | `<src>of the amendment, of course, are </src><tgt><\|wait\|></tgt>` | 878 |
| 13 | `<src>myriad. </src><tgt><\|wait\|></tgt>` | `<src>myriad. </src><tgt><\|wait\|></tgt>` | 1562 |

---

### Test Example 33 / 60
- UID: KO_B00001_S08942_W000000
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | `<src>그중 에서 </src><tgt><\|wait\|></tgt>` | 863 |
| 2 | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | `<src>150만 개가 종업원 수 </src><tgt><\|wait\|></tgt>` | 1429 |
| 3 | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | `<src>10명 미만 으로 </src><tgt><\|wait\|></tgt>` | 1675 |
| 4 | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | `<src>아주 작은 기업 들이 </src><tgt><\|wait\|></tgt>` | 1503 |
| 5 | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | `<src>많았습니다. </src><tgt><\|wait\|></tgt>` | 1266 |
| 6 | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | `<src>일반 적으로는 </src><tgt><\|wait\|></tgt>` | 772 |
| 7 | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | `<src>작은 업체 들은 성장 하거나 </src><tgt><\|wait\|></tgt>` | 1777 |
| 8 | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | `<src>혹은 폐업 할 길을 </src><tgt><\|wait\|></tgt>` | 1528 |
| 9 | `<src>걷게 되는데 </src><tgt>そのうち150万社が、従業員数10人未満の非常に小さな企業でした。一般的に小規模な企業は成長するか廃業するかの道を歩むものですが、</tgt>` | `<src>걷게 되는데 </src><tgt>そのうち150万件は従業員数10人未満の非常に小さな企業が多くありました。一般的に小さな企業は成長するか、あるいは廃業する道を選びます。しかし、</tgt>` | 2981 |
| 10 | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | `<src>일본 의 소기업들은 </src><tgt><\|wait\|></tgt>` | 2121 |
| 11 | `<src>성장 도 폐업 도 </src><tgt><\|wait\|></tgt>` | `<src>성장 도 </src><tgt><\|wait\|></tgt>` | 1839 |
| 12 | `<src>하지 않는 현상 들을 </src><tgt><\|wait\|></tgt>` | `<src>폐업 도 하지 않는 </src><tgt><\|wait\|></tgt>` | 950 |
| 13 | `<src>보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | `<src>현상 들만 보이 게 된 거죠. </src><tgt><\|wait\|></tgt>` | 1540 |

---

### Test Example 34 / 60
- UID: JA_1u7y1Gam6ly_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>授業</src><tgt><\|wait\|></tgt>` | 1040 |
| 2 | `<src>十一二手とか</src><tgt><\|wait\|></tgt>` | `<src>一日一日の</src><tgt><\|wait\|></tgt>` | 930 |
| 3 | `<src>じゃないですか。おそらく</src><tgt><\|wait\|></tgt>` | `<src>予定だった。</src><tgt><\|wait\|></tgt>` | 1024 |
| 4 | `<src>十秒で。</src><tgt><\|wait\|></tgt>` | `<src>おそらく十秒で</src><tgt><\|wait\|></tgt>` | 1434 |
| 5 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1403 |
| 6 | `<src>一秒に</src><tgt><\|wait\|></tgt>` | `<src>一日一日に</src><tgt><\|wait\|></tgt>` | 1272 |
| 7 | `<src>一定強ぐらいの</src><tgt><\|wait\|></tgt>` | `<src>一秒ぐらいの</src><tgt><\|wait\|></tgt>` | 657 |
| 8 | `<src>計算ですか</src><tgt><\|wait\|></tgt>` | `<src>時間ですかね。</src><tgt><\|wait\|></tgt>` | 1517 |
| 9 | `<src>ね。</src><tgt>大概十一二手吧。差不多十秒。一秒一手多一点这样算。</tgt>` | `<src><\|wait\|></src><tgt>原计划是每天一次。大概十秒，嗯，每天一次，一秒左右吧。</tgt>` | 1899 |
| 10 | `<src>でなんか</src><tgt><\|wait\|></tgt>` | `<src>でなんか</src><tgt><\|wait\|></tgt>` | 1621 |
| 11 | `<src>おそらく</src><tgt><\|wait\|></tgt>` | `<src>おそらくよく</src><tgt><\|wait\|></tgt>` | 1066 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>十一日に</src><tgt><\|wait\|></tgt>` | 1799 |
| 13 | `<src>十一二手で</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1199 |
| 14 | `<src>あの</src><tgt><\|wait\|></tgt>` | `<src>であの</src><tgt><\|wait\|></tgt>` | 1525 |
| 15 | `<src>宮馬とかが</src><tgt><\|wait\|></tgt>` | `<src>宮川とかが</src><tgt><\|wait\|></tgt>` | 1522 |
| 16 | `<src>あるから。</src><tgt><\|wait\|></tgt>` | `<src>だから。</src><tgt><\|wait\|></tgt>` | 677 |

---

### Test Example 35 / 60
- UID: KO_GFCl_rbj8jM_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 856 |
| 2 | `<src>HTML이라고 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1070 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>HTML이라고 하는 </src><tgt><\|wait\|></tgt>` | 1634 |
| 4 | `<src>하는 컴퓨터 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1236 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 도 이해 할 수 있고 </src><tgt><\|wait\|></tgt>` | 1613 |
| 6 | `<src>있고 사람 도 이해 할 수 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1065 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>사람 도 이해 할 수 있는 </src><tgt><\|wait\|></tgt>` | 1613 |
| 8 | `<src>있는 컴퓨터 언어 의 </src><tgt><\|wait\|></tgt>` | `<src>컴퓨터 언어 에 </src><tgt><\|wait\|></tgt>` | 1732 |
| 9 | `<src>문법 에 </src><tgt>HTML是一种计算机语言，计算机能理解，人类也能理解。</tgt>` | `<src>문법 에 </src><tgt>HTML这种计算机语言，</tgt>` | 1763 |
| 10 | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>맞게 우리 가 이제 </src><tgt><\|wait\|></tgt>` | 1083 |
| 11 | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | `<src>코드 를 작성 해야 </src><tgt><\|wait\|></tgt>` | 2033 |
| 12 | `<src>되는데 </src><tgt><\|wait\|></tgt>` | `<src>되는데 </src><tgt><\|wait\|></tgt>` | 923 |
| 13 | `<src>그 코드 를 작성 하는 </src><tgt><\|wait\|></tgt>` | `<src>그 코드 를 </src><tgt><\|wait\|></tgt>` | 1531 |
| 14 | `<src>프로그램 이 </src><tgt><\|wait\|></tgt>` | `<src>작성 하는 프로그램 이 </src><tgt><\|wait\|></tgt>` | 1433 |
| 15 | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | `<src>필요 합니다. </src><tgt><\|wait\|></tgt>` | 821 |

---

### Test Example 36 / 60
- UID: KO_ErZ6Q3-uZb8_W000007
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>어 </src><tgt><\|wait\|></tgt>` | `<src>어 </src><tgt><\|wait\|></tgt>` | 1170 |
| 2 | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | `<src>어떻게 보면 </src><tgt><\|wait\|></tgt>` | 932 |
| 3 | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | `<src>가장 20대를 </src><tgt><\|wait\|></tgt>` | 1077 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>함께 한 </src><tgt><\|wait\|></tgt>` | 1381 |
| 5 | `<src>함께 한 동생 이자 </src><tgt><\|wait\|></tgt>` | `<src>동생 이자 </src><tgt><\|wait\|></tgt>` | 1508 |
| 6 | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | `<src>그래도 가족 </src><tgt><\|wait\|></tgt>` | 1561 |
| 7 | `<src>같은 동생 이잖아 </src><tgt><\|wait\|></tgt>` | `<src>같은 동생 이잖아. </src><tgt><\|wait\|></tgt>` | 1528 |
| 8 | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | `<src>그러니까 </src><tgt><\|wait\|></tgt>` | 1612 |
| 9 | `<src><\|wait\|></src><tgt>怎么说呢，他算是陪我度过最多20岁时光的弟弟，也是像家人一样的弟弟。所以</tgt>` | `<src><\|wait\|></src><tgt>嗯，怎么说呢，他也是最年轻的，和二十年代的人一起长大的，也是家人一样的弟弟。所以</tgt>` | 1841 |
| 10 | `<src>책임감 보다는 </src><tgt><\|wait\|></tgt>` | `<src>최근 감사 모다는 </src><tgt><\|wait\|></tgt>` | 550 |
| 11 | `<src>조금 </src><tgt><\|wait\|></tgt>` | `<src>조금 </src><tgt><\|wait\|></tgt>` | 1103 |
| 12 | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | `<src>자기 스스로 </src><tgt><\|wait\|></tgt>` | 2012 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>좀 </src><tgt><\|wait\|></tgt>` | 1839 |
| 14 | `<src>좀 많은 것을 </src><tgt><\|wait\|></tgt>` | `<src>많은 거 </src><tgt><\|wait\|></tgt>` | 826 |
| 15 | `<src>내려놓 고 </src><tgt><\|wait\|></tgt>` | `<src>내려 놓고 </src><tgt><\|wait\|></tgt>` | 1551 |
| 16 | `<src>행복 했으면 좋겠다. </src><tgt><\|wait\|></tgt>` | `<src>행복 했습니다는 </src><tgt><\|wait\|></tgt>` | 656 |

---

### Test Example 37 / 60
- UID: ZH_UJBZXO0vtl8_W000131
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>达到了一个</src><tgt><\|wait\|></tgt>` | 808 |
| 2 | `<src>达到了一个甜头，那</src><tgt><\|wait\|></tgt>` | `<src>甜头，那</src><tgt><\|wait\|></tgt>` | 1115 |
| 3 | `<src>如果你</src><tgt><\|wait\|></tgt>` | `<src>如果你</src><tgt><\|wait\|></tgt>` | 1284 |
| 4 | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | `<src>达到了甜头之后，</src><tgt><\|wait\|></tgt>` | 1448 |
| 5 | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | `<src>请你务必就要</src><tgt><\|wait\|></tgt>` | 1237 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1476 |
| 7 | `<src>先守住，</src><tgt><\|wait\|></tgt>` | `<src>先守住，</src><tgt><\|wait\|></tgt>` | 1457 |
| 8 | `<src>不要想说，哎，那我再</src><tgt><\|wait\|></tgt>` | `<src>不要想说，哎，</src><tgt><\|wait\|></tgt>` | 1915 |
| 9 | `<src><\|wait\|></src><tgt>うまくいったなと思ったらね。その時は必ず利益を確保してください。</tgt>` | `<src>那我再继续操作，</src><tgt>良いところまで来ましたね。もし良いところまで来たら、まずはしっかり守りましょう。そうして「あ、じゃあまた操作しよう」なんて考えないでください。</tgt>` | 3027 |
| 10 | `<src>继续操作下去哦。</src><tgt><\|wait\|></tgt>` | `<src>下去哦，</src><tgt><\|wait\|></tgt>` | 2124 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1972 |
| 12 | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | `<src>为什么会这么讲？</src><tgt><\|wait\|></tgt>` | 1009 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>因为呢，</src><tgt><\|wait\|></tgt>` | 1268 |
| 14 | `<src>因为呢。</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 930 |

---

### Test Example 38 / 60
- UID: EN_ndiOC6coCI0_W000005
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | `<src>Nothing new. </src><tgt><\|wait\|></tgt>` | 1039 |
| 2 | `<src>There were </src><tgt><\|wait\|></tgt>` | `<src>There were </src><tgt><\|wait\|></tgt>` | 1047 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1430 |
| 4 | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | `<src>such interfaces before, </src><tgt><\|wait\|></tgt>` | 1334 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1129 |
| 6 | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | `<src>netfilter, TC. </src><tgt><\|wait\|></tgt>` | 1574 |
| 7 | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | `<src>Yeah, so </src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src>this is just </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1800 |
| 9 | `<src>one another place </src><tgt>没什么新鲜的。以前就有过这样的接口，比如netfilter和 TC。所以这只是另一个</tgt>` | `<src>this is just one another place </src><tgt>没什么新奇的。以前也有过这样的接口，比如netfilter、TC。嗯，所以这只是</tgt>` | 2314 |
| 10 | `<src>to look at. </src><tgt><\|wait\|></tgt>` | `<src>to look at. </src><tgt><\|wait\|></tgt>` | 1049 |
| 11 | `<src>But </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 2213 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>But </src><tgt><\|wait\|></tgt>` | 1663 |
| 13 | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | `<src>developers or engineers </src><tgt><\|wait\|></tgt>` | 954 |
| 14 | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | `<src>working on BugRepo </src><tgt><\|wait\|></tgt>` | 1339 |
| 15 | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | `<src>should be aware of that. </src><tgt><\|wait\|></tgt>` | 963 |

---

### Test Example 39 / 60
- UID: ZH_B00021_S03098_W000013
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1096 |
| 2 | `<src>揣摩或感知对手</src><tgt><\|wait\|></tgt>` | `<src>揣摩或感觉对手</src><tgt><\|wait\|></tgt>` | 1096 |
| 3 | `<src>的感情或</src><tgt><\|wait\|></tgt>` | `<src>的感情或</src><tgt><\|wait\|></tgt>` | 1212 |
| 4 | `<src>真实意图的，</src><tgt><\|wait\|></tgt>` | `<src>真实意图的。</src><tgt><\|wait\|></tgt>` | 1492 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1151 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>很多是</src><tgt><\|wait\|></tgt>` | 1504 |
| 7 | `<src>很多时候经常</src><tgt><\|wait\|></tgt>` | `<src>好经常</src><tgt><\|wait\|></tgt>` | 1471 |
| 8 | `<src>会听到人们</src><tgt><\|wait\|></tgt>` | `<src>会听到人们这样说。</src><tgt><\|wait\|></tgt>` | 1533 |
| 9 | `<src>这样说：“</src><tgt>相手の感情や本当の意図を察したり推し量ったりするとき、よく耳にするのが</tgt>` | `<src><\|wait\|></src><tgt>相手の感情や本当の意図を推し量ったり感じ取ったりすることです。よく耳にするのは、</tgt>` | 1558 |
| 10 | `<src>你们看，</src><tgt><\|wait\|></tgt>` | `<src>你们看，</src><tgt><\|wait\|></tgt>` | 748 |
| 11 | `<src>这个人</src><tgt><\|wait\|></tgt>` | `<src>这个人</src><tgt><\|wait\|></tgt>` | 1066 |
| 12 | `<src>又在说谎了，</src><tgt><\|wait\|></tgt>` | `<src>又在说谎了。</src><tgt><\|wait\|></tgt>` | 2107 |
| 13 | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | `<src>他的眼睛</src><tgt><\|wait\|></tgt>` | 1287 |
| 14 | `<src>已经说明了一切。”</src><tgt><\|wait\|></tgt>` | `<src>已经说明了一切。</src><tgt><\|wait\|></tgt>` | 1220 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1618 |
| 16 | `<src>也就是说。</src><tgt><\|wait\|></tgt>` | `<src>也就是</src><tgt><\|wait\|></tgt>` | 634 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>说。</src><tgt><\|wait\|></tgt>` | 730 |

---

### Test Example 40 / 60
- UID: KO_B00002_S01182_W000002
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | `<src>너희 도 </src><tgt><\|wait\|></tgt>` | 922 |
| 2 | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | `<src>알거니와 너희 가 </src><tgt><\|wait\|></tgt>` | 1223 |
| 3 | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | `<src>이방인으로 </src><tgt><\|wait\|></tgt>` | 1674 |
| 4 | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | `<src>있을 때에 </src><tgt><\|wait\|></tgt>` | 1326 |
| 5 | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | `<src>말 못하 는 </src><tgt><\|wait\|></tgt>` | 1061 |
| 6 | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | `<src>우상에게로 </src><tgt><\|wait\|></tgt>` | 1312 |
| 7 | `<src>끄는 그대로 </src><tgt><\|wait\|></tgt>` | `<src>그는 </src><tgt><\|wait\|></tgt>` | 1401 |
| 8 | `<src>끌려 갔느니라. </src><tgt><\|wait\|></tgt>` | `<src>그대로 걸려 갔느니라. </src><tgt><\|wait\|></tgt>` | 1938 |
| 9 | `<src><\|wait\|></src><tgt>あなたがたも知っているとおり、あなたがたが異邦人だった時、ものを言わない偶像に引かれるままに連れて行かれました。</tgt>` | `<src><\|wait\|></src><tgt>あなたたちも知っているだろう。あなたがたが異邦人であったとき、言葉を持たない偶像へとそのまま歩んでいったのだ。</tgt>` | 2636 |
| 10 | `<src>그러므로 내가 </src><tgt><\|wait\|></tgt>` | `<src>그러므로 </src><tgt><\|wait\|></tgt>` | 1726 |
| 11 | `<src>너희 에게 </src><tgt><\|wait\|></tgt>` | `<src>내가 너희 에게 </src><tgt><\|wait\|></tgt>` | 1283 |
| 12 | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | `<src>알리 노니 </src><tgt><\|wait\|></tgt>` | 1685 |
| 13 | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | `<src>하나님 의 영으로 </src><tgt><\|wait\|></tgt>` | 1530 |
| 14 | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | `<src>말하는 자는. </src><tgt><\|wait\|></tgt>` | 856 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 725 |

---

### Test Example 41 / 60
- UID: EN_nkR1jtzhDFY_W000034
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1130 |
| 2 | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | `<src>Educational attainment. </src><tgt><\|wait\|></tgt>` | 1056 |
| 3 | `<src>How far did you </src><tgt><\|wait\|></tgt>` | `<src>How far did you </src><tgt><\|wait\|></tgt>` | 1747 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>actually go </src><tgt><\|wait\|></tgt>` | 1135 |
| 5 | `<src>actually go in your education? Did you </src><tgt><\|wait\|></tgt>` | `<src>in your education? Did you </src><tgt><\|wait\|></tgt>` | 1370 |
| 6 | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | `<src>graduate from high school? </src><tgt><\|wait\|></tgt>` | 1333 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>That's one level </src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src>That's one level of attainment. Did you go </src><tgt><\|wait\|></tgt>` | `<src>of attainment. Did you go </src><tgt><\|wait\|></tgt>` | 1733 |
| 9 | `<src>to college, </src><tgt>교육 수준. 실제로 어디까지 교육을 받으셨나요? 고등학교를 졸업하셨나요? 그게 한 단계입니다. 대학에 진학하셨나요?</tgt>` | `<src>to college, </src><tgt>학력 수준. 교육은 얼마나 높이까지 올라가셨나요? 고등학교 졸업은 한 단계의 학력 수준입니다. 대학에 가셨나요?</tgt>` | 2654 |
| 10 | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | `<src>and if so, did you graduate? </src><tgt><\|wait\|></tgt>` | 1968 |
| 11 | `<src>That's another level of </src><tgt><\|wait\|></tgt>` | `<src>That's another level </src><tgt><\|wait\|></tgt>` | 1196 |
| 12 | `<src>attainment. </src><tgt><\|wait\|></tgt>` | `<src>of attainment. </src><tgt><\|wait\|></tgt>` | 1555 |
| 13 | `<src>So that's it for </src><tgt><\|wait\|></tgt>` | `<src>So that's it </src><tgt><\|wait\|></tgt>` | 1530 |
| 14 | `<src>now. I'll see you </src><tgt><\|wait\|></tgt>` | `<src>for now. I'll see you </src><tgt><\|wait\|></tgt>` | 1021 |
| 15 | `<src>online. </src><tgt><\|wait\|></tgt>` | `<src>online. </src><tgt><\|wait\|></tgt>` | 577 |

---

### Test Example 42 / 60
- UID: KO_EtpixiKDUjA_W000104
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | `<src>눈 감고 </src><tgt><\|wait\|></tgt>` | 1286 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1045 |
| 3 | `<src>선생 이 뭐라 빌 거야. </src><tgt><\|wait\|></tgt>` | `<src>선생 이 뭐라 빌 거야, </src><tgt><\|wait\|></tgt>` | 2113 |
| 4 | `<src>니한테 소름 이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>니한테 서름이 </src><tgt><\|wait\|></tgt>` | 1412 |
| 5 | `<src>닭살이 돋든 </src><tgt><\|wait\|></tgt>` | `<src>덧댄 자질 이 덧댄 </src><tgt><\|wait\|></tgt>` | 1683 |
| 6 | `<src>느낌 이 오면 </src><tgt><\|wait\|></tgt>` | `<src>느낌 이 오며 </src><tgt><\|wait\|></tgt>` | 497 |
| 7 | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | `<src>이걸 흔들 어서 </src><tgt><\|wait\|></tgt>` | 1620 |
| 8 | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | `<src>같이 놀자는 거야. </src><tgt><\|wait\|></tgt>` | 1573 |
| 9 | `<src>귀신 이 오면 </src><tgt>目を閉じて。私が祈るから。鳥肌が立ったり何かを感じたりしたら、これを振って。一緒に遊ぼうって合図だから。霊が来たら</tgt>` | `<src>귀신 이 오면 </src><tgt>目を閉じて、先生が何と祈っているのか、あなたに何が憑いているのかを感じて。そして、これを揺らして一緒に遊ぼうというんだ。鬼が来たら、</tgt>` | 3010 |
| 10 | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | `<src>물릴 거고 </src><tgt><\|wait\|></tgt>` | 1967 |
| 11 | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | `<src>신이 오면 </src><tgt><\|wait\|></tgt>` | 1923 |
| 12 | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | `<src>너 지켜 주라고 </src><tgt><\|wait\|></tgt>` | 770 |
| 13 | `<src>찔러 줄 거니 까 </src><tgt><\|wait\|></tgt>` | `<src>찔러 주라고 그러니까 </src><tgt><\|wait\|></tgt>` | 1533 |
| 14 | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | `<src>편안 한 마음 에 </src><tgt><\|wait\|></tgt>` | 729 |
| 15 | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | `<src>눈 감아. </src><tgt><\|wait\|></tgt>` | 590 |

---

### Test Example 43 / 60
- UID: EN_nOtTM2Tg_DY_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>That someone who's </src><tgt><\|wait\|></tgt>` | `<src>That someone who just </src><tgt><\|wait\|></tgt>` | 1182 |
| 2 | `<src>just getting going </src><tgt><\|wait\|></tgt>` | `<src>getting going </src><tgt><\|wait\|></tgt>` | 1038 |
| 3 | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | `<src>needs to get, </src><tgt><\|wait\|></tgt>` | 1544 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1231 |
| 5 | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | `<src>and I have ten of them </src><tgt><\|wait\|></tgt>` | 1353 |
| 6 | `<src>that I think are </src><tgt><\|wait\|></tgt>` | `<src>that are really important </src><tgt><\|wait\|></tgt>` | 1361 |
| 7 | `<src>really important. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1454 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>to to </src><tgt><\|wait\|></tgt>` | 1824 |
| 9 | `<src>I'm going to go into. </src><tgt>それは始めたばかりの人が手に入れるべきもので、私にとって本当に重要だと思うのが10個あります。それについてお話ししていきます。</tgt>` | `<src>I'm going to go </src><tgt>これから動き出している人たち、やるべきことを理解したい人たち、その10人についてお話しします。その10人には、</tgt>` | 2763 |
| 10 | `<src>I have about </src><tgt><\|wait\|></tgt>` | `<src>into, I have </src><tgt><\|wait\|></tgt>` | 1529 |
| 11 | `<src>one minute videos </src><tgt><\|wait\|></tgt>` | `<src>about one minute videos </src><tgt><\|wait\|></tgt>` | 1398 |
| 12 | `<src>that follow this video </src><tgt><\|wait\|></tgt>` | `<src>at the end of this video </src><tgt><\|wait\|></tgt>` | 1820 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>that cover each one. </src><tgt><\|wait\|></tgt>` | 1628 |
| 14 | `<src>that cover each one </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 775 |
| 15 | `<src>in a little more detail, but. </src><tgt><\|wait\|></tgt>` | `<src>You know, in a little more detail, </src><tgt><\|wait\|></tgt>` | 786 |

---

### Test Example 44 / 60
- UID: ZH_P0j1n-htgFu_W000028
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | `<src>在财运方面，</src><tgt><\|wait\|></tgt>` | 1038 |
| 2 | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | `<src>这个月财运可以说是</src><tgt><\|wait\|></tgt>` | 1170 |
| 3 | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | `<src>很不错的，但是</src><tgt><\|wait\|></tgt>` | 1584 |
| 4 | `<src>比较偏向正财的部分，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1230 |
| 5 | `<src>也就是</src><tgt><\|wait\|></tgt>` | `<src>比较偏向正财的部分，也就是</src><tgt><\|wait\|></tgt>` | 1519 |
| 6 | `<src>在事业方面的</src><tgt><\|wait\|></tgt>` | `<src>在事业方面</src><tgt><\|wait\|></tgt>` | 1080 |
| 7 | `<src>业绩成长所带来的红利</src><tgt><\|wait\|></tgt>` | `<src>的业绩增长</src><tgt><\|wait\|></tgt>` | 1471 |
| 8 | `<src>与收入的</src><tgt><\|wait\|></tgt>` | `<src>所带来的红利，以及收入的</src><tgt><\|wait\|></tgt>` | 1844 |
| 9 | `<src>提升。如果是在</src><tgt>金運ですが、今月はかなり良いです。ただ、どちらかというと本業の収入、つまり仕事の業績成長によるボーナスや昇給の運気が強めです。</tgt>` | `<src>提升。如果是在</src><tgt>金運についてですが、今月はかなり良いと言えます。ただ、特に正財の面で、つまり仕事の業績向上による恩恵や収入アップが期待できます。もし</tgt>` | 2925 |
| 10 | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | `<src>投资理财方面呢，</src><tgt><\|wait\|></tgt>` | 2113 |
| 11 | `<src>这个月</src><tgt><\|wait\|></tgt>` | `<src>这个月也是</src><tgt><\|wait\|></tgt>` | 1879 |
| 12 | `<src>也是不错，只是</src><tgt><\|wait\|></tgt>` | `<src>不错，只是相对于</src><tgt><\|wait\|></tgt>` | 864 |
| 13 | `<src>相对正财来说就</src><tgt><\|wait\|></tgt>` | `<src>正财来说，就</src><tgt><\|wait\|></tgt>` | 1590 |
| 14 | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | `<src>稍微弱了那么一点。</src><tgt><\|wait\|></tgt>` | 965 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 911 |

---

### Test Example 45 / 60
- UID: JA_Y8_nzz_wKN8_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | `<src>でこれはですね、</src><tgt><\|wait\|></tgt>` | 1101 |
| 2 | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | `<src>あのビジュアル開発環境</src><tgt><\|wait\|></tgt>` | 1123 |
| 3 | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | `<src>というだけじゃなくて</src><tgt><\|wait\|></tgt>` | 1692 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1233 |
| 5 | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルPython開発環境なんですね。</src><tgt><\|wait\|></tgt>` | 1389 |
| 6 | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | `<src>というのもフローリフを</src><tgt><\|wait\|></tgt>` | 1246 |
| 7 | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | `<src>ビジュアルに書いた後、</src><tgt><\|wait\|></tgt>` | 1707 |
| 8 | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | `<src>それあいさつはPythonコード</src><tgt><\|wait\|></tgt>` | 1604 |
| 9 | `<src>にそこから</src><tgt>This isn't just a visual development environment; it's a visual Python development environment.</tgt>` | `<src>にそこから</src><tgt>So, this isn't just a visual development environment. It's a visual Python development environment. You write the flow in Visual, and then</tgt>` | 2522 |
| 10 | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | `<src>生成されて、それが</src><tgt><\|wait\|></tgt>` | 1114 |
| 11 | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | `<src>実行されることで</src><tgt><\|wait\|></tgt>` | 1826 |
| 12 | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | `<src>信号処理が行われるという</src><tgt><\|wait\|></tgt>` | 1868 |
| 13 | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | `<src>構造になっているからです。</src><tgt><\|wait\|></tgt>` | 1371 |
| 14 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 756 |
| 15 | `<src>はい。</src><tgt><\|wait\|></tgt>` | `<src>はい。</src><tgt><\|wait\|></tgt>` | 881 |
| 16 | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | `<src>じゃあ。</src><tgt><\|wait\|></tgt>` | 959 |

---

### Test Example 46 / 60
- UID: KO_Dl3QxRTDLhU_W000081
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그래서 뭐 </src><tgt><\|wait\|></tgt>` | `<src>그래서 </src><tgt><\|wait\|></tgt>` | 1128 |
| 2 | `<src>물론 이제 이런 경우 들도 </src><tgt><\|wait\|></tgt>` | `<src>뭐 물론 이제 </src><tgt><\|wait\|></tgt>` | 869 |
| 3 | `<src>있습니다. </src><tgt><\|wait\|></tgt>` | `<src>이런 경우 들도 있습니다. 저희 가 </src><tgt><\|wait\|></tgt>` | 1332 |
| 4 | `<src>저희 가 A라는 사람 과 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1273 |
| 5 | `<src>B라는 사람 이 서로 </src><tgt><\|wait\|></tgt>` | `<src>A라는 사람 과 다른 사람 이 </src><tgt><\|wait\|></tgt>` | 1465 |
| 6 | `<src>컨설턴트예요, </src><tgt><\|wait\|></tgt>` | `<src>서로 컨설턴트예요, </src><tgt><\|wait\|></tgt>` | 1643 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1456 |
| 8 | `<src>모이 킹 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | `<src>이제 컨설턴트여가지고 </src><tgt><\|wait\|></tgt>` | 1910 |
| 9 | `<src>A라는 사람 이 </src><tgt>もちろん、こうしたケースもあります。AさんとBさんはお互いに模擬ハッキングのコンサルタントです。例えば、Aさんが</tgt>` | `<src>A라는 사람 이 </src><tgt>ですから、もちろんこういうケースもあります。Aさんと別の人が、お互いにコンサルタントで、Aさんがコンサルタントで、Aさんが</tgt>` | 2701 |
| 10 | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | `<src>어떤 악성 코드 를 </src><tgt><\|wait\|></tgt>` | 1911 |
| 11 | `<src>뿌렸 을 때 </src><tgt><\|wait\|></tgt>` | `<src>주었을 때 </src><tgt><\|wait\|></tgt>` | 1170 |
| 12 | `<src>B라는 사람 이 </src><tgt><\|wait\|></tgt>` | `<src>비란 사람 이 </src><tgt><\|wait\|></tgt>` | 1600 |
| 13 | `<src>실제 </src><tgt><\|wait\|></tgt>` | `<src>실제 크로스사이트로 </src><tgt><\|wait\|></tgt>` | 1480 |
| 14 | `<src>크로스사이트 스쿠티에서 </src><tgt><\|wait\|></tgt>` | `<src>T에서 </src><tgt><\|wait\|></tgt>` | 738 |
| 15 | `<src>EX 파일 까지 </src><tgt><\|wait\|></tgt>` | `<src>EX 파일까지 </src><tgt><\|wait\|></tgt>` | 834 |
| 16 | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | `<src>감염 이 될까. </src><tgt><\|wait\|></tgt>` | 979 |

---

### Test Example 47 / 60
- UID: KO_EyI5xeRFbyu_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>주가 지수 가 이제 </src><tgt><\|wait\|></tgt>` | `<src>주가 지수 가 </src><tgt><\|wait\|></tgt>` | 1006 |
| 2 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1033 |
| 3 | `<src>상승 하는 흐름 을 보인다 면 </src><tgt><\|wait\|></tgt>` | `<src>인증 상승 하는 흐름 을 보인 다면 </src><tgt><\|wait\|></tgt>` | 2237 |
| 4 | `<src>이런 대형주 도 </src><tgt><\|wait\|></tgt>` | `<src>이런 대형 주도 </src><tgt><\|wait\|></tgt>` | 1540 |
| 5 | `<src>큰 폭의 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1535 |
| 6 | `<src>상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | `<src>큰 폭의 상승 을 하겠지만 </src><tgt><\|wait\|></tgt>` | 1017 |
| 7 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 829 |
| 8 | `<src>이 가벼운 </src><tgt><\|wait\|></tgt>` | `<src>먼저 가벼운 </src><tgt><\|wait\|></tgt>` | 1731 |
| 9 | `<src>종목 들이 </src><tgt>If the stock index shows an upward trend, these large- cap stocks will see significant gains.</tgt>` | `<src>종목 들이 </src><tgt>If the stock index is rising, these large- cap stocks will likely see a sharp rise. But first,</tgt>` | 2207 |
| 10 | `<src>먼저 </src><tgt><\|wait\|></tgt>` | `<src>먼저 </src><tgt><\|wait\|></tgt>` | 959 |
| 11 | `<src>시장 을 주도 하면서 </src><tgt><\|wait\|></tgt>` | `<src>시장 을 주도 하면서 움직이 기 때문 에 </src><tgt><\|wait\|></tgt>` | 2299 |
| 12 | `<src>움직이 기 때문 에 항상 </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1742 |
| 13 | `<src>요 시총이 </src><tgt><\|wait\|></tgt>` | `<src>항상 요 시총이 </src><tgt><\|wait\|></tgt>` | 1513 |
| 14 | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | `<src>가벼운 종목 을 </src><tgt><\|wait\|></tgt>` | 870 |
| 15 | `<src>눈여겨 봐야 될 것 </src><tgt><\|wait\|></tgt>` | `<src>눈여겨봐야 </src><tgt><\|wait\|></tgt>` | 838 |
| 16 | `<src>같습니다. </src><tgt><\|wait\|></tgt>` | `<src>될 것 같습니다. </src><tgt><\|wait\|></tgt>` | 949 |

---

### Test Example 48 / 60
- UID: JA_4wtcjSQrmjg_W000022
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>だったら</src><tgt><\|wait\|></tgt>` | `<src>だったらもう</src><tgt><\|wait\|></tgt>` | 1155 |
| 2 | `<src>もう眠らせてやれ。</src><tgt><\|wait\|></tgt>` | `<src>蒸らせてやれ</src><tgt><\|wait\|></tgt>` | 1103 |
| 3 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1313 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>俺は今</src><tgt><\|wait\|></tgt>` | 1380 |
| 5 | `<src>今奇跡を見てる。</src><tgt><\|wait\|></tgt>` | `<src>引き締めろ</src><tgt><\|wait\|></tgt>` | 1157 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1526 |
| 7 | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | `<src>もう限界なんか</src><tgt><\|wait\|></tgt>` | 1534 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>遠い超えている</src><tgt><\|wait\|></tgt>` | 1846 |
| 9 | `<src>遠い超えてる船の奇跡よ。</src><tgt>그럼 이제 잠들게 해줘. 난 지금 기적을 보고 있어. 이미 한계를 훨씬 뛰어넘은 배의 기적을 말이야.</tgt>` | `<src>船長貴勢気</src><tgt>그럼 그냥 쪄버려. 난 지금 당장 꽉 잡아. 한계는 이미 저 멀리 지나간 거야, 선장. 그 끈기,</tgt>` | 2904 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1782 |
| 11 | `<src>長年</src><tgt><\|wait\|></tgt>` | `<src>長年</src><tgt><\|wait\|></tgt>` | 1092 |
| 12 | `<src>船大工をやってる</src><tgt><\|wait\|></tgt>` | `<src>船団大工をやってる</src><tgt><\|wait\|></tgt>` | 1822 |
| 13 | `<src>が、</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1558 |
| 14 | `<src>俺は</src><tgt><\|wait\|></tgt>` | `<src>俺がこんなにすごい</src><tgt><\|wait\|></tgt>` | 883 |
| 15 | `<src>こんなにすごい海賊船を</src><tgt><\|wait\|></tgt>` | `<src>海賊船を見た</src><tgt><\|wait\|></tgt>` | 596 |
| 16 | `<src>見たことがない。</src><tgt><\|wait\|></tgt>` | `<src>ことがない。</src><tgt><\|wait\|></tgt>` | 875 |

---

### Test Example 49 / 60
- UID: KO_B00002_S00012_W000001
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>들어가 면 </src><tgt><\|wait\|></tgt>` | `<src>들어감 에는 </src><tgt><\|wait\|></tgt>` | 1273 |
| 2 | `<src>엄청 헤맵니다. </src><tgt><\|wait\|></tgt>` | `<src>엄청 </src><tgt><\|wait\|></tgt>` | 1059 |
| 3 | `<src>운전 을 </src><tgt><\|wait\|></tgt>` | `<src>해맞입니다. 운전을 </src><tgt><\|wait\|></tgt>` | 1845 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>할 건 </src><tgt><\|wait\|></tgt>` | 1111 |
| 5 | `<src>하건 걸어 걸어다니 </src><tgt><\|wait\|></tgt>` | `<src>거로 거로 다 </src><tgt><\|wait\|></tgt>` | 1151 |
| 6 | `<src>공간 에 뭐 </src><tgt><\|wait\|></tgt>` | `<src>이건데 </src><tgt><\|wait\|></tgt>` | 1371 |
| 7 | `<src>강북 을 가면 </src><tgt><\|wait\|></tgt>` | `<src>뭐 강북 으로 가면 </src><tgt><\|wait\|></tgt>` | 1625 |
| 8 | `<src>말할 것도 없고 외국 에 나가 면 </src><tgt><\|wait\|></tgt>` | `<src>말할 것도 없고 </src><tgt><\|wait\|></tgt>` | 1743 |
| 9 | `<src><\|wait\|></src><tgt>一进去就会晕头转向。不管是开车还是走路，去江北就不用说了，去外国</tgt>` | `<src>외국 에게 나가 는 것도 </src><tgt>去的话，会非常难。开车的话，都是以车为主。去江北，那更是难说，</tgt>` | 2574 |
| 10 | `<src>또 장렬이에요. </src><tgt><\|wait\|></tgt>` | `<src>장렬이에요. 좀 </src><tgt><\|wait\|></tgt>` | 1554 |
| 11 | `<src>좀 창피 하네요. </src><tgt><\|wait\|></tgt>` | `<src>신기 하네요. </src><tgt><\|wait\|></tgt>` | 1463 |
| 12 | `<src>대신 에 </src><tgt><\|wait\|></tgt>` | `<src>대신 에 이제 </src><tgt><\|wait\|></tgt>` | 1783 |
| 13 | `<src>이제 </src><tgt><\|wait\|></tgt>` | `<src>열심히 </src><tgt><\|wait\|></tgt>` | 1376 |
| 14 | `<src>열심히 물어봐요. </src><tgt><\|wait\|></tgt>` | `<src>모르 바요. 그거 는 </src><tgt><\|wait\|></tgt>` | 874 |
| 15 | `<src>그거 는 다인 것 같아요. </src><tgt><\|wait\|></tgt>` | `<src>잘한 것 같아요. </src><tgt><\|wait\|></tgt>` | 853 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 942 |

---

### Test Example 50 / 60
- UID: EN_nUk3lH51lD8_W000039
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1036 |
| 2 | `<src>Activity than </src><tgt><\|wait\|></tgt>` | `<src>Activity than </src><tgt><\|wait\|></tgt>` | 1016 |
| 3 | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | `<src>self-defining what we think </src><tgt><\|wait\|></tgt>` | 1247 |
| 4 | `<src>the standard is because you're </src><tgt><\|wait\|></tgt>` | `<src>the standard is, because you're </src><tgt><\|wait\|></tgt>` | 1583 |
| 5 | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | `<src>absolutely correct, </src><tgt><\|wait\|></tgt>` | 1137 |
| 6 | `<src>but the reality </src><tgt><\|wait\|></tgt>` | `<src>but the reality </src><tgt><\|wait\|></tgt>` | 1496 |
| 7 | `<src>is is that </src><tgt><\|wait\|></tgt>` | `<src>is is that </src><tgt><\|wait\|></tgt>` | 1478 |
| 8 | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | `<src>because we're the new kid on the </src><tgt><\|wait\|></tgt>` | 1878 |
| 9 | `<src>block and because the </src><tgt>私たちが何が基準であるかを自己定義するよりも、あなたが完全に正しいのです。しかし現実には、</tgt>` | `<src>block and because the </src><tgt>活動、つまり自分自身で基準を定義することです。なぜなら、あなたは完全に正しいからです。しかし、現実は、私たちが新しい世代だからです。そして、</tgt>` | 2835 |
| 10 | `<src>standards have </src><tgt><\|wait\|></tgt>` | `<src>standards have </src><tgt><\|wait\|></tgt>` | 1719 |
| 11 | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | `<src>changed from 20 </src><tgt><\|wait\|></tgt>` | 1229 |
| 12 | `<src>years ago, </src><tgt><\|wait\|></tgt>` | `<src>years ago, </src><tgt><\|wait\|></tgt>` | 1712 |
| 13 | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | `<src>we are being held to </src><tgt><\|wait\|></tgt>` | 1473 |
| 14 | `<src>a higher standard because </src><tgt><\|wait\|></tgt>` | `<src>a higher standard because. </src><tgt><\|wait\|></tgt>` | 841 |
| 15 | `<src>everything at this point is being </src><tgt><\|wait\|></tgt>` | `<src>Everything at this point is being </src><tgt><\|wait\|></tgt>` | 828 |
| 16 | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | `<src>held to a higher standard. </src><tgt><\|wait\|></tgt>` | 937 |

---

### Test Example 51 / 60
- UID: KO_EBFCgXs9SPQ_W000037
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | `<src>그리고 이에 대해 </src><tgt><\|wait\|></tgt>` | 831 |
| 2 | `<src>많은 사람 들이 분석 을 </src><tgt><\|wait\|></tgt>` | `<src>많은 사람 들이 </src><tgt><\|wait\|></tgt>` | 1071 |
| 3 | `<src>내놓 았습니다. </src><tgt><\|wait\|></tgt>` | `<src>분석 을 내놓 았습니다. </src><tgt><\|wait\|></tgt>` | 2059 |
| 4 | `<src>여기 로쿠자 의 </src><tgt><\|wait\|></tgt>` | `<src>여기 로쿠자 </src><tgt><\|wait\|></tgt>` | 1404 |
| 5 | `<src>분석 을 보시면 </src><tgt><\|wait\|></tgt>` | `<src>의 분석 을 보시면 </src><tgt><\|wait\|></tgt>` | 1327 |
| 6 | `<src>소니가 </src><tgt><\|wait\|></tgt>` | `<src>소니가 </src><tgt><\|wait\|></tgt>` | 752 |
| 7 | `<src>26비트 FP </src><tgt><\|wait\|></tgt>` | `<src>268F </src><tgt><\|wait\|></tgt>` | 1557 |
| 8 | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | `<src>파이프 를 </src><tgt><\|wait\|></tgt>` | 1715 |
| 9 | `<src>128비트로 낮춘 </src><tgt>そしてこれについて多くの人々が分析を出しています。こちらのロクザの分析を見ると、ソニーが26ビットFPパイプを128ビットに下げた</tgt>` | `<src>128비 트로 </src><tgt>これについて多くの人が分析を提出しました。ロクジャの分析を見ると、ソニーは268Fファインダーを128ビットに</tgt>` | 2929 |
| 10 | `<src>것으로 보인다. </src><tgt><\|wait\|></tgt>` | `<src>낮춘 것을 로프 인다. </src><tgt><\|wait\|></tgt>` | 2212 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1854 |
| 12 | `<src>Xbox Series X에서도 없는 </src><tgt><\|wait\|></tgt>` | `<src>X 박스 시리즈 X에서도 없는 </src><tgt><\|wait\|></tgt>` | 1048 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1350 |
| 14 | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | `<src>인피니트 캐시 </src><tgt><\|wait\|></tgt>` | 963 |
| 15 | `<src>L3가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | `<src>SD가 여기 도 없다. </src><tgt><\|wait\|></tgt>` | 783 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 476 |

---

### Test Example 52 / 60
- UID: EN_oVINouZo8aQ_W000138
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Um, </src><tgt><\|wait\|></tgt>` | 1053 |
| 2 | `<src>Also, </src><tgt><\|wait\|></tgt>` | `<src>also, </src><tgt><\|wait\|></tgt>` | 1023 |
| 3 | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | `<src>you will not be able to </src><tgt><\|wait\|></tgt>` | 1285 |
| 4 | `<src>move media objects </src><tgt><\|wait\|></tgt>` | `<src>move media objects </src><tgt><\|wait\|></tgt>` | 1434 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1164 |
| 6 | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | `<src>between the resources. </src><tgt><\|wait\|></tgt>` | 1562 |
| 7 | `<src>So, if </src><tgt><\|wait\|></tgt>` | `<src>So, if </src><tgt><\|wait\|></tgt>` | 1498 |
| 8 | `<src>you get into </src><tgt><\|wait\|></tgt>` | `<src>you get into the </src><tgt><\|wait\|></tgt>` | 1668 |
| 9 | `<src>a situation </src><tgt>另外，你没法在资源之间移动媒体对象。所以，如果</tgt>` | `<src>situation where you </src><tgt>嗯，另外，您将无法在资源之间移动媒体对象。所以，如果您遇到</tgt>` | 1251 |
| 10 | `<src>where you realize </src><tgt><\|wait\|></tgt>` | `<src>realize you've added </src><tgt><\|wait\|></tgt>` | 887 |
| 11 | `<src>you've added the wrong media </src><tgt><\|wait\|></tgt>` | `<src>the wrong media </src><tgt><\|wait\|></tgt>` | 1102 |
| 12 | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | `<src>files to a particular resource, </src><tgt><\|wait\|></tgt>` | 2140 |
| 13 | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | `<src>you need to let us know, </src><tgt><\|wait\|></tgt>` | 2057 |
| 14 | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | `<src>and we can see about </src><tgt><\|wait\|></tgt>` | 1257 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>uploading those media </src><tgt><\|wait\|></tgt>` | 1029 |
| 16 | `<src>moving those media files and then making sure they </src><tgt><\|wait\|></tgt>` | `<src>files and then making sure they </src><tgt><\|wait\|></tgt>` | 995 |
| 17 | `<src>get backed up </src><tgt><\|wait\|></tgt>` | `<src>get backed up </src><tgt><\|wait\|></tgt>` | 957 |
| 18 | `<src>properly. </src><tgt>你发现自己给某个资源加错了媒体文件，就告诉我们一声。我们可以帮你想想办法把那些媒体文件移过去，然后确保它们都备份好。</tgt>` | `<src>properly. </src><tgt>发现将错误的媒体文件添加到某个资源中，您需要通知我们。我们来查看上传这些媒体文件，并确保它们得到正确备份。</tgt>` | 786 |

---

### Test Example 53 / 60
- UID: ZH_W0NbyT5Ak-A_W000071
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>弗洛伊德</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 881 |
| 2 | `<src>首次觉知到</src><tgt><\|wait\|></tgt>` | `<src>为了以的首知觉</src><tgt><\|wait\|></tgt>` | 1185 |
| 3 | `<src>那个现象：</src><tgt><\|wait\|></tgt>` | `<src>知道那个现象，</src><tgt><\|wait\|></tgt>` | 1577 |
| 4 | `<src>每当我们</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1233 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>每当我们处于</src><tgt><\|wait\|></tgt>` | 975 |
| 6 | `<src>处于爱之中，</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1528 |
| 7 | `<src>所谓的爱，</src><tgt><\|wait\|></tgt>` | `<src>爱之中，所有的爱</src><tgt><\|wait\|></tgt>` | 1584 |
| 8 | `<src>我们也</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1719 |
| 9 | `<src>同时进入恨。</src><tgt>프로이트가 처음으로 그 현상을 알아차렸습니다. 우리가 사랑 속에 있을 때—소위 사랑이라 부르는 것—우리는 동시에 미움 속으로도 들어갑니다.</tgt>` | `<src>门都会同时进入</src><tgt>그 현상을 알기 위해 ' 에이 ' 의식을 갖추어야 합니다. 우리가 사랑 속에 있을 때, 모든 사랑의 문은</tgt>` | 2513 |
| 10 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 894 |
| 11 | `<src>在早上的时候，</src><tgt><\|wait\|></tgt>` | `<src>恨，在早上的时候，</src><tgt><\|wait\|></tgt>` | 2197 |
| 12 | `<src>它是爱；</src><tgt><\|wait\|></tgt>` | `<src>它是爱。</src><tgt><\|wait\|></tgt>` | 1685 |
| 13 | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | `<src>到了晚上，</src><tgt><\|wait\|></tgt>` | 1350 |
| 14 | `<src>它就变成恨。</src><tgt><\|wait\|></tgt>` | `<src>它就变成</src><tgt><\|wait\|></tgt>` | 869 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 946 |
| 16 | `<src>那个钟摆</src><tgt><\|wait\|></tgt>` | `<src>恨那个钟摆，</src><tgt><\|wait\|></tgt>` | 907 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>继续在</src><tgt><\|wait\|></tgt>` | 367 |
| 18 | `<src>继续在移动。</src><tgt>아침에는 그것이 사랑이지만, 밤이 되면 미움으로 변합니다. 그 시계추는 계속 움직이고 있습니다.</tgt>` | `<src>一动，</src><tgt>동시에 증오로 들어갑니다. 아침에는 사랑입니다. 밤이 되면 증오라는 시계추가 되어 계속 흔들립니다.</tgt>` | 837 |

---

### Test Example 54 / 60
- UID: EN_nUk3lH51lD8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | `<src>I was a bit </src><tgt><\|wait\|></tgt>` | 1350 |
| 2 | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | `<src>in turmoil </src><tgt><\|wait\|></tgt>` | 962 |
| 3 | `<src>in the first section </src><tgt><\|wait\|></tgt>` | `<src>in the first section </src><tgt><\|wait\|></tgt>` | 1153 |
| 4 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1270 |
| 5 | `<src>about the EHR fields </src><tgt><\|wait\|></tgt>` | `<src>about the EHR field. </src><tgt><\|wait\|></tgt>` | 1445 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Being an </src><tgt><\|wait\|></tgt>` | 1547 |
| 7 | `<src>being of critical importance </src><tgt><\|wait\|></tgt>` | `<src>incredibly important </src><tgt><\|wait\|></tgt>` | 1482 |
| 8 | `<src>versus variant </src><tgt><\|wait\|></tgt>` | `<src>versus </src><tgt><\|wait\|></tgt>` | 1495 |
| 9 | `<src><\|wait\|></src><tgt>最初のセクションでは少し葛藤していました。EHRフィールドの決定的な重要性と、</tgt>` | `<src><\|wait\|></src><tgt>EHRの分野について、最初のセクションで少し混乱していました。非常に重要なものと</tgt>` | 866 |
| 10 | `<src>databases, </src><tgt><\|wait\|></tgt>` | `<src>variant databases, </src><tgt><\|wait\|></tgt>` | 1470 |
| 11 | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | `<src>which is obviously one of my loves. </src><tgt><\|wait\|></tgt>` | 1194 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Is that if </src><tgt><\|wait\|></tgt>` | 1979 |
| 13 | `<src>Is that if we don't agree </src><tgt><\|wait\|></tgt>` | `<src>we don't agree upon </src><tgt><\|wait\|></tgt>` | 1725 |
| 14 | `<src>upon the fields that need </src><tgt><\|wait\|></tgt>` | `<src>the fields that need </src><tgt><\|wait\|></tgt>` | 777 |
| 15 | `<src>to be in these </src><tgt><\|wait\|></tgt>` | `<src>to be in these </src><tgt><\|wait\|></tgt>` | 1558 |
| 16 | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | `<src>data sources that we can </src><tgt><\|wait\|></tgt>` | 831 |
| 17 | `<src>draw from, </src><tgt><\|wait\|></tgt>` | `<src>draw from, </src><tgt><\|wait\|></tgt>` | 666 |
| 18 | `<src>there's nothing to draw from, right? </src><tgt>私が個人的に愛してやまないバリアントデータベースの間での葛藤です。つまり、活用できるデータソースに必要なフィールドについて合意できなければ、そもそも引き出せるデータは何もない、ということですよね？</tgt>` | `<src>there's nothing to draw from, right? </src><tgt>バリアントデータベースを比べると、その違いが非常に大きいんです。もちろん、それは私が大好きな分野の一つです。つまり、これらのデータソースに含めるべきフィールドについて合意できなければ、そこから何も得られませんよね？</tgt>` | 1721 |
| 19 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 348 |

---

### Test Example 55 / 60
- UID: EN_nlSouryhO2c_W000065
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | `<src>And at one point, </src><tgt><\|wait\|></tgt>` | 871 |
| 2 | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | `<src>he knows Jesus </src><tgt><\|wait\|></tgt>` | 1037 |
| 3 | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | `<src>is hungry. </src><tgt><\|wait\|></tgt>` | 1615 |
| 4 | `<src>He knows that </src><tgt><\|wait\|></tgt>` | `<src>He knows that </src><tgt><\|wait\|></tgt>` | 1330 |
| 5 | `<src>he's been without food, </src><tgt><\|wait\|></tgt>` | `<src>he's going to </src><tgt><\|wait\|></tgt>` | 1152 |
| 6 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>be in the wilderness </src><tgt><\|wait\|></tgt>` | 1375 |
| 7 | `<src>been in the wilderness forty days, that he's hungry. </src><tgt><\|wait\|></tgt>` | `<src>for forty days, that he's hungry, </src><tgt><\|wait\|></tgt>` | 1819 |
| 8 | `<src>And so he says </src><tgt><\|wait\|></tgt>` | `<src>and so he sends to </src><tgt><\|wait\|></tgt>` | 1575 |
| 9 | `<src>to Jesus," Hey, </src><tgt>ある時、彼はイエスが空腹だと知っています。食べ物をとらずに荒野で四十日過ごして、空腹だってことを知ってるんですね。で、彼はイエスに言うんです。「おい、</tgt>` | `<src>Jesus. </src><tgt>ある時、彼はイエスが飢えていることを知ります。彼は40日間荒野にいること、そして飢えていることを知っています。だから、イエスに送ります。</tgt>` | 2934 |
| 10 | `<src>if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | `<src>Hey, if you're the Son of God, prove it. </src><tgt><\|wait\|></tgt>` | 2519 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Turn </src><tgt><\|wait\|></tgt>` | 1727 |
| 12 | `<src>Turn these stones to bread." </src><tgt><\|wait\|></tgt>` | `<src>these stones to bread. </src><tgt><\|wait\|></tgt>` | 1496 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>How did he </src><tgt><\|wait\|></tgt>` | 779 |
| 14 | `<src>How did Jesus deal with that </src><tgt><\|wait\|></tgt>` | `<src>just deal with that? </src><tgt><\|wait\|></tgt>` | 949 |
| 15 | `<src>temptation? </src><tgt><\|wait\|></tgt>` | `<src>That temptation. </src><tgt><\|wait\|></tgt>` | 958 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Man, </src><tgt><\|wait\|></tgt>` | 411 |
| 17 | `<src>Man shall not live </src><tgt><\|wait\|></tgt>` | `<src>Jonathan lead by bread. </src><tgt><\|wait\|></tgt>` | 296 |
| 18 | `<src>by bread alone. </src><tgt>お前が神の子なら、証明してみろよ。この石をパンに変えてみろ」。イエスはその誘惑にどう対処したんでしょう？人はパンだけで生きるものではない。</tgt>` | `<src>Alone. </src><tgt>「おい、もしお前が神の御子なら、証明してみろ。この石をパンに変えてみろ。彼はどうやってその誘惑に対処したんだ？いやはや、ヨハネはパンによって導いた。一人で。」</tgt>` | 1069 |

---

### Test Example 56 / 60
- UID: EN_nSOXneMb4Ec_W000365
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Chinese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1280 |
| 2 | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | `<src>Meaningful individual </src><tgt><\|wait\|></tgt>` | 1063 |
| 3 | `<src>right, </src><tgt><\|wait\|></tgt>` | `<src>right, </src><tgt><\|wait\|></tgt>` | 1019 |
| 4 | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | `<src>and the Supreme Court </src><tgt><\|wait\|></tgt>` | 1365 |
| 5 | `<src>came along </src><tgt><\|wait\|></tgt>` | `<src>came along </src><tgt><\|wait\|></tgt>` | 1404 |
| 6 | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | `<src>last, not leading. </src><tgt><\|wait\|></tgt>` | 1581 |
| 7 | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | `<src>And I don't think the courts want to be </src><tgt><\|wait\|></tgt>` | 1598 |
| 8 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1791 |
| 9 | `<src>the the vanguard of social </src><tgt>有意义的个人权利，而最高法院是最后才介入的，不是引领者。我不认为</tgt>` | `<src>the the vanguard of </src><tgt>有意义的个人权利，最高法院是最后才跟进的，而不是引领。我不认为法院想成为</tgt>` | 2014 |
| 10 | `<src>change </src><tgt><\|wait\|></tgt>` | `<src>social change </src><tgt><\|wait\|></tgt>` | 1125 |
| 11 | `<src>these days, </src><tgt><\|wait\|></tgt>` | `<src>these days. </src><tgt><\|wait\|></tgt>` | 1970 |
| 12 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1941 |
| 13 | `<src>but they rather reflect </src><tgt><\|wait\|></tgt>` | `<src>But they rather reflect </src><tgt><\|wait\|></tgt>` | 761 |
| 14 | `<src>the consensus </src><tgt><\|wait\|></tgt>` | `<src>the consensus </src><tgt><\|wait\|></tgt>` | 1461 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 712 |
| 16 | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | `<src>that's already emerged. </src><tgt><\|wait\|></tgt>` | 725 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>So, </src><tgt><\|wait\|></tgt>` | 822 |
| 18 | `<src>So you have some </src><tgt>法院现在想成为社会变革的先锋，它们更倾向于反映已经形成的共识。所以，</tgt>` | `<src>you have some </src><tgt>当今社会变革的前沿。但它们更多地反映的是已经形成的共识。所以，</tgt>` | 627 |
| 19 | `<src>federal judges </src><tgt><\|wait\|></tgt>` | `<src>federal judges, </src><tgt><\|wait\|></tgt>` | 386 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 416 |
| 21 | `<src>who. </src><tgt><\|wait\|></tgt>` | `<src>who. </src><tgt><\|wait\|></tgt>` | 419 |

---

### Test Example 57 / 60
- UID: ZH_UJBZXO0vtl8_W000079
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Korean. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | `<src>那我们看一下</src><tgt><\|wait\|></tgt>` | 1074 |
| 2 | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | `<src>它的图片哦，</src><tgt><\|wait\|></tgt>` | 1059 |
| 3 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1258 |
| 4 | `<src>图片的部分呢，我们可以看到</src><tgt><\|wait\|></tgt>` | `<src>图片的不分分呢，</src><tgt><\|wait\|></tgt>` | 1485 |
| 5 | `<src>的一个是客厅</src><tgt><\|wait\|></tgt>` | `<src>我们可以看到的一个是</src><tgt><\|wait\|></tgt>` | 1174 |
| 6 | `<src>的部分。</src><tgt><\|wait\|></tgt>` | `<src>课听的部分，</src><tgt><\|wait\|></tgt>` | 1539 |
| 7 | `<src>那客厅一般</src><tgt><\|wait\|></tgt>` | `<src>课听一般都</src><tgt><\|wait\|></tgt>` | 1563 |
| 8 | `<src>都是属于</src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1730 |
| 9 | `<src>我们</src><tgt>그럼 사진을 한번 볼까요? 사진 부분을 보면 거실 공간이 보이네요. 거실은 보통 우리가</tgt>` | `<src>是属于我们在</src><tgt>그럼 사진을 한번 살펴볼게요. 사진을 나눠 보면, 하나는 강의 듣는 부분이에요. 강의 듣기는 보통</tgt>` | 2392 |
| 10 | `<src>在休息的地方，</src><tgt><\|wait\|></tgt>` | `<src>休息的地方。</src><tgt><\|wait\|></tgt>` | 987 |
| 11 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>所以</src><tgt><\|wait\|></tgt>` | 2065 |
| 12 | `<src>所以呢，这身体的部分</src><tgt><\|wait\|></tgt>` | `<src>呢，是身体的部分</src><tgt><\|wait\|></tgt>` | 1897 |
| 13 | `<src>也会反映的是</src><tgt><\|wait\|></tgt>` | `<src>呢，反映的是</src><tgt><\|wait\|></tgt>` | 1439 |
| 14 | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | `<src>你需要给自己</src><tgt><\|wait\|></tgt>` | 768 |
| 15 | `<src>一点时间，</src><tgt><\|wait\|></tgt>` | `<src>一点时间，可以</src><tgt><\|wait\|></tgt>` | 939 |
| 16 | `<src>可以好好的</src><tgt><\|wait\|></tgt>` | `<src>好好的做</src><tgt><\|wait\|></tgt>` | 942 |
| 17 | `<src>坐下来休息。可是</src><tgt><\|wait\|></tgt>` | `<src>一下洗去，</src><tgt><\|wait\|></tgt>` | 412 |
| 18 | `<src>我们可以看到这边是</src><tgt>쉬는 곳이잖아요. 그래서 이 신체 부위도 여러분이 자신에게 시간을 내서 편안히 앉아 쉴 필요가 있다는 걸 말해 주고 있어요. 그런데 여기는</tgt>` | `<src>可我们可以看到这边是</src><tgt>쉴 때 하는 거예요. 그래서 신체 부분은 여러분이 잠시 시간을 내서 제대로 샤워할 수 있도록 하라는 뜻이에요. 여기</tgt>` | 734 |
| 19 | `<src>空无一人的嘛，</src><tgt><\|wait\|></tgt>` | `<src>小朋友一人的人的嘛。</src><tgt><\|wait\|></tgt>` | 404 |
| 20 | `<src>啊，</src><tgt><\|wait\|></tgt>` | `<src>啊，</src><tgt><\|wait\|></tgt>` | 397 |
| 21 | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | `<src>所以是说。</src><tgt><\|wait\|></tgt>` | 339 |

---

### Test Example 58 / 60
- UID: EN_nLFyRxIRQBo_W000057
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to Japanese. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>These people are </src><tgt><\|wait\|></tgt>` | `<src>These people are </src><tgt><\|wait\|></tgt>` | 906 |
| 2 | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | `<src>completely rare, </src><tgt><\|wait\|></tgt>` | 1037 |
| 3 | `<src>and they often </src><tgt><\|wait\|></tgt>` | `<src>and they often </src><tgt><\|wait\|></tgt>` | 1330 |
| 4 | `<src>show up to </src><tgt><\|wait\|></tgt>` | `<src>show up to </src><tgt><\|wait\|></tgt>` | 1384 |
| 5 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1157 |
| 6 | `<src>completely revolutionize the world. </src><tgt><\|wait\|></tgt>` | `<src>completely revolutionize the world </src><tgt><\|wait\|></tgt>` | 1595 |
| 7 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1462 |
| 8 | `<src>Their personality is </src><tgt><\|wait\|></tgt>` | `<src>the personality is something that </src><tgt><\|wait\|></tgt>` | 1840 |
| 9 | `<src>something of a </src><tgt>こうした人々は非常に稀です。そして、世界を根本から変えるような存在であることがよくあります。彼らの性格は</tgt>` | `<src>have a contradiction, </src><tgt>これらの人々は極めて稀で、世界を完全に変革することがよくあります。その性格には矛盾があり、</tgt>` | 2298 |
| 10 | `<src>contradiction. </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 1020 |
| 11 | `<src>While they're </src><tgt><\|wait\|></tgt>` | `<src>while they're </src><tgt><\|wait\|></tgt>` | 2087 |
| 12 | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | `<src>extroverted, </src><tgt><\|wait\|></tgt>` | 1859 |
| 13 | `<src>they also hate </src><tgt><\|wait\|></tgt>` | `<src>they also hate </src><tgt><\|wait\|></tgt>` | 1139 |
| 14 | `<src>meaningless conversations </src><tgt><\|wait\|></tgt>` | `<src>meaningless conversations. </src><tgt><\|wait\|></tgt>` | 1101 |
| 15 | `<src>and like to </src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 941 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>And like it gets straight </src><tgt><\|wait\|></tgt>` | 822 |
| 17 | `<src>get straight to the point. </src><tgt><\|wait\|></tgt>` | `<src>to the point. </src><tgt><\|wait\|></tgt>` | 465 |
| 18 | `<src>They also love to </src><tgt>矛盾しています。外交的である一方、無意味な会話は嫌います。そして、要点を突くのを好みます。また、</tgt>` | `<src>They also love to. </src><tgt>外向的である一方で、無意味な会話も嫌います。そして、話はいつもストレートです。彼らはまた、</tgt>` | 801 |
| 19 | `<src>play </src><tgt><\|wait\|></tgt>` | `<src>Play the devil's advocate, </src><tgt><\|wait\|></tgt>` | 453 |
| 20 | `<src>the devil's advocate, and they </src><tgt><\|wait\|></tgt>` | `<src>and they </src><tgt><\|wait\|></tgt>` | 398 |
| 21 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>never shy away </src><tgt><\|wait\|></tgt>` | 339 |
| 22 | `<src>never shy away from a debate. </src><tgt><\|wait\|></tgt>` | `<src>from a debate. </src><tgt><\|wait\|></tgt>` | 353 |
| 23 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 338 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>Any AP </src><tgt><\|wait\|></tgt>` | 325 |
| 25 | `<src>ENTP stands for </src><tgt><\|wait\|></tgt>` | `<src>stands for. </src><tgt><\|wait\|></tgt>` | 297 |

---

### Test Example 59 / 60
- UID: KO_EAuwJ72nbgM_W000050
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이전 에 이준석은 </src><tgt><\|wait\|></tgt>` | 976 |
| 2 | `<src>당무 를 거부 한 </src><tgt><\|wait\|></tgt>` | `<src>강물 을 거부 한 </src><tgt><\|wait\|></tgt>` | 1169 |
| 3 | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | `<src>명분 이 후보 를 </src><tgt><\|wait\|></tgt>` | 1912 |
| 4 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 1405 |
| 5 | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | `<src>후보 의 당선 을 </src><tgt><\|wait\|></tgt>` | 1582 |
| 6 | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | `<src>위해서 라면서 </src><tgt><\|wait\|></tgt>` | 613 |
| 7 | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | `<src>제법 생색까지 </src><tgt><\|wait\|></tgt>` | 1587 |
| 8 | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | `<src>냈지만 이제 는 </src><tgt><\|wait\|></tgt>` | 1622 |
| 9 | `<src>윤석열 후보 가 </src><tgt>Previously, Lee Jun- seok claimed his reason for refusing party duties was for the candidate's sake— for the candidate's election— and he even made quite a show of it. But now,</tgt>` | `<src>윤석열 후보 가 </src><tgt>Earlier, Lee Jun- seok claimed he was rejecting the river for the sake of the candidate and even seemed to be trying to show off his support for the candidate's victory. But now, Yoon Suk- yeol</tgt>` | 3196 |
| 10 | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | `<src>김종인 을 </src><tgt><\|wait\|></tgt>` | 2139 |
| 11 | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | `<src>제거 한 순간 </src><tgt><\|wait\|></tgt>` | 1840 |
| 12 | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | `<src>이준석은 </src><tgt><\|wait\|></tgt>` | 1445 |
| 13 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>더루내놓고 </src><tgt><\|wait\|></tgt>` | 829 |
| 14 | `<src>드러내 놓고 윤석열 후보 를 떨어뜨리 겠다는 </src><tgt><\|wait\|></tgt>` | `<src>윤석열 후보 를 </src><tgt><\|wait\|></tgt>` | 953 |
| 15 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>떨어뜨리 겠다는 뚜렷 이 </src><tgt><\|wait\|></tgt>` | 1053 |
| 16 | `<src>독기를 품은 공격 성을 </src><tgt><\|wait\|></tgt>` | `<src>보이 는 공격 성을 </src><tgt><\|wait\|></tgt>` | 421 |
| 17 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>보이 기로 </src><tgt><\|wait\|></tgt>` | 342 |
| 18 | `<src>보이 기로 작정 한 </src><tgt>the moment Yoon Suk- yeol removed Kim Chong- in, Lee Jun -seok has decided to openly display his hostility, with a venomous intent to bring Yoon down.</tgt>` | `<src>작정 한 </src><tgt>is determined to attack and bring down Yoon Suk- yeol, who has removed Kim Jong- in.</tgt>` | 573 |
| 19 | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | `<src>것입니다. </src><tgt><\|wait\|></tgt>` | 421 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>가슴 발 </src><tgt><\|wait\|></tgt>` | 275 |
| 21 | `<src>가슴 발 이준석의 성상납 건 </src><tgt><\|wait\|></tgt>` | `<src>이준석의 성상납 건. </src><tgt><\|wait\|></tgt>` | 322 |
| 22 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | 231 |
| 23 | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | `<src>민주당 이 </src><tgt><\|wait\|></tgt>` | 282 |
| 24 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>공격 하기에 얼마나 </src><tgt><\|wait\|></tgt>` | 343 |
| 25 | `<src>공격 하기에 얼마나 큰 호재입니까? </src><tgt><\|wait\|></tgt>` | `<src>큰 호재 입니까. </src><tgt><\|wait\|></tgt>` | 335 |

---

### Test Example 60 / 60
- UID: JA_0WSDjPceAxQ_W000016
- SYSTEM_PROMPT: You are a professional simultaneous interpreter. Translate to English. Keep at least 8 wait windows before each target release.

| round | ground truth | predict | process time (ms) |
|---|---|---|---|
| 1 | `<src>まあ</src><tgt><\|wait\|></tgt>` | `<src>まあ</src><tgt><\|wait\|></tgt>` | 1110 |
| 2 | `<src>食堂ね</src><tgt><\|wait\|></tgt>` | `<src>食後ね今</src><tgt><\|wait\|></tgt>` | 880 |
| 3 | `<src>今作ってる</src><tgt><\|wait\|></tgt>` | `<src>作ってみたいな</src><tgt><\|wait\|></tgt>` | 1077 |
| 4 | `<src>みたいですなのでここのね</src><tgt><\|wait\|></tgt>` | `<src>ですね。なので</src><tgt><\|wait\|></tgt>` | 1432 |
| 5 | `<src>ゴールドストーンホテル</src><tgt><\|wait\|></tgt>` | `<src>ここの木彫サロンホテル</src><tgt><\|wait\|></tgt>` | 1523 |
| 6 | `<src>も</src><tgt><\|wait\|></tgt>` | `<src>も</src><tgt><\|wait\|></tgt>` | 1526 |
| 7 | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | `<src>朝食が食べれる場所</src><tgt><\|wait\|></tgt>` | 1014 |
| 8 | `<src>になってる</src><tgt><\|wait\|></tgt>` | `<src>になってる</src><tgt><\|wait\|></tgt>` | 793 |
| 9 | `<src>予定になってるので</src><tgt>Well, it seems they're building a dining area right now, so this Gold Stone Hotel is also planning to have breakfast available.</tgt>` | `<src>予定になっているので</src><tgt>Well, I'd like to make something after a meal. So, this Kobo Salon Hotel is also planned to be a place where you can have breakfast.</tgt>` | 2658 |
| 10 | `<src>今後ねここ</src><tgt><\|wait\|></tgt>` | `<src>今後ね</src><tgt><\|wait\|></tgt>` | 869 |
| 11 | `<src>ゴールドストーンホテルを</src><tgt><\|wait\|></tgt>` | `<src>ここ五六人</src><tgt><\|wait\|></tgt>` | 1058 |
| 12 | `<src>泊まってみたい</src><tgt><\|wait\|></tgt>` | `<src>ドーストンホテル泊まってみたりな</src><tgt><\|wait\|></tgt>` | 2277 |
| 13 | `<src>なっていう方はですね</src><tgt><\|wait\|></tgt>` | `<src>っていう方はですね</src><tgt><\|wait\|></tgt>` | 1934 |
| 14 | `<src>検討なさってみて</src><tgt><\|wait\|></tgt>` | `<src>検討させて</src><tgt><\|wait\|></tgt>` | 811 |
| 15 | `<src>もまあいいんじゃないか</src><tgt><\|wait\|></tgt>` | `<src>見て、まあいいんじゃないか</src><tgt><\|wait\|></tgt>` | 1545 |
| 16 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>なと。はい。</src><tgt><\|wait\|></tgt>` | 957 |
| 17 | `<src>なとはい思いますここ</src><tgt><\|wait\|></tgt>` | `<src>と思います。</src><tgt><\|wait\|></tgt>` | 836 |
| 18 | `<src>のホテルからですね釜山</src><tgt>So, for anyone thinking about staying here in the future, it might be worth considering. From this hotel,</tgt>` | `<src>ここのホテルからですね。</src><tgt>So, I'd like to see if five or six of us can stay there in the future. I think it's a good idea. Yes. From this hotel...</tgt>` | 855 |
| 19 | `<src>駅ももう</src><tgt><\|wait\|></tgt>` | `<src>부산駅も</src><tgt><\|wait\|></tgt>` | 400 |
| 20 | `<src><\|wait\|></src><tgt><\|wait\|></tgt>` | `<src>もう歩いて</src><tgt><\|wait\|></tgt>` | 381 |
| 21 | `<src>歩いて一分</src><tgt><\|wait\|></tgt>` | `<src>一分</src><tgt><\|wait\|></tgt>` | 413 |
| 22 | `<src>かかるかかかんないかそんな</src><tgt><\|wait\|></tgt>` | `<src>かかるかかかんないか</src><tgt><\|wait\|></tgt>` | 371 |
| 23 | `<src>レベルのね</src><tgt><\|wait\|></tgt>` | `<src>そんなレベルのね</src><tgt><\|wait\|></tgt>` | 346 |
| 24 | `<src>立地のいいねまあ</src><tgt><\|wait\|></tgt>` | `<src>立地のいいねまあホテル</src><tgt><\|wait\|></tgt>` | 364 |
| 25 | `<src>ホテルになってますので</src><tgt><\|wait\|></tgt>` | `<src>なってますので</src><tgt><\|wait\|></tgt>` | 322 |
| 26 | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | `<src>よかったらですね</src><tgt><\|wait\|></tgt>` | 314 |
| 27 | `<src>ご検討なさってみて</src><tgt>it's less than a minute's walk to Busan Station, so the location is really good. If you'd like,</tgt>` | `<src>ご検討なさってみて</src><tgt>the hotel is really well- located— you can walk to Busan Station in about a minute or so. So if you're interested, please consider staying there.</tgt>` | 378 |
| 28 | `<src>ください</src><tgt><\|wait\|></tgt>` | `<src>ください。それでは</src><tgt><\|wait\|></tgt>` | 194 |
| 29 | `<src>それではですね今回は。</src><tgt><\|wait\|></tgt>` | `<src>ね今回は。</src><tgt><\|wait\|></tgt>` | 202 |
