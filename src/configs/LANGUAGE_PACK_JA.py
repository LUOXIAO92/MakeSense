# --- TIME WINDOW PRESSURED SEGMENTATION ---

TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

raw_text: "個人的には思ったんですけれども私前回の封筒ファイルの時もそうだったんですがこのなんか私こうしっかりしてないとダメみたいで私はこのデザインペーパーにクラフトボードをまた使いましたなのでかなりしっかりした出来栄えになっていると思いますここも何で止めようか迷って"

word_indices: 
* W0. {0: '個人的', 1: 'に', 2: 'は'}
* W1. {3: '思っ', 4: 'た', 5: 'ん', 6: 'です', 7: 'けれど'}
* W2. {8: 'も'}
* W3. {9: '私', 10: '前回', 11: 'の'}
* W4. {12: '封筒', 13: 'ファイル', 14: 'の', 15: '時', 16: 'も', 17: 'そう'}
* W5. {18: 'だっ', 19: 'た', 20: 'ん', 21: 'です'}
* W6. {}
* W7. {}
* W8. {22: 'が', 23: 'この', 24: 'なんか', 25: '私', 26: 'こう', 27: 'しっかり'}
* W9. {28: 'し', 29: 'て', 30: 'ない', 31: 'と', 32: 'ダメ'}
* W10. {33: 'みたい'}
* W11. {34: 'で', 35: '私'}
* W12. {}
* W13. {}
* W14. {36: 'は', 37: 'この', 38: 'デザイン'}
* W15. {39: 'ペーパー'}
* W16. {40: 'に', 41: 'クラフト'}
* W17. {42: 'ボード', 43: 'を'}
* W18. {44: 'また', 45: '使い', 46: 'まし'}
* W19. {47: 'た', 48: 'な', 49: 'の'}
* W20. {50: 'で'}
* W21. {51: 'かなり'}
* W22. {52: 'しっかり', 53: 'し'}
* W23. {54: 'た', 55: '出来栄え'}
* W24. {56: 'に', 57: 'なっ'}
* W25. {58: 'て', 59: 'いる', 60: 'と', 61: '思い'}
* W26. {}
* W27. {62: 'ます', 63: 'ここ', 64: 'も'}
* W28. {65: '何', 66: 'で', 67: '止めよう', 68: 'か'}
* W29. {69: '迷っ', 70: 'て'}

<scratchpad>
* W0. {0: '個人的', 1: 'に', 2: 'は'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 個人的には, stable minimal sense unit in the current window: [0,1,2]

* W1. {3: '思っ', 4: 'た', 5: 'ん', 6: 'です', 7: 'けれど'}
  - carried_over: None
  - defer: 'けれど' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [7]
  - release_units:
    1. 思ったんです, stable minimal sense unit in the current window: [3,4,5,6]

* W2. {8: 'も'}
  - carried_over: {7: 'けれど'}
  - defer: None
  - release_units:
    1. けれども, 'けれど' is carried over from the previous window; released here because it is now a stable minimal sense unit: [7,8]

* W3. {9: '私', 10: '前回', 11: 'の'}
  - carried_over: None
  - defer: '前回の' is not yet the best stable minimal sense unit in the current window; defer it to the next window: [10,11]
  - release_units:
    1. 私, stable minimal sense unit in the current window: [9]

* W4. {12: '封筒', 13: 'ファイル', 14: 'の', 15: '時', 16: 'も', 17: 'そう'}
  - carried_over: {10: '前回', 11: 'の'}
  - defer: 'そう' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [17]
  - release_units:
    1. 前回の, '前回の' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11]
    2. 封筒ファイルの時も, stable minimal sense unit in the current window: [12,13,14,15,16]

* W5. {18: 'だっ', 19: 'た', 20: 'ん', 21: 'です'}
  - carried_over: {17: 'そう'}
  - defer: None
  - release_units:
    1. そうだったんです, 'そう' is carried over from the previous window; released here as the best locally available minimal sense unit under the current window-bounded constraint, even though a host-dependent tail appears later in the stream: [17,18,19,20,21]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W8. {22: 'が', 23: 'この', 24: 'なんか', 25: '私', 26: 'こう', 27: 'しっかり'}
  - carried_over: None
  - defer: '私こうしっかり' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material and only the remainder should move forward: [25,26,27]
  - release_units:
    1. が, this host-dependent tail is released separately here as a legal exception because its host phrase was already emitted in the previous window: [22]
    2. このなんか, stable minimal sense unit in the current window: [23,24]

* W9. {28: 'し', 29: 'て', 30: 'ない', 31: 'と', 32: 'ダメ'}
  - carried_over: {25: '私', 26: 'こう', 27: 'しっかり'}
  - defer: 'ダメ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [32]
  - release_units:
    1. 私, '私' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25]
    2. こうしっかりしてないと, 'こうしっかり' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27,28,29,30,31]

* W10. {33: 'みたい'}
  - carried_over: {32: 'ダメ'}
  - defer: 'ダメみたい' is not yet the best stable minimal sense unit in the current window; defer it to the next window: [32,33]
  - release_units: None

* W11. {34: 'で', 35: '私'}
  - carried_over: {32: 'ダメ', 33: 'みたい'}
  - defer: None
  - release_units:
    1. ダメみたいで, 'ダメみたい' is carried over from the previous window; released here because it is now a stable minimal sense unit: [32,33,34]
    2. 私, stable minimal sense unit in the current window: [35]

* W12. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W13. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W14. {36: 'は', 37: 'この', 38: 'デザイン'}
  - carried_over: None
  - defer: 'このデザイン' is not yet the best stable minimal sense unit in the current window; defer it to the next window because the current window must already flush after empty windows and only the remainder should move forward: [37,38]
  - release_units:
    1. は, latency-forced partial release; the current window must emit something now, and no better local unit beginning at は is available: [36]

* W15. {39: 'ペーパー'}
  - carried_over: {37: 'この', 38: 'デザイン'}
  - defer: None
  - release_units:
    1. このデザインペーパー, 'このデザイン' is carried over from the previous window; released here because it is now a stable minimal sense unit: [37,38,39]

* W16. {40: 'に', 41: 'クラフト'}
  - carried_over: None
  - defer: 'にクラフト' is not yet the best stable minimal sense unit in the current window; defer it to the next window: [40,41]
  - release_units: None

* W17. {42: 'ボード', 43: 'を'}
  - carried_over: {40: 'に', 41: 'クラフト'}
  - defer: None
  - release_units:
    1. に, latency-forced partial release; the current window must emit something now after a no-output window, and no better local unit beginning at に is available: [40]
    2. クラフトボードを, 'クラフト' is carried over from the previous window; released here because it is now a stable minimal sense unit: [41,42,43]

* W18. {44: 'また', 45: '使い', 46: 'まし'}
  - carried_over: None
  - defer: 'また使いまし' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [44,45,46]
  - release_units: None

* W19. {47: 'た', 48: 'な', 49: 'の'}
  - carried_over: {44: 'また', 45: '使い', 46: 'まし'}
  - defer: 'なの' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [48,49]
  - release_units:
    1. また使いました, 'また使いまし' is carried over from the previous window; released here because it is now a stable minimal sense unit: [44,45,46,47]

* W20. {50: 'で'}
  - carried_over: {48: 'な', 49: 'の'}
  - defer: None
  - release_units:
    1. なので, 'なの' is carried over from the previous window; released here because it is now a stable minimal sense unit: [48,49,50]

* W21. {51: 'かなり'}
  - carried_over: None
  - defer: None
  - release_units:
    1. かなり, stable minimal sense unit in the current window: [51]

* W22. {52: 'しっかり', 53: 'し'}
  - carried_over: None
  - defer: 'しっかりし' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [52,53]
  - release_units: None

* W23. {54: 'た', 55: '出来栄え'}
  - carried_over: {52: 'しっかり', 53: 'し'}
  - defer: None
  - release_units:
    1. しっかりした出来栄え, 'しっかりし' is carried over from the previous window; released here because it is now a stable minimal sense unit: [52,53,54,55]

* W24. {56: 'に', 57: 'なっ'}
  - carried_over: None
  - defer: 'になっ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [56,57]
  - release_units: None

* W25. {58: 'て', 59: 'いる', 60: 'と', 61: '思い'}
  - carried_over: {56: 'に', 57: 'なっ'}
  - defer: 'と思い' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [60,61]
  - release_units:
    1. になっている, 'になっ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [56,57,58,59]

* W26. {}
  - carried_over: {60: 'と', 61: '思い'}
  - defer: 'と思い' still does not yet form the best stable release unit / minimal sense unit here; continue deferring it across the empty window because no new material arrives in the current window: [60,61]
  - release_units: None

* W27. {62: 'ます', 63: 'ここ', 64: 'も'}
  - carried_over: {60: 'と', 61: '思い'}
  - defer: None
  - release_units:
    1. と思います, 'と思い' is carried over from the previous window; released here because it is now a stable minimal sense unit: [60,61,62]
    2. ここも, stable minimal sense unit in the current window: [63,64]

* W28. {65: '何', 66: 'で', 67: '止めよう', 68: 'か'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 何で止めようか, stable minimal sense unit in the current window: [65,66,67,68]

* W29. {69: '迷っ', 70: 'て'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 迷って, latency-forced partial release at stream end because the source itself cuts off before a fuller continuation arrives: [69,70]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4,5,6],
  [7,8],
  [9],
  [10,11],
  [12,13,14,15,16],
  [17,18,19,20,21],
  [22],
  [23,24],
  [25],
  [26,27,28,29,30,31],
  [32,33,34],
  [35],
  [36],
  [37,38,39],
  [40],
  [41,42,43],
  [44,45,46,47],
  [48,49,50],
  [51],
  [52,53,54,55],
  [56,57,58,59],
  [60,61,62],
  [63,64],
  [65,66,67,68],
  [69,70]
]
</result>


## Sample 2:

raw_text: "ただ、それがまあ弱みとはいえ、その反面ね、人数が多いからこそ、できる、強さというものも、相対的に大きくなってきます。例えばですけど、え、まあ、案件とか。"

word_indices:
* W0. {0: 'ただ', 1: '、'}
* W1. {2: 'それ', 3: 'が', 4: 'まあ', 5: '弱み', 6: 'と'}
* W2. {7: 'は'}
* W3. {8: 'いえ', 9: '、', 10: 'その', 11: '反面'}
* W4. {12: 'ね', 13: '、', 14: '人数', 15: 'が'}
* W5. {16: '多い', 17: 'から', 18: 'こそ', 19: '、'}
* W6. {}
* W7. {20: 'できる', 21: '、', 22: '強さ', 23: 'と', 24: 'いう', 25: 'もの'}
* W8. {26: 'も', 27: '、', 28: '相対的', 29: 'に'}
* W9. {30: '大きく', 31: 'なっ', 32: 'て', 33: 'き'}
* W10. {34: 'ます', 35: '。', 36: '例えば', 37: 'です'}
* W11. {38: 'けど', 39: '、'}
* W12. {40: 'え', 41: '、', 42: 'まあ', 43: '、'}
* W13. {44: '案件', 45: 'と', 46: 'か', 47: '。'}

<scratchpad>
* W0. {0: 'ただ', 1: '、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. ただ、, stable minimal sense unit in the current window: [0,1]

* W1. {2: 'それ', 3: 'が', 4: 'まあ', 5: '弱み', 6: 'と'}
  - carried_over: None
  - defer: '弱みと' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [5,6]
  - release_units:
    1. それが, stable minimal sense unit in the current window: [2,3]
    2. まあ, stable minimal sense unit in the current window: [4]

* W2. {7: 'は'}
  - carried_over: {5: '弱み', 6: 'と'}
  - defer: '弱みとは' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [5,6,7]
  - release_units: None

* W3. {8: 'いえ', 9: '、', 10: 'その', 11: '反面'}
  - carried_over: {5: '弱み', 6: 'と', 7: 'は'}
  - defer: 'その反面' is not yet the best stable minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [10,11]
  - release_units:
    1. 弱みとはいえ、, '弱みとは' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7,8,9]

* W4. {12: 'ね', 13: '、', 14: '人数', 15: 'が'}
  - carried_over: {10: 'その', 11: '反面'}
  - defer: None
  - release_units:
    1. その反面ね、, 'その反面' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12,13]
    2. 人数が, stable minimal sense unit in the current window: [14,15]

* W5. {16: '多い', 17: 'から', 18: 'こそ', 19: '、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 多いからこそ、, stable minimal sense unit in the current window: [16,17,18,19]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {20: 'できる', 21: '、', 22: '強さ', 23: 'と', 24: 'いう', 25: 'もの'}
  - carried_over: None
  - defer: '強さというもの' is not yet the best stable minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [22,23,24,25]
  - release_units:
    1. できる、, stable minimal sense unit in the current window: [20,21]

* W8. {26: 'も', 27: '、', 28: '相対的', 29: 'に'}
  - carried_over: {22: '強さ', 23: 'と', 24: 'いう', 25: 'もの'}
  - defer: None
  - release_units:
    1. 強さというものも、, '強さというもの' is carried over from the previous window; released here because it is now a stable minimal sense unit: [22,23,24,25,26,27]
    2. 相対的に, stable minimal sense unit in the current window: [28,29]

* W9. {30: '大きく', 31: 'なっ', 32: 'て', 33: 'き'}
  - carried_over: None
  - defer: '大きくなってき' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [30,31,32,33]
  - release_units: None

* W10. {34: 'ます', 35: '。', 36: '例えば', 37: 'です'}
  - carried_over: {30: '大きく', 31: 'なっ', 32: 'て', 33: 'き'}
  - defer: '例えばです' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [36,37]
  - release_units:
    1. 大きくなってきます。, '大きくなってき' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32,33,34,35]

* W11. {38: 'けど', 39: '、'}
  - carried_over: {36: '例えば', 37: 'です'}
  - defer: None
  - release_units:
    1. 例えばですけど、, '例えばです' is carried over from the previous window; released here because it is now a stable minimal sense unit: [36,37,38,39]

* W12. {40: 'え', 41: '、', 42: 'まあ', 43: '、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. え、, stable minimal sense unit in the current window: [40,41]
    2. まあ、, stable minimal sense unit in the current window: [42,43]

* W13. {44: '案件', 45: 'と', 46: 'か', 47: '。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 案件とか。, stable minimal sense unit in the current window: [44,45,46,47]
</scratchpad>
<result>
[
  [0,1],
  [2,3],
  [4],
  [5,6,7,8,9],
  [10,11,12,13],
  [14,15],
  [16,17,18,19],
  [20,21],
  [22,23,24,25,26,27],
  [28,29],
  [30,31,32,33,34,35],
  [36,37,38,39],
  [40,41],
  [42,43],
  [44,45,46,47]
]
</result>


## Sample 3:

<scratchpad>
* W0. {0: '一'}
  - carried_over: None
  - defer: '一' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [0]
  - release_units: None

* W1. {1: '決定戦'}
  - carried_over: {0: '一'}
  - defer: None
  - release_units:
    1. 一決定戦, '一' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1]

* W2. {2: ',DBS'}
  - carried_over: None
  - defer: ',DBS' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [2]
  - release_units: None

* W3. {3: 'という', 4: '当', 5: '時の'}
  - carried_over: {2: ',DBS'}
  - defer: None
  - release_units:
    1. ,DBSという, ',DBS' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3]
    2. 当時の, stable minimal sense unit in the current window: [4,5]

* W4. {6: 'ジャ', 7: 'ニ'}
  - carried_over: None
  - defer: 'ジャニ' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [6,7]
  - release_units: None

* W5. {8: 'ー氏の情', 9: '愛', 10: '事'}
  - carried_over: {6: 'ジャ', 7: 'ニ'}
  - defer: '事' is not yet enough to complete the fixed unit 情愛事情 in the current window; defer it to the next window because the current window must already flush after a no-output window and only the remainder should move forward: [10]
  - release_units:
    1. ジャニー氏の情愛, 'ジャニ' is carried over from the previous window; non-ideal release unit caused by tokenization error and window pressure: the fixed unit 情愛事情 is split across windows by the tokenization, and the current window must emit something now after a no-output window, so only the locally best partial release can be emitted here: [6,7,8,9]

* W6. {11: '情が', 12: 'くっ', 13: 'き'}
  - carried_over: {10: '事'}
  - defer: 'くっき' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [12,13]
  - release_units:
    1. 事情が, '事' is carried over from the previous window; non-ideal release unit continued here as a legal exception because the fixed unit 情愛事情 was forced to split across windows by tokenization error and its earlier part was already emitted in the previous window: [10,11]

* W7. {14: 'り反映さ', 15: 'れた', 16: '奇', 17: '妙'}
  - carried_over: {12: 'くっ', 13: 'き'}
  - defer: '奇妙' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [16,17]
  - release_units:
    1. くっきり反映された, 'くっき' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13,14,15]

* W8. {18: 'な', 19: 'テレ', 20: 'ビ'}
  - carried_over: {16: '奇', 17: '妙'}
  - defer: 'テレビ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [19,20]
  - release_units:
    1. 奇妙な, '奇妙' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17,18]

* W9. {21: '番組も', 22: '放送', 23: 'さ'}
  - carried_over: {19: 'テレ', 20: 'ビ'}
  - defer: '放送さ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [22,23]
  - release_units:
    1. テレビ番組も, 'テレビ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20,21]

* W10. {24: 'れて', 25: 'い', 26: 'る', 27: '。'}
  - carried_over: {22: '放送', 23: 'さ'}
  - defer: None
  - release_units:
    1. 放送されている。, '放送さ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [22,23,24,25,26,27]
</scratchpad>
<result>
[
  [0,1],
  [2,3],
  [4,5],
  [6,7,8,9],
  [10,11],
  [12,13,14,15],
  [16,17,18],
  [19,20,21],
  [22,23,24,25,26,27]
]
</result>


## Sample 4:

raw_text: "それなら、私も思ってまーす、ということで。ま、このまま、そのまま、レビューをするわけですけども。実は、この演習業がレンズですね。昼間も撮影できるんですね。ま、こういう感じで、えぇ、写真が撮れます。すごい、昼間、写真撮っても、ちょっとなんか、アーティスティックな感じで撮れるっていうんですかね。これ、オートフォーカスのレンズではないので、マニュアルフォーカスの"

word_indices:
* W0. {0: 'それ', 1: 'なら', 2: '、', 3: '私'}
* W1. {4: 'も', 5: '思っ', 6: 'て'}
* W2. {7: 'まー', 8: 'す', 9: '、', 10: 'と', 11: 'いう'}
* W3. {12: 'こと', 13: 'で', 14: '。', 15: 'ま', 16: '、', 17: 'この', 18: 'まま', 19: '、'}
* W4. {20: 'そのまま', 21: '、', 22: 'レビュー', 23: 'を', 24: 'する'}
* W5. {25: 'わけ', 26: 'です', 27: 'けど'}
* W6. {28: 'も', 29: '。', 30: '実', 31: 'は', 32: '、', 33: 'この', 34: '演習', 35: '業', 36: 'が'}
* W7. {37: 'レンズ', 38: 'です', 39: 'ね', 40: '。', 41: '昼間'}
* W8. {42: 'も', 43: '撮影', 44: 'できる', 45: 'ん', 46: 'です'}
* W9. {47: 'ね', 48: '。', 49: 'ま', 50: '、', 51: 'こう'}
* W10. {52: 'いう', 53: '感じ'}
* W11. {54: 'で', 55: '、', 56: 'えぇ', 57: '、', 58: '写真'}
* W12. {59: 'が', 60: '撮れ'}
* W13. {61: 'ます', 62: '。', 63: 'すごい', 64: '、'}
* W14. {65: '昼間', 66: '、', 67: '写真', 68: '撮っ', 69: 'て'}
* W15. {70: 'も', 71: '、', 72: 'ちょっと'}
* W16. {73: 'なんか', 74: '、', 75: 'アーティスティック'}
* W17. {76: 'な', 77: '感じ', 78: 'で'}
* W18. {79: '撮れる', 80: 'って', 81: 'いう', 82: 'ん', 83: 'です', 84: 'か'}
* W19. {85: 'ね', 86: '。', 87: 'これ', 88: '、'}
* W20. {89: 'オートフォーカス', 90: 'の'}
* W21. {91: 'レンズ', 92: 'で', 93: 'は', 94: 'ない', 95: 'の', 96: 'で', 97: '、'}
* W22. {98: 'マニュアル', 99: 'フォーカス', 100: 'の'}

<scratchpad>
* W0. {0: 'それ', 1: 'なら', 2: '、', 3: '私'}
  - carried_over: None
  - defer: '私' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [3]
  - release_units:
    1. それなら、, stable minimal sense unit in the current window: [0,1,2]

* W1. {4: 'も', 5: '思っ', 6: 'て'}
  - carried_over: {3: '私'}
  - defer: '思って' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [5,6]
  - release_units:
    1. 私も, '私' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3,4]

* W2. {7: 'まー', 8: 'す', 9: '、', 10: 'と', 11: 'いう'}
  - carried_over: {5: '思っ', 6: 'て'}
  - defer: 'という' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [10,11]
  - release_units:
    1. 思ってまーす、, '思って' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7,8,9]

* W3. {12: 'こと', 13: 'で', 14: '。', 15: 'ま', 16: '、', 17: 'この', 18: 'まま', 19: '、'}
  - carried_over: {10: 'と', 11: 'いう'}
  - defer: None
  - release_units:
    1. ということで。, 'という' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12,13,14]
    2. ま、, stable minimal sense unit in the current window: [15,16]
    3. このまま、, stable minimal sense unit in the current window: [17,18,19]

* W4. {20: 'そのまま', 21: '、', 22: 'レビュー', 23: 'を', 24: 'する'}
  - carried_over: None
  - defer: None
  - release_units:
    1. そのまま、, stable minimal sense unit in the current window: [20,21]
    2. レビューをする, stable minimal sense unit in the current window: [22,23,24]

* W5. {25: 'わけ', 26: 'です', 27: 'けど'}
  - carried_over: None
  - defer: 'わけですけど' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [25,26,27]
  - release_units: None

* W6. {28: 'も', 29: '。', 30: '実', 31: 'は', 32: '、', 33: 'この', 34: '演習', 35: '業', 36: 'が'}
  - carried_over: {25: 'わけ', 26: 'です', 27: 'けど'}
  - defer: None
  - release_units:
    1. わけですけども。, 'わけですけど' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26,27,28,29]
    2. 実は、, stable minimal sense unit in the current window: [30,31,32]
    3. この演習業が, stable minimal sense unit in the current window: [33,34,35,36]

* W7. {37: 'レンズ', 38: 'です', 39: 'ね', 40: '。', 41: '昼間'}
  - carried_over: None
  - defer: '昼間' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [41]
  - release_units:
    1. レンズですね。, stable minimal sense unit in the current window: [37,38,39,40]

* W8. {42: 'も', 43: '撮影', 44: 'できる', 45: 'ん', 46: 'です'}
  - carried_over: {41: '昼間'}
  - defer: '撮影できるんです' is not yet the best stable minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [43,44,45,46]
  - release_units:
    1. 昼間も, '昼間' is carried over from the previous window; released here because it is now a stable minimal sense unit: [41,42]

* W9. {47: 'ね', 48: '。', 49: 'ま', 50: '、', 51: 'こう'}
  - carried_over: {43: '撮影', 44: 'できる', 45: 'ん', 46: 'です'}
  - defer: 'こう' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [51]
  - release_units:
    1. 撮影できるんですね。, '撮影できるんです' is carried over from the previous window; released here because it is now a stable minimal sense unit: [43,44,45,46,47,48]
    2. ま、, stable minimal sense unit in the current window: [49,50]

* W10. {52: 'いう', 53: '感じ'}
  - carried_over: {51: 'こう'}
  - defer: 'こういう感じ' is not yet the best stable minimal sense unit in the current window; defer it to the next window: [51,52,53]
  - release_units: None

* W11. {54: 'で', 55: '、', 56: 'えぇ', 57: '、', 58: '写真'}
  - carried_over: {51: 'こう', 52: 'いう', 53: '感じ'}
  - defer: '写真' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [58]
  - release_units:
    1. こういう感じで、, 'こういう感じ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [51,52,53,54,55]
    2. えぇ、, stable minimal sense unit in the current window: [56,57]

* W12. {59: 'が', 60: '撮れ'}
  - carried_over: {58: '写真'}
  - defer: '撮れ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [60]
  - release_units:
    1. 写真が, '写真' is carried over from the previous window; released here because it is now a stable minimal sense unit: [58,59]

* W13. {61: 'ます', 62: '。', 63: 'すごい', 64: '、'}
  - carried_over: {60: '撮れ'}
  - defer: None
  - release_units:
    1. 撮れます。, '撮れ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [60,61,62]
    2. すごい、, stable minimal sense unit in the current window: [63,64]

* W14. {65: '昼間', 66: '、', 67: '写真', 68: '撮っ', 69: 'て'}
  - carried_over: None
  - defer: '写真撮って' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [67,68,69]
  - release_units:
    1. 昼間、, stable minimal sense unit in the current window: [65,66]

* W15. {70: 'も', 71: '、', 72: 'ちょっと'}
  - carried_over: {67: '写真', 68: '撮っ', 69: 'て'}
  - defer: 'ちょっと' is not yet the best stable minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [72]
  - release_units:
    1. 写真撮っても、, '写真撮って' is carried over from the previous window; released here because it is now a stable minimal sense unit: [67,68,69,70,71]

* W16. {73: 'なんか', 74: '、', 75: 'アーティスティック'}
  - carried_over: {72: 'ちょっと'}
  - defer: 'アーティスティック' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [75]
  - release_units:
    1. ちょっとなんか、, 'ちょっと' is carried over from the previous window; released here because it is now a stable minimal sense unit: [72,73,74]

* W17. {76: 'な', 77: '感じ', 78: 'で'}
  - carried_over: {75: 'アーティスティック'}
  - defer: None
  - release_units:
    1. アーティスティックな感じで, 'アーティスティック' is carried over from the previous window; released here because it is now a stable minimal sense unit: [75,76,77,78]

* W18. {79: '撮れる', 80: 'って', 81: 'いう', 82: 'ん', 83: 'です', 84: 'か'}
  - carried_over: None
  - defer: '撮れるっていうんですか' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [79,80,81,82,83,84]
  - release_units: None

* W19. {85: 'ね', 86: '。', 87: 'これ', 88: '、'}
  - carried_over: {79: '撮れる', 80: 'って', 81: 'いう', 82: 'ん', 83: 'です', 84: 'か'}
  - defer: None
  - release_units:
    1. 撮れるっていうんですかね。, '撮れるっていうんですか' is carried over from the previous window; released here because it is now a stable minimal sense unit: [79,80,81,82,83,84,85,86]
    2. これ、, stable minimal sense unit in the current window: [87,88]

* W20. {89: 'オートフォーカス', 90: 'の'}
  - carried_over: None
  - defer: None
  - release_units:
    1. オートフォーカスの, stable minimal sense unit in the current window: [89,90]

* W21. {91: 'レンズ', 92: 'で', 93: 'は', 94: 'ない', 95: 'の', 96: 'で', 97: '、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. レンズではないので、, non-ideal release unit; this continuation is released here because the modifier-like local unit オートフォーカスの was already emitted in the previous window: [91,92,93,94,95,96,97]

* W22. {98: 'マニュアル', 99: 'フォーカス', 100: 'の'}
  - carried_over: None
  - defer: None
  - release_units:
    1. マニュアルフォーカスの, stable minimal sense unit in the current window: [98,99,100]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4],
  [5,6,7,8,9],
  [10,11,12,13,14],
  [15,16],
  [17,18,19],
  [20,21],
  [22,23,24],
  [25,26,27,28,29],
  [30,31,32],
  [33,34,35,36],
  [37,38,39,40],
  [41,42],
  [43,44,45,46,47,48],
  [49,50],
  [51,52,53,54,55],
  [56,57],
  [58,59],
  [60,61,62],
  [63,64],
  [65,66],
  [67,68,69,70,71],
  [72,73,74],
  [75,76,77,78],
  [79,80,81,82,83,84,85,86],
  [87,88],
  [89,90],
  [91,92,93,94,95,96,97],
  [98,99,100]
]
</result>


## Sample 5:

raw_text: "ね。普通の8ビートに戻ったりね。フィルイン挟んでこういう練習をしてもらえると、頭打ち。で、頭打ちはどこに入れてもいいので、停滞させる感じ。それと、もう一つは、イントロとかサビで使うと、スネアが多いんで盛り上がるんですよ。特に最後の盛り上がったところ盛り上がりきるときに6番なんか足使うと、めっちゃ盛り上がるんで、エンディングなんかでも最後同じこと繰り返してると、途中から頭打ちにしちゃうっていうのも一つの手ですね。頭打ちするとき盛り上げたかったらシンバルにしちゃう。"

word_indices:
* W0. {0: 'ね', 1: '。', 2: '普通', 3: 'の', 4: '8'}
* W1. {5: 'ビート', 6: 'に', 7: '戻っ', 8: 'たり'}
* W2. {9: 'ね', 10: '。', 11: 'フィルイン', 12: '挟ん', 13: 'で'}
* W3. {14: 'こう', 15: 'いう', 16: '練習', 17: 'を', 18: 'し', 19: 'て'}
* W4. {20: 'もらえる', 21: 'と', 22: '、'}
* W5. {23: '頭打ち', 24: '。', 25: 'で', 26: '、'}
* W6. {27: '頭打ち', 28: 'は', 29: 'どこ', 30: 'に', 31: '入れ', 32: 'て', 33: 'も', 34: 'いい', 35: 'の'}
* W7. {36: 'で', 37: '、', 38: '停滞', 39: 'さ'}
* W8. {40: 'せる', 41: '感じ', 42: '。', 43: 'それ'}
* W9. {44: 'と', 45: '、', 46: 'もう', 47: '一', 48: 'つ', 49: 'は', 50: '、'}
* W10. {51: 'イントロ', 52: 'と', 53: 'か', 54: 'サビ'}
* W11. {55: 'で'}
* W12. {56: '使う', 57: 'と', 58: '、', 59: 'スネア', 60: 'が', 61: '多い', 62: 'ん', 63: 'で'}
* W13. {64: '盛り上がる', 65: 'ん', 66: 'です'}
* W14. {67: 'よ', 68: '。', 69: '特に', 70: '最後'}
* W15. {71: 'の', 72: '盛り上がっ', 73: 'た'}
* W16. {74: 'ところ', 75: '盛り上がり', 76: 'きる'}
* W17. {77: 'とき', 78: 'に', 79: '6', 80: '番'}
* W18. {81: 'なんか', 82: '足', 83: '使う', 84: 'と', 85: '、'}
* W19. {86: 'めっちゃ', 87: '盛り上がる', 88: 'ん'}
* W20. {89: 'で', 90: '、', 91: 'エンディング'}
* W21. {92: 'なんか', 93: 'で', 94: 'も', 95: '最後'}
* W22. {96: '同じ', 97: 'こと', 98: '繰り返し', 99: 'てる'}
* W23. {100: 'と', 101: '、', 102: '途中', 103: 'から'}
* W24. {104: '頭打ち', 105: 'に', 106: 'し', 107: 'ちゃう', 108: 'って', 109: 'いう', 110: 'の', 111: 'も', 112: '一'}
* W25. {113: 'つ', 114: 'の', 115: '手', 116: 'です'}
* W26. {117: 'ね', 118: '。', 119: '頭打ち', 120: 'する', 121: 'とき'}
* W27. {122: '盛り上げ', 123: 'たかっ', 124: 'たら', 125: 'シンバル'}
* W28. {126: 'に', 127: 'し', 128: 'ちゃう', 129: '。'}

<scratchpad>
* W0. {0: 'ね', 1: '。', 2: '普通', 3: 'の', 4: '8'}
  - carried_over: None
  - defer: '普通の8' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [2,3,4]
  - release_units:
    1. ね。, stable minimal sense unit in the current window: [0,1]

* W1. {5: 'ビート', 6: 'に', 7: '戻っ', 8: 'たり'}
  - carried_over: {2: '普通', 3: 'の', 4: '8'}
  - defer: '戻ったり' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [7,8]
  - release_units:
    1. 普通の8ビートに, '普通の8' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4,5,6]

* W2. {9: 'ね', 10: '。', 11: 'フィルイン', 12: '挟ん', 13: 'で'}
  - carried_over: {7: '戻っ', 8: 'たり'}
  - defer: None
  - release_units:
    1. 戻ったりね。, '戻ったり' is carried over from the previous window; released here because it is now a stable minimal sense unit: [7,8,9,10]
    2. フィルイン挟んで, stable minimal sense unit in the current window: [11,12,13]

* W3. {14: 'こう', 15: 'いう', 16: '練習', 17: 'を', 18: 'し', 19: 'て'}
  - carried_over: None
  - defer: 'して' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [18,19]
  - release_units:
    1. こういう練習を, stable minimal sense unit in the current window: [14,15,16,17]

* W4. {20: 'もらえる', 21: 'と', 22: '、'}
  - carried_over: {18: 'し', 19: 'て'}
  - defer: None
  - release_units:
    1. してもらえると、, 'して' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20,21,22]

* W5. {23: '頭打ち', 24: '。', 25: 'で', 26: '、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 頭打ち。, stable minimal sense unit in the current window: [23,24]
    2. で、, stable minimal sense unit in the current window: [25,26]

* W6. {27: '頭打ち', 28: 'は', 29: 'どこ', 30: 'に', 31: '入れ', 32: 'て', 33: 'も', 34: 'いい', 35: 'の'}
  - carried_over: None
  - defer: 'いいの' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [34,35]
  - release_units:
    1. 頭打ちは, stable minimal sense unit in the current window: [27,28]
    2. どこに, stable minimal sense unit in the current window: [29,30]
    3. 入れても, stable minimal sense unit in the current window: [31,32,33]

* W7. {36: 'で', 37: '、', 38: '停滞', 39: 'さ'}
  - carried_over: {34: 'いい', 35: 'の'}
  - defer: '停滞さ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [38,39]
  - release_units:
    1. いいので、, 'いいの' is carried over from the previous window; released here because it is now a stable minimal sense unit: [34,35,36,37]

* W8. {40: 'せる', 41: '感じ', 42: '。', 43: 'それ'}
  - carried_over: {38: '停滞', 39: 'さ'}
  - defer: 'それ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [43]
  - release_units:
    1. 停滞させる感じ。, '停滞さ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [38,39,40,41,42]

* W9. {44: 'と', 45: '、', 46: 'もう', 47: '一', 48: 'つ', 49: 'は', 50: '、'}
  - carried_over: {43: 'それ'}
  - defer: None
  - release_units:
    1. それと、, 'それ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [43,44,45]
    2. もう一つは、, stable minimal sense unit in the current window: [46,47,48,49,50]

* W10. {51: 'イントロ', 52: 'と', 53: 'か', 54: 'サビ'}
  - carried_over: None
  - defer: 'サビ' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [54]
  - release_units:
    1. イントロとか, stable minimal sense unit in the current window: [51,52,53]

* W11. {55: 'で'}
  - carried_over: {54: 'サビ'}
  - defer: None
  - release_units:
    1. サビで, 'サビ' is carried over from the previous window; released here because it is now a stable minimal sense unit: [54,55]

* W12. {56: '使う', 57: 'と', 58: '、', 59: 'スネア', 60: 'が', 61: '多い', 62: 'ん', 63: 'で'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 使うと、, stable minimal sense unit in the current window: [56,57,58]
    2. スネアが, stable minimal sense unit in the current window: [59,60]
    3. 多いんで, stable minimal sense unit in the current window: [61,62,63]

* W13. {64: '盛り上がる', 65: 'ん', 66: 'です'}
  - carried_over: None
  - defer: '盛り上がるんです' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [64,65,66]
  - release_units: None

* W14. {67: 'よ', 68: '。', 69: '特に', 70: '最後'}
  - carried_over: {64: '盛り上がる', 65: 'ん', 66: 'です'}
  - defer: '最後' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [70]
  - release_units:
    1. 盛り上がるんですよ。, '盛り上がるんです' is carried over from the previous window; released here because it is now a stable minimal sense unit: [64,65,66,67,68]
    2. 特に, stable minimal sense unit in the current window: [69]

* W15. {71: 'の', 72: '盛り上がっ', 73: 'た'}
  - carried_over: {70: '最後'}
  - defer: '盛り上がった' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [72,73]
  - release_units:
    1. 最後の, '最後' is carried over from the previous window; released here because it is now a stable minimal sense unit: [70,71]

* W16. {74: 'ところ', 75: '盛り上がり', 76: 'きる'}
  - carried_over: {72: '盛り上がっ', 73: 'た'}
  - defer: '盛り上がりきる' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [75,76]
  - release_units:
    1. 盛り上がったところ, '盛り上がった' is carried over from the previous window; released here because it is now a stable minimal sense unit: [72,73,74]

* W17. {77: 'とき', 78: 'に', 79: '6', 80: '番'}
  - carried_over: {75: '盛り上がり', 76: 'きる'}
  - defer: None
  - release_units:
    1. 盛り上がりきるときに, '盛り上がりきる' is carried over from the previous window; released here because it is now a stable minimal sense unit: [75,76,77,78]
    2. 6番, stable minimal sense unit in the current window: [79,80]

* W18. {81: 'なんか', 82: '足', 83: '使う', 84: 'と', 85: '、'}
  - carried_over: None
  - defer: None
  - release_units:
    1. なんか, this host-dependent tail is released separately here as a legal exception because its host phrase 6番 was already emitted in the previous window: [81]
    2. 足使うと、, stable minimal sense unit in the current window: [82,83,84,85]

* W19. {86: 'めっちゃ', 87: '盛り上がる', 88: 'ん'}
  - carried_over: None
  - defer: 'めっちゃ盛り上がるん' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [86,87,88]
  - release_units: None

* W20. {89: 'で', 90: '、', 91: 'エンディング'}
  - carried_over: {86: 'めっちゃ', 87: '盛り上がる', 88: 'ん'}
  - defer: 'エンディング' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [91]
  - release_units:
    1. めっちゃ盛り上がるんで、, 'めっちゃ盛り上がるん' is carried over from the previous window; released here because it is now a stable minimal sense unit: [86,87,88,89,90]

* W21. {92: 'なんか', 93: 'で', 94: 'も', 95: '最後'}
  - carried_over: {91: 'エンディング'}
  - defer: '最後' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier carried-over material: [95]
  - release_units:
    1. エンディングなんかでも, 'エンディング' is carried over from the previous window; released here because it is now a stable minimal sense unit: [91,92,93,94]

* W22. {96: '同じ', 97: 'こと', 98: '繰り返し', 99: 'てる'}
  - carried_over: {95: '最後'}
  - defer: '繰り返してる' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [98,99]
  - release_units:
    1. 最後, '最後' is carried over from the previous window; released here because it is now a stable minimal sense unit: [95]
    2. 同じこと, stable minimal sense unit in the current window: [96,97]

* W23. {100: 'と', 101: '、', 102: '途中', 103: 'から'}
  - carried_over: {98: '繰り返し', 99: 'てる'}
  - defer: None
  - release_units:
    1. 繰り返してると、, '繰り返してる' is carried over from the previous window; released here because it is now a stable minimal sense unit: [98,99,100,101]
    2. 途中から, stable minimal sense unit in the current window: [102,103]

* W24. {104: '頭打ち', 105: 'に', 106: 'し', 107: 'ちゃう', 108: 'って', 109: 'いう', 110: 'の', 111: 'も', 112: '一'}
  - carried_over: None
  - defer: '一' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [112]
  - release_units:
    1. 頭打ちに, stable minimal sense unit in the current window: [104,105]
    2. しちゃうっていうのも, stable minimal sense unit in the current window: [106,107,108,109,110,111]

* W25. {113: 'つ', 114: 'の', 115: '手', 116: 'です'}
  - carried_over: {112: '一'}
  - defer: '一つの手です' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [112,113,114,115,116]
  - release_units: None

* W26. {117: 'ね', 118: '。', 119: '頭打ち', 120: 'する', 121: 'とき'}
  - carried_over: {112: '一', 113: 'つ', 114: 'の', 115: '手', 116: 'です'}
  - defer: None
  - release_units:
    1. 一つの手ですね。, '一つの手です' is carried over from the previous window; released here because it is now a stable minimal sense unit: [112,113,114,115,116,117,118]
    2. 頭打ちするとき, stable minimal sense unit in the current window: [119,120,121]

* W27. {122: '盛り上げ', 123: 'たかっ', 124: 'たら', 125: 'シンバル'}
  - carried_over: None
  - defer: 'シンバル' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the current window already releases earlier material: [125]
  - release_units:
    1. 盛り上げたかったら, stable minimal sense unit in the current window: [122,123,124]

* W28. {126: 'に', 127: 'し', 128: 'ちゃう', 129: '。'}
  - carried_over: {125: 'シンバル'}
  - defer: None
  - release_units:
    1. シンバルにしちゃう。, 'シンバル' is carried over from the previous window; released here because it is now a stable minimal sense unit: [125,126,127,128,129]
</scratchpad>
<result>
[
  [0,1],
  [2,3,4,5,6],
  [7,8,9,10],
  [11,12,13],
  [14,15,16,17],
  [18,19,20,21,22],
  [23,24],
  [25,26],
  [27,28],
  [29,30],
  [31,32,33],
  [34,35,36,37],
  [38,39,40,41,42],
  [43,44,45],
  [46,47,48,49,50],
  [51,52,53],
  [54,55],
  [56,57,58],
  [59,60],
  [61,62,63],
  [64,65,66,67,68],
  [69],
  [70,71],
  [72,73,74],
  [75,76,77,78],
  [79,80],
  [81],
  [82,83,84,85],
  [86,87,88,89,90],
  [91,92,93,94],
  [95],
  [96,97],
  [98,99,100,101],
  [102,103],
  [104,105],
  [106,107,108,109,110,111],
  [112,113,114,115,116,117,118],
  [119,120,121],
  [122,123,124],
  [125,126,127,128,129]
]
</result>
""".lstrip("\n")


# --- PURE TEXT SEGMENTATION ---

PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

token_indices:
{0: '個人的', 1: 'に', 2: 'は', 3: '思っ', 4: 'た', 5: 'ん', 6: 'です', 7: 'けれど', 8: 'も', 9: '私', 10: '前回', 11: 'の', 12: '封筒', 13: 'ファイル', 14: 'の', 15: '時', 16: 'も', 17: 'そう', 18: 'だっ', 19: 'た', 20: 'ん', 21: 'です', 22: 'が', 23: 'この', 24: 'なんか', 25: '私', 26: 'こう', 27: 'しっかり', 28: 'し', 29: 'て', 30: 'ない', 31: 'と', 32: 'ダメ', 33: 'みたい', 34: 'で', 35: '私', 36: 'は', 37: 'この', 38: 'デザイン', 39: 'ペーパー', 40: 'に', 41: 'クラフト', 42: 'ボード', 43: 'を', 44: 'また', 45: '使い', 46: 'まし', 47: 'た', 48: 'な', 49: 'の', 50: 'で', 51: 'かなり', 52: 'しっかり', 53: 'し', 54: 'た', 55: '出来栄え', 56: 'に', 57: 'なっ', 58: 'て', 59: 'いる', 60: 'と', 61: '思い', 62: 'ます', 63: 'ここ', 64: 'も', 65: '何', 66: 'で', 67: '止めよう', 68: 'か', 69: '迷っ', 70: 'て'}

<scratchpad>
1. 個人的には
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [0, 1, 2]

2. 思ったんです
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [3, 4, 5, 6]

3. けれども
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [7, 8]

4. 私
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [9]

5. 前回の
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [10, 11]

6. 封筒ファイルの時も
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [12, 13, 14, 15, 16]

7. そうだったんです
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [17, 18, 19, 20, 21]

8. が
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [22]

9. このなんか
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [23, 24]

10. 私
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [25]

11. こうしっかりしてないと
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [26, 27, 28, 29, 30, 31]

12. ダメみたいで
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [32, 33, 34]

13. 私
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [35]

14. は
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [36]

15. このデザインペーパー
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [37, 38, 39]

16. に
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [40]

17. クラフトボードを
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [41, 42, 43]

18. また使いました
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [44, 45, 46, 47]

19. なので
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [48, 49, 50]

20. かなり
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [51]

21. しっかりした出来栄え
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [52, 53, 54, 55]

22. になっている
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [56, 57, 58, 59]

23. と思います
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [60, 61, 62]

24. ここも
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [63, 64]

25. 何で止めようか
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [65, 66, 67, 68]

26. 迷って
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [69, 70]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4,5,6],
  [7,8],
  [9],
  [10,11],
  [12,13,14,15,16],
  [17,18,19,20,21],
  [22],
  [23,24],
  [25],
  [26,27,28,29,30,31],
  [32,33,34],
  [35],
  [36],
  [37,38,39],
  [40],
  [41,42,43],
  [44,45,46,47],
  [48,49,50],
  [51],
  [52,53,54,55],
  [56,57,58,59],
  [60,61,62],
  [63,64],
  [65,66,67,68],
  [69,70]
]
</result>


## Sample 2:

token_indices:
{0: 'ただ', 1: '、', 2: 'それ', 3: 'が', 4: 'まあ', 5: '弱み', 6: 'と', 7: 'は', 8: 'いえ', 9: '、', 10: 'その', 11: '反面', 12: 'ね', 13: '、', 14: '人数', 15: 'が', 16: '多い', 17: 'から', 18: 'こそ', 19: '、', 20: 'できる', 21: '、', 22: '強さ', 23: 'と', 24: 'いう', 25: 'もの', 26: 'も', 27: '、', 28: '相対的', 29: 'に', 30: '大きく', 31: 'なっ', 32: 'て', 33: 'き', 34: 'ます', 35: '。', 36: '例えば', 37: 'です', 38: 'けど', 39: '、', 40: 'え', 41: '、', 42: 'まあ', 43: '、', 44: '案件', 45: 'と', 46: 'か', 47: '。'}

<scratchpad>
1. ただ、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [0, 1]

2. それが
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [2, 3]

3. まあ
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [4]

4. 弱みとはいえ、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [5, 6, 7, 8, 9]

5. その反面ね、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [10, 11, 12, 13]

6. 人数が
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [14, 15]

7. 多いからこそ、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [16, 17, 18, 19]

8. できる、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [20, 21]

9. 強さというものも、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [22, 23, 24, 25, 26, 27]

10. 相対的に
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [28, 29]

11. 大きくなってきます。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [30, 31, 32, 33, 34, 35]

12. 例えばですけど、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [36, 37, 38, 39]

13. え、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [40, 41]

14. まあ、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [42, 43]

15. 案件とか。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [44, 45, 46, 47]
</scratchpad>
<result>
[
  [0,1],
  [2,3],
  [4],
  [5,6,7,8,9],
  [10,11,12,13],
  [14,15],
  [16,17,18,19],
  [20,21],
  [22,23,24,25,26,27],
  [28,29],
  [30,31,32,33,34,35],
  [36,37,38,39],
  [40,41],
  [42,43],
  [44,45,46,47]
]
</result>


## Sample 3:

token_indices:
{0: '一', 1: '決定戦', 2: ',DBS', 3: 'という', 4: '当', 5: '時の', 6: 'ジャ', 7: 'ニ', 8: 'ー氏の情', 9: '愛', 10: '事', 11: '情が', 12: 'くっ', 13: 'き', 14: 'り反映さ', 15: 'れた', 16: '奇', 17: '妙', 18: 'な', 19: 'テレ', 20: 'ビ', 21: '番組も', 22: '放送', 23: 'さ', 24: 'れて', 25: 'い', 26: 'る', 27: '。'}

<scratchpad>
1. 一決定戦
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [0, 1]

2. ,DBSという
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [2, 3]

3. 当時の
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [4, 5]

4. ジャニー氏の情愛事情が
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [6, 7, 8, 9, 10, 11]

5. くっきり反映された
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [12, 13, 14, 15]

6. 奇妙な
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [16, 17, 18]

7. テレビ番組も
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [19, 20, 21]

8. 放送されている。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [22, 23, 24, 25, 26, 27]
</scratchpad>
<result>
[
  [0,1],
  [2,3],
  [4,5],
  [6,7,8,9,10,11],
  [12,13,14,15],
  [16,17,18],
  [19,20,21],
  [22,23,24,25,26,27]
]
</result>


## Sample 4:

token_indices:
{0: 'それ', 1: 'なら', 2: '、', 3: '私', 4: 'も', 5: '思っ', 6: 'て', 7: 'まー', 8: 'す', 9: '、', 10: 'と', 11: 'いう', 12: 'こと', 13: 'で', 14: '。', 15: 'ま', 16: '、', 17: 'この', 18: 'まま', 19: '、', 20: 'そのまま', 21: '、', 22: 'レビュー', 23: 'を', 24: 'する', 25: 'わけ', 26: 'です', 27: 'けど', 28: 'も', 29: '。', 30: '実', 31: 'は', 32: '、', 33: 'この', 34: '演習', 35: '業', 36: 'が', 37: 'レンズ', 38: 'です', 39: 'ね', 40: '。', 41: '昼間', 42: 'も', 43: '撮影', 44: 'できる', 45: 'ん', 46: 'です', 47: 'ね', 48: '。', 49: 'ま', 50: '、', 51: 'こう', 52: 'いう', 53: '感じ', 54: 'で', 55: '、', 56: 'えぇ', 57: '、', 58: '写真', 59: 'が', 60: '撮れ', 61: 'ます', 62: '。', 63: 'すごい', 64: '、', 65: '昼間', 66: '、', 67: '写真', 68: '撮っ', 69: 'て', 70: 'も', 71: '、', 72: 'ちょっと', 73: 'なんか', 74: '、', 75: 'アーティスティック', 76: 'な', 77: '感じ', 78: 'で', 79: '撮れる', 80: 'って', 81: 'いう', 82: 'ん', 83: 'です', 84: 'か', 85: 'ね', 86: '。', 87: 'これ', 88: '、', 89: 'オートフォーカス', 90: 'の', 91: 'レンズ', 92: 'で', 93: 'は', 94: 'ない', 95: 'の', 96: 'で', 97: '、', 98: 'マニュアル', 99: 'フォーカス', 100: 'の'}

<scratchpad>
1. それなら、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [0, 1, 2]

2. 私も
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [3, 4]

3. 思ってまーす、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [5, 6, 7, 8, 9]

4. ということで。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [10, 11, 12, 13, 14]

5. ま、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [15, 16]

6. このまま、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [17, 18, 19]

7. そのまま、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [20, 21]

8. レビューをする
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [22, 23, 24]

9. わけですけども。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [25, 26, 27, 28, 29]

10. 実は、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [30, 31, 32]

11. この演習業が
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [33, 34, 35, 36]

12. レンズですね。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [37, 38, 39, 40]

13. 昼間も
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [41, 42]

14. 撮影できるんですね。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [43, 44, 45, 46, 47, 48]

15. ま、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [49, 50]

16. こういう感じで、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [51, 52, 53, 54, 55]

17. えぇ、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [56, 57]

18. 写真が
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [58, 59]

19. 撮れます。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [60, 61, 62]

20. すごい、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [63, 64]

21. 昼間、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [65, 66]

22. 写真撮っても、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [67, 68, 69, 70, 71]

23. ちょっとなんか、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [72, 73, 74]

24. アーティスティックな感じで
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [75, 76, 77, 78]

25. 撮れるっていうんですかね。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [79, 80, 81, 82, 83, 84, 85, 86]

26. これ、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [87, 88]

27. オートフォーカスの
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [89, 90]

28. レンズではないので、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [91, 92, 93, 94, 95, 96, 97]

29. マニュアルフォーカスの
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [98, 99, 100]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4],
  [5,6,7,8,9],
  [10,11,12,13,14],
  [15,16],
  [17,18,19],
  [20,21],
  [22,23,24],
  [25,26,27,28,29],
  [30,31,32],
  [33,34,35,36],
  [37,38,39,40],
  [41,42],
  [43,44,45,46,47,48],
  [49,50],
  [51,52,53,54,55],
  [56,57],
  [58,59],
  [60,61,62],
  [63,64],
  [65,66],
  [67,68,69,70,71],
  [72,73,74],
  [75,76,77,78],
  [79,80,81,82,83,84,85,86],
  [87,88],
  [89,90],
  [91,92,93,94,95,96,97],
  [98,99,100]
]
</result>


## Sample 5:

token_indices:
{0: 'ね', 1: '。', 2: '普通', 3: 'の', 4: '8', 5: 'ビート', 6: 'に', 7: '戻っ', 8: 'たり', 9: 'ね', 10: '。', 11: 'フィルイン', 12: '挟ん', 13: 'で', 14: 'こう', 15: 'いう', 16: '練習', 17: 'を', 18: 'し', 19: 'て', 20: 'もらえる', 21: 'と', 22: '、', 23: '頭打ち', 24: '。', 25: 'で', 26: '、', 27: '頭打ち', 28: 'は', 29: 'どこ', 30: 'に', 31: '入れ', 32: 'て', 33: 'も', 34: 'いい', 35: 'の', 36: 'で', 37: '、', 38: '停滞', 39: 'さ', 40: 'せる', 41: '感じ', 42: '。', 43: 'それ', 44: 'と', 45: '、', 46: 'もう', 47: '一', 48: 'つ', 49: 'は', 50: '、', 51: 'イントロ', 52: 'と', 53: 'か', 54: 'サビ', 55: 'で', 56: '使う', 57: 'と', 58: '、', 59: 'スネア', 60: 'が', 61: '多い', 62: 'ん', 63: 'で', 64: '盛り上がる', 65: 'ん', 66: 'です', 67: 'よ', 68: '。', 69: '特に', 70: '最後', 71: 'の', 72: '盛り上がっ', 73: 'た', 74: 'ところ', 75: '盛り上がり', 76: 'きる', 77: 'とき', 78: 'に', 79: '6', 80: '番', 81: 'なんか', 82: '足', 83: '使う', 84: 'と', 85: '、', 86: 'めっちゃ', 87: '盛り上がる', 88: 'ん', 89: 'で', 90: '、', 91: 'エンディング', 92: 'なんか', 93: 'で', 94: 'も', 95: '最後', 96: '同じ', 97: 'こと', 98: '繰り返し', 99: 'てる', 100: 'と', 101: '、', 102: '途中', 103: 'から', 104: '頭打ち', 105: 'に', 106: 'し', 107: 'ちゃう', 108: 'って', 109: 'いう', 110: 'の', 111: 'も', 112: '一', 113: 'つ', 114: 'の', 115: '手', 116: 'です', 117: 'ね', 118: '。', 119: '頭打ち', 120: 'する', 121: 'とき', 122: '盛り上げ', 123: 'たかっ', 124: 'たら', 125: 'シンバル', 126: 'に', 127: 'し', 128: 'ちゃう', 129: '。'}

<scratchpad>
1. ね。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [0, 1]

2. 普通の8ビートに
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [2, 3, 4, 5, 6]

3. 戻ったりね。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [7, 8, 9, 10]

4. フィルイン挟んで
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [11, 12, 13]

5. こういう練習を
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [14, 15, 16, 17]

6. してもらえると、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [18, 19, 20, 21, 22]

7. 頭打ち。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [23, 24]

8. で、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [25, 26]

9. 頭打ちは
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [27, 28]

10. どこに
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [29, 30]

11. 入れても
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [31, 32, 33]

12. いいので、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [34, 35, 36, 37]

13. 停滞させる感じ。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [38, 39, 40, 41, 42]

14. それと、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [43, 44, 45]

15. もう一つは、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [46, 47, 48, 49, 50]

16. イントロとか
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [51, 52, 53]

17. サビで
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [54, 55]

18. 使うと、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [56, 57, 58]

19. スネアが
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [59, 60]

20. 多いんで
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [61, 62, 63]

21. 盛り上がるんですよ。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [64, 65, 66, 67, 68]

22. 特に
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [69]

23. 最後の
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [70, 71]

24. 盛り上がったところ
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [72, 73, 74]

25. 盛り上がりきるときに
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [75, 76, 77, 78]

26. 6番
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [79, 80]

27. なんか
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [81]

28. 足使うと、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [82, 83, 84, 85]

29. めっちゃ盛り上がるんで、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [86, 87, 88, 89, 90]

30. エンディングなんかでも
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [91, 92, 93, 94]

31. 最後
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [95]

32. 同じこと
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [96, 97]

33. 繰り返してると、
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [98, 99, 100, 101]

34. 途中から
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [102, 103]

35. 頭打ちに
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [104, 105]

36. しちゃうっていうのも
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [106, 107, 108, 109, 110, 111]

37. 一つの手ですね。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [112, 113, 114, 115, 116, 117, 118]

38. 頭打ちするとき
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [119, 120, 121]

39. 盛り上げたかったら
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [122, 123, 124]

40. シンバルにしちゃう。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Japanese local unit
   - sense_unit: [125, 126, 127, 128, 129]
</scratchpad>
<result>
[
  [0,1],
  [2,3,4,5,6],
  [7,8,9,10],
  [11,12,13],
  [14,15,16,17],
  [18,19,20,21,22],
  [23,24],
  [25,26],
  [27,28],
  [29,30],
  [31,32,33],
  [34,35,36,37],
  [38,39,40,41,42],
  [43,44,45],
  [46,47,48,49,50],
  [51,52,53],
  [54,55],
  [56,57,58],
  [59,60],
  [61,62,63],
  [64,65,66,67,68],
  [69],
  [70,71],
  [72,73,74],
  [75,76,77,78],
  [79,80],
  [81],
  [82,83,84,85],
  [86,87,88,89,90],
  [91,92,93,94],
  [95],
  [96,97],
  [98,99,100,101],
  [102,103],
  [104,105],
  [106,107,108,109,110,111],
  [112,113,114,115,116,117,118],
  [119,120,121],
  [122,123,124],
  [125,126,127,128,129]
]
</result>
""".lstrip("\n")


# --- JAPANESE LANGUAGE PACK (Minimal Incremental Patch) ---

GENERAL_LANGUAGE_PACK = """
## JAPANESE LANGUAGE PACK (Minimal Incremental Patch)

### Core Bias

Japanese should be segmented around **small stable local units**, not around larger sentence-like spans.

### Protect These Units

Prefer not to split the following unless latency pressure forces it:
- **content word + attached particle units**
- **bunsetsu-like local units**
- **connective / explanatory units**
- **auxiliary chains**
- **polite-ending / sentence-ending chains**
- **compound nouns**
- **proper names**
- **katakana compound terms**
- **fixed nominal units**

### Typical Stable Japanese Units

Examples of the kinds of units that should usually stay together:
- noun / phrase + particle units  
  e.g. units like `個人的には`, `私は`, `人数が`, `写真が`

- connective / explanatory units  
  e.g. units like `けれども`, `とはいえ`, `なので`, `ということで`

- auxiliary / ending chains  
  e.g. units like `と思います`, `わけですけども`, `撮れます`, `使いました`

- compound noun / fixed nominal units  
  e.g. units like `封筒ファイル`, `デザインペーパー`, `クラフトボード`, `テレビ番組`, `オートフォーカス`, `マニュアルフォーカス`

### Do Not Expose Bare Particles or Detached Tails

Avoid releasing these as standalone output unless they are already inside a stable local unit:
- bare particles
- detached connective tails
- detached auxiliary tails
- detached polite endings
- fragments taken from the middle of a compound noun

These usually need their local phrase context.

### Allow Small Discourse Units

Japanese may release some very small discourse-level units if they already have clear local discourse value.

Typical allowed cases include:
- discourse markers
- fillers
- stance-marking units
- turn-opening units
- spoken emphasis units

Examples of the type of unit allowed:
- `ただ、`
- `まあ`
- `ね、`
- `え、`
- `えぇ、`
- `ま、`
- `それなら、`
- `例えばですけど、`
- `実は、`
- `これ、`

These are allowed not because they are fully closed, but because they already carry local discourse function.

### Preferred Japanese Stability Signals

When deciding whether a local unit is stable enough, prefer units that already contain one of these:
- a bunsetsu-like phrase
- a content word with its particle
- a connective / explanatory unit
- an auxiliary / ending chain
- a compound noun
- a proper name
- a small discourse unit with clear local function

### Japanese-Specific Failure Modes to Avoid

Do not drift into these bad cuts:
- separating a particle from its host phrase
- splitting inside a connective / explanatory unit
- splitting inside an auxiliary or ending chain
- splitting a compound noun into fragments
- splitting a katakana compound term into fragments

Typical bad patterns to avoid are:
- particle stranded by itself
- connective tail split off
- ending chain split in the middle
- compound noun broken into smaller pieces

### Practical Japanese Bias

If two candidate cuts are possible, prefer the one that keeps:
- the tighter content-word + particle unit
- the tighter bunsetsu-like unit
- the tighter connective / explanatory unit
- the tighter auxiliary / ending chain
- the tighter compound noun
- the tighter discourse unit with local meaning
""".lstrip("\n")


