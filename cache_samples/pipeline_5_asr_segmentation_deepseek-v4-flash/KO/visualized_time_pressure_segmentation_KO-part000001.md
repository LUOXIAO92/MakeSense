=== KO_GazVxt6TX_8_W000008 ===

status: finished

raw_text:
다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.

word_indices:
* W0. {0: '다', 1: '마귀를'}
* W1. {2: '따르 면', 3: '망할', 4: '수는'}
* W2. {5: '있지만,'}
* W3. {6: '그렇 죠?', 7: '뭐', 8: '교회'}
* W4. {9: '십일조가', 10: '줄어서'}
* W5. {11: '망하 고', 12: '할', 13: '일이'}
* W6. {14: '아닙니다.', 15: '그리고'}
* W7. {16: '이', 17: '지상 에서', 18: '할', 19: '일은'}
* W8. {20: '끝없이', 21: '이'}
* W9. {22: '천국 을'}
* W10. {23: '확장 시켜가.'}

scratchpad:
* W0. {0: '다', 1: '마귀를'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 다 마귀를, stable minimal sense unit in the current window: [0,1]

* W1. {2: '따르 면', 3: '망할', 4: '수는'}
  - carried_over: None
  - defer: '망할 수는' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [3,4]
  - release_units:
    1. 따르 면, stable minimal sense unit in the current window: [2]

* W2. {5: '있지만,'}
  - carried_over: {3: '망할', 4: '수는'}
  - defer: None
  - release_units:
    1. 망할 수는 있지만,, '망할 수는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3,4,5]

* W3. {6: '그렇 죠?', 7: '뭐', 8: '교회'}
  - carried_over: None
  - defer: '교회' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [8]
  - release_units:
    1. 그렇 죠?, stable minimal sense unit in the current window: [6]
    2. 뭐, stable minimal sense unit in the current window: [7]

* W4. {9: '십일조가', 10: '줄어서'}
  - carried_over: {8: '교회'}
  - defer: None
  - release_units:
    1. 교회 십일조가, '교회' is carried over from the previous window; released here because it is now a stable minimal sense unit: [8,9]
    2. 줄어서, stable minimal sense unit in the current window: [10]

* W5. {11: '망하 고', 12: '할', 13: '일이'}
  - carried_over: None
  - defer: '할 일이' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [12,13]
  - release_units:
    1. 망하 고, stable minimal sense unit in the current window: [11]

* W6. {14: '아닙니다.', 15: '그리고'}
  - carried_over: {12: '할', 13: '일이'}
  - defer: None
  - release_units:
    1. 할 일이 아닙니다., '할 일이' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13,14]
    2. 그리고, stable minimal sense unit in the current window: [15]

* W7. {16: '이', 17: '지상 에서', 18: '할', 19: '일은'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 이 지상 에서 할 일은, stable minimal sense unit in the current window: [16,17,18,19]

* W8. {20: '끝없이', 21: '이'}
  - carried_over: None
  - defer: '이' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [21]
  - release_units:
    1. 끝없이, stable minimal sense unit in the current window: [20]

* W9. {22: '천국 을'}
  - carried_over: {21: '이'}
  - defer: None
  - release_units:
    1. 이 천국 을, '이' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22]

* W10. {23: '확장 시켜가.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 확장 시켜가., stable minimal sense unit in the current window: [23]

result:
[
  [0,1],
  [2],
  [3,4,5],
  [6],
  [7],
  [8,9],
  [10],
  [11],
  [12,13,14],
  [15],
  [16,17,18,19],
  [20],
  [21,22],
  [23]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>다 마귀를 </src>; start=0.00, end=1.00
* W1. <src>따르 면 </src>; start=1.00, end=2.00
* W2. <src>망할 수는 있지만, </src>; start=2.00, end=3.00
* W3. <src>그렇 죠? 뭐 </src>; start=3.00, end=4.00
* W4. <src>교회 십일조가 줄어서 </src>; start=4.00, end=5.00
* W5. <src>망하 고 </src>; start=5.00, end=6.00
* W6. <src>할 일이 아닙니다. 그리고 </src>; start=6.00, end=7.00
* W7. <src>이 지상 에서 할 일은 </src>; start=7.00, end=8.00
* W8. <src>끝없이 </src>; start=8.00, end=9.00
* W9. <src>이 천국 을 </src>; start=9.00, end=10.00
* W10. <src>확장 시켜가. </src>; start=10.00, end=10.39
```

---
=== KO_B00002_S05012_W000000 ===

status: finished

raw_text:
근데 이게 시기적으로 결혼이 뭐 했었으면 진작에 가능했었던 사람들이에요. 근데 어느 정도 시기를 좀 보고 자기가 벌려놓은 일이나 해야 될 일들이 있었기 때문에 그거를 좀 다 좀

word_indices:
* W0. {0: '근데', 1: '이게'}
* W1. {2: '시기 적으로'}
* W2. {3: '결혼 이', 4: '뭐'}
* W3. {5: '했었 으면'}
* W4. {6: '진작 에'}
* W5. {7: '가능 했었던'}
* W6. {}
* W7. {8: '사람 들이에요.', 9: '근데', 10: '어느'}
* W8. {11: '정도', 12: '시기 를', 13: '좀'}
* W9. {14: '보고', 15: '자기 가'}
* W10. {16: '벌려 놓은', 17: '일이나'}
* W11. {18: '해야', 19: '될', 20: '일들이'}
* W12. {21: '있었기', 22: '때문 에'}
* W13. {23: '그거 를', 24: '좀', 25: '다'}
* W14. {26: '좀'}

scratchpad:
* W0. {0: '근데', 1: '이게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 근데, stable minimal sense unit in the current window: [0]
    2. 이게, stable minimal sense unit in the current window: [1]

* W1. {2: '시기 적으로'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 시기 적으로, stable minimal sense unit in the current window: [2]

* W2. {3: '결혼 이', 4: '뭐'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 결혼 이, stable minimal sense unit in the current window: [3]
    2. 뭐, stable minimal sense unit in the current window: [4]

* W3. {5: '했었 으면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 했었 으면, stable minimal sense unit in the current window: [5]

* W4. {6: '진작 에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 진작 에, stable minimal sense unit in the current window: [6]

* W5. {7: '가능 했었던'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 가능 했었던, stable minimal sense unit in the current window: [7]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {8: '사람 들이에요.', 9: '근데', 10: '어느'}
  - carried_over: None
  - defer: '어느' does not yet form a stable minimal sense unit in the current window; defer it to the next window because the current window must release something (previous window was empty) and deferring only the remainder is allowed after releasing other units: [10]
  - release_units:
    1. 사람 들이에요., stable minimal sense unit in the current window: [8]
    2. 근데, stable minimal sense unit in the current window: [9]

* W8. {11: '정도', 12: '시기 를', 13: '좀'}
  - carried_over: {10: '어느'}
  - defer: None
  - release_units:
    1. 어느 정도, '어느' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11]
    2. 시기 를, stable minimal sense unit in the current window: [12]
    3. 좀, stable minimal sense unit in the current window: [13]

* W9. {14: '보고', 15: '자기 가'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 보고, stable minimal sense unit in the current window: [14]
    2. 자기 가, stable minimal sense unit in the current window: [15]

* W10. {16: '벌려 놓은', 17: '일이나'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 벌려 놓은, stable minimal sense unit in the current window: [16]
    2. 일이나, stable minimal sense unit in the current window: [17]

* W11. {18: '해야', 19: '될', 20: '일들이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 해야 될, stable minimal sense unit (predicate chain) in the current window: [18,19]
    2. 일들이, stable minimal sense unit in the current window: [20]

* W12. {21: '있었기', 22: '때문 에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 있었기 때문에, stable minimal sense unit in the current window: [21,22]

* W13. {23: '그거 를', 24: '좀', 25: '다'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그거 를, stable minimal sense unit in the current window: [23]
    2. 좀, stable minimal sense unit in the current window: [24]
    3. 다, stable minimal sense unit in the current window: [25]

* W14. {26: '좀'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 좀, stable minimal sense unit in the current window: [26]

result:
[
  [0],
  [1],
  [2],
  [3],
  [4],
  [5],
  [6],
  [7],
  [8],
  [9],
  [10,11],
  [12],
  [13],
  [14],
  [15],
  [16],
  [17],
  [18,19],
  [20],
  [21,22],
  [23],
  [24],
  [25],
  [26]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>근데 이게 </src>; start=0.00, end=1.00
* W1. <src>시기 적으로 </src>; start=1.00, end=2.00
* W2. <src>결혼 이 뭐 </src>; start=2.00, end=3.00
* W3. <src>했었 으면 </src>; start=3.00, end=4.00
* W4. <src>진작 에 </src>; start=4.00, end=5.00
* W5. <src>가능 했었던 </src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>사람 들이에요. 근데 </src>; start=7.00, end=8.00
* W8. <src>어느 정도 시기 를 좀 </src>; start=8.00, end=9.00
* W9. <src>보고 자기 가 </src>; start=9.00, end=10.00
* W10. <src>벌려 놓은 일이나 </src>; start=10.00, end=11.00
* W11. <src>해야 될 일들이 </src>; start=11.00, end=12.00
* W12. <src>있었기 때문 에 </src>; start=12.00, end=13.00
* W13. <src>그거 를 좀 다 </src>; start=13.00, end=14.00
* W14. <src>좀 </src>; start=14.00, end=14.36
```

---
