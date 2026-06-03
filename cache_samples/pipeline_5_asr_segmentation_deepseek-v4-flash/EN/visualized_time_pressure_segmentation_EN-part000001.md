=== EN_oINupCbfGEo_W000003 ===

status: finished

raw_text:
Images show the surface of Charon is mostly covered by water ice. We saw steep cliffs and a giant canyon near the equator that stretches more than 600 miles. Scientists also found organic materials on its icy surface.

word_indices:
* W0. {0: 'Images', 1: 'show', 2: 'the'}
* W1. {3: 'surface', 4: 'of', 5: 'Charon'}
* W2. {6: 'is', 7: 'mostly', 8: 'covered'}
* W3. {9: 'by', 10: 'water', 11: 'ice.'}
* W4. {12: 'We', 13: 'saw', 14: 'steep'}
* W5. {15: 'cliffs', 16: 'and', 17: 'a'}
* W6. {18: 'giant', 19: 'canyon'}
* W7. {20: 'near', 21: 'the', 22: 'equator', 23: 'that'}
* W8. {24: 'stretches', 25: 'more', 26: 'than', 27: '600'}
* W9. {28: 'miles.'}
* W10. {29: 'Scientists'}
* W11. {30: 'also', 31: 'found', 32: 'organic'}
* W12. {33: 'materials', 34: 'on', 35: 'its'}
* W13. {36: 'icy', 37: 'surface.'}
* W14. {}

scratchpad:
* W0. {0: 'Images', 1: 'show', 2: 'the'}
  - carried_over: None
  - defer: 'the' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [2]
  - release_units:
    1. Images show, stable minimal sense unit in the current window: [0,1]

* W1. {3: 'surface', 4: 'of', 5: 'Charon'}
  - carried_over: {2: 'the'}
  - defer: None
  - release_units:
    1. the surface of Charon, 'the' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3,4,5]

* W2. {6: 'is', 7: 'mostly', 8: 'covered'}
  - carried_over: None
  - defer: None
  - release_units:
    1. is mostly covered, stable minimal sense unit in the current window: [6,7,8]

* W3. {9: 'by', 10: 'water', 11: 'ice.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. by water ice., stable minimal sense unit in the current window: [9,10,11]

* W4. {12: 'We', 13: 'saw', 14: 'steep'}
  - carried_over: None
  - defer: 'steep' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [14]
  - release_units:
    1. We saw, stable minimal sense unit in the current window: [12,13]

* W5. {15: 'cliffs', 16: 'and', 17: 'a'}
  - carried_over: {14: 'steep'}
  - defer: 'a' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [17]
  - release_units:
    1. steep cliffs and, 'steep' is carried over from the previous window; released here because it is now a stable minimal sense unit: [14,15,16]

* W6. {18: 'giant', 19: 'canyon'}
  - carried_over: {17: 'a'}
  - defer: None
  - release_units:
    1. a giant canyon, 'a' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19]

* W7. {20: 'near', 21: 'the', 22: 'equator', 23: 'that'}
  - carried_over: None
  - defer: None
  - release_units:
    1. near the equator, stable minimal sense unit in the current window: [20,21,22]
    2. that, latency-forced partial release; 'that' is a bare function word that would ideally be grouped with the following clause, but releasing it now prevents a no-output gap while also allowing the remaining clause to form normally later without forcing an large early split: [23]

* W8. {24: 'stretches', 25: 'more', 26: 'than', 27: '600'}
  - carried_over: None
  - defer: '600' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [27]
  - release_units:
    1. stretches more than, stable minimal sense unit in the current window: [24,25,26]

* W9. {28: 'miles.'}
  - carried_over: {27: '600'}
  - defer: None
  - release_units:
    1. 600 miles., '600' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28]

* W10. {29: 'Scientists'}
  - carried_over: None
  - defer: None
  - release_units:
    1. Scientists, latency-forced partial release; this is a single token and not a stable minimal sense unit by itself, but releasing it now is better than causing a no-output gap, since it will be followed immediately by a verb phrase in the next window: [29]

* W11. {30: 'also', 31: 'found', 32: 'organic'}
  - carried_over: None
  - defer: 'organic' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [32]
  - release_units:
    1. also found, stable minimal sense unit in the current window: [30,31]

* W12. {33: 'materials', 34: 'on', 35: 'its'}
  - carried_over: {32: 'organic'}
  - defer: 'on its' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [34,35]
  - release_units:
    1. organic materials, 'organic' is carried over from the previous window; released here because it is now a stable minimal sense unit: [32,33]

* W13. {36: 'icy', 37: 'surface.'}
  - carried_over: {34: 'on', 35: 'its'}
  - defer: None
  - release_units:
    1. on its icy surface., 'on its' is carried over from the previous window; released here because it is now a stable minimal sense unit: [34,35,36,37]

* W14. {}
  - carried_over: None
  - defer: None
  - release_units: None

result:
[
  [0,1],
  [2,3,4,5],
  [6,7,8],
  [9,10,11],
  [12,13],
  [14,15,16],
  [17,18,19],
  [20,21,22],
  [23],
  [24,25,26],
  [27,28],
  [29],
  [30,31],
  [32,33],
  [34,35,36,37]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>Images show </src>; start=0.00, end=1.00
* W1. <src>the surface of Charon </src>; start=1.00, end=2.00
* W2. <src>is mostly covered </src>; start=2.00, end=3.00
* W3. <src>by water ice. </src>; start=3.00, end=4.00
* W4. <src>We saw </src>; start=4.00, end=5.00
* W5. <src>steep cliffs and </src>; start=5.00, end=6.00
* W6. <src>a giant canyon </src>; start=6.00, end=7.00
* W7. <src>near the equator that </src>; start=7.00, end=8.00
* W8. <src>stretches more than </src>; start=8.00, end=9.00
* W9. <src>600 miles. </src>; start=9.00, end=10.00
* W10. <src>Scientists </src>; start=10.00, end=11.00
* W11. <src>also found </src>; start=11.00, end=12.00
* W12. <src>organic materials </src>; start=12.00, end=13.00
* W13. <src>on its icy surface. </src>; start=13.00, end=14.00
* W14. <src><|wait|></src>; start=14.00, end=14.01
```

---
=== EN_oxvGebm2jXu_W000008 ===

status: finished

raw_text:
Harvard Business School professor Laura Huang has also done quite a bit of research when it comes to our "quote unquote" gut instincts, and she discusses the results in her book *Edge: Turning Adversity into Advantage*. She explains how these instincts can lead to some terrible decisions in both work and normal life.

word_indices:
* W0. {0: 'Harvard', 1: 'Business', 2: 'School'}
* W1. {3: 'professor', 4: 'Laura'}
* W2. {5: 'Huang', 6: 'has', 7: 'also'}
* W3. {8: 'done', 9: 'quite', 10: 'a', 11: 'bit', 12: 'of'}
* W4. {13: 'research', 14: 'when', 15: 'it', 16: 'comes', 17: 'to', 18: 'our"'}
* W5. {19: 'quote', 20: 'unquote"', 21: 'gut'}
* W6. {22: 'instincts,', 23: 'and'}
* W7. {24: 'she', 25: 'discusses', 26: 'the'}
* W8. {27: 'results', 28: 'in', 29: 'her'}
* W9. {30: 'book*', 31: 'Edge:'}
* W10. {32: 'Turning'}
* W11. {33: 'Adversity', 34: 'into'}
* W12. {35: 'Advantage*.', 36: 'She'}
* W13. {37: 'explains', 38: 'how', 39: 'these'}
* W14. {40: 'instincts', 41: 'can', 42: 'lead', 43: 'to'}
* W15. {44: 'some', 45: 'terrible', 46: 'decisions'}
* W16. {47: 'in', 48: 'both', 49: 'work'}
* W17. {50: 'and', 51: 'normal'}
* W18. {52: 'life.'}

scratchpad:
* W0. {0: 'Harvard', 1: 'Business', 2: 'School'}
  - carried_over: None
  - defer: None
  - release_units:
    1. Harvard Business School, stable minimal sense unit (compact noun phrase): [0,1,2]

* W1. {3: 'professor', 4: 'Laura'}
  - carried_over: None
  - defer: 'professor Laura' does not yet form the best stable minimal sense unit; deferring to combine with 'Huang' from next window to form a tighter name unit: [3,4]
  - release_units: None

* W2. {5: 'Huang', 6: 'has', 7: 'also'}
  - carried_over: {3: 'professor', 4: 'Laura'}
  - defer: 'has also' does not yet form a stable minimal sense unit; defer to next window to combine with 'done': [6,7]
  - release_units:
    1. professor Laura Huang, carried_over from previous window combined with new token: [3,4,5]

* W3. {8: 'done', 9: 'quite', 10: 'a', 11: 'bit', 12: 'of'}
  - carried_over: {6: 'has', 7: 'also'}
  - defer: None
  - release_units:
    1. has also done, carried_over + new token: [6,7,8]
    2. quite a bit of, stable collocation (fixed phrase): [9,10,11,12]

* W4. {13: 'research', 14: 'when', 15: 'it', 16: 'comes', 17: 'to', 18: 'our"'}
  - carried_over: None
  - defer: 'our"' does not yet form a stable minimal sense unit; defer to next window to combine with the quote phrase: [18]
  - release_units:
    1. research, minimal sense unit (content word): [13]
    2. when it comes to, stable fixed phrase: [14,15,16,17]

* W5. {19: 'quote', 20: 'unquote"', 21: 'gut'}
  - carried_over: {18: 'our"'}
  - defer: 'our quote unquote gut' does not yet form a stable minimal sense unit; defer to next window to combine with 'instincts' for a compact noun-centered frame: [18,19,20,21]
  - release_units: None

* W6. {22: 'instincts,', 23: 'and'}
  - carried_over: {18: 'our"', 19: 'quote', 20: 'unquote"', 21: 'gut'}
  - defer: 'and' does not yet form a stable minimal sense unit; defer to next window: [23]
  - release_units:
    1. our quote unquote gut instincts,, carried_over + new token: [18,19,20,21,22]

* W7. {24: 'she', 25: 'discusses', 26: 'the'}
  - carried_over: {23: 'and'}
  - defer: 'the' does not yet form a stable minimal sense unit; defer to next window to combine with 'results': [26]
  - release_units:
    1. and she discusses, carried_over + new tokens: [23,24,25]

* W8. {27: 'results', 28: 'in', 29: 'her'}
  - carried_over: {26: 'the'}
  - defer: 'in her' does not yet form a stable minimal sense unit; defer to next window to combine with 'book*': [28,29]
  - release_units:
    1. the results, carried_over + new token: [26,27]

* W9. {30: 'book*', 31: 'Edge:'}
  - carried_over: {28: 'in', 29: 'her'}
  - defer: None
  - release_units:
    1. in her book* Edge:, carried_over + new tokens: [28,29,30,31]

* W10. {32: 'Turning'}
  - carried_over: None
  - defer: 'Turning' does not yet form a stable minimal sense unit; defer to next window to combine with 'Adversity' and 'into': [32]
  - release_units: None

* W11. {33: 'Adversity', 34: 'into'}
  - carried_over: {32: 'Turning'}
  - defer: None
  - release_units:
    1. Turning Adversity into, carried_over + new tokens; latency-forced partial release because prior window had no output and a fuller continuation exists next: [32,33,34]

* W12. {35: 'Advantage*.', 36: 'She'}
  - carried_over: None
  - defer: 'She' does not yet form a stable minimal sense unit; defer to next window to combine with 'explains': [36]
  - release_units:
    1. Advantage*., stable minimal sense unit (book title end): [35]

* W13. {37: 'explains', 38: 'how', 39: 'these'}
  - carried_over: {36: 'She'}
  - defer: 'these' does not yet form a stable minimal sense unit; defer to next window to combine with 'instincts': [39]
  - release_units:
    1. She explains how, carried_over + new tokens: [36,37,38]

* W14. {40: 'instincts', 41: 'can', 42: 'lead', 43: 'to'}
  - carried_over: {39: 'these'}
  - defer: None
  - release_units:
    1. these instincts, carried_over + new token: [39,40]
    2. can lead to, stable verb phrase: [41,42,43]

* W15. {44: 'some', 45: 'terrible', 46: 'decisions'}
  - carried_over: None
  - defer: None
  - release_units:
    1. some terrible decisions, stable noun phrase: [44,45,46]

* W16. {47: 'in', 48: 'both', 49: 'work'}
  - carried_over: None
  - defer: 'in both work' does not yet form a stable minimal sense unit; defer to next window to combine with 'and' and 'normal': [47,48,49]
  - release_units: None

* W17. {50: 'and', 51: 'normal'}
  - carried_over: {47: 'in', 48: 'both', 49: 'work'}
  - defer: 'normal' does not yet form a stable minimal sense unit; defer to next window to combine with 'life.': [51]
  - release_units:
    1. in both work and, carried_over + new token; latency-forced partial release because prior window had no output: [47,48,49,50]

* W18. {52: 'life.'}
  - carried_over: {51: 'normal'}
  - defer: None
  - release_units:
    1. normal life., carried_over + new token: [51,52]

result:
[
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11,12],
  [13],
  [14,15,16,17],
  [18,19,20,21,22],
  [23,24,25],
  [26,27],
  [28,29,30,31],
  [32,33,34],
  [35],
  [36,37,38],
  [39,40],
  [41,42,43],
  [44,45,46],
  [47,48,49,50],
  [51,52]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>Harvard Business School </src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>professor Laura Huang </src>; start=2.00, end=3.00
* W3. <src>has also done quite a bit of </src>; start=3.00, end=4.00
* W4. <src>research when it comes to </src>; start=4.00, end=5.00
* W5. <src><|wait|></src>; start=5.00, end=6.00
* W6. <src>our" quote unquote" gut instincts, </src>; start=6.00, end=7.00
* W7. <src>and she discusses </src>; start=7.00, end=8.00
* W8. <src>the results </src>; start=8.00, end=9.00
* W9. <src>in her book* Edge: </src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=11.00
* W11. <src>Turning Adversity into </src>; start=11.00, end=12.00
* W12. <src>Advantage*. </src>; start=12.00, end=13.00
* W13. <src>She explains how </src>; start=13.00, end=14.00
* W14. <src>these instincts can lead to </src>; start=14.00, end=15.00
* W15. <src>some terrible decisions </src>; start=15.00, end=16.00
* W16. <src><|wait|></src>; start=16.00, end=17.00
* W17. <src>in both work and </src>; start=17.00, end=18.00
* W18. <src>normal life. </src>; start=18.00, end=18.33
```

---
=== EN_B00016_S00442_W000017 ===

status: finished

raw_text:
This here returned undefined, and so then the second one got returned. While here, in this one, this value was 20, and so it is this 20 that immediately got returned.

word_indices:
* W0. {0: 'This', 1: 'here', 2: 'returned'}
* W1. {3: 'undefined,', 4: 'and', 5: 'so'}
* W2. {6: 'then', 7: 'the', 8: 'second', 9: 'one'}
* W3. {10: 'got', 11: 'returned.'}
* W4. {12: 'While', 13: 'here,', 14: 'in'}
* W5. {15: 'this', 16: 'one,'}
* W6. {17: 'this', 18: 'value', 19: 'was'}
* W7. {20: '20,', 21: 'and'}
* W8. {22: 'so', 23: 'it', 24: 'is', 25: 'this'}
* W9. {26: '20', 27: 'that', 28: 'immediately'}
* W10. {29: 'got', 30: 'returned.'}

scratchpad:
* W0. {0: 'This', 1: 'here', 2: 'returned'}
  - carried_over: None
  - defer: 'returned' does not yet form a stable minimal sense unit with the current material; it likely pairs with 'undefined,' in the next window: [2]
  - release_units:
    1. This here, stable compact noun phrase: [0,1]

* W1. {3: 'undefined,', 4: 'and', 5: 'so'}
  - carried_over: {2: 'returned'}
  - defer: None
  - release_units:
    1. returned undefined,, 'returned' carried over; verb + complement forms a stable minimal sense unit: [2,3]
    2. and so, stable discourse connective: [4,5]

* W2. {6: 'then', 7: 'the', 8: 'second', 9: 'one'}
  - carried_over: None
  - defer: None
  - release_units:
    1. then the second one, stable noun phrase with lead-in: [6,7,8,9]

* W3. {10: 'got', 11: 'returned.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. got returned., stable verb phrase: [10,11]

* W4. {12: 'While', 13: 'here,', 14: 'in'}
  - carried_over: None
  - defer: 'in' is a preposition that expects a following object; defer it to the next window: [14]
  - release_units:
    1. While here,, stable lead-in frame: [12,13]

* W5. {15: 'this', 16: 'one,'}
  - carried_over: {14: 'in'}
  - defer: None
  - release_units:
    1. in this one,, 'in' carried over; complete prepositional phrase: [14,15,16]

* W6. {17: 'this', 18: 'value', 19: 'was'}
  - carried_over: None
  - defer: None
  - release_units:
    1. this value was, compact subject‑copula frame: [17,18,19]

* W7. {20: '20,', 21: 'and'}
  - carried_over: None
  - defer: 'and' is a bare connector; defer it to next window to pair with 'so': [21]
  - release_units:
    1. 20,, stable numeric value: [20]

* W8. {22: 'so', 23: 'it', 24: 'is', 25: 'this'}
  - carried_over: {21: 'and'}
  - defer: None
  - release_units:
    1. and so it is this, 'and' carried over; lead-in frame now stable: [21,22,23,24,25]

* W9. {26: '20', 27: 'that', 28: 'immediately'}
  - carried_over: None
  - defer: '20 that immediately' is not yet a stable release unit; defer whole chunk to next window to form the relative clause: [26,27,28]
  - release_units: None

* W10. {29: 'got', 30: 'returned.'}
  - carried_over: {26: '20', 27: 'that', 28: 'immediately'}
  - defer: None
  - release_units:
    1. 20 that immediately got returned., carried-over forms a complete relative clause: [26,27,28,29,30]

result:
[
  [0,1],
  [2,3],
  [4,5],
  [6,7,8,9],
  [10,11],
  [12,13],
  [14,15,16],
  [17,18,19],
  [20],
  [21,22,23,24,25],
  [26,27,28,29,30]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>This here </src>; start=0.00, end=1.00
* W1. <src>returned undefined, and so </src>; start=1.00, end=2.00
* W2. <src>then the second one </src>; start=2.00, end=3.00
* W3. <src>got returned. </src>; start=3.00, end=4.00
* W4. <src>While here, </src>; start=4.00, end=5.00
* W5. <src>in this one, </src>; start=5.00, end=6.00
* W6. <src>this value was </src>; start=6.00, end=7.00
* W7. <src>20, </src>; start=7.00, end=8.00
* W8. <src>and so it is this </src>; start=8.00, end=9.00
* W9. <src><|wait|></src>; start=9.00, end=10.00
* W10. <src>20 that immediately got returned. </src>; start=10.00, end=10.65
```

---
=== EN_B00016_S00602_W000000 ===

status: finished

raw_text:
My grandfather was a World War II aviator, and my great uncle was an Air Force pilot who was shot down over Vietnam and spent five years in the Hanoi Hilton with John McCain and.

word_indices:
* W0. {0: 'My', 1: 'grandfather', 2: 'was', 3: 'a'}
* W1. {4: 'World', 5: 'War', 6: 'II'}
* W2. {7: 'aviator,', 8: 'and', 9: 'my'}
* W3. {10: 'great', 11: 'uncle'}
* W4. {12: 'was', 13: 'an'}
* W5. {14: 'Air', 15: 'Force', 16: 'pilot', 17: 'who', 18: 'was'}
* W6. {19: 'shot', 20: 'down'}
* W7. {21: 'over', 22: 'Vietnam'}
* W8. {23: 'and', 24: 'spent', 25: 'five'}
* W9. {26: 'years', 27: 'in', 28: 'the', 29: 'Hanoi'}
* W10. {30: 'Hilton', 31: 'with', 32: 'John'}
* W11. {33: 'McCain', 34: 'and.'}
* W12. {}

scratchpad:
* W0. {0: 'My', 1: 'grandfather', 2: 'was', 3: 'a'}
  - carried_over: None
  - defer: 'a' does not yet form a stable unit with the preceding; defer it to the next window: [3]
  - release_units:
    1. My grandfather was, stable minimal sense unit in the current window: [0,1,2]

* W1. {4: 'World', 5: 'War', 6: 'II'}
  - carried_over: {3: 'a'}
  - defer: 'World War II' does not yet form a stable minimal sense unit with the carried 'a'; defer the current tokens to the next window: [4,5,6]
  - release_units: None

* W2. {7: 'aviator,', 8: 'and', 9: 'my'}
  - carried_over: {3: 'a', 4: 'World', 5: 'War', 6: 'II'}
  - defer: 'and my' does not yet form a stable unit; defer to the next window: [8,9]
  - release_units:
    1. a World War II aviator,, carried over from previous window; released here because it now forms a stable noun phrase: [3,4,5,6,7]

* W3. {10: 'great', 11: 'uncle'}
  - carried_over: {8: 'and', 9: 'my'}
  - defer: None
  - release_units:
    1. and my great uncle, carried over from previous window; stable minimal sense unit: [8,9,10,11]

* W4. {12: 'was', 13: 'an'}
  - carried_over: None
  - defer: 'was an' does not yet form a stable unit; defer to the next window: [12,13]
  - release_units: None

* W5. {14: 'Air', 15: 'Force', 16: 'pilot', 17: 'who', 18: 'was'}
  - carried_over: {12: 'was', 13: 'an'}
  - defer: 'who was' does not yet form a stable unit; defer to the next window: [17,18]
  - release_units:
    1. was an Air Force pilot, carried over from previous window; stable verb phrase: [12,13,14,15,16]

* W6. {19: 'shot', 20: 'down'}
  - carried_over: {17: 'who', 18: 'was'}
  - defer: None
  - release_units:
    1. who was shot down, carried over from previous window; stable phrasal verb unit: [17,18,19,20]

* W7. {21: 'over', 22: 'Vietnam'}
  - carried_over: None
  - defer: None
  - release_units:
    1. over Vietnam, stable prepositional phrase: [21,22]

* W8. {23: 'and', 24: 'spent', 25: 'five'}
  - carried_over: None
  - defer: 'and spent five' does not yet form a stable unit; defer to the next window: [23,24,25]
  - release_units: None

* W9. {26: 'years', 27: 'in', 28: 'the', 29: 'Hanoi'}
  - carried_over: {23: 'and', 24: 'spent', 25: 'five'}
  - defer: 'in the Hanoi' does not yet form a stable unit; defer to the next window: [27,28,29]
  - release_units:
    1. and spent five years, carried over from previous window; stable verb phrase: [23,24,25,26]

* W10. {30: 'Hilton', 31: 'with', 32: 'John'}
  - carried_over: {27: 'in', 28: 'the', 29: 'Hanoi'}
  - defer: 'with John' does not yet form a stable unit; defer to the next window: [31,32]
  - release_units:
    1. in the Hanoi Hilton, carried over from previous window; stable prepositional phrase: [27,28,29,30]

* W11. {33: 'McCain', 34: 'and.'}
  - carried_over: {31: 'with', 32: 'John'}
  - defer: None (end of stream)
  - release_units:
    1. with John McCain, carried over from previous window; stable prepositional phrase: [31,32,33]
    2. and., end-of-stream fragment: [34]

* W12. {}
  - carried_over: None
  - defer: None
  - release_units: None

result:
[
  [0,1,2],
  [3,4,5,6,7],
  [8,9,10,11],
  [12,13,14,15,16],
  [17,18,19,20],
  [21,22],
  [23,24,25,26],
  [27,28,29,30],
  [31,32,33],
  [34]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>My grandfather was </src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>a World War II aviator, </src>; start=2.00, end=3.00
* W3. <src>and my great uncle </src>; start=3.00, end=4.00
* W4. <src><|wait|></src>; start=4.00, end=5.00
* W5. <src>was an Air Force pilot </src>; start=5.00, end=6.00
* W6. <src>who was shot down </src>; start=6.00, end=7.00
* W7. <src>over Vietnam </src>; start=7.00, end=8.00
* W8. <src><|wait|></src>; start=8.00, end=9.00
* W9. <src>and spent five years </src>; start=9.00, end=10.00
* W10. <src>in the Hanoi Hilton </src>; start=10.00, end=11.00
* W11. <src>with John McCain and. </src>; start=11.00, end=12.00
* W12. <src><|wait|></src>; start=12.00, end=12.03
```

---
