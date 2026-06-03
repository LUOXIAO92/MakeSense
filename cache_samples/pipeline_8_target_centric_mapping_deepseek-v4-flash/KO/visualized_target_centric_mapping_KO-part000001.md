=== KO_GazVxt6TX_8_W000008 ===

source:
- language: Korean
- transcription: 다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.
- source_tokens:
  0. 다
  1. 마귀를
  2. 따르
  3. 면
  4. 망할
  5. 수는
  6. 있지만,
  7. 그렇
  8. 죠?
  9. 뭐
  10. 교회
  11. 십일조가
  12. 줄어서
  13. 망하
  14. 고
  15. 할
  16. 일이
  17. 아닙니다.
  18. 그리고
  19. 이
  20. 지상
  21. 에서
  22. 할
  23. 일은
  24. 끝없이
  25. 이
  26. 천국
  27. 을
  28. 확장
  29. 시켜가.

target:
- language: Japanese
- translation: 悪魔に従えば滅びることもあるでしょう。そうですよね？ですが、教会の什一献金が減って滅びる話ではありません。そして、この地上でやるべきことは、この天国を絶え間なく広げていくことです。
- target_sense_units:
  0. 悪魔に従えば
  1. 滅びることもあるでしょう。
  2. そうですよね？
  3. ですが、
  4. 教会の什一献金が
  5. 減って滅びる
  6. 話ではありません。
  7. そして、
  8. この地上で
  9. やるべきことは、
  10. この天国を
  11. 絶え間なく
  12. 広げていく
  13. ことです。

scratchpad:
* target[0]: "悪魔に従えば"
  - source_tokens: `1: "마귀를", 2: "따르", 3: "면"`
  - mapping_reason: "마귀(悪魔)를 따르다(従う) + 조건(~면)"

* target[1]: "滅びることもあるでしょう。"
  - source_tokens: `4: "망할", 5: "수는", 6: "있지만,", 0: "다"`
  - mapping_reason: "망할(滅びる) + 수(것) + 있지만(こともあるでしょう) + 다(all/emphasizer)"

* target[2]: "そうですよね？"
  - source_tokens: `7: "그렇", 8: "죠?"`
  - mapping_reason: "그렇죠?(そうですよね？)"

* target[3]: "ですが、"
  - source_tokens: `9: "뭐"`
  - mapping_reason: "뭐(discourse marker/but)"

* target[4]: "教会の什一献金が"
  - source_tokens: `10: "교회", 11: "십일조가"`
  - mapping_reason: "교회(教会) + 십일조(什一献金)"

* target[5]: "減って滅びる"
  - source_tokens: `12: "줄어서", 13: "망하", 14: "고"`
  - mapping_reason: "줄어서(減って) + 망하고(滅びる)"

* target[6]: "話ではありません。"
  - source_tokens: `15: "할", 16: "일이", 17: "아닙니다."`
  - mapping_reason: "할 일이 아니다(話ではない)"

* target[7]: "そして、"
  - source_tokens: `18: "그리고"`
  - mapping_reason: "그리고(そして)"

* target[8]: "この地上で"
  - source_tokens: `19: "이", 20: "지상", 21: "에서"`
  - mapping_reason: "이(この) + 지상(地上) + 에서(で)"

* target[9]: "やるべきことは、"
  - source_tokens: `22: "할", 23: "일은"`
  - mapping_reason: "할 일(やるべきこと)"

* target[10]: "この天国を"
  - source_tokens: `25: "이", 26: "천국", 27: "을"`
  - mapping_reason: "이(この) + 천국(天国) + 을(を)"

* target[11]: "絶え間なく"
  - source_tokens: `24: "끝없이"`
  - mapping_reason: "끝없이(絶え間なく)"

* target[12]: "広げていく"
  - source_tokens: `28: "확장", 29: "시켜가."`
  - mapping_reason: "확장시켜가(広げていく)"

* target[13]: "ことです。"
  - source_tokens: `23: "일은"`
  - mapping_reason: "일은(こと - nominalizer structure)"

result:
```html
0. <src>다 마귀를 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>따르 면 </src> <tgt>悪魔に従えば</tgt>; start=1.00, end=2.00
2. <src>망할 수는 있지만, </src> <tgt>滅びることもあるでしょう。</tgt>; start=2.00, end=3.00
3. <src>그렇 죠? 뭐 </src> <tgt>そうですよね？ですが、</tgt>; start=3.00, end=4.00
4. <src>교회 십일조가 줄어서 </src> <tgt>教会の什一献金が</tgt>; start=4.00, end=5.00
5. <src>망하 고 </src> <tgt>減って滅びる</tgt>; start=5.00, end=6.00
6. <src>할 일이 아닙니다. 그리고 </src> <tgt>話ではありません。そして、</tgt>; start=6.00, end=7.00
7. <src>이 지상 에서 할 일은 </src> <tgt>この地上でやるべきことは、</tgt>; start=7.00, end=8.00
8. <src>끝없이 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>이 천국 을 </src> <tgt>この天国を絶え間なく</tgt>; start=9.00, end=10.00
10. <src>확장 시켜가. </src> <tgt>広げていくことです。</tgt>; start=10.00, end=10.39
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_GazVxt6TX_8_W000008 ===

source:
- language: Korean
- transcription: 다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.
- source_tokens:
  0. 다
  1. 마귀를
  2. 따르
  3. 면
  4. 망할
  5. 수는
  6. 있지만,
  7. 그렇
  8. 죠?
  9. 뭐
  10. 교회
  11. 십일조가
  12. 줄어서
  13. 망하
  14. 고
  15. 할
  16. 일이
  17. 아닙니다.
  18. 그리고
  19. 이
  20. 지상
  21. 에서
  22. 할
  23. 일은
  24. 끝없이
  25. 이
  26. 천국
  27. 을
  28. 확장
  29. 시켜가.

target:
- language: English
- translation: Following the devil might lead to ruin, right? But that's not about ruin from a decrease in church tithes. And our task here on this earth is to endlessly expand this kingdom of heaven.
- target_sense_units:
  0. Following the devil
  1. might lead to
  2. ruin,
  3. right?
  4. But that's not about
  5. ruin
  6. from a decrease
  7. in church tithes.
  8. And our task
  9. here on this earth
  10. is to
  11. endlessly expand
  12. this kingdom of heaven.

scratchpad:
* target[0]: "Following the devil"
  - source_tokens: `1: "마귀를", 2: "따르"`
  - mapping_reason: "Following" maps to "따르", "the devil" maps to "마귀를".

* target[1]: "might lead to"
  - source_tokens: `3: "면", 5: "수는"`
  - mapping_reason: Expresses the conditional possibility of the preceding clause.

* target[2]: "ruin,"
  - source_tokens: `4: "망할"`
  - mapping_reason: Direct translation of "ruin".

* target[3]: "right?"
  - source_tokens: `7: "그렇", 8: "죠?"`
  - mapping_reason: Confirmation marker.

* target[4]: "But that's not about"
  - source_tokens: `6: "있지만,", 9: "뭐", 17: "아닙니다."`
  - mapping_reason: Contrastive conjunction and negation of the topic.

* target[5]: "ruin"
  - source_tokens: `13: "망하"`
  - mapping_reason: Repetition of the concept of ruin.

* target[6]: "from a decrease"
  - source_tokens: `12: "줄어서"`
  - mapping_reason: Causality of the decrease.

* target[7]: "in church tithes."
  - source_tokens: `10: "교회", 11: "십일조가"`
  - mapping_reason: Object of the decrease.

* target[8]: "And our task"
  - source_tokens: `18: "그리고", 22: "할", 23: "일은"`
  - mapping_reason: Discourse connector and the subject "task".

* target[9]: "here on this earth"
  - source_tokens: `19: "이", 20: "지상", 21: "에서"`
  - mapping_reason: Spatial location.

* target[10]: "is to"
  - source_tokens: `14: "고", 15: "할", 16: "일이"`
  - mapping_reason: Copula/linking structure.

* target[11]: "endlessly expand"
  - source_tokens: `24: "끝없이", 28: "확장", 29: "시켜가."`
  - mapping_reason: Adverbial modifier and verb.

* target[12]: "this kingdom of heaven."
  - source_tokens: `25: "이", 26: "천국", 27: "을"`
  - mapping_reason: Object of the expansion.

result:
```html
0. <src>다 마귀를 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>따르 면 </src> <tgt>Following the devil</tgt>; start=1.00, end=2.00
2. <src>망할 수는 있지만, </src> <tgt>might lead to ruin,</tgt>; start=2.00, end=3.00
3. <src>그렇 죠? 뭐 </src> <tgt>right?</tgt>; start=3.00, end=4.00
4. <src>교회 십일조가 줄어서 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>망하 고 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>할 일이 아닙니다. 그리고 </src> <tgt>But that's not about ruin from a decrease in church tithes.</tgt>; start=6.00, end=7.00
7. <src>이 지상 에서 할 일은 </src> <tgt>And our task here on this earth is to</tgt>; start=7.00, end=8.00
8. <src>끝없이 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>이 천국 을 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>확장 시켜가. </src> <tgt>endlessly expand this kingdom of heaven.</tgt>; start=10.00, end=10.39
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_B00002_S05012_W000000 ===

source:
- language: Korean
- transcription: 근데 이게 시기적으로 결혼이 뭐 했었으면 진작에 가능했었던 사람들이에요. 근데 어느 정도 시기를 좀 보고 자기가 벌려놓은 일이나 해야 될 일들이 있었기 때문에 그거를 좀 다 좀
- source_tokens:
  0. 근데
  1. 이게
  2. 시기
  3. 적으로
  4. 결혼
  5. 이
  6. 뭐
  7. 했었
  8. 으면
  9. 진작
  10. 에
  11. 가능
  12. 했었던
  13. 사람
  14. 들이에요.
  15. 근데
  16. 어느
  17. 정도
  18. 시기
  19. 를
  20. 좀
  21. 보고
  22. 자기
  23. 가
  24. 벌려
  25. 놓은
  26. 일이나
  27. 해야
  28. 될
  29. 일들이
  30. 있었기
  31. 때문
  32. 에
  33. 그거
  34. 를
  35. 좀
  36. 다
  37. 좀

target:
- language: Chinese
- translation: 但从时间上说，这些人要是结婚的话，其实早就结了。只是他们要等时机，因为自己还有手头的事或者必须做的事，所以那些都...
- target_sense_units:
  0. 但
  1. 从时间上说，
  2. 这些人要是结婚的话，
  3. 其实
  4. 早就结了。
  5. 只是
  6. 他们要等时机，
  7. 因为
  8. 自己还有
  9. 手头的事
  10. 或者
  11. 必须做的事，
  12. 所以
  13. 那些都...

scratchpad:
* target[0]: "但"
  - source_tokens: `0: "근데"`
  - mapping_reason: Discourse connective "근데" (But)

* target[1]: "从时间上说，"
  - source_tokens: `2: "시기", 3: "적으로"`
  - mapping_reason: Temporal framing "시기적으로"

* target[2]: "这些人要是结婚的话，"
  - source_tokens: `1: "이게", 4: "결혼", 5: "이", 7: "했었", 8: "으면", 13: "사람", 14: "들이에요."`
  - mapping_reason: Subject "이게(사람들)" and conditional clause "결혼했었으면"

* target[3]: "其实"
  - source_tokens: `9: "진작"`
  - mapping_reason: Adverbial "진작" (long ago/actually)

* target[4]: "早就结了。"
  - source_tokens: `10: "에", 11: "가능", 12: "했었던"`
  - mapping_reason: Possibility of action in the past "가능했었던"

* target[5]: "只是"
  - source_tokens: `15: "근데"`
  - mapping_reason: Contrastive discourse connective "근데"

* target[6]: "他们要等时机，"
  - source_tokens: `16: "어느", 17: "정도", 18: "시기", 19: "를", 20: "좀", 21: "보고"`
  - mapping_reason: "시기(를) 보고" (waiting for a certain time)

* target[7]: "因为"
  - source_tokens: `30: "있었기", 31: "때문", 32: "에"`
  - mapping_reason: Causal marker "있었기 때문에"

* target[8]: "自己还有"
  - source_tokens: `22: "자기", 23: "가"`
  - mapping_reason: Reflexive pronoun "자기"

* target[9]: "手头的事"
  - source_tokens: `24: "벌려", 25: "놓은", 26: "일이나"`
  - mapping_reason: "벌려놓은 일" (things started/at hand)

* target[10]: "或者"
  - source_tokens: `26: "일이나"`
  - mapping_reason: "이나" (or)

* target[11]: "必须做的事，"
  - source_tokens: `27: "해야", 28: "될", 29: "일들이"`
  - mapping_reason: "해야 될 일" (things that must be done)

* target[12]: "所以"
  - source_tokens: `31: "때문", 32: "에"`
  - mapping_reason: Resultative marker derived from the cause "때문에"

* target[13]: "那些都..."
  - source_tokens: `33: "그거", 34: "를", 35: "좀", 36: "다", 37: "좀"`
  - mapping_reason: Object reference "그거를" and adverbial "다 좀"

result:
```html
0. <src>근데 이게 </src> <tgt>但</tgt>; start=0.00, end=1.00
1. <src>시기 적으로 </src> <tgt>从时间上说，</tgt>; start=1.00, end=2.00
2. <src>결혼 이 뭐 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>했었 으면 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>진작 에 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>가능 했었던 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>사람 들이에요. 근데 </src> <tgt>这些人要是结婚的话，其实早就结了。只是</tgt>; start=7.00, end=8.00
8. <src>어느 정도 시기 를 좀 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>보고 자기 가 </src> <tgt>他们要等时机，</tgt>; start=9.00, end=10.00
10. <src>벌려 놓은 일이나 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>해야 될 일들이 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>있었기 때문 에 </src> <tgt>因为自己还有手头的事或者必须做的事，所以</tgt>; start=12.00, end=13.00
13. <src>그거 를 좀 다 </src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>좀 </src> <tgt>那些都...</tgt>; start=14.00, end=14.36
```

- max_empty_window_count: 5


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_GazVxt6TX_8_W000008 ===

source:
- language: Korean
- transcription: 다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.
- source_tokens:
  0. 다
  1. 마귀를
  2. 따르
  3. 면
  4. 망할
  5. 수는
  6. 있지만,
  7. 그렇
  8. 죠?
  9. 뭐
  10. 교회
  11. 십일조가
  12. 줄어서
  13. 망하
  14. 고
  15. 할
  16. 일이
  17. 아닙니다.
  18. 그리고
  19. 이
  20. 지상
  21. 에서
  22. 할
  23. 일은
  24. 끝없이
  25. 이
  26. 천국
  27. 을
  28. 확장
  29. 시켜가.

target:
- language: Chinese
- translation: 虽然追随魔鬼可能会导致灭亡，对吧？但这并不是因为教会什一奉献减少而导致的灭亡。而且，我们在地上的使命就是不断地扩展这个天国。
- target_sense_units:
  0. 虽然
  1. 追随魔鬼
  2. 可能会导致灭亡，
  3. 对吧？
  4. 但
  5. 这并不是
  6. 因为
  7. 教会什一奉献减少
  8. 而导致的灭亡。
  9. 而且，
  10. 我们在地上的使命
  11. 就是
  12. 不断地扩展
  13. 这个天国。

scratchpad:
* target[0]: "虽然"
  - source_tokens: `6: "있지만,"`
  - mapping_reason: Expresses the concessive relation (although).

* target[1]: "追随魔鬼"
  - source_tokens: `1: "마귀를", 2: "따르"`
  - mapping_reason: Object and verb meaning.

* target[2]: "可能会导致灭亡，"
  - source_tokens: `4: "망할", 5: "수는"`
  - mapping_reason: Possibility and outcome (ruin).

* target[3]: "对吧？"
  - source_tokens: `7: "그렇", 8: "죠?"`
  - mapping_reason: Confirmation/agreement marker.

* target[4]: "但"
  - source_tokens: `6: "있지만,"`
  - mapping_reason: Contrastive conjunction.

* target[5]: "这并不是"
  - source_tokens: `17: "아닙니다."`
  - mapping_reason: Negation of the following proposition.

* target[6]: "因为"
  - source_tokens: `12: "줄어서"`
  - mapping_reason: Causal relation.

* target[7]: "教会什一奉献减少"
  - source_tokens: `10: "교회", 11: "십일조가", 12: "줄어서"`
  - mapping_reason: Subject and cause.

* target[8]: "而导致的灭亡。"
  - source_tokens: `13: "망하", 14: "고"`
  - mapping_reason: Consequence (ruin).

* target[9]: "而且，"
  - source_tokens: `18: "그리고"`
  - mapping_reason: Additive discourse marker.

* target[10]: "我们在地上的使命"
  - source_tokens: `19: "이", 20: "지상", 21: "에서", 22: "할", 23: "일은"`
  - mapping_reason: Subject/topic (the work to do on earth).

* target[11]: "就是"
  - source_tokens: `23: "일은"`
  - mapping_reason: Copula/identifying relation.

* target[12]: "不断地扩展"
  - source_tokens: `24: "끝없이", 28: "확장", 29: "시켜가."`
  - mapping_reason: Adverbial and verb meaning.

* target[13]: "这个天国。"
  - source_tokens: `25: "이", 26: "천국", 27: "을"`
  - mapping_reason: Object of the expansion.

result:
```html
0. <src>다 마귀를 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>따르 면 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>망할 수는 있지만, </src> <tgt>虽然追随魔鬼可能会导致灭亡，</tgt>; start=2.00, end=3.00
3. <src>그렇 죠? 뭐 </src> <tgt>对吧？但</tgt>; start=3.00, end=4.00
4. <src>교회 십일조가 줄어서 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>망하 고 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>할 일이 아닙니다. 그리고 </src> <tgt>这并不是因为教会什一奉献减少而导致的灭亡。而且，</tgt>; start=6.00, end=7.00
7. <src>이 지상 에서 할 일은 </src> <tgt>我们在地上的使命就是</tgt>; start=7.00, end=8.00
8. <src>끝없이 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>이 천국 을 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>확장 시켜가. </src> <tgt>不断地扩展这个天国。</tgt>; start=10.00, end=10.39
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_B00002_S05012_W000000 ===

source:
- language: Korean
- transcription: 근데 이게 시기적으로 결혼이 뭐 했었으면 진작에 가능했었던 사람들이에요. 근데 어느 정도 시기를 좀 보고 자기가 벌려놓은 일이나 해야 될 일들이 있었기 때문에 그거를 좀 다 좀
- source_tokens:
  0. 근데
  1. 이게
  2. 시기
  3. 적으로
  4. 결혼
  5. 이
  6. 뭐
  7. 했었
  8. 으면
  9. 진작
  10. 에
  11. 가능
  12. 했었던
  13. 사람
  14. 들이에요.
  15. 근데
  16. 어느
  17. 정도
  18. 시기
  19. 를
  20. 좀
  21. 보고
  22. 자기
  23. 가
  24. 벌려
  25. 놓은
  26. 일이나
  27. 해야
  28. 될
  29. 일들이
  30. 있었기
  31. 때문
  32. 에
  33. 그거
  34. 를
  35. 좀
  36. 다
  37. 좀

target:
- language: English
- translation: But in terms of timing, these are people who could have gotten married a long time ago if they had wanted to. But they were waiting for the right time, and because they had things they'd started or things to do, they were kind of just...
- target_sense_units:
  0. But in terms of timing,
  1. these are people who
  2. could have
  3. gotten married
  4. a long time ago
  5. if they had wanted to.
  6. But they were
  7. waiting for
  8. the right time,
  9. and because they had
  10. things they'd started
  11. or things to do,
  12. they were
  13. kind of
  14. just...

scratchpad:
* target[0]: "But in terms of timing,"
  - source_tokens: `0: "근데", 2: "시기", 3: "적으로"`
  - mapping_reason: "근데" (But), "시기적으로" (in terms of timing)

* target[1]: "these are people who"
  - source_tokens: `1: "이게", 13: "사람", 14: "들이에요."`
  - mapping_reason: "이게" (these), "사람들이에요" (are people)

* target[2]: "could have"
  - source_tokens: `11: "가능", 12: "했었던"`
  - mapping_reason: "가능했었던" (could have)

* target[3]: "gotten married"
  - source_tokens: `4: "결혼", 5: "이"`
  - mapping_reason: "결혼" (married)

* target[4]: "a long time ago"
  - source_tokens: `9: "진작", 10: "에"`
  - mapping_reason: "진작에" (long time ago)

* target[5]: "if they had wanted to."
  - source_tokens: `6: "뭐", 7: "했었", 8: "으면"`
  - mapping_reason: "뭐 했었으면" (if they had wanted to/if they had done [it])

* target[6]: "But they were"
  - source_tokens: `15: "근데"`
  - mapping_reason: "근데" (But)

* target[7]: "waiting for"
  - source_tokens: `21: "보고"`
  - mapping_reason: "보고" (waiting for/looking at)

* target[8]: "the right time,"
  - source_tokens: `16: "어느", 17: "정도", 18: "시기", 19: "를", 20: "좀"`
  - mapping_reason: "어느 정도 시기를 좀" (the right time)

* target[9]: "and because they had"
  - source_tokens: `30: "있었기", 31: "때문", 32: "에"`
  - mapping_reason: "있었기 때문에" (because they had)

* target[10]: "things they'd started"
  - source_tokens: `22: "자기", 23: "가", 24: "벌려", 25: "놓은", 26: "일이나"`
  - mapping_reason: "자기가 벌려놓은 일이나" (things they had started)

* target[11]: "or things to do,"
  - source_tokens: `27: "해야", 28: "될", 29: "일들이"`
  - mapping_reason: "해야 될 일들이" (things to do)

* target[12]: "they were"
  - source_tokens: `33: "그거", 34: "를"`
  - mapping_reason: "그거를" (referring to the previous clause as the topic of the final action)

* target[13]: "kind of"
  - source_tokens: `35: "좀", 37: "좀"`
  - mapping_reason: "좀" (kind of)

* target[14]: "just..."
  - source_tokens: `36: "다"`
  - mapping_reason: "다" (just/all - used as a filler here)

result:
```html
0. <src>근데 이게 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>시기 적으로 </src> <tgt>But in terms of timing,</tgt>; start=1.00, end=2.00
2. <src>결혼 이 뭐 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>했었 으면 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>진작 에 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>가능 했었던 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>사람 들이에요. 근데 </src> <tgt>these are people who could have gotten married a long time ago if they had wanted to. But they were</tgt>; start=7.00, end=8.00
8. <src>어느 정도 시기 를 좀 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>보고 자기 가 </src> <tgt>waiting for the right time,</tgt>; start=9.00, end=10.00
10. <src>벌려 놓은 일이나 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>해야 될 일들이 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>있었기 때문 에 </src> <tgt>and because they had things they'd started or things to do,</tgt>; start=12.00, end=13.00
13. <src>그거 를 좀 다 </src> <tgt>they were</tgt>; start=13.00, end=14.00
14. <src>좀 </src> <tgt>kind of just...</tgt>; start=14.00, end=14.36
```

- max_empty_window_count: 5


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_B00002_S05012_W000000 ===

source:
- language: Korean
- transcription: 근데 이게 시기적으로 결혼이 뭐 했었으면 진작에 가능했었던 사람들이에요. 근데 어느 정도 시기를 좀 보고 자기가 벌려놓은 일이나 해야 될 일들이 있었기 때문에 그거를 좀 다 좀
- source_tokens:
  0. 근데
  1. 이게
  2. 시기
  3. 적으로
  4. 결혼
  5. 이
  6. 뭐
  7. 했었
  8. 으면
  9. 진작
  10. 에
  11. 가능
  12. 했었던
  13. 사람
  14. 들이에요.
  15. 근데
  16. 어느
  17. 정도
  18. 시기
  19. 를
  20. 좀
  21. 보고
  22. 자기
  23. 가
  24. 벌려
  25. 놓은
  26. 일이나
  27. 해야
  28. 될
  29. 일들이
  30. 있었기
  31. 때문
  32. 에
  33. 그거
  34. 를
  35. 좀
  36. 다
  37. 좀

target:
- language: Japanese
- translation: でも、結婚するなら、時期的にはとっくにできた人たちなんですよ。ただ、ある程度タイミングを見てたし、自分でやり始めたことや、やらないといけないことがあったので、それを全部ちょっと…
- target_sense_units:
  0. でも、
  1. 結婚するなら、
  2. 時期
  3. 的には
  4. とっくにできた人たち
  5. なんですよ。
  6. ただ、
  7. ある程度
  8. タイミングを
  9. 見てたし、
  10. 自分で
  11. やり始めたことや、
  12. やらないといけないこと
  13. が
  14. あったので、
  15. それを
  16. 全部
  17. ちょっと…

scratchpad:
* target[0]: "でも、"
  - source_tokens: `0: "근데"`
  - mapping_reason: Discourse connective "but".
* target[1]: "結婚するなら、"
  - source_tokens: `4: "결혼", 5: "이", 6: "뭐", 7: "했었", 8: "으면"`
  - mapping_reason: Conditional structure regarding marriage.
* target[2]: "時期"
  - source_tokens: `2: "시기"`
  - mapping_reason: Noun "time/period".
* target[3]: "的には"
  - source_tokens: `3: "적으로"`
  - mapping_reason: Adverbial suffix indicating "in terms of".
* target[4]: "とっくにできた人たち"
  - source_tokens: `9: "진작", 10: "에", 11: "가능", 12: "했었던", 13: "사람", 14: "들이에요."`
  - mapping_reason: "Already possible" + "people".
* target[5]: "なんですよ。"
  - source_tokens: `14: "들이에요."`
  - mapping_reason: Sentence ending/explicative tone.
* target[6]: "ただ、"
  - source_tokens: `15: "근데"`
  - mapping_reason: Discourse connective "however".
* target[7]: "ある程度"
  - source_tokens: `16: "어느", 17: "정도"`
  - mapping_reason: Quantifier "to some extent".
* target[8]: "タイミングを"
  - source_tokens: `18: "시기", 19: "를"`
  - mapping_reason: Object "timing".
* target[9]: "見てたし、"
  - source_tokens: `20: "좀", 21: "보고"`
  - mapping_reason: Verb "to watch/consider".
* target[10]: "自分で"
  - source_tokens: `22: "자기", 23: "가"`
  - mapping_reason: Reflexive "oneself".
* target[11]: "やり始めたことや、"
  - source_tokens: `24: "벌려", 25: "놓은", 26: "일이나"`
  - mapping_reason: "Things started/undertaken".
* target[12]: "やらないといけないこと"
  - source_tokens: `27: "해야", 28: "될", 29: "일들이"`
  - mapping_reason: "Things that must be done".
* target[13]: "が"
  - source_tokens: `29: "일들이"`
  - mapping_reason: Subject marker for the preceding clause.
* target[14]: "あったので、"
  - source_tokens: `30: "있었기", 31: "때문", 32: "에"`
  - mapping_reason: Causal marker "because".
* target[15]: "それを"
  - source_tokens: `33: "그거", 34: "를"`
  - mapping_reason: Object "that".
* target[16]: "全部"
  - source_tokens: `36: "다"`
  - mapping_reason: "All".
* target[17]: "ちょっと…"
  - source_tokens: `35: "좀", 37: "좀"`
  - mapping_reason: Hesitation/softener.

result:
```html
0. <src>근데 이게 </src> <tgt>でも、</tgt>; start=0.00, end=1.00
1. <src>시기 적으로 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>결혼 이 뭐 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>했었 으면 </src> <tgt>結婚するなら、時期的には</tgt>; start=3.00, end=4.00
4. <src>진작 에 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>가능 했었던 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>사람 들이에요. 근데 </src> <tgt>とっくにできた人たちなんですよ。ただ、</tgt>; start=7.00, end=8.00
8. <src>어느 정도 시기 를 좀 </src> <tgt>ある程度タイミングを</tgt>; start=8.00, end=9.00
9. <src>보고 자기 가 </src> <tgt>見てたし、自分で</tgt>; start=9.00, end=10.00
10. <src>벌려 놓은 일이나 </src> <tgt>やり始めたことや、</tgt>; start=10.00, end=11.00
11. <src>해야 될 일들이 </src> <tgt>やらないといけないことが</tgt>; start=11.00, end=12.00
12. <src>있었기 때문 에 </src> <tgt>あったので、</tgt>; start=12.00, end=13.00
13. <src>그거 를 좀 다 </src> <tgt>それを全部</tgt>; start=13.00, end=14.00
14. <src>좀 </src> <tgt>ちょっと…</tgt>; start=14.00, end=14.36
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
