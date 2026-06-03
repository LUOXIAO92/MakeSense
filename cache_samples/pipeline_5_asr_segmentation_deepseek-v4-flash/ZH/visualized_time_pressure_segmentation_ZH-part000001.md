=== ZH_B00021_S06758_W000029 ===

status: finished

raw_text:
我仿佛看到了他们游走在太行山上的足迹，深一脚浅一脚；我仿佛听到了他们放歌太行山上的声音，时而高，时而低，时而欢快，时而呜咽。

word_indices:
* W0. {0: '我', 1: '仿佛'}
* W1. {2: '看到', 3: '了'}
* W2. {4: '他们', 5: '游走', 6: '在'}
* W3. {7: '太行', 8: '山', 9: '上', 10: '的'}
* W4. {11: '足迹，'}
* W5. {12: '深', 13: '一', 14: '脚'}
* W6. {15: '浅', 16: '一'}
* W7. {17: '脚；'}
* W8. {18: '我', 19: '仿佛'}
* W9. {20: '听到', 21: '了', 22: '他们'}
* W10. {23: '放歌'}
* W11. {24: '太行', 25: '山', 26: '上', 27: '的'}
* W12. {28: '声音，'}
* W13. {29: '时', 30: '而', 31: '高，'}
* W14. {32: '时', 33: '而', 34: '低，'}
* W15. {35: '时', 36: '而'}
* W16. {37: '欢快，'}
* W17. {38: '时', 39: '而', 40: '呜', 41: '咽。'}

scratchpad:
* W0. {0: '我', 1: '仿佛'}
  - carried_over: None
  - defer: '我仿佛' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non‑empty and delaying by one window is still legal: [0,1]
  - release_units: None

* W1. {2: '看到', 3: '了'}
  - carried_over: {0: '我', 1: '仿佛'}
  - defer: None
  - release_units:
    1. 我仿佛看到了, '我仿佛' is carried over from the previous window; released here because it is now a stable minimal sense unit (subject + verb + aspect marker, 4 tokens): [0,1,2,3]

* W2. {4: '他们', 5: '游走', 6: '在'}
  - carried_over: None
  - defer: '他们在游走' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non‑empty: [4,5,6]
  - release_units: None

* W3. {7: '太行', 8: '山', 9: '上', 10: '的'}
  - carried_over: {4: '他们', 5: '游走', 6: '在'}
  - defer: '的' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [10]
  - release_units:
    1. 他们游走, latency‑forced partial release to keep chunk size ≤5; the fuller phrase will follow in the next chunk: [4,5]
    2. 在太行山上, released as a compact prepositional phrase that pairs with the previous verb chunk: [6,7,8,9]

* W4. {11: '足迹，'}
  - carried_over: {10: '的'}
  - defer: None
  - release_units:
    1. 的足迹，, '的' is carried over from the previous window; forms a stable minimal sense unit (modifier + noun + punctuation): [10,11]

* W5. {12: '深', 13: '一', 14: '脚'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 深一脚, stable minimal sense unit (part of the parallel structure): [12,13,14]

* W6. {15: '浅', 16: '一'}
  - carried_over: None
  - defer: '浅一' is not yet a stable release unit / minimal sense unit; defer it to the next window because the previous window had output and the next window is non‑empty: [15,16]
  - release_units: None

* W7. {17: '脚；'}
  - carried_over: {15: '浅', 16: '一'}
  - defer: None
  - release_units:
    1. 浅一脚；, '浅一' is carried over from the previous window; forms a stable minimal sense unit: [15,16,17]

* W8. {18: '我', 19: '仿佛'}
  - carried_over: None
  - defer: '我仿佛' is not yet a stable release unit / minimal sense unit; defer it to the next window because the previous window had output and the next window is non‑empty: [18,19]
  - release_units: None

* W9. {20: '听到', 21: '了', 22: '他们'}
  - carried_over: {18: '我', 19: '仿佛'}
  - defer: None
  - release_units:
    1. 我仿佛听到了他们, '我仿佛' is carried over; forms a stable minimal sense unit (5 tokens, subject + verb + object): [18,19,20,21,22]

* W10. {23: '放歌'}
  - carried_over: None
  - defer: '放歌' does not yet form a stable minimal sense unit; defer it to the next window because the previous window had output and the next window is non‑empty: [23]
  - release_units: None

* W11. {24: '太行', 25: '山', 26: '上', 27: '的'}
  - carried_over: {23: '放歌'}
  - defer: '的' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [27]
  - release_units:
    1. 放歌太行山上, '放歌' is carried over; released as a stable minimal sense unit (verb + location, 4 tokens): [23,24,25,26]

* W12. {28: '声音，'}
  - carried_over: {27: '的'}
  - defer: None
  - release_units:
    1. 的声音，, '的' is carried over; forms a stable minimal sense unit: [27,28]

* W13. {29: '时', 30: '而', 31: '高，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 时而高，, stable minimal sense unit: [29,30,31]

* W14. {32: '时', 33: '而', 34: '低，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 时而低，, stable minimal sense unit: [32,33,34]

* W15. {35: '时', 36: '而'}
  - carried_over: None
  - defer: '时而' is not yet a stable release unit / minimal sense unit; defer it to the next window because the previous window had output and the next window is non‑empty: [35,36]
  - release_units: None

* W16. {37: '欢快，'}
  - carried_over: {35: '时', 36: '而'}
  - defer: None
  - release_units:
    1. 时而欢快，, '时而' is carried over; forms a stable minimal sense unit: [35,36,37]

* W17. {38: '时', 39: '而', 40: '呜', 41: '咽。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 时而呜咽。, stable minimal sense unit: [38,39,40,41]

result:
[
  [0,1,2,3],
  [4,5],
  [6,7,8,9],
  [10,11],
  [12,13,14],
  [15,16,17],
  [18,19,20,21,22],
  [23,24,25,26],
  [27,28],
  [29,30,31],
  [32,33,34],
  [35,36,37],
  [38,39,40,41]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '我', 1: '仿佛'} - output: release_units None
* W1. input: {2: '看到', 3: '了'} - output: release_units 1.{0: '我', 1: '仿佛', 2: '看到', 3: '了'}
* W2. input: {4: '他们', 5: '游走', 6: '在'} - output: release_units None
* W3. input: {7: '太行', 8: '山', 9: '上', 10: '的'} - output: release_units 1.{4: '他们', 5: '游走', 6: '在', 7: '太行', 8: '山', 9: '上'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W4. input: {11: '足迹，'} - output: release_units 1.{10: '的', 11: '足迹，'}
* W5. input: {12: '深', 13: '一', 14: '脚'} - output: release_units 1.{12: '深', 13: '一', 14: '脚'}
* W6. input: {15: '浅', 16: '一'} - output: release_units None
* W7. input: {17: '脚；'} - output: release_units 1.{15: '浅', 16: '一', 17: '脚；'}
* W8. input: {18: '我', 19: '仿佛'} - output: release_units None
* W9. input: {20: '听到', 21: '了', 22: '他们'} - output: release_units 1.{18: '我', 19: '仿佛', 20: '听到', 21: '了'}
* W10. input: {23: '放歌'} - output: release_units 1.{22: '他们', 23: '放歌'}
* W11. input: {24: '太行', 25: '山', 26: '上', 27: '的'} - output: release_units 1.{24: '太行', 25: '山', 26: '上'}
* W12. input: {28: '声音，'} - output: release_units 1.{27: '的', 28: '声音，'}
* W13. input: {29: '时', 30: '而', 31: '高，'} - output: release_units 1.{29: '时', 30: '而', 31: '高，'}
* W14. input: {32: '时', 33: '而', 34: '低，'} - output: release_units 1.{32: '时', 33: '而', 34: '低，'}
* W15. input: {35: '时', 36: '而'} - output: release_units None
* W16. input: {37: '欢快，'} - output: release_units 1.{35: '时', 36: '而', 37: '欢快，'}
* W17. input: {38: '时', 39: '而', 40: '呜', 41: '咽。'} - output: release_units 1.{38: '时', 39: '而', 40: '呜', 41: '咽。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '我', 1: '仿佛'}
  - carried_over: None
  - defer: '我仿佛' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1]
  - release_units: None

* W1. {2: '看到', 3: '了'}
  - carried_over: {0: '我', 1: '仿佛'}
  - defer: None
  - release_units:
    1. 我仿佛看到了, '我仿佛' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2,3]

* W2. {4: '他们', 5: '游走', 6: '在'}
  - carried_over: None
  - defer: '他们游走在' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [4,5,6]
  - release_units: None

* W3. {7: '太行', 8: '山', 9: '上', 10: '的'}
  - carried_over: {4: '他们', 5: '游走', 6: '在'}
  - defer: '的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10]
  - release_units:
    1. 他们游走在太行山上, '他们游走在' is carried over from the previous window; released here because it is now a stable minimal sense unit: [4,5,6,7,8,9]

* W4. {11: '足迹，'}
  - carried_over: {10: '的'}
  - defer: None
  - release_units:
    1. 的足迹， '的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11]

* W5. {12: '深', 13: '一', 14: '脚'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 深一脚, stable minimal sense unit in the current window: [12,13,14]

* W6. {15: '浅', 16: '一'}
  - carried_over: None
  - defer: '浅一' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [15,16]
  - release_units: None

* W7. {17: '脚；'}
  - carried_over: {15: '浅', 16: '一'}
  - defer: None
  - release_units:
    1. 浅一脚； '浅一' is carried over from the previous window; released here because it is now a stable minimal sense unit: [15,16,17]

* W8. {18: '我', 19: '仿佛'}
  - carried_over: None
  - defer: '我仿佛' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [18,19]
  - release_units: None

* W9. {20: '听到', 21: '了', 22: '他们'}
  - carried_over: {18: '我', 19: '仿佛'}
  - defer: '他们' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [22]
  - release_units:
    1. 我仿佛听到了, '我仿佛' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20,21]

* W10. {23: '放歌'}
  - carried_over: {22: '他们'}
  - defer: None
  - release_units:
    1. 他们放歌, '他们' is carried over from the previous window; released here because it is now a stable minimal sense unit: [22,23]

* W11. {24: '太行', 25: '山', 26: '上', 27: '的'}
  - carried_over: None
  - defer: '的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [27]
  - release_units:
    1. 太行山上, stable minimal sense unit in the current window: [24,25,26]

* W12. {28: '声音，'}
  - carried_over: {27: '的'}
  - defer: None
  - release_units:
    1. 的声音， '的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28]

* W13. {29: '时', 30: '而', 31: '高，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 时而高， stable minimal sense unit in the current window: [29,30,31]

* W14. {32: '时', 33: '而', 34: '低，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 时而低， stable minimal sense unit in the current window: [32,33,34]

* W15. {35: '时', 36: '而'}
  - carried_over: None
  - defer: '时而' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [35,36]
  - release_units: None

* W16. {37: '欢快，'}
  - carried_over: {35: '时', 36: '而'}
  - defer: None
  - release_units:
    1. 时而欢快， '时而' is carried over from the previous window; released here because it is now a stable minimal sense unit: [35,36,37]

* W17. {38: '时', 39: '而', 40: '呜', 41: '咽。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 时而呜咽。 stable minimal sense unit in the current window: [38,39,40,41]
  result:
[
  [0,1,2,3],
  [4,5,6,7,8,9],
  [10,11],
  [12,13,14],
  [15,16,17],
  [18,19,20,21],
  [22,23],
  [24,25,26],
  [27,28],
  [29,30,31],
  [32,33,34],
  [35,36,37],
  [38,39,40,41]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '我', 1: '仿佛'} - output: release_units None
* W1. input: {2: '看到', 3: '了'} - output: release_units 1.{0: '我', 1: '仿佛', 2: '看到', 3: '了'}
* W2. input: {4: '他们', 5: '游走', 6: '在'} - output: release_units None
* W3. input: {7: '太行', 8: '山', 9: '上', 10: '的'} - output: release_units 1.{4: '他们', 5: '游走', 6: '在', 7: '太行', 8: '山', 9: '上'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W4. input: {11: '足迹，'} - output: release_units 1.{10: '的', 11: '足迹，'}
* W5. input: {12: '深', 13: '一', 14: '脚'} - output: release_units 1.{12: '深', 13: '一', 14: '脚'}
* W6. input: {15: '浅', 16: '一'} - output: release_units None
* W7. input: {17: '脚；'} - output: release_units 1.{15: '浅', 16: '一', 17: '脚；'}
* W8. input: {18: '我', 19: '仿佛'} - output: release_units None
* W9. input: {20: '听到', 21: '了', 22: '他们'} - output: release_units 1.{18: '我', 19: '仿佛', 20: '听到', 21: '了'}
* W10. input: {23: '放歌'} - output: release_units 1.{22: '他们', 23: '放歌'}
* W11. input: {24: '太行', 25: '山', 26: '上', 27: '的'} - output: release_units 1.{24: '太行', 25: '山', 26: '上'}
* W12. input: {28: '声音，'} - output: release_units 1.{27: '的', 28: '声音，'}
* W13. input: {29: '时', 30: '而', 31: '高，'} - output: release_units 1.{29: '时', 30: '而', 31: '高，'}
* W14. input: {32: '时', 33: '而', 34: '低，'} - output: release_units 1.{32: '时', 33: '而', 34: '低，'}
* W15. input: {35: '时', 36: '而'} - output: release_units None
* W16. input: {37: '欢快，'} - output: release_units 1.{35: '时', 36: '而', 37: '欢快，'}
* W17. input: {38: '时', 39: '而', 40: '呜', 41: '咽。'} - output: release_units 1.{38: '时', 39: '而', 40: '呜', 41: '咽。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src><|wait|></src>; start=0.00, end=1.00
* W1. <src>我仿佛看到了</src>; start=1.00, end=2.00
* W2. <src>他们游走</src>; start=2.00, end=3.00
* W3. <src>在太行山上</src>; start=3.00, end=4.00
* W4. <src>的足迹，</src>; start=4.00, end=5.00
* W5. <src>深一脚</src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>浅一脚；</src>; start=7.00, end=8.00
* W8. <src><|wait|></src>; start=8.00, end=9.00
* W9. <src>我仿佛听到了他们</src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=11.00
* W11. <src>放歌太行山上</src>; start=11.00, end=12.00
* W12. <src>的声音，</src>; start=12.00, end=13.00
* W13. <src>时而高，</src>; start=13.00, end=14.00
* W14. <src>时而低，</src>; start=14.00, end=15.00
* W15. <src><|wait|></src>; start=15.00, end=16.00
* W16. <src>时而欢快，</src>; start=16.00, end=17.00
* W17. <src>时而呜咽。</src>; start=17.00, end=17.84
```

---
=== ZH_B00021_S00398_W000012 ===

status: finished

raw_text:
三月二十二号，美国证券交易委员会宣布对加密资产企业家孙宇晨及其三家全资公司提起诉讼，指控他们没有经过注册提供和出售加密资产证券Tronics和BitTorrent。

word_indices:
* W0. {0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. {4: '美国', 5: '证券', 6: '交易', 7: '委员'}
* W2. {8: '会', 9: '宣布', 10: '对'}
* W3. {11: '加密', 12: '资产', 13: '企业'}
* W4. {14: '家', 15: '孙', 16: '宇晨'}
* W5. {17: '及', 18: '其', 19: '三', 20: '家'}
* W6. {21: '全资', 22: '公司', 23: '提起'}
* W7. {24: '诉讼，', 25: '指控'}
* W8. {26: '他们', 27: '没有', 28: '经过', 29: '注册'}
* W9. {30: '提供', 31: '和', 32: '出售', 33: '加密'}
* W10. {34: '资产', 35: '证券'}
* W11. {36: 'Tronics', 37: '和'}
* W12. {38: 'BitTorrent。'}

scratchpad:
* W0. {0: '三', 1: '月', 2: '二十二', 3: '号，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 三月二十二号，， stable minimal sense unit: [0,1,2,3]

* W1. {4: '美国', 5: '证券', 6: '交易', 7: '委员'}
  - carried_over: None
  - defer: '美国证券交易委员' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and defer is allowed: [4,5,6,7]
  - release_units: None

* W2. {8: '会', 9: '宣布', 10: '对'}
  - carried_over: {4: '美国', 5: '证券', 6: '交易', 7: '委员'}
  - defer: '宣布对' is not yet the best stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9,10]
  - release_units:
    1. 美国证券交易委员会, '美国证券交易委员' is carried over from the previous window; released here as a compact proper noun phrase: [4,5,6,7,8]

* W3. {11: '加密', 12: '资产', 13: '企业'}
  - carried_over: {9: '宣布', 10: '对'}
  - defer: '企业' is not yet a stable release unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [13]
  - release_units:
    1. 宣布对加密资产, '宣布对' is carried over from the previous window; released here as a compact verb–prepositional object unit: [9,10,11,12]

* W4. {14: '家', 15: '孙', 16: '宇晨'}
  - carried_over: {13: '企业'}
  - defer: None
  - release_units:
    1. 企业家孙宇晨, '企业' is carried over from the previous window; released here as a stable noun phrase (title + name): [13,14,15,16]

* W5. {17: '及', 18: '其', 19: '三', 20: '家'}
  - carried_over: None
  - defer: '三家' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [19,20]
  - release_units:
    1. 及其, released here as a compact conjunction unit: [17,18]

* W6. {21: '全资', 22: '公司', 23: '提起'}
  - carried_over: {19: '三', 20: '家'}
  - defer: '提起' is not yet a stable release unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [23]
  - release_units:
    1. 三家全资公司, '三家' is carried over from the previous window; released here as a compact noun phrase: [19,20,21,22]

* W7. {24: '诉讼，', 25: '指控'}
  - carried_over: {23: '提起'}
  - defer: '，指控' is not yet a stable release unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 提起诉讼， '提起' is carried over from the previous window; released here as a compact verb-object unit: [23,24]

* W8. {26: '他们', 27: '没有', 28: '经过', 29: '注册'}
  - carried_over: {25: '，指控'}
  - defer: None
  - release_units:
    1. ，指控他们没有经过注册, '，指控' is carried over from the previous window; released here as a compact clause unit: [25,26,27,28,29]

* W9. {30: '提供', 31: '和', 32: '出售', 33: '加密'}
  - carried_over: None
  - defer: '加密' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [33]
  - release_units:
    1. 提供和出售, stable minimal sense unit in the current window: [30,31,32]

* W10. {34: '资产', 35: '证券'}
  - carried_over: {33: '加密'}
  - defer: None
  - release_units:
    1. 加密资产证券, '加密' is carried over from the previous window; released here as a tight noun phrase: [33,34,35]

* W11. {36: 'Tronics', 37: '和'}
  - carried_over: None
  - defer: 'Tronics和' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output: [36,37]
  - release_units: None

* W12. {38: 'BitTorrent。'}
  - carried_over: {36: 'Tronics', 37: '和'}
  - defer: None
  - release_units:
    1. Tronics和BitTorrent。 'Tronics和' is carried over from the previous window; released here as a stable noun phrase: [36,37,38]

result:
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18],
  [19,20,21,22],
  [23,24],
  [25,26,27,28,29],
  [30,31,32],
  [33,34,35],
  [36,37,38]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '三', 1: '月', 2: '二十二', 3: '号，'} - output: release_units 1.{0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. input: {4: '美国', 5: '证券', 6: '交易', 7: '委员'} - output: release_units None
* W2. input: {8: '会', 9: '宣布', 10: '对'} - output: release_units 1.{4: '美国', 5: '证券', 6: '交易', 7: '委员', 8: '会'}; 2.{9: '宣布'}
* W3. input: {11: '加密', 12: '资产', 13: '企业'} - output: release_units None
* W4. input: {14: '家', 15: '孙', 16: '宇晨'} - output: release_units None <- ISSUE1: consecutive non-empty wait x2, delay too long.
* W5. input: {17: '及', 18: '其', 19: '三', 20: '家'} - output: release_units None <- ISSUE1: consecutive non-empty wait x3, delay too long.
* W6. input: {21: '全资', 22: '公司', 23: '提起'} - output: release_units 1.{10: '对', 11: '加密', 12: '资产', 13: '企业', 14: '家', 15: '孙', 16: '宇晨', 17: '及', 18: '其', 19: '三', 20: '家', 21: '全资', 22: '公司'} <- ISSUE2: oversized chunk release unit 1 size=13 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {24: '诉讼，', 25: '指控'} - output: release_units 1.{23: '提起', 24: '诉讼，'}
* W8. input: {26: '他们', 27: '没有', 28: '经过', 29: '注册'} - output: release_units 1.{25: '指控', 26: '他们'}
* W9. input: {30: '提供', 31: '和', 32: '出售', 33: '加密'} - output: release_units None
* W10. input: {34: '资产', 35: '证券'} - output: release_units 1.{27: '没有', 28: '经过', 29: '注册', 30: '提供', 31: '和', 32: '出售', 33: '加密', 34: '资产', 35: '证券'} <- ISSUE2: oversized chunk release unit 1 size=9 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {36: 'Tronics', 37: '和'} - output: release_units None
* W12. input: {38: 'BitTorrent。'} - output: release_units 1.{36: 'Tronics', 37: '和', 38: 'BitTorrent。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '三', 1: '月', 2: '二十二', 3: '号，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 三月二十二号， stable minimal sense unit (date expression): [0,1,2,3]

* W1. {4: '美国', 5: '证券', 6: '交易', 7: '委员'}
  - carried_over: None
  - defer: '美国证券交易委员' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [4,5,6,7]
  - release_units: None

* W2. {8: '会', 9: '宣布', 10: '对'}
  - carried_over: {4: '美国',5: '证券',6: '交易',7: '委员'}
  - defer: '宣布对' does not yet form a stable minimal sense unit; defer to next window: [9,10]
  - release_units:
    1. 美国证券交易委员会, carried over from previous window with current token '会': [4,5,6,7,8]

* W3. {11: '加密', 12: '资产', 13: '企业'}
  - carried_over: {9: '宣布',10: '对'}
  - defer: '宣布对加密资产企业' does not yet form a stable minimal sense unit; defer to next window: [9,10,11,12,13]
  - release_units: None

* W4. {14: '家', 15: '孙', 16: '宇晨'}
  - carried_over: {9: '宣布',10: '对',11: '加密',12: '资产',13: '企业'}
  - defer: '对加密资产企业家孙宇晨' does not yet form a stable minimal sense unit because more of the PP follows; defer it to the next window: [10,11,12,13,14,15,16]
  - release_units:
    1. 宣布, latency-forced partial release; the combined unit is not yet stable but current window must output because the previous window had no output: [9]

* W5. {17: '及', 18: '其', 19: '三', 20: '家'}
  - carried_over: {10: '对',11: '加密',12: '资产',13: '企业',14: '家',15: '孙',16: '宇晨'}
  - defer: '对加密资产企业家孙宇晨及其三家' still incomplete; defer to next window: [10,11,12,13,14,15,16,17,18,19,20]
  - release_units: None

* W6. {21: '全资', 22: '公司', 23: '提起'}
  - carried_over: {10: '对',11: '加密',12: '资产',13: '企业',14: '家',15: '孙',16: '宇晨',17: '及',18: '其',19: '三',20: '家'}
  - defer: '提起' does not yet form a stable minimal sense unit; defer it to the next window: [23]
  - release_units:
    1. 对加密资产企业家孙宇晨及其三家全资公司, carried over from previous window with current tokens; now a stable minimal sense unit (prepositional phrase): [10,11,12,13,14,15,16,17,18,19,20,21,22]

* W7. {24: '诉讼，', 25: '指控'}
  - carried_over: {23: '提起'}
  - defer: '指控' does not yet form a stable minimal sense unit; defer it to the next window: [25]
  - release_units:
    1. 提起诉讼， carried over with current; now a stable verb-object unit: [23,24]

* W8. {26: '他们', 27: '没有', 28: '经过', 29: '注册'}
  - carried_over: {25: '指控'}
  - defer: '指控他们没有经过注册' does not yet form a stable minimal sense unit because it continues with the verb phrase; defer to next window: [25,26,27,28,29]
  - release_units: None

* W9. {30: '提供', 31: '和', 32: '出售', 33: '加密'}
  - carried_over: {25: '指控',26: '他们',27: '没有',28: '经过',29: '注册'}
  - defer: '没有经过注册提供和出售加密' does not yet form a stable minimal sense unit; defer to next window: [27,28,29,30,31,32,33]
  - release_units:
    1. 指控他们, latency-forced partial release; releasing the smallest stable verb-object unit now because current window must output (previous window had no output): [25,26]

* W10. {34: '资产', 35: '证券'}
  - carried_over: {27: '没有',28: '经过',29: '注册',30: '提供',31: '和',32: '出售',33: '加密'}
  - defer: '没有经过注册提供和出售加密资产证券' still incomplete; defer to include the asset names: [27,28,29,30,31,32,33,34,35]
  - release_units: None

* W11. {36: 'Tronics', 37: '和'}
  - carried_over: {27: '没有',28: '经过',29: '注册',30: '提供',31: '和',32: '出售',33: '加密',34: '资产',35: '证券'}
  - defer: 'Tronics和' does not yet form a stable sense unit; defer to next window: [36,37]
  - release_units:
    1. 没有经过注册提供和出售加密资产证券, latency-forced partial release; releasing the verb phrase now because current window must output: [27,28,29,30,31,32,33,34,35]

* W12. {38: 'BitTorrent。'}
  - carried_over: {36: 'Tronics',37: '和'}
  - defer: None
  - release_units:
    1. Tronics和BitTorrent。 carried over with current; stable noun phrase: [36,37,38]
  result:
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9],
  [10,11,12,13,14,15,16,17,18,19,20,21,22],
  [23,24],
  [25,26],
  [27,28,29,30,31,32,33,34,35],
  [36,37,38]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '三', 1: '月', 2: '二十二', 3: '号，'} - output: release_units 1.{0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. input: {4: '美国', 5: '证券', 6: '交易', 7: '委员'} - output: release_units None
* W2. input: {8: '会', 9: '宣布', 10: '对'} - output: release_units 1.{4: '美国', 5: '证券', 6: '交易', 7: '委员', 8: '会'}; 2.{9: '宣布'}
* W3. input: {11: '加密', 12: '资产', 13: '企业'} - output: release_units None
* W4. input: {14: '家', 15: '孙', 16: '宇晨'} - output: release_units None <- ISSUE1: consecutive non-empty wait x2, delay too long.
* W5. input: {17: '及', 18: '其', 19: '三', 20: '家'} - output: release_units None <- ISSUE1: consecutive non-empty wait x3, delay too long.
* W6. input: {21: '全资', 22: '公司', 23: '提起'} - output: release_units 1.{10: '对', 11: '加密', 12: '资产', 13: '企业', 14: '家', 15: '孙', 16: '宇晨', 17: '及', 18: '其', 19: '三', 20: '家', 21: '全资', 22: '公司'} <- ISSUE2: oversized chunk release unit 1 size=13 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {24: '诉讼，', 25: '指控'} - output: release_units 1.{23: '提起', 24: '诉讼，'}
* W8. input: {26: '他们', 27: '没有', 28: '经过', 29: '注册'} - output: release_units 1.{25: '指控', 26: '他们'}
* W9. input: {30: '提供', 31: '和', 32: '出售', 33: '加密'} - output: release_units None
* W10. input: {34: '资产', 35: '证券'} - output: release_units 1.{27: '没有', 28: '经过', 29: '注册', 30: '提供', 31: '和', 32: '出售', 33: '加密', 34: '资产', 35: '证券'} <- ISSUE2: oversized chunk release unit 1 size=9 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {36: 'Tronics', 37: '和'} - output: release_units None
* W12. input: {38: 'BitTorrent。'} - output: release_units 1.{36: 'Tronics', 37: '和', 38: 'BitTorrent。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '三', 1: '月', 2: '二十二', 3: '号，'} - output: release_units 1.{0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. input: {4: '美国', 5: '证券', 6: '交易', 7: '委员'} - output: release_units None
* W2. input: {8: '会', 9: '宣布', 10: '对'} - output: release_units 1.{4: '美国', 5: '证券', 6: '交易', 7: '委员', 8: '会'}
* W3. input: {11: '加密', 12: '资产', 13: '企业'} - output: release_units None
* W4. input: {14: '家', 15: '孙', 16: '宇晨'} - output: release_units 1.{9: '宣布', 10: '对', 11: '加密', 12: '资产', 13: '企业', 14: '家', 15: '孙', 16: '宇晨'} <- ISSUE2: oversized chunk release unit 1 size=8 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {17: '及', 18: '其', 19: '三', 20: '家'} - output: release_units None
* W6. input: {21: '全资', 22: '公司', 23: '提起'} - output: release_units 1.{17: '及', 18: '其', 19: '三', 20: '家', 21: '全资', 22: '公司'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {24: '诉讼，', 25: '指控'} - output: release_units 1.{23: '提起', 24: '诉讼，'}
* W8. input: {26: '他们', 27: '没有', 28: '经过', 29: '注册'} - output: release_units 1.{25: '指控', 26: '他们'}; 2.{27: '没有', 28: '经过', 29: '注册'}
* W9. input: {30: '提供', 31: '和', 32: '出售', 33: '加密'} - output: release_units None
* W10. input: {34: '资产', 35: '证券'} - output: release_units 1.{30: '提供', 31: '和', 32: '出售', 33: '加密', 34: '资产', 35: '证券'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {36: 'Tronics', 37: '和'} - output: release_units None
* W12. input: {38: 'BitTorrent。'} - output: release_units 1.{36: 'Tronics', 37: '和', 38: 'BitTorrent。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '三', 1: '月', 2: '二十二', 3: '号，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 三月二十二号， stable minimal sense unit: [0,1,2,3]

* W1. {4: '美国', 5: '证券', 6: '交易', 7: '委员'}
  - carried_over: None
  - defer: '美国证券交易委员' is not yet a stable minimal sense unit; defer it to the next window because the previous window already had output: [4,5,6,7]
  - release_units: None

* W2. {8: '会', 9: '宣布', 10: '对'}
  - carried_over: {4: '美国', 5: '证券', 6: '交易', 7: '委员'}
  - defer: '宣布对' is not yet a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9,10]
  - release_units:
    1. 美国证券交易委员会, '美国证券交易委员' is carried over from the previous window; released here because it is now a stable minimal sense unit: [4,5,6,7,8]

* W3. {11: '加密', 12: '资产', 13: '企业'}
  - carried_over: {9: '宣布', 10: '对'}
  - defer: '宣布对加密资产企业' does not yet form a stable minimal sense unit; defer it to the next window because the previous window had output and the next window is non-empty: [9,10,11,12,13]
  - release_units: None

* W4. {14: '家', 15: '孙', 16: '宇晨'}
  - carried_over: {9: '宣布', 10: '对', 11: '加密', 12: '资产', 13: '企业'}
  - defer: None
  - release_units:
    1. 宣布对加密资产企业家孙宇晨, latency-forced partial release; the previous window had no output, so the current window must flush something; this is the smallest locally stable meaning unit available now: [9,10,11,12,13,14,15,16]

* W5. {17: '及', 18: '其', 19: '三', 20: '家'}
  - carried_over: None
  - defer: '及其三家' does not yet form a stable minimal sense unit; defer it to the next window because the previous window already had output: [17,18,19,20]
  - release_units: None

* W6. {21: '全资', 22: '公司', 23: '提起'}
  - carried_over: {17: '及', 18: '其', 19: '三', 20: '家'}
  - defer: '提起' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [23]
  - release_units:
    1. 及其三家全资公司, '及其三家' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19,20,21,22]

* W7. {24: '诉讼，', 25: '指控'}
  - carried_over: {23: '提起'}
  - defer: '指控' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 提起诉讼， '提起' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24]

* W8. {26: '他们', 27: '没有', 28: '经过', 29: '注册'}
  - carried_over: {25: '指控'}
  - defer: '没有经过注册' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [27,28,29]
  - release_units:
    1. 指控他们, '指控' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26]

* W9. {30: '提供', 31: '和', 32: '出售', 33: '加密'}
  - carried_over: {27: '没有', 28: '经过', 29: '注册'}
  - defer: '提供和出售加密' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [30,31,32,33]
  - release_units:
    1. 没有经过注册, '没有经过注册' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28,29]

* W10. {34: '资产', 35: '证券'}
  - carried_over: {30: '提供', 31: '和', 32: '出售', 33: '加密'}
  - defer: None
  - release_units:
    1. 提供和出售加密资产证券, '提供和出售加密' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32,33,34,35]

* W11. {36: 'Tronics', 37: '和'}
  - carried_over: None
  - defer: 'Tronics和' does not yet form a stable minimal sense unit; defer it to the next window because the previous window already had output: [36,37]
  - release_units: None

* W12. {38: 'BitTorrent。'}
  - carried_over: {36: 'Tronics', 37: '和'}
  - defer: None
  - release_units:
    1. Tronics和BitTorrent。 'Tronics和' is carried over from the previous window; released here because it is now a stable minimal sense unit: [36,37,38]
  result:
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9,10,11,12,13,14,15,16],
  [17,18,19,20,21,22],
  [23,24],
  [25,26],
  [27,28,29],
  [30,31,32,33,34,35],
  [36,37,38]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '三', 1: '月', 2: '二十二', 3: '号，'} - output: release_units 1.{0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. input: {4: '美国', 5: '证券', 6: '交易', 7: '委员'} - output: release_units None
* W2. input: {8: '会', 9: '宣布', 10: '对'} - output: release_units 1.{4: '美国', 5: '证券', 6: '交易', 7: '委员', 8: '会'}
* W3. input: {11: '加密', 12: '资产', 13: '企业'} - output: release_units None
* W4. input: {14: '家', 15: '孙', 16: '宇晨'} - output: release_units 1.{9: '宣布', 10: '对', 11: '加密', 12: '资产', 13: '企业', 14: '家', 15: '孙', 16: '宇晨'} <- ISSUE2: oversized chunk release unit 1 size=8 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {17: '及', 18: '其', 19: '三', 20: '家'} - output: release_units None
* W6. input: {21: '全资', 22: '公司', 23: '提起'} - output: release_units 1.{17: '及', 18: '其', 19: '三', 20: '家', 21: '全资', 22: '公司'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {24: '诉讼，', 25: '指控'} - output: release_units 1.{23: '提起', 24: '诉讼，'}
* W8. input: {26: '他们', 27: '没有', 28: '经过', 29: '注册'} - output: release_units 1.{25: '指控', 26: '他们'}; 2.{27: '没有', 28: '经过', 29: '注册'}
* W9. input: {30: '提供', 31: '和', 32: '出售', 33: '加密'} - output: release_units None
* W10. input: {34: '资产', 35: '证券'} - output: release_units 1.{30: '提供', 31: '和', 32: '出售', 33: '加密', 34: '资产', 35: '证券'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {36: 'Tronics', 37: '和'} - output: release_units None
* W12. input: {38: 'BitTorrent。'} - output: release_units 1.{36: 'Tronics', 37: '和', 38: 'BitTorrent。'}

Reconfirm the RULEs and your task!


- retry: 2/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '三', 1: '月', 2: '二十二', 3: '号，'} - output: release_units 1.{0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. input: {4: '美国', 5: '证券', 6: '交易', 7: '委员'} - output: release_units None
* W2. input: {8: '会', 9: '宣布', 10: '对'} - output: release_units 1.{4: '美国', 5: '证券', 6: '交易', 7: '委员', 8: '会'}
* W3. input: {11: '加密', 12: '资产', 13: '企业'} - output: release_units 1.{9: '宣布', 10: '对', 11: '加密', 12: '资产'}
* W4. input: {14: '家', 15: '孙', 16: '宇晨'} - output: release_units 1.{13: '企业', 14: '家', 15: '孙', 16: '宇晨'}
* W5. input: {17: '及', 18: '其', 19: '三', 20: '家'} - output: release_units None
* W6. input: {21: '全资', 22: '公司', 23: '提起'} - output: release_units 1.{19: '三', 20: '家', 21: '全资', 22: '公司'}
* W7. input: {24: '诉讼，', 25: '指控'} - output: release_units 1.{23: '提起', 24: '诉讼，'}
* W8. input: {26: '他们', 27: '没有', 28: '经过', 29: '注册'} - output: release_units 1.{25: '指控', 26: '他们', 27: '没有', 28: '经过', 29: '注册'}
* W9. input: {30: '提供', 31: '和', 32: '出售', 33: '加密'} - output: release_units 1.{30: '提供', 31: '和', 32: '出售'}
* W10. input: {34: '资产', 35: '证券'} - output: release_units 1.{33: '加密', 34: '资产', 35: '证券'}
* W11. input: {36: 'Tronics', 37: '和'} - output: release_units None
* W12. input: {38: 'BitTorrent。'} - output: release_units 1.{17: '及', 18: '其', 36: 'Tronics', 37: '和', 38: 'BitTorrent。'}

Non-monotonic sense unit groups:
ISSUE5: sense_units.groups[9] contains indices [17, 18] that do not come strictly after previous emitted index 35. sense_units.groups must be globally monotonic and non-overlapping.

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '三',1: '月',2: '二十二',3: '号，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 三月二十二号，, date minimal sense unit: [0,1,2,3]

* W1. {4: '美国',5: '证券',6: '交易',7: '委员'}
  - carried_over: None
  - defer: '美国证券交易委员' does not yet form a stable minimal sense unit; defer to next window: [4,5,6,7]
  - release_units: None

* W2. {8: '会',9: '宣布',10: '对'}
  - carried_over: {4: '美国',5: '证券',6: '交易',7: '委员'}
  - defer: '宣布对' does not yet form a stable minimal sense unit; defer to next window: [9,10]
  - release_units:
    1. 美国证券交易委员会, carried over from previous window; released here because it is now a stable minimal sense unit: [4,5,6,7,8]

* W3. {11: '加密',12: '资产',13: '企业'}
  - carried_over: {9: '宣布',10: '对'}
  - defer: '企业' is deferred to next window to combine with '家' to form '企业家': [13]
  - release_units:
    1. 宣布对加密资产, carried over [9,10] combined with current [11,12]; released as a stable verb-preposition phrase: [9,10,11,12]

* W4. {14: '家',15: '孙',16: '宇晨'}
  - carried_over: {13: '企业'}
  - defer: None
  - release_units:
    1. 企业家孙宇晨, '企业' carried over from previous window; forms a stable noun phrase: [13,14,15,16]

* W5. {17: '及',18: '其',19: '三',20: '家'}
  - carried_over: None
  - defer: '及其三家' does not yet form a stable minimal sense unit; defer to next window: [17,18,19,20]
  - release_units: None

* W6. {21: '全资',22: '公司',23: '提起'}
  - carried_over: {17: '及',18: '其',19: '三',20: '家'}
  - defer: '及其提起' does not yet form a stable minimal sense unit; defer to next window: [17,18,23]
  - release_units:
    1. 三家全资公司, carried over [19,20] combined with current [21,22]; released as a stable noun phrase: [19,20,21,22]

* W7. {24: '诉讼，',25: '指控'}
  - carried_over: {17: '及',18: '其',23: '提起'}
  - defer: '及其指控' does not yet form a stable minimal sense unit; defer to next window: [17,18,25]
  - release_units:
    1. 提起诉讼，, '提起' carried over from previous window; forms a stable verb-object unit: [23,24]

* W8. {26: '他们',27: '没有',28: '经过',29: '注册'}
  - carried_over: {17: '及',18: '其',25: '指控'}
  - defer: '及其指控他们没有经过注册' does not yet form a stable minimal sense unit; defer all to next window: [17,18,25,26,27,28,29]
  - release_units: None

* W9. {30: '提供',31: '和',32: '出售',33: '加密'}
  - carried_over: {17: '及',18: '其',25: '指控',26: '他们',27: '没有',28: '经过',29: '注册'}
  - defer: '及其提供和出售加密' does not yet form a stable minimal sense unit; defer to next window: [17,18,30,31,32,33]
  - release_units:
    1. 指控他们没有经过注册, '指控他们没有经过注册' carried over from previous window; released as a stable verb-object clause: [25,26,27,28,29]

* W10. {34: '资产',35: '证券'}
  - carried_over: {17: '及',18: '其',30: '提供',31: '和',32: '出售',33: '加密'}
  - defer: '及其加密资产证券' does not yet form a stable minimal sense unit; defer to next window: [17,18,33,34,35]
  - release_units:
    1. 提供和出售, carried over [30,31,32]; released as a compact verb phrase: [30,31,32]

* W11. {36: 'Tronics',37: '和'}
  - carried_over: {17: '及',18: '其',33: '加密',34: '资产',35: '证券'}
  - defer: '及其Tronics和' does not yet form a stable minimal sense unit; defer to next window: [17,18,36,37]
  - release_units:
    1. 加密资产证券, carried over [33,34,35]; released as a stable noun phrase: [33,34,35]

* W12. {38: 'BitTorrent。'}
  - carried_over: {17: '及',18: '其',36: 'Tronics',37: '和'}
  - defer: None
  - release_units:
    1. 及其Tronics和BitTorrent。, carried over [17,18,36,37] combined with current [38]; released as a stable conjunction-names unit: [17,18,36,37,38]
  result:
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9,10,11,12],
  [13,14,15,16],
  [19,20,21,22],
  [23,24],
  [25,26,27,28,29],
  [30,31,32],
  [33,34,35],
  [17,18,36,37,38]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '三', 1: '月', 2: '二十二', 3: '号，'} - output: release_units 1.{0: '三', 1: '月', 2: '二十二', 3: '号，'}
* W1. input: {4: '美国', 5: '证券', 6: '交易', 7: '委员'} - output: release_units None
* W2. input: {8: '会', 9: '宣布', 10: '对'} - output: release_units 1.{4: '美国', 5: '证券', 6: '交易', 7: '委员', 8: '会'}
* W3. input: {11: '加密', 12: '资产', 13: '企业'} - output: release_units 1.{9: '宣布', 10: '对', 11: '加密', 12: '资产'}
* W4. input: {14: '家', 15: '孙', 16: '宇晨'} - output: release_units 1.{13: '企业', 14: '家', 15: '孙', 16: '宇晨'}
* W5. input: {17: '及', 18: '其', 19: '三', 20: '家'} - output: release_units None
* W6. input: {21: '全资', 22: '公司', 23: '提起'} - output: release_units 1.{19: '三', 20: '家', 21: '全资', 22: '公司'}
* W7. input: {24: '诉讼，', 25: '指控'} - output: release_units 1.{23: '提起', 24: '诉讼，'}
* W8. input: {26: '他们', 27: '没有', 28: '经过', 29: '注册'} - output: release_units 1.{25: '指控', 26: '他们', 27: '没有', 28: '经过', 29: '注册'}
* W9. input: {30: '提供', 31: '和', 32: '出售', 33: '加密'} - output: release_units 1.{30: '提供', 31: '和', 32: '出售'}
* W10. input: {34: '资产', 35: '证券'} - output: release_units 1.{33: '加密', 34: '资产', 35: '证券'}
* W11. input: {36: 'Tronics', 37: '和'} - output: release_units None
* W12. input: {38: 'BitTorrent。'} - output: release_units 1.{17: '及', 18: '其', 36: 'Tronics', 37: '和', 38: 'BitTorrent。'}

Non-monotonic sense unit groups:
ISSUE5: sense_units.groups[9] contains indices [17, 18] that do not come strictly after previous emitted index 35. sense_units.groups must be globally monotonic and non-overlapping.

Reconfirm the RULEs and your task!


- retry: 3/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>三月二十二号，</src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>美国证券交易委员会</src>; start=2.00, end=3.00
* W3. <src>宣布对加密资产</src>; start=3.00, end=4.00
* W4. <src>企业家孙宇晨</src>; start=4.00, end=5.00
* W5. <src>及其</src>; start=5.00, end=6.00
* W6. <src>三家全资公司</src>; start=6.00, end=7.00
* W7. <src>提起诉讼，</src>; start=7.00, end=8.00
* W8. <src>指控他们没有经过注册</src>; start=8.00, end=9.00
* W9. <src>提供和出售</src>; start=9.00, end=10.00
* W10. <src>加密资产证券</src>; start=10.00, end=11.00
* W11. <src><|wait|></src>; start=11.00, end=12.00
* W12. <src>Tronics和BitTorrent。</src>; start=12.00, end=12.51
```

---
=== ZH_UJBZXO0vtl8_W000127 ===

status: finished

raw_text:
同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。

word_indices:
* W0. {0: '同样', 1: '也是'}
* W1. {2: '针对', 3: '要', 4: '留意'}
* W2. {5: '金钱', 6: '的', 7: '部分，'}
* W3. {8: '我们', 9: '从', 10: '这里'}
* W4. {11: '呢', 12: '可以'}
* W5. {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'}
* W6. {18: '副', 19: '卡片，'}
* W7. {20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. {24: '手。'}
* W9. {25: '那么', 26: '手', 27: '的'}
* W10. {28: '时候', 29: '呢，'}
* W11. {30: '通常', 31: '它'}
* W12. {32: '非常', 33: '的'}
* W13. {34: '直白，', 35: '代表', 36: '是'}
* W14. {37: '我们', 38: '的', 39: '金钱'}
* W15. {40: '呢，', 41: '可能', 42: '就'}
* W16. {43: '尽量', 44: '呢'}
* W17. {45: '不要，'}
* W18. {46: '就是'}
* W19. {47: '做', 48: '太多', 49: '的'}
* W20. {50: '规划，'}
* W21. {51: '尤其', 52: '是'}
* W22. {53: '针对', 54: '家中'}
* W23. {55: '的', 56: '男性'}
* W24. {57: '长男。'}

scratchpad:
* W0. {0: '同样', 1: '也是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 同样也是, stable minimal sense unit (discourse): [0,1]

* W1. {2: '针对', 3: '要', 4: '留意'}
  - carried_over: None
  - defer: '针对要留意' does not yet form a stable minimal sense unit; defer it to the next window: [2,3,4]
  - release_units: None

* W2. {5: '金钱', 6: '的', 7: '部分，'}
  - carried_over: {2: '针对', 3: '要', 4: '留意'}
  - defer: '金钱的部分，' is deferred to the next window because only the remainder is deferred after the current window has already emitted something; also to preserve index order: [5,6,7]
  - release_units:
    1. 针对要留意, latency-forced partial release; W1 had no output so W2 must flush, and we release the earlier carried-over tokens to maintain order: [2,3,4]

* W3. {8: '我们', 9: '从', 10: '这里'}
  - carried_over: {5: '金钱', 6: '的', 7: '部分，'}
  - defer: '我们从这里' is deferred to the next window: [8,9,10]
  - release_units:
    1. 金钱的部分，, stable minimal sense unit (noun phrase), carried over from previous window: [5,6,7]

* W4. {11: '呢', 12: '可以'}
  - carried_over: {8: '我们', 9: '从', 10: '这里'}
  - defer: '可以' is deferred to the next window: [12]
  - release_units:
    1. 我们从这里呢, stable minimal sense unit (topic phrase with particle), '我们从这里' carried over plus '呢' from current window: [8,9,10,11]

* W5. {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'}
  - carried_over: {12: '可以'}
  - defer: '这一' is deferred to the next window: [16,17]
  - release_units:
    1. 可以看到的是, stable minimal sense unit (verb phrase), '可以' carried over plus '看到的是' from current window: [12,13,14,15]

* W6. {18: '副', 19: '卡片，'}
  - carried_over: {16: '这', 17: '一'}
  - defer: None
  - release_units:
    1. 这一副卡片，, stable minimal sense unit (noun phrase), carried over '这一' plus '副卡片，': [16,17,18,19]

* W7. {20: '它', 21: '代表', 22: '的', 23: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 它代表的是, stable minimal sense unit (clause fragment): [20,21,22,23]

* W8. {24: '手。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 手。, stable minimal sense unit: [24]

* W9. {25: '那么', 26: '手', 27: '的'}
  - carried_over: None
  - defer: '手的' is deferred to the next window: [26,27]
  - release_units:
    1. 那么, stable minimal sense unit (discourse marker): [25]

* W10. {28: '时候', 29: '呢，'}
  - carried_over: {26: '手', 27: '的'}
  - defer: None
  - release_units:
    1. 手的时候呢，, stable minimal sense unit (topic phrase), carried over '手的' plus '时候呢，': [26,27,28,29]

* W11. {30: '通常', 31: '它'}
  - carried_over: None
  - defer: '它' is deferred to the next window: [31]
  - release_units:
    1. 通常, stable minimal sense unit (adverb): [30]

* W12. {32: '非常', 33: '的'}
  - carried_over: {31: '它'}
  - defer: '的' is deferred to the next window: [33]
  - release_units:
    1. 它非常, latency-forced partial release; '它' carried over plus '非常' from current window: [31,32]

* W13. {34: '直白，', 35: '代表', 36: '是'}
  - carried_over: {33: '的'}
  - defer: '代表是' is deferred to the next window: [35,36]
  - release_units:
    1. 的直白，, stable minimal sense unit (adjective phrase with comma), carried over '的' plus '直白，': [33,34]

* W14. {37: '我们', 38: '的', 39: '金钱'}
  - carried_over: {35: '代表', 36: '是'}
  - defer: None
  - release_units:
    1. 代表是我们的金钱, stable minimal sense unit (verb-object phrase), carried over '代表是' plus '我们的金钱': [35,36,37,38,39]

* W15. {40: '呢，', 41: '可能', 42: '就'}
  - carried_over: None
  - defer: '可能就' is deferred to the next window: [41,42]
  - release_units:
    1. 呢，, small discourse unit (particle with comma): [40]

* W16. {43: '尽量', 44: '呢'}
  - carried_over: {41: '可能', 42: '就'}
  - defer: '呢' is deferred to the next window: [44]
  - release_units:
    1. 可能就尽量, stable adverbial phrase, carried over '可能就' plus '尽量': [41,42,43]

* W17. {45: '不要，'}
  - carried_over: {44: '呢'}
  - defer: '不要，' is deferred to the next window: [45]
  - release_units:
    1. 呢, latency-forced partial release; discourse particle released separately due to order: [44]

* W18. {46: '就是'}
  - carried_over: {45: '不要，'}
  - defer: '就是' is deferred to the next window: [46]
  - release_units:
    1. 不要，, stable minimal sense unit (negative imperative with comma): [45]

* W19. {47: '做', 48: '太多', 49: '的'}
  - carried_over: {46: '就是'}
  - defer: '的' is deferred to the next window: [49]
  - release_units:
    1. 就是做太多, stable verb phrase, carried over '就是' plus '做太多': [46,47,48]

* W20. {50: '规划，'}
  - carried_over: {49: '的'}
  - defer: None
  - release_units:
    1. 的规划，, stable noun phrase, carried over '的' plus '规划，': [49,50]

* W21. {51: '尤其', 52: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 尤其是, stable discourse marker: [51,52]

* W22. {53: '针对', 54: '家中'}
  - carried_over: None
  - defer: '针对家中' does not yet form a stable minimal sense unit; defer it to the next window: [53,54]
  - release_units: None

* W23. {55: '的', 56: '男性'}
  - carried_over: {53: '针对', 54: '家中'}
  - defer: None
  - release_units:
    1. 针对家中的男性, stable minimal sense unit (prepositional phrase), carried over '针对家中' plus '的男性': [53,54,55,56]

* W24. {57: '长男。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 长男。, stable minimal sense unit: [57]

result:
[
[0,1],
[2,3,4],
[5,6,7],
[8,9,10,11],
[12,13,14,15],
[16,17,18,19],
[20,21,22,23],
[24],
[25],
[26,27,28,29],
[30],
[31,32],
[33,34],
[35,36,37,38,39],
[40],
[41,42,43],
[44],
[45],
[46,47,48],
[49,50],
[51,52],
[53,54,55,56],
[57]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units None
* W8. input: {24: '手。'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是', 24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units None
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{25: '那么', 26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常', 31: '它'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{32: '非常', 33: '的', 34: '直白，'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units 1.{35: '代表', 36: '是', 37: '我们', 38: '的', 39: '金钱'}
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{40: '呢，'}; 2.{41: '可能', 42: '就'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units None
* W17. input: {45: '不要，'} - output: release_units 1.{43: '尽量', 44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '同样', 1: '也是'}
  - carried_over: None
  - defer: '同样也是' is not yet a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1]
  - release_units: None

* W1. {2: '针对', 3: '要', 4: '留意'}
  - carried_over: {0: '同样', 1: '也是'}
  - defer: '针对要留意' is not yet a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [2,3,4]
  - release_units:
    1. 同样也是, '同样也是' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1]

* W2. {5: '金钱', 6: '的', 7: '部分，'}
  - carried_over: {2: '针对', 3: '要', 4: '留意'}
  - defer: None
  - release_units:
    1. 针对要留意的部分， '针对要留意' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4,5,6,7]

* W3. {8: '我们', 9: '从', 10: '这里'}
  - carried_over: None
  - defer: '我们从这里' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [8,9,10]
  - release_units: None

* W4. {11: '呢', 12: '可以'}
  - carried_over: {8: '我们', 9: '从', 10: '这里'}
  - defer: '可以' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [12]
  - release_units:
    1. 我们从这里呢, '我们从这里' is carried over from the previous window; released here because it is now a stable minimal sense unit: [8,9,10,11]

* W5. {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'}
  - carried_over: {12: '可以'}
  - defer: '这一' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16,17]
  - release_units:
    1. 可以看到的是, '可以' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13,14,15]

* W6. {18: '副', 19: '卡片，'}
  - carried_over: {16: '这', 17: '一'}
  - defer: None
  - release_units:
    1. 这一副卡片， '这一' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17,18,19]

* W7. {20: '它', 21: '代表', 22: '的', 23: '是'}
  - carried_over: None
  - defer: '它代表的是' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [20,21,22,23]
  - release_units: None

* W8. {24: '手。'}
  - carried_over: {20: '它', 21: '代表', 22: '的', 23: '是'}
  - defer: None
  - release_units:
    1. 它代表的是手。 '它代表的是' is carried over from the previous window; released here because it is now a stable minimal sense unit: [20,21,22,23,24]

* W9. {25: '那么', 26: '手', 27: '的'}
  - carried_over: None
  - defer: '那么手的' is not yet a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [25,26,27]
  - release_units: None

* W10. {28: '时候', 29: '呢，'}
  - carried_over: {25: '那么', 26: '手', 27: '的'}
  - defer: None
  - release_units:
    1. 那么手的时候呢， '那么手的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26,27,28,29]

* W11. {30: '通常', 31: '它'}
  - carried_over: None
  - defer: '通常它' is not yet a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [30,31]
  - release_units: None

* W12. {32: '非常', 33: '的'}
  - carried_over: {30: '通常', 31: '它'}
  - defer: '非常的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [32,33]
  - release_units:
    1. 通常它, '通常它' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31]

* W13. {34: '直白，', 35: '代表', 36: '是'}
  - carried_over: {32: '非常', 33: '的'}
  - defer: '代表是' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [35,36]
  - release_units:
    1. 非常的直白， '非常的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [32,33,34]

* W14. {37: '我们', 38: '的', 39: '金钱'}
  - carried_over: {35: '代表', 36: '是'}
  - defer: None
  - release_units:
    1. 代表是我们的金钱, '代表是' is carried over from the previous window; released here because it is now a stable minimal sense unit: [35,36,37,38,39]

* W15. {40: '呢，', 41: '可能', 42: '就'}
  - carried_over: None
  - defer: '可能就' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [41,42]
  - release_units:
    1. 呢， stable minimal sense unit in the current window: [40]

* W16. {43: '尽量', 44: '呢'}
  - carried_over: {41: '可能', 42: '就'}
  - defer: '尽量呢' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [43,44]
  - release_units:
    1. 可能就, '可能就' is carried over from the previous window; released here because it is now a stable minimal sense unit: [41,42]

* W17. {45: '不要，'}
  - carried_over: {43: '尽量', 44: '呢'}
  - defer: None
  - release_units:
    1. 尽量呢不要， '尽量呢' is carried over from the previous window; released here because it is now a stable minimal sense unit: [43,44,45]

* W18. {46: '就是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 就是, stable minimal sense unit in the current window: [46]

* W19. {47: '做', 48: '太多', 49: '的'}
  - carried_over: None
  - defer: '做太多的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [47,48,49]
  - release_units: None

* W20. {50: '规划，'}
  - carried_over: {47: '做', 48: '太多', 49: '的'}
  - defer: None
  - release_units:
    1. 做太多的规划， '做太多的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [47,48,49,50]

* W21. {51: '尤其', 52: '是'}
  - carried_over: None
  - defer: '尤其是' is not yet a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [51,52]
  - release_units: None

* W22. {53: '针对', 54: '家中'}
  - carried_over: {51: '尤其', 52: '是'}
  - defer: '针对家中' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [53,54]
  - release_units:
    1. 尤其是, '尤其是' is carried over from the previous window; released here because it is now a stable minimal sense unit: [51,52]

* W23. {55: '的', 56: '男性'}
  - carried_over: {53: '针对', 54: '家中'}
  - defer: None
  - release_units:
    1. 针对家中的男性, '针对家中' is carried over from the previous window; released here because it is now a stable minimal sense unit: [53,54,55,56]

* W24. {57: '长男。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 长男。 stable minimal sense unit in the current window: [57]
  result:
[
  [0,1],
  [2,3,4,5,6,7],
  [8,9,10,11],
  [12,13,14,15],
  [16,17,18,19],
  [20,21,22,23,24],
  [25,26,27,28,29],
  [30,31],
  [32,33,34],
  [35,36,37,38,39],
  [40],
  [41,42],
  [43,44,45],
  [46],
  [47,48,49,50],
  [51,52],
  [53,54,55,56],
  [57]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units None
* W8. input: {24: '手。'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是', 24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units None
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{25: '那么', 26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常', 31: '它'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{32: '非常', 33: '的', 34: '直白，'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units 1.{35: '代表', 36: '是', 37: '我们', 38: '的', 39: '金钱'}
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{40: '呢，'}; 2.{41: '可能', 42: '就'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units None
* W17. input: {45: '不要，'} - output: release_units 1.{43: '尽量', 44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. input: {24: '手。'} - output: release_units 1.{24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units None
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{25: '那么', 26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{31: '它', 32: '非常', 33: '的', 34: '直白，'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units 1.{35: '代表', 36: '是', 37: '我们', 38: '的'}
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{39: '金钱', 40: '呢，'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units None
* W17. input: {45: '不要，'} - output: release_units 1.{41: '可能', 42: '就', 43: '尽量', 44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '同样', 1: '也是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 同样也是, stable minimal sense unit: [0,1]

* W1. {2: '针对', 3: '要', 4: '留意'}
  - carried_over: None
  - defer: '针对要留意' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [2,3,4]
  - release_units: None

* W2. {5: '金钱', 6: '的', 7: '部分，'}
  - carried_over: {2: '针对', 3: '要', 4: '留意'}
  - defer: None
  - release_units:
    1. 针对要留意金钱的部分， '针对要留意' is carried over from the previous window; released here because it is now a stable minimal sense unit — '针对' is a coverb governing the whole phrase '要留意金钱的部分', and splitting would break the tight coverb-phrase cohesion: [2,3,4,5,6,7]

* W3. {8: '我们', 9: '从', 10: '这里'}
  - carried_over: None
  - defer: '我们从这里' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [8,9,10]
  - release_units: None

* W4. {11: '呢', 12: '可以'}
  - carried_over: {8: '我们', 9: '从', 10: '这里'}
  - defer: '可以' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [12]
  - release_units:
    1. 我们从这里呢, '我们从这里' is carried over from the previous window; released here because it is now a stable minimal sense unit forming a topic phrase with '呢': [8,9,10,11]

* W5. {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'}
  - carried_over: {12: '可以'}
  - defer: '这一' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16,17]
  - release_units:
    1. 可以看到的是, '可以' is carried over from the previous window; released here as a stable minimal sense unit — this is a compact predicate-complement unit: [12,13,14,15]

* W6. {18: '副', 19: '卡片，'}
  - carried_over: {16: '这', 17: '一'}
  - defer: None
  - release_units:
    1. 这一副卡片， '这一' is carried over from the previous window; released here because it is now a stable minimal sense unit forming a compact noun phrase: [16,17,18,19]

* W7. {20: '它', 21: '代表', 22: '的', 23: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 它代表的是, stable minimal sense unit — subject + '的是' construction forming a compact local frame: [20,21,22,23]

* W8. {24: '手。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 手。 stable minimal sense unit completing the previous frame: [24]

* W9. {25: '那么', 26: '手', 27: '的'}
  - carried_over: None
  - defer: '那么手' would be released together with the following material; defer all of it to the next window because the previous window (W8) had output and delaying by one window is still legal: [25,26,27]
  - release_units: None

* W10. {28: '时候', 29: '呢，'}
  - carried_over: {25: '那么', 26: '手', 27: '的'}
  - defer: None
  - release_units:
    1. 那么手的时候呢， '那么手' is carried over from the previous window; released here because it is now a stable minimal sense unit forming a topic phrase: [25,26,27,28,29]

* W11. {30: '通常', 31: '它'}
  - carried_over: None
  - defer: '通常它' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the previous window (W10) had output and delaying by one window is still legal: [30,31]
  - release_units: None

* W12. {32: '非常', 33: '的'}
  - carried_over: {30: '通常', 31: '它'}
  - defer: '它非常的' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [31,32,33]
  - release_units:
    1. 通常, latency-forced partial release; the current window follows a no-output window (W11) so it must flush something; '通常' is a small discourse adverb that carries local interpretability: [30]

* W13. {34: '直白，', 35: '代表', 36: '是'}
  - carried_over: {31: '它', 32: '非常', 33: '的'}
  - defer: '代表是' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [35,36]
  - release_units:
    1. 它非常的直白， '它非常的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [31,32,33,34]

* W14. {37: '我们', 38: '的', 39: '金钱'}
  - carried_over: {35: '代表', 36: '是'}
  - defer: '金钱' is deferred to keep '代表是我们的' as a compact local unit, preserving tighter cohesion so that the following '金钱呢，' can stay together in the next window: [39]
  - release_units:
    1. 代表是我们的, '代表是' is carried over from the previous window; released here because it is now a stable minimal sense unit: [35,36,37,38]

* W15. {40: '呢，', 41: '可能', 42: '就'}
  - carried_over: {39: '金钱'}
  - defer: '可能就' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [41,42]
  - release_units:
    1. 金钱呢， '金钱' is carried over from the previous window; released here because it is now a stable minimal sense unit — the noun + discourse particle forms a compact local unit, avoiding exposing '呢' alone: [39,40]

* W16. {43: '尽量', 44: '呢'}
  - carried_over: {41: '可能', 42: '就'}
  - defer: '可能就尽量呢' does not yet form a stable release unit / minimal sense unit in the current window; defer all to the next window because the previous window (W15) had output and delaying by one window is still legal: [41,42,43,44]
  - release_units: None

* W17. {45: '不要，'}
  - carried_over: {41: '可能', 42: '就', 43: '尽量', 44: '呢'}
  - defer: None
  - release_units:
    1. 可能就尽量呢不要， '可能就尽量呢' is carried over from the previous window; released here because it is now a stable minimal sense unit forming a coherent adverbial-plus-negation phrase: [41,42,43,44,45]

* W18. {46: '就是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 就是, stable minimal sense unit as a discourse stance marker: [46]

* W19. {47: '做', 48: '太多', 49: '的'}
  - carried_over: None
  - defer: '做太多的' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the previous window (W18) had output and delaying by one window is still legal: [47,48,49]
  - release_units: None

* W20. {50: '规划，'}
  - carried_over: {47: '做', 48: '太多', 49: '的'}
  - defer: None
  - release_units:
    1. 做太多的规划， '做太多的' is carried over from the previous window; released here because it is now a stable minimal sense unit forming a verb-object phrase: [47,48,49,50]

* W21. {51: '尤其', 52: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 尤其是, stable minimal sense unit: [51,52]

* W22. {53: '针对', 54: '家中'}
  - carried_over: None
  - defer: '针对家中' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the previous window (W21) had output and delaying by one window is still legal: [53,54]
  - release_units: None

* W23. {55: '的', 56: '男性'}
  - carried_over: {53: '针对', 54: '家中'}
  - defer: None
  - release_units:
    1. 针对家中的男性, '针对家中' is carried over from the previous window; released here because it is now a stable minimal sense unit forming a coverb-phrase: [53,54,55,56]

* W24. {57: '长男。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 长男。 stable minimal sense unit: [57]
  result:
[
  [0,1],
  [2,3,4,5,6,7],
  [8,9,10,11],
  [12,13,14,15],
  [16,17,18,19],
  [20,21,22,23],
  [24],
  [25,26,27,28,29],
  [30],
  [31,32,33,34],
  [35,36,37,38],
  [39,40],
  [41,42,43,44,45],
  [46],
  [47,48,49,50],
  [51,52],
  [53,54,55,56],
  [57]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. input: {24: '手。'} - output: release_units 1.{24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units None
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{25: '那么', 26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{31: '它', 32: '非常', 33: '的', 34: '直白，'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units 1.{35: '代表', 36: '是', 37: '我们', 38: '的'}
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{39: '金钱', 40: '呢，'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units None
* W17. input: {45: '不要，'} - output: release_units 1.{41: '可能', 42: '就', 43: '尽量', 44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!


- retry: 2/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. input: {24: '手。'} - output: release_units 1.{24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units 1.{25: '那么'}
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常'}; 2.{31: '它'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{32: '非常', 33: '的', 34: '直白，'}; 2.{35: '代表', 36: '是'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units None
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{37: '我们', 38: '的', 39: '金钱', 40: '呢，'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units 1.{41: '可能', 42: '就', 43: '尽量'}
* W17. input: {45: '不要，'} - output: release_units 1.{44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '同样', 1: '也是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 同样也是, stable minimal sense unit in the current window: [0,1]

* W1. {2: '针对', 3: '要', 4: '留意'}
  - carried_over: None
  - defer: '针对要留意' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal and the previous window had output: [2,3,4]
  - release_units: None

* W2. {5: '金钱', 6: '的', 7: '部分，'}
  - carried_over: {2: '针对', 3: '要', 4: '留意'}
  - defer: None
  - release_units:
    1. 针对要留意金钱的部分， '针对要留意' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4,5,6,7]

* W3. {8: '我们', 9: '从', 10: '这里'}
  - carried_over: None
  - defer: '我们从这里' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal and the previous window had output: [8,9,10]
  - release_units: None

* W4. {11: '呢', 12: '可以'}
  - carried_over: {8: '我们', 9: '从', 10: '这里'}
  - defer: '可以' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [12]
  - release_units:
    1. 我们从这里呢, '我们从这里' is carried over from the previous window; released here because it is now a stable minimal sense unit: [8,9,10,11]

* W5. {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'}
  - carried_over: {12: '可以'}
  - defer: '这一' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16,17]
  - release_units:
    1. 可以看到的是, '可以' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13,14,15]

* W6. {18: '副', 19: '卡片，'}
  - carried_over: {16: '这', 17: '一'}
  - defer: None
  - release_units:
    1. 这一副卡片， '这一' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17,18,19]

* W7. {20: '它', 21: '代表', 22: '的', 23: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 它代表的是, stable minimal sense unit in the current window: [20,21,22,23]

* W8. {24: '手。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 手。 stable minimal sense unit in the current window: [24]

* W9. {25: '那么', 26: '手', 27: '的'}
  - carried_over: None
  - defer: '手的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal and the previous window had output: [26,27]
  - release_units:
    1. 那么, stable minimal sense unit in the current window: [25]

* W10. {28: '时候', 29: '呢，'}
  - carried_over: {26: '手', 27: '的'}
  - defer: None
  - release_units:
    1. 手的时候呢， '手的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27,28,29]

* W11. {30: '通常', 31: '它'}
  - carried_over: None
  - defer: '它' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [31]
  - release_units:
    1. 通常, stable minimal sense unit in the current window: [30]

* W12. {32: '非常', 33: '的'}
  - carried_over: {31: '它'}
  - defer: '非常的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [32,33]
  - release_units:
    1. 它, '它' is carried over from the previous window; released here because it is now a stable minimal sense unit: [31]

* W13. {34: '直白，', 35: '代表', 36: '是'}
  - carried_over: {32: '非常', 33: '的'}
  - defer: '代表是' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [35,36]
  - release_units:
    1. 非常的直白， '非常的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [32,33,34]

* W14. {37: '我们', 38: '的', 39: '金钱'}
  - carried_over: {35: '代表', 36: '是'}
  - defer: '我们的金钱' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [37,38,39]
  - release_units:
    1. 代表是, '代表是' is carried over from the previous window; released here because it is now a stable minimal sense unit: [35,36]

* W15. {40: '呢，', 41: '可能', 42: '就'}
  - carried_over: {37: '我们', 38: '的', 39: '金钱'}
  - defer: '可能就' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [41,42]
  - release_units:
    1. 我们的金钱呢， '我们的金钱' is carried over from the previous window; released here because it is now a stable minimal sense unit: [37,38,39,40]

* W16. {43: '尽量', 44: '呢'}
  - carried_over: {41: '可能', 42: '就'}
  - defer: '呢' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [44]
  - release_units:
    1. 可能就尽量, '可能就' is carried over from the previous window; released here because it is now a stable minimal sense unit: [41,42,43]

* W17. {45: '不要，'}
  - carried_over: {44: '呢'}
  - defer: None
  - release_units:
    1. 呢不要， '呢' is carried over from the previous window; released here because it is now a stable minimal sense unit: [44,45]

* W18. {46: '就是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 就是, stable minimal sense unit in the current window: [46]

* W19. {47: '做', 48: '太多', 49: '的'}
  - carried_over: None
  - defer: '做太多的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal and the previous window had output: [47,48,49]
  - release_units: None

* W20. {50: '规划，'}
  - carried_over: {47: '做', 48: '太多', 49: '的'}
  - defer: None
  - release_units:
    1. 做太多的规划， '做太多的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [47,48,49,50]

* W21. {51: '尤其', 52: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 尤其是, stable minimal sense unit in the current window: [51,52]

* W22. {53: '针对', 54: '家中'}
  - carried_over: None
  - defer: '针对家中' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal and the previous window had output: [53,54]
  - release_units: None

* W23. {55: '的', 56: '男性'}
  - carried_over: {53: '针对', 54: '家中'}
  - defer: None
  - release_units:
    1. 针对家中的男性, '针对家中' is carried over from the previous window; released here because it is now a stable minimal sense unit: [53,54,55,56]

* W24. {57: '长男。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 长男。 stable minimal sense unit in the current window: [57]
  result:
[
  [0,1],
  [2,3,4,5,6,7],
  [8,9,10,11],
  [12,13,14,15],
  [16,17,18,19],
  [20,21,22,23],
  [24],
  [25],
  [26,27,28,29],
  [30],
  [31],
  [32,33,34],
  [35,36],
  [37,38,39,40],
  [41,42,43],
  [44,45],
  [46],
  [47,48,49,50],
  [51,52],
  [53,54,55,56],
  [57]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. input: {24: '手。'} - output: release_units 1.{24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units 1.{25: '那么'}
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常'}; 2.{31: '它'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{32: '非常', 33: '的', 34: '直白，'}; 2.{35: '代表', 36: '是'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units None
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{37: '我们', 38: '的', 39: '金钱', 40: '呢，'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units 1.{41: '可能', 42: '就', 43: '尽量'}
* W17. input: {45: '不要，'} - output: release_units 1.{44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!


- retry: 3/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. input: {24: '手。'} - output: release_units 1.{24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units 1.{25: '那么'}
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常', 31: '它'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{32: '非常', 33: '的', 34: '直白，'}; 2.{35: '代表', 36: '是'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units None
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{37: '我们', 38: '的', 39: '金钱', 40: '呢，'}; 2.{41: '可能', 42: '就'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units None
* W17. input: {45: '不要，'} - output: release_units 1.{43: '尽量', 44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '同样', 1: '也是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 同样也是, stable minimal sense unit in the current window: [0,1]

* W1. {2: '针对', 3: '要', 4: '留意'}
  - carried_over: None
  - defer: '针对要留意' does not yet form an ideal stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [2,3,4]
  - release_units: None

* W2. {5: '金钱', 6: '的', 7: '部分，'}
  - carried_over: {2: '针对', 3: '要', 4: '留意'}
  - defer: None
  - release_units:
    1. 针对要留意金钱的部分， '针对要留意' is carried over from the previous window; released here because it is now a stable minimal sense unit covering a preposition + verb-object phrase: [2,3,4,5,6,7]

* W3. {8: '我们', 9: '从', 10: '这里'}
  - carried_over: None
  - defer: '我们从这里' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [8,9,10]
  - release_units: None

* W4. {11: '呢', 12: '可以'}
  - carried_over: {8: '我们', 9: '从', 10: '这里'}
  - defer: '可以' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [12]
  - release_units:
    1. 我们从这里呢, '我们从这里' is carried over from the previous window; released here because adding '呢' creates a stable topic-marked locative unit: [8,9,10,11]

* W5. {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'}
  - carried_over: {12: '可以'}
  - defer: '这一' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16,17]
  - release_units:
    1. 可以看到的是, '可以' is carried over from the previous window; released here because it now forms a stable verb phrase meaning 'can see is': [12,13,14,15]

* W6. {18: '副', 19: '卡片，'}
  - carried_over: {16: '这', 17: '一'}
  - defer: None
  - release_units:
    1. 这一副卡片， '这一' is carried over from the previous window; released here because it now forms a stable demonstrative-classifier-noun unit: [16,17,18,19]

* W7. {20: '它', 21: '代表', 22: '的', 23: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 它代表的是, stable minimal sense unit in the current window: [20,21,22,23]

* W8. {24: '手。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 手。 stable minimal sense unit in the current window: [24]

* W9. {25: '那么', 26: '手', 27: '的'}
  - carried_over: None
  - defer: '手的' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [26,27]
  - release_units:
    1. 那么, stable minimal sense unit in the current window: [25]

* W10. {28: '时候', 29: '呢，'}
  - carried_over: {26: '手', 27: '的'}
  - defer: None
  - release_units:
    1. 手的时候呢， '手的' is carried over from the previous window; released here because it now forms a stable time-reference topic phrase: [26,27,28,29]

* W11. {30: '通常', 31: '它'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 通常它, stable minimal sense unit in the current window: [30,31]

* W12. {32: '非常', 33: '的'}
  - carried_over: None
  - defer: '非常的' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [32,33]
  - release_units: None

* W13. {34: '直白，', 35: '代表', 36: '是'}
  - carried_over: {32: '非常', 33: '的'}
  - defer: None
  - release_units:
    1. 非常的直白， '非常的' is carried over from the previous window; released here because it now forms a stable adjective phrase: [32,33,34]
    2. 代表是, stable minimal sense unit in the current window: [35,36]

* W14. {37: '我们', 38: '的', 39: '金钱'}
  - carried_over: None
  - defer: '我们的金钱' is deferred to the next window to combine with the following topic particle for a fuller local unit: [37,38,39]
  - release_units: None

* W15. {40: '呢，', 41: '可能', 42: '就'}
  - carried_over: {37: '我们', 38: '的', 39: '金钱'}
  - defer: None
  - release_units:
    1. 我们的金钱呢， '我们的金钱' is carried over from the previous window; released here because it now forms a stable topic phrase: [37,38,39,40]
    2. 可能就, stable adverb chain in the current window: [41,42]

* W16. {43: '尽量', 44: '呢'}
  - carried_over: None
  - defer: '尽量呢' does not yet form a stable minimal sense unit; defer to next window: [43,44]
  - release_units: None

* W17. {45: '不要，'}
  - carried_over: {43: '尽量', 44: '呢'}
  - defer: None
  - release_units:
    1. 尽量呢不要， '尽量呢' is carried over from the previous window; released here because it now forms a stable verb phrase meaning 'try not to': [43,44,45]

* W18. {46: '就是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 就是, stable discourse linking unit in the current window: [46]

* W19. {47: '做', 48: '太多', 49: '的'}
  - carried_over: None
  - defer: '做太多的' does not yet form a stable minimal sense unit; defer to next window because the previous window had output and the next window is non-empty: [47,48,49]
  - release_units: None

* W20. {50: '规划，'}
  - carried_over: {47: '做', 48: '太多', 49: '的'}
  - defer: None
  - release_units:
    1. 做太多的规划， '做太多的' is carried over from the previous window; released here because it now forms a stable verb-object unit: [47,48,49,50]

* W21. {51: '尤其', 52: '是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 尤其是, stable adverb collocation in the current window: [51,52]

* W22. {53: '针对', 54: '家中'}
  - carried_over: None
  - defer: '针对家中' does not yet form a stable minimal sense unit; defer to next window because the previous window had output and the next window is non-empty: [53,54]
  - release_units: None

* W23. {55: '的', 56: '男性'}
  - carried_over: {53: '针对', 54: '家中'}
  - defer: None
  - release_units:
    1. 针对家中的男性, '针对家中' is carried over from the previous window; released here because it now forms a stable prepositional noun phrase: [53,54,55,56]

* W24. {57: '长男。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 长男。 stable nominal unit in the current window: [57]
  result:
[
  [0,1],
  [2,3,4,5,6,7],
  [8,9,10,11],
  [12,13,14,15],
  [16,17,18,19],
  [20,21,22,23],
  [24],
  [25],
  [26,27,28,29],
  [30,31],
  [32,33,34],
  [35,36],
  [37,38,39,40],
  [41,42],
  [43,44,45],
  [46],
  [47,48,49,50],
  [51,52],
  [53,54,55,56],
  [57]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '同样', 1: '也是'} - output: release_units 1.{0: '同样', 1: '也是'}
* W1. input: {2: '针对', 3: '要', 4: '留意'} - output: release_units None
* W2. input: {5: '金钱', 6: '的', 7: '部分，'} - output: release_units 1.{2: '针对', 3: '要', 4: '留意', 5: '金钱', 6: '的', 7: '部分，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {8: '我们', 9: '从', 10: '这里'} - output: release_units None
* W4. input: {11: '呢', 12: '可以'} - output: release_units 1.{8: '我们', 9: '从', 10: '这里', 11: '呢'}
* W5. input: {13: '看到', 14: '的', 15: '是', 16: '这', 17: '一'} - output: release_units 1.{12: '可以', 13: '看到', 14: '的', 15: '是'}
* W6. input: {18: '副', 19: '卡片，'} - output: release_units 1.{16: '这', 17: '一', 18: '副', 19: '卡片，'}
* W7. input: {20: '它', 21: '代表', 22: '的', 23: '是'} - output: release_units 1.{20: '它', 21: '代表', 22: '的', 23: '是'}
* W8. input: {24: '手。'} - output: release_units 1.{24: '手。'}
* W9. input: {25: '那么', 26: '手', 27: '的'} - output: release_units 1.{25: '那么'}
* W10. input: {28: '时候', 29: '呢，'} - output: release_units 1.{26: '手', 27: '的', 28: '时候', 29: '呢，'}
* W11. input: {30: '通常', 31: '它'} - output: release_units 1.{30: '通常', 31: '它'}
* W12. input: {32: '非常', 33: '的'} - output: release_units None
* W13. input: {34: '直白，', 35: '代表', 36: '是'} - output: release_units 1.{32: '非常', 33: '的', 34: '直白，'}; 2.{35: '代表', 36: '是'}
* W14. input: {37: '我们', 38: '的', 39: '金钱'} - output: release_units None
* W15. input: {40: '呢，', 41: '可能', 42: '就'} - output: release_units 1.{37: '我们', 38: '的', 39: '金钱', 40: '呢，'}; 2.{41: '可能', 42: '就'}
* W16. input: {43: '尽量', 44: '呢'} - output: release_units None
* W17. input: {45: '不要，'} - output: release_units 1.{43: '尽量', 44: '呢', 45: '不要，'}
* W18. input: {46: '就是'} - output: release_units 1.{46: '就是'}
* W19. input: {47: '做', 48: '太多', 49: '的'} - output: release_units None
* W20. input: {50: '规划，'} - output: release_units 1.{47: '做', 48: '太多', 49: '的', 50: '规划，'}
* W21. input: {51: '尤其', 52: '是'} - output: release_units 1.{51: '尤其', 52: '是'}
* W22. input: {53: '针对', 54: '家中'} - output: release_units None
* W23. input: {55: '的', 56: '男性'} - output: release_units 1.{53: '针对', 54: '家中', 55: '的', 56: '男性'}
* W24. input: {57: '长男。'} - output: release_units 1.{57: '长男。'}

Reconfirm the RULEs and your task!


- retry: 4/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>同样也是</src>; start=0.00, end=1.00
* W1. <src>针对要留意</src>; start=1.00, end=2.00
* W2. <src>金钱的部分，</src>; start=2.00, end=3.00
* W3. <src><|wait|></src>; start=3.00, end=4.00
* W4. <src>我们从这里呢</src>; start=4.00, end=5.00
* W5. <src>可以看到的是</src>; start=5.00, end=6.00
* W6. <src>这一副卡片，</src>; start=6.00, end=7.00
* W7. <src>它代表的是</src>; start=7.00, end=8.00
* W8. <src>手。</src>; start=8.00, end=9.00
* W9. <src>那么</src>; start=9.00, end=10.00
* W10. <src>手的时候呢，</src>; start=10.00, end=11.00
* W11. <src>通常</src>; start=11.00, end=12.00
* W12. <src>它非常</src>; start=12.00, end=13.00
* W13. <src>的直白，</src>; start=13.00, end=14.00
* W14. <src>代表是我们的金钱</src>; start=14.00, end=15.00
* W15. <src>呢，</src>; start=15.00, end=16.00
* W16. <src>可能就尽量呢</src>; start=16.00, end=17.00
* W17. <src>不要，</src>; start=17.00, end=18.00
* W18. <src><|wait|></src>; start=18.00, end=19.00
* W19. <src>就是做太多</src>; start=19.00, end=20.00
* W20. <src>的规划，</src>; start=20.00, end=21.00
* W21. <src>尤其是</src>; start=21.00, end=22.00
* W22. <src><|wait|></src>; start=22.00, end=23.00
* W23. <src>针对家中的男性</src>; start=23.00, end=24.00
* W24. <src>长男。</src>; start=24.00, end=24.87
```

---
