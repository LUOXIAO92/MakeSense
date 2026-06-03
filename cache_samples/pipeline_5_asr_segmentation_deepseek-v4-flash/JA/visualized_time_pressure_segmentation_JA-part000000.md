=== JA_B4lnt-FtXPy_W000004 ===

status: finished

raw_text:
5年間の国債運営成果を報告した。青瓦台のパクスヒョン国民総統秘書官は、文在寅大統領の革新となる経済政策基本路線、所得主導成長について。

word_indices:
* W0. {0: '5', 1: '年間', 2: 'の'}
* W1. {3: '国債'}
* W2. {4: '運営', 5: '成果', 6: 'を'}
* W3. {7: '報告', 8: 'し', 9: 'た。'}
* W4. {}
* W5. {10: '青瓦', 11: '台', 12: 'の'}
* W6. {13: 'パクスヒョン'}
* W7. {14: '国民', 15: '総統'}
* W8. {16: '秘書', 17: '官', 18: 'は、'}
* W9. {19: '文在', 20: '寅'}
* W10. {21: '大統領', 22: 'の'}
* W11. {23: '革新', 24: 'と', 25: 'なる'}
* W12. {26: '経済'}
* W13. {27: '政策', 28: '基本'}
* W14. {29: '路線、'}
* W15. {30: '所得', 31: '主導'}
* W16. {32: '成長', 33: 'に', 34: 'つい', 35: 'て。'}

scratchpad:
* W0. {0: '5', 1: '年間', 2: 'の'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 5年間の, stable nominal unit with particle: [0,1,2]

* W1. {3: '国債'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 国債, stable noun as minimal sense unit: [3]

* W2. {4: '運営', 5: '成果', 6: 'を'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 運営成果を, compound noun with particle: [4,5,6]

* W3. {7: '報告', 8: 'し', 9: 'た。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 報告した。, past-tense verb phrase: [7,8,9]

* W4. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W5. {10: '青瓦', 11: '台', 12: 'の'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 青瓦台の, proper noun with particle; forced to release because previous window was empty: [10,11,12]

* W6. {13: 'パクスヒョン'}
  - carried_over: None
  - defer: None
  - release_units:
    1. パクスヒョン, stable proper name: [13]

* W7. {14: '国民', 15: '総統'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 国民総統, compound noun (title): [14,15]

* W8. {16: '秘書', 17: '官', 18: 'は、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 秘書官は、, noun + particle unit with comma: [16,17,18]

* W9. {19: '文在', 20: '寅'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 文在寅, proper name (split by tokenization, kept together): [19,20]

* W10. {21: '大統領', 22: 'の'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 大統領の, noun + particle: [21,22]

* W11. {23: '革新', 24: 'と', 25: 'なる'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 革新となる, predicate phrase: [23,24,25]

* W12. {26: '経済'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 経済, stable noun: [26]

* W13. {27: '政策', 28: '基本'}
  - carried_over: None
  - defer: '基本' attaches to '路線' in the next window; defer [28] to W14: [28]
  - release_units:
    1. 政策, stable noun released now: [27]

* W14. {29: '路線、'}
  - carried_over: {28: '基本'}
  - defer: None
  - release_units:
    1. 基本路線、, '基本' carried over, forms stable bunsetsu: [28,29]

* W15. {30: '所得', 31: '主導'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 所得主導, compound noun: [30,31]

* W16. {32: '成長', 33: 'に', 34: 'つい', 35: 'て。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 成長について。, stable phrase with particle and period: [32,33,34,35]

result:
[
  [0,1,2],
  [3],
  [4,5,6],
  [7,8,9],
  [10,11,12],
  [13],
  [14,15],
  [16,17,18],
  [19,20],
  [21,22],
  [23,24,25],
  [26],
  [27],
  [28,29],
  [30,31],
  [32,33,34,35]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>5年間の</src>; start=0.00, end=1.00
* W1. <src>国債</src>; start=1.00, end=2.00
* W2. <src>運営成果を</src>; start=2.00, end=3.00
* W3. <src>報告した。</src>; start=3.00, end=4.00
* W4. <src><|wait|></src>; start=4.00, end=5.00
* W5. <src>青瓦台の</src>; start=5.00, end=6.00
* W6. <src>パクスヒョン</src>; start=6.00, end=7.00
* W7. <src>国民総統</src>; start=7.00, end=8.00
* W8. <src>秘書官は、</src>; start=8.00, end=9.00
* W9. <src>文在寅</src>; start=9.00, end=10.00
* W10. <src>大統領の</src>; start=10.00, end=11.00
* W11. <src>革新となる</src>; start=11.00, end=12.00
* W12. <src>経済</src>; start=12.00, end=13.00
* W13. <src>政策</src>; start=13.00, end=14.00
* W14. <src>基本路線、</src>; start=14.00, end=15.00
* W15. <src>所得主導</src>; start=15.00, end=16.00
* W16. <src>成長について。</src>; start=16.00, end=16.93
```

---
=== JA_B8if86uiSic_W000033 ===

status: finished

raw_text:
じゃあ戻したロール紙をここに入れます。えっとケースから紙を引き出し、お好みの長さに切ってご使用くださいと書いてあります。

word_indices:
* W0. {0: 'じゃあ', 1: '戻し', 2: 'た', 3: 'ロール'}
* W1. {4: '紙', 5: 'を'}
* W2. {6: 'ここ', 7: 'に', 8: '入れ'}
* W3. {9: 'ます。', 10: 'えっ'}
* W4. {11: 'と', 12: 'ケース', 13: 'から', 14: '紙', 15: 'を'}
* W5. {16: '引き出し、'}
* W6. {17: 'お', 18: '好み', 19: 'の', 20: '長'}
* W7. {21: 'さ', 22: 'に', 23: '切っ', 24: 'て', 25: 'ご'}
* W8. {26: '使用', 27: 'ください'}
* W9. {28: 'と', 29: '書い', 30: 'て', 31: 'あり', 32: 'ます。'}
* W10. {}

scratchpad:
* W0. {0: 'じゃあ', 1: '戻し', 2: 'た', 3: 'ロール'}
  - carried_over: None
  - defer: '戻したロール' does not yet form a stable minimal sense unit; defer to next window: [1,2,3]
  - release_units:
    1. じゃあ, stable discourse-level minimal sense unit: [0]

* W1. {4: '紙', 5: 'を'}
  - carried_over: {1: '戻し', 2: 'た', 3: 'ロール'}
  - defer: None
  - release_units:
    1. 戻したロール紙を, '戻したロール' carried over from previous window; now forms a stable noun phrase with particle: [1,2,3,4,5]

* W2. {6: 'ここ', 7: 'に', 8: '入れ'}
  - carried_over: None
  - defer: '入れ' does not yet form a stable minimal sense unit; defer to next window: [8]
  - release_units:
    1. ここに, stable minimal sense unit in the current window: [6,7]

* W3. {9: 'ます。', 10: 'えっ'}
  - carried_over: {8: '入れ'}
  - defer: 'えっ' does not yet form a stable minimal sense unit; defer to next window: [10]
  - release_units:
    1. 入れます。, '入れ' carried over from previous window; released here as a complete polite verb: [8,9]

* W4. {11: 'と', 12: 'ケース', 13: 'から', 14: '紙', 15: 'を'}
  - carried_over: {10: 'えっ'}
  - defer: None
  - release_units:
    1. えっと, 'えっ' carried over from previous window; forms a stable discourse connective: [10,11]
    2. ケースから, stable noun phrase with particle: [12,13]
    3. 紙を, stable noun phrase with particle: [14,15]

* W5. {16: '引き出し、'}
  - carried_over: None
  - defer: '引き出し、' does not yet form a stable minimal sense unit; defer to next window: [16]
  - release_units: None

* W6. {17: 'お', 18: '好み', 19: 'の', 20: '長'}
  - carried_over: {16: '引き出し、'}
  - defer: 'お好みの長' does not yet form a stable minimal sense unit; defer to next window: [17,18,19,20]
  - release_units:
    1. 引き出し、, latency-forced partial release; previous window had no output, so current window must flush something, even though the fragment is not ideal: [16]

* W7. {21: 'さ', 22: 'に', 23: '切っ', 24: 'て', 25: 'ご'}
  - carried_over: {17: 'お', 18: '好み', 19: 'の', 20: '長'}
  - defer: '切ってご' does not yet form a stable minimal sense unit; defer to next window: [23,24,25]
  - release_units:
    1. お好みの長さに, 'お好みの長' carried over from previous window; now forms a stable noun phrase with particle: [17,18,19,20,21,22]

* W8. {26: '使用', 27: 'ください'}
  - carried_over: {23: '切っ', 24: 'て', 25: 'ご'}
  - defer: None
  - release_units:
    1. 切ってご使用ください, '切ってご' carried over from previous window; now forms a stable polite request phrase: [23,24,25,26,27]

* W9. {28: 'と', 29: '書い', 30: 'て', 31: 'あり', 32: 'ます。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. と書いてあります。, stable complete phrase: [28,29,30,31,32]

* W10. {}
  - carried_over: None
  - defer: None
  - release_units: None

result:
[
  [0],
  [1,2,3,4,5],
  [6,7],
  [8,9],
  [10,11],
  [12,13],
  [14,15],
  [16],
  [17,18,19,20,21,22],
  [23,24,25,26,27],
  [28,29,30,31,32]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>じゃあ</src>; start=0.00, end=1.00
* W1. <src>戻したロール紙を</src>; start=1.00, end=2.00
* W2. <src>ここに</src>; start=2.00, end=3.00
* W3. <src>入れます。</src>; start=3.00, end=4.00
* W4. <src>えっとケースから紙を</src>; start=4.00, end=5.00
* W5. <src>引き出し、</src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>お好みの長さに</src>; start=7.00, end=8.00
* W8. <src>切ってご使用ください</src>; start=8.00, end=9.00
* W9. <src>と書いてあります。</src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=10.15
```

---
=== JA_Y-0K120KsxA_W000042 ===

status: finished

raw_text:
1100円でまあ使えてしまうということで、この車内ワイファイとエアボックスを連携することによって、もう最強のオーディオができるようになるとまあいうことで、今まで。

word_indices:
* W0. {0: '1100', 1: '円'}
* W1. {2: 'で', 3: 'まあ', 4: '使え', 5: 'て', 6: 'しまう', 7: 'と', 8: 'いう'}
* W2. {9: 'こと', 10: 'で、'}
* W3. {11: 'この', 12: '車内', 13: 'ワイファイ'}
* W4. {14: 'と', 15: 'エア', 16: 'ボックス'}
* W5. {17: 'を', 18: '連携', 19: 'する'}
* W6. {20: 'こと', 21: 'に', 22: 'よっ', 23: 'て、', 24: 'もう'}
* W7. {25: '最強', 26: 'の'}
* W8. {27: 'オーディオ', 28: 'が', 29: 'できる'}
* W9. {30: 'よう', 31: 'に', 32: 'なる', 33: 'と'}
* W10. {34: 'まあ', 35: 'いう', 36: 'こと', 37: 'で、'}
* W11. {38: '今', 39: 'まで。'}
* W12. {}
* W13. {}

scratchpad:
* W0. {0: '1100', 1: '円'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 1100円, stable minimal sense unit: [0,1]

* W1. {2: 'で', 3: 'まあ', 4: '使え', 5: 'て', 6: 'しまう', 7: 'と', 8: 'いう'}
  - carried_over: None
  - defer: 'という' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [7,8]
  - release_units:
    1. で, host-dependent tail from previous window's 1100円; released as a legal exception: [2]
    2. まあ, stable discourse unit: [3]
    3. 使えてしまう, stable predicate unit: [4,5,6]

* W2. {9: 'こと', 10: 'で、'}
  - carried_over: {7: 'と', 8: 'いう'}
  - defer: None
  - release_units:
    1. ということで、, 'という' carried over from the previous window; stable connective unit: [7,8,9,10]

* W3. {11: 'この', 12: '車内', 13: 'ワイファイ'}
  - carried_over: None
  - defer: None
  - release_units:
    1. この車内ワイファイ, stable noun phrase: [11,12,13]

* W4. {14: 'と', 15: 'エア', 16: 'ボックス'}
  - carried_over: None
  - defer: None
  - release_units:
    1. と, host-dependent tail from previous window's noun phrase; released as a legal exception: [14]
    2. エアボックス, stable compound noun: [15,16]

* W5. {17: 'を', 18: '連携', 19: 'する'}
  - carried_over: None
  - defer: None
  - release_units:
    1. を, host-dependent tail from previous window's エアボックス; released as a legal exception: [17]
    2. 連携する, stable verb phrase: [18,19]

* W6. {20: 'こと', 21: 'に', 22: 'よっ', 23: 'て、', 24: 'もう'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ことによって、, stable set phrase: [20,21,22,23]
    2. もう, stable discourse marker: [24]

* W7. {25: '最強', 26: 'の'}
  - carried_over: None
  - defer: '最強の' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [25,26]
  - release_units: None

* W8. {27: 'オーディオ', 28: 'が', 29: 'できる'}
  - carried_over: {25: '最強', 26: 'の'}
  - defer: None
  - release_units:
    1. 最強のオーディオが, '最強の' carried over from the previous window; stable bunsetsu unit: [25,26,27,28]
    2. できる, stable predicate unit: [29]

* W9. {30: 'よう', 31: 'に', 32: 'なる', 33: 'と'}
  - carried_over: None
  - defer: 'と' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [33]
  - release_units:
    1. ようになる, stable predicate unit: [30,31,32]

* W10. {34: 'まあ', 35: 'いう', 36: 'こと', 37: 'で、'}
  - carried_over: {33: 'と'}
  - defer: None
  - release_units:
    1. と, carried over from the previous window; released as a particle tail: [33]
    2. まあ, stable discourse unit: [34]
    3. いうことで、, stable connective unit: [35,36,37]

* W11. {38: '今', 39: 'まで。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 今まで, stable temporal expression: [38,39]

* W12. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W13. {}
  - carried_over: None
  - defer: None
  - release_units: None

result:
[
  [0,1],
  [2],
  [3],
  [4,5,6],
  [7,8,9,10],
  [11,12,13],
  [14],
  [15,16],
  [17],
  [18,19],
  [20,21,22,23],
  [24],
  [25,26,27,28],
  [29],
  [30,31,32],
  [33],
  [34],
  [35,36,37],
  [38,39]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>1100円</src>; start=0.00, end=1.00
* W1. <src>でまあ使えてしまう</src>; start=1.00, end=2.00
* W2. <src>ということで、</src>; start=2.00, end=3.00
* W3. <src>この車内ワイファイ</src>; start=3.00, end=4.00
* W4. <src>とエアボックス</src>; start=4.00, end=5.00
* W5. <src>を連携する</src>; start=5.00, end=6.00
* W6. <src>ことによって、もう</src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>最強のオーディオができる</src>; start=8.00, end=9.00
* W9. <src>ようになると</src>; start=9.00, end=10.00
* W10. <src>まあいうことで、</src>; start=10.00, end=11.00
* W11. <src>今まで。</src>; start=11.00, end=12.00
* W12. <src><|wait|></src>; start=12.00, end=13.00
* W13. <src><|wait|></src>; start=13.00, end=13.45
```

---
=== JA_ACoDViff5So_W000029 ===

status: finished

raw_text:
まあえっとこれがいくつかの特別な状態があるんですけれども、性格あるんですけれども、例えば重要なポイントは。

word_indices:
* W0. {0: 'まあえっ', 1: 'と', 2: 'これ'}
* W1. {3: 'が', 4: 'いく', 5: 'つ', 6: 'か'}
* W2. {7: 'の', 8: '特別'}
* W3. {9: 'な', 10: '状態'}
* W4. {11: 'が', 12: 'ある', 13: 'ん', 14: 'です', 15: 'けれど'}
* W5. {16: 'も、'}
* W6. {17: '性格'}
* W7. {18: 'ある', 19: 'ん', 20: 'です', 21: 'けれど', 22: 'も、'}
* W8. {23: '例えば'}
* W9. {24: '重要', 25: 'な', 26: 'ポイント', 27: 'は。'}
* W10. {}

scratchpad:
* W0. {0: 'まあえっ', 1: 'と', 2: 'これ'}
  - carried_over: None
  - defer: 'これ' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [2]
  - release_units:
    1. まあえっと, stable discourse filler / minimal sense unit in the current window: [0,1]

* W1. {3: 'が', 4: 'いく', 5: 'つ', 6: 'か'}
  - carried_over: {2: 'これ'}
  - defer: None
  - release_units:
    1. これが, 'これ' is carried over from the previous window; released here because it is now a stable minimal sense unit (content word + particle): [2,3]
    2. いくつか, stable minimal sense unit in the current window: [4,5,6]

* W2. {7: 'の', 8: '特別'}
  - carried_over: None
  - defer: 'の特別' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [7,8]
  - release_units: None

* W3. {9: 'な', 10: '状態'}
  - carried_over: {7: 'の', 8: '特別'}
  - defer: None
  - release_units:
    1. の, host-dependent tail; its host phrase いくつか was already emitted in a previous window: [7]
    2. 特別な状態, '特別' is carried over from the previous window; released here because it is now a stable minimal sense unit (modifier-head noun phrase): [8,9,10]

* W4. {11: 'が', 12: 'ある', 13: 'ん', 14: 'です', 15: 'けれど'}
  - carried_over: None
  - defer: 'けれど' does not yet form a stable minimal sense unit in the current window; defer it to the next window to combine with も: [15]
  - release_units:
    1. が, host-dependent tail; its host noun phrase 特別な状態 was already emitted in the previous window: [11]
    2. あるんです, stable minimal sense unit (auxiliary/explanatory chain) in the current window: [12,13,14]

* W5. {16: 'も、'}
  - carried_over: {15: 'けれど'}
  - defer: None
  - release_units:
    1. けれども、, 'けれど' is carried over from the previous window; released here because it is now a stable minimal sense unit (connective unit): [15,16]

* W6. {17: '性格'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 性格, stable minimal sense unit (noun) in the current window: [17]

* W7. {18: 'ある', 19: 'ん', 20: 'です', 21: 'けれど', 22: 'も、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. あるんですけれども、, stable minimal sense unit (predicate phrase with connective ending) in the current window: [18,19,20,21,22]

* W8. {23: '例えば'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 例えば, stable minimal sense unit (discourse marker) in the current window: [23]

* W9. {24: '重要', 25: 'な', 26: 'ポイント', 27: 'は。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 重要なポイントは。, stable minimal sense unit (noun phrase with topic marker and period) in the current window: [24,25,26,27]

* W10. {}
  - carried_over: None
  - defer: None
  - release_units: None

result:
[
  [0,1],
  [2,3],
  [4,5,6],
  [7],
  [8,9,10],
  [11],
  [12,13,14],
  [15,16],
  [17],
  [18,19,20,21,22],
  [23],
  [24,25,26,27]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>まあえっと</src>; start=0.00, end=1.00
* W1. <src>これがいくつか</src>; start=1.00, end=2.00
* W2. <src>の</src>; start=2.00, end=3.00
* W3. <src>特別な状態</src>; start=3.00, end=4.00
* W4. <src>があるんです</src>; start=4.00, end=5.00
* W5. <src>けれども、</src>; start=5.00, end=6.00
* W6. <src>性格</src>; start=6.00, end=7.00
* W7. <src>あるんですけれども、</src>; start=7.00, end=8.00
* W8. <src>例えば</src>; start=8.00, end=9.00
* W9. <src>重要なポイントは。</src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=10.07
```

---
=== JA_055Z9Ti9z9Y_W000045 ===

status: finished

raw_text:
これがギアです。ギアが緩むと芯が上げ下げできなくなってしまうので、ギアの先に役ねじのナットがついているっていうことですね。はい、分解完了。

word_indices:
* W0. {0: 'これ', 1: 'が', 2: 'ギア'}
* W1. {3: 'です。'}
* W2. {4: 'ギア', 5: 'が', 6: '緩む'}
* W3. {7: 'と', 8: '芯', 9: 'が'}
* W4. {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'}
* W5. {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'}
* W6. {19: 'の', 20: '先', 21: 'に'}
* W7. {22: '役ねじ', 23: 'の'}
* W8. {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'}
* W9. {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
* W10. {33: 'ね。'}
* W11. {34: 'はい、'}
* W12. {35: '分解', 36: '完了。'}

scratchpad:
* W0. {0: 'これ', 1: 'が', 2: 'ギア'}
  - carried_over: None
  - defer: None
  - release_units:
    1. これがギア, stable minimal sense unit in the current window: [0,1,2]

* W1. {3: 'です。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. です。, stable minimal sense unit in the current window: [3]

* W2. {4: 'ギア', 5: 'が', 6: '緩む'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ギアが緩む, stable minimal sense unit in the current window: [4,5,6]

* W3. {7: 'と', 8: '芯', 9: 'が'}
  - carried_over: None
  - defer: 'と芯が' does not yet form a stable minimal sense unit on its own; defer all to the next window to combine with the following verb phrase: [7,8,9]
  - release_units: None

* W4. {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'}
  - carried_over: {7: 'と', 8: '芯', 9: 'が'}
  - defer: None
  - release_units:
    1. と芯が, carried over from the previous window; released here as a conditional phrase: [7,8,9]
    2. 上げ下げできなくなって, stable minimal sense unit from the current window; released separately to keep chunk size within 7 tokens: [10,11,12,13,14]

* W5. {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'}
  - carried_over: None
  - defer: 'ギア' does not yet form a stable unit here; defer it to the next window to combine with 'の先に': [18]
  - release_units:
    1. しまうので、, stable minimal sense unit (causal conjunction): [15,16,17]

* W6. {19: 'の', 20: '先', 21: 'に'}
  - carried_over: {18: 'ギア'}
  - defer: None
  - release_units:
    1. ギアの先に, 'ギア' carried over from the previous window; released here as a stable noun phrase: [18,19,20,21]

* W7. {22: '役ねじ', 23: 'の'}
  - carried_over: None
  - defer: '役ねじの' deferred to the next window to keep the compound noun '役ねじのナット' together: [22,23]
  - release_units: None

* W8. {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'}
  - carried_over: {22: '役ねじ', 23: 'の'}
  - defer: 'ついて' deferred to the next window to combine with 'いる' and keep verb chain intact; also to avoid oversized chunk: [26,27]
  - release_units:
    1. 役ねじのナットが, '役ねじの' carried over; released here as a stable noun phrase: [22,23,24,25]

* W9. {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
  - carried_over: {26: 'つい', 27: 'て'}
  - defer: None
  - release_units:
    1. ついているっていうことです, 'ついて' carried over; released here as a complete verb phrase and nominalizer, exactly 7 tokens: [26,27,28,29,30,31,32]

* W10. {33: 'ね。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ね。, stable minimal sense unit: [33]

* W11. {34: 'はい、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. はい、, stable minimal sense unit: [34]

* W12. {35: '分解', 36: '完了。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 分解完了。, stable minimal sense unit: [35,36]

result:
[
  [0,1,2],
  [3],
  [4,5,6],
  [7,8,9],
  [10,11,12,13,14],
  [15,16,17],
  [18,19,20,21],
  [22,23,24,25],
  [26,27,28,29,30,31,32],
  [33],
  [34],
  [35,36]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: 'これ', 1: 'が', 2: 'ギア'} - output: release_units 1.{0: 'これ', 1: 'が', 2: 'ギア'}
* W1. input: {3: 'です。'} - output: release_units 1.{3: 'です。'}
* W2. input: {4: 'ギア', 5: 'が', 6: '緩む'} - output: release_units 1.{4: 'ギア', 5: 'が', 6: '緩む'}
* W3. input: {7: 'と', 8: '芯', 9: 'が'} - output: release_units None
* W4. input: {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'} - output: release_units 1.{7: 'と', 8: '芯', 9: 'が', 10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'} <- ISSUE2: oversized chunk release unit 1 size=8 > 7. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'} - output: release_units 1.{15: 'しまう', 16: 'の', 17: 'で、'}
* W6. input: {19: 'の', 20: '先', 21: 'に'} - output: release_units 1.{18: 'ギア', 19: 'の', 20: '先', 21: 'に'}
* W7. input: {22: '役ねじ', 23: 'の'} - output: release_units None
* W8. input: {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'} - output: release_units 1.{22: '役ねじ', 23: 'の', 24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'}
* W9. input: {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'} - output: release_units 1.{28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
* W10. input: {33: 'ね。'} - output: release_units 1.{33: 'ね。'}
* W11. input: {34: 'はい、'} - output: release_units 1.{34: 'はい、'}
* W12. input: {35: '分解', 36: '完了。'} - output: release_units 1.{35: '分解', 36: '完了。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: 'これ', 1: 'が', 2: 'ギア'}
  - carried_over: None
  - defer: None
  - release_units:
    1. これがギア, stable minimal sense unit in the current window: [0,1,2]

* W1. {3: 'です。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. です。, stable minimal sense unit in the current window: [3]

* W2. {4: 'ギア', 5: 'が', 6: '緩む'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ギアが緩む, stable minimal sense unit in the current window: [4,5,6]

* W3. {7: 'と', 8: '芯', 9: 'が'}
  - carried_over: None
  - defer: 'と芯が' does not yet form a stable minimal sense unit in the current window; defer it to the next window to combine with the following verb phrase: [7,8,9]
  - release_units: None

* W4. {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'}
  - carried_over: {7: 'と', 8: '芯', 9: 'が'}
  - defer: None
  - release_units:
    1. と芯が上げ下げできなくなって, 'と芯が' is carried over from the previous window; released here because it now forms a stable conditional clause unit: [7,8,9,10,11,12,13,14]

* W5. {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'}
  - carried_over: None
  - defer: 'ギア' does not yet form a stable minimal sense unit in the current window; defer it to the next window to pair with the following particle: [18]
  - release_units:
    1. しまうので、, stable minimal sense unit in the current window: [15,16,17]

* W6. {19: 'の', 20: '先', 21: 'に'}
  - carried_over: {18: 'ギア'}
  - defer: None
  - release_units:
    1. ギアの先に, 'ギア' is carried over from the previous window; released here because it now forms a stable locational unit: [18,19,20,21]

* W7. {22: '役ねじ', 23: 'の'}
  - carried_over: None
  - defer: '役ねじの' does not yet form a stable minimal sense unit; defer it to the next window to combine with the following noun: [22,23]
  - release_units: None

* W8. {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'}
  - carried_over: {22: '役ねじ', 23: 'の'}
  - defer: None
  - release_units:
    1. 役ねじのナットがついて, '役ねじの' is carried over from the previous window; released here because it now forms a stable subject-verb unit: [22,23,24,25,26,27]

* W9. {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
  - carried_over: None
  - defer: None
  - release_units:
    1. いるってことです, stable minimal sense unit in the current window: [28,29,30,31,32]

* W10. {33: 'ね。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ね。, stable minimal sense unit in the current window: [33]

* W11. {34: 'はい、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. はい、, stable minimal sense unit in the current window: [34]

* W12. {35: '分解', 36: '完了。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 分解完了。, stable minimal sense unit in the current window: [35,36]
  result:
[
  [0,1,2],
  [3],
  [4,5,6],
  [7,8,9,10,11,12,13,14],
  [15,16,17],
  [18,19,20,21],
  [22,23,24,25,26,27],
  [28,29,30,31,32],
  [33],
  [34],
  [35,36]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: 'これ', 1: 'が', 2: 'ギア'} - output: release_units 1.{0: 'これ', 1: 'が', 2: 'ギア'}
* W1. input: {3: 'です。'} - output: release_units 1.{3: 'です。'}
* W2. input: {4: 'ギア', 5: 'が', 6: '緩む'} - output: release_units 1.{4: 'ギア', 5: 'が', 6: '緩む'}
* W3. input: {7: 'と', 8: '芯', 9: 'が'} - output: release_units None
* W4. input: {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'} - output: release_units 1.{7: 'と', 8: '芯', 9: 'が', 10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'} <- ISSUE2: oversized chunk release unit 1 size=8 > 7. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'} - output: release_units 1.{15: 'しまう', 16: 'の', 17: 'で、'}
* W6. input: {19: 'の', 20: '先', 21: 'に'} - output: release_units 1.{18: 'ギア', 19: 'の', 20: '先', 21: 'に'}
* W7. input: {22: '役ねじ', 23: 'の'} - output: release_units None
* W8. input: {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'} - output: release_units 1.{22: '役ねじ', 23: 'の', 24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'}
* W9. input: {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'} - output: release_units 1.{28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
* W10. input: {33: 'ね。'} - output: release_units 1.{33: 'ね。'}
* W11. input: {34: 'はい、'} - output: release_units 1.{34: 'はい、'}
* W12. input: {35: '分解', 36: '完了。'} - output: release_units 1.{35: '分解', 36: '完了。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: 'これ', 1: 'が', 2: 'ギア'} - output: release_units 1.{0: 'これ', 1: 'が', 2: 'ギア'}
* W1. input: {3: 'です。'} - output: release_units 1.{3: 'です。'}
* W2. input: {4: 'ギア', 5: 'が', 6: '緩む'} - output: release_units 1.{4: 'ギア', 5: 'が', 6: '緩む'}
* W3. input: {7: 'と', 8: '芯', 9: 'が'} - output: release_units 1.{7: 'と', 8: '芯', 9: 'が'}
* W4. input: {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'} - output: release_units None
* W5. input: {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'} - output: release_units 1.{10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て', 15: 'しまう', 16: 'の', 17: 'で、'} <- ISSUE2: oversized chunk release unit 1 size=8 > 7. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W6. input: {19: 'の', 20: '先', 21: 'に'} - output: release_units 1.{18: 'ギア', 19: 'の', 20: '先', 21: 'に'}
* W7. input: {22: '役ねじ', 23: 'の'} - output: release_units None
* W8. input: {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'} - output: release_units 1.{22: '役ねじ', 23: 'の', 24: 'ナット', 25: 'が'}
* W9. input: {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'} - output: release_units 1.{26: 'つい', 27: 'て', 28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
* W10. input: {33: 'ね。'} - output: release_units 1.{33: 'ね。'}
* W11. input: {34: 'はい、'} - output: release_units 1.{34: 'はい、'}
* W12. input: {35: '分解', 36: '完了。'} - output: release_units 1.{35: '分解', 36: '完了。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: 'これ', 1: 'が', 2: 'ギア'}
  - carried_over: None
  - defer: None
  - release_units:
    1. これがギア, stable minimal sense unit in the current window: [0,1,2]

* W1. {3: 'です。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. です。, stable minimal sense unit in the current window: [3]

* W2. {4: 'ギア', 5: 'が', 6: '緩む'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ギアが緩む, stable minimal sense unit in the current window: [4,5,6]

* W3. {7: 'と', 8: '芯', 9: 'が'}
  - carried_over: None
  - defer: 'と芯が' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [7,8,9]
  - release_units: None

* W4. {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'}
  - carried_over: {7: 'と', 8: '芯', 9: 'が'}
  - defer: '上げ下げできなくなって' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [10,11,12,13,14]
  - release_units:
    1. と芯が, 'と芯が' is carried over from the previous window; released here because it is now a stable minimal sense unit: [7,8,9]

* W5. {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'}
  - carried_over: {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'}
  - defer: 'ギア' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [18]
  - release_units:
    1. 上げ下げできなくなってしまうので、, '上げ下げできなくなって' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12,13,14,15,16,17]

* W6. {19: 'の', 20: '先', 21: 'に'}
  - carried_over: {18: 'ギア'}
  - defer: None
  - release_units:
    1. ギアの先に, 'ギア' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20,21]

* W7. {22: '役ねじ', 23: 'の'}
  - carried_over: None
  - defer: '役ねじの' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [22,23]
  - release_units: None

* W8. {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'}
  - carried_over: {22: '役ねじ', 23: 'の'}
  - defer: 'ついて' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [26,27]
  - release_units:
    1. 役ねじのナットが, '役ねじの' is carried over from the previous window; released here because it is now a stable minimal sense unit: [22,23,24,25]

* W9. {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
  - carried_over: {26: 'つい', 27: 'て'}
  - defer: None
  - release_units:
    1. ついているっていうことです, 'ついて' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27,28,29,30,31,32]

* W10. {33: 'ね。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ね。, stable minimal sense unit in the current window: [33]

* W11. {34: 'はい、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. はい、, stable minimal sense unit in the current window: [34]

* W12. {35: '分解', 36: '完了。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 分解完了。, stable minimal sense unit in the current window: [35,36]
  result:
[
  [0,1,2],
  [3],
  [4,5,6],
  [7,8,9],
  [10,11,12,13,14,15,16,17],
  [18,19,20,21],
  [22,23,24,25],
  [26,27,28,29,30,31,32],
  [33],
  [34],
  [35,36]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: 'これ', 1: 'が', 2: 'ギア'} - output: release_units 1.{0: 'これ', 1: 'が', 2: 'ギア'}
* W1. input: {3: 'です。'} - output: release_units 1.{3: 'です。'}
* W2. input: {4: 'ギア', 5: 'が', 6: '緩む'} - output: release_units 1.{4: 'ギア', 5: 'が', 6: '緩む'}
* W3. input: {7: 'と', 8: '芯', 9: 'が'} - output: release_units 1.{7: 'と', 8: '芯', 9: 'が'}
* W4. input: {10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て'} - output: release_units None
* W5. input: {15: 'しまう', 16: 'の', 17: 'で、', 18: 'ギア'} - output: release_units 1.{10: '上げ下げ', 11: 'でき', 12: 'なく', 13: 'なっ', 14: 'て', 15: 'しまう', 16: 'の', 17: 'で、'} <- ISSUE2: oversized chunk release unit 1 size=8 > 7. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W6. input: {19: 'の', 20: '先', 21: 'に'} - output: release_units 1.{18: 'ギア', 19: 'の', 20: '先', 21: 'に'}
* W7. input: {22: '役ねじ', 23: 'の'} - output: release_units None
* W8. input: {24: 'ナット', 25: 'が', 26: 'つい', 27: 'て'} - output: release_units 1.{22: '役ねじ', 23: 'の', 24: 'ナット', 25: 'が'}
* W9. input: {28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'} - output: release_units 1.{26: 'つい', 27: 'て', 28: 'いる', 29: 'って', 30: 'いう', 31: 'こと', 32: 'です'}
* W10. input: {33: 'ね。'} - output: release_units 1.{33: 'ね。'}
* W11. input: {34: 'はい、'} - output: release_units 1.{34: 'はい、'}
* W12. input: {35: '分解', 36: '完了。'} - output: release_units 1.{35: '分解', 36: '完了。'}

Reconfirm the RULEs and your task!


- retry: 2/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>これがギア</src>; start=0.00, end=1.00
* W1. <src>です。</src>; start=1.00, end=2.00
* W2. <src>ギアが緩む</src>; start=2.00, end=3.00
* W3. <src>と芯が</src>; start=3.00, end=4.00
* W4. <src>上げ下げできなくなって</src>; start=4.00, end=5.00
* W5. <src>しまうので、</src>; start=5.00, end=6.00
* W6. <src>ギアの先に</src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>役ねじのナットが</src>; start=8.00, end=9.00
* W9. <src>ついているっていうことです</src>; start=9.00, end=10.00
* W10. <src>ね。</src>; start=10.00, end=11.00
* W11. <src>はい、</src>; start=11.00, end=12.00
* W12. <src>分解完了。</src>; start=12.00, end=12.80
```

---
=== JA__gKKQYSi4mg_W000178 ===

status: finished

raw_text:
と今までのオープンデータだけだと、例えば災害の時たあのあこんなデータあればなって思ってたものとかももしかしたらあるかもしれないのでぜひ探してみてください。

word_indices:
* W0. {0: 'と', 1: '今', 2: 'まで'}
* W1. {3: 'の', 4: 'オープン', 5: 'データ'}
* W2. {6: 'だけ', 7: 'だ', 8: 'と、'}
* W3. {9: '例えば', 10: '災害', 11: 'の'}
* W4. {12: '時', 13: 'た', 14: 'あの'}
* W5. {15: 'あこんな', 16: 'データ', 17: 'あれ', 18: 'ば'}
* W6. {19: 'なって', 20: '思っ', 21: 'て', 22: 'た'}
* W7. {23: 'もの', 24: 'と', 25: 'か', 26: 'も'}
* W8. {27: 'もしかし', 28: 'たら', 29: 'ある', 30: 'か'}
* W9. {31: 'も', 32: 'しれ', 33: 'ない', 34: 'の', 35: 'で'}
* W10. {36: 'ぜひ', 37: '探し', 38: 'て', 39: 'み', 40: 'て'}
* W11. {41: 'ください。'}

scratchpad:
* W0. {0: 'と', 1: '今', 2: 'まで'}
  - carried_over: None
  - defer: 'と今まで' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [0,1,2]
  - release_units: None

* W1. {3: 'の', 4: 'オープン', 5: 'データ'}
  - carried_over: {0: 'と', 1: '今', 2: 'まで'}
  - defer: None
  - release_units:
    1. 'と', small discourse unit: [0]
    2. '今までの', bunsetsu unit: [1,2,3]
    3. 'オープンデータ', compound noun: [4,5]

* W2. {6: 'だけ', 7: 'だ', 8: 'と、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'だけだと、', stable minimal sense unit: [6,7,8]

* W3. {9: '例えば', 10: '災害', 11: 'の'}
  - carried_over: None
  - defer: None
  - release_units:
    1. '例えば', discourse unit: [9]
    2. '災害の', bunsetsu unit: [10,11]

* W4. {12: '時', 13: 'た', 14: 'あの'}
  - carried_over: None
  - defer: '時たあの' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [12,13,14]
  - release_units: None

* W5. {15: 'あこんな', 16: 'データ', 17: 'あれ', 18: 'ば'}
  - carried_over: {12: '時', 13: 'た', 14: 'あの'}
  - defer: None
  - release_units:
    1. '時', noun unit: [12]
    2. 'たあの', filler unit: [13,14]
    3. 'あこんなデータ', modifier-head unit: [15,16]
    4. 'あれば', conditional verb unit: [17,18]

* W6. {19: 'なって', 20: '思っ', 21: 'て', 22: 'た'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'なって', verb te-form: [19]
    2. '思ってた', verb phrase: [20,21,22]

* W7. {23: 'もの', 24: 'と', 25: 'か', 26: 'も'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'ものとかも', stable unit: [23,24,25,26]

* W8. {27: 'もしかし', 28: 'たら', 29: 'ある', 30: 'か'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'もしかしたら', set phrase: [27,28]
    2. 'あるか', verb+particle: [29,30]

* W9. {31: 'も', 32: 'しれ', 33: 'ない', 34: 'の', 35: 'で'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'かもしれない', set phrase: [31,32,33]
    2. 'ので', conjunction: [34,35]

* W10. {36: 'ぜひ', 37: '探し', 38: 'て', 39: 'み', 40: 'て'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'ぜひ', adverb: [36]
    2. '探してみて', verb phrase: [37,38,39,40]

* W11. {41: 'ください。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 'ください。', polite request: [41]

result:
[
  [0],
  [1,2,3],
  [4,5],
  [6,7,8],
  [9],
  [10,11],
  [12],
  [13,14],
  [15,16],
  [17,18],
  [19],
  [20,21,22],
  [23,24,25,26],
  [27,28],
  [29,30],
  [31,32,33],
  [34,35],
  [36],
  [37,38,39,40],
  [41]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>と</src>; start=0.00, end=1.00
* W1. <src>今までのオープンデータ</src>; start=1.00, end=2.00
* W2. <src>だけだと、</src>; start=2.00, end=3.00
* W3. <src>例えば災害の</src>; start=3.00, end=4.00
* W4. <src>時たあの</src>; start=4.00, end=5.00
* W5. <src>あこんなデータあれば</src>; start=5.00, end=6.00
* W6. <src>なって思ってた</src>; start=6.00, end=7.00
* W7. <src>ものとかも</src>; start=7.00, end=8.00
* W8. <src>もしかしたらあるか</src>; start=8.00, end=9.00
* W9. <src>もしれないので</src>; start=9.00, end=10.00
* W10. <src>ぜひ探してみて</src>; start=10.00, end=11.00
* W11. <src>ください。</src>; start=11.00, end=11.46
```

---
=== JA__gKKQYSi4mg_W000167 ===

status: finished

raw_text:
あの測量したデータになります。こういったデータであったり、これは奈良県の工事なんですけど。

word_indices:
* W0. {0: 'あの'}
* W1. {1: '測量', 2: 'し', 3: 'た'}
* W2. {4: 'データ', 5: 'に', 6: 'なり'}
* W3. {7: 'ます。'}
* W4. {8: 'こう', 9: 'いっ', 10: 'た'}
* W5. {11: 'データ', 12: 'で', 13: 'あっ', 14: 'たり、'}
* W6. {15: 'これ'}
* W7. {16: 'は', 17: '奈良', 18: '県'}
* W8. {19: 'の'}
* W9. {20: '工事', 21: 'な', 22: 'ん'}
* W10. {23: 'です', 24: 'けど。'}

scratchpad:
* W0. {0: 'あの'}
  - carried_over: None
  - defer: None
  - release_units:
    1. あの, stable minimal sense unit in the current window: [0]

* W1. {1: '測量', 2: 'し', 3: 'た'}
  - carried_over: None
  - defer: '測量した' does not yet form a stable minimal sense unit; defer it to the next window: [1,2,3]
  - release_units: None

* W2. {4: 'データ', 5: 'に', 6: 'なり'}
  - carried_over: {1: '測量', 2: 'し', 3: 'た'}
  - defer: 'になり' does not yet form a stable minimal sense unit; defer it to the next window: [5,6]
  - release_units:
    1. 測量したデータ, '測量した' is carried over from the previous window; released here because it is now a stable minimal sense unit: [1,2,3,4]

* W3. {7: 'ます。'}
  - carried_over: {5: 'に', 6: 'なり'}
  - defer: None
  - release_units:
    1. になります。, 'になり' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7]

* W4. {8: 'こう', 9: 'いっ', 10: 'た'}
  - carried_over: None
  - defer: None
  - release_units:
    1. こういった, stable minimal sense unit in the current window: [8,9,10]

* W5. {11: 'データ', 12: 'で', 13: 'あっ', 14: 'たり、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. データであったり、, stable minimal sense unit in the current window: [11,12,13,14]

* W6. {15: 'これ'}
  - carried_over: None
  - defer: 'これ' does not yet form a stable minimal sense unit; defer it to the next window: [15]
  - release_units: None

* W7. {16: 'は', 17: '奈良', 18: '県'}
  - carried_over: {15: 'これ'}
  - defer: '奈良県' does not yet form a stable minimal sense unit; defer it to the next window: [17,18]
  - release_units:
    1. これは, 'これ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [15,16]

* W8. {19: 'の'}
  - carried_over: {17: '奈良', 18: '県'}
  - defer: '奈良県の' does not yet form a stable minimal sense unit; defer it to the next window: [17,18,19]
  - release_units: None

* W9. {20: '工事', 21: 'な', 22: 'ん'}
  - carried_over: {17: '奈良', 18: '県', 19: 'の'}
  - defer: 'なん' does not yet form a stable minimal sense unit; defer it to the next window: [21,22]
  - release_units:
    1. 奈良県の工事, '奈良県の' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19,20]

* W10. {23: 'です', 24: 'けど。'}
  - carried_over: {21: 'な', 22: 'ん'}
  - defer: None
  - release_units:
    1. なんですけど。, 'なん' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22,23,24]

result:
[
  [0],
  [1,2,3,4],
  [5,6,7],
  [8,9,10],
  [11,12,13,14],
  [15,16],
  [17,18,19,20],
  [21,22,23,24]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>あの</src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>測量したデータ</src>; start=2.00, end=3.00
* W3. <src>になります。</src>; start=3.00, end=4.00
* W4. <src>こういった</src>; start=4.00, end=5.00
* W5. <src>データであったり、</src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>これは</src>; start=7.00, end=8.00
* W8. <src><|wait|></src>; start=8.00, end=9.00
* W9. <src>奈良県の工事</src>; start=9.00, end=10.00
* W10. <src>なんですけど。</src>; start=10.00, end=10.53
```

---
