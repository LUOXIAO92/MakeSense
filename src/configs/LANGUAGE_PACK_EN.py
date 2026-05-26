# --- TIME WINDOW PRESSURED SEGMENTATION ---

TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

raw_text: "It's definitely something that I'd like to learn more about and I'm planning to hopefully use for part of a personal project for a new website redesign. But I think that's pretty much all I've got."

word_indices:
* W0. {0: "It's", 1: 'definitely', 2: 'something'}
* W1. {3: 'that', 4: "I'd", 5: 'like', 6: 'to', 7: 'learn', 8: 'more', 9: 'about'}
* W2. {10: 'and', 11: "I'm", 12: 'planning', 13: 'to'}
* W3. {14: 'hopefully', 15: 'use', 16: 'for'}
* W4. {17: 'part', 18: 'of', 19: 'a', 20: 'personal'}
* W5. {21: 'project', 22: 'for', 23: 'a', 24: 'new', 25: 'website'}
* W6. {}
* W7. {}
* W8. {}
* W9. {}
* W10. {26: 'redesign.', 27: 'But', 28: 'I', 29: 'think', 30: "that's", 31: 'pretty'}
* W11. {32: 'much', 33: 'all', 34: "I've", 35: 'got.'}

<scratchpad>
* W0. {0: "It's", 1: 'definitely', 2: 'something'}
  - carried_over: None
  - defer: 'something' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [2]
  - release_units:
    1. It's definitely, stable minimal sense unit in the current window: [0,1]

* W1. {3: 'that', 4: "I'd", 5: 'like', 6: 'to', 7: 'learn', 8: 'more', 9: 'about'}
  - carried_over: {2: 'something'}
  - defer: None
  - release_units:
    1. something that, 'something' is carried over from the previous window; released here because it is now a stable minimal sense unit: [2,3]
    2. I'd like to, stable minimal sense unit in the current window: [4,5,6]
    3. learn more about, stable minimal sense unit in the current window: [7,8,9]

* W2. {10: 'and', 11: "I'm", 12: 'planning', 13: 'to'}
  - carried_over: None
  - defer: None
  - release_units:
    1. and I'm planning to, stable minimal sense unit in the current window: [10,11,12,13]

* W3. {14: 'hopefully', 15: 'use', 16: 'for'}
  - carried_over: None
  - defer: None
  - release_units:
    1. hopefully use for, stable minimal sense unit in the current window: [14,15,16]

* W4. {17: 'part', 18: 'of', 19: 'a', 20: 'personal'}
  - carried_over: None
  - defer: 'part of a personal' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [17,18,19,20]
  - release_units: None

* W5. {21: 'project', 22: 'for', 23: 'a', 24: 'new', 25: 'website'}
  - carried_over: {17: 'part', 18: 'of', 19: 'a', 20: 'personal'}
  - defer: None
  - release_units:
    1. part of a personal project, 'part of a personal' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19,20,21]
    2. for a new website, stable minimal sense unit in the current window: [22,23,24,25]

* W6. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W7. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W8. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W9. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W10. {26: 'redesign.', 27: 'But', 28: 'I', 29: 'think', 30: "that's", 31: 'pretty'}
  - carried_over: None
  - defer: "that's pretty" is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [30,31]
  - release_units:
    1. redesign., stable minimal sense unit in the current window: [26]
    2. But I think, stable minimal sense unit in the current window: [27,28,29]

* W11. {32: 'much', 33: 'all', 34: "I've", 35: 'got.'}
  - carried_over: {30: "that's", 31: 'pretty'}
  - defer: None
  - release_units:
    1. that's pretty much, "that's pretty" is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32]
    2. all I've got., stable minimal sense unit in the current window: [33,34,35]
</scratchpad>
<result>
[
  [0,1],
  [2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12,13],
  [14,15,16],
  [17,18,19,20,21],
  [22,23,24,25],
  [26],
  [27,28,29],
  [30,31,32],
  [33,34,35]
]
</result>


## Sample 2:

raw_text: "These people are completely rare and they often show up to completely revolutionize the world. Their personality is something of a contradiction. While they're extroverted, they also hate meaningless conversations and like to get straight to the point. They also love to play the devil's advocate and they never shy away from a debate. ENTP stands for"

word_indices: 
* W0. {0: 'These', 1: 'people', 2: 'are'}
* W1. {3: 'completely', 4: 'rare'}
* W2. {5: 'and', 6: 'they', 7: 'often'}
* W3. {8: 'show', 9: 'up', 10: 'to'}
* W4. {11: 'completely'}
* W5. {12: 'revolutionize', 13: 'the'}
* W6. {14: 'world.', 15: 'Their'}
* W7. {16: 'personality', 17: 'is'}
* W8. {18: 'something', 19: 'of', 20: 'a'}
* W9. {}
* W10. {21: 'contradiction.', 22: 'While', 23: "they're"}
* W11. {24: 'extroverted,'}
* W12. {25: 'they', 26: 'also', 27: 'hate'}
* W13. {28: 'meaningless'}
* W14. {29: 'conversations', 30: 'and'}
* W15. {31: 'like', 32: 'to', 33: 'get'}
* W16. {34: 'straight', 35: 'to', 36: 'the'}
* W17. {}
* W18. {37: 'point.', 38: 'They', 39: 'also', 40: 'love', 41: 'to', 42: 'play'}
* W19. {43: 'the', 44: "devil's"}
* W20. {45: 'advocate', 46: 'and', 47: 'they'}
* W21. {48: 'never', 49: 'shy', 50: 'away'}
* W22. {51: 'from', 52: 'a'}
* W23. {53: 'debate.'}
* W24. {54: 'ENTP', 55: 'stands'}
* W25. {56: 'for'}

<scratchpad>
* W0. {0: 'These', 1: 'people', 2: 'are'}
  - carried_over: None
  - defer: None
  - release_units:
    1. These people are, stable minimal sense unit in the current window: [0,1,2]

* W1. {3: 'completely', 4: 'rare'}
  - carried_over: None
  - defer: None
  - release_units:
    1. completely rare, stable minimal sense unit in the current window: [3,4]

* W2. {5: 'and', 6: 'they', 7: 'often'}
  - carried_over: None
  - defer: None
  - release_units:
    1. and they often, stable minimal sense unit in the current window: [5,6,7]

* W3. {8: 'show', 9: 'up', 10: 'to'}
  - carried_over: None
  - defer: None
  - release_units:
    1. show up to, stable minimal sense unit in the current window: [8,9,10]

* W4. {11: 'completely'}
  - carried_over: None
  - defer: 'completely' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [11]
  - release_units: None

* W5. {12: 'revolutionize', 13: 'the'}
  - carried_over: {11: 'completely'}
  - defer: 'the' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [13]
  - release_units:
    1. completely revolutionize, 'completely' is carried over from the previous window; latency-forced partial release because waiting longer would violate output continuity: [11,12]

* W6. {14: 'world.', 15: 'Their'}
  - carried_over: {13: 'the'}
  - defer: 'Their' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [15]
  - release_units:
    1. the world., 'the' is carried over from the previous window; released here because it is now a stable minimal sense unit: [13,14]

* W7. {16: 'personality', 17: 'is'}
  - carried_over: {15: 'Their'}
  - defer: None
  - release_units:
    1. Their personality is, 'Their' is carried over from the previous window; released here because it is now a stable minimal sense unit: [15,16,17]

* W8. {18: 'something', 19: 'of', 20: 'a'}
  - carried_over: None
  - defer: 'something of a' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [18,19,20]
  - release_units: None

* W9. {}
  - carried_over: {18: 'something', 19: 'of', 20: 'a'}
  - defer: None
  - release_units:
    1. something of a, 'something of a' is carried over from the previous window; latency-forced partial release because waiting longer would violate output continuity: [18,19,20]

* W10. {21: 'contradiction.', 22: 'While', 23: "they're"}
  - carried_over: None
  - defer: "While they're" is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [22,23]
  - release_units:
    1. contradiction., stable minimal sense unit in the current window: [21]

* W11. {24: 'extroverted,'}
  - carried_over: {22: 'While', 23: "they're"}
  - defer: None
  - release_units:
    1. While they're extroverted, 'While they're' is carried over from the previous window; released here because it is now a stable minimal sense unit: [22,23,24]

* W12. {25: 'they', 26: 'also', 27: 'hate'}
  - carried_over: None
  - defer: None
  - release_units:
    1. they also hate, stable minimal sense unit in the current window: [25,26,27]

* W13. {28: 'meaningless'}
  - carried_over: None
  - defer: 'meaningless' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [28]
  - release_units: None

* W14. {29: 'conversations', 30: 'and'}
  - carried_over: {28: 'meaningless'}
  - defer: 'and' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [30]
  - release_units:
    1. meaningless conversations, 'meaningless' is carried over from the previous window; released here because it is now a stable minimal sense unit: [28,29]

* W15. {31: 'like', 32: 'to', 33: 'get'}
  - carried_over: {30: 'and'}
  - defer: None
  - release_units:
    1. and like to get, 'and' is carried over from the previous window; released here because it is now a stable minimal sense unit: [30,31,32,33]

* W16. {34: 'straight', 35: 'to', 36: 'the'}
  - carried_over: None
  - defer: 'straight to the' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [34,35,36]
  - release_units: None

* W17. {}
  - carried_over: {34: 'straight', 35: 'to', 36: 'the'}
  - defer: None
  - release_units:
    1. straight to the, 'straight to the' is carried over from the previous window; latency-forced partial release because waiting longer would violate output continuity: [34,35,36]

* W18. {37: 'point.', 38: 'They', 39: 'also', 40: 'love', 41: 'to', 42: 'play'}
  - carried_over: None
  - defer: None
  - release_units:
    1. point., stable minimal sense unit in the current window: [37]
    2. They also love to play, stable minimal sense unit in the current window: [38,39,40,41,42]

* W19. {43: 'the', 44: "devil's"}
  - carried_over: None
  - defer: 'the devil's' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [43,44]
  - release_units: None

* W20. {45: 'advocate', 46: 'and', 47: 'they'}
  - carried_over: {43: 'the', 44: "devil's"}
  - defer: 'and they' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [46,47]
  - release_units:
    1. the devil's advocate, 'the devil's' is carried over from the previous window; released here because it is now a stable minimal sense unit: [43,44,45]

* W21. {48: 'never', 49: 'shy', 50: 'away'}
  - carried_over: {46: 'and', 47: 'they'}
  - defer: None
  - release_units:
    1. and they never shy away, 'and they' is carried over from the previous window; released here because it is now a stable minimal sense unit: [46,47,48,49,50]

* W22. {51: 'from', 52: 'a'}
  - carried_over: None
  - defer: 'from a' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [51,52]
  - release_units: None

* W23. {53: 'debate.'}
  - carried_over: {51: 'from', 52: 'a'}
  - defer: None
  - release_units:
    1. from a debate., 'from a' is carried over from the previous window; released here because it is now a stable minimal sense unit: [51,52,53]

* W24. {54: 'ENTP', 55: 'stands'}
  - carried_over: None
  - defer: 'ENTP stands' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [54,55]
  - release_units: None

* W25. {56: 'for'}
  - carried_over: {54: 'ENTP', 55: 'stands'}
  - defer: None
  - release_units:
    1. ENTP stands for, 'ENTP stands' is carried over from the previous window; released here because it is now a stable minimal sense unit: [54,55,56]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4],
  [5,6,7],
  [8,9,10],
  [11,12],
  [13,14],
  [15,16,17],
  [18,19,20],
  [21],
  [22,23,24],
  [25,26,27],
  [28,29],
  [30,31,32,33],
  [34,35,36],
  [37],
  [38,39,40,41,42],
  [43,44,45],
  [46,47,48,49,50],
  [51,52,53],
  [54,55,56]
]
</result>


## Sample 3:

raw_text: "And that's the method that tells how many elements are currently in the ArrayList. If the number of prices is greater than zero, then we have work to do. Otherwise,"

word_indices: 
* W0. {0: 'And', 1: "that's", 2: 'the', 3: 'method'}
* W1. {4: 'that', 5: 'tells', 6: 'how', 7: 'many'}
* W2. {8: 'elements', 9: 'are', 10: 'currently'}
* W3. {11: 'in', 12: 'the'}
* W4. {}
* W5. {}
* W6. {13: 'ArrayList.', 14: 'If', 15: 'the', 16: 'number', 17: 'of'}
* W7. {18: 'prices', 19: 'is', 20: 'greater'}
* W8. {21: 'than', 22: 'zero,'}
* W9. {23: 'then', 24: 'we'}
* W10. {25: 'have', 26: 'work', 27: 'to'}
* W11. {}
* W12. {28: 'do.', 29: 'Otherwise,'}

<scratchpad>
* W0. {0: 'And', 1: "that's", 2: 'the', 3: 'method'}
  - carried_over: None
  - defer: None
  - release_units:
    1. And that's the method, stable minimal sense unit in the current window: [0,1,2,3]

* W1. {4: 'that', 5: 'tells', 6: 'how', 7: 'many'}
  - carried_over: None
  - defer: 'how many' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [6,7]
  - release_units:
    1. that tells, stable minimal sense unit in the current window: [4,5]

* W2. {8: 'elements', 9: 'are', 10: 'currently'}
  - carried_over: {6: 'how', 7: 'many'}
  - defer: 'currently' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [10]
  - release_units:
    1. how many elements are, 'how many' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7,8,9]

* W3. {11: 'in', 12: 'the'}
  - carried_over: {10: 'currently'}
  - defer: 'currently in the' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [10,11,12]
  - release_units: None

* W4. {}
  - carried_over: {10: 'currently', 11: 'in', 12: 'the'}
  - defer: None
  - release_units:
    1. currently in the, 'currently in the' is carried over from the previous window; latency-forced partial release because waiting longer would violate output continuity: [10,11,12]

* W5. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W6. {13: 'ArrayList.', 14: 'If', 15: 'the', 16: 'number', 17: 'of'}
  - carried_over: None
  - defer: 'If the number of' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [14,15,16,17]
  - release_units:
    1. ArrayList., stable minimal sense unit in the current window: [13]

* W7. {18: 'prices', 19: 'is', 20: 'greater'}
  - carried_over: {14: 'If', 15: 'the', 16: 'number', 17: 'of'}
  - defer: 'is greater' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [19,20]
  - release_units:
    1. If the number of prices, 'If the number of' is carried over from the previous window; released here because it is now a stable minimal sense unit: [14,15,16,17,18]

* W8. {21: 'than', 22: 'zero,'}
  - carried_over: {19: 'is', 20: 'greater'}
  - defer: None
  - release_units:
    1. is greater than zero,, 'is greater' is carried over from the previous window; released here because it is now a stable minimal sense unit: [19,20,21,22]

* W9. {23: 'then', 24: 'we'}
  - carried_over: None
  - defer: 'then we' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [23,24]
  - release_units: None

* W10. {25: 'have', 26: 'work', 27: 'to'}
  - carried_over: {23: 'then', 24: 'we'}
  - defer: 'to' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [27]
  - release_units:
    1. then we have work, 'then we' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25,26]

* W11. {}
  - carried_over: {27: 'to'}
  - defer: 'to' still does not yet form the best stable release unit / minimal sense unit in the current window; defer it to the next window because waiting one more window is required before it can form a stable local unit: [27]
  - release_units: None

* W12. {28: 'do.', 29: 'Otherwise,'}
  - carried_over: {27: 'to'}
  - defer: None
  - release_units:
    1. to do., 'to' is carried over from the previous window; released here because it is now a stable minimal sense unit: [27,28]
    2. Otherwise,, stable minimal sense unit in the current window: [29]
</scratchpad>
<result>
[
  [0,1,2,3],
  [4,5],
  [6,7,8,9],
  [10,11,12],
  [13],
  [14,15,16,17,18],
  [19,20,21,22],
  [23,24,25,26],
  [27,28],
  [29]
]
</result>


## Sample 4:

raw_text: "I wouldn't say we spent a lot of time deciding which of these three buckets to put certain things in, so I'm primarily going to just go down the list that we came up with at the end in terms of major areas of either priority or opportunity or"

word_indices: 
* W0. {}, 
* W1. {0: 'I'}, 
* W2. {}, 
* W3. {}, 
* W4. {}, 
* W5. {1: "wouldn't", 2: 'say', 3: 'we', 4: 'spent', 5: 'a'}
* W6. {6: 'lot', 7: 'of', 8: 'time'}
* W7. {9: 'deciding', 10: 'which', 11: 'of'}
* W8. {12: 'these', 13: 'three', 14: 'buckets', 15: 'to'}
* W9. {16: 'put', 17: 'certain', 18: 'things'}
* W10. {19: 'in,', 20: 'so', 21: "I'm"}
* W11. {22: 'primarily', 23: 'going', 24: 'to', 25: 'just'}
* W12. {26: 'go', 27: 'down', 28: 'the', 29: 'list'}
* W13. {30: 'that', 31: 'we'}
* W14. {32: 'came', 33: 'up', 34: 'with', 35: 'at', 36: 'the'}
* W15. {37: 'end', 38: 'in'}
* W16. {39: 'terms', 40: 'of'}
* W17. {41: 'major', 42: 'areas', 43: 'of'}
* W18. {44: 'either', 45: 'priority', 46: 'or'}
* W19. {47: 'opportunity', 48: 'or'}

<scratchpad>
* W0. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W1. {0: 'I'}
  - carried_over: None
  - defer: None
  - release_units:
    1. I, latency-forced partial release; empty windows follow, so further waiting would create excessive no-output delay: [0]

* W2. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W3. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W4. {}
  - carried_over: None
  - defer: None
  - release_units: None

* W5. {1: "wouldn't", 2: 'say', 3: 'we', 4: 'spent', 5: 'a'}
  - carried_over: None
  - defer: 'a' is not yet a stable release unit in the current window; defer it to the next window: [5]
  - release_units:
    1. wouldn't say, stable minimal sense unit in the current window: [1,2]
    2. we spent, stable minimal sense unit in the current window: [3,4]

* W6. {6: 'lot', 7: 'of', 8: 'time'}
  - carried_over: {5: 'a'}
  - defer: None
  - release_units:
    1. a lot of time, 'a' is carried over from the previous window; stable minimal sense unit in the current window: [5,6,7,8]

* W7. {9: 'deciding', 10: 'which', 11: 'of'}
  - carried_over: None
  - defer: None
  - release_units:
    1. deciding which of, stable minimal sense unit in the current window: [9,10,11]

* W8. {12: 'these', 13: 'three', 14: 'buckets', 15: 'to'}
  - carried_over: None
  - defer: 'to' is not yet a stable release unit in the current window; defer it to the next window: [15]
  - release_units:
    1. these three buckets, stable minimal sense unit in the current window: [12,13,14]

* W9. {16: 'put', 17: 'certain', 18: 'things'}
  - carried_over: {15: 'to'}
  - defer: 'to put certain things' is not yet the best stable minimal sense unit in the current window; defer it to the next window: [15,16,17,18]
  - release_units: None

* W10. {19: 'in,', 20: 'so', 21: "I'm"}
  - carried_over: {15: 'to', 16: 'put', 17: 'certain', 18: 'things'}
  - defer: None
  - release_units:
    1. to put certain things in,, 'to put certain things' is carried over from the previous window; stable minimal sense unit in the current window: [15,16,17,18,19]
    2. so I'm, stable minimal sense unit in the current window: [20,21]

* W11. {22: 'primarily', 23: 'going', 24: 'to', 25: 'just'}
  - carried_over: None
  - defer: 'just' is not yet a stable release unit in the current window; defer it to the next window: [25]
  - release_units:
    1. primarily going to, stable minimal sense unit in the current window: [22,23,24]

* W12. {26: 'go', 27: 'down', 28: 'the', 29: 'list'}
  - carried_over: {25: 'just'}
  - defer: None
  - release_units:
    1. just go down the list, 'just' is carried over from the previous window; stable minimal sense unit in the current window: [25,26,27,28,29]

* W13. {30: 'that', 31: 'we'}
  - carried_over: None
  - defer: 'that we' is not yet a stable release unit in the current window; defer it to the next window: [30,31]
  - release_units: None

* W14. {32: 'came', 33: 'up', 34: 'with', 35: 'at', 36: 'the'}
  - carried_over: {30: 'that', 31: 'we'}
  - defer: 'at the' is not yet a stable release unit in the current window; defer it to the next window: [35,36]
  - release_units:
    1. that we came up with, 'that we' is carried over from the previous window; stable minimal sense unit in the current window: [30,31,32,33,34]

* W15. {37: 'end', 38: 'in'}
  - carried_over: {35: 'at', 36: 'the'}
  - defer: 'in' is not yet a stable release unit in the current window; defer it to the next window: [38]
  - release_units:
    1. at the end, 'at the' is carried over from the previous window; stable minimal sense unit in the current window: [35,36,37]

* W16. {39: 'terms', 40: 'of'}
  - carried_over: {38: 'in'}
  - defer: None
  - release_units:
    1. in terms of, 'in' is carried over from the previous window; stable minimal sense unit in the current window: [38,39,40]

* W17. {41: 'major', 42: 'areas', 43: 'of'}
  - carried_over: None
  - defer: None
  - release_units:
    1. major areas of, stable minimal sense unit in the current window: [41,42,43]

* W18. {44: 'either', 45: 'priority', 46: 'or'}
  - carried_over: None
  - defer: 'either priority or' is not yet a stable minimal sense unit in the current window; defer it to the next window: [44,45,46]
  - release_units: None

* W19. {47: 'opportunity', 48: 'or'}
  - carried_over: {44: 'either', 45: 'priority', 46: 'or'}
  - defer: None
  - release_units:
    1. either priority or opportunity or, 'either priority or' is carried over from the previous window; latency-forced partial release at stream end because the source itself cuts off mid-coordination: [44,45,46,47,48]
</scratchpad>
<result>
[
  [0],
  [1,2],
  [3,4],
  [5,6,7,8],
  [9,10,11],
  [12,13,14],
  [15,16,17,18,19],
  [20,21],
  [22,23,24],
  [25,26,27,28,29],
  [30,31,32,33,34],
  [35,36,37],
  [38,39,40],
  [41,42,43],
  [44,45,46,47,48]
]
</result>


## Sample 5:

raw_text: "MuseScore 4 is the result of a dedicated collaboration between my team and the open source community, who provided us with endless help on design and implementation, as well as translations, documentation, and support for users. For those who want to get up and running as fast as possible, we've released multiple tutorials which can be accessed from within MuseScore 4 itself, or by searching this channel."

Word_indices:
* W0. {0: 'MuseScore', 1: '4', 2: 'is'}
* W1. {3: 'the', 4: 'result', 5: 'of', 6: 'a'}
* W2. {7: 'dedicated', 8: 'collaboration'}
* W3. {9: 'between', 10: 'my', 11: 'team'}
* W4. {12: 'and', 13: 'the', 14: 'open', 15: 'source'}
* W5. {16: 'community,', 17: 'who'}
* W6. {18: 'provided', 19: 'us', 20: 'with', 21: 'endless'}
* W7. {22: 'help', 23: 'on', 24: 'design', 25: 'and'}
* W8. {26: 'implementation,'}
* W9. {27: 'as', 28: 'well', 29: 'as'}
* W10. {30: 'translations,'}
* W11. {31: 'documentation,', 32: 'and', 33: 'support', 34: 'for'}
* W12. {35: 'users.', 36: 'For'}
* W13. {37: 'those', 38: 'who', 39: 'want', 40: 'to', 41: 'get', 42: 'up', 43: 'and'}
* W14. {44: 'running', 45: 'as', 46: 'fast', 47: 'as', 48: 'possible,'}
* W15. {49: "we've", 50: 'released'}
* W16. {51: 'multiple', 52: 'tutorials'}
* W17. {53: 'which', 54: 'can', 55: 'be', 56: 'accessed', 57: 'from'}
* W18. {58: 'within', 59: 'MuseScore', 60: '4'}
* W19. {61: 'itself,', 62: 'or', 63: 'by'}
* W20. {64: 'searching', 65: 'this', 66: 'channel.'}

<scratchpad>
* W0. {0: 'MuseScore', 1: '4', 2: 'is'}
  - carried_over: None
  - defer: None
  - release_units:
    1. MuseScore 4 is, stable minimal sense unit in the current window: [0,1,2]

* W1. {3: 'the', 4: 'result', 5: 'of', 6: 'a'}
  - carried_over: None
  - defer: 'a' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [6]
  - release_units:
    1. the result of, stable minimal sense unit in the current window: [3,4,5]

* W2. {7: 'dedicated', 8: 'collaboration'}
  - carried_over: {6: 'a'}
  - defer: None
  - release_units:
    1. a dedicated collaboration, 'a' is carried over from the previous window; released here because it is now a stable minimal sense unit: [6,7,8]

* W3. {9: 'between', 10: 'my', 11: 'team'}
  - carried_over: None
  - defer: None
  - release_units:
    1. between my team, stable minimal sense unit in the current window: [9,10,11]

* W4. {12: 'and', 13: 'the', 14: 'open', 15: 'source'}
  - carried_over: None
  - defer: 'and the open source' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [12,13,14,15]
  - release_units: None

* W5. {16: 'community,', 17: 'who'}
  - carried_over: {12: 'and', 13: 'the', 14: 'open', 15: 'source'}
  - defer: 'who' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [17]
  - release_units:
    1. and the open source community,, 'and the open source' is carried over from the previous window; released here because it is now a stable minimal sense unit: [12,13,14,15,16]

* W6. {18: 'provided', 19: 'us', 20: 'with', 21: 'endless'}
  - carried_over: {17: 'who'}
  - defer: 'endless' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [21]
  - release_units:
    1. who provided us with, 'who' is carried over from the previous window; released here because it is now a stable minimal sense unit: [17,18,19,20]

* W7. {22: 'help', 23: 'on', 24: 'design', 25: 'and'}
  - carried_over: {21: 'endless'}
  - defer: 'on design and' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [23,24,25]
  - release_units:
    1. endless help, 'endless' is carried over from the previous window; released here because it is now a stable minimal sense unit: [21,22]

* W8. {26: 'implementation,'}
  - carried_over: {23: 'on', 24: 'design', 25: 'and'}
  - defer: None
  - release_units:
    1. on design and implementation,, 'on design and' is carried over from the previous window; released here because it is now a stable minimal sense unit: [23,24,25,26]

* W9. {27: 'as', 28: 'well', 29: 'as'}
  - carried_over: None
  - defer: None
  - release_units:
    1. as well as, stable minimal sense unit in the current window: [27,28,29]

* W10. {30: 'translations,'}
  - carried_over: None
  - defer: None
  - release_units:
    1. translations,, stable minimal sense unit in the current window: [30]

* W11. {31: 'documentation,', 32: 'and', 33: 'support', 34: 'for'}
  - carried_over: None
  - defer: None
  - release_units:
    1. documentation,, stable minimal sense unit in the current window: [31]
    2. and support for, stable minimal sense unit in the current window: [32,33,34]

* W12. {35: 'users.', 36: 'For'}
  - carried_over: None
  - defer: 'For' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [36]
  - release_units:
    1. users., stable minimal sense unit in the current window: [35]

* W13. {37: 'those', 38: 'who', 39: 'want', 40: 'to', 41: 'get', 42: 'up', 43: 'and'}
  - carried_over: {36: 'For'}
  - defer: 'get up and' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [41,42,43]
  - release_units:
    1. For those who want to, 'For' is carried over from the previous window; released here because it is now a stable minimal sense unit: [36,37,38,39,40]

* W14. {44: 'running', 45: 'as', 46: 'fast', 47: 'as', 48: 'possible,'}
  - carried_over: {41: 'get', 42: 'up', 43: 'and'}
  - defer: None
  - release_units:
    1. get up and running, 'get up and' is carried over from the previous window; released here because it is now a stable minimal sense unit: [41,42,43,44]
    2. as fast as possible,, stable minimal sense unit in the current window: [45,46,47,48]

* W15. {49: "we've", 50: 'released'}
  - carried_over: None
  - defer: None
  - release_units:
    1. we've released, stable minimal sense unit in the current window: [49,50]

* W16. {51: 'multiple', 52: 'tutorials'}
  - carried_over: None
  - defer: None
  - release_units:
    1. multiple tutorials, stable minimal sense unit in the current window: [51,52]

* W17. {53: 'which', 54: 'can', 55: 'be', 56: 'accessed', 57: 'from'}
  - carried_over: None
  - defer: None
  - release_units:
    1. which can be accessed from, stable minimal sense unit in the current window: [53,54,55,56,57]

* W18. {58: 'within', 59: 'MuseScore', 60: '4'}
  - carried_over: None
  - defer: None
  - release_units:
    1. within MuseScore 4, stable minimal sense unit in the current window: [58,59,60]

* W19. {61: 'itself,', 62: 'or', 63: 'by'}
  - carried_over: None
  - defer: 'or by' is not yet a stable release unit / minimal sense unit in the current window; defer it to the next window: [62,63]
  - release_units:
    1. itself,, non-ideal release unit; after the earlier local unit `within MuseScore 4` has already been released, `itself,` is left as the remaining continuation and is released here rather than delaying the stream for a larger re-grouping: [61]

* W20. {64: 'searching', 65: 'this', 66: 'channel.'}
  - carried_over: {62: 'or', 63: 'by'}
  - defer: None
  - release_units:
    1. or by searching, 'or by' is carried over from the previous window; released here because it is now a stable minimal sense unit: [62,63,64]
    2. this channel., stable minimal sense unit in the current window: [65,66]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11],
  [12,13,14,15,16],
  [17,18,19,20],
  [21,22],
  [23,24,25,26],
  [27,28,29],
  [30],
  [31],
  [32,33,34],
  [35],
  [36,37,38,39,40],
  [41,42,43,44],
  [45,46,47,48],
  [49,50],
  [51,52],
  [53,54,55,56,57],
  [58,59,60],
  [61],
  [62,63,64],
  [65,66]
]
</result>
""".lstrip("\n")


# --- PURE TEXT SEGMENTATION ---

PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES = """
## Sample 1:

token_indices:
{0: "It's", 1: 'definitely', 2: 'something', 3: 'that', 4: "I'd", 5: 'like', 6: 'to', 7: 'learn', 8: 'more', 9: 'about', 10: 'and', 11: "I'm", 12: 'planning', 13: 'to', 14: 'hopefully', 15: 'use', 16: 'for', 17: 'part', 18: 'of', 19: 'a', 20: 'personal', 21: 'project', 22: 'for', 23: 'a', 24: 'new', 25: 'website', 26: 'redesign.', 27: 'But', 28: 'I', 29: 'think', 30: "that's", 31: 'pretty', 32: 'much', 33: 'all', 34: "I've", 35: 'got.'}

<scratchpad>
1. It's definitely
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [0, 1]

2. something that
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [2, 3]

3. I'd like to
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [4, 5, 6]

4. learn more about
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [7, 8, 9]

5. and I'm planning to
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [10, 11, 12, 13]

6. hopefully use for
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [14, 15, 16]

7. part of a personal project
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [17, 18, 19, 20, 21]

8. for a new website
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [22, 23, 24, 25]

9. redesign.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [26]

10. But I think
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [27, 28, 29]

11. that's pretty much
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [30, 31, 32]

12. all I've got.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [33, 34, 35]
</scratchpad>
<result>
[
  [0,1],
  [2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12,13],
  [14,15,16],
  [17,18,19,20,21],
  [22,23,24,25],
  [26],
  [27,28,29],
  [30,31,32],
  [33,34,35]
]
</result>


## Sample 2:

token_indices:
{0: 'These', 1: 'people', 2: 'are', 3: 'completely', 4: 'rare', 5: 'and', 6: 'they', 7: 'often', 8: 'show', 9: 'up', 10: 'to', 11: 'completely', 12: 'revolutionize', 13: 'the', 14: 'world.', 15: 'Their', 16: 'personality', 17: 'is', 18: 'something', 19: 'of', 20: 'a', 21: 'contradiction.', 22: 'While', 23: "they're", 24: 'extroverted,', 25: 'they', 26: 'also', 27: 'hate', 28: 'meaningless', 29: 'conversations', 30: 'and', 31: 'like', 32: 'to', 33: 'get', 34: 'straight', 35: 'to', 36: 'the', 37: 'point.', 38: 'They', 39: 'also', 40: 'love', 41: 'to', 42: 'play', 43: 'the', 44: "devil's", 45: 'advocate', 46: 'and', 47: 'they', 48: 'never', 49: 'shy', 50: 'away', 51: 'from', 52: 'a', 53: 'debate.', 54: 'ENTP', 55: 'stands', 56: 'for'}

<scratchpad>
1. These people are
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [0, 1, 2]

2. completely rare
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [3, 4]

3. and they often
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [5, 6, 7]

4. show up to
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [8, 9, 10]

5. completely revolutionize
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [11, 12]

6. the world.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [13, 14]

7. Their personality is
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [15, 16, 17]

8. something of a
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [18, 19, 20]

9. contradiction.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [21]

10. While they're extroverted,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [22, 23, 24]

11. they also hate
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [25, 26, 27]

12. meaningless conversations
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [28, 29]

13. and like to get
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [30, 31, 32, 33]

14. straight to the
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [34, 35, 36]

15. point.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [37]

16. They also love to play
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [38, 39, 40, 41, 42]

17. the devil's advocate
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [43, 44, 45]

18. and they never shy away
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [46, 47, 48, 49, 50]

19. from a debate.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [51, 52, 53]

20. ENTP stands for
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [54, 55, 56]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4],
  [5,6,7],
  [8,9,10],
  [11,12],
  [13,14],
  [15,16,17],
  [18,19,20],
  [21],
  [22,23,24],
  [25,26,27],
  [28,29],
  [30,31,32,33],
  [34,35,36],
  [37],
  [38,39,40,41,42],
  [43,44,45],
  [46,47,48,49,50],
  [51,52,53],
  [54,55,56]
]
</result>


## Sample 3:

token_indices:
{0: 'And', 1: "that's", 2: 'the', 3: 'method', 4: 'that', 5: 'tells', 6: 'how', 7: 'many', 8: 'elements', 9: 'are', 10: 'currently', 11: 'in', 12: 'the', 13: 'ArrayList.', 14: 'If', 15: 'the', 16: 'number', 17: 'of', 18: 'prices', 19: 'is', 20: 'greater', 21: 'than', 22: 'zero,', 23: 'then', 24: 'we', 25: 'have', 26: 'work', 27: 'to', 28: 'do.', 29: 'Otherwise,'}

<scratchpad>
1. And that's the method
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [0, 1, 2, 3]

2. that tells
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [4, 5]

3. how many elements are
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [6, 7, 8, 9]

4. currently in the
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [10, 11, 12]

5. ArrayList.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [13]

6. If the number of prices
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [14, 15, 16, 17, 18]

7. is greater than zero,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [19, 20, 21, 22]

8. then we have work
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [23, 24, 25, 26]

9. to do.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [27, 28]

10. Otherwise,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [29]
</scratchpad>
<result>
[
  [0,1,2,3],
  [4,5],
  [6,7,8,9],
  [10,11,12],
  [13],
  [14,15,16,17,18],
  [19,20,21,22],
  [23,24,25,26],
  [27,28],
  [29]
]
</result>


## Sample 4:

token_indices:
{0: 'I', 1: "wouldn't", 2: 'say', 3: 'we', 4: 'spent', 5: 'a', 6: 'lot', 7: 'of', 8: 'time', 9: 'deciding', 10: 'which', 11: 'of', 12: 'these', 13: 'three', 14: 'buckets', 15: 'to', 16: 'put', 17: 'certain', 18: 'things', 19: 'in,', 20: 'so', 21: "I'm", 22: 'primarily', 23: 'going', 24: 'to', 25: 'just', 26: 'go', 27: 'down', 28: 'the', 29: 'list', 30: 'that', 31: 'we', 32: 'came', 33: 'up', 34: 'with', 35: 'at', 36: 'the', 37: 'end', 38: 'in', 39: 'terms', 40: 'of', 41: 'major', 42: 'areas', 43: 'of', 44: 'either', 45: 'priority', 46: 'or', 47: 'opportunity', 48: 'or'}

<scratchpad>
1. I
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [0]

2. wouldn't say
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [1, 2]

3. we spent
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [3, 4]

4. a lot of time
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [5, 6, 7, 8]

5. deciding which of
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [9, 10, 11]

6. these three buckets
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [12, 13, 14]

7. to put certain things in,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [15, 16, 17, 18, 19]

8. so I'm
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [20, 21]

9. primarily going to
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [22, 23, 24]

10. just go down the list
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [25, 26, 27, 28, 29]

11. that we came up with
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [30, 31, 32, 33, 34]

12. at the end
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [35, 36, 37]

13. in terms of
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [38, 39, 40]

14. major areas of
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [41, 42, 43]

15. either priority or opportunity or
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [44, 45, 46, 47, 48]
</scratchpad>
<result>
[
  [0],
  [1,2],
  [3,4],
  [5,6,7,8],
  [9,10,11],
  [12,13,14],
  [15,16,17,18,19],
  [20,21],
  [22,23,24],
  [25,26,27,28,29],
  [30,31,32,33,34],
  [35,36,37],
  [38,39,40],
  [41,42,43],
  [44,45,46,47,48]
]
</result>


## Sample 5:

token_indices:
{0: 'MuseScore', 1: '4', 2: 'is', 3: 'the', 4: 'result', 5: 'of', 6: 'a', 7: 'dedicated', 8: 'collaboration', 9: 'between', 10: 'my', 11: 'team', 12: 'and', 13: 'the', 14: 'open', 15: 'source', 16: 'community,', 17: 'who', 18: 'provided', 19: 'us', 20: 'with', 21: 'endless', 22: 'help', 23: 'on', 24: 'design', 25: 'and', 26: 'implementation,', 27: 'as', 28: 'well', 29: 'as', 30: 'translations,', 31: 'documentation,', 32: 'and', 33: 'support', 34: 'for', 35: 'users.', 36: 'For', 37: 'those', 38: 'who', 39: 'want', 40: 'to', 41: 'get', 42: 'up', 43: 'and', 44: 'running', 45: 'as', 46: 'fast', 47: 'as', 48: 'possible,', 49: "we've", 50: 'released', 51: 'multiple', 52: 'tutorials', 53: 'which', 54: 'can', 55: 'be', 56: 'accessed', 57: 'from', 58: 'within', 59: 'MuseScore', 60: '4', 61: 'itself,', 62: 'or', 63: 'by', 64: 'searching', 65: 'this', 66: 'channel.'}

<scratchpad>
1. MuseScore 4 is
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [0, 1, 2]

2. the result of
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [3, 4, 5]

3. a dedicated collaboration
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [6, 7, 8]

4. between my team
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [9, 10, 11]

5. and the open source community,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [12, 13, 14, 15, 16]

6. who provided us with
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [17, 18, 19, 20]

7. endless help
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [21, 22]

8. on design and implementation,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [23, 24, 25, 26]

9. as well as
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [27, 28, 29]

10. translations,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [30]

11. documentation,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [31]

12. and support for
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [32, 33, 34]

13. users.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [35]

14. For those who want to
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [36, 37, 38, 39, 40]

15. get up and running
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [41, 42, 43, 44]

16. as fast as possible,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [45, 46, 47, 48]

17. we've released
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [49, 50]

18. multiple tutorials
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [51, 52]

19. which can be accessed from
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [53, 54, 55, 56, 57]

20. within MuseScore 4
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [58, 59, 60]

21. itself,
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [61]

22. or by searching
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [62, 63, 64]

23. this channel.
   - reason: stable minimal sense unit; preserves the uploaded fine-grained English local unit
   - sense_unit: [65, 66]
</scratchpad>
<result>
[
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11],
  [12,13,14,15,16],
  [17,18,19,20],
  [21,22],
  [23,24,25,26],
  [27,28,29],
  [30],
  [31],
  [32,33,34],
  [35],
  [36,37,38,39,40],
  [41,42,43,44],
  [45,46,47,48],
  [49,50],
  [51,52],
  [53,54,55,56,57],
  [58,59,60],
  [61],
  [62,63,64],
  [65,66]
]
</result>
""".lstrip("\n")


# --- ENGLISH LANGUAGE PACK (Minimal Incremental Patch) ---

GENERAL_LANGUAGE_PACK = """
## ENGLISH LANGUAGE PACK (Minimal Incremental Patch)

### Core Bias

In English, prefer **small locally stable meaning units**, not larger clause-sized or sentence-sized spans.

A unit does **not** need full grammatical closure to be releasable.
A unit is often valid as soon as it forms a **tight local frame**.

---

### Protect These Tight Local Units

Prefer not to split the following unless window pressure forces it:

- **phrasal verbs**
- **verb + particle / verb + particle + preposition units**
- **`to + verb` units**
- **short verb-object units**
- **short prepositional units**
- **fixed collocations**
- **comparison / quantity units**
- **compact noun units**
- **noun-centered local frames**
- **short coordination / correlative frames**
- **short lead-in frames with clear local direction**

---

### Especially Important in English

#### 1. Noun-centered local frames

English often forms stable local units around a noun head plus a nearby relational tail.

These may already be stable even if they remain open to later continuation.

Typical examples:
- `the result of`
- `major areas of`
- `support for`
- `a lot of time`
- `these three buckets`
- `the open source community`

Do **not** wait for a larger noun phrase just because the frame could continue.

#### 2. Open-ended but already stable frames

A unit should **not** be rejected only because it ends in a function word such as:
- `of`
- `to`
- `for`
- `from`
- `or`

If the whole span already forms a tight English local frame, it may still be releasable.

Typical examples:
- `show up to`
- `learn more about`
- `in terms of`
- `which can be accessed from`
- `and support for`

#### 3. Coordination / correlative frames

English frequently uses small local coordination frames that should stay intact when possible.

Typical examples:
- `as well as`
- `design and implementation`
- `either priority or`
- `or by searching`

Do not break these too early unless latency pressure forces it.

#### 4. Lead-in frames

English may release short lead-in units when they already provide clear local direction.

Typical examples:
- `But I think`
- `so I'm`
- `For those who`
- `who provided us with`
- `which can be accessed`

These are valid because they already advance interpretation, not because they are fully closed.

---

### Do Not Expose Bare Function Words

Avoid releasing these by themselves unless latency pressure leaves no better option:

- bare articles: `a`, `an`, `the`
- bare prepositions: `in`, `of`, `to`, `from`, `for`
- bare determiners
- bare coordinators or relational tails

But note:

A **bare function word** is bad.
A **stable local frame ending in a function word** may still be good.

---

### Typical Stable English Units

Examples of unit types that are often stable enough for release:

- `show up to`
- `came up with`
- `stands for`
- `shy away from`
- `I'd like to`
- `going to`
- `want to`
- `we spent`
- `a lot of time`
- `the result of`
- `in terms of`
- `as well as`
- `greater than zero`
- `as fast as possible`
- `get up and running`
- `which can be accessed from`

---

### English-Specific Failure Modes to Avoid

Do not drift back to:

- clause-sized segmentation
- relative-clause-sized segmentation
- comma-sized segmentation
- waiting for larger grammatical closure just because it looks cleaner
- rejecting a unit only because it is still slightly open
- mechanically splitting a tight local frame just to make the chunk smaller

---

### Practical English Bias

If two cuts are both legal, prefer the one that preserves the tighter English local unit:

- tighter phrasal verb
- tighter `to + verb` unit
- tighter verb-object unit
- tighter prepositional unit
- tighter noun-centered frame
- tighter coordination / correlative frame
- tighter quantity / comparison unit
- tighter lead-in frame with clear local direction
""".lstrip("\n")