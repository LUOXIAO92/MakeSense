=== EN_nvdVVhi8VpA_W000110 ===

status: finished

raw_text:
Um, 42% of the way through the course, so as you can see, each pie slice represents a different topic, and they have a little bit more to learn in in matter, and a little bit more in atoms and ions and molecules. But you know, so this is telling you that.

word_indices:
* W0. {0: 'Um,'}
* W1. {1: '42%', 2: 'of', 3: 'the', 4: 'way', 5: 'through', 6: 'the'}
* W2. {7: 'course,', 8: 'so', 9: 'as', 10: 'you'}
* W3. {11: 'can', 12: 'see,', 13: 'each'}
* W4. {14: 'pie', 15: 'slice'}
* W5. {16: 'represents', 17: 'a', 18: 'different'}
* W6. {19: 'topic,', 20: 'and'}
* W7. {}
* W8. {21: 'they', 22: 'have', 23: 'a', 24: 'little', 25: 'bit', 26: 'more', 27: 'to'}
* W9. {28: 'learn', 29: 'in', 30: 'in'}
* W10. {31: 'matter,', 32: 'and', 33: 'a', 34: 'little'}
* W11. {35: 'bit', 36: 'more', 37: 'in', 38: 'atoms', 39: 'and'}
* W12. {40: 'ions', 41: 'and'}
* W13. {42: 'molecules.', 43: 'But'}
* W14. {44: 'you'}
* W15. {45: 'know,', 46: 'so', 47: 'this', 48: 'is'}
* W16. {49: 'telling', 50: 'you', 51: 'that.'}

scratchpad:
* W0. {0: 'Um,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. Um,, latency-forced partial release; empty windows follow, so further waiting would create excessive no-output delay: [0]

* W1. {1: '42%', 2: 'of', 3: 'the', 4: 'way', 5: 'through', 6: 'the'}
  - carried_over: None
  - defer: 'the' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [6]
  - release_units:
    1. 42% of the way through, stable minimal sense unit in the current window: [1,2,3,4,5]

* W2. {7: 'course,', 8: 'so', 9: 'as', 10: 'you'}
  - carried_over: {6: 'the'}
  - defer: 'so as you' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [8,9,10]
  - release_units:
    1. the course,, 'the' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7]

* W3. {11: 'can', 12: 'see,', 13: 'each'}
  - carried_over: {8: 'so', 9: 'as', 10: 'you'}
  - defer: 'each' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [13]
  - release_units:
    1. so as you can see,, 'so as you' is carried over from the previous window; released here because it is now a stable minimal sense unit: [8,9,10,11,12]

* W4. {14: 'pie', 15: 'slice'}
  - carried_over: {13: 'each'}
  - defer: None
  - release_units:
    1. each pie slice, 'each' is carried over from the previous window; stable minimal sense unit in the current window: [13,14,15]

* W5. {16: 'represents', 17: 'a', 18: 'different'}
  - carried_over: None
  - defer: 'a different' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [17,18]
  - release_units:
    1. represents, stable minimal sense unit in the current window: [16]

* W6. {19: 'topic,', 20: 'and'}
  - carried_over: {17: 'a', 18: 'different'}
  - defer: 'and' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [20]
  - release_units:
    1. a different topic,, 'a different' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19]

* W7. {}
  - carried_over: {20: 'and'}
  - defer: None
  - release_units:
    1. and, 'and' is carried over from the previous window; latency-forced partial release because waiting longer would violate output continuity: [20]

* W8. {21: 'they', 22: 'have', 23: 'a', 24: 'little', 25: 'bit', 26: 'more', 27: 'to'}
  - carried_over: None
  - defer: 'a little bit more to' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [23,24,25,26,27]
  - release_units:
    1. they have, stable minimal sense unit in the current window: [21,22]

* W9. {28: 'learn', 29: 'in', 30: 'in'}
  - carried_over: {23: 'a', 24: 'little', 25: 'bit', 26: 'more', 27: 'to'}
  - defer: 'in in' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [29,30]
  - release_units:
    1. a little bit more to learn, 'a little bit more to' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25,26,27,28]

* W10. {31: 'matter,', 32: 'and', 33: 'a', 34: 'little'}
  - carried_over: {29: 'in', 30: 'in'}
  - defer: 'a little' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [33,34]
  - release_units:
    1. in in matter,, 'in in' is carried over from the previous window; latency-forced partial release; the repetition 'in in' is not ideal but the local structure is clear: [29,30,31]
    2. and, stable minimal sense unit in the current window: [32]

* W11. {35: 'bit', 36: 'more', 37: 'in', 38: 'atoms', 39: 'and'}
  - carried_over: {33: 'a', 34: 'little'}
  - defer: 'in atoms and' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [37,38,39]
  - release_units:
    1. a little bit more, 'a little' is carried over from the previous window; released here because it is now a stable minimal sense unit: [33,34,35,36]

* W12. {40: 'ions', 41: 'and'}
  - carried_over: {37: 'in', 38: 'atoms', 39: 'and'}
  - defer: 'and' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [41]
  - release_units:
    1. in atoms and ions, 'in atoms and' is carried over from the previous window; released here because it is now a stable minimal sense unit: [37,38,39,40]

* W13. {42: 'molecules.', 43: 'But'}
  - carried_over: {41: 'and'}
  - defer: 'But' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [43]
  - release_units:
    1. and molecules., 'and' is carried over from the previous window; released here because it is now a stable minimal sense unit: [41,42]

* W14. {44: 'you'}
  - carried_over: {43: 'But'}
  - defer: None
  - release_units:
    1. But you, 'But' is carried over from the previous window; released here because it is now a stable minimal sense unit: [43,44]

* W15. {45: 'know,', 46: 'so', 47: 'this', 48: 'is'}
  - carried_over: None
  - defer: None
  - release_units:
    1. know, so this is, stable minimal sense unit in the current window: [45,46,47,48]

* W16. {49: 'telling', 50: 'you', 51: 'that.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. telling you that., stable minimal sense unit in the current window: [49,50,51]

result:
[
  [0],
  [1,2,3,4,5],
  [6,7],
  [8,9,10,11,12],
  [13,14,15],
  [16],
  [17,18,19],
  [20],
  [21,22],
  [23,24,25,26,27,28],
  [29,30,31],
  [32],
  [33,34,35,36],
  [37,38,39,40],
  [41,42],
  [43,44],
  [45,46,47,48],
  [49,50,51]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>Um, </src>; start=0.00, end=1.00
* W1. <src>42% of the way through </src>; start=1.00, end=2.00
* W2. <src>the course, </src>; start=2.00, end=3.00
* W3. <src>so as you can see, </src>; start=3.00, end=4.00
* W4. <src>each pie slice </src>; start=4.00, end=5.00
* W5. <src>represents </src>; start=5.00, end=6.00
* W6. <src>a different topic, and </src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>they have </src>; start=8.00, end=9.00
* W9. <src>a little bit more to learn </src>; start=9.00, end=10.00
* W10. <src>in in matter, and </src>; start=10.00, end=11.00
* W11. <src>a little bit more </src>; start=11.00, end=12.00
* W12. <src>in atoms and ions </src>; start=12.00, end=13.00
* W13. <src>and molecules. </src>; start=13.00, end=14.00
* W14. <src>But you </src>; start=14.00, end=15.00
* W15. <src>know, so this is </src>; start=15.00, end=16.00
* W16. <src>telling you that. </src>; start=16.00, end=16.94
```

---
=== EN_nIpxsCym-BM_W000211 ===

status: finished

raw_text:
By default, if you create a file called source/index, it's then going to push whatever you put in that file, any imports you use, things like that, out to

word_indices:
* W0. {0: 'By', 1: 'default,'}
* W1. {2: 'if', 3: 'you', 4: 'create', 5: 'a'}
* W2. {6: 'file', 7: 'called'}
* W3. {8: 'source/index,'}
* W4. {}
* W5. {9: "it's", 10: 'then', 11: 'going', 12: 'to', 13: 'push'}
* W6. {14: 'whatever', 15: 'you', 16: 'put', 17: 'in', 18: 'that'}
* W7. {19: 'file,', 20: 'any'}
* W8. {21: 'imports', 22: 'you', 23: 'use,', 24: 'things'}
* W9. {25: 'like', 26: 'that,'}
* W10. {27: 'out', 28: 'to'}

scratchpad:
* W0. {0: 'By', 1: 'default,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. By default,, stable minimal sense unit in the current window: [0,1]

* W1. {2: 'if', 3: 'you', 4: 'create', 5: 'a'}
  - carried_over: None
  - defer: 'a' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [5]
  - release_units:
    1. if you create, stable minimal sense unit in the current window: [2,3,4]

* W2. {6: 'file', 7: 'called'}
  - carried_over: {5: 'a'}
  - defer: 'called' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [7]
  - release_units:
    1. a file, 'a' is carried over from the previous window; released here because it is now a stable minimal sense unit: [5,6]

* W3. {8: 'source/index,'}
  - carried_over: {7: 'called'}
  - defer: None
  - release_units:
    1. called source/index,, 'called' is carried over from the previous window; released here because it is now a stable minimal sense unit: [7,8]

* W4. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W5. {9: "it's", 10: 'then', 11: 'going', 12: 'to', 13: 'push'}
  - carried_over: None
  - defer: None
  - release_units:
    1. it's then going to push, stable minimal sense unit in the current window: [9,10,11,12,13]

* W6. {14: 'whatever', 15: 'you', 16: 'put', 17: 'in', 18: 'that'}
  - carried_over: None
  - defer: 'that' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [18]
  - release_units:
    1. whatever you put in, stable minimal sense unit in the current window: [14,15,16,17]

* W7. {19: 'file,', 20: 'any'}
  - carried_over: {18: 'that'}
  - defer: 'any' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [20]
  - release_units:
    1. that file,, 'that' is carried over from the previous window; released here because it is now a stable minimal sense unit: [18,19]

* W8. {21: 'imports', 22: 'you', 23: 'use,', 24: 'things'}
  - carried_over: {20: 'any'}
  - defer: 'things' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [24]
  - release_units:
    1. any imports you use,, 'any' is carried over from the previous window; released here because it is now a stable minimal sense unit: [20,21,22,23]

* W9. {25: 'like', 26: 'that,'}
  - carried_over: {24: 'things'}
  - defer: None
  - release_units:
    1. things like that,, 'things' is carried over from the previous window; released here because it is now a stable minimal sense unit: [24,25,26]

* W10. {27: 'out', 28: 'to'}
  - carried_over: None
  - defer: None
  - release_units:
    1. out to, stable minimal sense unit in the current window: [27,28]

result:
[
  [0,1],
  [2,3,4],
  [5,6],
  [7,8],
  [9,10,11,12,13],
  [14,15,16,17],
  [18,19],
  [20,21,22,23],
  [24,25,26],
  [27,28]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>By default, </src>; start=0.00, end=1.00
* W1. <src>if you create </src>; start=1.00, end=2.00
* W2. <src>a file </src>; start=2.00, end=3.00
* W3. <src>called source/index, </src>; start=3.00, end=4.00
* W4. <src><|wait|></src>; start=4.00, end=5.00
* W5. <src>it's then going to push </src>; start=5.00, end=6.00
* W6. <src>whatever you put in </src>; start=6.00, end=7.00
* W7. <src>that file, </src>; start=7.00, end=8.00
* W8. <src>any imports you use, </src>; start=8.00, end=9.00
* W9. <src>things like that, </src>; start=9.00, end=10.00
* W10. <src>out to </src>; start=10.00, end=10.78
```

---
=== EN_nsPdq5m1h0y_W000029 ===

status: finished

raw_text:
We get the mass by taking the number of protons, which is always 35 for bromine, and we add it to the number of neutrons, which is new for this isotope. So 35 plus 47 is a mass of 82.

word_indices:
* W0. {0: 'We', 1: 'get', 2: 'the', 3: 'mass'}
* W1. {4: 'by', 5: 'taking', 6: 'the', 7: 'number', 8: 'of'}
* W2. {9: 'protons,', 10: 'which', 11: 'is'}
* W3. {12: 'always', 13: '35', 14: 'for'}
* W4. {15: 'bromine,'}
* W5. {16: 'and', 17: 'we', 18: 'add'}
* W6. {19: 'it', 20: 'to', 21: 'the', 22: 'number', 23: 'of'}
* W7. {24: 'neutrons,', 25: 'which', 26: 'is'}
* W8. {27: 'new', 28: 'for', 29: 'this'}
* W9. {30: 'isotope.', 31: 'So'}
* W10. {32: '35', 33: 'plus'}
* W11. {34: '47'}
* W12. {35: 'is', 36: 'a', 37: 'mass', 38: 'of'}
* W13. {39: '82.'}

scratchpad:
* W0. {0: 'We', 1: 'get', 2: 'the', 3: 'mass'}
  - carried_over: None
  - defer: None
  - release_units:
    1. We get the mass, stable minimal sense unit: [0,1,2,3]

* W1. {4: 'by', 5: 'taking', 6: 'the', 7: 'number', 8: 'of'}
  - carried_over: None
  - defer: None
  - release_units:
    1. by taking the number of, stable minimal sense unit (tight prepositional + noun-centered frame): [4,5,6,7,8]

* W2. {9: 'protons,', 10: 'which', 11: 'is'}
  - carried_over: None
  - defer: 'which is' does not yet form a stable minimal sense unit; defer it to the next window: [10,11]
  - release_units:
    1. protons,, stable noun unit with comma: [9]

* W3. {12: 'always', 13: '35', 14: 'for'}
  - carried_over: {10: 'which', 11: 'is'}
  - defer: 'for' is not yet a stable minimal sense unit; defer it to the next window because it starts a new prepositional phrase: [14]
  - release_units:
    1. which is always 35, carried over 'which is' + current 'always' and '35'; stable relative clause complement: [10,11,12,13]

* W4. {15: 'bromine,'}
  - carried_over: {14: 'for'}
  - defer: None
  - release_units:
    1. for bromine,, carried over 'for' + current 'bromine,'; stable prepositional phrase: [14,15]

* W5. {16: 'and', 17: 'we', 18: 'add'}
  - carried_over: None
  - defer: None
  - release_units:
    1. and we add, stable coordination lead‑in: [16,17,18]

* W6. {19: 'it', 20: 'to', 21: 'the', 22: 'number', 23: 'of'}
  - carried_over: None
  - defer: None
  - release_units:
    1. it to the number of, stable verb‑object + prepositional frame: [19,20,21,22,23]

* W7. {24: 'neutrons,', 25: 'which', 26: 'is'}
  - carried_over: None
  - defer: 'which is' does not yet form a stable minimal sense unit; defer it to the next window: [25,26]
  - release_units:
    1. neutrons,, stable noun unit: [24]

* W8. {27: 'new', 28: 'for', 29: 'this'}
  - carried_over: {25: 'which', 26: 'is'}
  - defer: 'for this' does not yet form a stable minimal sense unit; defer it to the next window: [28,29]
  - release_units:
    1. which is new, carried over 'which is' + current 'new'; stable relative clause: [25,26,27]

* W9. {30: 'isotope.', 31: 'So'}
  - carried_over: {28: 'for', 29: 'this'}
  - defer: None
  - release_units:
    1. for this isotope., carried over 'for this' + current 'isotope.'; stable prepositional phrase: [28,29,30]
    2. So, stable discourse marker: [31]

* W10. {32: '35', 33: 'plus'}
  - carried_over: None
  - defer: '35 plus' is not yet a stable minimal sense unit; defer it to the next window: [32,33]
  - release_units: None

* W11. {34: '47'}
  - carried_over: {32: '35', 33: 'plus'}
  - defer: None
  - release_units:
    1. 35 plus 47, carried over '35 plus' + current '47'; stable numeric expression: [32,33,34]

* W12. {35: 'is', 36: 'a', 37: 'mass', 38: 'of'}
  - carried_over: None
  - defer: None
  - release_units:
    1. is a mass of, stable predicate frame: [35,36,37,38]

* W13. {39: '82.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. 82., stable number unit: [39]

result:
[[0,1,2,3],[4,5,6,7,8],[9],[10,11,12,13],[14,15],[16,17,18],[19,20,21,22,23],[24],[25,26,27],[28,29,30],[31],[32,33,34],[35,36,37,38],[39]]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>We get the mass </src>; start=0.00, end=1.00
* W1. <src>by taking the number of </src>; start=1.00, end=2.00
* W2. <src>protons, </src>; start=2.00, end=3.00
* W3. <src>which is always 35 </src>; start=3.00, end=4.00
* W4. <src>for bromine, </src>; start=4.00, end=5.00
* W5. <src>and we add </src>; start=5.00, end=6.00
* W6. <src>it to the number of </src>; start=6.00, end=7.00
* W7. <src>neutrons, </src>; start=7.00, end=8.00
* W8. <src>which is new </src>; start=8.00, end=9.00
* W9. <src>for this isotope. So </src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=11.00
* W11. <src>35 plus 47 </src>; start=11.00, end=12.00
* W12. <src>is a mass of </src>; start=12.00, end=13.00
* W13. <src>82. </src>; start=13.00, end=13.53
```

---
=== EN_nCDIj7Cde90_W000000 ===

status: finished

raw_text:
I'm sorry for not making a video in three hours, but I wanted to tell you I am very sorry that I had to hit three other people like in the same place within less than ten minutes. I also thought that I could be banned from that location because I was being aggressive to them, and this meant.

word_indices:
* W0. {0: "I'm", 1: 'sorry', 2: 'for', 3: 'not'}
* W1. {4: 'making', 5: 'a', 6: 'video', 7: 'in'}
* W2. {8: 'three', 9: 'hours,'}
* W3. {10: 'but', 11: 'I', 12: 'wanted', 13: 'to', 14: 'tell'}
* W4. {15: 'you', 16: 'I'}
* W5. {17: 'am', 18: 'very', 19: 'sorry'}
* W6. {20: 'that', 21: 'I', 22: 'had', 23: 'to', 24: 'hit'}
* W7. {25: 'three', 26: 'other'}
* W8. {27: 'people'}
* W9. {28: 'like'}
* W10. {29: 'in', 30: 'the', 31: 'same'}
* W11. {32: 'place'}
* W12. {33: 'within', 34: 'less'}
* W13. {35: 'than', 36: 'ten', 37: 'minutes.'}
* W14. {38: 'I'}
* W15. {39: 'also', 40: 'thought', 41: 'that', 42: 'I', 43: 'could', 44: 'be'}
* W16. {45: 'banned', 46: 'from', 47: 'that'}
* W17. {48: 'location', 49: 'because', 50: 'I'}
* W18. {51: 'was', 52: 'being'}
* W19. {53: 'aggressive', 54: 'to'}
* W20. {55: 'them,'}
* W21. {56: 'and', 57: 'this'}
* W22. {58: 'meant.'}

scratchpad:
* W0. {0: "I'm", 1: 'sorry', 2: 'for', 3: 'not'}
  - carried_over: None
  - defer: 'for not' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [2,3]
  - release_units:
    1. I'm sorry, stable minimal sense unit in the current window: [0,1]

* W1. {4: 'making', 5: 'a', 6: 'video', 7: 'in'}
  - carried_over: {2: 'for', 3: 'not'}
  - defer: 'in' is not yet a stable release unit in the current window; defer it to the next window: [7]
  - release_units:
    1. for not making a video, 'for not' is carried over from the previous window; stable minimal sense unit: [2,3,4,5,6]

* W2. {8: 'three', 9: 'hours,'}
  - carried_over: {7: 'in'}
  - defer: None
  - release_units:
    1. in three hours,, 'in' is carried over from the previous window; stable minimal sense unit: [7,8,9]

* W3. {10: 'but', 11: 'I', 12: 'wanted', 13: 'to', 14: 'tell'}
  - carried_over: None
  - defer: 'tell' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [14]
  - release_units:
    1. but I wanted to, stable minimal sense unit in the current window: [10,11,12,13]

* W4. {15: 'you', 16: 'I'}
  - carried_over: {14: 'tell'}
  - defer: 'I' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [16]
  - release_units:
    1. tell you, 'tell' is carried over from the previous window; stable minimal sense unit: [14,15]

* W5. {17: 'am', 18: 'very', 19: 'sorry'}
  - carried_over: {16: 'I'}
  - defer: None
  - release_units:
    1. I am very sorry, 'I' is carried over from the previous window; stable minimal sense unit: [16,17,18,19]

* W6. {20: 'that', 21: 'I', 22: 'had', 23: 'to', 24: 'hit'}
  - carried_over: None
  - defer: 'hit' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [24]
  - release_units:
    1. that I had to, stable minimal sense unit in the current window: [20,21,22,23]

* W7. {25: 'three', 26: 'other'}
  - carried_over: {24: 'hit'}
  - defer: 'hit three other' does not yet form a stable minimal sense unit; defer all to the next window: [24,25,26]
  - release_units: None

* W8. {27: 'people'}
  - carried_over: {24: 'hit', 25: 'three', 26: 'other'}
  - defer: None
  - release_units:
    1. hit three other people, carried over from previous window; stable minimal sense unit: [24,25,26,27]

* W9. {28: 'like'}
  - carried_over: None
  - defer: 'like' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [28]
  - release_units: None

* W10. {29: 'in', 30: 'the', 31: 'same'}
  - carried_over: {28: 'like'}
  - defer: 'in the same' does not yet form a stable minimal sense unit; defer to the next window: [29,30,31]
  - release_units:
    1. like, latency-forced partial release; previous window had no output, so current window must flush something: [28]

* W11. {32: 'place'}
  - carried_over: {29: 'in', 30: 'the', 31: 'same'}
  - defer: None
  - release_units:
    1. in the same place, carried over from previous window; stable minimal sense unit: [29,30,31,32]

* W12. {33: 'within', 34: 'less'}
  - carried_over: None
  - defer: 'within less' does not yet form a stable minimal sense unit; defer all to the next window: [33,34]
  - release_units: None

* W13. {35: 'than', 36: 'ten', 37: 'minutes.'}
  - carried_over: {33: 'within', 34: 'less'}
  - defer: None
  - release_units:
    1. within less than ten minutes., 'within less' carried over from previous window; stable minimal sense unit: [33,34,35,36,37]

* W14. {38: 'I'}
  - carried_over: None
  - defer: 'I' does not yet form a stable minimal sense unit; defer it to the next window: [38]
  - release_units: None

* W15. {39: 'also', 40: 'thought', 41: 'that', 42: 'I', 43: 'could', 44: 'be'}
  - carried_over: {38: 'I'}
  - defer: 'be' does not yet form a stable minimal sense unit in the current window; defer it to the next window: [44]
  - release_units:
    1. I also thought that I could, 'I' carried over from previous window; stable minimal sense unit: [38,39,40,41,42,43]

* W16. {45: 'banned', 46: 'from', 47: 'that'}
  - carried_over: {44: 'be'}
  - defer: 'that' does not yet form a stable minimal sense unit; defer it to the next window: [47]
  - release_units:
    1. be banned from, 'be' carried over from previous window; stable minimal sense unit: [44,45,46]

* W17. {48: 'location', 49: 'because', 50: 'I'}
  - carried_over: {47: 'that'}
  - defer: 'because I' does not yet form a stable minimal sense unit; defer it to the next window: [49,50]
  - release_units:
    1. that location, 'that' carried over from previous window; stable minimal sense unit: [47,48]

* W18. {51: 'was', 52: 'being'}
  - carried_over: {49: 'because', 50: 'I'}
  - defer: 'being' does not yet form a stable minimal sense unit; defer it to the next window: [52]
  - release_units:
    1. because I was, 'because I' carried over from previous window; stable minimal sense unit: [49,50,51]

* W19. {53: 'aggressive', 54: 'to'}
  - carried_over: {52: 'being'}
  - defer: 'to' does not yet form a stable minimal sense unit; defer it to the next window: [54]
  - release_units:
    1. being aggressive, 'being' carried over from previous window; stable minimal sense unit: [52,53]

* W20. {55: 'them,'}
  - carried_over: {54: 'to'}
  - defer: None
  - release_units:
    1. to them,, 'to' carried over from previous window; stable minimal sense unit: [54,55]

* W21. {56: 'and', 57: 'this'}
  - carried_over: None
  - defer: 'and this' does not yet form a stable minimal sense unit; defer all to the next window: [56,57]
  - release_units: None

* W22. {58: 'meant.'}
  - carried_over: {56: 'and', 57: 'this'}
  - defer: None
  - release_units:
    1. and this meant., 'and this' carried over from previous window; stable minimal sense unit: [56,57,58]

result:
[
  [0,1],
  [2,3,4,5,6],
  [7,8,9],
  [10,11,12,13],
  [14,15],
  [16,17,18,19],
  [20,21,22,23],
  [24,25,26,27],
  [28],
  [29,30,31,32],
  [33,34,35,36,37],
  [38,39,40,41,42,43],
  [44,45,46],
  [47,48],
  [49,50,51],
  [52,53],
  [54,55],
  [56,57,58]
]

attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>I'm sorry </src>; start=0.00, end=1.00
* W1. <src>for not making a video </src>; start=1.00, end=2.00
* W2. <src>in three hours, </src>; start=2.00, end=3.00
* W3. <src>but I wanted to </src>; start=3.00, end=4.00
* W4. <src>tell you </src>; start=4.00, end=5.00
* W5. <src>I am very sorry </src>; start=5.00, end=6.00
* W6. <src>that I had to </src>; start=6.00, end=7.00
* W7. <src><|wait|></src>; start=7.00, end=8.00
* W8. <src>hit three other people </src>; start=8.00, end=9.00
* W9. <src>like </src>; start=9.00, end=10.00
* W10. <src><|wait|></src>; start=10.00, end=11.00
* W11. <src>in the same place </src>; start=11.00, end=12.00
* W12. <src><|wait|></src>; start=12.00, end=13.00
* W13. <src>within less than ten minutes. </src>; start=13.00, end=14.00
* W14. <src><|wait|></src>; start=14.00, end=15.00
* W15. <src>I also thought that I could </src>; start=15.00, end=16.00
* W16. <src>be banned from </src>; start=16.00, end=17.00
* W17. <src>that location </src>; start=17.00, end=18.00
* W18. <src>because I was </src>; start=18.00, end=19.00
* W19. <src>being aggressive </src>; start=19.00, end=20.00
* W20. <src>to them, </src>; start=20.00, end=21.00
* W21. <src><|wait|></src>; start=21.00, end=22.00
* W22. <src>and this meant. </src>; start=22.00, end=22.20
```

---
=== EN_nN_EW5TiHKQ_W000023 ===

status: finished

raw_text:
Who can help you way more than I can. I really appreciate my trans followers when they tell me that they value my opinion on books, or when they tell me that they read a book because of me. Like I have gotten so many DMs from people saying, "Hey, I read Stay Gold because of you, and it was so good," and that honestly makes me so happy.

word_indices:
* W0. {0: 'Who', 1: 'can', 2: 'help'}
* W1. {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'}
* W2. {8: 'can.', 9: 'I', 10: 'really'}
* W3. {11: 'appreciate', 12: 'my', 13: 'trans'}
* W4. {14: 'followers', 15: 'when', 16: 'they', 17: 'tell'}
* W5. {18: 'me', 19: 'that'}
* W6. {20: 'they', 21: 'value', 22: 'my'}
* W7. {23: 'opinion', 24: 'on', 25: 'books,'}
* W8. {26: 'or'}
* W9. {27: 'when', 28: 'they', 29: 'tell', 30: 'me'}
* W10. {31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'}
* W11. {36: 'because', 37: 'of', 38: 'me.', 39: 'Like'}
* W12. {40: 'I', 41: 'have'}
* W13. {42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs', 46: 'from'}
* W14. {47: 'people', 48: 'saying,"'}
* W15. {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'}
* W16. {53: 'Gold', 54: 'because', 55: 'of', 56: 'you,', 57: 'and', 58: 'it'}
* W17. {59: 'was', 60: 'so', 61: 'good,"', 62: 'and'}
* W18. {63: 'that', 64: 'honestly', 65: 'makes'}
* W19. {66: 'me', 67: 'so', 68: 'happy.'}

scratchpad:
* W0. {0: 'Who', 1: 'can', 2: 'help'}
  - carried_over: None
  - defer: None
  - release_units:
    1. "Who can help", minimal sense unit (question start): [0,1,2]

* W1. {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'}
  - carried_over: None
  - defer: "'you way more than I' needs 'can' to form a stable comparison unit; defer all to next window": [3,4,5,6,7]
  - release_units: None

* W2. {8: 'can.', 9: 'I', 10: 'really'}
  - carried_over: {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'}
  - defer: "'I really' is better combined with 'appreciate' in next window to form a stronger lead-in; defer these": [9,10]
  - release_units:
    1. "you way more than I can.", carried over "you way more than I" + current "can.", stable minimal sense unit: [3,4,5,6,7,8]

* W3. {11: 'appreciate', 12: 'my', 13: 'trans'}
  - carried_over: {9: 'I', 10: 'really'}
  - defer: "'my trans' needs the noun 'followers' to complete; defer": [12,13]
  - release_units:
    1. "I really appreciate", "I really" carried over + current "appreciate", stable lead-in unit: [9,10,11]

* W4. {14: 'followers', 15: 'when', 16: 'they', 17: 'tell'}
  - carried_over: {12: 'my', 13: 'trans'}
  - defer: "'when they tell' is better combined with next object; defer": [15,16,17]
  - release_units:
    1. "my trans followers", carried "my trans" + current "followers", stable noun unit: [12,13,14]

* W5. {18: 'me', 19: 'that'}
  - carried_over: {15: 'when', 16: 'they', 17: 'tell'}
  - defer: None
  - release_units:
    1. "when they tell me that", carried "when they tell" + current "me that", stable lead-in unit: [15,16,17,18,19]

* W6. {20: 'they', 21: 'value', 22: 'my'}
  - carried_over: None
  - defer: "'they value my' needs object; defer all": [20,21,22]
  - release_units: None

* W7. {23: 'opinion', 24: 'on', 25: 'books,'}
  - carried_over: {20: 'they', 21: 'value', 22: 'my'}
  - defer: None
  - release_units:
    1. "they value my opinion on books,", carried "they value my" + current "opinion on books,", stable minimal predicate unit: [20,21,22,23,24,25]

* W8. {26: 'or'}
  - carried_over: None
  - defer: "'or' is a bare coordinator; defer to combine with next clause": [26]
  - release_units: None

* W9. {27: 'when', 28: 'they', 29: 'tell', 30: 'me'}
  - carried_over: {26: 'or'}
  - defer: None
  - release_units:
    1. "or when they tell me", carried "or" + current "when they tell me", forced flush (previous window had no output), stable lead-in unit: [26,27,28,29,30]

* W10. {31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'}
  - carried_over: None
  - defer: None
  - release_units:
    1. "that they read a book", stable complement clause: [31,32,33,34,35]

* W11. {36: 'because', 37: 'of', 38: 'me.', 39: 'Like'}
  - carried_over: None
  - defer: "'Like' is a discourse marker; defer to combine with next subject": [39]
  - release_units:
    1. "because of me.", stable minimal unit: [36,37,38]

* W12. {40: 'I', 41: 'have'}
  - carried_over: {39: 'Like'}
  - defer: None
  - release_units:
    1. "Like I have", carried "Like" + current "I have", stable lead-in: [39,40,41]

* W13. {42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs', 46: 'from'}
  - carried_over: None
  - defer: "'gotten so many DMs from' expects object; defer all": [42,43,44,45,46]
  - release_units: None

* W14. {47: 'people', 48: 'saying,"'}
  - carried_over: {42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs', 46: 'from'}
  - defer: None
  - release_units:
    1. "gotten so many DMs", carried "gotten so many DMs" from previous + current start? Actually carried [42,43,44,45] plus current? Wait, carried includes 46 'from'? I mis-assigned. Carried indices: 42,43,44,45,46 (from W13). Current indices: 47,48. So combined: 42-48. Split into two stable units: first unit "gotten so many DMs" [42,43,44,45] - note token 46 'from' is not included; second unit "from people saying," [46,47,48]. Both released together.
      1a. "gotten so many DMs" (carried 42-45): [42,43,44,45]
      1b. "from people saying," (carried 46 + current 47-48): [46,47,48]

* W15. {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'}
  - carried_over: None
  - defer: "'Hey, I read Stay' needs the rest of book title; defer all": [49,50,51,52]
  - release_units: None

* W16. {53: 'Gold', 54: 'because', 55: 'of', 56: 'you,', 57: 'and', 58: 'it'}
  - carried_over: {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'}
  - defer: None
  - release_units:
    1. "Hey, I read Stay Gold", carried "Hey, I read Stay" + current "Gold", stable core: [49,50,51,52,53]
    2. "because of you,", current "because of you,", stable prepositional unit: [54,55,56]
    3. "and it", current "and it", stable connector lead-in: [57,58]

* W17. {59: 'was', 60: 'so', 61: 'good,"', 62: 'and'}
  - carried_over: None
  - defer: "'and' is a bare coordinator; defer to combine with next clause": [62]
  - release_units:
    1. "was so good,", current, stable minimal unit: [59,60,61]

* W18. {63: 'that', 64: 'honestly', 65: 'makes'}
  - carried_over: {62: 'and'}
  - defer: None
  - release_units:
    1. "and that honestly makes", carried "and" + current "that honestly makes", stable lead-in unit: [62,63,64,65]

* W19. {66: 'me', 67: 'so', 68: 'happy.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. "me so happy.", current, stable minimal unit: [66,67,68]

result:
[
  [0,1,2],
  [3,4,5,6,7,8],
  [9,10,11],
  [12,13,14],
  [15,16,17,18,19],
  [20,21,22,23,24,25],
  [26,27,28,29,30],
  [31,32,33,34,35],
  [36,37,38],
  [39,40,41],
  [42,43,44,45],
  [46,47,48],
  [49,50,51,52,53],
  [54,55,56],
  [57,58],
  [59,60,61],
  [62,63,64,65],
  [66,67,68]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: 'Who', 1: 'can', 2: 'help'} - output: release_units 1.{0: 'Who', 1: 'can', 2: 'help'}
* W1. input: {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'} - output: release_units None
* W2. input: {8: 'can.', 9: 'I', 10: 'really'} - output: release_units 1.{3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I', 8: 'can.'}
* W3. input: {11: 'appreciate', 12: 'my', 13: 'trans'} - output: release_units 1.{9: 'I', 10: 'really', 11: 'appreciate'}
* W4. input: {14: 'followers', 15: 'when', 16: 'they', 17: 'tell'} - output: release_units 1.{12: 'my', 13: 'trans', 14: 'followers'}
* W5. input: {18: 'me', 19: 'that'} - output: release_units 1.{15: 'when', 16: 'they', 17: 'tell', 18: 'me', 19: 'that'}
* W6. input: {20: 'they', 21: 'value', 22: 'my'} - output: release_units None
* W7. input: {23: 'opinion', 24: 'on', 25: 'books,'} - output: release_units 1.{20: 'they', 21: 'value', 22: 'my', 23: 'opinion', 24: 'on', 25: 'books,'}
* W8. input: {26: 'or'} - output: release_units None
* W9. input: {27: 'when', 28: 'they', 29: 'tell', 30: 'me'} - output: release_units 1.{26: 'or', 27: 'when', 28: 'they', 29: 'tell', 30: 'me'}
* W10. input: {31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'} - output: release_units 1.{31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'}
* W11. input: {36: 'because', 37: 'of', 38: 'me.', 39: 'Like'} - output: release_units 1.{36: 'because', 37: 'of', 38: 'me.'}
* W12. input: {40: 'I', 41: 'have'} - output: release_units 1.{39: 'Like', 40: 'I', 41: 'have'}
* W13. input: {42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs', 46: 'from'} - output: release_units 1.{42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs'}
* W14. input: {47: 'people', 48: 'saying,"'} - output: release_units 1.{46: 'from', 47: 'people', 48: 'saying,"'}
* W15. input: {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'} - output: release_units None
* W16. input: {53: 'Gold', 54: 'because', 55: 'of', 56: 'you,', 57: 'and', 58: 'it'} - output: release_units 1.{49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay', 53: 'Gold', 54: 'because', 55: 'of', 56: 'you,'} <- ISSUE2: oversized chunk release unit 1 size=8 > 6. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W17. input: {59: 'was', 60: 'so', 61: 'good,"', 62: 'and'} - output: release_units 1.{57: 'and', 58: 'it', 59: 'was', 60: 'so', 61: 'good,"'}
* W18. input: {63: 'that', 64: 'honestly', 65: 'makes'} - output: release_units 1.{62: 'and', 63: 'that', 64: 'honestly', 65: 'makes'}
* W19. input: {66: 'me', 67: 'so', 68: 'happy.'} - output: release_units 1.{66: 'me', 67: 'so', 68: 'happy.'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: 'Who', 1: 'can', 2: 'help'}
  - carried_over: None
  - defer: None
  - release_units:
    1. Who can help, stable minimal sense unit (compact interrogative lead-in): [0,1,2]

* W1. {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'}
  - carried_over: None
  - defer: 'you way more than I' is not yet a stable minimal sense unit; the comparison predicate is missing and expected in the next window; defer it to the next window because the previous window had output: [3,4,5,6,7]
  - release_units: None

* W2. {8: 'can.', 9: 'I', 10: 'really'}
  - carried_over: {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'}
  - defer: 'I really' is the start of a new sentence; defer it to the next window to pair with 'appreciate' for a tighter lead-in: [9,10]
  - release_units:
    1. you way more than I can., carried over from the previous window; now forms a complete comparison minimal sense unit: [3,4,5,6,7,8]

* W3. {11: 'appreciate', 12: 'my', 13: 'trans'}
  - carried_over: {9: 'I', 10: 'really'}
  - defer: 'my trans' is a possessive+adjective that expects a noun (followers); defer it to the next window: [12,13]
  - release_units:
    1. I really appreciate, 'I really' is carried over from the previous window; now forms a stable lead-in minimal sense unit: [9,10,11]

* W4. {14: 'followers', 15: 'when', 16: 'they', 17: 'tell'}
  - carried_over: {12: 'my', 13: 'trans'}
  - defer: 'when they tell' is the start of a subordinate clause; defer it to the next window to form a fuller lead-in: [15,16,17]
  - release_units:
    1. my trans followers, carried over from the previous window; forms a compact noun-centered local frame: [12,13,14]

* W5. {18: 'me', 19: 'that'}
  - carried_over: {15: 'when', 16: 'they', 17: 'tell'}
  - defer: None
  - release_units:
    1. when they tell me that, carried over from the previous window; forms a compact lead-in minimal sense unit: [15,16,17,18,19]

* W6. {20: 'they', 21: 'value', 22: 'my'}
  - carried_over: None
  - defer: 'they value my' is incomplete (needs object); defer all to the next window because the previous window had output: [20,21,22]
  - release_units: None

* W7. {23: 'opinion', 24: 'on', 25: 'books,'}
  - carried_over: {20: 'they', 21: 'value', 22: 'my'}
  - defer: None
  - release_units:
    1. they value my opinion on books,, carried over from the previous window; now forms a stable minimal sense unit (subject-verb-object-prepositional phrase): [20,21,22,23,24,25]

* W8. {26: 'or'}
  - carried_over: None
  - defer: 'or' is a bare conjunction; defer it to the next window to form a larger coordinate lead-in: [26]
  - release_units: None

* W9. {27: 'when', 28: 'they', 29: 'tell', 30: 'me'}
  - carried_over: {26: 'or'}
  - defer: None
  - release_units:
    1. or when they tell me, carried over from the previous window; forms a compact lead-in minimal sense unit: [26,27,28,29,30]

* W10. {31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'}
  - carried_over: None
  - defer: None
  - release_units:
    1. that they read a book, stable minimal sense unit (content clause): [31,32,33,34,35]

* W11. {36: 'because', 37: 'of', 38: 'me.', 39: 'Like'}
  - carried_over: None
  - defer: 'Like' is a discourse marker starting a new sentence; defer it to the next window: [39]
  - release_units:
    1. because of me., stable minimal sense unit (prepositional phrase ending a sentence): [36,37,38]

* W12. {40: 'I', 41: 'have'}
  - carried_over: {39: 'Like'}
  - defer: None
  - release_units:
    1. Like I have, carried over from the previous window; forms a stable lead-in minimal sense unit: [39,40,41]

* W13. {42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs', 46: 'from'}
  - carried_over: None
  - defer: 'from' is a preposition that expects a noun; defer it to the next window: [46]
  - release_units:
    1. gotten so many DMs, stable minimal sense unit (verb phrase with quantifier and noun): [42,43,44,45]

* W14. {47: 'people', 48: 'saying,"'}
  - carried_over: {46: 'from'}
  - defer: None
  - release_units:
    1. from people saying,, carried over from the previous window; forms a stable minimal sense unit (prepositional phrase plus participle): [46,47,48]

* W15. {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'}
  - carried_over: None
  - defer: 'Hey, I read Stay' is incomplete (needs 'Gold'); defer all to the next window because the previous window had output: [49,50,51,52]
  - release_units: None

* W16. {53: 'Gold', 54: 'because', 55: 'of', 56: 'you,', 57: 'and', 58: 'it'}
  - carried_over: {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'}
  - defer: 'and it' starts the next clause in the quote; defer to the next window to avoid splitting mid-unit: [57,58]
  - release_units:
    1. Hey, I read Stay Gold because of you,, carried over from the previous window; now forms a stable minimal sense unit (complete quoted clause): [49,50,51,52,53,54,55,56]

* W17. {59: 'was', 60: 'so', 61: 'good,"', 62: 'and'}
  - carried_over: {57: 'and', 58: 'it'}
  - defer: 'and' (index 62) is the start of the main narrative continuation; defer it to the next window: [62]
  - release_units:
    1. and it was so good,, carried over from the previous window; forms a stable minimal sense unit (completes the quote clause): [57,58,59,60,61]

* W18. {63: 'that', 64: 'honestly', 65: 'makes'}
  - carried_over: {62: 'and'}
  - defer: None
  - release_units:
    1. and that honestly makes, carried over from the previous window; forms a stable lead-in minimal sense unit: [62,63,64,65]

* W19. {66: 'me', 67: 'so', 68: 'happy.'}
  - carried_over: None
  - defer: None
  - release_units:
    1. me so happy., stable minimal sense unit (completes the main clause): [66,67,68]
  result:
[
  [0,1,2],
  [3,4,5,6,7,8],
  [9,10,11],
  [12,13,14],
  [15,16,17,18,19],
  [20,21,22,23,24,25],
  [26,27,28,29,30],
  [31,32,33,34,35],
  [36,37,38],
  [39,40,41],
  [42,43,44,45],
  [46,47,48],
  [49,50,51,52,53,54,55,56],
  [57,58,59,60,61],
  [62,63,64,65],
  [66,67,68]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: 'Who', 1: 'can', 2: 'help'} - output: release_units 1.{0: 'Who', 1: 'can', 2: 'help'}
* W1. input: {3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I'} - output: release_units None
* W2. input: {8: 'can.', 9: 'I', 10: 'really'} - output: release_units 1.{3: 'you', 4: 'way', 5: 'more', 6: 'than', 7: 'I', 8: 'can.'}
* W3. input: {11: 'appreciate', 12: 'my', 13: 'trans'} - output: release_units 1.{9: 'I', 10: 'really', 11: 'appreciate'}
* W4. input: {14: 'followers', 15: 'when', 16: 'they', 17: 'tell'} - output: release_units 1.{12: 'my', 13: 'trans', 14: 'followers'}
* W5. input: {18: 'me', 19: 'that'} - output: release_units 1.{15: 'when', 16: 'they', 17: 'tell', 18: 'me', 19: 'that'}
* W6. input: {20: 'they', 21: 'value', 22: 'my'} - output: release_units None
* W7. input: {23: 'opinion', 24: 'on', 25: 'books,'} - output: release_units 1.{20: 'they', 21: 'value', 22: 'my', 23: 'opinion', 24: 'on', 25: 'books,'}
* W8. input: {26: 'or'} - output: release_units None
* W9. input: {27: 'when', 28: 'they', 29: 'tell', 30: 'me'} - output: release_units 1.{26: 'or', 27: 'when', 28: 'they', 29: 'tell', 30: 'me'}
* W10. input: {31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'} - output: release_units 1.{31: 'that', 32: 'they', 33: 'read', 34: 'a', 35: 'book'}
* W11. input: {36: 'because', 37: 'of', 38: 'me.', 39: 'Like'} - output: release_units 1.{36: 'because', 37: 'of', 38: 'me.'}
* W12. input: {40: 'I', 41: 'have'} - output: release_units 1.{39: 'Like', 40: 'I', 41: 'have'}
* W13. input: {42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs', 46: 'from'} - output: release_units 1.{42: 'gotten', 43: 'so', 44: 'many', 45: 'DMs'}
* W14. input: {47: 'people', 48: 'saying,"'} - output: release_units 1.{46: 'from', 47: 'people', 48: 'saying,"'}
* W15. input: {49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay'} - output: release_units None
* W16. input: {53: 'Gold', 54: 'because', 55: 'of', 56: 'you,', 57: 'and', 58: 'it'} - output: release_units 1.{49: 'Hey,', 50: 'I', 51: 'read', 52: 'Stay', 53: 'Gold', 54: 'because', 55: 'of', 56: 'you,'} <- ISSUE2: oversized chunk release unit 1 size=8 > 6. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W17. input: {59: 'was', 60: 'so', 61: 'good,"', 62: 'and'} - output: release_units 1.{57: 'and', 58: 'it', 59: 'was', 60: 'so', 61: 'good,"'}
* W18. input: {63: 'that', 64: 'honestly', 65: 'makes'} - output: release_units 1.{62: 'and', 63: 'that', 64: 'honestly', 65: 'makes'}
* W19. input: {66: 'me', 67: 'so', 68: 'happy.'} - output: release_units 1.{66: 'me', 67: 'so', 68: 'happy.'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>Who can help </src>; start=0.00, end=1.00
* W1. <src><|wait|></src>; start=1.00, end=2.00
* W2. <src>you way more than I can. </src>; start=2.00, end=3.00
* W3. <src>I really appreciate </src>; start=3.00, end=4.00
* W4. <src>my trans followers </src>; start=4.00, end=5.00
* W5. <src>when they tell me that </src>; start=5.00, end=6.00
* W6. <src><|wait|></src>; start=6.00, end=7.00
* W7. <src>they value my opinion on books, </src>; start=7.00, end=8.00
* W8. <src><|wait|></src>; start=8.00, end=9.00
* W9. <src>or when they tell me </src>; start=9.00, end=10.00
* W10. <src>that they read a book </src>; start=10.00, end=11.00
* W11. <src>because of me. </src>; start=11.00, end=12.00
* W12. <src>Like I have </src>; start=12.00, end=13.00
* W13. <src>gotten so many DMs </src>; start=13.00, end=14.00
* W14. <src>from people saying," </src>; start=14.00, end=15.00
* W15. <src><|wait|></src>; start=15.00, end=16.00
* W16. <src>Hey, I read Stay Gold because of you, and it </src>; start=16.00, end=17.00
* W17. <src>was so good," </src>; start=17.00, end=18.00
* W18. <src>and that honestly makes </src>; start=18.00, end=19.00
* W19. <src>me so happy. </src>; start=19.00, end=19.81
```

---
=== EN_n_UNfbRo_MQ_W000005 ===

status: finished

raw_text:
But the Commonwealth Department of Agriculture, Fisheries and Forestry had the foresight to identify the need for Australia to be ahead of the game and well coordinated, and so developed the Australian Animal Welfare Strategy eight years ago.

word_indices:
* W0. {0: 'But', 1: 'the', 2: 'Commonwealth'}
* W1. {3: 'Department', 4: 'of', 5: 'Agriculture,'}
* W2. {6: 'Fisheries', 7: 'and'}
* W3. {8: 'Forestry', 9: 'had', 10: 'the'}
* W4. {11: 'foresight', 12: 'to'}
* W5. {13: 'identify', 14: 'the', 15: 'need', 16: 'for'}
* W6. {17: 'Australia', 18: 'to', 19: 'be'}
* W7. {20: 'ahead', 21: 'of', 22: 'the', 23: 'game'}
* W8. {24: 'and', 25: 'well'}
* W9. {26: 'coordinated,', 27: 'and'}
* W10. {28: 'so', 29: 'developed', 30: 'the'}
* W11. {31: 'Australian', 32: 'Animal', 33: 'Welfare'}
* W12. {34: 'Strategy', 35: 'eight'}
* W13. {36: 'years', 37: 'ago.'}

scratchpad:
* W0. {0: 'But', 1: 'the', 2: 'Commonwealth'}
  - carried_over: None
  - defer: 'But the Commonwealth' does not yet form a stable minimal sense unit; defer to next window: [0,1,2]
  - release_units: None

* W1. {3: 'Department', 4: 'of', 5: 'Agriculture,'}
  - carried_over: {0: 'But', 1: 'the', 2: 'Commonwealth'}
  - defer: None
  - release_units:
    1. But the Commonwealth, carried over from previous window; stable lead-in frame: [0,1,2]
    2. Department of Agriculture,, stable noun-centered local frame in current window: [3,4,5]

* W2. {6: 'Fisheries', 7: 'and'}
  - carried_over: None
  - defer: 'Fisheries and' does not yet form a stable minimal sense unit; defer to next window: [6,7]
  - release_units: None

* W3. {8: 'Forestry', 9: 'had', 10: 'the'}
  - carried_over: {6: 'Fisheries', 7: 'and'}
  - defer: 'had the' does not yet form a stable minimal sense unit; defer to next window: [9,10]
  - release_units:
    1. Fisheries and Forestry, carried over from previous window; compact coordination unit: [6,7,8]

* W4. {11: 'foresight', 12: 'to'}
  - carried_over: {9: 'had', 10: 'the'}
  - defer: None
  - release_units:
    1. had the foresight to, carried over from previous window; stable verb phrase with infinitive: [9,10,11,12]

* W5. {13: 'identify', 14: 'the', 15: 'need', 16: 'for'}
  - carried_over: None
  - defer: None
  - release_units:
    1. identify the need for, stable minimal sense unit: verb + noun phrase + preposition: [13,14,15,16]

* W6. {17: 'Australia', 18: 'to', 19: 'be'}
  - carried_over: None
  - defer: 'Australia to be' does not yet form a stable minimal sense unit; defer to next window: [17,18,19]
  - release_units: None

* W7. {20: 'ahead', 21: 'of', 22: 'the', 23: 'game'}
  - carried_over: {17: 'Australia', 18: 'to', 19: 'be'}
  - defer: None
  - release_units:
    1. Australia to be, carried over from previous window; compact lead-in frame: [17,18,19]
    2. ahead of the game, stable prepositional phrase in current window: [20,21,22,23]

* W8. {24: 'and', 25: 'well'}
  - carried_over: None
  - defer: 'and well' does not yet form a stable minimal sense unit; defer to next window: [24,25]
  - release_units: None

* W9. {26: 'coordinated,', 27: 'and'}
  - carried_over: {24: 'and', 25: 'well'}
  - defer: 'and' does not yet form a stable minimal sense unit; defer to next window: [27]
  - release_units:
    1. and well coordinated,, carried over from previous window; stable minimal sense unit: [24,25,26]

* W10. {28: 'so', 29: 'developed', 30: 'the'}
  - carried_over: {27: 'and'}
  - defer: None
  - release_units:
    1. and so developed the, carried over from previous window; stable lead-in frame: [27,28,29,30]

* W11. {31: 'Australian', 32: 'Animal', 33: 'Welfare'}
  - carried_over: None
  - defer: 'Australian Animal Welfare' does not yet form a stable minimal sense unit; defer to next window: [31,32,33]
  - release_units: None

* W12. {34: 'Strategy', 35: 'eight'}
  - carried_over: {31: 'Australian', 32: 'Animal', 33: 'Welfare'}
  - defer: 'eight' does not yet form a stable minimal sense unit; defer to next window: [35]
  - release_units:
    1. Australian Animal Welfare Strategy, carried over from previous window; stable proper noun phrase: [31,32,33,34]

* W13. {36: 'years', 37: 'ago.'}
  - carried_over: {35: 'eight'}
  - defer: None
  - release_units:
    1. eight years ago., carried over from previous window; stable minimal sense unit: [35,36,37]

result:
[
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18,19],
  [20,21,22,23],
  [24,25,26],
  [27,28,29,30],
  [31,32,33,34],
  [35,36,37]
]

attempts:

- retry: 0/5
  status: failed_after_response
  reason: Sense unit segmentation validation failed:
* W0. input: {0: 'But', 1: 'the', 2: 'Commonwealth'} - output: release_units None
* W1. input: {3: 'Department', 4: 'of', 5: 'Agriculture,'} - output: release_units 1.{0: 'But', 1: 'the', 2: 'Commonwealth', 3: 'Department', 4: 'of', 5: 'Agriculture,'}
* W2. input: {6: 'Fisheries', 7: 'and'} - output: release_units None
* W3. input: {8: 'Forestry', 9: 'had', 10: 'the'} - output: release_units 1.{6: 'Fisheries', 7: 'and', 8: 'Forestry'}
* W4. input: {11: 'foresight', 12: 'to'} - output: release_units 1.{9: 'had', 10: 'the', 11: 'foresight', 12: 'to'}
* W5. input: {13: 'identify', 14: 'the', 15: 'need', 16: 'for'} - output: release_units 1.{13: 'identify', 14: 'the', 15: 'need', 16: 'for'}
* W6. input: {17: 'Australia', 18: 'to', 19: 'be'} - output: release_units None
* W7. input: {20: 'ahead', 21: 'of', 22: 'the', 23: 'game'} - output: release_units 1.{17: 'Australia', 18: 'to', 19: 'be', 20: 'ahead', 21: 'of', 22: 'the', 23: 'game'} <- ISSUE2: oversized chunk release unit 1 size=7 > 6. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W8. input: {24: 'and', 25: 'well'} - output: release_units None
* W9. input: {26: 'coordinated,', 27: 'and'} - output: release_units 1.{24: 'and', 25: 'well', 26: 'coordinated,'}
* W10. input: {28: 'so', 29: 'developed', 30: 'the'} - output: release_units 1.{27: 'and', 28: 'so', 29: 'developed'}
* W11. input: {31: 'Australian', 32: 'Animal', 33: 'Welfare'} - output: release_units None
* W12. input: {34: 'Strategy', 35: 'eight'} - output: release_units 1.{30: 'the', 31: 'Australian', 32: 'Animal', 33: 'Welfare', 34: 'Strategy'}
* W13. input: {36: 'years', 37: 'ago.'} - output: release_units 1.{35: 'eight', 36: 'years', 37: 'ago.'}

Reconfirm the RULEs and your task!

  scratchpad:
* W0. {0: 'But', 1: 'the', 2: 'Commonwealth'}
  - carried_over: None
  - defer: 'But the Commonwealth' does not yet form a stable minimal sense unit because it would split the tight noun phrase 'the Commonwealth Department'; defer it to the next window: [0,1,2]
  - release_units: None

* W1. {3: 'Department', 4: 'of', 5: 'Agriculture,'}
  - carried_over: {0: 'But', 1: 'the', 2: 'Commonwealth'}
  - defer: None
  - release_units:
    1. But the Commonwealth Department of Agriculture,, 'But the Commonwealth' is carried over; released here because it now forms a stable minimal sense unit (tight noun-centered frame with lead-in): [0,1,2,3,4,5]

* W2. {6: 'Fisheries', 7: 'and'}
  - carried_over: None
  - defer: 'Fisheries and' is not yet a stable unit; defer to next window: [6,7]
  - release_units: None

* W3. {8: 'Forestry', 9: 'had', 10: 'the'}
  - carried_over: {6: 'Fisheries', 7: 'and'}
  - defer: 'had the' is not yet a stable unit; defer to next window: [9,10]
  - release_units:
    1. Fisheries and Forestry, carried over 'Fisheries' and 'and'; released as a stable minimal sense unit (tight coordination): [6,7,8]

* W4. {11: 'foresight', 12: 'to'}
  - carried_over: {9: 'had', 10: 'the'}
  - defer: None
  - release_units:
    1. had the foresight to, carried over 'had' and 'the'; released as a stable minimal sense unit (verb phrase with object and infinitive): [9,10,11,12]

* W5. {13: 'identify', 14: 'the', 15: 'need', 16: 'for'}
  - carried_over: None
  - defer: None
  - release_units:
    1. identify the need for, stable minimal sense unit (verb phrase with object and preposition): [13,14,15,16]

* W6. {17: 'Australia', 18: 'to', 19: 'be'}
  - carried_over: None
  - defer: 'Australia to be' is not yet a stable unit; defer to next window: [17,18,19]
  - release_units: None

* W7. {20: 'ahead', 21: 'of', 22: 'the', 23: 'game'}
  - carried_over: {17: 'Australia', 18: 'to', 19: 'be'}
  - defer: None
  - release_units:
    1. Australia to be ahead of the game, carried over 'Australia to be'; released as a stable minimal sense unit (tight idiomatic phrase 'ahead of the game'): [17,18,19,20,21,22,23]

* W8. {24: 'and', 25: 'well'}
  - carried_over: None
  - defer: 'and well' is not yet a stable unit; defer to next window: [24,25]
  - release_units: None

* W9. {26: 'coordinated,', 27: 'and'}
  - carried_over: {24: 'and', 25: 'well'}
  - defer: 'and' (index 27) is not yet part of a stable unit; defer to next window: [27]
  - release_units:
    1. and well coordinated,, carried over 'and' and 'well'; released as a stable minimal sense unit (completing the coordination 'ahead of the game and well coordinated,'): [24,25,26]

* W10. {28: 'so', 29: 'developed', 30: 'the'}
  - carried_over: {27: 'and'}
  - defer: 'the' (index 30) does not yet form a stable unit; defer to next window: [30]
  - release_units:
    1. and so developed, carried over 'and'; released as a lead-in frame with clear local direction: [27,28,29]

* W11. {31: 'Australian', 32: 'Animal', 33: 'Welfare'}
  - carried_over: {30: 'the'}
  - defer: 'the Australian Animal Welfare' needs the head 'Strategy' to form a complete noun phrase; defer to next window: [30,31,32,33]
  - release_units: None

* W12. {34: 'Strategy', 35: 'eight'}
  - carried_over: {30: 'the', 31: 'Australian', 32: 'Animal', 33: 'Welfare'}
  - defer: 'eight' is not yet a stable unit; defer to next window: [35]
  - release_units:
    1. the Australian Animal Welfare Strategy, carried over 'the Australian Animal Welfare'; released as a stable minimal sense unit (complete noun phrase): [30,31,32,33,34]

* W13. {36: 'years', 37: 'ago.'}
  - carried_over: {35: 'eight'}
  - defer: None
  - release_units:
    1. eight years ago., carried over 'eight'; released as a stable minimal sense unit (adverbial phrase): [35,36,37]
  result:
[
  [0,1,2,3,4,5],
  [6,7,8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18,19,20,21,22,23],
  [24,25,26],
  [27,28,29],
  [30,31,32,33,34],
  [35,36,37]
]
  error:
Sense unit segmentation validation failed:
* W0. input: {0: 'But', 1: 'the', 2: 'Commonwealth'} - output: release_units None
* W1. input: {3: 'Department', 4: 'of', 5: 'Agriculture,'} - output: release_units 1.{0: 'But', 1: 'the', 2: 'Commonwealth', 3: 'Department', 4: 'of', 5: 'Agriculture,'}
* W2. input: {6: 'Fisheries', 7: 'and'} - output: release_units None
* W3. input: {8: 'Forestry', 9: 'had', 10: 'the'} - output: release_units 1.{6: 'Fisheries', 7: 'and', 8: 'Forestry'}
* W4. input: {11: 'foresight', 12: 'to'} - output: release_units 1.{9: 'had', 10: 'the', 11: 'foresight', 12: 'to'}
* W5. input: {13: 'identify', 14: 'the', 15: 'need', 16: 'for'} - output: release_units 1.{13: 'identify', 14: 'the', 15: 'need', 16: 'for'}
* W6. input: {17: 'Australia', 18: 'to', 19: 'be'} - output: release_units None
* W7. input: {20: 'ahead', 21: 'of', 22: 'the', 23: 'game'} - output: release_units 1.{17: 'Australia', 18: 'to', 19: 'be', 20: 'ahead', 21: 'of', 22: 'the', 23: 'game'} <- ISSUE2: oversized chunk release unit 1 size=7 > 6. Likely accumulated too much before emitting or packed too many tokens into one phrase.
* W8. input: {24: 'and', 25: 'well'} - output: release_units None
* W9. input: {26: 'coordinated,', 27: 'and'} - output: release_units 1.{24: 'and', 25: 'well', 26: 'coordinated,'}
* W10. input: {28: 'so', 29: 'developed', 30: 'the'} - output: release_units 1.{27: 'and', 28: 'so', 29: 'developed'}
* W11. input: {31: 'Australian', 32: 'Animal', 33: 'Welfare'} - output: release_units None
* W12. input: {34: 'Strategy', 35: 'eight'} - output: release_units 1.{30: 'the', 31: 'Australian', 32: 'Animal', 33: 'Welfare', 34: 'Strategy'}
* W13. input: {36: 'years', 37: 'ago.'} - output: release_units 1.{35: 'eight', 36: 'years', 37: 'ago.'}

Reconfirm the RULEs and your task!


- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded
  error:


parsed_asr_blocks:
```html
* W0. <src>But the Commonwealth </src>; start=0.00, end=1.00
* W1. <src>Department of Agriculture, </src>; start=1.00, end=2.00
* W2. <src><|wait|></src>; start=2.00, end=3.00
* W3. <src>Fisheries and Forestry </src>; start=3.00, end=4.00
* W4. <src>had the foresight to </src>; start=4.00, end=5.00
* W5. <src>identify the need for </src>; start=5.00, end=6.00
* W6. <src>Australia to be </src>; start=6.00, end=7.00
* W7. <src>ahead of the game </src>; start=7.00, end=8.00
* W8. <src><|wait|></src>; start=8.00, end=9.00
* W9. <src>and well coordinated, </src>; start=9.00, end=10.00
* W10. <src>and so developed the </src>; start=10.00, end=11.00
* W11. <src><|wait|></src>; start=11.00, end=12.00
* W12. <src>Australian Animal Welfare Strategy </src>; start=12.00, end=13.00
* W13. <src><|wait|></src>; start=13.00, end=13.66
```

---
