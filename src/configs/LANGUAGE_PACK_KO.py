# --- TIME WINDOW PRESSURED SEGMENTATION ---

TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

raw_text: "그러니까 땅을 사기 전에 위에서 언급한 바와 같이 반드시 기본 설계를 한 후 매입하고 또 일단 그 땅이 내 땅이 되면 그 땅을 최대한 활량하는 방법을 찾는 것이 현명할 것입니다."

word_indices:
* W0. {0: '그러니까', 1: '땅을'}
* W1. {2: '사기', 3: '전에'}
* W2. {4: '위에서', 5: '언급한', 6: '바와'}
* W3. {7: '같이'}
* W4. {8: '반드시', 9: '기본', 10: '설계를'}
* W5. {11: '한', 12: '후'}
* W6. {13: '매입하고', 14: '또'}
* W7. {15: '일단', 16: '그'}
* W8. {17: '땅이', 18: '내', 19: '땅이'}
* W9. {20: '되면', 21: '그'}
* W10. {22: '땅을', 23: '최대한'}
* W12. {24: '활량하는', 25: '방법을', 26: '찾는'}
* W13. {27: '것이', 28: '현명할'}
* W14. {29: '것입니다.'}

<scratchpad>
* W0. {0: '그러니까', 1: '땅을'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그러니까, stable minimal sense unit in the current window: [0]
    2. 땅을, stable minimal sense unit in the current window: [1]

* W1. {2: '사기', 3: '전에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 사기 전에, stable minimal sense unit in the current window: [2,3]

* W2. {4: '위에서', 5: '언급한', 6: '바와'}
  - carried_over: None
  - defer: '위에서 언급한 바와' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [4,5,6]
  - release_units: None

* W3. {7: '같이'}
  - carried_over: {4: '위에서', 5: '언급한', 6: '바와'}
  - defer: None
  - release_units:
    1. 위에서 언급한 바와 같이, '위에서 언급한 바와' is carried over from the previous window; released here because it is now a stable minimal sense unit: [4,5,6,7]

* W4. {8: '반드시', 9: '기본', 10: '설계를'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 반드시 기본 설계를, stable minimal sense unit in the current window: [8,9,10]

* W5. {11: '한', 12: '후'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 한 후, stable minimal sense unit in the current window: [11,12]

* W6. {13: '매입하고', 14: '또'}
  - carried_over: None
  - defer: '또' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window: [14]
  - release_units:
    1. 매입하고, stable minimal sense unit in the current window: [13]

* W7. {15: '일단', 16: '그'}
  - carried_over: {14: '또'}
  - defer: '그' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16]
  - release_units:
    1. 또 일단, '또' is carried over from the previous window; released here because it is now a stable minimal sense unit: [14,15]

* W8. {17: '땅이', 18: '내', 19: '땅이'}
  - carried_over: {16: '그'}
  - defer: None
  - release_units:
    1. 그 땅이, '그' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17]
    2. 내 땅이, stable minimal sense unit in the current window: [18,19]

* W9. {20: '되면', 21: '그'}
  - carried_over: None
  - defer: '그' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [21]
  - release_units:
    1. 되면, stable minimal sense unit in the current window: [20]

* W10. {22: '땅을', 23: '최대한'}
  - carried_over: {21: '그'}
  - defer: '최대한' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [23]
  - release_units:
    1. 그 땅을, '그' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22]

* W12. {24: '활량하는', 25: '방법을', 26: '찾는'}
  - carried_over: {23: '최대한'}
  - defer: '찾는' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [26]
  - release_units:
    1. 최대한 활량하는 방법을, '최대한' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25]

* W13. {27: '것이', 28: '현명할'}
  - carried_over: {26: '찾는'}
  - defer: '현명할' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [28]
  - release_units:
    1. 찾는 것이, '찾는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [26,27]

* W14. {29: '것입니다.'}
  - carried_over: {28: '현명할'}
  - defer: None
  - release_units:
    1. 현명할 것입니다., '현명할' is carried over from the previous window; released here because it is now a stable minimal sense unit: [28,29]
</scratchpad>
<result>
[
  [0],
  [1],
  [2,3],
  [4,5,6,7],
  [8,9,10],
  [11,12],
  [13],
  [14,15],
  [16,17],
  [18,19],
  [20],
  [21,22],
  [23,24,25],
  [26,27],
  [28,29]
]
</result>


## Sample 2:

raw_text: "동진료소견서를 살펴보면, 최종 뇌원 당시 항원치료 후 입원치료가 필요한 상태가 아니었음이라고 기지되어 있고, 동병원의사소견서에 의하면 식사량은 좋아졌으며 전신 상태는 호전의 경과를 보여 집으로 귀가했습니다라고 기지되어 있습니다."

word_indices:
* W0. {}
* W1. {0: '동진료소견서를', 1: '살펴보면,'}
* W2. {2: '최종'}
* W3. {3: '뇌원', 4: '당시'}
* W4. {5: '항원치료', 6: '후'}
* W5. {7: '입원치료가'}
* W6. {8: '필요한', 9: '상태가'}
* W7. {10: '아니었음이라고'}
* W8. {11: '기지되어', 12: '있고,'}
* W9. {}
* W10. {13: '동병원의사소견서에', 14: '의하면'}
* W11. {}
* W12. {15: '식사량은', 16: '좋아졌으며'}
* W13. {17: '전신', 18: '상태는'}
* W14. {19: '호전의'}
* W15. {20: '경과를', 21: '보여'}
* W16. {22: '집으로'}
* W17. {23: '귀가했습니다라고', 24: '기지되어'}
* W18. {25: '있습니다.'}

<scratchpad>
* W0. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W1. {0: '동진료소견서를', 1: '살펴보면,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 동진료소견서를 살펴보면,, stable minimal sense unit in the current window: [0,1]

* W2. {2: '최종'}
  - carried_over: None
  - defer: '최종' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [2]
  - release_units: None

* W3. {3: '뇌원', 4: '당시'}
  - carried_over: {2: '최종'}
  - defer: None
  - release_units:
    1. 최종 뇌원 당시, '최종' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4]

* W4. {5: '항원치료', 6: '후'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 항원치료 후, stable minimal sense unit in the current window: [5,6]

* W5. {7: '입원치료가'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 입원치료가, stable minimal sense unit in the current window: [7]

* W6. {8: '필요한', 9: '상태가'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 필요한 상태가, stable minimal sense unit in the current window: [8,9]

* W7. {10: '아니었음이라고'}
  - carried_over: None
  - defer: '아니었음이라고' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [10]
  - release_units: None

* W8. {11: '기지되어', 12: '있고,'}
  - carried_over: {10: '아니었음이라고'}
  - defer: None
  - release_units:
    1. 아니었음이라고 기지되어 있고,, '아니었음이라고' is carried over from the previous window; released here because it is now a stable minimal sense unit: [10,11,12]

* W9. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W10. {13: '동병원의사소견서에', 14: '의하면'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 동병원의사소견서에 의하면, stable minimal sense unit in the current window: [13,14]

* W11. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W12. {15: '식사량은', 16: '좋아졌으며'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 식사량은, stable minimal sense unit in the current window: [15]
    2. 좋아졌으며, stable minimal sense unit in the current window: [16]

* W13. {17: '전신', 18: '상태는'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 전신 상태는, stable minimal sense unit in the current window: [17,18]

* W14. {19: '호전의'}
  - carried_over: None
  - defer: '호전의' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [19]
  - release_units: None

* W15. {20: '경과를', 21: '보여'}
  - carried_over: {19: '호전의'}
  - defer: None
  - release_units:
    1. 호전의 경과를, '호전의' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20]
    2. 보여, stable minimal sense unit in the current window: [21]

* W16. {22: '집으로'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 집으로, stable minimal sense unit in the current window: [22]

* W17. {23: '귀가했습니다라고', 24: '기지되어'}
  - carried_over: None
  - defer: '귀가했습니다라고 기지되어' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [23,24]
  - release_units: None

* W18. {25: '있습니다.'}
  - carried_over: {23: '귀가했습니다라고', 24: '기지되어'}
  - defer: None
  - release_units:
    1. 귀가했습니다라고 기지되어 있습니다., '귀가했습니다라고 기지되어' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25]
</scratchpad>
<result>
[
  [0,1],
  [2,3,4],
  [5,6],
  [7],
  [8,9],
  [10,11,12],
  [13,14],
  [15],
  [16],
  [17,18],
  [19,20],
  [21],
  [22],
  [23,24,25]
]
</result>


## Sample 3:

raw_text: "뉴라이즈 하이브리드의 미션을 규격인 SP4로 중축하는 100% 합성류로 해당 오일에 대한 자세한 내용은 영상 하단 더보기에 있는 작업기에서 확인할 수 있습니다. 신류를 출입합니다. 레벨링 작업을 감안한 용량을 출입하구요. 신료가 잘 들도록 변속을 진행합니다."

word_indices:
* W0. {0: '뉴라이즈', 1: '하이브리드의'}
* W1. {2: '미션을', 3: '규격인'}
* W2. {4: 'SP4로', 5: '중축하는'}
* W3. {6: '100%', 7: '합성류로'}
* W4. {8: '해당', 9: '오일에', 10: '대한'}
* W5. {11: '자세한', 12: '내용은'}
* W6. {13: '영상', 14: '하단'}
* W7. {15: '더보기에', 16: '있는'}
* W8. {17: '작업기에서', 18: '확인할', 19: '수'}
* W9. {}
* W10. {20: '있습니다.', 21: '신류를'}
* W11. {22: '출입합니다.'}
* W12. {23: '레벨링', 24: '작업을', 25: '감안한'}
* W13. {26: '용량을'}
* W14. {}
* W15. {}
* W16. {27: '출입하구요.', 28: '신료가', 29: '잘', 30: '들도록'}
* W17. {31: '변속을'}

<scratchpad>
* W0. {0: '뉴라이즈', 1: '하이브리드의'}
  - carried_over: None
  - defer: '뉴라이즈 하이브리드의' does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0,1]
  - release_units: None

* W1. {2: '미션을', 3: '규격인'}
  - carried_over: {0: '뉴라이즈', 1: '하이브리드의'}
  - defer: '규격인' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [3]
  - release_units:
    1. 뉴라이즈 하이브리드의 미션을, '뉴라이즈 하이브리드의' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2]

* W2. {4: 'SP4로', 5: '중축하는'}
  - carried_over: {3: '규격인'}
  - defer: '중축하는' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [5]
  - release_units:
    1. 규격인 SP4로, '규격인' is carried over from the previous window; released here because it is now a stable minimal sense unit: [3,4]

* W3. {6: '100%', 7: '합성류로'}
  - carried_over: {5: '중축하는'}
  - defer: None
  - release_units:
    1. 중축하는 100% 합성류로, '중축하는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7]

* W4. {8: '해당', 9: '오일에', 10: '대한'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 해당 오일에 대한, stable minimal sense unit in the current window: [8,9,10]

* W5. {11: '자세한', 12: '내용은'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 자세한 내용은, stable minimal sense unit in the current window: [11,12]

* W6. {13: '영상', 14: '하단'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 영상 하단, stable minimal sense unit in the current window: [13,14]

* W7. {15: '더보기에', 16: '있는'}
  - carried_over: None
  - defer: '있는' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [16]
  - release_units:
    1. 더보기에, stable minimal sense unit in the current window: [15]

* W8. {17: '작업기에서', 18: '확인할', 19: '수'}
  - carried_over: {16: '있는'}
  - defer: '확인할 수' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [18,19]
  - release_units:
    1. 있는 작업기에서, '있는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [16,17]

* W9. {}
  - carried_over: {18: '확인할', 19: '수'}
  - defer: '확인할 수' still does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because waiting one more window is still required under the current carry chain: [18,19]
  - release_units: None

* W10. {20: '있습니다.', 21: '신류를'}
  - carried_over: {18: '확인할', 19: '수'}
  - defer: '신류를' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [21]
  - release_units:
    1. 확인할 수 있습니다., '확인할 수' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19,20]

* W11. {22: '출입합니다.'}
  - carried_over: {21: '신류를'}
  - defer: None
  - release_units:
    1. 신류를 출입합니다., '신류를' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22]

* W12. {23: '레벨링', 24: '작업을', 25: '감안한'}
  - carried_over: None
  - defer: '감안한' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [25]
  - release_units:
    1. 레벨링 작업을, stable minimal sense unit in the current window: [23,24]

* W13. {26: '용량을'}
  - carried_over: {25: '감안한'}
  - defer: None
  - release_units:
    1. 감안한 용량을, '감안한' is carried over from the previous window; released here because it is now a stable minimal sense unit: [25,26]

* W14. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W15. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W16. {27: '출입하구요.', 28: '신료가', 29: '잘', 30: '들도록'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 출입하구요., stable minimal sense unit in the current window: [27]
    2. 신료가, stable minimal sense unit in the current window: [28]
    3. 잘 들도록, stable minimal sense unit in the current window: [29,30]

* W17. {31: '변속을'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 변속을, stable minimal sense unit in the current window: [31]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4],
  [5,6,7],
  [8,9,10],
  [11,12],
  [13,14],
  [15],
  [16,17],
  [18,19,20],
  [21,22],
  [23,24],
  [25,26],
  [27],
  [28],
  [29,30],
  [31]
]
</result>


## Sample 4:

raw_text: "그래서, 이 양자 태기를 하라고 말씀을 드리는 거예요. 이해하셨죠? 용약이 500인 이유에 대해서 여러분한테 설명해 드렸습니다. 그 다음에 케이스 같은 경우에는 어느 케이스 써도 문제 없을 정도로 저 발열입니다. 근데,"

word_indices:
* W0. {0: '그래서,', 1: '이'}
* W1. {2: '양자', 3: '태기를', 4: '하라고'}
* W2. {5: '말씀을', 6: '드리는'}
* W3. {7: '거예요.', 8: '이해하셨죠?'}
* W4. {9: '용약이'}
* W5. {10: '500인', 11: '이유에', 12: '대해서'}
* W6. {13: '여러분한테', 14: '설명해'}
* W7. {}
* W8. {15: '드렸습니다.', 16: '그', 17: '다음에'}
* W9. {18: '케이스', 19: '같은', 20: '경우에는'}
* W10. {21: '어느', 22: '케이스', 23: '써도', 24: '문제'}
* W11. {25: '없을', 26: '정도로', 27: '저'}
* W12. {}
* W13. {28: '발열입니다.', 29: '근데,'}

<scratchpad>
* W0. {0: '그래서,', 1: '이'}
  - carried_over: None
  - defer: '이' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [1]
  - release_units:
    1. 그래서,, stable minimal sense unit in the current window: [0]

* W1. {2: '양자', 3: '태기를', 4: '하라고'}
  - carried_over: {1: '이'}
  - defer: None
  - release_units:
    1. 이 양자 태기를, '이' is carried over from the previous window; released here because it is now a stable minimal sense unit: [1,2,3]
    2. 하라고, stable minimal sense unit in the current window: [4]

* W2. {5: '말씀을', 6: '드리는'}
  - carried_over: None
  - defer: '말씀을 드리는' does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [5,6]
  - release_units: None

* W3. {7: '거예요.', 8: '이해하셨죠?'}
  - carried_over: {5: '말씀을', 6: '드리는'}
  - defer: None
  - release_units:
    1. 말씀을 드리는 거예요., '말씀을 드리는' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6,7]
    2. 이해하셨죠?, stable minimal sense unit in the current window: [8]

* W4. {9: '용약이'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 용약이, stable minimal sense unit in the current window: [9]

* W5. {10: '500인', 11: '이유에', 12: '대해서'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 500인 이유에 대해서, stable minimal sense unit in the current window: [10,11,12]

* W6. {13: '여러분한테', 14: '설명해'}
  - carried_over: None
  - defer: '설명해' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [14]
  - release_units:
    1. 여러분한테, stable minimal sense unit in the current window: [13]

* W7. {}
  - carried_over: {14: '설명해'}
  - defer: '설명해' still does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because it is still being carried across windows: [14]
  - release_units: None

* W8. {15: '드렸습니다.', 16: '그', 17: '다음에'}
  - carried_over: {14: '설명해'}
  - defer: None
  - release_units:
    1. 설명해 드렸습니다., '설명해' is carried over from the previous window; released here because it is now a stable minimal sense unit: [14,15]
    2. 그 다음에, stable minimal sense unit in the current window: [16,17]

* W9. {18: '케이스', 19: '같은', 20: '경우에는'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 케이스, stable minimal sense unit in the current window: [18]
    2. 같은 경우에는, stable minimal sense unit in the current window: [19,20]

* W10. {21: '어느', 22: '케이스', 23: '써도', 24: '문제'}
  - carried_over: None
  - defer: '문제' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [24]
  - release_units:
    1. 어느 케이스, stable minimal sense unit in the current window: [21,22]
    2. 써도, stable minimal sense unit in the current window: [23]

* W11. {25: '없을', 26: '정도로', 27: '저'}
  - carried_over: {24: '문제'}
  - defer: '저' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because only the remainder is deferred after the current window has already emitted something: [27]
  - release_units:
    1. 문제, '문제' is carried over from the previous window; released here because it is now a stable minimal sense unit: [24]
    2. 없을 정도로, stable minimal sense unit in the current window: [25,26]

* W12. {}
  - carried_over: {27: '저'}
  - defer: '저' still does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because it is still being carried across windows: [27]
  - release_units: None

* W13. {28: '발열입니다.', 29: '근데,'}
  - carried_over: {27: '저'}
  - defer: None
  - release_units:
    1. 저 발열입니다., '저' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28]
    2. 근데,, stable minimal sense unit in the current window: [29]
</scratchpad>
<result>
[
  [0],
  [1,2,3],
  [4],
  [5,6,7],
  [8],
  [9],
  [10,11,12],
  [13],
  [14,15],
  [16,17],
  [18],
  [19,20],
  [21,22],
  [23],
  [24],
  [25,26],
  [27,28],
  [29]
]
</result>


## Sample 5:

raw_text: "그 프린스턴 신학교에 유학을 왔죠. 그래서 신학 공부를 하는 중에 폐 뼈 폐 겨락을 걸렸습니다. 그래서 할 수 없이 공부를 중단하고,"

word_indices:
* W0. {0: '그'}, 
* W1. {1: '프린스턴', 2: '신학교에'}, 
* W2. {3: '유학을', 4: '왔죠.'}, 
* W3. {5: '그래서'}, 
* W4. {6: '신학', 7: '공부를'}, 
* W5. {8: '하는', 9: '중에'}, 
* W6. {10: '폐', 11: '뼈', 12: '폐'}, 
* W7. {13: '겨락을'}, 
* W8. {}, 
* W9. {14: '걸렸습니다.', 15: '그래서'}, 
* W10. {16: '할', 17: '수', 18: '없이', 19: '공부를'}, 
* W11. {}, 
* W12. {20: '중단하고,'}

<scratchpad>
* W0. {0: '그'}
  - carried_over: None
  - defer: '그' does not yet form a stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [0]
  - release_units: None

* W1. {1: '프린스턴', 2: '신학교에'}
  - carried_over: {0: '그'}
  - defer: None
  - release_units:
    1. 그 프린스턴 신학교에, '그' is carried over from the previous window; released here because it is now a stable minimal sense unit: [0,1,2]

* W2. {3: '유학을', 4: '왔죠.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 유학을, stable minimal sense unit in the current window: [3]
    2. 왔죠., stable minimal sense unit in the current window: [4]

* W3. {5: '그래서'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 그래서, stable minimal sense unit in the current window: [5]

* W4. {6: '신학', 7: '공부를'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 신학 공부를, stable minimal sense unit in the current window: [6,7]

* W5. {8: '하는', 9: '중에'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 하는 중에, stable minimal sense unit in the current window: [8,9]

* W6. {10: '폐', 11: '뼈', 12: '폐'}
  - carried_over: None
  - defer: '폐 뼈 폐' does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because the next window is non-empty and delaying by one window is still legal: [10,11,12]
  - release_units: None

* W7. {13: '겨락을'}
  - carried_over: {10: '폐', 11: '뼈', 12: '폐'}
  - defer: None
  - release_units:
    1. 폐 뼈 폐 겨락을, '폐 뼈 폐' is carried over from the previous window; latency-forced partial release because waiting longer would violate output continuity and this is the smallest locally interpretable fragment available now: [10,11,12,13]

* W8. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W9. {14: '걸렸습니다.', 15: '그래서'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 걸렸습니다., stable minimal sense unit in the current window: [14]
    2. 그래서, stable minimal sense unit in the current window: [15]

* W10. {16: '할', 17: '수', 18: '없이', 19: '공부를'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 할 수 없이, stable minimal sense unit in the current window: [16,17,18]
    2. 공부를, stable minimal sense unit in the current window: [19]

* W11. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W12. {20: '중단하고,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 중단하고,, stable minimal sense unit in the current window: [20]
</scratchpad>
<result>
[
  [0,1,2],
  [3],
  [4],
  [5],
  [6,7],
  [8,9],
  [10,11,12,13],
  [14],
  [15],
  [16,17,18],
  [19],
  [20]
]
</result>
""".lstrip("\n")


# --- PURE TEXT SEGMENTATION ---

PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

token_indices:
{0: '그러니까', 1: '땅을', 2: '사기', 3: '전에', 4: '위에서', 5: '언급한', 6: '바와', 7: '같이', 8: '반드시', 9: '기본', 10: '설계를', 11: '한', 12: '후', 13: '매입하고', 14: '또', 15: '일단', 16: '그', 17: '땅이', 18: '내', 19: '땅이', 20: '되면', 21: '그', 22: '땅을', 23: '최대한', 24: '활량하는', 25: '방법을', 26: '찾는', 27: '것이', 28: '현명할', 29: '것입니다.'}

<scratchpad>
1. 그러니까
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [0]

2. 땅을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [1]

3. 사기 전에
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [2, 3]

4. 위에서 언급한 바와 같이
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [4, 5, 6, 7]

5. 반드시 기본 설계를
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [8, 9, 10]

6. 한 후
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [11, 12]

7. 매입하고
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [13]

8. 또 일단
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [14, 15]

9. 그 땅이
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [16, 17]

10. 내 땅이
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [18, 19]

11. 되면
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [20]

12. 그 땅을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [21, 22]

13. 최대한 활량하는 방법을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [23, 24, 25]

14. 찾는 것이
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [26, 27]

15. 현명할 것입니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [28, 29]
</scratchpad>
<result>
[
  [0],
  [1],
  [2,3],
  [4,5,6,7],
  [8,9,10],
  [11,12],
  [13],
  [14,15],
  [16,17],
  [18,19],
  [20],
  [21,22],
  [23,24,25],
  [26,27],
  [28,29]
]
</result>


## Sample 2:

token_indices:
{0: '동진료소견서를', 1: '살펴보면,', 2: '최종', 3: '뇌원', 4: '당시', 5: '항원치료', 6: '후', 7: '입원치료가', 8: '필요한', 9: '상태가', 10: '아니었음이라고', 11: '기지되어', 12: '있고,', 13: '동병원의사소견서에', 14: '의하면', 15: '식사량은', 16: '좋아졌으며', 17: '전신', 18: '상태는', 19: '호전의', 20: '경과를', 21: '보여', 22: '집으로', 23: '귀가했습니다라고', 24: '기지되어', 25: '있습니다.'}

<scratchpad>
1. 동진료소견서를 살펴보면,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [0, 1]

2. 최종 뇌원 당시
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [2, 3, 4]

3. 항원치료 후
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [5, 6]

4. 입원치료가
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [7]

5. 필요한 상태가
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [8, 9]

6. 아니었음이라고 기지되어 있고,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [10, 11, 12]

7. 동병원의사소견서에 의하면
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [13, 14]

8. 식사량은
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [15]

9. 좋아졌으며
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [16]

10. 전신 상태는
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [17, 18]

11. 호전의 경과를
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [19, 20]

12. 보여
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [21]

13. 집으로
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [22]

14. 귀가했습니다라고 기지되어 있습니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [23, 24, 25]
</scratchpad>
<result>
[
  [0,1],
  [2,3,4],
  [5,6],
  [7],
  [8,9],
  [10,11,12],
  [13,14],
  [15],
  [16],
  [17,18],
  [19,20],
  [21],
  [22],
  [23,24,25]
]
</result>


## Sample 3:

token_indices:
{0: '뉴라이즈', 1: '하이브리드의', 2: '미션을', 3: '규격인', 4: 'SP4로', 5: '중축하는', 6: '100%', 7: '합성류로', 8: '해당', 9: '오일에', 10: '대한', 11: '자세한', 12: '내용은', 13: '영상', 14: '하단', 15: '더보기에', 16: '있는', 17: '작업기에서', 18: '확인할', 19: '수', 20: '있습니다.', 21: '신류를', 22: '출입합니다.', 23: '레벨링', 24: '작업을', 25: '감안한', 26: '용량을', 27: '출입하구요.', 28: '신료가', 29: '잘', 30: '들도록', 31: '변속을'}

<scratchpad>
1. 뉴라이즈 하이브리드의 미션을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [0, 1, 2]

2. 규격인 SP4로
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [3, 4]

3. 중축하는 100% 합성류로
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [5, 6, 7]

4. 해당 오일에 대한
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [8, 9, 10]

5. 자세한 내용은
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [11, 12]

6. 영상 하단
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [13, 14]

7. 더보기에
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [15]

8. 있는 작업기에서
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [16, 17]

9. 확인할 수 있습니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [18, 19, 20]

10. 신류를 출입합니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [21, 22]

11. 레벨링 작업을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [23, 24]

12. 감안한 용량을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [25, 26]

13. 출입하구요.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [27]

14. 신료가
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [28]

15. 잘 들도록
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [29, 30]

16. 변속을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [31]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4],
  [5,6,7],
  [8,9,10],
  [11,12],
  [13,14],
  [15],
  [16,17],
  [18,19,20],
  [21,22],
  [23,24],
  [25,26],
  [27],
  [28],
  [29,30],
  [31]
]
</result>


## Sample 4:

token_indices:
{0: '그래서,', 1: '이', 2: '양자', 3: '태기를', 4: '하라고', 5: '말씀을', 6: '드리는', 7: '거예요.', 8: '이해하셨죠?', 9: '용약이', 10: '500인', 11: '이유에', 12: '대해서', 13: '여러분한테', 14: '설명해', 15: '드렸습니다.', 16: '그', 17: '다음에', 18: '케이스', 19: '같은', 20: '경우에는', 21: '어느', 22: '케이스', 23: '써도', 24: '문제', 25: '없을', 26: '정도로', 27: '저', 28: '발열입니다.', 29: '근데,'}

<scratchpad>
1. 그래서,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [0]

2. 이 양자 태기를
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [1, 2, 3]

3. 하라고
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [4]

4. 말씀을 드리는 거예요.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [5, 6, 7]

5. 이해하셨죠?
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [8]

6. 용약이
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [9]

7. 500인 이유에 대해서
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [10, 11, 12]

8. 여러분한테
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [13]

9. 설명해 드렸습니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [14, 15]

10. 그 다음에
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [16, 17]

11. 케이스
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [18]

12. 같은 경우에는
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [19, 20]

13. 어느 케이스
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [21, 22]

14. 써도
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [23]

15. 문제
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [24]

16. 없을 정도로
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [25, 26]

17. 저 발열입니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [27, 28]

18. 근데,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [29]
</scratchpad>
<result>
[
  [0],
  [1,2,3],
  [4],
  [5,6,7],
  [8],
  [9],
  [10,11,12],
  [13],
  [14,15],
  [16,17],
  [18],
  [19,20],
  [21,22],
  [23],
  [24],
  [25,26],
  [27,28],
  [29]
]
</result>


## Sample 5:

token_indices:
{0: '그', 1: '프린스턴', 2: '신학교에', 3: '유학을', 4: '왔죠.', 5: '그래서', 6: '신학', 7: '공부를', 8: '하는', 9: '중에', 10: '폐', 11: '뼈', 12: '폐', 13: '겨락을', 14: '걸렸습니다.', 15: '그래서', 16: '할', 17: '수', 18: '없이', 19: '공부를', 20: '중단하고,'}

<scratchpad>
1. 그 프린스턴 신학교에
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [0, 1, 2]

2. 유학을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [3]

3. 왔죠.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [4]

4. 그래서
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [5]

5. 신학 공부를
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [6, 7]

6. 하는 중에
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [8, 9]

7. 폐 뼈 폐 겨락을
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [10, 11, 12, 13]

8. 걸렸습니다.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [14]

9. 그래서
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [15]

10. 할 수 없이
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [16, 17, 18]

11. 공부를
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [19]

12. 중단하고,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained Korean local unit
   - sense_unit: [20]
</scratchpad>
<result>
[
  [0,1,2],
  [3],
  [4],
  [5],
  [6,7],
  [8,9],
  [10,11,12,13],
  [14],
  [15],
  [16,17,18],
  [19],
  [20]
]
</result>
""".lstrip("\n")


# --- KOREAN LANGUAGE PACK (Minimal Incremental Patch) ---

GENERAL_LANGUAGE_PACK = """
## KOREAN LANGUAGE PACK (Minimal Incremental Patch)

### Core Bias

Korean should be segmented around **small stable local units**, not around larger sentence-like spans.

### Protect These Units

Prefer not to split the following unless latency pressure forces it:
- **noun / phrase + particle units**
- **eojeol-like local units**
- **connective / conditional / explanatory ending units**
- **predicate-ending chains**
- **polite-ending / sentence-ending chains**
- **compound nouns**
- **proper names**
- **technical terms**
- **modifier + noun units**

### Typical Stable Korean Units

Examples of the kinds of units that should usually stay together:
- noun / phrase + particle units  
  e.g. units like `땅을`, `신학교에`, `유학을`, `식사량은`, `그 땅이`, `내 땅이`

- connective / conditional / explanatory ending units  
  e.g. units like `사기 전에`, `한 후`, `되면`, `의하면`, `없을 정도로`

- predicate / ending chains  
  e.g. units like `설명해 드렸습니다`, `말씀을 드리는 거예요`, `현명할 것입니다`

- compound noun / fixed nominal units  
  e.g. units like `동진료소견서`, `뉴라이즈 하이브리드`, or other compact technical / nominal units

### Do Not Expose Bare Particles or Detached Ending Tails

Avoid releasing these as standalone output unless they are already inside a stable local unit:
- bare particles
- detached connective tails
- detached conditional tails
- detached explanatory tails
- detached polite endings
- fragments taken from the middle of a compound noun

These usually need their local phrase context.

### Allow Small Discourse Units

Korean may release some very small discourse-level units if they already have clear local discourse value.

Typical allowed cases include:
- discourse markers
- turn-opening units
- transition units
- stance-marking units

Examples of the type of unit allowed:
- `그러니까`
- `그래서,`
- `근데,`
- `그 다음에`
- `또 일단`

These are allowed not because they are fully closed, but because they already carry local discourse function.

### Preferred Korean Stability Signals

When deciding whether a local unit is stable enough, prefer units that already contain one of these:
- a noun / phrase with its particle
- an eojeol-like local unit
- a connective / conditional / explanatory ending unit
- a predicate-ending chain
- a compound noun
- a proper name
- a modifier + noun unit
- a small discourse unit with clear local function

### Korean-Specific Failure Modes to Avoid

Do not drift into these bad cuts:
- separating a particle from its host phrase
- splitting inside a predicate-ending chain
- splitting inside a connective / conditional / explanatory ending unit
- splitting a compound noun into fragments
- splitting a modifier away from its noun when they form one tight local unit

Typical bad patterns to avoid are:
- particle stranded by itself
- ending chain split in the middle
- connective tail split off
- compound noun broken into smaller pieces

### Practical Korean Bias

If two candidate cuts are possible, prefer the one that keeps:
- the tighter noun / phrase + particle unit
- the tighter eojeol-like unit
- the tighter connective / conditional / explanatory ending unit
- the tighter predicate-ending chain
- the tighter compound noun
- the tighter modifier + noun unit
- the tighter discourse unit with local meaning
""".lstrip("\n")