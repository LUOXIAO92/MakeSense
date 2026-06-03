=== KO_G1hDgTWHSC8_W000038 ===

status: finished

raw_text:
자기 그림을 그리면서 카피할 때 머리 속에 기억해두고 메모해둔 표현 방법을 그대로 실제 적용하면서 그림을 그립니다. 그러면 그림 그리는 실력이 빠르게 좋아집니다.

word_indices:
* W0. {0: '자기', 1: '그림 을'}
* W1. {2: '그리 면서', 3: '카피할', 4: '때'}
* W2. {5: '머리', 6: '속에'}
* W3. {7: '기억 해두고', 8: '메모 해둔'}
* W4. {9: '표현', 10: '방법 을'}
* W5. {11: '그대로', 12: '실제'}
* W6. {13: '적용 하면서'}
* W7. {14: '그림 을', 15: '그립 니다.'}
* W8. {16: '그러면'}
* W9. {17: '그림', 18: '그리 는', 19: '실력 이'}
* W10. {20: '빠르 게'}
* W11. {21: '좋아집니다.'}

scratchpad:
* W0. {0: '자기', 1: '그림 을'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 자기 그림 을, stable minimal sense unit in the current window: [0,1]

* W1. {2: '그리 면서', 3: '카피할', 4: '때'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그리 면서 카피할 때, stable minimal sense unit in the current window: [2,3,4]

* W2. {5: '머리', 6: '속에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 머리 속에, stable minimal sense unit in the current window: [5,6]

* W3. {7: '기억 해두고', 8: '메모 해둔'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 기억 해두고, stable minimal sense unit in the current window: [7]
    2. 메모 해둔, stable minimal sense unit in the current window: [8]

* W4. {9: '표현', 10: '방법 을'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 표현 방법 을, stable minimal sense unit in the current window: [9,10]

* W5. {11: '그대로', 12: '실제'}
  - carried_over: None
  - defer: '실제' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [12]
  - release_units:
    1. 그대로, stable minimal sense unit in the current window: [11]

* W6. {13: '적용 하면서'}
  - carried_over: {12: '실제'}
  - defer: None
  - release_units:
    1. 실제 적용 하면서, '실제' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13]

* W7. {14: '그림 을', 15: '그립 니다.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그림 을, stable minimal sense unit in the current window: [14]
    2. 그립 니다., stable minimal sense unit in the current window: [15]

* W8. {16: '그러면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그러면, stable minimal sense unit in the current window: [16]

* W9. {17: '그림', 18: '그리 는', 19: '실력 이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그림 그리 는 실력 이, stable minimal sense unit in the current window: [17,18,19]

* W10. {20: '빠르 게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 빠르 게, stable minimal sense unit in the current window: [20]

* W11. {21: '좋아집니다.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 좋아집니다., stable minimal sense unit in the current window: [21]

result:
[
  [0,1],
  [2,3,4],
  [5,6],
  [7],
  [8],
  [9,10],
  [11],
  [12,13],
  [14],
  [15],
  [16],
  [17,18,19],
  [20],
  [21]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>자기 그림 을 </src>; start=0.00, end=1.00
* W1. <src>그리 면서 카피할 때 </src>; start=1.00, end=2.00
* W2. <src>머리 속에 </src>; start=2.00, end=3.00
* W3. <src>기억 해두고 메모 해둔 </src>; start=3.00, end=4.00
* W4. <src>표현 방법 을 </src>; start=4.00, end=5.00
* W5. <src>그대로 </src>; start=5.00, end=6.00
* W6. <src>실제 적용 하면서 </src>; start=6.00, end=7.00
* W7. <src>그림 을 그립 니다. </src>; start=7.00, end=8.00
* W8. <src>그러면 </src>; start=8.00, end=9.00
* W9. <src>그림 그리 는 실력 이 </src>; start=9.00, end=10.00
* W10. <src>빠르 게 </src>; start=10.00, end=11.00
* W11. <src>좋아집니다. </src>; start=11.00, end=11.14
```

---
=== KO_DlMYWhPK1Lg_W000119 ===

status: finished

raw_text:
악인네는 서로 내놔 하니까 그러면 어떻게 서로까지 뜯고 싸움을 해야만이 되는 사람이잖아. 그러면 어떻게 이제 이게 BJ 궁합은 어떻게 한 사람이 어떻게 어?

word_indices:
* W0. {0: '악인네는'}
* W1. {1: '서로', 2: '내놔', 3: '하니까'}
* W2. {4: '그러면'}
* W3. {5: '어떻게'}
* W4. {6: '서로 까지', 7: '뜯고'}
* W5. {8: '싸움 을', 9: '해야 만이', 10: '되는'}
* W6. {11: '사람 이잖아.'}
* W7. {12: '그러면'}
* W8. {13: '어떻게'}
* W9. {14: '이제', 15: '이게', 16: 'BJ'}
* W10. {17: '궁합은', 18: '어떻게'}
* W11. {19: '한', 20: '사람 이', 21: '어떻게', 22: '어?'}
* W12. {}
* W13. {}

scratchpad:
* W0. {0: '악인네는'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 악인네는, stable minimal sense unit in the current window: [0]

* W1. {1: '서로', 2: '내놔', 3: '하니까'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 서로 내놔 하니까, stable minimal sense unit in the current window: [1,2,3]

* W2. {4: '그러면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그러면, stable minimal sense unit in the current window: [4]

* W3. {5: '어떻게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 어떻게, stable minimal sense unit in the current window: [5]

* W4. {6: '서로 까지', 7: '뜯고'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 서로 까지 뜯고, stable minimal sense unit in the current window: [6,7]

* W5. {8: '싸움 을', 9: '해야 만이', 10: '되는'}
  - carried_over: None
  - defer: '되는' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [10]
  - release_units:
    1. 싸움 을, stable minimal sense unit in the current window: [8]
    2. 해야 만이, stable minimal sense unit in the current window: [9]

* W6. {11: '사람 이잖아.'}
  - carried_over: {10: '되는'}
  - defer: None
  - release_units:
    1. 되는 사람 이잖아., '되는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11]

* W7. {12: '그러면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그러면, stable minimal sense unit in the current window: [12]

* W8. {13: '어떻게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 어떻게, stable minimal sense unit in the current window: [13]

* W9. {14: '이제', 15: '이게', 16: 'BJ'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 이제, stable minimal sense unit in the current window: [14]
    2. 이게, stable minimal sense unit in the current window: [15]
    3. BJ, stable minimal sense unit in the current window: [16]

* W10. {17: '궁합은', 18: '어떻게'}
  - carried_over: None
  - defer: '어떻게' does not yet form a stable minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [18]
  - release_units:
    1. 궁합은, stable minimal sense unit in the current window: [17]

* W11. {19: '한', 20: '사람 이', 21: '어떻게', 22: '어?'}
  - carried_over: {18: '어떻게'}
  - defer: None
  - release_units:
    1. 어떻게 한 사람 이, '어떻게' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20]
    2. 어떻게, stable minimal sense unit in the current window: [21]
    3. 어?, stable minimal sense unit in the current window: [22]

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
  [0],
  [1,2,3],
  [4],
  [5],
  [6,7],
  [8],
  [9],
  [10,11],
  [12],
  [13],
  [14],
  [15],
  [16],
  [17],
  [18,19,20],
  [21],
  [22]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>악인네는 </src>; start=0.00, end=1.00
* W1. <src>서로 내놔 하니까 </src>; start=1.00, end=2.00
* W2. <src>그러면 </src>; start=2.00, end=3.00
* W3. <src>어떻게 </src>; start=3.00, end=4.00
* W4. <src>서로 까지 뜯고 </src>; start=4.00, end=5.00
* W5. <src>싸움 을 해야 만이 </src>; start=5.00, end=6.00
* W6. <src>되는 사람 이잖아. </src>; start=6.00, end=7.00
* W7. <src>그러면 </src>; start=7.00, end=8.00
* W8. <src>어떻게 </src>; start=8.00, end=9.00
* W9. <src>이제 이게 BJ </src>; start=9.00, end=10.00
* W10. <src>궁합은 </src>; start=10.00, end=11.00
* W11. <src>어떻게 한 사람 이 어떻게 어? </src>; start=11.00, end=12.00
* W12. <src><|wait|></src>; start=12.00, end=13.00
* W13. <src><|wait|></src>; start=13.00, end=13.12
```

---
=== KO_E7ZEWK_4k08_W000004 ===

status: finished

raw_text:
그러나 하나님의 백성의 믿음은 어떻게 강해질 수 있을까? 엄마, 엄마도 있다. 어떻게 강해질 수 있을까? 볼까요? 둘, 셋.

word_indices:
* W0. {0: '그러나'}
* W1. {1: '하나님 의'}
* W2. {2: '백성 의', 3: '믿음 은'}
* W3. {4: '어떻게'}
* W4. {5: '강해 질', 6: '수'}
* W5. {7: '있을까?'}
* W6. {8: '엄마,', 9: '엄마 도'}
* W7. {10: '있다.'}
* W8. {}
* W9. {11: '어떻게', 12: '강해 질', 13: '수'}
* W10. {14: '있을까?'}
* W11. {15: '볼까요?', 16: '둘,'}
* W12. {17: '셋.'}
* W13. {}

scratchpad:
* W0. {0: '그러나'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그러나, stable minimal sense unit (discourse marker) in the current window: [0]

* W1. {1: '하나님 의'}
  - carried_over: None
  - defer: '하나님 의' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [1]
  - release_units: None

* W2. {2: '백성 의', 3: '믿음 은'}
  - carried_over: {1: '하나님 의'}
  - defer: '믿음 은' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [3]
  - release_units:
    1. 하나님 의 백성 의, '하나님 의' is carried over from the previous window; released here because it is now a stable minimal sense unit: [1,2]

* W3. {4: '어떻게'}
  - carried_over: {3: '믿음 은'}
  - defer: None
  - release_units:
    1. 믿음 은, '믿음 은' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3]
    2. 어떻게, stable minimal sense unit in the current window: [4]

* W4. {5: '강해 질', 6: '수'}
  - carried_over: None
  - defer: '강해 질 수' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [5,6]
  - release_units: None

* W5. {7: '있을까?'}
  - carried_over: {5: '강해 질', 6: '수'}
  - defer: None
  - release_units:
    1. 강해 질 수 있을까?, '강해 질 수' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7]

* W6. {8: '엄마,', 9: '엄마 도'}
  - carried_over: None
  - defer: '엄마 도' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [9]
  - release_units:
    1. 엄마,, stable minimal sense unit in the current window: [8]

* W7. {10: '있다.'}
  - carried_over: {9: '엄마 도'}
  - defer: None
  - release_units:
    1. 엄마 도 있다., '엄마 도' is carried over from the previous window; released here because it is now a stable minimal sense unit: [9,10]

* W8. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W9. {11: '어떻게', 12: '강해 질', 13: '수'}
  - carried_over: None
  - defer: '어떻게 강해 질 수' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [11,12,13]
  - release_units: None

* W10. {14: '있을까?'}
  - carried_over: {11: '어떻게', 12: '강해 질', 13: '수'}
  - defer: None
  - release_units:
    1. 어떻게 강해 질 수 있을까?, '어떻게 강해 질 수' is carried over from the previous window; released here because it is now a stable minimal sense unit: [11,12,13,14]

* W11. {15: '볼까요?', 16: '둘,'}
  - carried_over: None
  - defer: '둘,' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16]
  - release_units:
    1. 볼까요?, stable minimal sense unit in the current window: [15]

* W12. {17: '셋.'}
  - carried_over: {16: '둘,'}
  - defer: None
  - release_units:
    1. 둘, 셋., '둘,' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17]

* W13. {}
  - carried_over: None
  - defer: None
  - release_units: None

result:
[
  [0],
  [1,2],
  [3],
  [4],
  [5,6,7],
  [8],
  [9,10],
  [11,12,13,14],
  [15],
  [16,17]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>그러나 </src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>하나님 의 백성 의 믿음 은 </src>; start=2.00, end=3.00
* W3. <src>어떻게 </src>; start=3.00, end=4.00
* W4. <src><|wait|></src>; start=4.00, end=5.00
* W5. <src>강해 질 수 있을까? </src>; start=5.00, end=6.00
* W6. <src>엄마, </src>; start=6.00, end=7.00
* W7. <src>엄마 도 있다. </src>; start=7.00, end=8.00
* W8. <src><|wait|></src>; start=8.00, end=9.00
* W9. <src><|wait|></src>; start=9.00, end=10.00
* W10. <src>어떻게 강해 질 수 있을까? </src>; start=10.00, end=11.00
* W11. <src>볼까요? </src>; start=11.00, end=12.00
* W12. <src>둘, 셋. </src>; start=12.00, end=13.00
* W13. <src><|wait|></src>; start=13.00, end=13.02
```

---
=== KO_G7RmVIWMrHo_W000018 ===

status: finished

raw_text:
제가 좀 직관적으로 이해하셔야 될 부분의 측면이 있어서 여러분들이 잘 한번 보시고 아주 이렇게 하니까 행이 병합이 되는구나 이렇게 느끼셨으면 좋겠습니다. 말로 하려니까 너무 힘드네요. 자, 그다음 여기는 합계라고 되어 있는 부분은 여기 있는 이 각각의 칸 세 개의 칸을

word_indices:
* W0. {0: '제가', 1: '좀', 2: '직관적으로'}
* W1. {3: '이해 하셔야', 4: '될'}
* W2. {5: '부분 의'}
* W3. {6: '측면 이', 7: '있어서'}
* W4. {8: '여러분 들이', 9: '잘', 10: '한번'}
* W5. {11: '보시고'}
* W6. {12: '아주', 13: '이렇게', 14: '하니까'}
* W7. {15: '행이'}
* W8. {16: '병합이'}
* W9. {17: '되는구나', 18: '이렇게', 19: '느끼 셨으면'}
* W10. {20: '좋겠습니다.', 21: '말로'}
* W11. {22: '하려니까', 23: '너무', 24: '힘드 네요.'}
* W12. {25: '자,'}
* W13. {26: '그다음', 27: '여기 는'}
* W14. {28: '합계 라고', 29: '되어', 30: '있는', 31: '부분 은'}
* W15. {32: '여기', 33: '있는', 34: '이'}
* W16. {35: '각각 의'}
* W17. {36: '칸', 37: '세', 38: '개의'}
* W18. {39: '칸을'}

scratchpad:
* W0. {0: '제가', 1: '좀', 2: '직관적으로'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 제가, stable minimal sense unit: [0]
    2. 좀 직관적으로, stable minimal sense unit: [1,2]

* W1. {3: '이해 하셔야', 4: '될'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 이해 하셔야 될, stable minimal sense unit: [3,4]

* W2. {5: '부분 의'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 부분 의, stable minimal sense unit: [5]

* W3. {6: '측면 이', 7: '있어서'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 측면 이 있어서, stable minimal sense unit: [6,7]

* W4. {8: '여러분 들이', 9: '잘', 10: '한번'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 여러분 들이, stable minimal sense unit: [8]
    2. 잘, stable minimal sense unit: [9]
    3. 한번, stable minimal sense unit: [10]

* W5. {11: '보시고'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 보시고, stable minimal sense unit: [11]

* W6. {12: '아주', 13: '이렇게', 14: '하니까'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 아주, stable minimal sense unit: [12]
    2. 이렇게, stable minimal sense unit: [13]
    3. 하니까, stable minimal sense unit: [14]

* W7. {15: '행이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 행이, stable minimal sense unit: [15]

* W8. {16: '병합이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 병합이, stable minimal sense unit: [16]

* W9. {17: '되는구나', 18: '이렇게', 19: '느끼 셨으면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 되는구나, stable minimal sense unit: [17]
    2. 이렇게, stable minimal sense unit: [18]
    3. 느끼 셨으면, stable minimal sense unit: [19]

* W10. {20: '좋겠습니다.', 21: '말로'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 좋겠습니다., stable minimal sense unit: [20]
    2. 말로, stable minimal sense unit: [21]

* W11. {22: '하려니까', 23: '너무', 24: '힘드 네요.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 하려니까, stable minimal sense unit: [22]
    2. 너무, stable minimal sense unit: [23]
    3. 힘드 네요., stable minimal sense unit: [24]

* W12. {25: '자,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 자,, stable minimal sense unit: [25]

* W13. {26: '그다음', 27: '여기 는'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그다음, stable minimal sense unit: [26]
    2. 여기 는, stable minimal sense unit: [27]

* W14. {28: '합계 라고', 29: '되어', 30: '있는', 31: '부분 은'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 합계 라고 되어 있는, stable minimal sense unit: [28,29,30]
    2. 부분 은, stable minimal sense unit: [31]

* W15. {32: '여기', 33: '있는', 34: '이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 여기 있는 이, stable minimal sense unit: [32,33,34]

* W16. {35: '각각 의'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 각각 의, stable minimal sense unit: [35]

* W17. {36: '칸', 37: '세', 38: '개의'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 칸 세 개의, stable minimal sense unit: [36,37,38]

* W18. {39: '칸을'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 칸을, stable minimal sense unit: [39]

result:
[
  [0],
  [1,2],
  [3,4],
  [5],
  [6,7],
  [8],
  [9],
  [10],
  [11],
  [12],
  [13],
  [14],
  [15],
  [16],
  [17],
  [18],
  [19],
  [20],
  [21],
  [22],
  [23],
  [24],
  [25],
  [26],
  [27],
  [28,29,30],
  [31],
  [32,33,34],
  [35],
  [36,37,38],
  [39]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>제가 좀 직관적으로 </src>; start=0.00, end=1.00
* W1. <src>이해 하셔야 될 </src>; start=1.00, end=2.00
* W2. <src>부분 의 </src>; start=2.00, end=3.00
* W3. <src>측면 이 있어서 </src>; start=3.00, end=4.00
* W4. <src>여러분 들이 잘 한번 </src>; start=4.00, end=5.00
* W5. <src>보시고 </src>; start=5.00, end=6.00
* W6. <src>아주 이렇게 하니까 </src>; start=6.00, end=7.00
* W7. <src>행이 </src>; start=7.00, end=8.00
* W8. <src>병합이 </src>; start=8.00, end=9.00
* W9. <src>되는구나 이렇게 느끼 셨으면 </src>; start=9.00, end=10.00
* W10. <src>좋겠습니다. 말로 </src>; start=10.00, end=11.00
* W11. <src>하려니까 너무 힘드 네요. </src>; start=11.00, end=12.00
* W12. <src>자, </src>; start=12.00, end=13.00
* W13. <src>그다음 여기 는 </src>; start=13.00, end=14.00
* W14. <src>합계 라고 되어 있는 부분 은 </src>; start=14.00, end=15.00
* W15. <src>여기 있는 이 </src>; start=15.00, end=16.00
* W16. <src>각각 의 </src>; start=16.00, end=17.00
* W17. <src>칸 세 개의 </src>; start=17.00, end=18.00
* W18. <src>칸을 </src>; start=18.00, end=18.40
```

---
=== KO_E9GzA6TOlV4_W000007 ===

status: finished

raw_text:
일단 배그는 파밍이 제일 중요합니다, 여러분. 파밍을 열심히 해주세요. 어 발소리 난다. 어 당황한 척하면서 이렇게 파밍해주면 됩니다, 여러분.

word_indices:
* W0. {0: '일단', 1: '배그는', 2: '파밍이'}
* W1. {3: '제일', 4: '중요 합니다,'}
* W2. {5: '여러분.'}
* W3. {6: '파밍을', 7: '열심히'}
* W4. {8: '해주세요.', 9: '어'}
* W5. {10: '발소리', 11: '난다.'}
* W6. {}
* W7. {}
* W8. {12: '어'}
* W9. {13: '당황 한'}
* W10. {14: '척하 면서'}
* W11. {15: '이렇게'}
* W12. {16: '파밍해주면', 17: '됩니다,', 18: '여러분.'}

scratchpad:
* W0. {0: '일단', 1: '배그는', 2: '파밍이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 일단, stable minimal sense unit (discourse marker): [0]
    2. 배그는, stable minimal sense unit (noun+particle): [1]
    3. 파밍이, stable minimal sense unit (noun+particle): [2]

* W1. {3: '제일', 4: '중요 합니다,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 제일 중요 합니다,, stable minimal sense unit (adverb+predicate): [3,4]

* W2. {5: '여러분.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 여러분., stable minimal sense unit (vocative): [5]

* W3. {6: '파밍을', 7: '열심히'}
  - carried_over: None
  - defer: '열심히' does not yet form the best stable unit with the current material; defer it to the next window to combine with the upcoming verb: [7]
  - release_units:
    1. 파밍을, stable minimal sense unit (noun+particle): [6]

* W4. {8: '해주세요.', 9: '어'}
  - carried_over: {7: '열심히'}
  - defer: None
  - release_units:
    1. 열심히 해주세요., '열심히' is carried over from the previous window; released here because it now forms a stable minimal sense unit (adverb+verb): [7,8]
    2. 어, stable minimal sense unit (interjection): [9]

* W5. {10: '발소리', 11: '난다.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 발소리 난다., stable minimal sense unit (noun+predicate): [10,11]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W8. {12: '어'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 어, stable minimal sense unit (interjection); previous window had no output so current window must release: [12]

* W9. {13: '당황 한'}
  - carried_over: None
  - defer: '당황 한' does not yet form a stable minimal sense unit alone; defer it to the next window to combine with '척하면서': [13]
  - release_units: None

* W10. {14: '척하 면서'}
  - carried_over: {13: '당황 한'}
  - defer: None
  - release_units:
    1. 당황 한 척하면서, '당황 한' is carried over from the previous window; released here because it now forms a stable minimal sense unit (adjective+verb combination); previous window had no output so this window must release: [13,14]

* W11. {15: '이렇게'}
  - carried_over: None
  - defer: '이렇게' does not yet form a stable minimal sense unit with the current material; defer it to the next window to combine with the verb: [15]
  - release_units: None

* W12. {16: '파밍해주면', 17: '됩니다,', 18: '여러분.'}
  - carried_over: {15: '이렇게'}
  - defer: None
  - release_units:
    1. 이렇게 파밍해주면, '이렇게' is carried over from the previous window; released here because it now forms a stable minimal sense unit (adverb+conditional predicate): [15,16]
    2. 됩니다,, stable minimal sense unit (predicate): [17]
    3. 여러분., stable minimal sense unit (vocative): [18]

result:
[
  [0],
  [1],
  [2],
  [3,4],
  [5],
  [6],
  [7,8],
  [9],
  [10,11],
  [12],
  [13,14],
  [15,16],
  [17],
  [18]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>일단 배그는 파밍이 </src>; start=0.00, end=1.00
* W1. <src>제일 중요 합니다, </src>; start=1.00, end=2.00
* W2. <src>여러분. </src>; start=2.00, end=3.00
* W3. <src>파밍을 </src>; start=3.00, end=4.00
* W4. <src>열심히 해주세요. 어 </src>; start=4.00, end=5.00
* W5. <src>발소리 난다. </src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>어 </src>; start=8.00, end=9.00
* W9. <src><|wait|></src>; start=9.00, end=10.00
* W10. <src>당황 한 척하 면서 </src>; start=10.00, end=11.00
* W11. <src><|wait|></src>; start=11.00, end=12.00
* W12. <src>이렇게 파밍해주면 됩니다, 여러분. </src>; start=12.00, end=12.73
```

---
=== KO_G3A_RG4qGF4_W000002 ===

status: finished

raw_text:
그리고 아 그리고 우리가 뉴욕에 살고 있으니까 좀 뉴욕과 뉴저지 지역의 유명한 곳을 소개해드릴 수도 있어요. 그렇죠, 그렇죠. 직접 그 현장에 가서 저희들이 이제 체험도 해보고 소개도 해드리고 그런 프로그램도 만들 기획이고요. 어 뉴욕 미니스에 대한 설명을 좀 해주시죠.

word_indices:
* W0. {0: '그리고'}
* W1. {1: '아', 2: '그리고'}
* W2. {3: '우리 가'}
* W3. {4: '뉴욕 에', 5: '살고'}
* W4. {6: '있으니까', 7: '좀', 8: '뉴욕 과'}
* W5. {9: '뉴저지', 10: '지역 의', 11: '유명 한'}
* W6. {12: '곳을', 13: '소개 해드릴', 14: '수도'}
* W7. {15: '있어요.', 16: '그렇 죠,', 17: '그렇 죠.'}
* W8. {18: '직접', 19: '그', 20: '현장 에'}
* W9. {21: '가서'}
* W10. {22: '저희 들이', 23: '이제', 24: '체험 도'}
* W11. {25: '해보고', 26: '소개 도'}
* W12. {27: '해드리고', 28: '그런'}
* W13. {29: '프로그램 도', 30: '만들'}
* W14. {31: '기획 이고요.', 32: '어'}
* W15. {33: '뉴욕'}
* W16. {34: '미니 스에', 35: '대한', 36: '설명 을'}
* W17. {37: '좀', 38: '해주시죠.'}

scratchpad:
* W0. {0: '그리고'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그리고, stable minimal sense unit in the current window: [0]

* W1. {1: '아', 2: '그리고'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 아 그리고, stable minimal sense unit in the current window: [1,2]

* W2. {3: '우리 가'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 우리 가, stable minimal sense unit in the current window: [3]

* W3. {4: '뉴욕 에', 5: '살고'}
  - carried_over: None
  - defer: '살고' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [5]
  - release_units:
    1. 뉴욕 에, stable minimal sense unit in the current window: [4]

* W4. {6: '있으니까', 7: '좀', 8: '뉴욕 과'}
  - carried_over: {5: '살고'}
  - defer: '뉴욕 과' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [8]
  - release_units:
    1. 살고 있으니까, '살고' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6]
    2. 좀, stable minimal sense unit in the current window: [7]

* W5. {9: '뉴저지', 10: '지역 의', 11: '유명 한'}
  - carried_over: {8: '뉴욕 과'}
  - defer: '유명 한' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [11]
  - release_units:
    1. 뉴욕 과 뉴저지 지역 의, '뉴욕 과' is carried over from the previous window; released here because it is now a stable minimal sense unit: [8,9,10]

* W6. {12: '곳을', 13: '소개 해드릴', 14: '수도'}
  - carried_over: {11: '유명 한'}
  - defer: '소개 해드릴 수도' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [13,14]
  - release_units:
    1. 유명 한 곳을, '유명 한' is carried over from the previous window; released here because it is now a stable minimal sense unit: [11,12]

* W7. {15: '있어요.', 16: '그렇 죠,', 17: '그렇 죠.'}
  - carried_over: {13: '소개 해드릴', 14: '수도'}
  - defer: None
  - release_units:
    1. 소개 해드릴 수도 있어요., '소개 해드릴 수도' is carried over from the previous window; released here because it is now a stable minimal sense unit: [13,14,15]
    2. 그렇 죠,, stable minimal sense unit in the current window: [16]
    3. 그렇 죠., stable minimal sense unit in the current window: [17]

* W8. {18: '직접', 19: '그', 20: '현장 에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 직접 그 현장 에, stable minimal sense unit in the current window: [18,19,20]

* W9. {21: '가서'}
  - carried_over: None
  - defer: '가서' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [21]
  - release_units: None

* W10. {22: '저희 들이', 23: '이제', 24: '체험 도'}
  - carried_over: {21: '가서'}
  - defer: '체험 도' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [24]
  - release_units:
    1. 가서 저희 들이, '가서' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22]
    2. 이제, stable minimal sense unit in the current window: [23]

* W11. {25: '해보고', 26: '소개 도'}
  - carried_over: {24: '체험 도'}
  - defer: '소개 도' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [26]
  - release_units:
    1. 체험 도 해보고, '체험 도' is carried over from the previous window; released here because it is now a stable minimal sense unit: [24,25]

* W12. {27: '해드리고', 28: '그런'}
  - carried_over: {26: '소개 도'}
  - defer: '그런' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [28]
  - release_units:
    1. 소개 도 해드리고, '소개 도' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27]

* W13. {29: '프로그램 도', 30: '만들'}
  - carried_over: {28: '그런'}
  - defer: '만들' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [30]
  - release_units:
    1. 그런 프로그램 도, '그런' is carried over from the previous window; released here because it is now a stable minimal sense unit: [28,29]

* W14. {31: '기획 이고요.', 32: '어'}
  - carried_over: {30: '만들'}
  - defer: None
  - release_units:
    1. 만들 기획 이고요., '만들' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31]
    2. 어, stable minimal sense unit in the current window: [32]

* W15. {33: '뉴욕'}
  - carried_over: None
  - defer: '뉴욕' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [33]
  - release_units: None

* W16. {34: '미니 스에', 35: '대한', 36: '설명 을'}
  - carried_over: {33: '뉴욕'}
  - defer: None
  - release_units:
    1. 뉴욕 미니 스에 대한 설명 을, '뉴욕' is carried over from the previous window; released here because it is now a stable minimal sense unit: [33,34,35,36]

* W17. {37: '좀', 38: '해주시죠.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 좀 해주시죠., stable minimal sense unit in the current window: [37,38]

result:
[
  [0],
  [1,2],
  [3],
  [4],
  [5,6],
  [7],
  [8,9,10],
  [11,12],
  [13,14,15],
  [16],
  [17],
  [18,19,20],
  [21,22],
  [23],
  [24,25],
  [26,27],
  [28,29],
  [30,31],
  [32],
  [33,34,35,36],
  [37,38]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>그리고 </src>; start=0.00, end=1.00
* W1. <src>아 그리고 </src>; start=1.00, end=2.00
* W2. <src>우리 가 </src>; start=2.00, end=3.00
* W3. <src>뉴욕 에 </src>; start=3.00, end=4.00
* W4. <src>살고 있으니까 좀 </src>; start=4.00, end=5.00
* W5. <src>뉴욕 과 뉴저지 지역 의 </src>; start=5.00, end=6.00
* W6. <src>유명 한 곳을 </src>; start=6.00, end=7.00
* W7. <src>소개 해드릴 수도 있어요. 그렇 죠, 그렇 죠. </src>; start=7.00, end=8.00
* W8. <src>직접 그 현장 에 </src>; start=8.00, end=9.00
* W9. <src><|wait|></src>; start=9.00, end=10.00
* W10. <src>가서 저희 들이 이제 </src>; start=10.00, end=11.00
* W11. <src>체험 도 해보고 </src>; start=11.00, end=12.00
* W12. <src>소개 도 해드리고 </src>; start=12.00, end=13.00
* W13. <src>그런 프로그램 도 </src>; start=13.00, end=14.00
* W14. <src>만들 기획 이고요. 어 </src>; start=14.00, end=15.00
* W15. <src><|wait|></src>; start=15.00, end=16.00
* W16. <src>뉴욕 미니 스에 대한 설명 을 </src>; start=16.00, end=17.00
* W17. <src>좀 해주시죠. </src>; start=17.00, end=17.74
```

---
=== KO_GxLlh9Eui8c_W000249 ===

status: finished

raw_text:
돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.

word_indices:
* W0. {0: '돌파 하고'}
* W1. {1: '승리 해야', 2: '한다.'}
* W2. {3: '다만', 4: '배도에'}
* W3. {5: '죄까지', 6: '갈', 7: '수'}
* W4. {8: '있으니', 9: '하나님'}
* W5. {10: '앞에서', 11: '늘'}
* W6. {12: '겸손 하라는'}
* W7. {13: '메시지 를', 14: '전하 는'}
* W8. {15: '대신'}
* W9. {16: '진짜', 17: '거듭 난'}
* W10. {18: '성도 도', 19: '진짜'}
* W11. {20: '지옥 에', 21: '아주', 22: '잘'}
* W12. {23: '가니까'}
* W13. {24: '대부분', 25: '지옥'}
* W14. {26: '가니까.'}

scratchpad:
* W0. {0: '돌파 하고'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 돌파 하고, stable minimal sense unit in the current window: [0]

* W1. {1: '승리 해야', 2: '한다.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 승리 해야 한다., stable minimal sense unit in the current window: [1,2]

* W2. {3: '다만', 4: '배도에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 다만, stable minimal sense unit in the current window: [3]
    2. 배도에, stable minimal sense unit in the current window: [4]

* W3. {5: '죄까지', 6: '갈', 7: '수'}
  - carried_over: None
  - defer: '갈 수' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [6,7]
  - release_units:
    1. 죄까지, stable minimal sense unit in the current window: [5]

* W4. {8: '있으니', 9: '하나님'}
  - carried_over: {6: '갈', 7: '수'}
  - defer: None
  - release_units:
    1. 갈 수 있으니, '갈 수' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7,8]
    2. 하나님, stable minimal sense unit in the current window: [9]

* W5. {10: '앞에서', 11: '늘'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 앞에서, stable minimal sense unit in the current window: [10]
    2. 늘, stable minimal sense unit in the current window: [11]

* W6. {12: '겸손 하라는'}
  - carried_over: None
  - defer: '겸손 하라는' does not yet form a stable minimal sense unit; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [12]
  - release_units: None

* W7. {13: '메시지 를', 14: '전하 는'}
  - carried_over: {12: '겸손 하라는'}
  - defer: '전하 는' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [14]
  - release_units:
    1. 겸손 하라는 메시지 를, '겸손 하라는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13]

* W8. {15: '대신'}
  - carried_over: {14: '전하 는'}
  - defer: None
  - release_units:
    1. 전하 는 대신, '전하 는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [14,15]

* W9. {16: '진짜', 17: '거듭 난'}
  - carried_over: None
  - defer: '진짜 거듭 난' does not yet form a stable minimal sense unit; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [16,17]
  - release_units: None

* W10. {18: '성도 도', 19: '진짜'}
  - carried_over: {16: '진짜', 17: '거듭 난'}
  - defer: '진짜' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [19]
  - release_units:
    1. 진짜 거듭 난 성도 도, '진짜 거듭 난' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17,18]

* W11. {20: '지옥 에', 21: '아주', 22: '잘'}
  - carried_over: {19: '진짜'}
  - defer: '아주 잘' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [21,22]
  - release_units:
    1. 진짜 지옥 에, '진짜' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20]

* W12. {23: '가니까'}
  - carried_over: {21: '아주', 22: '잘'}
  - defer: None
  - release_units:
    1. 아주 잘 가니까, '아주' and '잘' are carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22,23]

* W13. {24: '대부분', 25: '지옥'}
  - carried_over: None
  - defer: '지옥' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 대부분, stable minimal sense unit in the current window: [24]

* W14. {26: '가니까.'}
  - carried_over: {25: '지옥'}
  - defer: None
  - release_units:
    1. 지옥 가니까., '지옥' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26]

result:
[
  [0],
  [1,2],
  [3],
  [4],
  [5],
  [6,7,8],
  [9],
  [10],
  [11],
  [12,13],
  [14,15],
  [16,17,18],
  [19,20],
  [21,22,23],
  [24],
  [25,26]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>돌파 하고 </src>; start=0.00, end=1.00
* W1. <src>승리 해야 한다. </src>; start=1.00, end=2.00
* W2. <src>다만 배도에 </src>; start=2.00, end=3.00
* W3. <src>죄까지 </src>; start=3.00, end=4.00
* W4. <src>갈 수 있으니 하나님 </src>; start=4.00, end=5.00
* W5. <src>앞에서 늘 </src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>겸손 하라는 메시지 를 </src>; start=7.00, end=8.00
* W8. <src>전하 는 대신 </src>; start=8.00, end=9.00
* W9. <src><|wait|></src>; start=9.00, end=10.00
* W10. <src>진짜 거듭 난 성도 도 </src>; start=10.00, end=11.00
* W11. <src>진짜 지옥 에 </src>; start=11.00, end=12.00
* W12. <src>아주 잘 가니까 </src>; start=12.00, end=13.00
* W13. <src>대부분 </src>; start=13.00, end=14.00
* W14. <src>지옥 가니까. </src>; start=14.00, end=14.30
```

---
=== KO_G1hDgTWHSC8_W000002 ===

status: finished

raw_text:
유튜브에 그림을 올리는 고수들이나 거리에서 그림을 그리는 사람들을 보면 별로 힘들이지 않고 대충 그려도 보기 좋게 완성되는 것 같은데 나는 언제 좀 저렇게 그림을 그릴 수 있을까 하는 생각을 하게 됩니다.

word_indices:
* W0. {0: '유튜브 에'}
* W1. {1: '그림 을', 2: '올리 는'}
* W2. {3: '고수 들이나'}
* W3. {4: '거리 에서', 5: '그림 을', 6: '그리 는'}
* W4. {7: '사람 들을', 8: '보면'}
* W5. {9: '별로', 10: '힘들 이지'}
* W6. {11: '않고', 12: '대충', 13: '그려 도'}
* W7. {14: '보기', 15: '좋게'}
* W8. {16: '완성 되는', 17: '것', 18: '같은데'}
* W9. {19: '나는', 20: '언제', 21: '좀'}
* W10. {22: '저렇게', 23: '그림 을'}
* W11. {24: '그릴', 25: '수', 26: '있을까', 27: '하는'}
* W12. {28: '생각 을', 29: '하게'}
* W13. {30: '됩니다.'}

scratchpad:
* W0. {0: '유튜브 에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 유튜브 에, stable minimal sense unit (noun + particle): [0]

* W1. {1: '그림 을', 2: '올리 는'}
  - carried_over: None
  - defer: '올리 는' does not yet form a stable minimal sense unit; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [2]
  - release_units:
    1. 그림 을, stable minimal sense unit (noun + particle): [1]

* W2. {3: '고수 들이나'}
  - carried_over: {2: '올리 는'}
  - defer: None
  - release_units:
    1. 올리 는 고수 들이나, '올리 는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3]

* W3. {4: '거리 에서', 5: '그림 을', 6: '그리 는'}
  - carried_over: None
  - defer: '그리 는' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [6]
  - release_units:
    1. 거리 에서, stable minimal sense unit (noun + particle): [4]
    2. 그림 을, stable minimal sense unit (noun + particle): [5]

* W4. {7: '사람 들을', 8: '보면'}
  - carried_over: {6: '그리 는'}
  - defer: None
  - release_units:
    1. 그리 는 사람 들을, '그리 는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7]
    2. 보면, stable minimal sense unit (connective ending): [8]

* W5. {9: '별로', 10: '힘들 이지'}
  - carried_over: None
  - defer: '힘들 이지' does not yet form a stable minimal sense unit; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [10]
  - release_units:
    1. 별로, stable minimal sense unit (adverb): [9]

* W6. {11: '않고', 12: '대충', 13: '그려 도'}
  - carried_over: {10: '힘들 이지'}
  - defer: None
  - release_units:
    1. 힘들 이지 않고, '힘들 이지' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11]
    2. 대충, stable minimal sense unit (adverb): [12]
    3. 그려 도, stable minimal sense unit (connective ending): [13]

* W7. {14: '보기', 15: '좋게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 보기 좋게, stable minimal sense unit (modifier + complement): [14,15]

* W8. {16: '완성 되는', 17: '것', 18: '같은데'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 완성 되는 것 같은데, stable minimal sense unit (predicate-ending chain): [16,17,18]

* W9. {19: '나는', 20: '언제', 21: '좀'}
  - carried_over: None
  - defer: '언제 좀' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [20,21]
  - release_units:
    1. 나는, stable minimal sense unit (noun + particle): [19]

* W10. {22: '저렇게', 23: '그림 을'}
  - carried_over: {20: '언제', 21: '좀'}
  - defer: None
  - release_units:
    1. 언제 좀 저렇게, '언제 좀' is carried over from the previous window; released here because it is now a stable minimal sense unit: [20,21,22]
    2. 그림 을, stable minimal sense unit (noun + particle): [23]

* W11. {24: '그릴', 25: '수', 26: '있을까', 27: '하는'}
  - carried_over: None
  - defer: '하는' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [27]
  - release_units:
    1. 그릴 수 있을까, stable minimal sense unit (predicate-ending chain): [24,25,26]

* W12. {28: '생각 을', 29: '하게'}
  - carried_over: {27: '하는'}
  - defer: '하게' does not yet form a stable minimal sense unit; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [29]
  - release_units:
    1. 하는 생각 을, '하는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28]

* W13. {30: '됩니다.'}
  - carried_over: {29: '하게'}
  - defer: None
  - release_units:
    1. 하게 됩니다., '하게' is carried over from the previous window; released here because it is now a stable minimal sense unit: [29,30]

result:
[
  [0],
  [1],
  [2,3],
  [4],
  [5],
  [6,7],
  [8],
  [9],
  [10,11],
  [12],
  [13],
  [14,15],
  [16,17,18],
  [19],
  [20,21,22],
  [23],
  [24,25,26],
  [27,28],
  [29,30]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '유튜브 에'} - output: release_units 1.{0: '유튜브 에'}
* W1. input: {1: '그림 을', 2: '올리 는'} - output: release_units None
* W2. input: {3: '고수 들이나'} - output: release_units 1.{1: '그림 을', 2: '올리 는', 3: '고수 들이나'}
* W3. input: {4: '거리 에서', 5: '그림 을', 6: '그리 는'} - output: release_units None
* W4. input: {7: '사람 들을', 8: '보면'} - output: release_units 1.{4: '거리 에서', 5: '그림 을', 6: '그리 는', 7: '사람 들을', 8: '보면'} <- ISSUE2: oversized chunk release unit 1 size=5 > 4. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {9: '별로', 10: '힘들 이지'} - output: release_units None
* W6. input: {11: '않고', 12: '대충', 13: '그려 도'} - output: release_units 1.{9: '별로', 10: '힘들 이지', 11: '않고'}; 2.{12: '대충', 13: '그려 도'}
* W7. input: {14: '보기', 15: '좋게'} - output: release_units 1.{14: '보기', 15: '좋게'}
* W8. input: {16: '완성 되는', 17: '것', 18: '같은데'} - output: release_units 1.{16: '완성 되는', 17: '것', 18: '같은데'}
* W9. input: {19: '나는', 20: '언제', 21: '좀'} - output: release_units 1.{19: '나는'}
* W10. input: {22: '저렇게', 23: '그림 을'} - output: release_units 1.{20: '언제', 21: '좀', 22: '저렇게', 23: '그림 을'}
* W11. input: {24: '그릴', 25: '수', 26: '있을까', 27: '하는'} - output: release_units 1.{24: '그릴', 25: '수', 26: '있을까', 27: '하는'}
* W12. input: {28: '생각 을', 29: '하게'} - output: release_units 1.{28: '생각 을', 29: '하게'}
* W13. input: {30: '됩니다.'} - output: release_units 1.{30: '됩니다.'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '유튜브 에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 유튜브 에, stable minimal sense unit in the current window: [0]

* W1. {1: '그림 을', 2: '올리 는'}
  - carried_over: None
  - defer: '그림 을 올리 는' does not yet form a stable release unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [1,2]
  - release_units: None

* W2. {3: '고수 들이나'}
  - carried_over: {1: '그림 을', 2: '올리 는'}
  - defer: None
  - release_units:
    1. 그림을 올리는 고수들이나, '그림 을 올리 는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [1,2,3]

* W3. {4: '거리 에서', 5: '그림 을', 6: '그리 는'}
  - carried_over: None
  - defer: '거리 에서 그림 을 그리 는' does not yet form a stable release unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [4,5,6]
  - release_units: None

* W4. {7: '사람 들을', 8: '보면'}
  - carried_over: {4: '거리 에서', 5: '그림 을', 6: '그리 는'}
  - defer: None
  - release_units:
    1. 거리에서 그림을 그리는 사람들을 보면, '거리 에서 그림 을 그리 는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [4,5,6,7,8]

* W5. {9: '별로', 10: '힘들 이지'}
  - carried_over: None
  - defer: '별로 힘들 이지' does not yet form a stable release unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [9,10]
  - release_units: None

* W6. {11: '않고', 12: '대충', 13: '그려 도'}
  - carried_over: {9: '별로', 10: '힘들 이지'}
  - defer: None
  - release_units:
    1. 별로 힘들이지 않고, '별로 힘들 이지' is carried over from the previous window; released here because it is now a stable minimal sense unit: [9,10,11]
    2. 대충 그려 도, stable minimal sense unit in the current window: [12,13]

* W7. {14: '보기', 15: '좋게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 보기 좋게, stable minimal sense unit in the current window: [14,15]

* W8. {16: '완성 되는', 17: '것', 18: '같은데'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 완성 되는 것 같은데, stable minimal sense unit in the current window: [16,17,18]

* W9. {19: '나는', 20: '언제', 21: '좀'}
  - carried_over: None
  - defer: '언제 좀' does not yet form a stable release unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [20,21]
  - release_units:
    1. 나는, stable minimal sense unit in the current window: [19]

* W10. {22: '저렇게', 23: '그림 을'}
  - carried_over: {20: '언제', 21: '좀'}
  - defer: None
  - release_units:
    1. 언제 좀 저렇게 그림을, '언제 좀' is carried over from the previous window; released here because it is now a stable minimal sense unit: [20,21,22,23]

* W11. {24: '그릴', 25: '수', 26: '있을까', 27: '하는'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그릴 수 있을까 하는, stable minimal sense unit in the current window: [24,25,26,27]

* W12. {28: '생각 을', 29: '하게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 생각 을 하게, stable minimal sense unit in the current window: [28,29]

* W13. {30: '됩니다.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 됩니다., stable minimal sense unit in the current window: [30]
  result:
[
  [0],
  [1,2,3],
  [4,5,6,7,8],
  [9,10,11],
  [12,13],
  [14,15],
  [16,17,18],
  [19],
  [20,21,22,23],
  [24,25,26,27],
  [28,29],
  [30]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '유튜브 에'} - output: release_units 1.{0: '유튜브 에'}
* W1. input: {1: '그림 을', 2: '올리 는'} - output: release_units None
* W2. input: {3: '고수 들이나'} - output: release_units 1.{1: '그림 을', 2: '올리 는', 3: '고수 들이나'}
* W3. input: {4: '거리 에서', 5: '그림 을', 6: '그리 는'} - output: release_units None
* W4. input: {7: '사람 들을', 8: '보면'} - output: release_units 1.{4: '거리 에서', 5: '그림 을', 6: '그리 는', 7: '사람 들을', 8: '보면'} <- ISSUE2: oversized chunk release unit 1 size=5 > 4. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W5. input: {9: '별로', 10: '힘들 이지'} - output: release_units None
* W6. input: {11: '않고', 12: '대충', 13: '그려 도'} - output: release_units 1.{9: '별로', 10: '힘들 이지', 11: '않고'}; 2.{12: '대충', 13: '그려 도'}
* W7. input: {14: '보기', 15: '좋게'} - output: release_units 1.{14: '보기', 15: '좋게'}
* W8. input: {16: '완성 되는', 17: '것', 18: '같은데'} - output: release_units 1.{16: '완성 되는', 17: '것', 18: '같은데'}
* W9. input: {19: '나는', 20: '언제', 21: '좀'} - output: release_units 1.{19: '나는'}
* W10. input: {22: '저렇게', 23: '그림 을'} - output: release_units 1.{20: '언제', 21: '좀', 22: '저렇게', 23: '그림 을'}
* W11. input: {24: '그릴', 25: '수', 26: '있을까', 27: '하는'} - output: release_units 1.{24: '그릴', 25: '수', 26: '있을까', 27: '하는'}
* W12. input: {28: '생각 을', 29: '하게'} - output: release_units 1.{28: '생각 을', 29: '하게'}
* W13. input: {30: '됩니다.'} - output: release_units 1.{30: '됩니다.'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: '유튜브 에'} - output: release_units 1.{0: '유튜브 에'}
* W1. input: {1: '그림 을', 2: '올리 는'} - output: release_units None
* W2. input: {3: '고수 들이나'} - output: release_units 1.{1: '그림 을', 2: '올리 는', 3: '고수 들이나'}
* W3. input: {4: '거리 에서', 5: '그림 을', 6: '그리 는'} - output: release_units 1.{4: '거리 에서', 5: '그림 을', 6: '그리 는'}
* W4. input: {7: '사람 들을', 8: '보면'} - output: release_units 1.{7: '사람 들을', 8: '보면'}
* W5. input: {9: '별로', 10: '힘들 이지'} - output: release_units None
* W6. input: {11: '않고', 12: '대충', 13: '그려 도'} - output: release_units 1.{9: '별로', 10: '힘들 이지', 11: '않고', 12: '대충', 13: '그려 도'} <- ISSUE2: oversized chunk release unit 1 size=5 > 4. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {14: '보기', 15: '좋게'} - output: release_units 1.{14: '보기', 15: '좋게'}
* W8. input: {16: '완성 되는', 17: '것', 18: '같은데'} - output: release_units 1.{16: '완성 되는', 17: '것', 18: '같은데'}
* W9. input: {19: '나는', 20: '언제', 21: '좀'} - output: release_units 1.{19: '나는'}
* W10. input: {22: '저렇게', 23: '그림 을'} - output: release_units None
* W11. input: {24: '그릴', 25: '수', 26: '있을까', 27: '하는'} - output: release_units 1.{20: '언제', 21: '좀', 22: '저렇게', 23: '그림 을', 24: '그릴', 25: '수', 26: '있을까'} <- ISSUE2: oversized chunk release unit 1 size=7 > 4. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W12. input: {28: '생각 을', 29: '하게'} - output: release_units 1.{27: '하는', 28: '생각 을'}
* W13. input: {30: '됩니다.'} - output: release_units 1.{29: '하게', 30: '됩니다.'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: '유튜브 에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 유튜브 에, stable noun+particle minimal sense unit: [0]

* W1. {1: '그림 을', 2: '올리 는'}
  - carried_over: None
  - defer: '그림 을 올리 는' does not yet form the best stable release unit; defer to next window because the previous window had output and delaying by one window is still legal: [1,2]
  - release_units: None

* W2. {3: '고수 들이나'}
  - carried_over: {1: '그림 을', 2: '올리 는'}
  - defer: None
  - release_units:
    1. 그림 을 올리 는 고수 들이나, carried-over material plus new token form a stable minimal sense unit: [1,2,3]

* W3. {4: '거리 에서', 5: '그림 을', 6: '그리 는'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 거리 에서 그림 을 그리 는, stable modifier phrase minimal sense unit: [4,5,6]

* W4. {7: '사람 들을', 8: '보면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 사람 들을 보면, stable noun+connective minimal sense unit: [7,8]

* W5. {9: '별로', 10: '힘들 이지'}
  - carried_over: None
  - defer: '별로 힘들 이지' does not yet form a stable release unit alone; defer to next window because the previous window had output: [9,10]
  - release_units: None

* W6. {11: '않고', 12: '대충', 13: '그려 도'}
  - carried_over: {9: '별로', 10: '힘들 이지'}
  - defer: None
  - release_units:
    1. 별로 힘들 이지 않고 대충 그려 도, carried-over material plus new tokens form a stable adverbial phrase minimal sense unit: [9,10,11,12,13]

* W7. {14: '보기', 15: '좋게'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 보기 좋게, stable adverbial unit: [14,15]

* W8. {16: '완성 되는', 17: '것', 18: '같은데'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 완성 되는 것 같은데, stable predicate ending minimal sense unit: [16,17,18]

* W9. {19: '나는', 20: '언제', 21: '좀'}
  - carried_over: None
  - defer: '언제 좀' does not yet form a stable unit; defer to next window because the previous window had output and only the remainder is deferred after releasing a stable part: [20,21]
  - release_units:
    1. 나는, stable subject minimal sense unit: [19]

* W10. {22: '저렇게', 23: '그림 을'}
  - carried_over: {20: '언제', 21: '좀'}
  - defer: '언제 좀 저렇게 그림 을' does not yet form a stable release unit; defer to next window because the previous window had output: [20,21,22,23]
  - release_units: None

* W11. {24: '그릴', 25: '수', 26: '있을까', 27: '하는'}
  - carried_over: {20: '언제', 21: '좀', 22: '저렇게', 23: '그림 을'}
  - defer: '하는' does not yet form a stable release unit with the current material; defer to next window because only the remainder is deferred after the current window has emitted a stable unit: [27]
  - release_units:
    1. 언제 좀 저렇게 그림 을 그릴 수 있을까, carried-over material plus new tokens form a stable question phrase minimal sense unit: [20,21,22,23,24,25,26]

* W12. {28: '생각 을', 29: '하게'}
  - carried_over: {27: '하는'}
  - defer: '하게' does not yet form a stable release unit; defer to next window because only the remainder is deferred after the current window has emitted a stable unit: [29]
  - release_units:
    1. 하는 생각을, carried-over material plus new token form a stable noun phrase minimal sense unit: [27,28]

* W13. {30: '됩니다.'}
  - carried_over: {29: '하게'}
  - defer: None
  - release_units:
    1. 하게 됩니다, carried-over material plus new token form a stable predicate ending minimal sense unit: [29,30]
  result:
[
  [0],
  [1,2,3],
  [4,5,6],
  [7,8],
  [9,10,11,12,13],
  [14,15],
  [16,17,18],
  [19],
  [20,21,22,23,24,25,26],
  [27,28],
  [29,30]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: '유튜브 에'} - output: release_units 1.{0: '유튜브 에'}
* W1. input: {1: '그림 을', 2: '올리 는'} - output: release_units None
* W2. input: {3: '고수 들이나'} - output: release_units 1.{1: '그림 을', 2: '올리 는', 3: '고수 들이나'}
* W3. input: {4: '거리 에서', 5: '그림 을', 6: '그리 는'} - output: release_units 1.{4: '거리 에서', 5: '그림 을', 6: '그리 는'}
* W4. input: {7: '사람 들을', 8: '보면'} - output: release_units 1.{7: '사람 들을', 8: '보면'}
* W5. input: {9: '별로', 10: '힘들 이지'} - output: release_units None
* W6. input: {11: '않고', 12: '대충', 13: '그려 도'} - output: release_units 1.{9: '별로', 10: '힘들 이지', 11: '않고', 12: '대충', 13: '그려 도'} <- ISSUE2: oversized chunk release unit 1 size=5 > 4. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W7. input: {14: '보기', 15: '좋게'} - output: release_units 1.{14: '보기', 15: '좋게'}
* W8. input: {16: '완성 되는', 17: '것', 18: '같은데'} - output: release_units 1.{16: '완성 되는', 17: '것', 18: '같은데'}
* W9. input: {19: '나는', 20: '언제', 21: '좀'} - output: release_units 1.{19: '나는'}
* W10. input: {22: '저렇게', 23: '그림 을'} - output: release_units None
* W11. input: {24: '그릴', 25: '수', 26: '있을까', 27: '하는'} - output: release_units 1.{20: '언제', 21: '좀', 22: '저렇게', 23: '그림 을', 24: '그릴', 25: '수', 26: '있을까'} <- ISSUE2: oversized chunk release unit 1 size=7 > 4. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W12. input: {28: '생각 을', 29: '하게'} - output: release_units 1.{27: '하는', 28: '생각 을'}
* W13. input: {30: '됩니다.'} - output: release_units 1.{29: '하게', 30: '됩니다.'}

Reconfirm the RULEs and your task!


- retry: 2/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>유튜브 에 </src>; start=0.00, end=1.00
* W1. <src>그림 을 </src>; start=1.00, end=2.00
* W2. <src>올리 는 고수 들이나 </src>; start=2.00, end=3.00
* W3. <src>거리 에서 그림 을 </src>; start=3.00, end=4.00
* W4. <src>그리 는 사람 들을 보면 </src>; start=4.00, end=5.00
* W5. <src>별로 </src>; start=5.00, end=6.00
* W6. <src>힘들 이지 않고 대충 그려 도 </src>; start=6.00, end=7.00
* W7. <src>보기 좋게 </src>; start=7.00, end=8.00
* W8. <src>완성 되는 것 같은데 </src>; start=8.00, end=9.00
* W9. <src>나는 </src>; start=9.00, end=10.00
* W10. <src>언제 좀 저렇게 그림 을 </src>; start=10.00, end=11.00
* W11. <src>그릴 수 있을까 </src>; start=11.00, end=12.00
* W12. <src>하는 생각 을 </src>; start=12.00, end=13.00
* W13. <src>하게 됩니다. </src>; start=13.00, end=13.24
```

---
