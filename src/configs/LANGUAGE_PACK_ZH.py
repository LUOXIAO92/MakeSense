# --- TIME WINDOW PRESSURED SEGMENTATION ---

TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

raw_text: "我们跟民众一起协作出来的东西，那被民众接受了，而且民众也觉得也看到政府的努力，那我觉得这个是跟民众互信是有一个正相关的一个关系。"

word_indices: 
* W0. {0: '我们', 1: '跟'}
* W1. {2: '民众', 3: '一起', 4: '协作'}
* W2. {5: '出来', 6: '的', 7: '东西', 8: '，'}
* W3. {9: '那', 10: '被', 11: '民众'}
* W4. {12: '接受'}
* W5. {13: '了', 14: '，', 15: '而且', 16: '民众', 17: '也'}
* W6. {18: '觉得', 19: '也', 20: '看到', 21: '政府'}
* W7. {22: '的', 23: '努力', 24: '，', 25: '那', 26: '我'}
* W8. {27: '觉得', 28: '这个', 29: '是', 30: '跟', 31: '民众'}
* W9. {32: '互信'}
* W10. {33: '是', 34: '有', 35: '一个', 36: '正'}
* W12. {37: '相关', 38: '的', 39: '一个'}
* W13. {40: '关系', 41: '。'}

<scratchpad>
* W0. {0: '我们', 1: '跟'}
  - carried_over: None
  - defer: '我们跟' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [0,1]
  - release_units: None

* W1. {2: '民众', 3: '一起', 4: '协作'}
  - carried_over: {0: '我们', 1: '跟'}
  - defer: '协作' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window: [4]
  - release_units:
    1. 我们跟民众一起, '我们跟' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2,3]

* W2. {5: '出来', 6: '的', 7: '东西', 8: '，'}
  - carried_over: {4: '协作'}
  - defer: None
  - release_units:
    1. 协作出来的东西， '协作' is carried over from the previous window; released here because it is now a stable minimal sense unit: [4,5,6,7,8]

* W3. {9: '那', 10: '被', 11: '民众'}
  - carried_over: None
  - defer: '被民众' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10,11]
  - release_units:
    1. 那, stable minimal sense unit in the current window: [9]

* W4. {12: '接受'}
  - carried_over: {10: '被', 11: '民众'}
  - defer: '被民众接受' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [10,11,12]
  - release_units: None

* W5. {13: '了', 14: '，', 15: '而且', 16: '民众', 17: '也'}
  - carried_over: {10: '被', 11: '民众', 12: '接受'}
  - defer: '民众也' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16,17]
  - release_units:
    1. 被民众接受了， '被民众接受' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12,13,14]
    2. 而且, stable minimal sense unit in the current window: [15]

* W6. {18: '觉得', 19: '也', 20: '看到', 21: '政府'}
  - carried_over: {16: '民众', 17: '也'}
  - defer: '政府' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [21]
  - release_units:
    1. 民众也觉得, '民众也' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17,18]
    2. 也看到, stable minimal sense unit in the current window: [19,20]

* W7. {22: '的', 23: '努力', 24: '，', 25: '那', 26: '我'}
  - carried_over: {21: '政府'}
  - defer: '那我' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25,26]
  - release_units:
    1. 政府的努力， '政府' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22,23,24]

* W8. {27: '觉得', 28: '这个', 29: '是', 30: '跟', 31: '民众'}
  - carried_over: {25: '那', 26: '我'}
  - defer: '跟民众' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [30,31]
  - release_units:
    1. 那我觉得, '那我' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26,27]
    2. 这个是, stable minimal sense unit in the current window: [28,29]

* W9. {32: '互信'}
  - carried_over: {30: '跟', 31: '民众'}
  - defer: None
  - release_units:
    1. 跟民众互信, '跟民众' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32]

* W10. {33: '是', 34: '有', 35: '一个', 36: '正'}
  - carried_over: None
  - defer: '正' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [36]
  - release_units:
    1. 是有一个, stable minimal sense unit in the current window: [33,34,35]

* W12. {37: '相关', 38: '的', 39: '一个'}
  - carried_over: {36: '正'}
  - defer: '一个' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [39]
  - release_units:
    1. 正相关的, '正' is carried over from the previous window; released here because it is now a stable minimal sense unit: [36,37,38]

* W13. {40: '关系', 41: '。'}
  - carried_over: {39: '一个'}
  - defer: None
  - release_units:
    1. 一个关系。 '一个' is carried over from the previous window; released here because it is now a stable minimal sense unit: [39,40,41]
</scratchpad>
<result>
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9],
  [10,11,12,13,14],
  [15],
  [16,17,18],
  [19,20],
  [21,22,23,24],
  [25,26,27],
  [28,29],
  [30,31,32],
  [33,34,35],
  [36,37,38],
  [39,40,41]
]
</result>


## Sample 2:

raw_text: "我们得完成很多事情，才能解放地球。光明势力也很开心，看见有人愿意做事。毕竟，地球上有七十亿人，有能力又愿意投入这项工作的人却不多。"

word_indices: 
* W0. {0: '我们', 1: '得', 2: '完成'}
* W1. {3: '很多'}
* W2. {4: '事情', 5: '，', 6: '才能', 7: '解放'}
* W3. {}
* W4. {8: '地球', 9: '。', 10: '光明'}
* W5. {11: '势力', 12: '也', 13: '很'}
* W6. {14: '开心', 15: '，'}
* W7. {16: '看见', 17: '有人', 18: '愿意'}
* W8. {19: '做事', 20: '。'}
* W9. {21: '毕竟', 22: '，'}
* W10. {23: '地球', 24: '上', 25: '有'}
* W11. {26: '七十'}
* W12. {27: '亿人', 28: '，', 29: '有'}
* W13. {30: '能力', 31: '又', 32: '愿意'}
* W14. {33: '投入', 34: '这项', 35: '工作'}
* W15. {36: '的', 37: '人', 38: '却'}
* W16. {39: '不', 40: '多', 41: '。'}

<scratchpad>
* W0. {0: '我们', 1: '得', 2: '完成'}
  - carried_over: None
  - defer: '我们得完成' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1,2]
  - release_units: None

* W1. {3: '很多'}
  - carried_over: {0: '我们', 1: '得', 2: '完成'}
  - defer: '很多' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [3]
  - release_units:
    1. 我们得完成, latency-forced partial release; waiting longer would violate output continuity, so only the smallest locally interpretable fragment is released now: [0,1,2]

* W2. {4: '事情', 5: '，', 6: '才能', 7: '解放'}
  - carried_over: {3: '很多'}
  - defer: '才能解放' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [6,7]
  - release_units:
    1. 很多事情， '很多' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3,4,5]

* W3. {}
  - carried_over: {6: '才能', 7: '解放'}
  - defer: '才能解放' still does not yet form the best stable release unit / minimal sense unit here; continue deferring it across the empty window because no new material arrives in the current window: [6,7]
  - release_units: None

* W4. {8: '地球', 9: '。', 10: '光明'}
  - carried_over: {6: '才能', 7: '解放'}
  - defer: '光明' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [10]
  - release_units:
    1. 才能解放地球。 '才能解放' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7,8,9]

* W5. {11: '势力', 12: '也', 13: '很'}
  - carried_over: {10: '光明'}
  - defer: '也很' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [12,13]
  - release_units:
    1. 光明势力, '光明' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11]

* W6. {14: '开心', 15: '，'}
  - carried_over: {12: '也', 13: '很'}
  - defer: None
  - release_units:
    1. 也很开心， '也很' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13,14,15]

* W7. {16: '看见', 17: '有人', 18: '愿意'}
  - carried_over: None
  - defer: '愿意' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [18]
  - release_units:
    1. 看见有人, stable minimal sense unit in the current window: [16,17]

* W8. {19: '做事', 20: '。'}
  - carried_over: {18: '愿意'}
  - defer: None
  - release_units:
    1. 愿意做事。 '愿意' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20]

* W9. {21: '毕竟', 22: '，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 毕竟， stable minimal sense unit in the current window: [21,22]

* W10. {23: '地球', 24: '上', 25: '有'}
  - carried_over: None
  - defer: '地球上有' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [23,24,25]
  - release_units: None

* W11. {26: '七十'}
  - carried_over: {23: '地球', 24: '上', 25: '有'}
  - defer: '有七十' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25,26]
  - release_units:
    1. 地球上, latency-forced partial release; waiting longer would violate output continuity, so only the smallest locally interpretable fragment is released now: [23,24]

* W12. {27: '亿人', 28: '，', 29: '有'}
  - carried_over: {25: '有', 26: '七十'}
  - defer: '有' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [29]
  - release_units:
    1. 有七十亿人， '有七十' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26,27,28]

* W13. {30: '能力', 31: '又', 32: '愿意'}
  - carried_over: {29: '有'}
  - defer: None
  - release_units:
    1. 有能力, '有' is carried over from the previous window; released here because it is now a stable minimal sense unit: [29,30]
    2. 又愿意, stable minimal sense unit in the current window: [31,32]

* W14. {33: '投入', 34: '这项', 35: '工作'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 投入这项工作, released here because it is the smallest locally stable meaning unit available under the current window token boundary: [33,34,35]

* W15. {36: '的', 37: '人', 38: '却'}
  - carried_over: None
  - defer: '却' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [38]
  - release_units:
    1. 的人, this is a non-ideal but locally valid leftover release unit created by the earlier local-optimal release of `投入这项工作`; it appears separately here under the current window sequence: [36,37]

* W16. {39: '不', 40: '多', 41: '。'}
  - carried_over: {38: '却'}
  - defer: None
  - release_units:
    1. 却不多。 '却' is carried over from the previous window; released here because it is now a stable minimal sense unit: [38,39,40,41]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4,5],
  [6,7,8,9],
  [10,11],
  [12,13,14,15],
  [16,17],
  [18,19,20],
  [21,22],
  [23,24],
  [25,26,27,28],
  [29,30],
  [31,32],
  [33,34,35],
  [36,37],
  [38,39,40,41]
]
</result>


## Sample 3:

raw_text: "等他回答之后，我们要去验证他答对与或者错。那答对与错答案在这里，那我们要去算什么？如果"

word_indices:
* W0. {0: '等', 1: '他', 2: '回答'}
* W1. {3: '之后', 4: '，', 5: '我们', 6: '要', 7: '去'}
* W2. {8: '验证', 9: '他'}
* W3. {}
* W4. {10: '答对', 11: '与', 12: '或者'}
* W5. {13: '错', 14: '。'}
* W6. {}
* W7. {15: '那'}
* W8. {16: '答对', 17: '与', 18: '错'}
* W9. {19: '答案', 20: '在'}
* W10. {21: '这里', 22: '，', 23: '那', 24: '我们'}
* W11. {25: '要', 26: '去', 27: '算'}
* W12. {}
* W13. {28: '什么', 29: '？', 30: '如果'}

<scratchpad>
* W0. {0: '等', 1: '他', 2: '回答'}
  - carried_over: None
  - defer: '等他回答' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1,2]
  - release_units: None

* W1. {3: '之后', 4: '，', 5: '我们', 6: '要', 7: '去'}
  - carried_over: {0: '等', 1: '他', 2: '回答'}
  - defer: '我们要去' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [5,6,7]
  - release_units:
    1. 等他回答之后， '等他回答' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2,3,4]

* W2. {8: '验证', 9: '他'}
  - carried_over: {5: '我们', 6: '要', 7: '去'}
  - defer: '验证他' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [8,9]
  - release_units:
    1. 我们要去, '我们要去' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7]

* W3. {}
  - carried_over: {8: '验证', 9: '他'}
  - defer: '验证他' still does not yet form the best stable release unit / minimal sense unit here; continue deferring it across the empty window because no new material arrives in the current window: [8,9]
  - release_units: None

* W4. {10: '答对', 11: '与', 12: '或者'}
  - carried_over: {8: '验证', 9: '他'}
  - defer: '答对与或者' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10,11,12]
  - release_units:
    1. 验证他, released here under window pressure because the previous window had no output, so the current window must flush something now; this is the smallest locally interpretable unit available at this point: [8,9]

* W5. {13: '错', 14: '。'}
  - carried_over: {10: '答对', 11: '与', 12: '或者'}
  - defer: None
  - release_units:
    1. 答对与或者错。 '答对与或者' is carried over from the previous window; released here because it is now a locally stable meaning unit referring to the answer-correctness outcome: [10,11,12,13,14]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {15: '那'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 那, stable minimal sense unit in the current window: [15]

* W8. {16: '答对', 17: '与', 18: '错'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 答对与错, stable minimal sense unit in the current window: [16,17,18]

* W9. {19: '答案', 20: '在'}
  - carried_over: None
  - defer: '在' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [20]
  - release_units:
    1. 答案, stable minimal sense unit in the current window: [19]

* W10. {21: '这里', 22: '，', 23: '那', 24: '我们'}
  - carried_over: {20: '在'}
  - defer: '我们' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [24]
  - release_units:
    1. 在这里， '在' is carried over from the previous window; released here because it is now a stable minimal sense unit: [20,21,22]
    2. 那, stable minimal sense unit in the current window: [23]

* W11. {25: '要', 26: '去', 27: '算'}
  - carried_over: {24: '我们'}
  - defer: '算' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [27]
  - release_units:
    1. 我们要去, '我们' is carried over from the previous window; released here because it is now a stable minimal sense unit: [24,25,26]

* W12. {}
  - carried_over: {27: '算'}
  - defer: '算' still does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [27]
  - release_units: None

* W13. {28: '什么', 29: '？', 30: '如果'}
  - carried_over: {27: '算'}
  - defer: None
  - release_units:
    1. 算什么？ '算' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28,29]
    2. 如果, this appears here as a stream-end leftover opener because the source cuts off immediately after it in the current ASR segment: [30]
</scratchpad>
<result>
[
  [0,1,2,3,4],
  [5,6,7],
  [8,9],
  [10,11,12,13,14],
  [15],
  [16,17,18],
  [19],
  [20,21,22],
  [23],
  [24,25,26],
  [27,28,29],
  [30]
]
</result>


## Sample 4:

raw_text: "就我在这儿就分享给大家，就是我要吃猪油，要吃大油，要吃各种油为主。实际上，英国的健康杂志呢，啊，列出了一百个健康食品当中呢，这个猪大油呢，它排名是第八位。"

word_indices: 
* W0. {0: '就', 1: '我', 2: '在'}, 
* W1. {3: '这儿', 4: '就', 5: '分享', 6: '给'}, 
* W2. {7: '大家', 8: '，'}, 
* W3. {9: '就是', 10: '我要'}, 
* W4. {11: '吃'}, 
* W5. {12: '猪油', 13: '，', 14: '要', 15: '吃'}, 
* W6. {}, 
* W7. {16: '大油', 17: '，', 18: '要', 19: '吃', 20: '各种'}, 
* W8. {21: '油'}, 
* W9. {}, 
* W10. {22: '为主', 23: '。', 24: '实际上', 25: '，'}, 
* W11. {26: '英国', 27: '的', 28: '健康'}, 
* W12. {29: '杂志'}, 
* W13. {30: '呢', 31: '，', 32: '啊', 33: '，', 34: '列出', 35: '了'}, 
* W14. {36: '一百个'}, 
* W15. {37: '健康', 38: '食品', 39: '当中'}, 
* W16. {40: '呢', 41: '，', 42: '这个'}, 
* W17. {43: '猪大油'}, 
* W18. {44: '呢', 45: '，', 46: '它', 47: '排名'}, 
* W19. {48: '是', 49: '第八位', 50: '。'}

<scratchpad>
* W0. {0: '就', 1: '我', 2: '在'}
  - carried_over: None
  - defer: '就我在' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1,2]
  - release_units: None

* W1. {3: '这儿', 4: '就', 5: '分享', 6: '给'}
  - carried_over: {0: '就', 1: '我', 2: '在'}
  - defer: '就分享给' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [4,5,6]
  - release_units:
    1. 就, '就' is carried over from the previous window; released here as a small discourse piece that surfaces before the earlier local-optimal unit `我在这儿` under the current window sequence: [0]
    2. 我在这儿, '我在' is carried over from the previous window; released here because it is now a stable minimal sense unit: [1,2,3]

* W2. {7: '大家', 8: '，'}
  - carried_over: {4: '就', 5: '分享', 6: '给'}
  - defer: None
  - release_units:
    1. 就, '就' is carried over from the previous window; released here as a small discourse piece preceding the following action unit under the current window sequence: [4]
    2. 分享给大家， '分享给' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7,8]

* W3. {9: '就是', 10: '我要'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 就是, stable minimal sense unit in the current window: [9]
    2. 我要, stable minimal sense unit in the current window: [10]

* W4. {11: '吃'}
  - carried_over: None
  - defer: '吃' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [11]
  - release_units: None

* W5. {12: '猪油', 13: '，', 14: '要', 15: '吃'}
  - carried_over: {11: '吃'}
  - defer: '要吃' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [14,15]
  - release_units:
    1. 吃猪油， '吃' is carried over from the previous window; released here because it is now a stable minimal sense unit: [11,12,13]

* W6. {}
  - carried_over: {14: '要', 15: '吃'}
  - defer: '要吃' still does not yet form the best stable release unit / minimal sense unit here; continue deferring it across the empty window because no new material arrives in the current window: [14,15]
  - release_units: None

* W7. {16: '大油', 17: '，', 18: '要', 19: '吃', 20: '各种'}
  - carried_over: {14: '要', 15: '吃'}
  - defer: '要吃各种' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [18,19,20]
  - release_units:
    1. 要吃大油， '要吃' is carried over from the previous window; released here because it is now a stable minimal sense unit: [14,15,16,17]

* W8. {21: '油'}
  - carried_over: {18: '要', 19: '吃', 20: '各种'}
  - defer: None
  - release_units:
    1. 要吃各种油, '要吃各种' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20,21]

* W9. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W10. {22: '为主', 23: '。', 24: '实际上', 25: '，'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 为主。 stable minimal sense unit in the current window: [22,23]
    2. 实际上， stable minimal sense unit in the current window: [24,25]

* W11. {26: '英国', 27: '的', 28: '健康'}
  - carried_over: None
  - defer: '英国的健康' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [26,27,28]
  - release_units: None

* W12. {29: '杂志'}
  - carried_over: {26: '英国', 27: '的', 28: '健康'}
  - defer: None
  - release_units:
    1. 英国的健康杂志, '英国的健康' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27,28,29]

* W13. {30: '呢', 31: '，', 32: '啊', 33: '，', 34: '列出', 35: '了'}
  - carried_over: None
  - defer: '列出了' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [34,35]
  - release_units:
    1. 呢， this host-dependent tail is released separately here because its host phrase was already emitted in the previous window: [30,31]
    2. 啊， stable minimal sense unit in the current window: [32,33]

* W14. {36: '一百个'}
  - carried_over: {34: '列出', 35: '了'}
  - defer: None
  - release_units:
    1. 列出了一百个, '列出了' is carried over from the previous window; released here because it is now a stable minimal sense unit: [34,35,36]
  
* W15. {37: '健康', 38: '食品', 39: '当中'}
  - carried_over: None
  - defer: '当中' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [39]
  - release_units:
    1. 健康食品, stable minimal sense unit in the current window: [37,38]

* W16. {40: '呢', 41: '，', 42: '这个'}
  - carried_over: {39: '当中'}
  - defer: '这个' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [42]
  - release_units:
    1. 当中呢， '当中' is carried over from the previous window; released here as the continuation left over after the earlier local-optimal release of `健康食品`: [39,40,41]

* W17. {43: '猪大油'}
  - carried_over: {42: '这个'}
  - defer: '这个猪大油' is not yet the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [42,43]
  - release_units: None

* W18. {44: '呢', 45: '，', 46: '它', 47: '排名'}
  - carried_over: {42: '这个', 43: '猪大油'}
  - defer: None
  - release_units:
    1. 这个猪大油呢， '这个猪大油' is carried over from the previous window; released here because it is now a stable minimal sense unit: [42,43,44,45]
    2. 它排名, stable minimal sense unit in the current window: [46,47]

* W19. {48: '是', 49: '第八位', 50: '。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 是第八位。 stable minimal sense unit in the current window: [48,49,50]
</scratchpad>
<result>
[
  [0],
  [1,2,3],
  [4],
  [5,6,7,8],
  [9],
  [10],
  [11,12,13],
  [14,15,16,17],
  [18,19,20,21],
  [22,23],
  [24,25],
  [26,27,28,29],
  [30,31],
  [32,33],
  [34,35,36],
  [37,38],
  [39,40,41],
  [42,43,44,45],
  [46,47],
  [48,49,50]
]
</result>


## Sample 5:

raw_text: "今天在佛教界有一个最大的误会，提到性的时候，就是佛性。佛性是什么？光啊，就就完事儿了。实际上，你只见光，你的层次太低了。"

word_indices:
* W0. {0: '今天', 1: '在'}
* W1. {2: '佛教界', 3: '有', 4: '一个'}
* W2. {5: '最大', 6: '的'}
* W3. {7: '误会', 8: '，', 9: '提到', 10: '性', 11: '的'}
* W4. {12: '时候', 13: '，'}
* W5. {14: '就是'}
* W6. {15: '佛性', 16: '。', 17: '佛性', 18: '是', 19: '什么', 20: '？'}
* W7. {}
* W8. {21: '光', 22: '啊', 23: '，', 24: '就', 25: '就', 26: '完', 27: '事儿'}
* W9. {28: '了', 29: '。'}
* W10. {30: '实际上', 31: '，', 32: '你'}
* W11. {33: '只见'}
* W12. {34: '光', 35: '，', 36: '你'}
* W13. {37: '的', 38: '层次'}
* W14. {39: '太低', 40: '了', 41: '。'}

<scratchpad>
* W0. {0: '今天', 1: '在'}
  - carried_over: None
  - defer: '在' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [1]
  - release_units:
    1. 今天, stable minimal sense unit in the current window: [0]

* W1. {2: '佛教界', 3: '有', 4: '一个'}
  - carried_over: {1: '在'}
  - defer: '有一个' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [3,4]
  - release_units:
    1. 在佛教界, '在' is carried over from the previous window; released here because it is now a stable minimal sense unit: [1,2]

* W2. {5: '最大', 6: '的'}
  - carried_over: {3: '有', 4: '一个'}
  - defer: '最大的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [5,6]
  - release_units:
    1. 有一个, '有一个' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3,4]

* W3. {7: '误会', 8: '，', 9: '提到', 10: '性', 11: '的'}
  - carried_over: {5: '最大', 6: '的'}
  - defer: '提到性的' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9,10,11]
  - release_units:
    1. 最大的误会， '最大的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7,8]

* W4. {12: '时候', 13: '，'}
  - carried_over: {9: '提到', 10: '性', 11: '的'}
  - defer: None
  - release_units:
    1. 提到性的时候， '提到性的' is carried over from the previous window; released here because it is now a stable minimal sense unit: [9,10,11,12,13]

* W5. {14: '就是'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 就是, stable minimal sense unit in the current window: [14]

* W6. {15: '佛性', 16: '。', 17: '佛性', 18: '是', 19: '什么', 20: '？'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 佛性。 stable minimal sense unit in the current window: [15,16]
    2. 佛性是什么？ stable minimal sense unit in the current window: [17,18,19,20]

* W7. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W8. {21: '光', 22: '啊', 23: '，', 24: '就', 25: '就', 26: '完', 27: '事儿'}
  - carried_over: None
  - defer: '就就完事儿' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [24,25,26,27]
  - release_units:
    1. 光啊， stable minimal sense unit in the current window; it already functions as a local answer unit to the preceding question `佛性是什么？`: [21,22,23]

* W9. {28: '了', 29: '。'}
  - carried_over: {24: '就', 25: '就', 26: '完', 27: '事儿'}
  - defer: None
  - release_units:
    1. 就就完事儿了。 '就就完事儿' is carried over from the previous window; released here because it is now a stable minimal sense unit: [24,25,26,27,28,29]

* W10. {30: '实际上', 31: '，', 32: '你'}
  - carried_over: None
  - defer: '你' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [32]
  - release_units:
    1. 实际上， stable minimal sense unit in the current window: [30,31]

* W11. {33: '只见'}
  - carried_over: {32: '你'}
  - defer: '你只见' is not yet the best stable release unit / minimal sense unit in the current window; continue deferring it to the next window because the previous window already had output and the next window is non-empty: [32,33]
  - release_units: None

* W12. {34: '光', 35: '，', 36: '你'}
  - carried_over: {32: '你', 33: '只见'}
  - defer: '你' is deferred to the next window because only the remainder is deferred after the current window has already emitted something: [36]
  - release_units:
    1. 你只见光， '你只见' is carried over from the previous window; released here because it is now a stable minimal sense unit in the current window: [32,33,34,35]

* W13. {37: '的', 38: '层次'}
  - carried_over: {36: '你'}
  - defer: None
  - release_units:
    1. 你的层次, '你' is carried over from the previous window; released here because it is now a stable minimal sense unit: [36,37,38]

* W14. {39: '太低', 40: '了', 41: '。'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 太低了。 stable minimal sense unit in the current window: [39,40,41]
</scratchpad>
<result>
[
  [0],
  [1,2],
  [3,4],
  [5,6,7,8],
  [9,10,11,12,13],
  [14],
  [15,16],
  [17,18,19,20],
  [21,22,23],
  [24,25,26,27,28,29],
  [30,31],
  [32,33,34,35],
  [36,37,38],
  [39,40,41]
]
</result>
""".lstrip("\n")


# --- PURE TEXT SEGMENTATION ---

PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

token_indices:
{0: '我们', 1: '跟', 2: '民众', 3: '一起', 4: '协作', 5: '出来', 6: '的', 7: '东西', 8: '，', 9: '那', 10: '被', 11: '民众', 12: '接受', 13: '了', 14: '，', 15: '而且', 16: '民众', 17: '也', 18: '觉得', 19: '也', 20: '看到', 21: '政府', 22: '的', 23: '努力', 24: '，', 25: '那', 26: '我', 27: '觉得', 28: '这个', 29: '是', 30: '跟', 31: '民众', 32: '互信', 33: '是', 34: '有', 35: '一个', 36: '正', 37: '相关', 38: '的', 39: '一个', 40: '关系', 41: '。'}

<scratchpad>
1. 我们跟民众一起
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [0, 1, 2, 3]

2. 协作出来的东西，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [4, 5, 6, 7, 8]

3. 那
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [9]

4. 被民众接受了，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [10, 11, 12, 13, 14]

5. 而且
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [15]

6. 民众也觉得
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [16, 17, 18]

7. 也看到
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [19, 20]

8. 政府的努力，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [21, 22, 23, 24]

9. 那我觉得
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [25, 26, 27]

10. 这个是
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [28, 29]

11. 跟民众互信
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [30, 31, 32]

12. 是有一个
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [33, 34, 35]

13. 正相关的
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [36, 37, 38]

14. 一个关系。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [39, 40, 41]
</scratchpad>
<result>
[
  [0,1,2,3],
  [4,5,6,7,8],
  [9],
  [10,11,12,13,14],
  [15],
  [16,17,18],
  [19,20],
  [21,22,23,24],
  [25,26,27],
  [28,29],
  [30,31,32],
  [33,34,35],
  [36,37,38],
  [39,40,41]
]
</result>


## Sample 2:

token_indices:
{0: '我们', 1: '得', 2: '完成', 3: '很多', 4: '事情', 5: '，', 6: '才能', 7: '解放', 8: '地球', 9: '。', 10: '光明', 11: '势力', 12: '也', 13: '很', 14: '开心', 15: '，', 16: '看见', 17: '有人', 18: '愿意', 19: '做事', 20: '。', 21: '毕竟', 22: '，', 23: '地球', 24: '上', 25: '有', 26: '七十', 27: '亿人', 28: '，', 29: '有', 30: '能力', 31: '又', 32: '愿意', 33: '投入', 34: '这项', 35: '工作', 36: '的', 37: '人', 38: '却', 39: '不', 40: '多', 41: '。'}

<scratchpad>
1. 我们得完成
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [0, 1, 2]

2. 很多事情，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [3, 4, 5]

3. 才能解放地球。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [6, 7, 8, 9]

4. 光明势力
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [10, 11]

5. 也很开心，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [12, 13, 14, 15]

6. 看见有人
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [16, 17]

7. 愿意做事。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [18, 19, 20]

8. 毕竟，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [21, 22]

9. 地球上
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [23, 24]

10. 有七十亿人，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [25, 26, 27, 28]

11. 有能力
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [29, 30]

12. 又愿意
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [31, 32]

13. 投入这项工作
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [33, 34, 35]

14. 的人
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [36, 37]

15. 却不多。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [38, 39, 40, 41]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4,5],
  [6,7,8,9],
  [10,11],
  [12,13,14,15],
  [16,17],
  [18,19,20],
  [21,22],
  [23,24],
  [25,26,27,28],
  [29,30],
  [31,32],
  [33,34,35],
  [36,37],
  [38,39,40,41]
]
</result>


## Sample 3:

token_indices:
{0: '等', 1: '他', 2: '回答', 3: '之后', 4: '，', 5: '我们', 6: '要', 7: '去', 8: '验证', 9: '他', 10: '答对', 11: '与', 12: '或者', 13: '错', 14: '。', 15: '那', 16: '答对', 17: '与', 18: '错', 19: '答案', 20: '在', 21: '这里', 22: '，', 23: '那', 24: '我们', 25: '要', 26: '去', 27: '算', 28: '什么', 29: '？', 30: '如果'}

<scratchpad>
1. 等他回答之后，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [0, 1, 2, 3, 4]

2. 我们要去
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [5, 6, 7]

3. 验证他
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [8, 9]

4. 答对与或者错。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [10, 11, 12, 13, 14]

5. 那
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [15]

6. 答对与错
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [16, 17, 18]

7. 答案
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [19]

8. 在这里，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [20, 21, 22]

9. 那
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [23]

10. 我们要去
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [24, 25, 26]

11. 算什么？
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [27, 28, 29]

12. 如果
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [30]
</scratchpad>
<result>
[
  [0,1,2,3,4],
  [5,6,7],
  [8,9],
  [10,11,12,13,14],
  [15],
  [16,17,18],
  [19],
  [20,21,22],
  [23],
  [24,25,26],
  [27,28,29],
  [30]
]
</result>


## Sample 4:

token_indices:
{0: '就', 1: '我', 2: '在', 3: '这儿', 4: '就', 5: '分享', 6: '给', 7: '大家', 8: '，', 9: '就是', 10: '我要', 11: '吃', 12: '猪油', 13: '，', 14: '要', 15: '吃', 16: '大油', 17: '，', 18: '要', 19: '吃', 20: '各种', 21: '油', 22: '为主', 23: '。', 24: '实际上', 25: '，', 26: '英国', 27: '的', 28: '健康', 29: '杂志', 30: '呢', 31: '，', 32: '啊', 33: '，', 34: '列出', 35: '了', 36: '一百个', 37: '健康', 38: '食品', 39: '当中', 40: '呢', 41: '，', 42: '这个', 43: '猪大油', 44: '呢', 45: '，', 46: '它', 47: '排名', 48: '是', 49: '第八位', 50: '。'}

<scratchpad>
1. 就
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [0]

2. 我在这儿
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [1, 2, 3]

3. 就
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [4]

4. 分享给大家，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [5, 6, 7, 8]

5. 就是
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [9]

6. 我要
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [10]

7. 吃猪油，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [11, 12, 13]

8. 要吃大油，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [14, 15, 16, 17]

9. 要吃各种油
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [18, 19, 20, 21]

10. 为主。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [22, 23]

11. 实际上，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [24, 25]

12. 英国的健康杂志
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [26, 27, 28, 29]

13. 呢，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [30, 31]

14. 啊，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [32, 33]

15. 列出了一百个
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [34, 35, 36]

16. 健康食品
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [37, 38]

17. 当中呢，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [39, 40, 41]

18. 这个猪大油呢，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [42, 43, 44, 45]

19. 它排名
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [46, 47]

20. 是第八位。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [48, 49, 50]
</scratchpad>
<result>
[
  [0],
  [1,2,3],
  [4],
  [5,6,7,8],
  [9],
  [10],
  [11,12,13],
  [14,15,16,17],
  [18,19,20,21],
  [22,23],
  [24,25],
  [26,27,28,29],
  [30,31],
  [32,33],
  [34,35,36],
  [37,38],
  [39,40,41],
  [42,43,44,45],
  [46,47],
  [48,49,50]
]
</result>


## Sample 5:

token_indices:
{0: '今天', 1: '在', 2: '佛教界', 3: '有', 4: '一个', 5: '最大', 6: '的', 7: '误会', 8: '，', 9: '提到', 10: '性', 11: '的', 12: '时候', 13: '，', 14: '就是', 15: '佛性', 16: '。', 17: '佛性', 18: '是', 19: '什么', 20: '？', 21: '光', 22: '啊', 23: '，', 24: '就', 25: '就', 26: '完', 27: '事儿', 28: '了', 29: '。', 30: '实际上', 31: '，', 32: '你', 33: '只见', 34: '光', 35: '，', 36: '你', 37: '的', 38: '层次', 39: '太低', 40: '了', 41: '。'}

<scratchpad>
1. 今天
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [0]

2. 在佛教界
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [1, 2]

3. 有一个
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [3, 4]

4. 最大的误会，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [5, 6, 7, 8]

5. 提到性的时候，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [9, 10, 11, 12, 13]

6. 就是
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [14]

7. 佛性。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [15, 16]

8. 佛性是什么？
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [17, 18, 19, 20]

9. 光啊，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [21, 22, 23]

10. 就就完事儿了。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [24, 25, 26, 27, 28, 29]

11. 实际上，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [30, 31]

12. 你只见光，
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [32, 33, 34, 35]

13. 你的层次
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [36, 37, 38]

14. 太低了。
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Chinese local unit
   - sense_unit: [39, 40, 41]
</scratchpad>
<result>
[
  [0],
  [1,2],
  [3,4],
  [5,6,7,8],
  [9,10,11,12,13],
  [14],
  [15,16],
  [17,18,19,20],
  [21,22,23],
  [24,25,26,27,28,29],
  [30,31],
  [32,33,34,35],
  [36,37,38],
  [39,40,41]
]
</result>
""".lstrip("\n")


# --- CHINESE LANGUAGE PACK (Minimal Incremental Patch) ---

GENERAL_LANGUAGE_PACK = """
## CHINESE LANGUAGE PACK (Minimal Incremental Patch)

### Core Bias

Chinese should be segmented around **small stable local units**, not around larger sentence-like spans.

### Protect These Units

Prefer not to split the following unless latency pressure forces it:
- **verb-object units**  
  e.g. actions together with their direct objects

- **preposition / coverb + governed phrase**  
  especially structures with words like:
  - `在`
  - `对`
  - `跟`
  - `给`
  - `向`
  - `把`
  - `被`

- **short `的` phrases**  
  especially when `的` is binding a compact modifier to its head

- **result / directional complement units**  
  especially when the verb and its complement form one stable local unit

- **fixed collocations / lexicalized mini-units**

- **subjective stance / opinion units**  
  short units like:
  - `我觉得`
  - `我认为`
  - `就是说`
  when they already function as stable local discourse units

### Do Not Expose Bare Structural Words

Avoid releasing these as standalone output unless they are already inside a stable local unit:
- `的`
- `在`
- `跟`
- `被`
- `给`
- `把`
- similar structural or relational words

These usually need their local phrase context.

### Do Not Expose Host-Dependent Discourse Particles / Topic Tails

Avoid releasing strongly host-dependent discourse particles or topic-marking tails as standalone output unless latency pressure clearly forces it.

These usually need to stay attached to their host unit, rather than being exposed on their own.

Typical examples include items like:
- `呢`
- similar sentence-final / topic-linked particles
- other short trailing discourse pieces that mainly function through attachment to the preceding unit

Prefer:
- keeping the particle or tail with its host phrase
- releasing the full host-linked local unit once it is stable

Avoid:
- splitting off a host-dependent tail just because a boundary is available
- treating such particles as independent minimal sense units when their discourse function is still tied to the host

### Allow Small Discourse Units

Chinese may release some very small discourse-level units if they already have clear local discourse value, for example:
- turn-introducing units
- stance-marking units
- discourse markers
- hesitation / spoken emphasis units

Examples of the type of unit allowed:
- `那`
- `毕竟`
- `实际上`
- `那我觉得`

These are allowed not because they are syntactically complete, but because they already carry local discourse function.

### Preferred Chinese Stability Signals

When deciding whether a local unit is stable enough, prefer units that already contain one of these:
- a verb with its object
- a preposition / coverb with its phrase
- a compact `的` phrase
- a fixed collocation
- a stance / discourse unit with clear local meaning

### Chinese-Specific Failure Mode to Avoid

Do not drift back to:
- comma-based segmentation
- clause-sized segmentation
- waiting for a more complete small sentence

The Chinese target here is usually **smaller than a clause** and often closer to a compact local meaning unit.

### Practical Chinese Bias

If two candidate cuts are possible, prefer the one that keeps:
- the tighter verb-object unit
- the tighter preposition / coverb phrase
- the tighter short `的` phrase
- the tighter fixed collocation
- the tighter stance / discourse unit
""".lstrip("\n")