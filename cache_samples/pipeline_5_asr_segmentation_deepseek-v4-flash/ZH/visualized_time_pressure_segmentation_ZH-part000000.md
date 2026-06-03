=== ZH_VJeW1Z4n0Qc_W000018 ===

status: finished

raw_text:
然后在洋馆的后面呢，其实有三排的，就是可以DIY互动的工作室跟体验的店家。但是因为今天我来的时间刚好是连假的最后一天，又是礼拜一，蛮多店都没开的，再加上洋馆也没有开放，所以我今天真的就是来这里单纯的逛逛。

word_indices:
* W0. {0: '然后', 1: '在', 2: '洋'}
* W1. {3: '馆', 4: '的', 5: '后面', 6: '呢，'}
* W2. {7: '其实', 8: '有'}
* W3. {9: '三', 10: '排'}
* W4. {11: '的，', 12: '就是', 13: '可以'}
* W5. {14: 'DIY'}
* W6. {15: '互动', 16: '的', 17: '工作', 18: '室'}
* W7. {19: '跟', 20: '体验', 21: '的'}
* W8. {22: '店家。'}
* W9. {23: '但是', 24: '因为', 25: '今天'}
* W10. {26: '我来', 27: '的', 28: '时间', 29: '刚好'}
* W11. {30: '是', 31: '连假', 32: '的'}
* W12. {33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'}
* W13. {38: '一，', 39: '蛮多', 40: '店', 41: '都'}
* W14. {42: '没开', 43: '的，', 44: '再'}
* W15. {45: '加上', 46: '洋', 47: '馆'}
* W16. {48: '也', 49: '没有', 50: '开放，'}
* W17. {51: '所以', 52: '我', 53: '今天'}
* W18. {54: '真的', 55: '就是', 56: '来', 57: '这里'}
* W19. {58: '单纯', 59: '的'}
* W20. {60: '逛逛。'}

scratchpad:
* W0. {0: '然后', 1: '在', 2: '洋'}
  - carried_over: None
  - defer: '在洋' is not yet a stable unit; defer to next window: [1,2]
  - release_units:
    1. 然后, stable discourse unit: [0]

* W1. {3: '馆', 4: '的', 5: '后面', 6: '呢，'}
  - carried_over: {1: '在', 2: '洋'}
  - defer: '呢，' is a host-dependent particle; defer to next window: [6]
  - release_units:
    1. 在洋馆的后面, '在洋' carried over: [1,2,3,4,5]

* W2. {7: '其实', 8: '有'}
  - carried_over: {6: '呢，'}
  - defer: '呢其实有' does not yet form a stable unit; defer to next window: [6,7,8]
  - release_units: None

* W3. {9: '三', 10: '排'}
  - carried_over: {6: '呢，', 7: '其实', 8: '有'}
  - defer: None
  - release_units:
    1. 呢其实有三排, '呢其实有' carried over: [6,7,8,9,10]

* W4. {11: '的，', 12: '就是', 13: '可以'}
  - carried_over: None
  - defer: '就是可以' does not yet form a stable unit; defer to next window: [12,13]
  - release_units:
    1. 的，, leftover tail from previous clause; released now: [11]

* W5. {14: 'DIY'}
  - carried_over: {12: '就是', 13: '可以'}
  - defer: None
  - release_units:
    1. 就是可以DIY, '就是可以' carried over: [12,13,14]

* W6. {15: '互动', 16: '的', 17: '工作', 18: '室'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 互动的工作室, stable unit: [15,16,17,18]

* W7. {19: '跟', 20: '体验', 21: '的'}
  - carried_over: None
  - defer: '跟体验的' does not yet have its object; defer all to next window: [19,20,21]
  - release_units: None

* W8. {22: '店家。'}
  - carried_over: {19: '跟', 20: '体验', 21: '的'}
  - defer: None
  - release_units:
    1. 跟体验的店家。, '跟体验的' carried over: [19,20,21,22]

* W9. {23: '但是', 24: '因为', 25: '今天'}
  - carried_over: None
  - defer: '因为今天' does not yet form a stable unit; defer to next window: [24,25]
  - release_units:
    1. 但是, stable discourse unit: [23]

* W10. {26: '我来', 27: '的', 28: '时间', 29: '刚好'}
  - carried_over: {24: '因为', 25: '今天'}
  - defer: '刚好' is not yet a stable unit; defer to next window: [29]
  - release_units:
    1. 因为今天我来的时间, '因为今天' carried over: [24,25,26,27,28]

* W11. {30: '是', 31: '连假', 32: '的'}
  - carried_over: {29: '刚好'}
  - defer: None
  - release_units:
    1. 刚好是连假的, '刚好' carried over: [29,30,31,32]

* W12. {33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'}
  - carried_over: None
  - defer: '又是礼拜' does not yet form a stable unit; defer to next window: [36,37]
  - release_units:
    1. 最后一天，, stable unit: [33,34,35]

* W13. {38: '一，', 39: '蛮多', 40: '店', 41: '都'}
  - carried_over: {36: '又是', 37: '礼拜'}
  - defer: '蛮多店都' does not yet form a stable unit; defer to next window: [39,40,41]
  - release_units:
    1. 又是礼拜一，, '又是礼拜' carried over: [36,37,38]

* W14. {42: '没开', 43: '的，', 44: '再'}
  - carried_over: {39: '蛮多', 40: '店', 41: '都'}
  - defer: '再' is not yet a stable unit; defer to next window: [44]
  - release_units:
    1. 蛮多店都没开的，, '蛮多店都' carried over: [39,40,41,42,43]

* W15. {45: '加上', 46: '洋', 47: '馆'}
  - carried_over: {44: '再'}
  - defer: None
  - release_units:
    1. 再加上洋馆, '再' carried over: [44,45,46,47]

* W16. {48: '也', 49: '没有', 50: '开放，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 也没有开放，, stable unit: [48,49,50]

* W17. {51: '所以', 52: '我', 53: '今天'}
  - carried_over: None
  - defer: '我今天' does not yet form a stable unit; defer to next window: [52,53]
  - release_units:
    1. 所以, stable discourse unit: [51]

* W18. {54: '真的', 55: '就是', 56: '来', 57: '这里'}
  - carried_over: {52: '我', 53: '今天'}
  - defer: '来这里' does not yet form a stable unit; defer to next window: [56,57]
  - release_units:
    1. 我真的就是, '我今天' carried over: [52,53,54,55]

* W19. {58: '单纯', 59: '的'}
  - carried_over: {56: '来', 57: '这里'}
  - defer: None
  - release_units:
    1. 来这里单纯的, '来这里' carried over: [56,57,58,59]

* W20. {60: '逛逛。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 逛逛。, stable unit: [60]

result:
[
[0],
[1,2,3,4,5],
[6,7,8,9,10],
[11],
[12,13,14],
[15,16,17,18],
[19,20,21,22],
[23],
[24,25,26,27,28],
[29,30,31,32],
[33,34,35],
[36,37,38],
[39,40,41,42,43],
[44,45,46,47],
[48,49,50],
[51],
[52,53,54,55],
[56,57,58,59],
[60]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '然后', 1: '在', 2: '洋'} - output: release_units None
* W1. input: {3: '馆', 4: '的', 5: '后面', 6: '呢，'} - output: release_units 1.{0: '然后', 1: '在', 2: '洋', 3: '馆', 4: '的', 5: '后面', 6: '呢，'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W2. input: {7: '其实', 8: '有'} - output: release_units None
* W3. input: {9: '三', 10: '排'} - output: release_units 1.{7: '其实', 8: '有', 9: '三', 10: '排'}
* W4. input: {11: '的，', 12: '就是', 13: '可以'} - output: release_units None
* W5. input: {14: 'DIY'} - output: release_units 1.{11: '的，', 12: '就是', 13: '可以', 14: 'DIY'}
* W6. input: {15: '互动', 16: '的', 17: '工作', 18: '室'} - output: release_units 1.{15: '互动', 16: '的', 17: '工作', 18: '室'}
* W7. input: {19: '跟', 20: '体验', 21: '的'} - output: release_units None
* W8. input: {22: '店家。'} - output: release_units 1.{19: '跟', 20: '体验', 21: '的', 22: '店家。'}
* W9. input: {23: '但是', 24: '因为', 25: '今天'} - output: release_units None
* W10. input: {26: '我来', 27: '的', 28: '时间', 29: '刚好'} - output: release_units 1.{23: '但是', 24: '因为', 25: '今天', 26: '我来', 27: '的', 28: '时间', 29: '刚好'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {30: '是', 31: '连假', 32: '的'} - output: release_units None
* W12. input: {33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'} - output: release_units 1.{30: '是', 31: '连假', 32: '的', 33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'} <- ISSUE2: oversized chunk release unit 1 size=8 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W13. input: {38: '一，', 39: '蛮多', 40: '店', 41: '都'} - output: release_units None
* W14. input: {42: '没开', 43: '的，', 44: '再'} - output: release_units 1.{38: '一，', 39: '蛮多', 40: '店', 41: '都', 42: '没开', 43: '的，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W15. input: {45: '加上', 46: '洋', 47: '馆'} - output: release_units 1.{44: '再', 45: '加上', 46: '洋', 47: '馆'}
* W16. input: {48: '也', 49: '没有', 50: '开放，'} - output: release_units 1.{48: '也', 49: '没有', 50: '开放，'}
* W17. input: {51: '所以', 52: '我', 53: '今天'} - output: release_units None
* W18. input: {54: '真的', 55: '就是', 56: '来', 57: '这里'} - output: release_units 1.{51: '所以', 52: '我', 53: '今天', 54: '真的', 55: '就是', 56: '来', 57: '这里'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W19. input: {58: '单纯', 59: '的'} - output: release_units None
* W20. input: {60: '逛逛。'} - output: release_units 1.{58: '单纯', 59: '的', 60: '逛逛。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '然后', 1: '在', 2: '洋'}
  - carried_over: None
  - defer: '然后在洋' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1,2]
  - release_units: None

* W1. {3: '馆', 4: '的', 5: '后面', 6: '呢，'}
  - carried_over: {0: '然后', 1: '在', 2: '洋'}
  - defer: None
  - release_units:
    1. 然后在洋馆的后面呢， '然后在洋' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2,3,4,5,6]

* W2. {7: '其实', 8: '有'}
  - carried_over: None
  - defer: '其实有' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [7,8]
  - release_units: None

* W3. {9: '三', 10: '排'}
  - carried_over: {7: '其实', 8: '有'}
  - defer: None
  - release_units:
    1. 其实有三排, '其实有' is carried over from the previous window; released here because it is now a stable minimal sense unit: [7,8,9,10]

* W4. {11: '的，', 12: '就是', 13: '可以'}
  - carried_over: None
  - defer: '的，就是可以' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [11,12,13]
  - release_units: None

* W5. {14: 'DIY'}
  - carried_over: {11: '的，', 12: '就是', 13: '可以'}
  - defer: None
  - release_units:
    1. 的，就是可以DIY, latency-forced partial release; the previous window had no output, so the current window must release something; this is the smallest locally interpretable fragment available: [11,12,13,14]

* W6. {15: '互动', 16: '的', 17: '工作', 18: '室'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 互动的工作室, stable minimal sense unit in the current window: [15,16,17,18]

* W7. {19: '跟', 20: '体验', 21: '的'}
  - carried_over: None
  - defer: '跟体验的' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [19,20,21]
  - release_units: None

* W8. {22: '店家。'}
  - carried_over: {19: '跟', 20: '体验', 21: '的'}
  - defer: None
  - release_units:
    1. 跟体验的店家。 '跟体验的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20,21,22]

* W9. {23: '但是', 24: '因为', 25: '今天'}
  - carried_over: None
  - defer: '但是因为今天' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [23,24,25]
  - release_units: None

* W10. {26: '我来', 27: '的', 28: '时间', 29: '刚好'}
  - carried_over: {23: '但是', 24: '因为', 25: '今天'}
  - defer: None
  - release_units:
    1. 但是因为今天我来的时间刚好, '但是因为今天' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25,26,27,28,29]

* W11. {30: '是', 31: '连假', 32: '的'}
  - carried_over: None
  - defer: '是连假的' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [30,31,32]
  - release_units: None

* W12. {33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'}
  - carried_over: {30: '是', 31: '连假', 32: '的'}
  - defer: None
  - release_units:
    1. 是连假的最后一天，又是礼拜, '是连假的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32,33,34,35,36,37]

* W13. {38: '一，', 39: '蛮多', 40: '店', 41: '都'}
  - carried_over: None
  - defer: '一，蛮多店都' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [38,39,40,41]
  - release_units: None

* W14. {42: '没开', 43: '的，', 44: '再'}
  - carried_over: {38: '一，', 39: '蛮多', 40: '店', 41: '都'}
  - defer: '再' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [44]
  - release_units:
    1. 一，蛮多店都没开的， latency-forced partial release; the previous window had no output, so the current window must release something; this is the minimal locally interpretable fragment, deferring '再' to the next window: [38,39,40,41,42,43]

* W15. {45: '加上', 46: '洋', 47: '馆'}
  - carried_over: {44: '再'}
  - defer: None
  - release_units:
    1. 再加上洋馆, '再' is carried over from the previous window; released here because it is now a stable minimal sense unit: [44,45,46,47]

* W16. {48: '也', 49: '没有', 50: '开放，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 也没有开放， stable minimal sense unit in the current window: [48,49,50]

* W17. {51: '所以', 52: '我', 53: '今天'}
  - carried_over: None
  - defer: '所以我今天' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [51,52,53]
  - release_units: None

* W18. {54: '真的', 55: '就是', 56: '来', 57: '这里'}
  - carried_over: {51: '所以', 52: '我', 53: '今天'}
  - defer: None
  - release_units:
    1. 所以我今天真的就是来这里, '所以我今天' is carried over from the previous window; released here because it is now a stable minimal sense unit: [51,52,53,54,55,56,57]

* W19. {58: '单纯', 59: '的'}
  - carried_over: None
  - defer: '单纯的' does not yet form a stable minimal sense unit here; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [58,59]
  - release_units: None

* W20. {60: '逛逛。'}
  - carried_over: {58: '单纯', 59: '的'}
  - defer: None
  - release_units:
    1. 单纯的逛逛。 '单纯的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [58,59,60]
  result:
[
  [0,1,2,3,4,5,6],
  [7,8,9,10],
  [11,12,13,14],
  [15,16,17,18],
  [19,20,21,22],
  [23,24,25,26,27,28,29],
  [30,31,32,33,34,35,36,37],
  [38,39,40,41,42,43],
  [44,45,46,47],
  [48,49,50],
  [51,52,53,54,55,56,57],
  [58,59,60]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '然后', 1: '在', 2: '洋'} - output: release_units None
* W1. input: {3: '馆', 4: '的', 5: '后面', 6: '呢，'} - output: release_units 1.{0: '然后', 1: '在', 2: '洋', 3: '馆', 4: '的', 5: '后面', 6: '呢，'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W2. input: {7: '其实', 8: '有'} - output: release_units None
* W3. input: {9: '三', 10: '排'} - output: release_units 1.{7: '其实', 8: '有', 9: '三', 10: '排'}
* W4. input: {11: '的，', 12: '就是', 13: '可以'} - output: release_units None
* W5. input: {14: 'DIY'} - output: release_units 1.{11: '的，', 12: '就是', 13: '可以', 14: 'DIY'}
* W6. input: {15: '互动', 16: '的', 17: '工作', 18: '室'} - output: release_units 1.{15: '互动', 16: '的', 17: '工作', 18: '室'}
* W7. input: {19: '跟', 20: '体验', 21: '的'} - output: release_units None
* W8. input: {22: '店家。'} - output: release_units 1.{19: '跟', 20: '体验', 21: '的', 22: '店家。'}
* W9. input: {23: '但是', 24: '因为', 25: '今天'} - output: release_units None
* W10. input: {26: '我来', 27: '的', 28: '时间', 29: '刚好'} - output: release_units 1.{23: '但是', 24: '因为', 25: '今天', 26: '我来', 27: '的', 28: '时间', 29: '刚好'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {30: '是', 31: '连假', 32: '的'} - output: release_units None
* W12. input: {33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'} - output: release_units 1.{30: '是', 31: '连假', 32: '的', 33: '最后', 34: '一', 35: '天，', 36: '又是', 37: '礼拜'} <- ISSUE2: oversized chunk release unit 1 size=8 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W13. input: {38: '一，', 39: '蛮多', 40: '店', 41: '都'} - output: release_units None
* W14. input: {42: '没开', 43: '的，', 44: '再'} - output: release_units 1.{38: '一，', 39: '蛮多', 40: '店', 41: '都', 42: '没开', 43: '的，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W15. input: {45: '加上', 46: '洋', 47: '馆'} - output: release_units 1.{44: '再', 45: '加上', 46: '洋', 47: '馆'}
* W16. input: {48: '也', 49: '没有', 50: '开放，'} - output: release_units 1.{48: '也', 49: '没有', 50: '开放，'}
* W17. input: {51: '所以', 52: '我', 53: '今天'} - output: release_units None
* W18. input: {54: '真的', 55: '就是', 56: '来', 57: '这里'} - output: release_units 1.{51: '所以', 52: '我', 53: '今天', 54: '真的', 55: '就是', 56: '来', 57: '这里'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W19. input: {58: '单纯', 59: '的'} - output: release_units None
* W20. input: {60: '逛逛。'} - output: release_units 1.{58: '单纯', 59: '的', 60: '逛逛。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>然后</src>; start=0.00, end=1.00
* W1. <src>在洋馆的后面</src>; start=1.00, end=2.00
* W2. <src><|wait|></src>; start=2.00, end=3.00
* W3. <src>呢，其实有三排</src>; start=3.00, end=4.00
* W4. <src>的，</src>; start=4.00, end=5.00
* W5. <src>就是可以DIY</src>; start=5.00, end=6.00
* W6. <src>互动的工作室</src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>跟体验的店家。</src>; start=8.00, end=9.00
* W9. <src>但是</src>; start=9.00, end=10.00
* W10. <src>因为今天我来的时间</src>; start=10.00, end=11.00
* W11. <src>刚好是连假的</src>; start=11.00, end=12.00
* W12. <src>最后一天，</src>; start=12.00, end=13.00
* W13. <src>又是礼拜一，</src>; start=13.00, end=14.00
* W14. <src>蛮多店都没开的，</src>; start=14.00, end=15.00
* W15. <src>再加上洋馆</src>; start=15.00, end=16.00
* W16. <src>也没有开放，</src>; start=16.00, end=17.00
* W17. <src>所以</src>; start=17.00, end=18.00
* W18. <src>我今天真的就是</src>; start=18.00, end=19.00
* W19. <src>来这里单纯的</src>; start=19.00, end=20.00
* W20. <src>逛逛。</src>; start=20.00, end=20.97
```

---
=== ZH_Y4xRc2amPxY_W000056 ===

status: finished

raw_text:
我们采用了以吃脂脂肪、肥肉和油为主的饮食结构以后呢，那给我们带来了巨大的好处。第一个好处呢，就是我们减肥了。

word_indices:
* W0. {0: '我们', 1: '采用', 2: '了'}
* W1. {3: '以'}
* W2. {4: '吃脂', 5: '脂肪、'}
* W3. {6: '肥肉', 7: '和', 8: '油', 9: '为'}
* W4. {10: '主', 11: '的', 12: '饮食', 13: '结构'}
* W5. {14: '以后', 15: '呢，'}
* W6. {16: '那', 17: '给', 18: '我们'}
* W7. {19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'}
* W8. {24: '第一', 25: '个'}
* W9. {26: '好处', 27: '呢，'}
* W10. {28: '就是', 29: '我们'}
* W11. {30: '减肥', 31: '了。'}

scratchpad:
* W0. {0: '我们', 1: '采用', 2: '了'}
  - carried_over: None
  - defer: '我们采用了' is not yet a stable minimal sense unit; defer to next window because the next window is non-empty and delaying by one window is legal: [0,1,2]
  - release_units: None

* W1. {3: '以'}
  - carried_over: {0: '我们', 1: '采用', 2: '了'}
  - defer: '以' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after releasing the forced flush: [3]
  - release_units:
    1. 我们采用了, latency-forced partial release; the previous window had no output, so the current window must flush the smallest locally interpretable fragment: [0,1,2]

* W2. {4: '吃脂', 5: '脂肪、'}
  - carried_over: {3: '以'}
  - defer: None
  - release_units:
    1. 以吃脂脂肪、, '以' is carried over from the previous window; released here as a prepositional phrase fragment that already carries local meaning and helps keep output continuous: [3,4,5]

* W3. {6: '肥肉', 7: '和', 8: '油', 9: '为'}
  - carried_over: None
  - defer: '为' does not yet form a stable minimal sense unit; defer it to the next window because releasing the noun phrase now keeps chunk sizes small and output continuous: [9]
  - release_units:
    1. 肥肉和油, stable minimal sense unit (noun phrase) in the current window: [6,7,8]

* W4. {10: '主', 11: '的', 12: '饮食', 13: '结构'}
  - carried_over: {9: '为'}
  - defer: None
  - release_units:
    1. 为主的饮食结构, '为' is carried over from the previous window; released here as a compact noun phrase unit: [9,10,11,12,13]

* W5. {14: '以后', 15: '呢，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 以后呢， stable minimal sense unit (temporal + discourse marker): [14,15]

* W6. {16: '那', 17: '给', 18: '我们'}
  - carried_over: None
  - defer: '给我们' does not yet form a stable minimal sense unit; defer it to combine with the following verb: [17,18]
  - release_units:
    1. 那, stable minimal sense unit (discourse marker): [16]

* W7. {19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'}
  - carried_over: {17: '给', 18: '我们'}
  - defer: None
  - release_units:
    1. 给我们带来了, '给我们' is carried over from the previous window; released as a compact verb unit (prepositional phrase + verb): [17,18,19,20]
    2. 巨大的好处。, stable noun phrase unit: [21,22,23]

* W8. {24: '第一', 25: '个'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 第一个, stable numeral-classifier unit: [24,25]

* W9. {26: '好处', 27: '呢，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 好处呢， stable noun + discourse particle unit: [26,27]

* W10. {28: '就是', 29: '我们'}
  - carried_over: None
  - defer: '我们' does not yet form a stable minimal sense unit; defer it to combine with the following predicate: [29]
  - release_units:
    1. 就是, stable discourse marker unit: [28]

* W11. {30: '减肥', 31: '了。'}
  - carried_over: {29: '我们'}
  - defer: None
  - release_units:
    1. 我们减肥了。, '我们' is carried over from the previous window; released as a complete clause unit: [29,30,31]

result:
[
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11,12,13],
  [14,15],
  [16],
  [17,18,19,20],
  [21,22,23],
  [24,25],
  [26,27],
  [28],
  [29,30,31]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '我们', 1: '采用', 2: '了'} - output: release_units 1.{0: '我们', 1: '采用', 2: '了'}
* W1. input: {3: '以'} - output: release_units None
* W2. input: {4: '吃脂', 5: '脂肪、'} - output: release_units None <- ISSUE1: consecutive non-empty wait x2, delay too long.
* W3. input: {6: '肥肉', 7: '和', 8: '油', 9: '为'} - output: release_units 1.{3: '以', 4: '吃脂', 5: '脂肪、', 6: '肥肉', 7: '和', 8: '油'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W4. input: {10: '主', 11: '的', 12: '饮食', 13: '结构'} - output: release_units 1.{9: '为', 10: '主', 11: '的', 12: '饮食', 13: '结构'}
* W5. input: {14: '以后', 15: '呢，'} - output: release_units 1.{14: '以后', 15: '呢，'}
* W6. input: {16: '那', 17: '给', 18: '我们'} - output: release_units 1.{16: '那'}
* W7. input: {19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'} - output: release_units 1.{17: '给', 18: '我们', 19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W8. input: {24: '第一', 25: '个'} - output: release_units 1.{24: '第一', 25: '个'}
* W9. input: {26: '好处', 27: '呢，'} - output: release_units 1.{26: '好处', 27: '呢，'}
* W10. input: {28: '就是', 29: '我们'} - output: release_units 1.{28: '就是'}
* W11. input: {30: '减肥', 31: '了。'} - output: release_units 1.{29: '我们', 30: '减肥', 31: '了。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '我们', 1: '采用', 2: '了'}
  - carried_over: None
  - defer: '我们采用了' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1,2]
  - release_units: None

* W1. {3: '以'}
  - carried_over: {0: '我们', 1: '采用', 2: '了'}
  - defer: '以' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [3]
  - release_units:
    1. 我们采用了, latency-forced partial release; previous window had no output, so the current window must flush the smallest locally interpretable fragment: [0,1,2]

* W2. {4: '吃脂', 5: '脂肪、'}
  - carried_over: {3: '以'}
  - defer: '以吃脂脂肪、' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and delaying by one window is still legal: [3,4,5]
  - release_units: None

* W3. {6: '肥肉', 7: '和', 8: '油', 9: '为'}
  - carried_over: {3: '以', 4: '吃脂', 5: '脂肪、'}
  - defer: '为' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9]
  - release_units:
    1. 以吃脂脂肪、肥肉和油, '以吃脂脂肪、' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3,4,5,6,7,8]

* W4. {10: '主', 11: '的', 12: '饮食', 13: '结构'}
  - carried_over: {9: '为'}
  - defer: None
  - release_units:
    1. 为主的饮食结构, '为' is carried over from the previous window; released here because it is now a stable minimal sense unit: [9,10,11,12,13]

* W5. {14: '以后', 15: '呢，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 以后呢， stable minimal sense unit in the current window: [14,15]

* W6. {16: '那', 17: '给', 18: '我们'}
  - carried_over: None
  - defer: '给我们' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [17,18]
  - release_units:
    1. 那, stable minimal sense unit in the current window: [16]

* W7. {19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'}
  - carried_over: {17: '给', 18: '我们'}
  - defer: None
  - release_units:
    1. 给我们带来了巨大的好处。 '给我们' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19,20,21,22,23]

* W8. {24: '第一', 25: '个'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 第一个, stable minimal sense unit in the current window: [24,25]

* W9. {26: '好处', 27: '呢，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 好处呢， stable minimal sense unit in the current window: [26,27]

* W10. {28: '就是', 29: '我们'}
  - carried_over: None
  - defer: '我们' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [29]
  - release_units:
    1. 就是, stable minimal sense unit in the current window: [28]

* W11. {30: '减肥', 31: '了。'}
  - carried_over: {29: '我们'}
  - defer: None
  - release_units:
    1. 我们减肥了。 '我们' is carried over from the previous window; released here because it is now a stable minimal sense unit: [29,30,31]
  result:
[
  [0,1,2],
  [3,4,5,6,7,8],
  [9,10,11,12,13],
  [14,15],
  [16],
  [17,18,19,20,21,22,23],
  [24,25],
  [26,27],
  [28],
  [29,30,31]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '我们', 1: '采用', 2: '了'} - output: release_units 1.{0: '我们', 1: '采用', 2: '了'}
* W1. input: {3: '以'} - output: release_units None
* W2. input: {4: '吃脂', 5: '脂肪、'} - output: release_units None <- ISSUE1: consecutive non-empty wait x2, delay too long.
* W3. input: {6: '肥肉', 7: '和', 8: '油', 9: '为'} - output: release_units 1.{3: '以', 4: '吃脂', 5: '脂肪、', 6: '肥肉', 7: '和', 8: '油'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W4. input: {10: '主', 11: '的', 12: '饮食', 13: '结构'} - output: release_units 1.{9: '为', 10: '主', 11: '的', 12: '饮食', 13: '结构'}
* W5. input: {14: '以后', 15: '呢，'} - output: release_units 1.{14: '以后', 15: '呢，'}
* W6. input: {16: '那', 17: '给', 18: '我们'} - output: release_units 1.{16: '那'}
* W7. input: {19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'} - output: release_units 1.{17: '给', 18: '我们', 19: '带来', 20: '了', 21: '巨大', 22: '的', 23: '好处。'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W8. input: {24: '第一', 25: '个'} - output: release_units 1.{24: '第一', 25: '个'}
* W9. input: {26: '好处', 27: '呢，'} - output: release_units 1.{26: '好处', 27: '呢，'}
* W10. input: {28: '就是', 29: '我们'} - output: release_units 1.{28: '就是'}
* W11. input: {30: '减肥', 31: '了。'} - output: release_units 1.{29: '我们', 30: '减肥', 31: '了。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>我们采用了</src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>以吃脂脂肪、</src>; start=2.00, end=3.00
* W3. <src>肥肉和油</src>; start=3.00, end=4.00
* W4. <src>为主的饮食结构</src>; start=4.00, end=5.00
* W5. <src>以后呢，</src>; start=5.00, end=6.00
* W6. <src>那</src>; start=6.00, end=7.00
* W7. <src>给我们带来了巨大的好处。</src>; start=7.00, end=8.00
* W8. <src>第一个</src>; start=8.00, end=9.00
* W9. <src>好处呢，</src>; start=9.00, end=10.00
* W10. <src>就是</src>; start=10.00, end=11.00
* W11. <src>我们减肥了。</src>; start=11.00, end=11.36
```

---
=== ZH_Q0a8pjeI4HA_W000054 ===

status: finished

raw_text:
那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命、在招命喽。换句话说，荧幕前的各位朋友。

word_indices:
* W0. {0: '那', 1: '你', 2: '就', 3: '可以'}
* W1. {4: '变成', 5: '那百', 6: '分', 7: '之'}
* W2. {8: '二十', 9: '的', 10: '人，', 11: '去'}
* W3. {12: '成就', 13: '不', 14: '一样', 15: '的'}
* W4. {16: '人生，', 17: '可以'}
* W5. {18: '知命、', 19: '懂'}
* W6. {20: '命、', 21: '用', 22: '命、'}
* W7. {23: '在', 24: '招命'}
* W8. {25: '喽。'}
* W9. {26: '换', 27: '句', 28: '话'}
* W10. {29: '说，', 30: '荧幕', 31: '前', 32: '的'}
* W11. {33: '各位', 34: '朋友。'}

scratchpad:
* W0. {0: '那', 1: '你', 2: '就', 3: '可以'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 那你可以, stable minimal sense unit (discourse opener), size 4 ≤ 5: [0,1,2,3]

* W1. {4: '变成', 5: '那百', 6: '分', 7: '之'}
  - carried_over: None
  - defer: '变成那百分之' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [4,5,6,7]
  - release_units: None

* W2. {8: '二十', 9: '的', 10: '人，', 11: '去'}
  - carried_over: {4: '变成', 5: '那百', 6: '分', 7: '之'}
  - defer: '的人去' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [9,10,11]
  - release_units:
    1. 变成那百分之二十, latency-forced partial release; waiting longer would create an oversized chunk >5 tokens, so the smallest locally stable unit under the size constraint is released now: [4,5,6,7,8]

* W3. {12: '成就', 13: '不', 14: '一样', 15: '的'}
  - carried_over: {9: '的', 10: '人，', 11: '去'}
  - defer: '不一样的' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [13,14,15]
  - release_units:
    1. 的人去成就, minimal sense unit (verb phrase), size 4 ≤ 5: [9,10,11,12]

* W4. {16: '人生，', 17: '可以'}
  - carried_over: {13: '不', 14: '一样', 15: '的'}
  - defer: None
  - release_units:
    1. 不一样的人生，可以, minimal sense unit (noun phrase + modal), size 5 ≤ 5: [13,14,15,16,17]

* W5. {18: '知命、', 19: '懂'}
  - carried_over: None
  - defer: '知命、懂' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [18,19]
  - release_units: None

* W6. {20: '命、', 21: '用', 22: '命、'}
  - carried_over: {18: '知命、', 19: '懂'}
  - defer: None
  - release_units:
    1. 知命、懂命、用命、, stable minimal sense unit (verb series), size 5 ≤ 5: [18,19,20,21,22]

* W7. {23: '在', 24: '招命'}
  - carried_over: None
  - defer: '在招命' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [23,24]
  - release_units: None

* W8. {25: '喽。'}
  - carried_over: {23: '在', 24: '招命'}
  - defer: None
  - release_units:
    1. 在招命喽。, stable minimal sense unit (verb phrase + particle), size 3 ≤ 5: [23,24,25]

* W9. {26: '换', 27: '句', 28: '话'}
  - carried_over: None
  - defer: '换句话说' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [26,27,28]
  - release_units: None

* W10. {29: '说，', 30: '荧幕', 31: '前', 32: '的'}
  - carried_over: {26: '换', 27: '句', 28: '话'}
  - defer: '荧幕前的' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [30,31,32]
  - release_units:
    1. 换句话说， stable minimal sense unit (discourse marker), size 4 ≤ 5: [26,27,28,29]

* W11. {33: '各位', 34: '朋友。'}
  - carried_over: {30: '荧幕', 31: '前', 32: '的'}
  - defer: None
  - release_units:
    1. 荧幕前的各位朋友。, stable minimal sense unit (noun phrase), size 5 ≤ 5: [30,31,32,33,34]

result:
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9,10,11,12],
  [13,14,15,16,17],
  [18,19,20,21,22],
  [23,24,25],
  [26,27,28,29],
  [30,31,32,33,34]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '那', 1: '你', 2: '就', 3: '可以'} - output: release_units 1.{0: '那', 1: '你', 2: '就', 3: '可以'}
* W1. input: {4: '变成', 5: '那百', 6: '分', 7: '之'} - output: release_units None
* W2. input: {8: '二十', 9: '的', 10: '人，', 11: '去'} - output: release_units 1.{4: '变成', 5: '那百', 6: '分', 7: '之', 8: '二十', 9: '的', 10: '人，'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {12: '成就', 13: '不', 14: '一样', 15: '的'} - output: release_units None
* W4. input: {16: '人生，', 17: '可以'} - output: release_units 1.{11: '去', 12: '成就', 13: '不', 14: '一样', 15: '的', 16: '人生，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {18: '知命、', 19: '懂'} - output: release_units 1.{17: '可以', 18: '知命、'}
* W6. input: {20: '命、', 21: '用', 22: '命、'} - output: release_units 1.{19: '懂', 20: '命、'}; 2.{21: '用', 22: '命、'}
* W7. input: {23: '在', 24: '招命'} - output: release_units None
* W8. input: {25: '喽。'} - output: release_units 1.{23: '在', 24: '招命', 25: '喽。'}
* W9. input: {26: '换', 27: '句', 28: '话'} - output: release_units None
* W10. input: {29: '说，', 30: '荧幕', 31: '前', 32: '的'} - output: release_units 1.{26: '换', 27: '句', 28: '话', 29: '说，'}
* W11. input: {33: '各位', 34: '朋友。'} - output: release_units 1.{30: '荧幕', 31: '前', 32: '的', 33: '各位', 34: '朋友。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '那', 1: '你', 2: '就', 3: '可以'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 那你就可以, stable minimal sense unit in the current window: [0,1,2,3]

* W1. {4: '变成', 5: '那百', 6: '分', 7: '之'}
  - carried_over: None
  - defer: '变成那百分之' does not yet form a stable minimal sense unit; defer it to the next window because the previous window had output and delaying by one window is still legal: [4,5,6,7]
  - release_units: None

* W2. {8: '二十', 9: '的', 10: '人，', 11: '去'}
  - carried_over: {4: '变成', 5: '那百', 6: '分', 7: '之'}
  - defer: '去' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [11]
  - release_units:
    1. 变成那百分之二十的人， '变成那百分之' is carried over from the previous window; released here because it is now a stable minimal sense unit: [4,5,6,7,8,9,10]

* W3. {12: '成就', 13: '不', 14: '一样', 15: '的'}
  - carried_over: {11: '去'}
  - defer: '去成就不一样的' does not yet form a stable minimal sense unit; defer it to the next window because the previous window had output and delaying by one window is still legal: [11,12,13,14,15]
  - release_units: None

* W4. {16: '人生，', 17: '可以'}
  - carried_over: {11: '去', 12: '成就', 13: '不', 14: '一样', 15: '的'}
  - defer: '可以' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [17]
  - release_units:
    1. 去成就不一样的人生， '去成就不一样的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [11,12,13,14,15,16]

* W5. {18: '知命、', 19: '懂'}
  - carried_over: {17: '可以'}
  - defer: '懂' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [19]
  - release_units:
    1. 可以知命， '可以' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18]

* W6. {20: '命、', 21: '用', 22: '命、'}
  - carried_over: {19: '懂'}
  - defer: None
  - release_units:
    1. 懂命， '懂' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20]
    2. 用命， stable minimal sense unit in the current window: [21,22]

* W7. {23: '在', 24: '招命'}
  - carried_over: None
  - defer: '在招命' does not yet form a stable minimal sense unit in the current window; defer it to the next window to combine with the following particle: [23,24]
  - release_units: None

* W8. {25: '喽。'}
  - carried_over: {23: '在', 24: '招命'}
  - defer: None
  - release_units:
    1. 在招命喽。 '在招命' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25]

* W9. {26: '换', 27: '句', 28: '话'}
  - carried_over: None
  - defer: '换句话' does not yet form a stable minimal sense unit in the current window; defer it to the next window to combine with '说': [26,27,28]
  - release_units: None

* W10. {29: '说，', 30: '荧幕', 31: '前', 32: '的'}
  - carried_over: {26: '换', 27: '句', 28: '话'}
  - defer: '荧幕前的' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [30,31,32]
  - release_units:
    1. 换句话说， '换句话' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27,28,29]

* W11. {33: '各位', 34: '朋友。'}
  - carried_over: {30: '荧幕', 31: '前', 32: '的'}
  - defer: None
  - release_units:
    1. 荧幕前的各位朋友。 '荧幕前的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32,33,34]
  result:
[
  [0,1,2,3],
  [4,5,6,7,8,9,10],
  [11,12,13,14,15,16],
  [17,18],
  [19,20],
  [21,22],
  [23,24,25],
  [26,27,28,29],
  [30,31,32,33,34]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '那', 1: '你', 2: '就', 3: '可以'} - output: release_units 1.{0: '那', 1: '你', 2: '就', 3: '可以'}
* W1. input: {4: '变成', 5: '那百', 6: '分', 7: '之'} - output: release_units None
* W2. input: {8: '二十', 9: '的', 10: '人，', 11: '去'} - output: release_units 1.{4: '变成', 5: '那百', 6: '分', 7: '之', 8: '二十', 9: '的', 10: '人，'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {12: '成就', 13: '不', 14: '一样', 15: '的'} - output: release_units None
* W4. input: {16: '人生，', 17: '可以'} - output: release_units 1.{11: '去', 12: '成就', 13: '不', 14: '一样', 15: '的', 16: '人生，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {18: '知命、', 19: '懂'} - output: release_units 1.{17: '可以', 18: '知命、'}
* W6. input: {20: '命、', 21: '用', 22: '命、'} - output: release_units 1.{19: '懂', 20: '命、'}; 2.{21: '用', 22: '命、'}
* W7. input: {23: '在', 24: '招命'} - output: release_units None
* W8. input: {25: '喽。'} - output: release_units 1.{23: '在', 24: '招命', 25: '喽。'}
* W9. input: {26: '换', 27: '句', 28: '话'} - output: release_units None
* W10. input: {29: '说，', 30: '荧幕', 31: '前', 32: '的'} - output: release_units 1.{26: '换', 27: '句', 28: '话', 29: '说，'}
* W11. input: {33: '各位', 34: '朋友。'} - output: release_units 1.{30: '荧幕', 31: '前', 32: '的', 33: '各位', 34: '朋友。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>那你就可以</src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>变成那百分之二十</src>; start=2.00, end=3.00
* W3. <src>的人，去成就</src>; start=3.00, end=4.00
* W4. <src>不一样的人生，可以</src>; start=4.00, end=5.00
* W5. <src><|wait|></src>; start=5.00, end=6.00
* W6. <src>知命、懂命、用命、</src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>在招命喽。</src>; start=8.00, end=9.00
* W9. <src><|wait|></src>; start=9.00, end=10.00
* W10. <src>换句话说，</src>; start=10.00, end=11.00
* W11. <src>荧幕前的各位朋友。</src>; start=11.00, end=11.73
```

---
=== ZH_sQjhyfFvfLY_W000018 ===

status: finished

raw_text:
把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class，好，这个这一个那个物件的class，好。

word_indices:
* W0. {0: '把', 1: '它', 2: '丢进'}
* W1. {3: '去', 4: '之后', 5: '呢，', 6: '它', 7: '会', 8: '在'}
* W2. {9: '它', 10: '会', 11: '找到', 12: '这', 13: '一'}
* W3. {14: '个', 15: 'class，', 16: '把', 17: '它'}
* W4. {18: '转变', 19: '成', 20: '为'}
* W5. {}
* W6. {21: '这', 22: '一', 23: '个', 24: 'class'}
* W7. {}
* W8. {25: '的', 26: '的'}
* W9. {27: 'class，'}
* W10. {}
* W11. {28: '好，'}
* W12. {29: '这', 30: '个', 31: '这'}
* W13. {32: '一', 33: '个'}
* W14. {34: '那', 35: '个', 36: '物件'}
* W15. {37: '的', 38: 'class，'}
* W16. {39: '好。'}

scratchpad:
* W0. {0: '把', 1: '它', 2: '丢进'}
  - carried_over: None
  - defer: '把它丢进' is not yet a stable minimal sense unit; it requires the directional complement to complete; defer it to the next window: [0,1,2]
  - release_units: None

* W1. {3: '去', 4: '之后', 5: '呢，', 6: '它', 7: '会', 8: '在'}
  - carried_over: {0: '把', 1: '它', 2: '丢进'}
  - defer: '它会在' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [6,7,8]
  - release_units:
    1. 把它丢进去, compact verb-object-result complement, stable minimal sense unit: [0,1,2,3]
    2. 之后呢，, temporal/discourse unit within the ≤5 size constraint: [4,5]

* W2. {9: '它', 10: '会', 11: '找到', 12: '这', 13: '一'}
  - carried_over: {6: '它', 7: '会', 8: '在'}
  - defer: '它会在它会找到这一' is still incomplete; the object of '找到' is not finished yet; since W1 had output, deferring for one step is legal: [6,7,8,9,10,11,12,13]
  - release_units: None

* W3. {14: '个', 15: 'class，', 16: '把', 17: '它'}
  - carried_over: {6: '它', 7: '会', 8: '在', 9: '它', 10: '会', 11: '找到', 12: '这', 13: '一'}
  - defer: '把它' is the start of a new coverb structure; defer to the next window: [16,17]
  - release_units:
    1. 它会在, latency-forced partial release; this appears to be a spoken false start before the restructured predicate, released as the smallest locally interpretable fragment: [6,7,8]
    2. 它会找到, compact verb phrase, stable minimal sense unit: [9,10,11]
    3. 这一个class，, noun phrase completing the object of 找到, stable minimal sense unit: [12,13,14,15]

* W4. {18: '转变', 19: '成', 20: '为'}
  - carried_over: {16: '把', 17: '它'}
  - defer: None
  - release_units:
    1. 把它转变成为, compact coverb-verb-result complement structure, stable minimal sense unit within the ≤5 size limit: [16,17,18,19,20]

* W5. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W6. {21: '这', 22: '一', 23: '个', 24: 'class'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 这一个class, compact noun phrase, stable minimal sense unit: [21,22,23,24]

* W7. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W8. {25: '的', 26: '的'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 的的, the previous window had no output, so this window must flush; both tokens together form a minimal sense unit capturing the spoken repetition: [25,26]

* W9. {27: 'class，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. class，, stable minimal sense unit in the current window: [27]

* W10. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W11. {28: '好，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 好，, discourse marker, stable minimal sense unit: [28]

* W12. {29: '这', 30: '个', 31: '这'}
  - carried_over: None
  - defer: '这' is a repeated false start or hesitation; it does not yet form a stable minimal sense unit in the current window; defer it to the next window: [31]
  - release_units:
    1. 这个, stable noun phrase, minimal sense unit: [29,30]

* W13. {32: '一', 33: '个'}
  - carried_over: {31: '这'}
  - defer: None
  - release_units:
    1. 这一个, '这' carried over from the previous window; forms a stable noun phrase: [31,32,33]

* W14. {34: '那', 35: '个', 36: '物件'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 那个物件, stable noun phrase, minimal sense unit: [34,35,36]

* W15. {37: '的', 38: 'class，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 的class，, possessive modifier-head structure, stable minimal sense unit: [37,38]

* W16. {39: '好。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 好。, discourse marker, stable minimal sense unit: [39]

result:
[
  [0,1,2,3],
  [4,5],
  [6,7,8],
  [9,10,11],
  [12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24],
  [25,26],
  [27],
  [28],
  [29,30],
  [31,32,33],
  [34,35,36],
  [37,38],
  [39]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '把', 1: '它', 2: '丢进'} - output: release_units None
* W1. input: {3: '去', 4: '之后', 5: '呢，', 6: '它', 7: '会', 8: '在'} - output: release_units 1.{0: '把', 1: '它', 2: '丢进', 3: '去', 4: '之后', 5: '呢，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W2. input: {9: '它', 10: '会', 11: '找到', 12: '这', 13: '一'} - output: release_units 1.{6: '它', 7: '会', 8: '在', 9: '它'}
* W3. input: {14: '个', 15: 'class，', 16: '把', 17: '它'} - output: release_units 1.{10: '会', 11: '找到', 12: '这', 13: '一', 14: '个', 15: 'class，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W4. input: {18: '转变', 19: '成', 20: '为'} - output: release_units 1.{16: '把', 17: '它', 18: '转变', 19: '成', 20: '为'}
* W5. input: {} - output: release_units None
* W6. input: {21: '这', 22: '一', 23: '个', 24: 'class'} - output: release_units 1.{21: '这', 22: '一', 23: '个', 24: 'class'}
* W7. input: {} - output: release_units None
* W8. input: {25: '的', 26: '的'} - output: release_units 1.{25: '的', 26: '的'}
* W9. input: {27: 'class，'} - output: release_units 1.{27: 'class，'}
* W10. input: {} - output: release_units None
* W11. input: {28: '好，'} - output: release_units 1.{28: '好，'}
* W12. input: {29: '这', 30: '个', 31: '这'} - output: release_units 1.{29: '这', 30: '个'}
* W13. input: {32: '一', 33: '个'} - output: release_units 1.{31: '这', 32: '一', 33: '个'}
* W14. input: {34: '那', 35: '个', 36: '物件'} - output: release_units 1.{34: '那', 35: '个', 36: '物件'}
* W15. input: {37: '的', 38: 'class，'} - output: release_units 1.{37: '的', 38: 'class，'}
* W16. input: {39: '好。'} - output: release_units 1.{39: '好。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '把', 1: '它', 2: '丢进'}
  - carried_over: None
  - defer: '把它丢进' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1,2]
  - release_units: None

* W1. {3: '去', 4: '之后', 5: '呢，', 6: '它', 7: '会', 8: '在'}
  - carried_over: {0: '把', 1: '它', 2: '丢进'}
  - defer: '它会在' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [6,7,8]
  - release_units:
    1. 把它丢进去之后呢, '把它丢进' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2,3,4,5]

* W2. {9: '它', 10: '会', 11: '找到', 12: '这', 13: '一'}
  - carried_over: {6: '它', 7: '会', 8: '在'}
  - defer: '会找到这一' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10,11,12,13]
  - release_units:
    1. 它会在它, '它会在' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7,8,9]

* W3. {14: '个', 15: 'class，', 16: '把', 17: '它'}
  - carried_over: {10: '会', 11: '找到', 12: '这', 13: '一'}
  - defer: '把它' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16,17]
  - release_units:
    1. 会找到这一个class， '会找到这一' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12,13,14,15]

* W4. {18: '转变', 19: '成', 20: '为'}
  - carried_over: {16: '把', 17: '它'}
  - defer: None
  - release_units:
    1. 把它转变成为, '把它' is carried over from the previous window; latency-forced partial release; empty windows follow so the current window must flush something now: [16,17,18,19,20]

* W5. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W6. {21: '这', 22: '一', 23: '个', 24: 'class'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 这一个class, stable minimal sense unit in the current window: [21,22,23,24]

* W7. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W8. {25: '的', 26: '的'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 的的, latency-forced partial release; previous window had no output so current window must flush something now: [25,26]

* W9. {27: 'class，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. class， stable minimal sense unit in the current window: [27]

* W10. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W11. {28: '好，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 好， stable minimal sense unit in the current window: [28]

* W12. {29: '这', 30: '个', 31: '这'}
  - carried_over: None
  - defer: '这个这' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [29,30,31]
  - release_units: None

* W13. {32: '一', 33: '个'}
  - carried_over: {29: '这', 30: '个', 31: '这'}
  - defer: '这一个' does not yet form a stable release unit? Actually '这一个' is stable, but we release the smaller unit '这个' first; defer the remainder: [31,32,33]
  - release_units:
    1. 这个, '这个' is carried over from the previous window; released here because it is now a stable minimal sense unit: [29,30]

* W14. {34: '那', 35: '个', 36: '物件'}
  - carried_over: {31: '这', 32: '一', 33: '个'}
  - defer: None
  - release_units:
    1. 这一个, '这一个' is carried over from the previous window; released here because it is now a stable minimal sense unit: [31,32,33]
    2. 那个物件, stable minimal sense unit in the current window: [34,35,36]

* W15. {37: '的', 38: 'class，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 的class， stable minimal sense unit in the current window: [37,38]

* W16. {39: '好。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 好。 stable minimal sense unit in the current window: [39]
  result:
[
  [0,1,2,3,4,5],
  [6,7,8,9],
  [10,11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24],
  [25,26],
  [27],
  [28],
  [29,30],
  [31,32,33],
  [34,35,36],
  [37,38],
  [39]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '把', 1: '它', 2: '丢进'} - output: release_units None
* W1. input: {3: '去', 4: '之后', 5: '呢，', 6: '它', 7: '会', 8: '在'} - output: release_units 1.{0: '把', 1: '它', 2: '丢进', 3: '去', 4: '之后', 5: '呢，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W2. input: {9: '它', 10: '会', 11: '找到', 12: '这', 13: '一'} - output: release_units 1.{6: '它', 7: '会', 8: '在', 9: '它'}
* W3. input: {14: '个', 15: 'class，', 16: '把', 17: '它'} - output: release_units 1.{10: '会', 11: '找到', 12: '这', 13: '一', 14: '个', 15: 'class，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W4. input: {18: '转变', 19: '成', 20: '为'} - output: release_units 1.{16: '把', 17: '它', 18: '转变', 19: '成', 20: '为'}
* W5. input: {} - output: release_units None
* W6. input: {21: '这', 22: '一', 23: '个', 24: 'class'} - output: release_units 1.{21: '这', 22: '一', 23: '个', 24: 'class'}
* W7. input: {} - output: release_units None
* W8. input: {25: '的', 26: '的'} - output: release_units 1.{25: '的', 26: '的'}
* W9. input: {27: 'class，'} - output: release_units 1.{27: 'class，'}
* W10. input: {} - output: release_units None
* W11. input: {28: '好，'} - output: release_units 1.{28: '好，'}
* W12. input: {29: '这', 30: '个', 31: '这'} - output: release_units 1.{29: '这', 30: '个'}
* W13. input: {32: '一', 33: '个'} - output: release_units 1.{31: '这', 32: '一', 33: '个'}
* W14. input: {34: '那', 35: '个', 36: '物件'} - output: release_units 1.{34: '那', 35: '个', 36: '物件'}
* W15. input: {37: '的', 38: 'class，'} - output: release_units 1.{37: '的', 38: 'class，'}
* W16. input: {39: '好。'} - output: release_units 1.{39: '好。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src><|wait|></src>; start=0.00, end=1.00
* W1. <src>把它丢进去之后呢，它会在</src>; start=1.00, end=2.00
* W2. <src>它会找到</src>; start=2.00, end=3.00
* W3. <src>这一个class，</src>; start=3.00, end=4.00
* W4. <src>把它转变成为</src>; start=4.00, end=5.00
* W5. <src><|wait|></src>; start=5.00, end=6.00
* W6. <src>这一个class</src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>的的</src>; start=8.00, end=9.00
* W9. <src>class，</src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=11.00
* W11. <src>好，</src>; start=11.00, end=12.00
* W12. <src>这个</src>; start=12.00, end=13.00
* W13. <src>这一个</src>; start=13.00, end=14.00
* W14. <src>那个物件</src>; start=14.00, end=15.00
* W15. <src>的class，</src>; start=15.00, end=16.00
* W16. <src>好。</src>; start=16.00, end=16.32
```

---
=== ZH_NWf8Wc2GVvM_W000007 ===

status: finished

raw_text:
启示录和翡翠石板都曾经预测到，这十四万四千名光之工作者的到来，会在卡利年代结束时，将地球从黑暗势力的手中拯救出来。

word_indices:
* W0. {0: '启示', 1: '录'}
* W1. {2: '和', 3: '翡翠'}
* W2. {4: '石板', 5: '都', 6: '曾经'}
* W3. {7: '预测', 8: '到，', 9: '这'}
* W4. {10: '十四万', 11: '四千', 12: '名', 13: '光'}
* W5. {14: '之', 15: '工作', 16: '者', 17: '的'}
* W6. {18: '到来，', 19: '会', 20: '在'}
* W7. {21: '卡利', 22: '年代', 23: '结束'}
* W8. {24: '时，', 25: '将'}
* W9. {26: '地球', 27: '从'}
* W10. {28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
* W11. {32: '拯救', 33: '出来。'}

scratchpad:
* W0. {0: '启示', 1: '录'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 启示录, stable minimal sense unit (proper noun, book name): [0,1]

* W1. {2: '和', 3: '翡翠'}
  - carried_over: None
  - defer: '和翡翠' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and the next window is non-empty: [2,3]
  - release_units: None

* W2. {4: '石板', 5: '都', 6: '曾经'}
  - carried_over: {2: '和', 3: '翡翠'}
  - defer: '都曾经' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [5,6]
  - release_units:
    1. 和翡翠石板, carried over from previous window; released here because it is now a stable minimal sense unit: [2,3,4]

* W3. {7: '预测', 8: '到，', 9: '这'}
  - carried_over: {5: '都', 6: '曾经'}
  - defer: '这' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9]
  - release_units:
    1. 都曾经预测到， carried over from previous window; released here because it is now a stable minimal sense unit: [5,6,7,8]

* W4. {10: '十四万', 11: '四千', 12: '名', 13: '光'}
  - carried_over: {9: '这'}
  - defer: '光' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [13]
  - release_units:
    1. 这十四万四千名, carried over from previous window; released here because it is now a stable minimal sense unit (demonstrative + numeral + classifier): [9,10,11,12]

* W5. {14: '之', 15: '工作', 16: '者', 17: '的'}
  - carried_over: {13: '光'}
  - defer: '的' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [17]
  - release_units:
    1. 光之工作者, carried over from previous window; released here because it is now a stable minimal sense unit: [13,14,15,16]

* W6. {18: '到来，', 19: '会', 20: '在'}
  - carried_over: {17: '的'}
  - defer: '会在' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [19,20]
  - release_units:
    1. 的到来， carried over from previous window; released here because it is now a stable minimal sense unit: [17,18]

* W7. {21: '卡利', 22: '年代', 23: '结束'}
  - carried_over: {19: '会', 20: '在'}
  - defer: '结束' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [23]
  - release_units:
    1. 会在卡利年代, carried over from previous window; released here because it is now a stable minimal sense unit: [19,20,21,22]

* W8. {24: '时，', 25: '将'}
  - carried_over: {23: '结束'}
  - defer: '将' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 结束时， carried over from previous window; released here because it is now a stable minimal sense unit: [23,24]

* W9. {26: '地球', 27: '从'}
  - carried_over: {25: '将'}
  - defer: '将地球从' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the previous window had output and delaying by one window is still legal: [25,26,27]
  - release_units: None

* W10. {28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
  - carried_over: {25: '将', 26: '地球', 27: '从'}
  - defer: '黑暗势力的手中' does not yet form a stable release unit paired with the carried-over part; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [28,29,30,31]
  - release_units:
    1. 将地球从, latency-forced partial release; the previous window had no output so the current window must flush something; this is the smallest locally interpretable fragment available: [25,26,27]

* W11. {32: '拯救', 33: '出来。'}
  - carried_over: {28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
  - defer: None
  - release_units:
    1. 黑暗势力的手中, carried over from previous window; released here because it is now a stable minimal sense unit: [28,29,30,31]
    2. 拯救出来, stable minimal sense unit in the current window: [32,33]

result:
[
  [0,1],
  [2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18],
  [19,20,21,22],
  [23,24],
  [25,26,27],
  [28,29,30,31],
  [32,33]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '启示', 1: '录'} - output: release_units 1.{0: '启示', 1: '录'}
* W1. input: {2: '和', 3: '翡翠'} - output: release_units None
* W2. input: {4: '石板', 5: '都', 6: '曾经'} - output: release_units 1.{2: '和', 3: '翡翠', 4: '石板'}
* W3. input: {7: '预测', 8: '到，', 9: '这'} - output: release_units 1.{5: '都', 6: '曾经', 7: '预测', 8: '到，'}; 2.{9: '这'}
* W4. input: {10: '十四万', 11: '四千', 12: '名', 13: '光'} - output: release_units None
* W5. input: {14: '之', 15: '工作', 16: '者', 17: '的'} - output: release_units 1.{10: '十四万', 11: '四千', 12: '名', 13: '光', 14: '之', 15: '工作', 16: '者'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W6. input: {18: '到来，', 19: '会', 20: '在'} - output: release_units 1.{17: '的', 18: '到来，'}
* W7. input: {21: '卡利', 22: '年代', 23: '结束'} - output: release_units 1.{19: '会', 20: '在', 21: '卡利', 22: '年代'}
* W8. input: {24: '时，', 25: '将'} - output: release_units 1.{23: '结束', 24: '时，'}
* W9. input: {26: '地球', 27: '从'} - output: release_units 1.{25: '将', 26: '地球'}
* W10. input: {28: '黑暗', 29: '势力', 30: '的', 31: '手中'} - output: release_units 1.{27: '从', 28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
* W11. input: {32: '拯救', 33: '出来。'} - output: release_units 1.{32: '拯救', 33: '出来。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '启示', 1: '录'}
  - carried_over: None
  - defer: '启示录' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1]
  - release_units: None

* W1. {2: '和', 3: '翡翠'}
  - carried_over: {0: '启示', 1: '录'}
  - defer: '和翡翠' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [2,3]
  - release_units:
    1. 启示录, '启示录' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1]

* W2. {4: '石板', 5: '都', 6: '曾经'}
  - carried_over: {2: '和', 3: '翡翠'}
  - defer: '都曾经' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [5,6]
  - release_units:
    1. 和翡翠石板, '和翡翠' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4]

* W3. {7: '预测', 8: '到，', 9: '这'}
  - carried_over: {5: '都', 6: '曾经'}
  - defer: '这' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [9]
  - release_units:
    1. 都曾经预测到， '都曾经' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7,8]

* W4. {10: '十四万', 11: '四千', 12: '名', 13: '光'}
  - carried_over: {9: '这'}
  - defer: '十四万四千名光' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10,11,12,13]
  - release_units:
    1. 这, '这' is carried over from the previous window; released here because it is now a stable minimal sense unit: [9]

* W5. {14: '之', 15: '工作', 16: '者', 17: '的'}
  - carried_over: {10: '十四万', 11: '四千', 12: '名', 13: '光'}
  - defer: '的' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [17]
  - release_units:
    1. 十四万四千名光之工作者, '十四万四千名光' is carried over from the previous window; the compact `光之工作者` unit is collected here, but the trailing `'的'` is deferred because the full noun phrase (`光之工作者的到来`) is still incomplete: [10,11,12,13,14,15,16]

* W6. {18: '到来，', 19: '会', 20: '在'}
  - carried_over: {17: '的'}
  - defer: '会在' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [19,20]
  - release_units:
    1. 的到来， '的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18]

* W7. {21: '卡利', 22: '年代', 23: '结束'}
  - carried_over: {19: '会', 20: '在'}
  - defer: '结束' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [23]
  - release_units:
    1. 会在卡利年代, '会在' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20,21,22]

* W8. {24: '时，', 25: '将'}
  - carried_over: {23: '结束'}
  - defer: '将' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 结束时， '结束' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24]

* W9. {26: '地球', 27: '从'}
  - carried_over: {25: '将'}
  - defer: '从' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [27]
  - release_units:
    1. 将地球, '将' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26]

* W10. {28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
  - carried_over: {27: '从'}
  - defer: None
  - release_units:
    1. 从黑暗势力的手中, '从' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28,29,30,31]

* W11. {32: '拯救', 33: '出来。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 拯救出来。 stable minimal sense unit in the current window: [32,33]
  result:
[
  [0,1],
  [2,3,4],
  [5,6,7,8],
  [9],
  [10,11,12,13,14,15,16],
  [17,18],
  [19,20,21,22],
  [23,24],
  [25,26],
  [27,28,29,30,31],
  [32,33]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '启示', 1: '录'} - output: release_units 1.{0: '启示', 1: '录'}
* W1. input: {2: '和', 3: '翡翠'} - output: release_units None
* W2. input: {4: '石板', 5: '都', 6: '曾经'} - output: release_units 1.{2: '和', 3: '翡翠', 4: '石板'}
* W3. input: {7: '预测', 8: '到，', 9: '这'} - output: release_units 1.{5: '都', 6: '曾经', 7: '预测', 8: '到，'}; 2.{9: '这'}
* W4. input: {10: '十四万', 11: '四千', 12: '名', 13: '光'} - output: release_units None
* W5. input: {14: '之', 15: '工作', 16: '者', 17: '的'} - output: release_units 1.{10: '十四万', 11: '四千', 12: '名', 13: '光', 14: '之', 15: '工作', 16: '者'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W6. input: {18: '到来，', 19: '会', 20: '在'} - output: release_units 1.{17: '的', 18: '到来，'}
* W7. input: {21: '卡利', 22: '年代', 23: '结束'} - output: release_units 1.{19: '会', 20: '在', 21: '卡利', 22: '年代'}
* W8. input: {24: '时，', 25: '将'} - output: release_units 1.{23: '结束', 24: '时，'}
* W9. input: {26: '地球', 27: '从'} - output: release_units 1.{25: '将', 26: '地球'}
* W10. input: {28: '黑暗', 29: '势力', 30: '的', 31: '手中'} - output: release_units 1.{27: '从', 28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
* W11. input: {32: '拯救', 33: '出来。'} - output: release_units 1.{32: '拯救', 33: '出来。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '启示', 1: '录'} - output: release_units 1.{0: '启示', 1: '录'}
* W1. input: {2: '和', 3: '翡翠'} - output: release_units None
* W2. input: {4: '石板', 5: '都', 6: '曾经'} - output: release_units 1.{2: '和', 3: '翡翠', 4: '石板'}
* W3. input: {7: '预测', 8: '到，', 9: '这'} - output: release_units 1.{5: '都', 6: '曾经', 7: '预测', 8: '到，'}
* W4. input: {10: '十四万', 11: '四千', 12: '名', 13: '光'} - output: release_units 1.{9: '这', 10: '十四万', 11: '四千', 12: '名'}
* W5. input: {14: '之', 15: '工作', 16: '者', 17: '的'} - output: release_units None
* W6. input: {18: '到来，', 19: '会', 20: '在'} - output: release_units 1.{13: '光', 14: '之', 15: '工作', 16: '者', 17: '的', 18: '到来，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {21: '卡利', 22: '年代', 23: '结束'} - output: release_units 1.{19: '会', 20: '在', 21: '卡利', 22: '年代'}
* W8. input: {24: '时，', 25: '将'} - output: release_units 1.{23: '结束', 24: '时，'}
* W9. input: {26: '地球', 27: '从'} - output: release_units None
* W10. input: {28: '黑暗', 29: '势力', 30: '的', 31: '手中'} - output: release_units 1.{25: '将', 26: '地球', 27: '从', 28: '黑暗', 29: '势力', 30: '的', 31: '手中'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {32: '拯救', 33: '出来。'} - output: release_units 1.{32: '拯救', 33: '出来。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '启示', 1: '录'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 启示录 is a stable proper name minimal sense unit: [0,1]

* W1. {2: '和', 3: '翡翠'}
  - carried_over: None
  - defer: '和翡翠' does not yet form a stable minimal sense unit; defer it to the next window because previous window had output: [2,3]
  - release_units: None

* W2. {4: '石板', 5: '都', 6: '曾经'}
  - carried_over: {2: '和', 3: '翡翠'}
  - defer: '都曾经' does not yet form a stable minimal sense unit; defer them to the next window because only the remainder is deferred after the current window has already emitted something: [5,6]
  - release_units:
    1. 和翡翠石板 is a stable noun phrase minimal sense unit (coordination of previous '启示录' with '翡翠石板'): [2,3,4]

* W3. {7: '预测', 8: '到，', 9: '这'}
  - carried_over: {5: '都', 6: '曾经'}
  - defer: '这' does not yet form a stable minimal sense unit as a standalone; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9]
  - release_units:
    1. 都曾经预测到， is a stable verb phrase minimal sense unit (adverb + verb + comma): [5,6,7,8]

* W4. {10: '十四万', 11: '四千', 12: '名', 13: '光'}
  - carried_over: {9: '这'}
  - defer: '这十四万四千名光' does not yet form a stable minimal sense unit; defer all to the next window because previous window had output and waiting is still legal: [9,10,11,12,13]
  - release_units: None

* W5. {14: '之', 15: '工作', 16: '者', 17: '的'}
  - carried_over: {9: '这', 10: '十四万', 11: '四千', 12: '名', 13: '光'}
  - defer: '光之工作者的' does not yet form a stable minimal sense unit as a standalone; defer them to the next window because only the remainder is deferred after the current window has already emitted something: [13,14,15,16,17]
  - release_units:
    1. 这十四万四千名 is a stable quantifier phrase minimal sense unit: [9,10,11,12]

* W6. {18: '到来，', 19: '会', 20: '在'}
  - carried_over: {13: '光', 14: '之', 15: '工作', 16: '者', 17: '的'}
  - defer: '会在' does not yet form a stable minimal sense unit; defer them to the next window because only the remainder is deferred after the current window has already emitted something: [19,20]
  - release_units:
    1. 光之工作者的到来， is a stable noun phrase minimal sense unit (including possessive and comma): [13,14,15,16,17,18]

* W7. {21: '卡利', 22: '年代', 23: '结束'}
  - carried_over: {19: '会', 20: '在'}
  - defer: '结束' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [23]
  - release_units:
    1. 会在卡利年代 is a stable prepositional phrase minimal sense unit (auxiliary + preposition + noun): [19,20,21,22]

* W8. {24: '时，', 25: '将'}
  - carried_over: {23: '结束'}
  - defer: '将' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 结束时， is a stable temporal clause ending minimal sense unit: [23,24]

* W9. {26: '地球', 27: '从'}
  - carried_over: {25: '将'}
  - defer: '将地球从' does not yet form a stable minimal sense unit; defer all to the next window because previous window had output and waiting is still legal: [25,26,27]
  - release_units: None

* W10. {28: '黑暗', 29: '势力', 30: '的', 31: '手中'}
  - carried_over: {25: '将', 26: '地球', 27: '从'}
  - defer: None
  - release_units:
    1. 将地球从黑暗势力的手中 is a stable prepositional phrase minimal sense unit (object + preposition + object of preposition), released now because previous window had no output: [25,26,27,28,29,30,31]

* W11. {32: '拯救', 33: '出来。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 拯救出来。 is a stable verb phrase minimal sense unit: [32,33]
  result:
[
  [0,1],
  [2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16,17,18],
  [19,20,21,22],
  [23,24],
  [25,26,27,28,29,30,31],
  [32,33]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '启示', 1: '录'} - output: release_units 1.{0: '启示', 1: '录'}
* W1. input: {2: '和', 3: '翡翠'} - output: release_units None
* W2. input: {4: '石板', 5: '都', 6: '曾经'} - output: release_units 1.{2: '和', 3: '翡翠', 4: '石板'}
* W3. input: {7: '预测', 8: '到，', 9: '这'} - output: release_units 1.{5: '都', 6: '曾经', 7: '预测', 8: '到，'}
* W4. input: {10: '十四万', 11: '四千', 12: '名', 13: '光'} - output: release_units 1.{9: '这', 10: '十四万', 11: '四千', 12: '名'}
* W5. input: {14: '之', 15: '工作', 16: '者', 17: '的'} - output: release_units None
* W6. input: {18: '到来，', 19: '会', 20: '在'} - output: release_units 1.{13: '光', 14: '之', 15: '工作', 16: '者', 17: '的', 18: '到来，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {21: '卡利', 22: '年代', 23: '结束'} - output: release_units 1.{19: '会', 20: '在', 21: '卡利', 22: '年代'}
* W8. input: {24: '时，', 25: '将'} - output: release_units 1.{23: '结束', 24: '时，'}
* W9. input: {26: '地球', 27: '从'} - output: release_units None
* W10. input: {28: '黑暗', 29: '势力', 30: '的', 31: '手中'} - output: release_units 1.{25: '将', 26: '地球', 27: '从', 28: '黑暗', 29: '势力', 30: '的', 31: '手中'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {32: '拯救', 33: '出来。'} - output: release_units 1.{32: '拯救', 33: '出来。'}

Reconfirm the RULEs and your task!


- retry: 2/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>启示录</src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>和翡翠石板</src>; start=2.00, end=3.00
* W3. <src>都曾经预测到，</src>; start=3.00, end=4.00
* W4. <src>这十四万四千名</src>; start=4.00, end=5.00
* W5. <src>光之工作者</src>; start=5.00, end=6.00
* W6. <src>的到来，</src>; start=6.00, end=7.00
* W7. <src>会在卡利年代</src>; start=7.00, end=8.00
* W8. <src>结束时，</src>; start=8.00, end=9.00
* W9. <src>将地球从</src>; start=9.00, end=10.00
* W10. <src>黑暗势力的手中</src>; start=10.00, end=11.00
* W11. <src>拯救出来。</src>; start=11.00, end=11.80
```

---
=== ZH_Y4xRc2amPxY_W000024 ===

status: finished

raw_text:
就会消耗我们身体骨骼当中的矿物质，更多的靠物矿物质。所以呢，这个肥胖人往往都会有这种关节和软组织的问题，就是因为什么？就是消耗了太多的矿物质。

word_indices:
* W0. {0: '就', 1: '会'}
* W1. {2: '消耗', 3: '我们'}
* W2. {4: '身体', 5: '骨骼'}
* W3. {6: '当中', 7: '的', 8: '矿'}
* W4. {9: '物质，', 10: '更多', 11: '的'}
* W5. {12: '靠物', 13: '矿', 14: '物质。'}
* W6. {}
* W7. {15: '所以', 16: '呢，', 17: '这', 18: '个'}
* W8. {19: '肥胖', 20: '人'}
* W9. {21: '往往', 22: '都会', 23: '有', 24: '这', 25: '种'}
* W10. {}
* W11. {26: '关节', 27: '和'}
* W12. {28: '软', 29: '组织', 30: '的'}
* W13. {31: '问题，', 32: '就是', 33: '因为'}
* W14. {34: '什么？', 35: '就是'}
* W15. {36: '消耗', 37: '了', 38: '太多'}
* W16. {39: '的', 40: '矿', 41: '物质。'}

scratchpad:
* W0. {0: '就', 1: '会'}
  - carried_over: None
  - defer: '就会' is not yet a stable release unit; defer to next window: [0,1]
  - release_units: None

* W1. {2: '消耗', 3: '我们'}
  - carried_over: {0: '就', 1: '会'}
  - defer: None
  - release_units:
    1. 就会消耗我们, latency-forced partial release because previous window had no output, so this window must release something; '就会消耗我们' is the smallest locally interpretable fragment: [0,1,2,3]

* W2. {4: '身体', 5: '骨骼'}
  - carried_over: None
  - defer: '身体骨骼' is not yet the best stable unit; defer to next window to combine with '当中': [4,5]
  - release_units: None

* W3. {6: '当中', 7: '的', 8: '矿'}
  - carried_over: {4: '身体', 5: '骨骼'}
  - defer: '的矿' are deferred to next window because only the remainder after releasing the locative phrase: [7,8]
  - release_units:
    1. 身体骨骼当中, latency-forced partial release; the previous window had no output, so this window must release something; '身体骨骼当中' is a minimal locative unit: [4,5,6]

* W4. {9: '物质，', 10: '更多', 11: '的'}
  - carried_over: {7: '的', 8: '矿'}
  - defer: '更多的' are deferred to next window because only the remainder after releasing the noun phrase: [10,11]
  - release_units:
    1. 的矿物质，, '的矿' carried over; released here as a minimal sense unit: [7,8,9]

* W5. {12: '靠物', 13: '矿', 14: '物质。'}
  - carried_over: {10: '更多', 11: '的'}
  - defer: None
  - release_units:
    1. 更多的靠物矿物质。, '更多的' carried over; released here as a minimal sense unit: [10,11,12,13,14]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {15: '所以', 16: '呢，', 17: '这', 18: '个'}
  - carried_over: None
  - defer: '这个' does not yet form a stable unit; defer to next window: [17,18]
  - release_units:
    1. 所以呢，, minimal sense unit (discourse marker): [15,16]

* W8. {19: '肥胖', 20: '人'}
  - carried_over: {17: '这', 18: '个'}
  - defer: None
  - release_units:
    1. 这个肥胖人, '这个' carried over; released here as a minimal sense unit: [17,18,19,20]

* W9. {21: '往往', 22: '都会', 23: '有', 24: '这', 25: '种'}
  - carried_over: None
  - defer: '这种' are deferred to next window because only the remainder after releasing the adverbial unit: [24,25]
  - release_units:
    1. 往往都会, latency-forced partial release; this window must release something to avoid two consecutive no-output windows (W10 is empty), and '往往都会' is a stable adverbial unit: [21,22,23]

* W10. {}
  - carried_over: {24: '这', 25: '种'}
  - defer: continue deferring across empty window: [24,25]
  - release_units: None

* W11. {26: '关节', 27: '和'}
  - carried_over: {24: '这', 25: '种'}
  - defer: '和' is deferred to next window because only the remainder after releasing the determiner-noun phrase: [27]
  - release_units:
    1. 这种关节, '这种' carried over; released here as a minimal sense unit: [24,25,26]

* W12. {28: '软', 29: '组织', 30: '的'}
  - carried_over: {27: '和'}
  - defer: '和软组织的' deferred to next window to combine with '问题，': [27,28,29,30]
  - release_units: None

* W13. {31: '问题，', 32: '就是', 33: '因为'}
  - carried_over: {27: '和', 28: '软', 29: '组织', 30: '的'}
  - defer: '就是因为' deferred to next window because only the remainder after releasing the noun phrase: [32,33]
  - release_units:
    1. 和软组织的问题，, '和软组织的' carried over; released here as a minimal sense unit: [27,28,29,30,31]

* W14. {34: '什么？', 35: '就是'}
  - carried_over: {32: '就是', 33: '因为'}
  - defer: '就是' deferred to next window because only the remainder after releasing the question: [35]
  - release_units:
    1. 就是因为什么？, '就是因为' carried over; released here as a minimal sense unit (question phrase): [32,33,34]

* W15. {36: '消耗', 37: '了', 38: '太多'}
  - carried_over: {35: '就是'}
  - defer: '就是消耗了太多' deferred to next window to combine with '的矿物质' to form a complete verb-object unit: [35,36,37,38]
  - release_units: None

* W16. {39: '的', 40: '矿', 41: '物质。'}
  - carried_over: {35: '就是', 36: '消耗', 37: '了', 38: '太多'}
  - defer: None
  - release_units:
    1. 就是消耗了太多的, latency-forced partial release; '就是消耗了太多的' is released as a predicate unit with the adjective phrase ending in '的', to avoid a single overly large chunk; the object follows: [35,36,37,38,39]
    2. 矿物质。, released as the object minimal sense unit: [40,41]

result:
[
  [0,1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12,13,14],
  [15,16],
  [17,18,19,20],
  [21,22,23],
  [24,25,26],
  [27,28,29,30,31],
  [32,33,34],
  [35,36,37,38,39],
  [40,41]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '就', 1: '会'} - output: release_units 1.{0: '就', 1: '会'}
* W1. input: {2: '消耗', 3: '我们'} - output: release_units None
* W2. input: {4: '身体', 5: '骨骼'} - output: release_units 1.{2: '消耗', 3: '我们', 4: '身体', 5: '骨骼'}
* W3. input: {6: '当中', 7: '的', 8: '矿'} - output: release_units None
* W4. input: {9: '物质，', 10: '更多', 11: '的'} - output: release_units 1.{6: '当中', 7: '的', 8: '矿', 9: '物质，'}
* W5. input: {12: '靠物', 13: '矿', 14: '物质。'} - output: release_units 1.{10: '更多', 11: '的', 12: '靠物', 13: '矿', 14: '物质。'}
* W6. input: {} - output: release_units None
* W7. input: {15: '所以', 16: '呢，', 17: '这', 18: '个'} - output: release_units 1.{15: '所以', 16: '呢，'}
* W8. input: {19: '肥胖', 20: '人'} - output: release_units 1.{17: '这', 18: '个', 19: '肥胖', 20: '人'}
* W9. input: {21: '往往', 22: '都会', 23: '有', 24: '这', 25: '种'} - output: release_units 1.{21: '往往', 22: '都会', 23: '有'}; 2.{24: '这', 25: '种'}
* W10. input: {} - output: release_units None
* W11. input: {26: '关节', 27: '和'} - output: release_units None
* W12. input: {28: '软', 29: '组织', 30: '的'} - output: release_units 1.{26: '关节', 27: '和', 28: '软', 29: '组织'}
* W13. input: {31: '问题，', 32: '就是', 33: '因为'} - output: release_units 1.{30: '的', 31: '问题，'}
* W14. input: {34: '什么？', 35: '就是'} - output: release_units 1.{32: '就是', 33: '因为', 34: '什么？'}; 2.{35: '就是'}
* W15. input: {36: '消耗', 37: '了', 38: '太多'} - output: release_units None
* W16. input: {39: '的', 40: '矿', 41: '物质。'} - output: release_units 1.{36: '消耗', 37: '了', 38: '太多', 39: '的', 40: '矿', 41: '物质。'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '就', 1: '会'}
  - carried_over: None
  - defer: '就会' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1]
  - release_units: None

* W1. {2: '消耗', 3: '我们'}
  - carried_over: {0: '就', 1: '会'}
  - defer: '消耗我们' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [2,3]
  - release_units:
    1. 就会, latency-forced partial release; waiting longer would violate output continuity, so only the smallest locally interpretable fragment is released now: [0,1]

* W2. {4: '身体', 5: '骨骼'}
  - carried_over: {2: '消耗', 3: '我们'}
  - defer: None
  - release_units:
    1. 消耗我们身体骨骼, '消耗我们' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4,5]

* W3. {6: '当中', 7: '的', 8: '矿'}
  - carried_over: None
  - defer: '当中的矿' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [6,7,8]
  - release_units: None

* W4. {9: '物质，', 10: '更多', 11: '的'}
  - carried_over: {6: '当中', 7: '的', 8: '矿'}
  - defer: '更多的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10,11]
  - release_units:
    1. 当中的矿物质， '当中的矿' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7,8,9]

* W5. {12: '靠物', 13: '矿', 14: '物质。'}
  - carried_over: {10: '更多', 11: '的'}
  - defer: None
  - release_units:
    1. 更多的靠物矿物质。 '更多的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12,13,14]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {15: '所以', 16: '呢，', 17: '这', 18: '个'}
  - carried_over: None
  - defer: '这个' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [17,18]
  - release_units:
    1. 所以呢， stable minimal sense unit in the current window: [15,16]

* W8. {19: '肥胖', 20: '人'}
  - carried_over: {17: '这', 18: '个'}
  - defer: None
  - release_units:
    1. 这个肥胖人, '这个' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19,20]

* W9. {21: '往往', 22: '都会', 23: '有', 24: '这', 25: '种'}
  - carried_over: None
  - defer: '这种' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [24,25]
  - release_units:
    1. 往往都会有, stable minimal sense unit in the current window: [21,22,23]

* W10. {}
  - carried_over: {24: '这', 25: '种'}
  - defer: '这种' still does not yet form the best stable release unit / minimal sense unit here; continue deferring it across the empty window because no new material arrives in the current window: [24,25]
  - release_units: None

* W11. {26: '关节', 27: '和'}
  - carried_over: {24: '这', 25: '种'}
  - defer: '关节和' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [26,27]
  - release_units:
    1. 这种, '这种' is carried over from the previous window; released here under window pressure because the previous window had no output, so the current window must flush something now; this is the smallest locally interpretable unit available at this point: [24,25]

* W12. {28: '软', 29: '组织', 30: '的'}
  - carried_over: {26: '关节', 27: '和'}
  - defer: '的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [30]
  - release_units:
    1. 关节和软组织, '关节和' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27,28,29]

* W13. {31: '问题，', 32: '就是', 33: '因为'}
  - carried_over: {30: '的'}
  - defer: '就是因为' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [32,33]
  - release_units:
    1. 的问题， '的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31]

* W14. {34: '什么？', 35: '就是'}
  - carried_over: {32: '就是', 33: '因为'}
  - defer: None
  - release_units:
    1. 就是因为什么？ '就是因为' is carried over from the previous window; released here because it is now a stable minimal sense unit: [32,33,34]
    2. 就是, stable minimal sense unit in the current window: [35]

* W15. {36: '消耗', 37: '了', 38: '太多'}
  - carried_over: None
  - defer: '太多了' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [36,37,38]
  - release_units: None

* W16. {39: '的', 40: '矿', 41: '物质。'}
  - carried_over: {36: '消耗', 37: '了', 38: '太多'}
  - defer: None
  - release_units:
    1. 消耗了太多的矿物质。 '消耗了太多' is carried over from the previous window; released here because it is now a stable minimal sense unit: [36,37,38,39,40,41]
  result:
[
  [0,1],
  [2,3,4,5],
  [6,7,8,9],
  [10,11,12,13,14],
  [15,16],
  [17,18,19,20],
  [21,22,23],
  [24,25],
  [26,27,28,29],
  [30,31],
  [32,33,34],
  [35],
  [36,37,38,39,40,41]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '就', 1: '会'} - output: release_units 1.{0: '就', 1: '会'}
* W1. input: {2: '消耗', 3: '我们'} - output: release_units None
* W2. input: {4: '身体', 5: '骨骼'} - output: release_units 1.{2: '消耗', 3: '我们', 4: '身体', 5: '骨骼'}
* W3. input: {6: '当中', 7: '的', 8: '矿'} - output: release_units None
* W4. input: {9: '物质，', 10: '更多', 11: '的'} - output: release_units 1.{6: '当中', 7: '的', 8: '矿', 9: '物质，'}
* W5. input: {12: '靠物', 13: '矿', 14: '物质。'} - output: release_units 1.{10: '更多', 11: '的', 12: '靠物', 13: '矿', 14: '物质。'}
* W6. input: {} - output: release_units None
* W7. input: {15: '所以', 16: '呢，', 17: '这', 18: '个'} - output: release_units 1.{15: '所以', 16: '呢，'}
* W8. input: {19: '肥胖', 20: '人'} - output: release_units 1.{17: '这', 18: '个', 19: '肥胖', 20: '人'}
* W9. input: {21: '往往', 22: '都会', 23: '有', 24: '这', 25: '种'} - output: release_units 1.{21: '往往', 22: '都会', 23: '有'}; 2.{24: '这', 25: '种'}
* W10. input: {} - output: release_units None
* W11. input: {26: '关节', 27: '和'} - output: release_units None
* W12. input: {28: '软', 29: '组织', 30: '的'} - output: release_units 1.{26: '关节', 27: '和', 28: '软', 29: '组织'}
* W13. input: {31: '问题，', 32: '就是', 33: '因为'} - output: release_units 1.{30: '的', 31: '问题，'}
* W14. input: {34: '什么？', 35: '就是'} - output: release_units 1.{32: '就是', 33: '因为', 34: '什么？'}; 2.{35: '就是'}
* W15. input: {36: '消耗', 37: '了', 38: '太多'} - output: release_units None
* W16. input: {39: '的', 40: '矿', 41: '物质。'} - output: release_units 1.{36: '消耗', 37: '了', 38: '太多', 39: '的', 40: '矿', 41: '物质。'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src><|wait|></src>; start=0.00, end=1.00
* W1. <src>就会消耗我们</src>; start=1.00, end=2.00
* W2. <src><|wait|></src>; start=2.00, end=3.00
* W3. <src>身体骨骼当中</src>; start=3.00, end=4.00
* W4. <src>的矿物质，</src>; start=4.00, end=5.00
* W5. <src>更多的靠物矿物质。</src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>所以呢，</src>; start=7.00, end=8.00
* W8. <src>这个肥胖人</src>; start=8.00, end=9.00
* W9. <src>往往都会有</src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=11.00
* W11. <src>这种关节</src>; start=11.00, end=12.00
* W12. <src><|wait|></src>; start=12.00, end=13.00
* W13. <src>和软组织的问题，</src>; start=13.00, end=14.00
* W14. <src>就是因为什么？</src>; start=14.00, end=15.00
* W15. <src><|wait|></src>; start=15.00, end=16.00
* W16. <src>就是消耗了太多的矿物质。</src>; start=16.00, end=16.84
```

---
=== ZH_Yu84L6YIP6A_W000010 ===

status: finished

raw_text:
说，我当时我只是看到月轮，我就跟师傅熊老师嘛，是我的师傅，我就汇报。二师傅，我成了。他说你成了什么了？我说我看到一个大月亮了，亮亮的，你看啊，一堂光。他说你成了个屁，哈哈哈哈哈！他就跟我说话不客气啊，你那个叫成了。

word_indices:
* W0. {0: '说，', 1: '我', 2: '当时', 3: '我'}
* W1. {4: '只', 5: '是', 6: '看到'}
* W2. {7: '月轮，', 8: '我', 9: '就', 10: '跟'}
* W3. {11: '师傅', 12: '熊'}
* W4. {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'}
* W5. {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'}
* W6. {23: '师傅，', 24: '我'}
* W7. {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
* W8. {32: '什么', 33: '了？', 34: '我'}
* W9. {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'}
* W10. {40: '大', 41: '月', 42: '亮', 43: '了，'}
* W11. {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'}
* W12. {49: '啊，', 50: '一'}
* W13. {51: '堂', 52: '光。', 53: '他', 54: '说'}
* W14. {55: '你', 56: '成', 57: '了', 58: '个'}
* W15. {59: '屁，'}
* W16. {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'}
* W17. {65: '说话', 66: '不', 67: '客气'}
* W18. {68: '啊，', 69: '你'}
* W19. {70: '那', 71: '个', 72: '叫成', 73: '了。'}

scratchpad:
* W0. {0: '说，', 1: '我', 2: '当时', 3: '我'}
  - carried_over: None
  - defer: '我 当时 我' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [1,2,3]
  - release_units:
    1. 说， stable minimal sense unit in the current window: [0]

* W1. {4: '只', 5: '是', 6: '看到'}
  - carried_over: {1: '我', 2: '当时', 3: '我'}
  - defer: all current tokens and carried over do not yet form a stable minimal sense unit; defer to next window: [1,2,3,4,5,6]
  - release_units: None

* W2. {7: '月轮，', 8: '我', 9: '就', 10: '跟'}
  - carried_over: {1: '我', 2: '当时', 3: '我', 4: '只', 5: '是', 6: '看到'}
  - defer: '月轮，我就跟' does not yet form a stable minimal sense unit; defer to next window: [7,8,9,10]
  - release_units:
    1. 我当时, '我 当时' is carried over from previous windows; released here as a minimal sense unit: [1,2]
    2. 我只是看到, '我 只 是 看到' is carried over; released here as a minimal sense unit: [3,4,5,6]

* W3. {11: '师傅', 12: '熊'}
  - carried_over: {7: '月轮，', 8: '我', 9: '就', 10: '跟'}
  - defer: '熊' does not yet form a stable minimal sense unit; defer to next window: [12]
  - release_units:
    1. 月轮， stable minimal sense unit in the current window: [7]
    2. 我就跟师傅, '我 就 跟' is carried over; released here as a minimal sense unit: [8,9,10,11]

* W4. {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'}
  - carried_over: {12: '熊'}
  - defer: None
  - release_units:
    1. 熊老师嘛， '熊' is carried over; released here as a minimal sense unit: [12,13,14]
    2. 是我的, stable minimal sense unit in the current window: [15,16,17]

* W5. {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'}
  - carried_over: None
  - defer: '二' does not yet form a stable minimal sense unit; defer to next window: [22]
  - release_units:
    1. 师傅，我就汇报。 stable minimal sense unit in the current window: [18,19,20,21]

* W6. {23: '师傅，', 24: '我'}
  - carried_over: {22: '二'}
  - defer: '我' does not yet form a stable minimal sense unit; defer to next window: [24]
  - release_units:
    1. 二师傅， '二' is carried over; released here as a minimal sense unit: [22,23]

* W7. {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
  - carried_over: {24: '我'}
  - defer: None
  - release_units:
    1. 我成了。 '我' is carried over; released here as a minimal sense unit: [24,25,26]
    2. 他说你成了, stable minimal sense unit in the current window: [27,28,29,30,31]

* W8. {32: '什么', 33: '了？', 34: '我'}
  - carried_over: None
  - defer: '我' does not yet form a stable minimal sense unit; defer to next window: [34]
  - release_units:
    1. 什么了？ stable minimal sense unit in the current window: [32,33]

* W9. {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'}
  - carried_over: {34: '我'}
  - defer: None
  - release_units:
    1. 我说我看到, '我' is carried over; released here as a minimal sense unit: [34,35,36,37]
    2. 一个, stable minimal sense unit in the current window: [38,39]

* W10. {40: '大', 41: '月', 42: '亮', 43: '了，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 大月亮了， stable minimal sense unit in the current window: [40,41,42,43]

* W11. {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 亮亮的，你看 stable minimal sense unit in the current window: [44,45,46,47,48]

* W12. {49: '啊，', 50: '一'}
  - carried_over: None
  - defer: '一' does not yet form a stable minimal sense unit; defer to next window: [50]
  - release_units:
    1. 啊， stable minimal sense unit in the current window: [49]

* W13. {51: '堂', 52: '光。', 53: '他', 54: '说'}
  - carried_over: {50: '一'}
  - defer: None
  - release_units:
    1. 一堂光。他说 '一' is carried over; released here as a minimal sense unit: [50,51,52,53,54]

* W14. {55: '你', 56: '成', 57: '了', 58: '个'}
  - carried_over: None
  - defer: '你成了个' does not yet form a stable minimal sense unit; defer to next window: [55,56,57,58]
  - release_units: None

* W15. {59: '屁，'}
  - carried_over: {55: '你', 56: '成', 57: '了', 58: '个'}
  - defer: None
  - release_units:
    1. 你成了个屁， '你成了个' is carried over; released here as a minimal sense unit: [55,56,57,58,59]

* W16. {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 哈哈哈哈哈！ stable minimal sense unit in the current window: [60]
    2. 他就跟我 stable minimal sense unit in the current window: [61,62,63,64]

* W17. {65: '说话', 66: '不', 67: '客气'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 说话不客气 stable minimal sense unit in the current window: [65,66,67]

* W18. {68: '啊，', 69: '你'}
  - carried_over: None
  - defer: '你' does not yet form a stable minimal sense unit; defer to next window: [69]
  - release_units:
    1. 啊， stable minimal sense unit in the current window: [68]

* W19. {70: '那', 71: '个', 72: '叫成', 73: '了。'}
  - carried_over: {69: '你'}
  - defer: None
  - release_units:
    1. 你那个叫成了。 '你' is carried over; released here as a minimal sense unit: [69,70,71,72,73]

result:
[
  [0],
  [1,2],
  [3,4,5,6],
  [7],
  [8,9,10,11],
  [12,13,14],
  [15,16,17],
  [18,19,20,21],
  [22,23],
  [24,25,26],
  [27,28,29,30,31],
  [32,33],
  [34,35,36,37],
  [38,39],
  [40,41,42,43],
  [44,45,46,47,48],
  [49],
  [50,51,52,53,54],
  [55,56,57,58,59],
  [60],
  [61,62,63,64],
  [65,66,67],
  [68],
  [69,70,71,72,73]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '说，', 1: '我', 2: '当时', 3: '我'} - output: release_units 1.{0: '说，', 1: '我', 2: '当时'}
* W1. input: {4: '只', 5: '是', 6: '看到'} - output: release_units None
* W2. input: {7: '月轮，', 8: '我', 9: '就', 10: '跟'} - output: release_units 1.{3: '我', 4: '只', 5: '是', 6: '看到', 7: '月轮，'}
* W3. input: {11: '师傅', 12: '熊'} - output: release_units None
* W4. input: {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'} - output: release_units 1.{8: '我', 9: '就', 10: '跟', 11: '师傅', 12: '熊', 13: '老师', 14: '嘛，'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'} - output: release_units 1.{15: '是', 16: '我', 17: '的', 18: '师傅，'}; 2.{19: '我', 20: '就', 21: '汇报。'}
* W6. input: {23: '师傅，', 24: '我'} - output: release_units 1.{22: '二', 23: '师傅，'}
* W7. input: {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'} - output: release_units 1.{24: '我', 25: '成', 26: '了。'}; 2.{27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
* W8. input: {32: '什么', 33: '了？', 34: '我'} - output: release_units 1.{32: '什么', 33: '了？'}
* W9. input: {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'} - output: release_units 1.{34: '我', 35: '说', 36: '我', 37: '看到'}
* W10. input: {40: '大', 41: '月', 42: '亮', 43: '了，'} - output: release_units 1.{38: '一', 39: '个', 40: '大', 41: '月', 42: '亮', 43: '了，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'} - output: release_units 1.{44: '亮', 45: '亮', 46: '的，'}; 2.{47: '你', 48: '看'}
* W12. input: {49: '啊，', 50: '一'} - output: release_units 1.{49: '啊，'}
* W13. input: {51: '堂', 52: '光。', 53: '他', 54: '说'} - output: release_units 1.{50: '一', 51: '堂', 52: '光。'}; 2.{53: '他', 54: '说'}
* W14. input: {55: '你', 56: '成', 57: '了', 58: '个'} - output: release_units None
* W15. input: {59: '屁，'} - output: release_units 1.{55: '你', 56: '成', 57: '了', 58: '个', 59: '屁，'}
* W16. input: {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'} - output: release_units 1.{60: '哈哈哈哈哈！'}
* W17. input: {65: '说话', 66: '不', 67: '客气'} - output: release_units 1.{61: '他', 62: '就', 63: '跟', 64: '我', 65: '说话', 66: '不', 67: '客气'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W18. input: {68: '啊，', 69: '你'} - output: release_units 1.{68: '啊，'}
* W19. input: {70: '那', 71: '个', 72: '叫成', 73: '了。'} - output: release_units 1.{69: '你', 70: '那', 71: '个', 72: '叫成', 73: '了。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '说，', 1: '我', 2: '当时', 3: '我'}
  - carried_over: None
  - defer: '说，我当时我' does not yet form a stable minimal sense unit; defer it to the next window: [0,1,2,3]
  - release_units: None

* W1. {4: '只', 5: '是', 6: '看到'}
  - carried_over: {0: '说，', 1: '我', 2: '当时', 3: '我'}
  - defer: '我只是看到' does not yet form a stable minimal sense unit; defer it to the next window: [3,4,5,6]
  - release_units:
    1. 说，我当时, '说，我当时' is carried over from the previous window; released here because it is now a stable minimal sense unit (discourse opening with temporal frame): [0,1,2]

* W2. {7: '月轮，', 8: '我', 9: '就', 10: '跟'}
  - carried_over: {3: '我', 4: '只', 5: '是', 6: '看到'}
  - defer: '我就跟' does not yet form a stable minimal sense unit; defer it to the next window: [8,9,10]
  - release_units:
    1. 我只是看到月轮， '我只是看到' is carried over from the previous window; released here because it is now a stable minimal sense unit (verb-object phrase): [3,4,5,6,7]

* W3. {11: '师傅', 12: '熊'}
  - carried_over: {8: '我', 9: '就', 10: '跟'}
  - defer: '我就跟师傅熊' does not yet form a stable minimal sense unit; defer it to the next window to keep the name together: [8,9,10,11,12]
  - release_units: None

* W4. {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'}
  - carried_over: {8: '我', 9: '就', 10: '跟', 11: '师傅', 12: '熊'}
  - defer: '是我的' does not yet form a stable minimal sense unit; defer it to the next window: [15,16,17]
  - release_units:
    1. 我就跟师傅熊老师嘛， '我就跟师傅熊' is carried over from the previous window; released here because it is now a stable minimal sense unit (verb-object with address): [8,9,10,11,12,13,14]

* W5. {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'}
  - carried_over: {15: '是', 16: '我', 17: '的'}
  - defer: '二' does not yet form a stable minimal sense unit; defer it to the next window: [22]
  - release_units:
    1. 是我的师傅， '是我的' is carried over from the previous window; released here because it is now a stable minimal sense unit (possessive phrase): [15,16,17,18]
    2. 我就汇报。 stable minimal sense unit in the current window: [19,20,21]

* W6. {23: '师傅，', 24: '我'}
  - carried_over: {22: '二'}
  - defer: '我' does not yet form a stable minimal sense unit; defer it to the next window: [24]
  - release_units:
    1. 二师傅， '二' is carried over from the previous window; released here because it is now a stable minimal sense unit (vocative): [22,23]

* W7. {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
  - carried_over: {24: '我'}
  - defer: None
  - release_units:
    1. 我成了。 '我' is carried over from the previous window; released here because it is now a stable minimal sense unit (clause): [24,25,26]
    2. 他说你成了, stable minimal sense unit in the current window (reporting clause): [27,28,29,30,31]

* W8. {32: '什么', 33: '了？', 34: '我'}
  - carried_over: None
  - defer: '我' does not yet form a stable minimal sense unit; defer it to the next window: [34]
  - release_units:
    1. 什么了？ stable minimal sense unit in the current window (question): [32,33]

* W9. {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'}
  - carried_over: {34: '我'}
  - defer: '一个' does not yet form a stable minimal sense unit; defer it to the next window: [38,39]
  - release_units:
    1. 我说我看到, '我' is carried over from the previous window; released here because it is now a stable minimal sense unit (verb phrase): [34,35,36,37]

* W10. {40: '大', 41: '月', 42: '亮', 43: '了，'}
  - carried_over: {38: '一', 39: '个'}
  - defer: None
  - release_units:
    1. 一个大月亮了， '一个' is carried over from the previous window; released here because it is now a stable minimal sense unit (noun phrase): [38,39,40,41,42,43]

* W11. {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 亮亮的， stable minimal sense unit in the current window (adjective phrase): [44,45,46]
    2. 你看, stable minimal sense unit in the current window (imperative): [47,48]

* W12. {49: '啊，', 50: '一'}
  - carried_over: None
  - defer: '一' does not yet form a stable minimal sense unit; defer it to the next window: [50]
  - release_units:
    1. 啊， stable minimal sense unit in the current window (discourse particle): [49]

* W13. {51: '堂', 52: '光。', 53: '他', 54: '说'}
  - carried_over: {50: '一'}
  - defer: None
  - release_units:
    1. 一堂光。 '一' is carried over from the previous window; released here because it is now a stable minimal sense unit (noun phrase): [50,51,52]
    2. 他说, stable minimal sense unit in the current window (reporting verb): [53,54]

* W14. {55: '你', 56: '成', 57: '了', 58: '个'}
  - carried_over: None
  - defer: '你成了个' does not yet form a stable minimal sense unit; defer it to the next window: [55,56,57,58]
  - release_units: None

* W15. {59: '屁，'}
  - carried_over: {55: '你', 56: '成', 57: '了', 58: '个'}
  - defer: None
  - release_units:
    1. 你成了个屁， '你成了个' is carried over from the previous window; released here because it is now a stable minimal sense unit (complete predicate): [55,56,57,58,59]

* W16. {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'}
  - carried_over: None
  - defer: '他就跟我' does not yet form a stable minimal sense unit; defer it to the next window: [61,62,63,64]
  - release_units:
    1. 哈哈哈哈哈！ stable minimal sense unit in the current window (laughter): [60]

* W17. {65: '说话', 66: '不', 67: '客气'}
  - carried_over: {61: '他', 62: '就', 63: '跟', 64: '我'}
  - defer: None
  - release_units:
    1. 他就跟我说话不客气, '他就跟我' is carried over from the previous window; released here because it is now a stable minimal sense unit (clause): [61,62,63,64,65,66,67]

* W18. {68: '啊，', 69: '你'}
  - carried_over: None
  - defer: '你' does not yet form a stable minimal sense unit; defer it to the next window: [69]
  - release_units:
    1. 啊， stable minimal sense unit in the current window (discourse particle): [68]

* W19. {70: '那', 71: '个', 72: '叫成', 73: '了。'}
  - carried_over: {69: '你'}
  - defer: None
  - release_units:
    1. 你那个叫成了。 '你' is carried over from the previous window; released here because it is now a stable minimal sense unit (sentence): [69,70,71,72,73]
  result:
[
  [0,1,2],
  [3,4,5,6,7],
  [8,9,10,11,12,13,14],
  [15,16,17,18],
  [19,20,21],
  [22,23],
  [24,25,26],
  [27,28,29,30,31],
  [32,33],
  [34,35,36,37],
  [38,39,40,41,42,43],
  [44,45,46],
  [47,48],
  [49],
  [50,51,52],
  [53,54],
  [55,56,57,58,59],
  [60],
  [61,62,63,64,65,66,67],
  [68],
  [69,70,71,72,73]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '说，', 1: '我', 2: '当时', 3: '我'} - output: release_units 1.{0: '说，', 1: '我', 2: '当时'}
* W1. input: {4: '只', 5: '是', 6: '看到'} - output: release_units None
* W2. input: {7: '月轮，', 8: '我', 9: '就', 10: '跟'} - output: release_units 1.{3: '我', 4: '只', 5: '是', 6: '看到', 7: '月轮，'}
* W3. input: {11: '师傅', 12: '熊'} - output: release_units None
* W4. input: {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'} - output: release_units 1.{8: '我', 9: '就', 10: '跟', 11: '师傅', 12: '熊', 13: '老师', 14: '嘛，'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'} - output: release_units 1.{15: '是', 16: '我', 17: '的', 18: '师傅，'}; 2.{19: '我', 20: '就', 21: '汇报。'}
* W6. input: {23: '师傅，', 24: '我'} - output: release_units 1.{22: '二', 23: '师傅，'}
* W7. input: {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'} - output: release_units 1.{24: '我', 25: '成', 26: '了。'}; 2.{27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
* W8. input: {32: '什么', 33: '了？', 34: '我'} - output: release_units 1.{32: '什么', 33: '了？'}
* W9. input: {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'} - output: release_units 1.{34: '我', 35: '说', 36: '我', 37: '看到'}
* W10. input: {40: '大', 41: '月', 42: '亮', 43: '了，'} - output: release_units 1.{38: '一', 39: '个', 40: '大', 41: '月', 42: '亮', 43: '了，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'} - output: release_units 1.{44: '亮', 45: '亮', 46: '的，'}; 2.{47: '你', 48: '看'}
* W12. input: {49: '啊，', 50: '一'} - output: release_units 1.{49: '啊，'}
* W13. input: {51: '堂', 52: '光。', 53: '他', 54: '说'} - output: release_units 1.{50: '一', 51: '堂', 52: '光。'}; 2.{53: '他', 54: '说'}
* W14. input: {55: '你', 56: '成', 57: '了', 58: '个'} - output: release_units None
* W15. input: {59: '屁，'} - output: release_units 1.{55: '你', 56: '成', 57: '了', 58: '个', 59: '屁，'}
* W16. input: {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'} - output: release_units 1.{60: '哈哈哈哈哈！'}
* W17. input: {65: '说话', 66: '不', 67: '客气'} - output: release_units 1.{61: '他', 62: '就', 63: '跟', 64: '我', 65: '说话', 66: '不', 67: '客气'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W18. input: {68: '啊，', 69: '你'} - output: release_units 1.{68: '啊，'}
* W19. input: {70: '那', 71: '个', 72: '叫成', 73: '了。'} - output: release_units 1.{69: '你', 70: '那', 71: '个', 72: '叫成', 73: '了。'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '说，', 1: '我', 2: '当时', 3: '我'} - output: release_units None
* W1. input: {4: '只', 5: '是', 6: '看到'} - output: release_units None <- ISSUE1: consecutive non-empty wait x2, delay too long.
* W2. input: {7: '月轮，', 8: '我', 9: '就', 10: '跟'} - output: release_units 1.{0: '说，', 1: '我', 2: '当时', 3: '我', 4: '只', 5: '是', 6: '看到', 7: '月轮，'}; 2.{8: '我', 9: '就'} <- ISSUE2: oversized chunk release unit 1 size=8 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {11: '师傅', 12: '熊'} - output: release_units None
* W4. input: {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'} - output: release_units 1.{10: '跟', 11: '师傅', 12: '熊', 13: '老师', 14: '嘛，'}
* W5. input: {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'} - output: release_units 1.{15: '是', 16: '我', 17: '的', 18: '师傅，'}; 2.{19: '我', 20: '就', 21: '汇报。'}
* W6. input: {23: '师傅，', 24: '我'} - output: release_units 1.{22: '二', 23: '师傅，'}
* W7. input: {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'} - output: release_units 1.{24: '我', 25: '成', 26: '了。'}
* W8. input: {32: '什么', 33: '了？', 34: '我'} - output: release_units 1.{27: '他', 28: '说', 29: '你', 30: '成', 31: '了', 32: '什么', 33: '了？'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W9. input: {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'} - output: release_units 1.{34: '我', 35: '说', 36: '我', 37: '看到'}
* W10. input: {40: '大', 41: '月', 42: '亮', 43: '了，'} - output: release_units 1.{38: '一', 39: '个', 40: '大', 41: '月', 42: '亮', 43: '了，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'} - output: release_units 1.{44: '亮', 45: '亮', 46: '的，'}
* W12. input: {49: '啊，', 50: '一'} - output: release_units 1.{47: '你', 48: '看', 49: '啊，'}
* W13. input: {51: '堂', 52: '光。', 53: '他', 54: '说'} - output: release_units 1.{50: '一', 51: '堂', 52: '光。'}; 2.{53: '他', 54: '说'}
* W14. input: {55: '你', 56: '成', 57: '了', 58: '个'} - output: release_units None
* W15. input: {59: '屁，'} - output: release_units 1.{55: '你', 56: '成', 57: '了', 58: '个', 59: '屁，'}
* W16. input: {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'} - output: release_units 1.{60: '哈哈哈哈哈！'}
* W17. input: {65: '说话', 66: '不', 67: '客气'} - output: release_units 1.{61: '他', 62: '就', 63: '跟', 64: '我', 65: '说话', 66: '不', 67: '客气'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W18. input: {68: '啊，', 69: '你'} - output: release_units 1.{68: '啊，'}
* W19. input: {70: '那', 71: '个', 72: '叫成', 73: '了。'} - output: release_units 1.{69: '你', 70: '那', 71: '个', 72: '叫成', 73: '了。'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '说，', 1: '我', 2: '当时', 3: '我'}
  - carried_over: None
  - defer: '我当时我' is not yet a stable minimal sense unit; defer it to the next window: [0,1,2,3]
  - release_units: None

* W1. {4: '只', 5: '是', 6: '看到'}
  - carried_over: {0: '说，', 1: '我', 2: '当时', 3: '我'}
  - defer: '只是看到' does not yet form a stable minimal sense unit with the carried-over material; defer it to the next window: [4,5,6]
  - release_units: None

* W2. {7: '月轮，', 8: '我', 9: '就', 10: '跟'}
  - carried_over: {0: '说，', 1: '我', 2: '当时', 3: '我', 4: '只', 5: '是', 6: '看到'}
  - defer: '我就跟' is not yet a stable minimal sense unit; defer it to the next window: [8,9,10]
  - release_units:
    1. 说，我当时我只是看到月轮， '说，我当时我' is carried over; '只是看到' is carried over; now forms a stable minimal sense unit: [0,1,2,3,4,5,6,7]

* W3. {11: '师傅', 12: '熊'}
  - carried_over: {8: '我', 9: '就', 10: '跟'}
  - defer: '跟师傅熊' is not yet a stable minimal sense unit; defer it to the next window: [10,11,12]
  - release_units:
    1. 我就, '我就' is carried over; released here as a stable minimal sense unit: [8,9]

* W4. {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'}
  - carried_over: {10: '跟', 11: '师傅', 12: '熊'}
  - defer: '是我的' is not yet a stable minimal sense unit; defer it to the next window: [15,16,17]
  - release_units:
    1. 跟师傅熊老师嘛， '跟师傅熊' is carried over; now forms a stable minimal sense unit: [10,11,12,13,14]

* W5. {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'}
  - carried_over: {15: '是', 16: '我', 17: '的'}
  - defer: '二' is not yet a stable minimal sense unit; defer it to the next window: [22]
  - release_units:
    1. 是我的师傅， '是我的' is carried over; now forms a stable minimal sense unit: [15,16,17,18]
    2. 我就汇报。 stable minimal sense unit: [19,20,21]

* W6. {23: '师傅，', 24: '我'}
  - carried_over: {22: '二'}
  - defer: '我' is not yet a stable minimal sense unit; defer it to the next window: [24]
  - release_units:
    1. 二师傅， '二' is carried over; now forms a stable minimal sense unit: [22,23]

* W7. {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
  - carried_over: {24: '我'}
  - defer: '他说你成了' is not yet a stable minimal sense unit; defer it to the next window: [27,28,29,30,31]
  - release_units:
    1. 我成了。 '我' is carried over; now forms a stable minimal sense unit: [24,25,26]

* W8. {32: '什么', 33: '了？', 34: '我'}
  - carried_over: {27: '他', 28: '说', 29: '你', 30: '成', 31: '了'}
  - defer: '我' is deferred to the next window: [34]
  - release_units:
    1. 他说你成了什么了？ '他说的你成了' is carried over; now forms a stable minimal sense unit: [27,28,29,30,31,32,33]

* W9. {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'}
  - carried_over: {34: '我'}
  - defer: '一个个' is not yet a stable minimal sense unit; defer it to the next window: [38,39]
  - release_units:
    1. 我说我看到, '我' is carried over; now forms a stable minimal sense unit: [34,35,36,37]

* W10. {40: '大', 41: '月', 42: '亮', 43: '了，'}
  - carried_over: {38: '一', 39: '个'}
  - defer: None
  - release_units:
    1. 一个大月亮了， '一个个' is carried over; now forms a stable minimal sense unit: [38,39,40,41,42,43]

* W11. {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'}
  - carried_over: None
  - defer: '你看' is not yet a stable minimal sense unit; defer it to the next window: [47,48]
  - release_units:
    1. 亮亮的， stable minimal sense unit: [44,45,46]

* W12. {49: '啊，', 50: '一'}
  - carried_over: {47: '你', 48: '看'}
  - defer: '一' is not yet a stable minimal sense unit; defer it to the next window: [50]
  - release_units:
    1. 你看啊， '你看' is carried over; now forms a stable minimal sense unit: [47,48,49]

* W13. {51: '堂', 52: '光。', 53: '他', 54: '说'}
  - carried_over: {50: '一'}
  - defer: '他说' is not yet a stable minimal sense unit; defer it to the next window: [53,54]
  - release_units:
    1. 一堂光。 '一' is carried over; now forms a stable minimal sense unit: [50,51,52]

* W14. {55: '你', 56: '成', 57: '了', 58: '个'}
  - carried_over: {53: '他', 54: '说'}
  - defer: '你成了个' is not yet a stable minimal sense unit; defer it to the next window: [55,56,57,58]
  - release_units:
    1. 他说, '他说' is carried over; now forms a stable minimal sense unit: [53,54]

* W15. {59: '屁，'}
  - carried_over: {55: '你', 56: '成', 57: '了', 58: '个'}
  - defer: None
  - release_units:
    1. 你成了个屁， '你成了个' is carried over; now forms a stable minimal sense unit: [55,56,57,58,59]

* W16. {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'}
  - carried_over: None
  - defer: '他就跟我' is not yet a stable minimal sense unit; defer it to the next window: [61,62,63,64]
  - release_units:
    1. 哈哈哈哈哈！ stable minimal sense unit: [60]

* W17. {65: '说话', 66: '不', 67: '客气'}
  - carried_over: {61: '他', 62: '就', 63: '跟', 64: '我'}
  - defer: None
  - release_units:
    1. 他就跟我说话不客气, '他就跟我' is carried over; now forms a stable minimal sense unit: [61,62,63,64,65,66,67]

* W18. {68: '啊，', 69: '你'}
  - carried_over: None
  - defer: '你' is deferred to the next window: [69]
  - release_units:
    1. 啊， stable minimal sense unit: [68]

* W19. {70: '那', 71: '个', 72: '叫成', 73: '了。'}
  - carried_over: {69: '你'}
  - defer: None
  - release_units:
    1. 你那个叫成了。 '你' is carried over; now forms a stable minimal sense unit: [69,70,71,72,73]
  result:
[
  [0,1,2,3,4,5,6,7],
  [8,9],
  [10,11,12,13,14],
  [15,16,17,18],
  [19,20,21],
  [22,23],
  [24,25,26],
  [27,28,29,30,31,32,33],
  [34,35,36,37],
  [38,39,40,41,42,43],
  [44,45,46],
  [47,48,49],
  [50,51,52],
  [53,54],
  [55,56,57,58,59],
  [60],
  [61,62,63,64,65,66,67],
  [68],
  [69,70,71,72,73]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '说，', 1: '我', 2: '当时', 3: '我'} - output: release_units None
* W1. input: {4: '只', 5: '是', 6: '看到'} - output: release_units None <- ISSUE1: consecutive non-empty wait x2, delay too long.
* W2. input: {7: '月轮，', 8: '我', 9: '就', 10: '跟'} - output: release_units 1.{0: '说，', 1: '我', 2: '当时', 3: '我', 4: '只', 5: '是', 6: '看到', 7: '月轮，'}; 2.{8: '我', 9: '就'} <- ISSUE2: oversized chunk release unit 1 size=8 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W3. input: {11: '师傅', 12: '熊'} - output: release_units None
* W4. input: {13: '老师', 14: '嘛，', 15: '是', 16: '我', 17: '的'} - output: release_units 1.{10: '跟', 11: '师傅', 12: '熊', 13: '老师', 14: '嘛，'}
* W5. input: {18: '师傅，', 19: '我', 20: '就', 21: '汇报。', 22: '二'} - output: release_units 1.{15: '是', 16: '我', 17: '的', 18: '师傅，'}; 2.{19: '我', 20: '就', 21: '汇报。'}
* W6. input: {23: '师傅，', 24: '我'} - output: release_units 1.{22: '二', 23: '师傅，'}
* W7. input: {25: '成', 26: '了。', 27: '他', 28: '说', 29: '你', 30: '成', 31: '了'} - output: release_units 1.{24: '我', 25: '成', 26: '了。'}
* W8. input: {32: '什么', 33: '了？', 34: '我'} - output: release_units 1.{27: '他', 28: '说', 29: '你', 30: '成', 31: '了', 32: '什么', 33: '了？'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W9. input: {35: '说', 36: '我', 37: '看到', 38: '一', 39: '个'} - output: release_units 1.{34: '我', 35: '说', 36: '我', 37: '看到'}
* W10. input: {40: '大', 41: '月', 42: '亮', 43: '了，'} - output: release_units 1.{38: '一', 39: '个', 40: '大', 41: '月', 42: '亮', 43: '了，'} <- ISSUE2: oversized chunk release unit 1 size=6 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W11. input: {44: '亮', 45: '亮', 46: '的，', 47: '你', 48: '看'} - output: release_units 1.{44: '亮', 45: '亮', 46: '的，'}
* W12. input: {49: '啊，', 50: '一'} - output: release_units 1.{47: '你', 48: '看', 49: '啊，'}
* W13. input: {51: '堂', 52: '光。', 53: '他', 54: '说'} - output: release_units 1.{50: '一', 51: '堂', 52: '光。'}; 2.{53: '他', 54: '说'}
* W14. input: {55: '你', 56: '成', 57: '了', 58: '个'} - output: release_units None
* W15. input: {59: '屁，'} - output: release_units 1.{55: '你', 56: '成', 57: '了', 58: '个', 59: '屁，'}
* W16. input: {60: '哈哈哈哈哈！', 61: '他', 62: '就', 63: '跟', 64: '我'} - output: release_units 1.{60: '哈哈哈哈哈！'}
* W17. input: {65: '说话', 66: '不', 67: '客气'} - output: release_units 1.{61: '他', 62: '就', 63: '跟', 64: '我', 65: '说话', 66: '不', 67: '客气'} <- ISSUE2: oversized chunk release unit 1 size=7 > 5. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W18. input: {68: '啊，', 69: '你'} - output: release_units 1.{68: '啊，'}
* W19. input: {70: '那', 71: '个', 72: '叫成', 73: '了。'} - output: release_units 1.{69: '你', 70: '那', 71: '个', 72: '叫成', 73: '了。'}

Reconfirm the RULEs and your task!


- retry: 2/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>说，我当时</src>; start=0.00, end=1.00
* W1. <src>我只是看到</src>; start=1.00, end=2.00
* W2. <src>月轮，</src>; start=2.00, end=3.00
* W3. <src>我就跟师傅</src>; start=3.00, end=4.00
* W4. <src>熊老师嘛，是我的</src>; start=4.00, end=5.00
* W5. <src>师傅，我就汇报。</src>; start=5.00, end=6.00
* W6. <src>二师傅，</src>; start=6.00, end=7.00
* W7. <src>我成了。他说你成了</src>; start=7.00, end=8.00
* W8. <src>什么了？</src>; start=8.00, end=9.00
* W9. <src>我说我看到一个</src>; start=9.00, end=10.00
* W10. <src>大月亮了，</src>; start=10.00, end=11.00
* W11. <src>亮亮的，你看</src>; start=11.00, end=12.00
* W12. <src>啊，</src>; start=12.00, end=13.00
* W13. <src>一堂光。他说</src>; start=13.00, end=14.00
* W14. <src><|wait|></src>; start=14.00, end=15.00
* W15. <src>你成了个屁，</src>; start=15.00, end=16.00
* W16. <src>哈哈哈哈哈！他就跟我</src>; start=16.00, end=17.00
* W17. <src>说话不客气</src>; start=17.00, end=18.00
* W18. <src>啊，</src>; start=18.00, end=19.00
* W19. <src>你那个叫成了。</src>; start=19.00, end=19.80
```

---
