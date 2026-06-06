=== KO_GazVxt6TX_8_W000008 ===

source:
- language: Korean
- transcription: 다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.
- source_tokens:
  0. 다
  1. 마귀를
  2. 따르 면
  3. 망할
  4. 수는
  5. 있지만,
  6. 그렇 죠?
  7. 뭐
  8. 교회
  9. 십일조가
  10. 줄어서
  11. 망하 고
  12. 할
  13. 일이
  14. 아닙니다.
  15. 그리고
  16. 이
  17. 지상 에서
  18. 할
  19. 일은
  20. 끝없이
  21. 이
  22. 천국 을
  23. 확장 시켜가.

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
  - source_tokens: `0: "다", 1: "마귀를", 2: "따르 면"`
  - mapping_reason: "다" (all/everyone) and "마귀를 따르 면" (following the devil) constitute the subject and action.

* target[1]: "might lead to"
  - source_tokens: `4: "수는", 5: "있지만,"`
  - mapping_reason: "수는 있지만" expresses the possibility (might).

* target[2]: "ruin,"
  - source_tokens: `3: "망할"`
  - mapping_reason: "망할" is the verb "to ruin".

* target[3]: "right?"
  - source_tokens: `6: "그렇 죠?"`
  - mapping_reason: Direct translation of "그렇 죠?".

* target[4]: "But that's not about"
  - source_tokens: `7: "뭐", 14: "아닙니다."`
  - mapping_reason: "뭐" functions as a discourse marker and "아닙니다" negates the topic.

* target[5]: "ruin"
  - source_tokens: `11: "망하 고"`
  - mapping_reason: "망하 고" is the root for ruin.

* target[6]: "from a decrease"
  - source_tokens: `10: "줄어서"`
  - mapping_reason: "줄어서" means because of a decrease.

* target[7]: "in church tithes."
  - source_tokens: `8: "교회", 9: "십일조가"`
  - mapping_reason: "교회 십일조가" translates to church tithes.

* target[8]: "And our task"
  - source_tokens: `15: "그리고", 18: "할", 19: "일은"`
  - mapping_reason: "그리고" (And) and "할 일은" (the task to do).

* target[9]: "here on this earth"
  - source_tokens: `16: "이", 17: "지상 에서"`
  - mapping_reason: "이 지상 에서" translates to on this earth.

* target[10]: "is to"
  - source_tokens: `12: "할", 13: "일이"`
  - mapping_reason: Implicit copula function for the task definition.

* target[11]: "endlessly expand"
  - source_tokens: `20: "끝없이", 23: "확장 시켜가."`
  - mapping_reason: "끝없이" (endlessly) and "확장 시켜가" (expand).

* target[12]: "this kingdom of heaven."
  - source_tokens: `21: "이", 22: "천국 을"`
  - mapping_reason: "이 천국 을" translates to this kingdom of heaven.

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
=== KO_GazVxt6TX_8_W000008 ===

source:
- language: Korean
- transcription: 다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.
- source_tokens:
  0. 다
  1. 마귀를
  2. 따르 면
  3. 망할
  4. 수는
  5. 있지만,
  6. 그렇 죠?
  7. 뭐
  8. 교회
  9. 십일조가
  10. 줄어서
  11. 망하 고
  12. 할
  13. 일이
  14. 아닙니다.
  15. 그리고
  16. 이
  17. 지상 에서
  18. 할
  19. 일은
  20. 끝없이
  21. 이
  22. 천국 을
  23. 확장 시켜가.

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
  - source_tokens: `1: "마귀를", 2: "따르 면"`
  - mapping_reason: "마귀를" (devil) + "따르 면" (if follow)

* target[1]: "滅びることもあるでしょう。"
  - source_tokens: `3: "망할", 4: "수는", 5: "있지만,"`
  - mapping_reason: "망할 수는" (can perish) + "있지만" (although/will be)

* target[2]: "そうですよね？"
  - source_tokens: `6: "그렇 죠?"`
  - mapping_reason: "그렇 죠?" (is it not so?)

* target[3]: "ですが、"
  - source_tokens: `7: "뭐"`
  - mapping_reason: "뭐" (well/but) acting as a discourse connective.

* target[4]: "教会の什一献金が"
  - source_tokens: `8: "교회", 9: "십일조가"`
  - mapping_reason: "교회" (church) + "십일조가" (tithe)

* target[5]: "減って滅びる"
  - source_tokens: `10: "줄어서", 11: "망하 고"`
  - mapping_reason: "줄어서" (decreased and) + "망하 고" (perish and)

* target[6]: "話ではありません。"
  - source_tokens: `12: "할", 13: "일이", 14: "아닙니다."`
  - mapping_reason: "할 일이 아닙니다" (it is not the matter to do/talk about)

* target[7]: "そして、"
  - source_tokens: `15: "그리고"`
  - mapping_reason: "그리고" (and)

* target[8]: "この地上で"
  - source_tokens: `16: "이", 17: "지상 에서"`
  - mapping_reason: "이" (this) + "지상 에서" (on earth)

* target[9]: "やるべきことは、"
  - source_tokens: `18: "할", 19: "일은"`
  - mapping_reason: "할 일은" (the work to do)

* target[10]: "この天国を"
  - source_tokens: `21: "이", 22: "천국 을"`
  - mapping_reason: "이" (this) + "천국 을" (heaven)

* target[11]: "絶え間なく"
  - source_tokens: `20: "끝없이"`
  - mapping_reason: "끝없이" (endlessly)

* target[12]: "広げていく"
  - source_tokens: `23: "확장 시켜가."`
  - mapping_reason: "확장 시켜가" (expand)

* target[13]: "ことです。"
  - source_tokens: `19: "일은"`
  - mapping_reason: "일은" (the matter/thing) serves as the nominalizer structure for the final clause.

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
=== KO_B00002_S05012_W000000 ===

source:
- language: Korean
- transcription: 근데 이게 시기적으로 결혼이 뭐 했었으면 진작에 가능했었던 사람들이에요. 근데 어느 정도 시기를 좀 보고 자기가 벌려놓은 일이나 해야 될 일들이 있었기 때문에 그거를 좀 다 좀
- source_tokens:
  0. 근데
  1. 이게
  2. 시기 적으로
  3. 결혼 이
  4. 뭐
  5. 했었 으면
  6. 진작 에
  7. 가능 했었던
  8. 사람 들이에요.
  9. 근데
  10. 어느
  11. 정도
  12. 시기 를
  13. 좀
  14. 보고
  15. 자기 가
  16. 벌려 놓은
  17. 일이나
  18. 해야
  19. 될
  20. 일들이
  21. 있었기
  22. 때문 에
  23. 그거 를
  24. 좀
  25. 다
  26. 좀

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
  - source_tokens: `0: "근데", 2: "시기 적으로"`
  - mapping_reason: "근데" (But) and "시기 적으로" (in terms of timing).
* target[1]: "these are people who"
  - source_tokens: `1: "이게", 8: "사람 들이에요."`
  - mapping_reason: "이게" (these) and "사람 들이에요" (people).
* target[2]: "could have"
  - source_tokens: `7: "가능 했었던"`
  - mapping_reason: "가능 했었던" expresses the possibility (could have).
* target[3]: "gotten married"
  - source_tokens: `3: "결론 이"`
  - mapping_reason: "결혼 이" (marriage).
* target[4]: "a long time ago"
  - source_tokens: `6: "진작 에"`
  - mapping_reason: "진작 에" (a long time ago).
* target[5]: "if they had wanted to."
  - source_tokens: `4: "뭐", 5: "했었 으면"`
  - mapping_reason: "뭐" and "했었 으면" (if they had done/wanted).
* target[6]: "But they were"
  - source_tokens: `9: "근데"`
  - mapping_reason: "근데" (But).
* target[7]: "waiting for"
  - source_tokens: `14: "보고"`
  - mapping_reason: "보고" (watching/waiting for).
* target[8]: "the right time,"
  - source_tokens: `10: "어느", 11: "정도", 12: "시기 를", 13: "좀"`
  - mapping_reason: "어느 정도 시기를 좀" (the right time).
* target[9]: "and because they had"
  - source_tokens: `21: "있었기", 22: "때문 에"`
  - mapping_reason: "있었기 때문에" (because they had).
* target[10]: "things they'd started"
  - source_tokens: `15: "자기 가", 16: "벌려 놓은", 17: "일이나"`
  - mapping_reason: "자기가 벌려 놓은 일" (things they had started).
* target[11]: "or things to do,"
  - source_tokens: `18: "해야", 19: "될", 20: "일들이"`
  - mapping_reason: "해야 될 일들" (things to do).
* target[12]: "they were"
  - source_tokens: `23: "그거 를"`
  - mapping_reason: "그거를" (the object they were dealing with).
* target[13]: "kind of"
  - source_tokens: `24: "좀", 26: "좀"`
  - mapping_reason: "좀" (kind of/a bit).
* target[14]: "just..."
  - source_tokens: `25: "다"`
  - mapping_reason: "다" (all/just).

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
  2. 시기 적으로
  3. 결혼 이
  4. 뭐
  5. 했었 으면
  6. 진작 에
  7. 가능 했었던
  8. 사람 들이에요.
  9. 근데
  10. 어느
  11. 정도
  12. 시기 를
  13. 좀
  14. 보고
  15. 자기 가
  16. 벌려 놓은
  17. 일이나
  18. 해야
  19. 될
  20. 일들이
  21. 있었기
  22. 때문 에
  23. 그거 를
  24. 좀
  25. 다
  26. 좀

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
  - mapping_reason: Discourse connective "but" mapping.

* target[1]: "从时间上说，"
  - source_tokens: `2: "시기 적으로"`
  - mapping_reason: Temporal context modifier.

* target[2]: "这些人要是结婚的话，"
  - source_tokens: `3: "결혼 이", 8: "사람 들이에요."`
  - mapping_reason: Subject and condition of marriage.

* target[3]: "其实"
  - source_tokens: `4: "뭐"`
  - mapping_reason: Discourse filler/emphasis.

* target[4]: "早就结了。"
  - source_tokens: `5: "했었 으면", 6: "진작 에", 7: "가능 했었던"`
  - mapping_reason: Temporal adverb and capability of past action.

* target[5]: "只是"
  - source_tokens: `9: "근데"`
  - mapping_reason: Contrastive conjunction.

* target[6]: "他们要等时机，"
  - source_tokens: `10: "어느", 11: "정도", 12: "시기 를", 13: "좀", 14: "보고"`
  - mapping_reason: Waiting for a certain timing.

* target[7]: "因为"
  - source_tokens: `21: "있었기", 22: "때문 에"`
  - mapping_reason: Causal marker.

* target[8]: "自己还有"
  - source_tokens: `15: "자기 가"`
  - mapping_reason: Subject and existence.

* target[9]: "手头的事"
  - source_tokens: `16: "벌려 놓은", 17: "일이나"`
  - mapping_reason: Ongoing/started tasks.

* target[10]: "或者"
  - source_tokens: `17: "일이나"`
  - mapping_reason: Disjunctive marker.

* target[11]: "必须做的事，"
  - source_tokens: `18: "해야", 19: "될", 20: "일들이"`
  - mapping_reason: Obligatory tasks.

* target[12]: "所以"
  - source_tokens: `21: "있었기", 22: "때문 에"`
  - mapping_reason: Consequence marker.

* target[13]: "那些都..."
  - source_tokens: `23: "그거 를", 24: "좀", 25: "다", 26: "좀"`
  - mapping_reason: Referring to the tasks and completion/extent.

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
=== KO_B00002_S05012_W000000 ===

source:
- language: Korean
- transcription: 근데 이게 시기적으로 결혼이 뭐 했었으면 진작에 가능했었던 사람들이에요. 근데 어느 정도 시기를 좀 보고 자기가 벌려놓은 일이나 해야 될 일들이 있었기 때문에 그거를 좀 다 좀
- source_tokens:
  0. 근데
  1. 이게
  2. 시기 적으로
  3. 결혼 이
  4. 뭐
  5. 했었 으면
  6. 진작 에
  7. 가능 했었던
  8. 사람 들이에요.
  9. 근데
  10. 어느
  11. 정도
  12. 시기 를
  13. 좀
  14. 보고
  15. 자기 가
  16. 벌려 놓은
  17. 일이나
  18. 해야
  19. 될
  20. 일들이
  21. 있었기
  22. 때문 에
  23. 그거 를
  24. 좀
  25. 다
  26. 좀

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
  - mapping_reason: Discourse connective "근데" (but/however).
* target[1]: "結婚するなら、"
  - source_tokens: `3: "결혼 이", 4: "뭐", 5: "했었 으면"`
  - mapping_reason: Conditional "if they were to marry".
* target[2]: "時期"
  - source_tokens: `2: "시기  적으로"`
  - mapping_reason: Temporal noun "시기".
* target[3]: "的には"
  - source_tokens: `2: "시기  적으로"`
  - mapping_reason: Suffix "-적으로" indicating "in terms of".
* target[4]: "とっくにできた人たち"
  - source_tokens: `6: "진작 에", 7: "가능 했었던", 8: "사람 들이에요."`
  - mapping_reason: "진작에" (long ago/already), "가능했었던" (could have done), "사람들이에요" (are people).
* target[5]: "なんですよ。"
  - source_tokens: `8: "사람 들이에요."`
  - mapping_reason: Explanatory sentence ending.
* target[6]: "ただ、"
  - source_tokens: `9: "근데"`
  - mapping_reason: Discourse connective "근데" (however/but).
* target[7]: "ある程度"
  - source_tokens: `10: "어느", 11: "정도"`
  - mapping_reason: Quantity/degree "어느 정도".
* target[8]: "タイミングを"
  - source_tokens: `12: "시기 를", 13: "좀"`
  - mapping_reason: "시기" (timing) and hedge "좀".
* target[9]: "見てたし、"
  - source_tokens: `14: "보고"`
  - mapping_reason: Verb "보고" (looked at/considered).
* target[10]: "自分で"
  - source_tokens: `15: "자기 가"`
  - mapping_reason: Reflexive pronoun "자기".
* target[11]: "やり始めたことや、"
  - source_tokens: `16: "벌려 놓은", 17: "일이나"`
  - mapping_reason: "벌려 놓은 일" (work one has started).
* target[12]: "やらないといけないこと"
  - source_tokens: `18: "해야", 19: "될", 20: "일들이"`
  - mapping_reason: "해야 될 일들" (work that must be done).
* target[13]: "が"
  - source_tokens: `20: "일들이"`
  - mapping_reason: Subject marker for the preceding clause.
* target[14]: "あったので、"
  - source_tokens: `21: "있었기", 22: "때문 에"`
  - mapping_reason: Causal relation "있었기 때문에".
* target[15]: "それを"
  - source_tokens: `23: "그거 를"`
  - mapping_reason: Object pronoun "그거".
* target[16]: "全部"
  - source_tokens: `25: "다"`
  - mapping_reason: Extent "다" (all).
* target[17]: "ちょっと…"
  - source_tokens: `24: "좀", 26: "좀"`
  - mapping_reason: Hedge "좀".

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
=== KO_GazVxt6TX_8_W000008 ===

source:
- language: Korean
- transcription: 다 마귀를 따르면 망할 수는 있지만, 그렇죠? 뭐 교회 십일조가 줄어서 망하고 할 일이 아닙니다. 그리고 이 지상에서 할 일은 끝없이 이 천국을 확장시켜가.
- source_tokens:
  0. 다
  1. 마귀를
  2. 따르 면
  3. 망할
  4. 수는
  5. 있지만,
  6. 그렇 죠?
  7. 뭐
  8. 교회
  9. 십일조가
  10. 줄어서
  11. 망하 고
  12. 할
  13. 일이
  14. 아닙니다.
  15. 그리고
  16. 이
  17. 지상 에서
  18. 할
  19. 일은
  20. 끝없이
  21. 이
  22. 천국 을
  23. 확장 시켜가.

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
  - source_tokens: `5: "있지만,"`
  - mapping_reason: concessive conjunction "虽然" maps to the "지만" part of "있지만".
* target[1]: "追随魔鬼"
  - source_tokens: `1: "마귀를", 2: "따르 면"`
  - mapping_reason: "追随" (follow) maps to "따르", "魔鬼" (devil) maps to "마귀를".
* target[2]: "可能会导致灭亡，"
  - source_tokens: `3: "망할", 4: "수는"`
  - mapping_reason: "灭亡" maps to "망할", "可能" maps to "수는".
* target[3]: "对吧？"
  - source_tokens: `6: "그렇 죠?"`
  - mapping_reason: Direct discourse marker.
* target[4]: "但"
  - source_tokens: `5: "있지만,"`
  - mapping_reason: Contrastive conjunction mapping to "있지만".
* target[5]: "这并不是"
  - source_tokens: `14: "아닙니다."`
  - mapping_reason: Negation "아닙니다" maps to "这并不是".
* target[6]: "因为"
  - source_tokens: `10: "줄어서"`
  - mapping_reason: Causal marker "因为" maps to "어서" in "줄어서".
* target[7]: "教会什一奉献减少"
  - source_tokens: `8: "교회", 9: "십일조가", 10: "줄어서"`
  - mapping_reason: "教会" (교회), "什一奉献" (십일조가), "减少" (줄어서).
* target[8]: "而导致的灭亡。"
  - source_tokens: `11: "망하 고"`
  - mapping_reason: "灭亡" maps to "망하".
* target[9]: "而且，"
  - source_tokens: `15: "그리고"`
  - mapping_reason: Discourse connective.
* target[10]: "我们在地上的使命"
  - source_tokens: `16: "이", 17: "지상 에서", 18: "할", 19: "일은"`
  - mapping_reason: "我们" (implied), "地上" (지상 에서), "使命" (할 일은).
* target[11]: "就是"
  - source_tokens: `19: "일은"`
  - mapping_reason: Copula/focus marker "就是" maps to the topic marker "은" in "일은".
* target[12]: "不断地扩展"
  - source_tokens: `20: "끝없이", 23: "확장 시켜가."`
  - mapping_reason: "不断地" (끝없이), "扩展" (확장 시켜가).
* target[13]: "这个天国。"
  - source_tokens: `21: "이", 22: "천국 을"`
  - mapping_reason: "这个" (이), "天国" (천국 을).

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
  status: failed_after_response
  reason: * target[8]
  - verdict: mapping_error
  - reason: "The target unit only reflects '망하고' (destruction). The remaining tokens (12, 13, 14) belong to the preceding negative predicate structure."
  - replace_source_tokens: 11: "망하 고"
  validation:
    scratchpad:
* target[0]: "虽然"
  - source_tokens: `5: "있지만,"`
  - mapping_reason: Concessive conjunction derived from the -지만 ending.

* target[1]: "追随魔鬼"
  - source_tokens: `1: "마귀를", 2: "따르 면"`
  - mapping_reason: Core action and object.

* target[2]: "可能会导致灭亡，"
  - source_tokens: `3: "망할", 4: "수는"`
  - mapping_reason: Potential state of perishing.

* target[3]: "对吧？"
  - source_tokens: `6: "그렇 죠?"`
  - mapping_reason: Confirmation marker.

* target[4]: "但"
  - source_tokens: `5: "있지만,"`
  - mapping_reason: Contrastive conjunction.

* target[5]: "这并不是"
  - source_tokens: `14: "아닙니다."`
  - mapping_reason: Negation of the following proposition.

* target[6]: "因为"
  - source_tokens: `10: "줄어서"`
  - mapping_reason: Causal marker.

* target[7]: "教会什一奉献减少"
  - source_tokens: `8: "교회", 9: "십일조가", 10: "줄어서"`
  - mapping_reason: Subject and cause for the perceived demise.

* target[8]: "而导致的灭亡。"
  - source_tokens: `11: "망하 고", 12: "할", 13: "일이", 14: "아닙니다."`
  - mapping_reason: Reiteration of the negation of the specific cause of demise.

* target[9]: "而且，"
  - source_tokens: `15: "그리고"`
  - mapping_reason: Discourse additive.

* target[10]: "我们在地上的使命"
  - source_tokens: `16: "이", 17: "지상 에서", 18: "할", 19: "일은"`
  - mapping_reason: Subject of the sentence referring to the work on earth.

* target[11]: "就是"
  - source_tokens: `19: "일은"`
  - mapping_reason: Copula/definition marker.

* target[12]: "不断地扩展"
  - source_tokens: `20: "끝없이", 23: "확장 시켜가."`
  - mapping_reason: Adverbial modifier and verb.

* target[13]: "这个天国。"
  - source_tokens: `21: "이", 22: "천국 을"`
  - mapping_reason: Object of the expansion.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1, 2]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [3, 4]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [6]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [14]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [10]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [8, 9, 10]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [11, 12, 13, 14]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [15]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [16, 17, 18, 19]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [20, 23]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [21, 22]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
