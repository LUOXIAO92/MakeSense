=== KO_E7ZEWK_4k08_W000004 ===

source:
- language: Korean
- transcription: 그러나 하나님의 백성의 믿음은 어떻게 강해질 수 있을까? 엄마, 엄마도 있다. 어떻게 강해질 수 있을까? 볼까요? 둘, 셋.
- source_tokens:
  0. 그러나
  1. 하나님 의
  2. 백성 의
  3. 믿음 은
  4. 어떻게
  5. 강해 질
  6. 수
  7. 있을까?
  8. 엄마,
  9. 엄마 도
  10. 있다.
  11. 어떻게
  12. 강해 질
  13. 수
  14. 있을까?
  15. 볼까요?
  16. 둘,
  17. 셋.

target:
- language: English
- translation: But how can the faith of God's people become stronger? Mom – Mom is here too. How can it become stronger? Let's see? Two, three.
- target_sense_units:
  0. But how can
  1. the faith of God's people
  2. become stronger?
  3. Mom– Mom is here too.
  4. How can it become stronger?
  5. Let's see?
  6. Two, three.

scratchpad:
* target[0]: "But how can"
  - source_tokens: `0: "그러나", 4: "어떻게"`
  - mapping_reason: "But" maps to "그러나", "how" maps to "어떻게".

* target[1]: "the faith of God's people"
  - source_tokens: `1: "하나님 의", 2: "백성 의", 3: "믿음 은"`
  - mapping_reason: "God's" (1), "people" (2), "faith" (3).

* target[2]: "become stronger?"
  - source_tokens: `5: "강해 질", 6: "수", 7: "있을까?"`
  - mapping_reason: "become stronger" (5), "can" (6, 7).

* target[3]: "Mom– Mom is here too."
  - source_tokens: `8: "엄마,", 9: "엄마 도", 10: "있다."`
  - mapping_reason: "Mom" (8), "Mom" (9), "is here" (10), "too" (9).

* target[4]: "How can it become stronger?"
  - source_tokens: `11: "어떻게", 12: "강해 질", 13: "수", 14: "있을까?"`
  - mapping_reason: "How" (11), "become stronger" (12), "can" (13, 14).

* target[5]: "Let's see?"
  - source_tokens: `15: "볼까요?"`
  - mapping_reason: Direct translation of "볼까요?".

* target[6]: "Two, three."
  - source_tokens: `16: "둘,", 17: "셋."`
  - mapping_reason: Direct translation of "둘" and "셋".

result:
```html
0. <src>그러나 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>하나님 의 백성 의 믿음 은 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>어떻게 </src> <tgt>But how can the faith of God's people</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>강해 질 수 있을까? </src> <tgt>become stronger?</tgt>; start=5.00, end=6.00
6. <src>엄마, </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>엄마 도 있다. </src> <tgt>Mom– Mom is here too.</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>어떻게 강해 질 수 있을까? </src> <tgt>How can it become stronger?</tgt>; start=10.00, end=11.00
11. <src>볼까요? </src> <tgt>Let's see?</tgt>; start=11.00, end=12.00
12. <src>둘, 셋. </src> <tgt>Two, three.</tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=13.02
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_E7ZEWK_4k08_W000004 ===

source:
- language: Korean
- transcription: 그러나 하나님의 백성의 믿음은 어떻게 강해질 수 있을까? 엄마, 엄마도 있다. 어떻게 강해질 수 있을까? 볼까요? 둘, 셋.
- source_tokens:
  0. 그러나
  1. 하나님 의
  2. 백성 의
  3. 믿음 은
  4. 어떻게
  5. 강해 질
  6. 수
  7. 있을까?
  8. 엄마,
  9. 엄마 도
  10. 있다.
  11. 어떻게
  12. 강해 질
  13. 수
  14. 있을까?
  15. 볼까요?
  16. 둘,
  17. 셋.

target:
- language: Chinese
- translation: 但上帝子民的信心要怎么变得更坚强呢？妈妈，妈妈也在呢。要怎么变得更坚强呢？我们来看看？二，三。
- target_sense_units:
  0. 但
  1. 上帝子民的信心
  2. 要怎么
  3. 变得更坚强呢？
  4. 妈妈，
  5. 妈妈也在呢。
  6. 要怎么
  7. 变得更坚强呢？
  8. 我们来看看？
  9. 二，
  10. 三。

scratchpad:
* target[0]: "但"
  - source_tokens: `0: "그러나"`
  - mapping_reason: Connective "but" mapping.
* target[1]: "上帝子民的信心"
  - source_tokens: `1: "하나님 의", 2: "백성 의", 3: "믿음 은"`
  - mapping_reason: Noun phrase "God's people's faith".
* target[2]: "要怎么"
  - source_tokens: `4: "어떻게"`
  - mapping_reason: Interrogative adverb "how".
* target[3]: "变得更坚强呢？"
  - source_tokens: `5: "강해 질", 6: "수", 7: "있을까?"`
  - mapping_reason: Verbal phrase "can become strong".
* target[4]: "妈妈，"
  - source_tokens: `8: "엄마,"`
  - mapping_reason: Direct address "Mom".
* target[5]: "妈妈也在呢。"
  - source_tokens: `9: "엄마 도", 10: "있다."`
  - mapping_reason: Subject with additive particle and existence verb.
* target[6]: "要怎么"
  - source_tokens: `11: "어떻게"`
  - mapping_reason: Interrogative adverb "how".
* target[7]: "变得更坚强呢？"
  - source_tokens: `12: "강해 질", 13: "수", 14: "있을까?"`
  - mapping_reason: Verbal phrase "can become strong".
* target[8]: "我们来看看？"
  - source_tokens: `15: "볼까요?"`
  - mapping_reason: Suggestive verb "shall we see".
* target[9]: "二，"
  - source_tokens: `16: "둘,"`
  - mapping_reason: Number "two".
* target[10]: "三。"
  - source_tokens: `17: "셋."`
  - mapping_reason: Number "three".

result:
```html
0. <src>그러나 </src> <tgt>但</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>하나님 의 백성 의 믿음 은 </src> <tgt>上帝子民的信心</tgt>; start=2.00, end=3.00
3. <src>어떻게 </src> <tgt>要怎么</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>강해 질 수 있을까? </src> <tgt>变得更坚强呢？</tgt>; start=5.00, end=6.00
6. <src>엄마, </src> <tgt>妈妈，</tgt>; start=6.00, end=7.00
7. <src>엄마 도 있다. </src> <tgt>妈妈也在呢。</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>어떻게 강해 질 수 있을까? </src> <tgt>要怎么变得更坚强呢？</tgt>; start=10.00, end=11.00
11. <src>볼까요? </src> <tgt>我们来看看？</tgt>; start=11.00, end=12.00
12. <src>둘, 셋. </src> <tgt>二，三。</tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=13.02
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_E9GzA6TOlV4_W000007 ===

source:
- language: Korean
- transcription: 일단 배그는 파밍이 제일 중요합니다, 여러분. 파밍을 열심히 해주세요. 어 발소리 난다. 어 당황한 척하면서 이렇게 파밍해주면 됩니다, 여러분.
- source_tokens:
  0. 일단
  1. 배그는
  2. 파밍이
  3. 제일
  4. 중요 합니다,
  5. 여러분.
  6. 파밍을
  7. 열심히
  8. 해주세요.
  9. 어
  10. 발소리
  11. 난다.
  12. 어
  13. 당황 한
  14. 척하 면서
  15. 이렇게
  16. 파밍해주면
  17. 됩니다,
  18. 여러분.

target:
- language: Japanese
- translation: まず、PUBGはファームが一番重要です、皆さん。一生懸命ファームしてください。あ、こうやってファームすればいいんですよ。慌てたふりをしながらね、皆さん。
- target_sense_units:
  0. まず、
  1. PUBGは
  2. ファームが
  3. 一番重要です、
  4. 皆さん。
  5. 一生懸命
  6. ファームしてください。
  7. あ、
  8. こうやって
  9. ファームすればいいんですよ。
  10. 慌てたふりをしながらね、
  11. 皆さん。

scratchpad:
* target[0]: "まず、"
  - source_tokens: `0: "일단"`
  - mapping_reason: "일단" (first of all) maps to "まず" (firstly).
* target[1]: "PUBGは"
  - source_tokens: `1: "배그는"`
  - mapping_reason: "배그" (PUBG) maps to "PUBG".
* target[2]: "ファームが"
  - source_tokens: `2: "파밍이"`
  - mapping_reason: "파밍" (farming/looting) maps to "ファーム".
* target[3]: "一番重要です、"
  - source_tokens: `3: "제일", 4: "중요 합니다,"`
  - mapping_reason: "제일" (most) and "중요합니다" (important) map to "一番重要です".
* target[4]: "皆さん。"
  - source_tokens: `5: "여러분."`
  - mapping_reason: "여러분" (everyone/guys) maps to "皆さん".
* target[5]: "一生懸命"
  - source_tokens: `7: "열심히"`
  - mapping_reason: "열심히" (diligently) maps to "一生懸命".
* target[6]: "ファームしてください。"
  - source_tokens: `6: "파밍을", 8: "해주세요."`
  - mapping_reason: "파밍을" (looting) and "해주세요" (please do) map to "ファームしてください".
* target[7]: "あ、"
  - source_tokens: `9: "어"`
  - mapping_reason: "어" (oh) maps to "あ".
* target[8]: "こうやって"
  - source_tokens: `15: "이렇게"`
  - mapping_reason: "이렇게" (like this) maps to "こうやって".
* target[9]: "ファームすればいいんですよ。"
  - source_tokens: `16: "파밍해주면", 17: "됩니다,"`
  - mapping_reason: "파밍해주면 됩니다" (you should loot) maps to "ファームすればいいんですよ".
* target[10]: "慌てたふりをしながらね、"
  - source_tokens: `13: "당황 한", 14: "척하 면서"`
  - mapping_reason: "당황한 척하면서" (pretending to be flustered) maps to "慌てたふりをしながら".
* target[11]: "皆さん。"
  - source_tokens: `18: "여러분."`
  - mapping_reason: "여러분" (everyone) maps to "皆さん".

result:
```html
0. <src>일단 배그는 파밍이 </src> <tgt>まず、PUBGはファームが</tgt>; start=0.00, end=1.00
1. <src>제일 중요 합니다, </src> <tgt>一番重要です、</tgt>; start=1.00, end=2.00
2. <src>여러분. </src> <tgt>皆さん。</tgt>; start=2.00, end=3.00
3. <src>파밍을 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>열심히 해주세요. 어 </src> <tgt>一生懸命ファームしてください。あ、</tgt>; start=4.00, end=5.00
5. <src>발소리 난다. </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>어 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>당황 한 척하 면서 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>이렇게 파밍해주면 됩니다, 여러분. </src> <tgt>こうやってファームすればいいんですよ。慌てたふりをしながらね、皆さん。</tgt>; start=12.00, end=12.73
```

- max_empty_window_count: 7


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_DlMYWhPK1Lg_W000119 ===

source:
- language: Korean
- transcription: 악인네는 서로 내놔 하니까 그러면 어떻게 서로까지 뜯고 싸움을 해야만이 되는 사람이잖아. 그러면 어떻게 이제 이게 BJ 궁합은 어떻게 한 사람이 어떻게 어?
- source_tokens:
  0. 악인네는
  1. 서로
  2. 내놔
  3. 하니까
  4. 그러면
  5. 어떻게
  6. 서로 까지
  7. 뜯고
  8. 싸움 을
  9. 해야 만이
  10. 되는
  11. 사람 이잖아.
  12. 그러면
  13. 어떻게
  14. 이제
  15. 이게
  16. BJ
  17. 궁합은
  18. 어떻게
  19. 한
  20. 사람 이
  21. 어떻게
  22. 어?

target:
- language: English
- translation: If bad people are telling each other to hand it over, doesn't that mean they have to tear each other apart and fight to get anywhere? So then, how does this BJ chemistry work? How can one person...?
- target_sense_units:
  0. If bad people are
  1. telling each other
  2. to hand it over,
  3. doesn't that mean
  4. they have to
  5. tear each other apart
  6. and fight to get anywhere?
  7. So then,
  8. how does this BJ chemistry
  9. work?
  10. How can one person...?

scratchpad:
* target[0]: "If bad people are"
  - source_tokens: `0: "악인네는"`
  - mapping_reason: "악인네는" (bad people) provides the subject and the "If" is implied by the context of the sentence structure.

* target[1]: "telling each other"
  - source_tokens: `1: "서로", 3: "하니까"`
  - mapping_reason: "서로" (each other) and "하니까" (doing/saying) capture the interaction.

* target[2]: "to hand it over,"
  - source_tokens: `2: "내놔"`
  - mapping_reason: "내놔" (hand it over) is the content of the demand.

* target[3]: "doesn't that mean"
  - source_tokens: `4: "그러면", 10: "되는"`
  - mapping_reason: "그러면" (then/so) and "되는" (becoming/meaning) frame the rhetorical question.

* target[4]: "they have to"
  - source_tokens: `9: "해야 만이"`
  - mapping_reason: "해야 만이" (must do) expresses the necessity/obligation.

* target[5]: "tear each other apart"
  - source_tokens: `6: "서로 까지", 7: "뜯고"`
  - mapping_reason: "서로 까지" (even each other) and "뜯고" (tearing) define the action.

* target[6]: "and fight to get anywhere?"
  - source_tokens: `8: "싸움 을", 11: "사람 이잖아."`
  - mapping_reason: "싸움 을" (fight) and "사람 이잖아" (that's the kind of person/result) convey the consequence.

* target[7]: "So then,"
  - source_tokens: `12: "그러면"`
  - mapping_reason: "그러면" (then/so) acts as a discourse connector.

* target[8]: "how does this BJ chemistry"
  - source_tokens: `13: "어떻게", 14: "이제", 15: "이게", 16: "BJ", 17: "궁합은"`
  - mapping_reason: "어떻게" (how), "이게" (this), "BJ", and "궁합은" (chemistry) form the subject of the question.

* target[9]: "work?"
  - source_tokens: `18: "어떻게"`
  - mapping_reason: "어떻게" (how/in what way) functions as the interrogative for the process.

* target[10]: "How can one person...?"
  - source_tokens: `19: "한", 20: "사람 이", 21: "어떻게", 22: "어?"`
  - mapping_reason: "한 사람 이" (one person) and "어떻게" (how) + "어?" (filler/hesitation) capture the unfinished question.

result:
```html
0. <src>악인네는 </src> <tgt>If bad people are</tgt>; start=0.00, end=1.00
1. <src>서로 내놔 하니까 </src> <tgt>telling each other to hand it over,</tgt>; start=1.00, end=2.00
2. <src>그러면 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>어떻게 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>서로 까지 뜯고 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>싸움 을 해야 만이 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>되는 사람 이잖아. </src> <tgt>doesn't that mean they have to tear each other apart and fight to get anywhere?</tgt>; start=6.00, end=7.00
7. <src>그러면 </src> <tgt>So then,</tgt>; start=7.00, end=8.00
8. <src>어떻게 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>이제 이게 BJ </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>궁합은 </src> <tgt>how does this BJ chemistry</tgt>; start=10.00, end=11.00
11. <src>어떻게 한 사람 이 어떻게 어? </src> <tgt>work? How can one person...?</tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=13.12
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_E7ZEWK_4k08_W000004 ===

source:
- language: Korean
- transcription: 그러나 하나님의 백성의 믿음은 어떻게 강해질 수 있을까? 엄마, 엄마도 있다. 어떻게 강해질 수 있을까? 볼까요? 둘, 셋.
- source_tokens:
  0. 그러나
  1. 하나님 의
  2. 백성 의
  3. 믿음 은
  4. 어떻게
  5. 강해 질
  6. 수
  7. 있을까?
  8. 엄마,
  9. 엄마 도
  10. 있다.
  11. 어떻게
  12. 강해 질
  13. 수
  14. 있을까?
  15. 볼까요?
  16. 둘,
  17. 셋.

target:
- language: Japanese
- translation: しかし、神の民の信仰はどうすれば強くなれるのでしょうか？ママ、ママもいるね。どうすれば強くなれるのでしょうか？見てみましょうか？に、さん。
- target_sense_units:
  0. しかし、
  1. 神の
  2. 民の
  3. 信仰は
  4. どうすれば
  5. 強くなれるのでしょうか？
  6. ママ、
  7. ママも
  8. いるね。
  9. どうすれば
  10. 強くなれるのでしょうか？
  11. 見てみましょうか？
  12. に、
  13. さん。

scratchpad:
* target[0]: "しかし、"
  - source_tokens: `0: "그러나"`
  - mapping_reason: Direct translation of the discourse connective.

* target[1]: "神の"
  - source_tokens: `1: "하나님 의"`
  - mapping_reason: Genitive modifier "God's".

* target[2]: "民の"
  - source_tokens: `2: "백성 의"`
  - mapping_reason: Genitive modifier "people's".

* target[3]: "信仰は"
  - source_tokens: `3: "믿음 은"`
  - mapping_reason: Subject "faith".

* target[4]: "どうすれば"
  - source_tokens: `4: "어떻게"`
  - mapping_reason: Interrogative adverb "how".

* target[5]: "強くなれるのでしょうか？"
  - source_tokens: `5: "강해 질", 6: "수", 7: "있을까?"`
  - mapping_reason: Verb phrase expressing potential/question "can become strong".

* target[6]: "ママ、"
  - source_tokens: `8: "엄마,"`
  - mapping_reason: Direct address "Mom".

* target[7]: "ママも"
  - source_tokens: `9: "엄마 도"`
  - mapping_reason: Subject with additive particle "also".

* target[8]: "いるね。"
  - source_tokens: `10: "있다."`
  - mapping_reason: Existential verb "exists".

* target[9]: "どうすれば"
  - source_tokens: `11: "어떻게"`
  - mapping_reason: Interrogative adverb "how".

* target[10]: "強くなれるのでしょうか？"
  - source_tokens: `12: "강해 질", 13: "수", 14: "있을까?"`
  - mapping_reason: Verb phrase expressing potential/question "can become strong".

* target[11]: "見てみましょうか？"
  - source_tokens: `15: "볼까요?"`
  - mapping_reason: Suggestive/interrogative verb "shall we see".

* target[12]: "に、"
  - source_tokens: `16: "둘,"`
  - mapping_reason: Number "two".

* target[13]: "さん。"
  - source_tokens: `17: "셋."`
  - mapping_reason: Number "three".

result:
```html
0. <src>그러나 </src> <tgt>しかし、</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>하나님 의 백성 의 믿음 은 </src> <tgt>神の民の信仰は</tgt>; start=2.00, end=3.00
3. <src>어떻게 </src> <tgt>どうすれば</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>강해 질 수 있을까? </src> <tgt>強くなれるのでしょうか？</tgt>; start=5.00, end=6.00
6. <src>엄마, </src> <tgt>ママ、</tgt>; start=6.00, end=7.00
7. <src>엄마 도 있다. </src> <tgt>ママもいるね。</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>어떻게 강해 질 수 있을까? </src> <tgt>どうすれば強くなれるのでしょうか？</tgt>; start=10.00, end=11.00
11. <src>볼까요? </src> <tgt>見てみましょうか？</tgt>; start=11.00, end=12.00
12. <src>둘, 셋. </src> <tgt>に、さん。</tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=13.02
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_E9GzA6TOlV4_W000007 ===

source:
- language: Korean
- transcription: 일단 배그는 파밍이 제일 중요합니다, 여러분. 파밍을 열심히 해주세요. 어 발소리 난다. 어 당황한 척하면서 이렇게 파밍해주면 됩니다, 여러분.
- source_tokens:
  0. 일단
  1. 배그는
  2. 파밍이
  3. 제일
  4. 중요 합니다,
  5. 여러분.
  6. 파밍을
  7. 열심히
  8. 해주세요.
  9. 어
  10. 발소리
  11. 난다.
  12. 어
  13. 당황 한
  14. 척하 면서
  15. 이렇게
  16. 파밍해주면
  17. 됩니다,
  18. 여러분.

target:
- language: English
- translation: First of all, looting is the most important thing in PUBG, guys. Make sure you loot hard. Oh, I hear footsteps. Oh, just keep looting like this, guys, while acting like you're panicked.
- target_sense_units:
  0. First of all,
  1. looting is
  2. the most important thing
  3. in PUBG,
  4. guys.
  5. Make sure
  6. you loot hard.
  7. Oh,
  8. I hear footsteps.
  9. Oh,
  10. just keep looting
  11. like this,
  12. guys,
  13. while acting like
  14. you're panicked.

scratchpad:
* target[0]: "First of all,"
  - source_tokens: `0: "일단"`
  - mapping_reason: Direct translation of discourse marker.
* target[1]: "looting is"
  - source_tokens: `2: "파밍이"`
  - mapping_reason: Subject of the sentence.
* target[2]: "the most important thing"
  - source_tokens: `3: "제일", 4: "중요 합니다,"`
  - mapping_reason: Superlative adjective phrase.
* target[3]: "in PUBG,"
  - source_tokens: `1: "배그는"`
  - mapping_reason: Contextual location/subject matter.
* target[4]: "guys."
  - source_tokens: `5: "여러분."`
  - mapping_reason: Direct address.
* target[5]: "Make sure"
  - source_tokens: `8: "해주세요."`
  - mapping_reason: Imperative instruction marker.
* target[6]: "you loot hard."
  - source_tokens: `6: "파밍을", 7: "열심히"`
  - mapping_reason: Action and adverbial modifier.
* target[7]: "Oh,"
  - source_tokens: `9: "어"`
  - mapping_reason: Interjection.
* target[8]: "I hear footsteps."
  - source_tokens: `10: "발소리", 11: "난다."`
  - mapping_reason: Perception of sound.
* target[9]: "Oh,"
  - source_tokens: `12: "어"`
  - mapping_reason: Interjection.
* target[10]: "just keep looting"
  - source_tokens: `16: "파밍해주면", 17: "됩니다,"`
  - mapping_reason: Continued action instruction.
* target[11]: "like this,"
  - source_tokens: `15: "이렇게"`
  - mapping_reason: Manner adverb.
* target[12]: "guys,"
  - source_tokens: `18: "여러분."`
  - mapping_reason: Direct address.
* target[13]: "while acting like"
  - source_tokens: `14: "척하 면서"`
  - mapping_reason: Conjunction indicating simultaneous action.
* target[14]: "you're panicked."
  - source_tokens: `13: "당황 한"`
  - mapping_reason: State of being.

result:
```html
0. <src>일단 배그는 파밍이 </src> <tgt>First of all, looting is</tgt>; start=0.00, end=1.00
1. <src>제일 중요 합니다, </src> <tgt>the most important thing in PUBG,</tgt>; start=1.00, end=2.00
2. <src>여러분. </src> <tgt>guys.</tgt>; start=2.00, end=3.00
3. <src>파밍을 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>열심히 해주세요. 어 </src> <tgt>Make sure you loot hard. Oh,</tgt>; start=4.00, end=5.00
5. <src>발소리 난다. </src> <tgt>I hear footsteps.</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>어 </src> <tgt>Oh,</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>당황 한 척하 면서 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>이렇게 파밍해주면 됩니다, 여러분. </src> <tgt>just keep looting like this, guys, while acting like you're panicked.</tgt>; start=12.00, end=12.73
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G1hDgTWHSC8_W000038 ===

source:
- language: Korean
- transcription: 자기 그림을 그리면서 카피할 때 머리 속에 기억해두고 메모해둔 표현 방법을 그대로 실제 적용하면서 그림을 그립니다. 그러면 그림 그리는 실력이 빠르게 좋아집니다.
- source_tokens:
  0. 자기
  1. 그림 을
  2. 그리 면서
  3. 카피할
  4. 때
  5. 머리
  6. 속에
  7. 기억 해두고
  8. 메모 해둔
  9. 표현
  10. 방법 을
  11. 그대로
  12. 실제
  13. 적용 하면서
  14. 그림 을
  15. 그립 니다.
  16. 그러면
  17. 그림
  18. 그리 는
  19. 실력 이
  20. 빠르 게
  21. 좋아집니다.

target:
- language: Japanese
- translation: 自分の絵を描きながら模写をするときは、頭の中で覚えてメモしておいた表現方法を、そのまま実際に使って描いています。そうすると、絵を描く実力がどんどん上達します。
- target_sense_units:
  0. 自分の
  1. 絵を
  2. 描きながら
  3. 模写をする
  4. ときは、
  5. 頭の中で
  6. 覚えて
  7. メモしておいた
  8. 表現方法を、
  9. そのまま
  10. 実際に
  11. 使って
  12. 描いています。
  13. そうすると、
  14. 絵を
  15. 描く実力が
  16. どんどん
  17. 上達します。

scratchpad:
* target[0]: "自分の"
  - source_tokens: `0: "자기"`
  - mapping_reason: "자기" (self/own) maps to "自分の".

* target[1]: "絵を"
  - source_tokens: `1: "그림 을"`
  - mapping_reason: "그림을" (picture/drawing) maps to "絵を".

* target[2]: "描きながら"
  - source_tokens: `2: "그리 면서"`
  - mapping_reason: "그리면서" (while drawing) maps to "描きながら".

* target[3]: "模写をする"
  - source_tokens: `3: "카피할"`
  - mapping_reason: "카피할" (to copy/trace) maps to "模写をする".

* target[4]: "ときは、"
  - source_tokens: `4: "때"`
  - mapping_reason: "때" (when) maps to "ときは".

* target[5]: "頭の中で"
  - source_tokens: `5: "머리", 6: "속에"`
  - mapping_reason: "머리 속에" (in the head) maps to "頭の中で".

* target[6]: "覚えて"
  - source_tokens: `7: "기억 해두고"`
  - mapping_reason: "기억해두고" (remembering) maps to "覚えて".

* target[7]: "メモしておいた"
  - source_tokens: `8: "메모 해둔"`
  - mapping_reason: "메모해둔" (noted down) maps to "メモしておいた".

* target[8]: "表現方法を、"
  - source_tokens: `9: "표현", 10: "방법 을"`
  - mapping_reason: "표현 방법을" (expression method) maps to "表現方法を".

* target[9]: "そのまま"
  - source_tokens: `11: "그대로"`
  - mapping_reason: "그대로" (as it is) maps to "そのまま".

* target[10]: "実際に"
  - source_tokens: `12: "실제"`
  - mapping_reason: "실제" (actually) maps to "実際に".

* target[11]: "使って"
  - source_tokens: `13: "적용 하면서"`
  - mapping_reason: "적용하면서" (applying/using) maps to "使って".

* target[12]: "描いています。"
  - source_tokens: `14: "그림 을", 15: "그립 니다."`
  - mapping_reason: "그림을 그립니다" (drawing a picture) maps to "描いています".

* target[13]: "そうすると、"
  - source_tokens: `16: "그러면"`
  - mapping_reason: "그러면" (then/if so) maps to "そうすると".

* target[14]: "絵を"
  - source_tokens: `17: "그림"`
  - mapping_reason: "그림" (picture) maps to "絵を".

* target[15]: "描く実力が"
  - source_tokens: `18: "그리 는", 19: "실력 이"`
  - mapping_reason: "그리는 실력이" (drawing skill) maps to "描く実力が".

* target[16]: "どんどん"
  - source_tokens: `20: "빠르 게"`
  - mapping_reason: "빠르게" (quickly/rapidly) maps to "どんどん".

* target[17]: "上達します。"
  - source_tokens: `21: "좋아집니다."`
  - mapping_reason: "좋아집니다" (improves) maps to "上達します".

result:
```html
0. <src>자기 그림 을 </src> <tgt>自分の絵を</tgt>; start=0.00, end=1.00
1. <src>그리 면서 카피할 때 </src> <tgt>描きながら模写をするときは、</tgt>; start=1.00, end=2.00
2. <src>머리 속에 </src> <tgt>頭の中で</tgt>; start=2.00, end=3.00
3. <src>기억 해두고 메모 해둔 </src> <tgt>覚えてメモしておいた</tgt>; start=3.00, end=4.00
4. <src>표현 방법 을 </src> <tgt>表現方法を、</tgt>; start=4.00, end=5.00
5. <src>그대로 </src> <tgt>そのまま</tgt>; start=5.00, end=6.00
6. <src>실제 적용 하면서 </src> <tgt>実際に使って</tgt>; start=6.00, end=7.00
7. <src>그림 을 그립 니다. </src> <tgt>描いています。</tgt>; start=7.00, end=8.00
8. <src>그러면 </src> <tgt>そうすると、</tgt>; start=8.00, end=9.00
9. <src>그림 그리 는 실력 이 </src> <tgt>絵を描く実力が</tgt>; start=9.00, end=10.00
10. <src>빠르 게 </src> <tgt>どんどん</tgt>; start=10.00, end=11.00
11. <src>좋아집니다. </src> <tgt>上達します。</tgt>; start=11.00, end=11.14
```

- max_empty_window_count: 0


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G3A_RG4qGF4_W000002 ===

source:
- language: Korean
- transcription: 그리고 아 그리고 우리가 뉴욕에 살고 있으니까 좀 뉴욕과 뉴저지 지역의 유명한 곳을 소개해드릴 수도 있어요. 그렇죠, 그렇죠. 직접 그 현장에 가서 저희들이 이제 체험도 해보고 소개도 해드리고 그런 프로그램도 만들 기획이고요. 어 뉴욕 미니스에 대한 설명을 좀 해주시죠.
- source_tokens:
  0. 그리고
  1. 아
  2. 그리고
  3. 우리 가
  4. 뉴욕 에
  5. 살고
  6. 있으니까
  7. 좀
  8. 뉴욕 과
  9. 뉴저지
  10. 지역 의
  11. 유명 한
  12. 곳을
  13. 소개 해드릴
  14. 수도
  15. 있어요.
  16. 그렇 죠,
  17. 그렇 죠.
  18. 직접
  19. 그
  20. 현장 에
  21. 가서
  22. 저희 들이
  23. 이제
  24. 체험 도
  25. 해보고
  26. 소개 도
  27. 해드리고
  28. 그런
  29. 프로그램 도
  30. 만들
  31. 기획 이고요.
  32. 어
  33. 뉴욕
  34. 미니 스에
  35. 대한
  36. 설명 을
  37. 좀
  38. 해주시죠.

target:
- language: Japanese
- translation: そして、あ、私たちはニューヨークに住んでいるので、ニューヨークやニュージャージー地域の有名な場所をご紹介することもできます。そうですね、その通りです。実際にその現場に行きます。そこで体験してご紹介するような番組も企画しています。えー、ニューヨーク・ミニスについて少し説明していただけますか？
- target_sense_units:
  0. そして、
  1. あ、
  2. 私たちは
  3. ニューヨークに
  4. 住んでいるので、
  5. ニューヨークや
  6. ニュージャージー地域の
  7. 有名な場所を
  8. ご紹介することもできます。
  9. そうですね、
  10. その通りです。
  11. 実際に
  12. その現場に
  13. 行きます。
  14. そこで
  15. 体験して
  16. ご紹介するような
  17. 番組も
  18. 企画しています。
  19. えー、
  20. ニューヨーク・ミニスについて
  21. 少し
  22. 説明していただけますか？

scratchpad:
* target[0]: "そして、"
  - source_tokens: `0: "그리고"`
  - mapping_reason: Discourse connective "and".
* target[1]: "あ、"
  - source_tokens: `1: "아"`
  - mapping_reason: Filler/interjection.
* target[2]: "私たちは"
  - source_tokens: `3: "우리 가"`
  - mapping_reason: Subject "we".
* target[3]: "ニューヨークに"
  - source_tokens: `4: "뉴욕 에"`
  - mapping_reason: Location "in New York".
* target[4]: "住んでいるので、"
  - source_tokens: `5: "살고", 6: "있으니까"`
  - mapping_reason: Verb "living" and causal connector "because".
* target[5]: "ニューヨークや"
  - source_tokens: `8: "뉴욕 과"`
  - mapping_reason: Location "New York" and conjunction "and/with".
* target[6]: "ニュージャージー地域の"
  - source_tokens: `9: "뉴저지", 10: "지역 의"`
  - mapping_reason: Location "New Jersey area".
* target[7]: "有名な場所を"
  - source_tokens: `11: "유명 한", 12: "곳을"`
  - mapping_reason: Object "famous places".
* target[8]: "ご紹介することもできます。"
  - source_tokens: `13: "소개 해드릴", 14: "수도", 15: "있어요."`
  - mapping_reason: Verb "can introduce".
* target[9]: "そうですね、"
  - source_tokens: `16: "그렇 죠,"`
  - mapping_reason: Agreement marker.
* target[10]: "その通りです。"
  - source_tokens: `17: "그렇 죠."`
  - mapping_reason: Agreement marker.
* target[11]: "実際に"
  - source_tokens: `18: "직접"`
  - mapping_reason: Adverb "actually/directly".
* target[12]: "その現場に"
  - source_tokens: `19: "그", 20: "현장 에"`
  - mapping_reason: Location "to that site".
* target[13]: "行きます。"
  - source_tokens: `21: "가서"`
  - mapping_reason: Verb "go".
* target[14]: "そこで"
  - source_tokens: `23: "이제"`
  - mapping_reason: Temporal/situational reference "then/there".
* target[15]: "体験して"
  - source_tokens: `24: "체험 도", 25: "해보고"`
  - mapping_reason: Verb "experience".
* target[16]: "ご紹介するような"
  - source_tokens: `26: "소개 도", 27: "해드리고"`
  - mapping_reason: Verb "introduce".
* target[17]: "番組も"
  - source_tokens: `28: "그런", 29: "프로그램 도"`
  - mapping_reason: Object "program".
* target[18]: "企画しています。"
  - source_tokens: `30: "만들", 31: "기획 이고요."`
  - mapping_reason: Verb "planning".
* target[19]: "えー、"
  - source_tokens: `32: "어"`
  - mapping_reason: Filler.
* target[20]: "ニューヨーク・ミニスについて"
  - source_tokens: `33: "뉴욕", 34: "미니 스에", 35: "대한"`
  - mapping_reason: Topic "about New York Minis".
* target[21]: "少し"
  - source_tokens: `37: "좀"`
  - mapping_reason: Adverb "a little".
* target[22]: "説明していただけますか？"
  - source_tokens: `36: "설명 을", 38: "해주시죠."`
  - mapping_reason: Verb "please explain".

result:
```html
0. <src>그리고 </src> <tgt>そして、</tgt>; start=0.00, end=1.00
1. <src>아 그리고 </src> <tgt>あ、</tgt>; start=1.00, end=2.00
2. <src>우리 가 </src> <tgt>私たちは</tgt>; start=2.00, end=3.00
3. <src>뉴욕 에 </src> <tgt>ニューヨークに</tgt>; start=3.00, end=4.00
4. <src>살고 있으니까 좀 </src> <tgt>住んでいるので、</tgt>; start=4.00, end=5.00
5. <src>뉴욕 과 뉴저지 지역 의 </src> <tgt>ニューヨークやニュージャージー地域の</tgt>; start=5.00, end=6.00
6. <src>유명 한 곳을 </src> <tgt>有名な場所を</tgt>; start=6.00, end=7.00
7. <src>소개 해드릴 수도 있어요. 그렇 죠, 그렇 죠. </src> <tgt>ご紹介することもできます。そうですね、その通りです。</tgt>; start=7.00, end=8.00
8. <src>직접 그 현장 에 </src> <tgt>実際にその現場に</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>가서 저희 들이 이제 </src> <tgt>行きます。そこで</tgt>; start=10.00, end=11.00
11. <src>체험 도 해보고 </src> <tgt>体験して</tgt>; start=11.00, end=12.00
12. <src>소개 도 해드리고 </src> <tgt>ご紹介するような</tgt>; start=12.00, end=13.00
13. <src>그런 프로그램 도 </src> <tgt>番組も</tgt>; start=13.00, end=14.00
14. <src>만들 기획 이고요. 어 </src> <tgt>企画しています。えー、</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>뉴욕 미니 스에 대한 설명 을 </src> <tgt>ニューヨーク・ミニスについて</tgt>; start=16.00, end=17.00
17. <src>좀 해주시죠. </src> <tgt>少し説明していただけますか？</tgt>; start=17.00, end=17.74
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G1hDgTWHSC8_W000038 ===

source:
- language: Korean
- transcription: 자기 그림을 그리면서 카피할 때 머리 속에 기억해두고 메모해둔 표현 방법을 그대로 실제 적용하면서 그림을 그립니다. 그러면 그림 그리는 실력이 빠르게 좋아집니다.
- source_tokens:
  0. 자기
  1. 그림 을
  2. 그리 면서
  3. 카피할
  4. 때
  5. 머리
  6. 속에
  7. 기억 해두고
  8. 메모 해둔
  9. 표현
  10. 방법 을
  11. 그대로
  12. 실제
  13. 적용 하면서
  14. 그림 을
  15. 그립 니다.
  16. 그러면
  17. 그림
  18. 그리 는
  19. 실력 이
  20. 빠르 게
  21. 좋아집니다.

target:
- language: English
- translation: When I copy while drawing my own pictures, I directly apply the techniques I've memorized or noted down. This helps improve my drawing skills quickly.
- target_sense_units:
  0. When I copy
  1. while drawing
  2. my own pictures,
  3. I directly apply
  4. the techniques
  5. I've memorized
  6. or noted down.
  7. This helps improve
  8. my drawing skills
  9. quickly.

scratchpad:
* target[0]: "When I copy"
  - source_tokens: `3: "카피할", 4: "때"`
  - mapping_reason: "When" maps to "때", "copy" maps to "카피할".
* target[1]: "while drawing"
  - source_tokens: `2: "그리 면서"`
  - mapping_reason: "drawing" maps to "그리", "while" maps to "면서".
* target[2]: "my own pictures,"
  - source_tokens: `0: "자기", 1: "그림 을"`
  - mapping_reason: "my own" maps to "자기", "pictures" maps to "그림".
* target[3]: "I directly apply"
  - source_tokens: `11: "그대로", 12: "실제", 13: "적용 하면서"`
  - mapping_reason: "directly" maps to "그대로" and "실제", "apply" maps to "적용 하면서".
* target[4]: "the techniques"
  - source_tokens: `9: "표현", 10: "방법 을"`
  - mapping_reason: "techniques" maps to "표현 방법".
* target[5]: "I've memorized"
  - source_tokens: `5: "머리", 6: "속에", 7: "기억 해두고"`
  - mapping_reason: "memorized" maps to "머리 속에 기억 해두고".
* target[6]: "or noted down."
  - source_tokens: `8: "메모 해둔"`
  - mapping_reason: "noted down" maps to "메모 해둔".
* target[7]: "This helps improve"
  - source_tokens: `16: "그러면", 21: "좋아집니다."`
  - mapping_reason: "This" maps to "그러면", "improve" maps to "좋아집니다".
* target[8]: "my drawing skills"
  - source_tokens: `17: "그림", 18: "그리 는", 19: "실력 이"`
  - mapping_reason: "drawing skills" maps to "그림 그리 는 실력".
* target[9]: "quickly."
  - source_tokens: `20: "빠르 게"`
  - mapping_reason: "quickly" maps to "빠르 게".

result:
```html
0. <src>자기 그림 을 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>그리 면서 카피할 때 </src> <tgt>When I copy while drawing my own pictures,</tgt>; start=1.00, end=2.00
2. <src>머리 속에 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>기억 해두고 메모 해둔 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>표현 방법 을 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>그대로 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>실제 적용 하면서 </src> <tgt>I directly apply the techniques I've memorized or noted down.</tgt>; start=6.00, end=7.00
7. <src>그림 을 그립 니다. </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>그러면 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>그림 그리 는 실력 이 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>빠르 게 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>좋아집니다. </src> <tgt>This helps improve my drawing skills quickly.</tgt>; start=11.00, end=11.14
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_DlMYWhPK1Lg_W000119 ===

source:
- language: Korean
- transcription: 악인네는 서로 내놔 하니까 그러면 어떻게 서로까지 뜯고 싸움을 해야만이 되는 사람이잖아. 그러면 어떻게 이제 이게 BJ 궁합은 어떻게 한 사람이 어떻게 어?
- source_tokens:
  0. 악인네는
  1. 서로
  2. 내놔
  3. 하니까
  4. 그러면
  5. 어떻게
  6. 서로 까지
  7. 뜯고
  8. 싸움 을
  9. 해야 만이
  10. 되는
  11. 사람 이잖아.
  12. 그러면
  13. 어떻게
  14. 이제
  15. 이게
  16. BJ
  17. 궁합은
  18. 어떻게
  19. 한
  20. 사람 이
  21. 어떻게
  22. 어?

target:
- language: Japanese
- translation: 悪人同士が「出せ」と言い合っていたら、お互いに奪い合って喧嘩するしかない人たちですよね。じゃあ、このBJの相性っていうのは、一人がどうやって……？
- target_sense_units:
  0. 悪人同士が
  1. 「出せ」と
  2. 言い合っていたら、
  3. お互いに
  4. 奪い合って
  5. 喧嘩する
  6. しかない
  7. 人たち
  8. ですよね。
  9. じゃあ、
  10. このBJの
  11. 相性っていうのは、
  12. 一人が
  13. どうやって……？

scratchpad:
* target[0]: "悪人同士が"
  - source_tokens: `0: "악인네는", 1: "서로"`
  - mapping_reason: "악인네" (bad people) + "서로" (each other/together) forms "悪人同士" (bad people together).
* target[1]: "「出せ」と"
  - source_tokens: `2: "내놔"`
  - mapping_reason: "내놔" maps to the quoted content "出せ".
* target[2]: "言い合っていたら、"
  - source_tokens: `3: "하니까"`
  - mapping_reason: "하니까" (if they say) maps to "言い合っていたら" (if they were saying to each other).
* target[3]: "お互いに"
  - source_tokens: `6: "서로 까지"`
  - mapping_reason: "서로 까지" maps to "お互いに" (each other).
* target[4]: "奪い合って"
  - source_tokens: `7: "뜯고"`
  - mapping_reason: "뜯고" (tearing/pulling/taking) maps to "奪い合って" (taking/fighting over).
* target[5]: "喧嘩する"
  - source_tokens: `8: "싸움 을"`
  - mapping_reason: "싸움" maps to "喧嘩".
* target[6]: "しかない"
  - source_tokens: `9: "해야 만이"`
  - mapping_reason: "해야 만이" (must do) maps to the restrictive "しかない" (have no choice but to).
* target[7]: "人たち"
  - source_tokens: `10: "되는", 11: "사람 이잖아."`
  - mapping_reason: "되는 사람" (person who becomes/is) maps to "人たち" (people).
* target[8]: "ですよね。"
  - source_tokens: `11: "사람 이잖아."`
  - mapping_reason: "-잖아" (is it not/isn't it) maps to the confirmative "ですよね".
* target[9]: "じゃあ、"
  - source_tokens: `12: "그러면"`
  - mapping_reason: "그러면" (then/well) maps to "じゃあ".
* target[10]: "このBJの"
  - source_tokens: `15: "이게", 16: "BJ"`
  - mapping_reason: "이게" (this) + "BJ" maps to "このBJの".
* target[11]: "相性っていうのは、"
  - source_tokens: `17: "궁합은"`
  - mapping_reason: "궁합은" maps to "相性".
* target[12]: "一人が"
  - source_tokens: `19: "한", 20: "사람 이"`
  - mapping_reason: "한 사람" maps to "一人".
* target[13]: "どうやって……？"
  - source_tokens: `13: "어떻게", 18: "어떻게", 21: "어떻게", 22: "어?"`
  - mapping_reason: Repeated "어떻게" and "어?" map to the questioning "どうやって".

result:
```html
0. <src>악인네는 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>서로 내놔 하니까 </src> <tgt>悪人同士が「出せ」と言い合っていたら、</tgt>; start=1.00, end=2.00
2. <src>그러면 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>어떻게 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>서로 까지 뜯고 </src> <tgt>お互いに奪い合って</tgt>; start=4.00, end=5.00
5. <src>싸움 을 해야 만이 </src> <tgt>喧嘩するしかない</tgt>; start=5.00, end=6.00
6. <src>되는 사람 이잖아. </src> <tgt>人たちですよね。</tgt>; start=6.00, end=7.00
7. <src>그러면 </src> <tgt>じゃあ、</tgt>; start=7.00, end=8.00
8. <src>어떻게 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>이제 이게 BJ </src> <tgt>このBJの</tgt>; start=9.00, end=10.00
10. <src>궁합은 </src> <tgt>相性っていうのは、</tgt>; start=10.00, end=11.00
11. <src>어떻게 한 사람 이 어떻게 어? </src> <tgt>一人がどうやって……？</tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=13.12
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_DlMYWhPK1Lg_W000119 ===

source:
- language: Korean
- transcription: 악인네는 서로 내놔 하니까 그러면 어떻게 서로까지 뜯고 싸움을 해야만이 되는 사람이잖아. 그러면 어떻게 이제 이게 BJ 궁합은 어떻게 한 사람이 어떻게 어?
- source_tokens:
  0. 악인네는
  1. 서로
  2. 내놔
  3. 하니까
  4. 그러면
  5. 어떻게
  6. 서로 까지
  7. 뜯고
  8. 싸움 을
  9. 해야 만이
  10. 되는
  11. 사람 이잖아.
  12. 그러면
  13. 어떻게
  14. 이제
  15. 이게
  16. BJ
  17. 궁합은
  18. 어떻게
  19. 한
  20. 사람 이
  21. 어떻게
  22. 어?

target:
- language: Chinese
- translation: 恶人之间互相要求对方拿出来，那他们不就是那种非得互相撕扯、打架才能解决的人吗？那现在这个BJ的相性啊，一个人怎么……？
- target_sense_units:
  0. 恶人之间
  1. 互相要求对方
  2. 拿出来，
  3. 那
  4. 他们不就是
  5. 那种
  6. 非得互相撕扯、打架
  7. 才能解决
  8. 的人吗？
  9. 那
  10. 现在
  11. 这个
  12. BJ的相性啊，
  13. 一个人
  14. 怎么……？

scratchpad:
* target[0]: "恶人之间"
  - source_tokens: `0: "악인네는"`
  - mapping_reason: "악인네" (evil people/villains) maps to "恶人", "는" implies the subject/group "之间".
* target[1]: "互相要求对方"
  - source_tokens: `1: "서로", 3: "하니까"`
  - mapping_reason: "서로" (each other) and the causative/quotative "하니까" (saying/demanding) create the requirement.
* target[2]: "拿出来，"
  - source_tokens: `2: "내놔"`
  - mapping_reason: "내놔" (give it out/bring it out) maps to "拿出来".
* target[3]: "那"
  - source_tokens: `4: "그러면"`
  - mapping_reason: "그러면" (then/in that case) maps to discourse marker "那".
* target[4]: "他们不就是"
  - source_tokens: `11: "사람 이잖아."`
  - mapping_reason: "-잖아" (isn't it the case that) maps to "不就是".
* target[5]: "那种"
  - source_tokens: `10: "되는"`
  - mapping_reason: "되는" (becoming/being such) functions as a classifier for the type of person.
* target[6]: "非得互相撕扯、打架"
  - source_tokens: `6: "서로 까지", 7: "뜯고", 8: "싸움 을"`
  - mapping_reason: "서로" (each other), "뜯고" (tearing/ripping), "싸움" (fighting) map to these actions.
* target[7]: "才能解决"
  - source_tokens: `9: "해야 만이"`
  - mapping_reason: "해야 만이" (must do only then) maps to "才能" (only then can).
* target[8]: "的人吗？"
  - source_tokens: `11: "사람 이잖아."`
  - mapping_reason: "사람" (person) maps to "人", question marker maps to "吗".
* target[9]: "那"
  - source_tokens: `12: "그러면"`
  - mapping_reason: "그러면" (then) maps to "那".
* target[10]: "现在"
  - source_tokens: `14: "이제"`
  - mapping_reason: "이제" (now) maps to "现在".
* target[11]: "这个"
  - source_tokens: `15: "이게"`
  - mapping_reason: "이게" (this thing) maps to "这个".
* target[12]: "BJ的相性啊，"
  - source_tokens: `16: "BJ", 17: "궁합은"`
  - mapping_reason: "BJ" and "궁합" (compatibility/affinity) map to "BJ的相性".
* target[13]: "一个人"
  - source_tokens: `19: "한", 20: "사람 이"`
  - mapping_reason: "한 사람" maps to "一个人".
* target[14]: "怎么……？"
  - source_tokens: `5: "어떻게", 13: "어떻게", 18: "어떻게", 21: "어떻게", 22: "어?"`
  - mapping_reason: Repeated "어떻게" (how) and the filler "어?" map to the hesitant "怎么……？".

result:
```html
0. <src>악인네는 </src> <tgt>恶人之间</tgt>; start=0.00, end=1.00
1. <src>서로 내놔 하니까 </src> <tgt>互相要求对方拿出来，</tgt>; start=1.00, end=2.00
2. <src>그러면 </src> <tgt>那</tgt>; start=2.00, end=3.00
3. <src>어떻게 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>서로 까지 뜯고 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>싸움 을 해야 만이 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>되는 사람 이잖아. </src> <tgt>他们不就是那种非得互相撕扯、打架才能解决的人吗？</tgt>; start=6.00, end=7.00
7. <src>그러면 </src> <tgt>那</tgt>; start=7.00, end=8.00
8. <src>어떻게 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>이제 이게 BJ </src> <tgt>现在这个</tgt>; start=9.00, end=10.00
10. <src>궁합은 </src> <tgt>BJ的相性啊，</tgt>; start=10.00, end=11.00
11. <src>어떻게 한 사람 이 어떻게 어? </src> <tgt>一个人怎么……？</tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=13.12
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_GxLlh9Eui8c_W000249 ===

source:
- language: Korean
- transcription: 돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.
- source_tokens:
  0. 돌파 하고
  1. 승리 해야
  2. 한다.
  3. 다만
  4. 배도에
  5. 죄까지
  6. 갈
  7. 수
  8. 있으니
  9. 하나님
  10. 앞에서
  11. 늘
  12. 겸손 하라는
  13. 메시지 를
  14. 전하 는
  15. 대신
  16. 진짜
  17. 거듭 난
  18. 성도 도
  19. 진짜
  20. 지옥 에
  21. 아주
  22. 잘
  23. 가니까
  24. 대부분
  25. 지옥
  26. 가니까.

target:
- language: Japanese
- translation: 突破して勝利しなければならない。ただ、背教の罪に至る可能性もある。だから「神の前で常に謙遜であるべきだ」というメッセージを伝える代わりに、本当に生まれ変わった聖徒も本当に地獄にとてもよく行く。なぜなら、ほとんどの人が地獄に行くからだ。
- target_sense_units:
  0. 突破して
  1. 勝利しなければならない。
  2. ただ、
  3. 背教の罪に
  4. 至る可能性もある。
  5. だから
  6. 「神の前で
  7. 常に謙遜であるべきだ」
  8. というメッセージを
  9. 伝える代わりに、
  10. 本当に
  11. 生まれ変わった聖徒も
  12. 本当に
  13. 地獄にとてもよく行く。
  14. なぜなら、
  15. ほとんどの人が
  16. 地獄に行くからだ。

scratchpad:
* target[0]: "突破して"
  - source_tokens: `0: "돌파 하고"`
  - mapping_reason: "돌파" (breakthrough) corresponds to "突破" (breakthrough).

* target[1]: "勝利しなければならない。"
  - source_tokens: `1: "승리 해야", 2: "한다."`
  - mapping_reason: "승리 해야 한다" corresponds to "勝利しなければならない".

* target[2]: "ただ、"
  - source_tokens: `3: "다만"`
  - mapping_reason: "다만" corresponds to "ただ".

* target[3]: "背教の罪に"
  - source_tokens: `4: "배도에", 5: "죄까지"`
  - mapping_reason: "배도" is apostasy/背教, "죄" is sin/罪.

* target[4]: "至る可能性もある。"
  - source_tokens: `6: "갈", 7: "수", 8: "있으니"`
  - mapping_reason: "갈 수 있으니" (can reach) corresponds to "至る可能性がある".

* target[5]: "だから"
  - source_tokens: `8: "있으니"`
  - mapping_reason: "있으니" implies a connective logic (since/therefore) leading to the next clause.

* target[6]: "「神の前で"
  - source_tokens: `9: "하나님", 10: "앞에서"`
  - mapping_reason: Direct translation of "하나님 앞에서".

* target[7]: "常に謙遜であるべきだ」"
  - source_tokens: `11: "늘", 12: "겸손 하라는"`
  - mapping_reason: "늘 겸손 하라는" corresponds to "常に謙遜であるべきだ".

* target[8]: "というメッセージを"
  - source_tokens: `13: "메시지 를"`
  - mapping_reason: Direct translation.

* target[9]: "伝える代わりに、"
  - source_tokens: `14: "전하 는", 15: "대신"`
  - mapping_reason: "전하는 대신" corresponds to "伝える代わりに".

* target[10]: "本当に"
  - source_tokens: `16: "진짜"`
  - mapping_reason: Direct translation.

* target[11]: "生まれ変わった聖徒も"
  - source_tokens: `17: "거듭 난", 18: "성도 도"`
  - mapping_reason: Direct translation.

* target[12]: "本当に"
  - source_tokens: `19: "진짜"`
  - mapping_reason: Direct translation.

* target[13]: "地獄にとてもよく行く。"
  - source_tokens: `20: "지옥 에", 21: "아주", 22: "잘", 23: "가니까"`
  - mapping_reason: "지옥에 아주 잘 가니까" corresponds to "地獄にとてもよく行く".

* target[14]: "なぜなら、"
  - source_tokens: `23: "가니까"`
  - mapping_reason: "가니까" (because) acts as a causal marker.

* target[15]: "ほとんどの人が"
  - source_tokens: `24: "대부분"`
  - mapping_reason: "대부분" corresponds to "ほとんどの".

* target[16]: "地獄に行くからだ。"
  - source_tokens: `25: "지옥", 26: "가니까."`
  - mapping_reason: "지옥 가니까" corresponds to "地獄に行くからだ".

result:
```html
0. <src>돌파 하고 </src> <tgt>突破して</tgt>; start=0.00, end=1.00
1. <src>승리 해야 한다. </src> <tgt>勝利しなければならない。</tgt>; start=1.00, end=2.00
2. <src>다만 배도에 </src> <tgt>ただ、</tgt>; start=2.00, end=3.00
3. <src>죄까지 </src> <tgt>背教の罪に</tgt>; start=3.00, end=4.00
4. <src>갈 수 있으니 하나님 </src> <tgt>至る可能性もある。だから</tgt>; start=4.00, end=5.00
5. <src>앞에서 늘 </src> <tgt>「神の前で</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>겸손 하라는 메시지 를 </src> <tgt>常に謙遜であるべきだ」というメッセージを</tgt>; start=7.00, end=8.00
8. <src>전하 는 대신 </src> <tgt>伝える代わりに、</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>진짜 거듭 난 성도 도 </src> <tgt>本当に生まれ変わった聖徒も</tgt>; start=10.00, end=11.00
11. <src>진짜 지옥 에 </src> <tgt>本当に</tgt>; start=11.00, end=12.00
12. <src>아주 잘 가니까 </src> <tgt>地獄にとてもよく行く。なぜなら、</tgt>; start=12.00, end=13.00
13. <src>대부분 </src> <tgt>ほとんどの人が</tgt>; start=13.00, end=14.00
14. <src>지옥 가니까. </src> <tgt>地獄に行くからだ。</tgt>; start=14.00, end=14.30
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G3A_RG4qGF4_W000002 ===

source:
- language: Korean
- transcription: 그리고 아 그리고 우리가 뉴욕에 살고 있으니까 좀 뉴욕과 뉴저지 지역의 유명한 곳을 소개해드릴 수도 있어요. 그렇죠, 그렇죠. 직접 그 현장에 가서 저희들이 이제 체험도 해보고 소개도 해드리고 그런 프로그램도 만들 기획이고요. 어 뉴욕 미니스에 대한 설명을 좀 해주시죠.
- source_tokens:
  0. 그리고
  1. 아
  2. 그리고
  3. 우리 가
  4. 뉴욕 에
  5. 살고
  6. 있으니까
  7. 좀
  8. 뉴욕 과
  9. 뉴저지
  10. 지역 의
  11. 유명 한
  12. 곳을
  13. 소개 해드릴
  14. 수도
  15. 있어요.
  16. 그렇 죠,
  17. 그렇 죠.
  18. 직접
  19. 그
  20. 현장 에
  21. 가서
  22. 저희 들이
  23. 이제
  24. 체험 도
  25. 해보고
  26. 소개 도
  27. 해드리고
  28. 그런
  29. 프로그램 도
  30. 만들
  31. 기획 이고요.
  32. 어
  33. 뉴욕
  34. 미니 스에
  35. 대한
  36. 설명 을
  37. 좀
  38. 해주시죠.

target:
- language: English
- translation: And, uh, since we live in New York, we could also introduce some famous spots in the New York and New Jersey area. Right, exactly. We're planning to make a program. We'll actually go to the sites, experience them ourselves, and introduce them to you. Uh, could you explain what 'New York Minis' is?
- target_sense_units:
  0. And, uh, since
  1. we live in
  2. New York,
  3. we could also introduce
  4. some famous spots
  5. in the New York
  6. and New Jersey area.
  7. Right, exactly.
  8. We're planning to
  9. make a program.
  10. We'll actually go to the sites,
  11. experience them ourselves,
  12. and introduce them to you.
  13. Uh, could you explain
  14. what ' New York Minis '
  15. is?

scratchpad:
* target[0]: "And, uh, since"
  - source_tokens: `0: "그리고", 1: "아", 6: "있으니까"`
  - mapping_reason: Connective and causal marker.
* target[1]: "we live in"
  - source_tokens: `3: "우리 가", 5: "살고"`
  - mapping_reason: Subject and state of living.
* target[2]: "New York,"
  - source_tokens: `4: "뉴욕 에"`
  - mapping_reason: Location.
* target[3]: "we could also introduce"
  - source_tokens: `7: "좀", 13: "소개 해드릴", 14: "수도", 15: "있어요."`
  - mapping_reason: Modal ability and action of introducing.
* target[4]: "some famous spots"
  - source_tokens: `11: "유명 한", 12: "곳을"`
  - mapping_reason: Object of introduction.
* target[5]: "in the New York"
  - source_tokens: `8: "뉴욕 과", 10: "지역 의"`
  - mapping_reason: Location modifier.
* target[6]: "and New Jersey area."
  - source_tokens: `9: "뉴저지", 10: "지역 의"`
  - mapping_reason: Location modifier.
* target[7]: "Right, exactly."
  - source_tokens: `16: "그렇 죠,", 17: "그렇 죠."`
  - mapping_reason: Agreement markers.
* target[8]: "We're planning to"
  - source_tokens: `31: "기획 이고요."`
  - mapping_reason: Intent/plan.
* target[9]: "make a program."
  - source_tokens: `29: "프로그램 도", 30: "만들"`
  - mapping_reason: Goal of the plan.
* target[10]: "We'll actually go to the sites,"
  - source_tokens: `18: "직접", 19: "그", 20: "현장 에", 21: "가서"`
  - mapping_reason: Action of visiting sites.
* target[11]: "experience them ourselves,"
  - source_tokens: `22: "저희 들이", 24: "체험 도", 25: "해보고"`
  - mapping_reason: Action of experiencing.
* target[12]: "and introduce them to you."
  - source_tokens: `26: "소개 도", 27: "해드리고"`
  - mapping_reason: Action of introducing.
* target[13]: "Uh, could you explain"
  - source_tokens: `32: "어", 38: "해주시죠."`
  - mapping_reason: Request for explanation.
* target[14]: "what ' New York Minis '"
  - source_tokens: `33: "뉴욕", 34: "미니 스에", 35: "대한"`
  - mapping_reason: Topic of explanation.
* target[15]: "is?"
  - source_tokens: `36: "설명 을", 37: "좀"`
  - mapping_reason: Question marker/explanation noun.

result:
```html
0. <src>그리고 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>아 그리고 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>우리 가 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>뉴욕 에 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>살고 있으니까 좀 </src> <tgt>And, uh, since we live in New York,</tgt>; start=4.00, end=5.00
5. <src>뉴욕 과 뉴저지 지역 의 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>유명 한 곳을 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>소개 해드릴 수도 있어요. 그렇 죠, 그렇 죠. </src> <tgt>we could also introduce some famous spots in the New York and New Jersey area. Right, exactly.</tgt>; start=7.00, end=8.00
8. <src>직접 그 현장 에 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>가서 저희 들이 이제 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>체험 도 해보고 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>소개 도 해드리고 </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>그런 프로그램 도 </src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>만들 기획 이고요. 어 </src> <tgt>We're planning to make a program. We'll actually go to the sites, experience them ourselves, and introduce them to you.</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>뉴욕 미니 스에 대한 설명 을 </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>좀 해주시죠. </src> <tgt>Uh, could you explain what ' New York Minis ' is?</tgt>; start=17.00, end=17.74
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_E9GzA6TOlV4_W000007 ===

source:
- language: Korean
- transcription: 일단 배그는 파밍이 제일 중요합니다, 여러분. 파밍을 열심히 해주세요. 어 발소리 난다. 어 당황한 척하면서 이렇게 파밍해주면 됩니다, 여러분.
- source_tokens:
  0. 일단
  1. 배그는
  2. 파밍이
  3. 제일
  4. 중요 합니다,
  5. 여러분.
  6. 파밍을
  7. 열심히
  8. 해주세요.
  9. 어
  10. 발소리
  11. 난다.
  12. 어
  13. 당황 한
  14. 척하 면서
  15. 이렇게
  16. 파밍해주면
  17. 됩니다,
  18. 여러분.

target:
- language: Chinese
- translation: 首先，大家，在绝地求生里搜集物资最重要。请努力搜集物资。哦，有脚步声。哦，大家，装作很慌张的样子，像这样搜集物资就行了。
- target_sense_units:
  0. 首先，
  1. 大家，
  2. 在绝地求生里
  3. 搜集物资
  4. 最重要。
  5. 请
  6. 努力搜集物资。
  7. 哦，
  8. 有脚步声。
  9. 哦，
  10. 大家，
  11. 装作很慌张的样子，
  12. 像这样
  13. 搜集物资
  14. 就行了。

scratchpad:
* target[0]: "首先，"
  - source_tokens: `0: "일단"`
  - mapping_reason: "일단" functions as a discourse marker for "firstly".

* target[1]: "大家，"
  - source_tokens: `5: "여러분."`
  - mapping_reason: Direct address to the audience.

* target[2]: "在绝地求生里"
  - source_tokens: `1: "배그는"`
  - mapping_reason: "배그" (Battlegrounds) acts as the topic/context.

* target[3]: "搜集物资"
  - source_tokens: `2: "파밍이"`
  - mapping_reason: "파밍" (farming/looting) is translated as "搜集物资".

* target[4]: "最重要。"
  - source_tokens: `3: "제일", 4: "중요 합니다,"`
  - mapping_reason: "제일" (most) and "중요합니다" (important).

* target[5]: "请"
  - source_tokens: `8: "해주세요."`
  - mapping_reason: "해주세요" provides the polite request marker.

* target[6]: "努力搜集物资。"
  - source_tokens: `6: "파밍을", 7: "열심히", 8: "해주세요."`
  - mapping_reason: "파밍" (looting), "열심히" (diligently/hard), and the verb structure.

* target[7]: "哦，"
  - source_tokens: `9: "어"`
  - mapping_reason: Exclamation/filler.

* target[8]: "有脚步声。"
  - source_tokens: `10: "발소리", 11: "난다."`
  - mapping_reason: "발소리" (footsteps) + "난다" (appears/is heard).

* target[9]: "哦，"
  - source_tokens: `12: "어"`
  - mapping_reason: Exclamation/filler.

* target[10]: "大家，"
  - source_tokens: `18: "여러분."`
  - mapping_reason: Direct address to the audience.

* target[11]: "装作很慌张的样子，"
  - source_tokens: `13: "당황 한", 14: "척하 면서"`
  - mapping_reason: "당황한" (flustered/panicked) + "척하면서" (pretending to).

* target[12]: "像这样"
  - source_tokens: `15: "이렇게"`
  - mapping_reason: "이렇게" (like this).

* target[13]: "搜集物资"
  - source_tokens: `16: "파밍해주면"`
  - mapping_reason: "파밍" (looting).

* target[14]: "就行了。"
  - source_tokens: `16: "파밍해주면", 17: "됩니다,"`
  - mapping_reason: "해주면 됩니다" (if you do it, it will be fine/that's enough).

result:
```html
0. <src>일단 배그는 파밍이 </src> <tgt>首先，</tgt>; start=0.00, end=1.00
1. <src>제일 중요 합니다, </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>여러분. </src> <tgt>大家，在绝地求生里搜集物资最重要。</tgt>; start=2.00, end=3.00
3. <src>파밍을 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>열심히 해주세요. 어 </src> <tgt>请努力搜集物资。哦，</tgt>; start=4.00, end=5.00
5. <src>발소리 난다. </src> <tgt>有脚步声。</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>어 </src> <tgt>哦，</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>당황 한 척하 면서 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>이렇게 파밍해주면 됩니다, 여러분. </src> <tgt>大家，装作很慌张的样子，像这样搜集物资就行了。</tgt>; start=12.00, end=12.73
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G7RmVIWMrHo_W000018 ===

source:
- language: Korean
- transcription: 제가 좀 직관적으로 이해하셔야 될 부분의 측면이 있어서 여러분들이 잘 한번 보시고 아주 이렇게 하니까 행이 병합이 되는구나 이렇게 느끼셨으면 좋겠습니다. 말로 하려니까 너무 힘드네요. 자, 그다음 여기는 합계라고 되어 있는 부분은 여기 있는 이 각각의 칸 세 개의 칸을
- source_tokens:
  0. 제가
  1. 좀
  2. 직관적으로
  3. 이해 하셔야
  4. 될
  5. 부분 의
  6. 측면 이
  7. 있어서
  8. 여러분 들이
  9. 잘
  10. 한번
  11. 보시고
  12. 아주
  13. 이렇게
  14. 하니까
  15. 행이
  16. 병합이
  17. 되는구나
  18. 이렇게
  19. 느끼 셨으면
  20. 좋겠습니다.
  21. 말로
  22. 하려니까
  23. 너무
  24. 힘드 네요.
  25. 자,
  26. 그다음
  27. 여기 는
  28. 합계 라고
  29. 되어
  30. 있는
  31. 부분 은
  32. 여기
  33. 있는
  34. 이
  35. 각각 의
  36. 칸
  37. 세
  38. 개의
  39. 칸을

target:
- language: English
- translation: There's something here you need to understand intuitively. So I hope you take a good look and really feel, 'Oh, so this is how you merge rows.' It's so hard to explain this in words. Okay, next, the part labeled 'Total' is meant for these three individual cells...
- target_sense_units:
  0. There's something here
  1. you need to understand intuitively.
  2. So I hope
  3. you take a good look
  4. and really feel,
  5. ' Oh, so this is
  6. how you merge rows.
  7. ' It's so hard
  8. to explain this in words.
  9. Okay, next, the part
  10. labeled ' Total '
  11. is meant for
  12. these three individual cells...

scratchpad:
* target[0]: "There's something here"
  - source_tokens: `0: "제가", 5: "부분 의", 6: "측면 이", 7: "있어서"`
  - mapping_reason: "제가" (I/subject), "부분의 측면이 있어서" (there is an aspect/part).
* target[1]: "you need to understand intuitively."
  - source_tokens: `2: "직관적으로", 3: "이해 하셔야", 4: "될"`
  - mapping_reason: "직관적으로" (intuitively), "이해하셔야 될" (need to understand).
* target[2]: "So I hope"
  - source_tokens: `19: "느끼 셨으면", 20: "좋겠습니다."`
  - mapping_reason: "느끼셨으면 좋겠습니다" (I hope you feel/experience).
* target[3]: "you take a good look"
  - source_tokens: `8: "여러분 들이", 9: "잘", 10: "한번", 11: "보시고"`
  - mapping_reason: "여러분들이" (you), "잘 한번 보시고" (take a good look).
* target[4]: "and really feel,"
  - source_tokens: `12: "아주", 19: "느끼 셨으면"`
  - mapping_reason: "아주" (really/very), "느끼셨으면" (feel).
* target[5]: "' Oh, so this is"
  - source_tokens: `13: "이렇게", 14: "하니까"`
  - mapping_reason: "이렇게 하니까" (doing this way/so this is).
* target[6]: "how you merge rows."
  - source_tokens: `15: "행이", 16: "병합이", 17: "되는구나"`
  - mapping_reason: "행이 병합이 되는구나" (rows are merged).
* target[7]: "' It's so hard"
  - source_tokens: `23: "너무", 24: "힘드 네요."`
  - mapping_reason: "너무 힘드네요" (It's so hard).
* target[8]: "to explain this in words."
  - source_tokens: `21: "말로", 22: "하려니까"`
  - mapping_reason: "말로 하려니까" (trying to do it with words/explain).
* target[9]: "Okay, next, the part"
  - source_tokens: `25: "자,", 26: "그다음", 31: "부분 은"`
  - mapping_reason: "자, 그다음" (Okay, next), "부분은" (the part).
* target[10]: "labeled ' Total '"
  - source_tokens: `28: "합계 라고", 29: "되어", 30: "있는"`
  - mapping_reason: "합계라고 되어 있는" (labeled as Total).
* target[11]: "is meant for"
  - source_tokens: `27: "여기 는"`
  - mapping_reason: "여기는" (this part is for/is meant for).
* target[12]: "these three individual cells..."
  - source_tokens: `32: "여기", 33: "있는", 34: "이", 35: "각각 의", 36: "칸", 37: "세", 38: "개의", 39: "칸을"`
  - mapping_reason: "여기 있는 이 각각의 칸 세 개의 칸을" (these three individual cells).

result:
```html
0. <src>제가 좀 직관적으로 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>이해 하셔야 될 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>부분 의 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>측면 이 있어서 </src> <tgt>There's something here you need to understand intuitively.</tgt>; start=3.00, end=4.00
4. <src>여러분 들이 잘 한번 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>보시고 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>아주 이렇게 하니까 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>행이 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>병합이 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>되는구나 이렇게 느끼 셨으면 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>좋겠습니다. 말로 </src> <tgt>So I hope you take a good look and really feel, ' Oh, so this is how you merge rows.</tgt>; start=10.00, end=11.00
11. <src>하려니까 너무 힘드 네요. </src> <tgt>' It's so hard to explain this in words.</tgt>; start=11.00, end=12.00
12. <src>자, </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>그다음 여기 는 </src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>합계 라고 되어 있는 부분 은 </src> <tgt>Okay, next, the part labeled ' Total ' is meant for</tgt>; start=14.00, end=15.00
15. <src>여기 있는 이 </src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>각각 의 </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>칸 세 개의 </src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>칸을 </src> <tgt>these three individual cells...</tgt>; start=18.00, end=18.40
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G1hDgTWHSC8_W000038 ===

source:
- language: Korean
- transcription: 자기 그림을 그리면서 카피할 때 머리 속에 기억해두고 메모해둔 표현 방법을 그대로 실제 적용하면서 그림을 그립니다. 그러면 그림 그리는 실력이 빠르게 좋아집니다.
- source_tokens:
  0. 자기
  1. 그림 을
  2. 그리 면서
  3. 카피할
  4. 때
  5. 머리
  6. 속에
  7. 기억 해두고
  8. 메모 해둔
  9. 표현
  10. 방법 을
  11. 그대로
  12. 실제
  13. 적용 하면서
  14. 그림 을
  15. 그립 니다.
  16. 그러면
  17. 그림
  18. 그리 는
  19. 실력 이
  20. 빠르 게
  21. 좋아집니다.

target:
- language: Chinese
- translation: 画自己的画、做临摹的时候，会把脑子里记住和记下来的表现手法直接用到实际画中。这样画画的水平就会提高得很快。
- target_sense_units:
  0. 画自己的画、
  1. 做临摹的时候，
  2. 会把
  3. 脑子里
  4. 记住和记下来
  5. 的表现手法
  6. 直接用到
  7. 实际画中。
  8. 这样
  9. 画画的水平
  10. 就会提高
  11. 得很快。

scratchpad:
* target[0]: "画自己的画、"
  - source_tokens: `0: "자기", 1: "그림 을", 2: "그리 면서"`
  - mapping_reason: "자기" (own), "그림" (picture/drawing), "그리다" (to draw)

* target[1]: "做临摹的时候，"
  - source_tokens: `3: "카피할", 4: "때"`
  - mapping_reason: "카피" (copy/imitate), "때" (when/time)

* target[2]: "会把"
  - source_tokens: `13: "적용 하면서"`
  - mapping_reason: Indicates the action of applying/using (instrumental case structure)

* target[3]: "脑子里"
  - source_tokens: `5: "머리", 6: "속에"`
  - mapping_reason: "머리 속" (inside the head/mind)

* target[4]: "记住和记下来"
  - source_tokens: `7: "기억 해두고", 8: "메모 해둔"`
  - mapping_reason: "기억하다" (remember), "메모하다" (note down)

* target[5]: "的表现手法"
  - source_tokens: `9: "표현", 10: "방법 을"`
  - mapping_reason: "표현 방법" (expression method/technique)

* target[6]: "直接用到"
  - source_tokens: `11: "그대로", 12: "실제", 13: "적용 하면서"`
  - mapping_reason: "그대로" (as it is/directly), "실제 적용" (actual application)

* target[7]: "实际画中。"
  - source_tokens: `14: "그림 을", 15: "그립 니다."`
  - mapping_reason: "그림" (picture/drawing), context of drawing action

* target[8]: "这样"
  - source_tokens: `16: "그러면"`
  - mapping_reason: "그러면" (then/in that case/thus)

* target[9]: "画画的水平"
  - source_tokens: `17: "그림", 18: "그리 는", 19: "실력 이"`
  - mapping_reason: "그림 그리는 실력" (drawing skill)

* target[10]: "就会提高"
  - source_tokens: `21: "좋아집니다."`
  - mapping_reason: "좋아지다" (improve/get better)

* target[11]: "得很快。"
  - source_tokens: `20: "빠르 게"`
  - mapping_reason: "빠르게" (quickly)

result:
```html
0. <src>자기 그림 을 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>그리 면서 카피할 때 </src> <tgt>画自己的画、做临摹的时候，</tgt>; start=1.00, end=2.00
2. <src>머리 속에 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>기억 해두고 메모 해둔 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>표현 방법 을 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>그대로 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>실제 적용 하면서 </src> <tgt>会把脑子里记住和记下来的表现手法直接用到</tgt>; start=6.00, end=7.00
7. <src>그림 을 그립 니다. </src> <tgt>实际画中。</tgt>; start=7.00, end=8.00
8. <src>그러면 </src> <tgt>这样</tgt>; start=8.00, end=9.00
9. <src>그림 그리 는 실력 이 </src> <tgt>画画的水平</tgt>; start=9.00, end=10.00
10. <src>빠르 게 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>좋아집니다. </src> <tgt>就会提高得很快。</tgt>; start=11.00, end=11.14
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G7RmVIWMrHo_W000018 ===

source:
- language: Korean
- transcription: 제가 좀 직관적으로 이해하셔야 될 부분의 측면이 있어서 여러분들이 잘 한번 보시고 아주 이렇게 하니까 행이 병합이 되는구나 이렇게 느끼셨으면 좋겠습니다. 말로 하려니까 너무 힘드네요. 자, 그다음 여기는 합계라고 되어 있는 부분은 여기 있는 이 각각의 칸 세 개의 칸을
- source_tokens:
  0. 제가
  1. 좀
  2. 직관적으로
  3. 이해 하셔야
  4. 될
  5. 부분 의
  6. 측면 이
  7. 있어서
  8. 여러분 들이
  9. 잘
  10. 한번
  11. 보시고
  12. 아주
  13. 이렇게
  14. 하니까
  15. 행이
  16. 병합이
  17. 되는구나
  18. 이렇게
  19. 느끼 셨으면
  20. 좋겠습니다.
  21. 말로
  22. 하려니까
  23. 너무
  24. 힘드 네요.
  25. 자,
  26. 그다음
  27. 여기 는
  28. 합계 라고
  29. 되어
  30. 있는
  31. 부분 은
  32. 여기
  33. 있는
  34. 이
  35. 각각 의
  36. 칸
  37. 세
  38. 개의
  39. 칸을

target:
- language: Chinese
- translation: 这部分需要大家直观地理解。希望大家仔细看看，感受一下“原来这样行就会合并啊”。光靠说真的太难了。好，接下来，这里写着“合计”的部分，是将这里的每一个格子，也就是这三个格子……
- target_sense_units:
  0. 这部分需要
  1. 大家直观地理解。
  2. 希望大家
  3. 仔细看看，
  4. 感受一下
  5. “原来这样
  6. 行就会合并啊”。
  7. 光靠说
  8. 真的太难了。
  9. 好，
  10. 接下来，
  11. 这里写着
  12. “合计”的部分，
  13. 是将
  14. 这里的
  15. 每一个格子，
  16. 也就是
  17. 这三个格子……

scratchpad:
* target[0]: "这部分需要"
  - source_tokens: `5: "부분 의", 3: "이해 하셔야", 4: "될"`
  - mapping_reason: "부분의" (this part) and "이해하셔야 될" (need to understand) combine to form the requirement of this section.
* target[1]: "大家直观地理解。"
  - source_tokens: `8: "여러분 들이", 2: "직관적으로", 3: "이해 하셔야"`
  - mapping_reason: "여러분들이" (everyone/you all), "직관적으로" (intuitively), "이해하셔야" (understand).
* target[2]: "希望大家"
  - source_tokens: `8: "여러분 들이", 20: "좋겠습니다."`
  - mapping_reason: "여러분들이" (you all) and the wish expressed by "좋겠습니다".
* target[3]: "仔细看看，"
  - source_tokens: `9: "잘", 10: "한번", 11: "보시고"`
  - mapping_reason: "잘" (carefully), "한번 보시고" (take a look).
* target[4]: "感受一下"
  - source_tokens: `19: "느끼 셨으면"`
  - mapping_reason: "느끼셨으면" (if you feel/experience).
* target[5]: "“原来这样"
  - source_tokens: `13: "이렇게", 14: "하니까"`
  - mapping_reason: "이렇게 하니까" (because it's done like this).
* target[6]: "行就会合并啊”。"
  - source_tokens: `15: "행이", 16: "병합이", 17: "되는구나"`
  - mapping_reason: "행이 병합이 되는구나" (the row is merged).
* target[7]: "光靠说"
  - source_tokens: `21: "말로", 22: "하려니까"`
  - mapping_reason: "말로 하려니까" (trying to do it with words).
* target[8]: "真的太难了。"
  - source_tokens: `23: "너무", 24: "힘드 네요."`
  - mapping_reason: "너무 힘드네요" (it is too hard).
* target[9]: "好，"
  - source_tokens: `25: "자,"`
  - mapping_reason: "자" (discourse marker 'well/okay').
* target[10]: "接下来，"
  - source_tokens: `26: "그다음"`
  - mapping_reason: "그다음" (next).
* target[11]: "这里写着"
  - source_tokens: `27: "여기 는", 29: "되어", 30: "있는"`
  - mapping_reason: "여기는 ... 되어 있는" (what is here/written here).
* target[12]: "“合计”的部分，"
  - source_tokens: `28: "합계 라고", 31: "부분 은"`
  - mapping_reason: "합계라고" (called total) and "부분은" (the part).
* target[13]: "是将"
  - source_tokens: `32: "여기", 33: "있는"`
  - mapping_reason: "여기 있는" (the ones here - context for the action).
* target[14]: "这里的"
  - source_tokens: `32: "여기", 34: "이"`
  - mapping_reason: "여기 이" (this here).
* target[15]: "每一个格子，"
  - source_tokens: `35: "각각 의", 36: "칸"`
  - mapping_reason: "각각의 칸" (each cell/grid).
* target[16]: "也就是"
  - source_tokens: `37: "세"`
  - mapping_reason: "세" (three, identifying the specific count).
* target[17]: "这三个格子……"
  - source_tokens: `38: "개의", 39: "칸을"`
  - mapping_reason: "개의 칸을" (the cells).

result:
```html
0. <src>제가 좀 직관적으로 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>이해 하셔야 될 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>부분 의 </src> <tgt>这部分需要</tgt>; start=2.00, end=3.00
3. <src>측면 이 있어서 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>여러분 들이 잘 한번 </src> <tgt>大家直观地理解。</tgt>; start=4.00, end=5.00
5. <src>보시고 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>아주 이렇게 하니까 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>행이 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>병합이 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>되는구나 이렇게 느끼 셨으면 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>좋겠습니다. 말로 </src> <tgt>希望大家仔细看看，感受一下“原来这样行就会合并啊”。</tgt>; start=10.00, end=11.00
11. <src>하려니까 너무 힘드 네요. </src> <tgt>光靠说真的太难了。</tgt>; start=11.00, end=12.00
12. <src>자, </src> <tgt>好，</tgt>; start=12.00, end=13.00
13. <src>그다음 여기 는 </src> <tgt>接下来，</tgt>; start=13.00, end=14.00
14. <src>합계 라고 되어 있는 부분 은 </src> <tgt>这里写着“合计”的部分，</tgt>; start=14.00, end=15.00
15. <src>여기 있는 이 </src> <tgt>是将这里的</tgt>; start=15.00, end=16.00
16. <src>각각 의 </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>칸 세 개의 </src> <tgt>每一个格子，也就是</tgt>; start=17.00, end=18.00
18. <src>칸을 </src> <tgt>这三个格子……</tgt>; start=18.00, end=18.40
```

- max_empty_window_count: 5


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G1hDgTWHSC8_W000002 ===

source:
- language: Korean
- transcription: 유튜브에 그림을 올리는 고수들이나 거리에서 그림을 그리는 사람들을 보면 별로 힘들이지 않고 대충 그려도 보기 좋게 완성되는 것 같은데 나는 언제 좀 저렇게 그림을 그릴 수 있을까 하는 생각을 하게 됩니다.
- source_tokens:
  0. 유튜브 에
  1. 그림 을
  2. 올리 는
  3. 고수 들이나
  4. 거리 에서
  5. 그림 을
  6. 그리 는
  7. 사람 들을
  8. 보면
  9. 별로
  10. 힘들 이지
  11. 않고
  12. 대충
  13. 그려 도
  14. 보기
  15. 좋게
  16. 완성 되는
  17. 것
  18. 같은데
  19. 나는
  20. 언제
  21. 좀
  22. 저렇게
  23. 그림 을
  24. 그릴
  25. 수
  26. 있을까
  27. 하는
  28. 생각 을
  29. 하게
  30. 됩니다.

target:
- language: English
- translation: When I see the pros on YouTube or people drawing on the street, it seems like they don't even try that hard – even a rough sketch turns out looking great. Then I find myself wondering when I'll ever be able to draw like that.
- target_sense_units:
  0. When I see
  1. the pros
  2. on YouTube
  3. or people
  4. drawing on the street,
  5. it seems like
  6. they don't even try
  7. that hard–
  8. even a rough sketch
  9. turns out
  10. looking great.
  11. Then I
  12. find myself
  13. wondering when
  14. I'll ever
  15. be able to
  16. draw like that.

scratchpad:
* target[0]: "When I see"
  - source_tokens: `8: "보면"`
  - mapping_reason: The verb '보면' provides the temporal/conditional 'When I see' context.
* target[1]: "the pros"
  - source_tokens: `3: "고수 들이나"`
  - mapping_reason: '고수' translates to 'pros'.
* target[2]: "on YouTube"
  - source_tokens: `0: "유튜브 에"`
  - mapping_reason: '유튜브' is YouTube.
* target[3]: "or people"
  - source_tokens: `3: "고수 들이나", 7: "사람 들을"`
  - mapping_reason: '이나' (or) and '사람들' (people).
* target[4]: "drawing on the street,"
  - source_tokens: `4: "거리 에서", 5: "그림 을", 6: "그리 는"`
  - mapping_reason: '거리에서' (on the street) + '그림을 그리는' (drawing).
* target[5]: "it seems like"
  - source_tokens: `17: "것", 18: "같은데"`
  - mapping_reason: '것 같은데' expresses the appearance/seeming.
* target[6]: "they don't even try"
  - source_tokens: `9: "별로", 10: "힘들 이지", 11: "않고"`
  - mapping_reason: '별로 힘들이지 않고' (don't try hard).
* target[7]: "that hard–"
  - source_tokens: `9: "별로", 10: "힘들 이지"`
  - mapping_reason: Reinforces the 'hard' aspect of the effort.
* target[8]: "even a rough sketch"
  - source_tokens: `12: "대충", 13: "그려 도"`
  - mapping_reason: '대충 그려도' (even if drawn roughly).
* target[9]: "turns out"
  - source_tokens: `16: "완성 되는"`
  - mapping_reason: '완성되는' (becoming finished/turning out).
* target[10]: "looking great."
  - source_tokens: `14: "보기", 15: "좋게"`
  - mapping_reason: '보기 좋게' (looking great).
* target[11]: "Then I"
  - source_tokens: `19: "나는"`
  - mapping_reason: '나는' (I).
* target[12]: "find myself"
  - source_tokens: `29: "하게", 30: "됩니다."`
  - mapping_reason: '하게 됩니다' (end up doing/find myself).
* target[13]: "wondering when"
  - source_tokens: `20: "언제", 27: "하는", 28: "생각 을"`
  - mapping_reason: '언제... 하는 생각을' (wondering when).
* target[14]: "I'll ever"
  - source_tokens: `21: "좀"`
  - mapping_reason: '좀' functions as an intensifier for 'ever'.
* target[15]: "be able to"
  - source_tokens: `25: "수", 26: "있을까"`
  - mapping_reason: '수 있을까' (be able to).
* target[16]: "draw like that."
  - source_tokens: `22: "저렇게", 23: "그림 을", 24: "그릴"`
  - mapping_reason: '저렇게 그림을 그릴' (draw like that).

result:
```html
0. <src>유튜브 에 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>그림 을 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>올리 는 고수 들이나 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>거리 에서 그림 을 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>그리 는 사람 들을 보면 </src> <tgt>When I see the pros on YouTube or people drawing on the street,</tgt>; start=4.00, end=5.00
5. <src>별로 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>힘들 이지 않고 대충 그려 도 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>보기 좋게 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>완성 되는 것 같은데 </src> <tgt>it seems like they don't even try that hard– even a rough sketch turns out looking great.</tgt>; start=8.00, end=9.00
9. <src>나는 </src> <tgt>Then I</tgt>; start=9.00, end=10.00
10. <src>언제 좀 저렇게 그림 을 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>그릴 수 있을까 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>하는 생각 을 </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>하게 됩니다. </src> <tgt>find myself wondering when I'll ever be able to draw like that.</tgt>; start=13.00, end=13.24
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G7RmVIWMrHo_W000018 ===

source:
- language: Korean
- transcription: 제가 좀 직관적으로 이해하셔야 될 부분의 측면이 있어서 여러분들이 잘 한번 보시고 아주 이렇게 하니까 행이 병합이 되는구나 이렇게 느끼셨으면 좋겠습니다. 말로 하려니까 너무 힘드네요. 자, 그다음 여기는 합계라고 되어 있는 부분은 여기 있는 이 각각의 칸 세 개의 칸을
- source_tokens:
  0. 제가
  1. 좀
  2. 직관적으로
  3. 이해 하셔야
  4. 될
  5. 부분 의
  6. 측면 이
  7. 있어서
  8. 여러분 들이
  9. 잘
  10. 한번
  11. 보시고
  12. 아주
  13. 이렇게
  14. 하니까
  15. 행이
  16. 병합이
  17. 되는구나
  18. 이렇게
  19. 느끼 셨으면
  20. 좋겠습니다.
  21. 말로
  22. 하려니까
  23. 너무
  24. 힘드 네요.
  25. 자,
  26. 그다음
  27. 여기 는
  28. 합계 라고
  29. 되어
  30. 있는
  31. 부분 은
  32. 여기
  33. 있는
  34. 이
  35. 각각 의
  36. 칸
  37. 세
  38. 개의
  39. 칸을

target:
- language: Japanese
- translation: 直感的に理解していただきたい点がありまして、皆さんよく見て、「こうやると行が結合されるんだな」と感じていただければと思います。言葉で説明するのは本当に難しいですね。さて、次は「合計」と書かれている部分ですが、ここにあるそれぞれのマス、この3つのマスを……
- target_sense_units:
  0. 直感的に
  1. 理解していただきたい
  2. 点が
  3. ありまして、
  4. 皆さん
  5. よく
  6. 見て、
  7. 「こうやると
  8. 行が
  9. 結合されるんだな」
  10. と
  11. 感じていただければ
  12. と思います。
  13. 言葉で
  14. 説明する
  15. のは
  16. 本当に
  17. 難しい
  18. ですね。
  19. さて、
  20. 次は
  21. 「合計」と
  22. 書かれている
  23. 部分
  24. ですが、
  25. ここに
  26. ある
  27. それぞれのマス、
  28. この3つのマス
  29. を……

scratchpad:
* target[0]: "直感的に"
  - source_tokens: `2: "직관적으로"`
  - mapping_reason: Direct adverbial translation.
* target[1]: "理解していただきたい"
  - source_tokens: `3: "이해 하셔야"`
  - mapping_reason: Verb phrase expressing request for understanding.
* target[2]: "点が"
  - source_tokens: `5: "부분 의"`
  - mapping_reason: "부분" (part/point) maps to "点".
* target[3]: "ありまして、"
  - source_tokens: `6: "측면 이", 7: "있어서"`
  - mapping_reason: "측면이 있어서" (there is an aspect) functions as the reason/preamble.
* target[4]: "皆さん"
  - source_tokens: `8: "여러분 들이"`
  - mapping_reason: Direct address.
* target[5]: "よく"
  - source_tokens: `9: "잘"`
  - mapping_reason: Adverbial modifier.
* target[6]: "見て、"
  - source_tokens: `10: "한번", 11: "보시고"`
  - mapping_reason: "보시고" (look at) + "한번" (once).
* target[7]: "「こうやると"
  - source_tokens: `12: "아주", 13: "이렇게", 14: "하니까"`
  - mapping_reason: "이렇게 하니까" (because doing it this way) corresponds to "こうやると".
* target[8]: "行が"
  - source_tokens: `15: "행이"`
  - mapping_reason: Direct noun translation.
* target[9]: "結合されるんだな」"
  - source_tokens: `16: "병합이", 17: "되는구나"`
  - mapping_reason: "병합이 되는구나" (it merges) corresponds to "結合されるんだな".
* target[10]: "と"
  - source_tokens: `18: "이렇게"`
  - mapping_reason: Quotative marker for the preceding thought.
* target[11]: "感じていただければ"
  - source_tokens: `19: "느끼 셨으면"`
  - mapping_reason: Verb phrase for feeling/realizing.
* target[12]: "と思います。"
  - source_tokens: `20: "좋겠습니다."`
  - mapping_reason: Polite expression of hope/wish.
* target[13]: "言葉で"
  - source_tokens: `21: "말로"`
  - mapping_reason: Direct noun translation.
* target[14]: "説明する"
  - source_tokens: `22: "하려니까"`
  - mapping_reason: "하려니까" (trying to do [by speaking]) implies explaining.
* target[15]: "のは"
  - source_tokens: `22: "하려니까"`
  - mapping_reason: Nominalizer for the action of speaking/explaining.
* target[16]: "本当に"
  - source_tokens: `23: "너무"`
  - mapping_reason: Adverbial intensifier.
* target[17]: "難しい"
  - source_tokens: `24: "힘드 네요."`
  - mapping_reason: "힘드네요" (is difficult/hard).
* target[18]: "ですね。"
  - source_tokens: `24: "힘드 네요."`
  - mapping_reason: Sentence ending particle for agreement.
* target[19]: "さて、"
  - source_tokens: `25: "자,"`
  - mapping_reason: Discourse marker.
* target[20]: "次は"
  - source_tokens: `26: "그다음"`
  - mapping_reason: Sequential marker.
* target[21]: "「合計」と"
  - source_tokens: `28: "합계 라고"`
  - mapping_reason: Direct noun translation + quotative marker.
* target[22]: "書かれている"
  - source_tokens: `29: "되어", 30: "있는"`
  - mapping_reason: "되어 있는" (is written/exists as).
* target[23]: "部分"
  - source_tokens: `31: "부분 은"`
  - mapping_reason: Direct noun translation.
* target[24]: "ですが、"
  - source_tokens: `27: "여기 는"`
  - mapping_reason: Topic marker and transition.
* target[25]: "ここに"
  - source_tokens: `32: "여기"`
  - mapping_reason: Locative.
* target[26]: "ある"
  - source_tokens: `33: "있는"`
  - mapping_reason: Existential verb.
* target[27]: "それぞれのマス、"
  - source_tokens: `34: "이", 35: "각각 의", 36: "칸"`
  - mapping_reason: "각각의 칸" (each cell).
* target[28]: "この3つのマス"
  - source_tokens: `37: "세", 38: "개의", 39: "칸을"`
  - mapping_reason: "세 개의 칸" (three cells).
* target[29]: "を……"
  - source_tokens: `39: "칸을"`
  - mapping_reason: Object marker.

result:
```html
0. <src>제가 좀 직관적으로 </src> <tgt>直感的に</tgt>; start=0.00, end=1.00
1. <src>이해 하셔야 될 </src> <tgt>理解していただきたい</tgt>; start=1.00, end=2.00
2. <src>부분 의 </src> <tgt>点が</tgt>; start=2.00, end=3.00
3. <src>측면 이 있어서 </src> <tgt>ありまして、</tgt>; start=3.00, end=4.00
4. <src>여러분 들이 잘 한번 </src> <tgt>皆さんよく</tgt>; start=4.00, end=5.00
5. <src>보시고 </src> <tgt>見て、</tgt>; start=5.00, end=6.00
6. <src>아주 이렇게 하니까 </src> <tgt>「こうやると</tgt>; start=6.00, end=7.00
7. <src>행이 </src> <tgt>行が</tgt>; start=7.00, end=8.00
8. <src>병합이 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>되는구나 이렇게 느끼 셨으면 </src> <tgt>結合されるんだな」と感じていただければ</tgt>; start=9.00, end=10.00
10. <src>좋겠습니다. 말로 </src> <tgt>と思います。言葉で</tgt>; start=10.00, end=11.00
11. <src>하려니까 너무 힘드 네요. </src> <tgt>説明するのは本当に難しいですね。</tgt>; start=11.00, end=12.00
12. <src>자, </src> <tgt>さて、</tgt>; start=12.00, end=13.00
13. <src>그다음 여기 는 </src> <tgt>次は</tgt>; start=13.00, end=14.00
14. <src>합계 라고 되어 있는 부분 은 </src> <tgt>「合計」と書かれている部分ですが、</tgt>; start=14.00, end=15.00
15. <src>여기 있는 이 </src> <tgt>ここにある</tgt>; start=15.00, end=16.00
16. <src>각각 의 </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>칸 세 개의 </src> <tgt>それぞれのマス、</tgt>; start=17.00, end=18.00
18. <src>칸을 </src> <tgt>この3つのマスを……</tgt>; start=18.00, end=18.40
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G3A_RG4qGF4_W000002 ===

source:
- language: Korean
- transcription: 그리고 아 그리고 우리가 뉴욕에 살고 있으니까 좀 뉴욕과 뉴저지 지역의 유명한 곳을 소개해드릴 수도 있어요. 그렇죠, 그렇죠. 직접 그 현장에 가서 저희들이 이제 체험도 해보고 소개도 해드리고 그런 프로그램도 만들 기획이고요. 어 뉴욕 미니스에 대한 설명을 좀 해주시죠.
- source_tokens:
  0. 그리고
  1. 아
  2. 그리고
  3. 우리 가
  4. 뉴욕 에
  5. 살고
  6. 있으니까
  7. 좀
  8. 뉴욕 과
  9. 뉴저지
  10. 지역 의
  11. 유명 한
  12. 곳을
  13. 소개 해드릴
  14. 수도
  15. 있어요.
  16. 그렇 죠,
  17. 그렇 죠.
  18. 직접
  19. 그
  20. 현장 에
  21. 가서
  22. 저희 들이
  23. 이제
  24. 체험 도
  25. 해보고
  26. 소개 도
  27. 해드리고
  28. 그런
  29. 프로그램 도
  30. 만들
  31. 기획 이고요.
  32. 어
  33. 뉴욕
  34. 미니 스에
  35. 대한
  36. 설명 을
  37. 좀
  38. 해주시죠.

target:
- language: Chinese
- translation: 而且，因为我们住在纽约嘛，所以也可以给大家介绍一些纽约和新泽西有名的景点。对，没错。我们还打算做一些节目，亲自去现场体验，然后给大家介绍。呃，那请介绍一下“纽约迷你”吧。
- target_sense_units:
  0. 而且，
  1. 因为
  2. 我们住在纽约嘛，
  3. 所以
  4. 也可以
  5. 给大家介绍
  6. 一些纽约和新泽西
  7. 有名的景点。
  8. 对，
  9. 没错。
  10. 我们还打算
  11. 做一些节目，
  12. 亲自去现场体验，
  13. 然后
  14. 给大家介绍。
  15. 呃，
  16. 那
  17. 请介绍一下
  18. “纽约迷你”吧。

scratchpad:
* target[0]: "而且，"
  - source_tokens: `0: "그리고"`
  - mapping_reason: Discourse connective "그리고" maps to "而且".

* target[1]: "因为"
  - source_tokens: `6: "있으니까"`
  - mapping_reason: Causal suffix "-니까" maps to "因为".

* target[2]: "我们住在纽约嘛，"
  - source_tokens: `3: "우리 가", 4: "뉴욕 에", 5: "살고"`
  - mapping_reason: Subject "우리", location "뉴욕", and verb "살고" map to "我们住在纽约".

* target[3]: "所以"
  - source_tokens: `6: "있으니까"`
  - mapping_reason: Causal structure implies "所以".

* target[4]: "也可以"
  - source_tokens: `7: "좀", 14: "수도", 15: "있어요."`
  - mapping_reason: Potential form "-수도 있어요" maps to "也可以".

* target[5]: "给大家介绍"
  - source_tokens: `13: "소개 해드릴"`
  - mapping_reason: "소개 해드릴" maps to "介绍".

* target[6]: "一些纽约和新泽西"
  - source_tokens: `8: "뉴욕 과", 9: "뉴저지"`
  - mapping_reason: "뉴욕 과 뉴저지" maps to "纽约和新泽西".

* target[7]: "有名的景点。"
  - source_tokens: `10: "지역 의", 11: "유명 한", 12: "곳을"`
  - mapping_reason: "유명 한 곳" maps to "有名的景点".

* target[8]: "对，"
  - source_tokens: `16: "그렇 죠,"`
  - mapping_reason: Agreement expression.

* target[9]: "没错。"
  - source_tokens: `17: "그렇 죠."`
  - mapping_reason: Agreement expression.

* target[10]: "我们还打算"
  - source_tokens: `22: "저희 들이", 30: "만들", 31: "기획 이고요."`
  - mapping_reason: "저희" (we) and "기획 이고요" (planning/intend) map to "我们打算".

* target[11]: "做一些节目，"
  - source_tokens: `28: "그런", 29: "프로그램 도"`
  - mapping_reason: "프로그램" maps to "节目".

* target[12]: "亲自去现场体验，"
  - source_tokens: `18: "직접", 20: "현장 에", 21: "가서", 24: "체험 도", 25: "해보고"`
  - mapping_reason: "직접", "현장", "가서", "체험", "해보고" map to "亲自去现场体验".

* target[13]: "然后"
  - source_tokens: `23: "이제"`
  - mapping_reason: Sequential marker.

* target[14]: "给大家介绍。"
  - source_tokens: `26: "소개 도", 27: "해드리고"`
  - mapping_reason: "소개 해드리고" maps to "给大家介绍".

* target[15]: "呃，"
  - source_tokens: `32: "어"`
  - mapping_reason: Filler.

* target[16]: "那"
  - source_tokens: `32: "어"`
  - mapping_reason: Discourse flow.

* target[17]: "请介绍一下"
  - source_tokens: `36: "설명 을", 38: "해주시죠."`
  - mapping_reason: "설명 을 해주시죠" maps to "请介绍一下".

* target[18]: "“纽约迷你”吧。"
  - source_tokens: `33: "뉴욕", 34: "미니 스에"`
  - mapping_reason: "뉴욕 미니스" maps to "纽约迷你".

result:
```html
0. <src>그리고 </src> <tgt>而且，</tgt>; start=0.00, end=1.00
1. <src>아 그리고 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>우리 가 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>뉴욕 에 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>살고 있으니까 좀 </src> <tgt>因为我们住在纽约嘛，所以</tgt>; start=4.00, end=5.00
5. <src>뉴욕 과 뉴저지 지역 의 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>유명 한 곳을 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>소개 해드릴 수도 있어요. 그렇 죠, 그렇 죠. </src> <tgt>也可以给大家介绍一些纽约和新泽西有名的景点。对，没错。</tgt>; start=7.00, end=8.00
8. <src>직접 그 현장 에 </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>가서 저희 들이 이제 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>체험 도 해보고 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>소개 도 해드리고 </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>그런 프로그램 도 </src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>만들 기획 이고요. 어 </src> <tgt>我们还打算做一些节目，亲自去现场体验，然后给大家介绍。呃，那</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>뉴욕 미니 스에 대한 설명 을 </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>좀 해주시죠. </src> <tgt>请介绍一下“纽约迷你”吧。</tgt>; start=17.00, end=17.74
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G1hDgTWHSC8_W000002 ===

source:
- language: Korean
- transcription: 유튜브에 그림을 올리는 고수들이나 거리에서 그림을 그리는 사람들을 보면 별로 힘들이지 않고 대충 그려도 보기 좋게 완성되는 것 같은데 나는 언제 좀 저렇게 그림을 그릴 수 있을까 하는 생각을 하게 됩니다.
- source_tokens:
  0. 유튜브 에
  1. 그림 을
  2. 올리 는
  3. 고수 들이나
  4. 거리 에서
  5. 그림 을
  6. 그리 는
  7. 사람 들을
  8. 보면
  9. 별로
  10. 힘들 이지
  11. 않고
  12. 대충
  13. 그려 도
  14. 보기
  15. 좋게
  16. 완성 되는
  17. 것
  18. 같은데
  19. 나는
  20. 언제
  21. 좀
  22. 저렇게
  23. 그림 을
  24. 그릴
  25. 수
  26. 있을까
  27. 하는
  28. 생각 을
  29. 하게
  30. 됩니다.

target:
- language: Japanese
- translation: YouTubeに絵を上げてる達人とか、街で絵を描いてる人を見ると、あまり力入れずにざっと描いてるように見えるけど、それでも見栄えよく仕上がってるんですよね。で、自分はいつになったらあんなふうに描けるようになるんだろう、って思っちゃいます。
- target_sense_units:
  0. YouTubeに
  1. 絵を
  2. 上げてる
  3. 達人とか、
  4. 街で
  5. 絵を
  6. 描いてる
  7. 人を
  8. 見ると、
  9. あまり
  10. 力入れずに
  11. ざっと描いてる
  12. ように見える
  13. けど、
  14. それでも
  15. 見栄えよく
  16. 仕上がってるんですよね。
  17. で、
  18. 自分は
  19. いつになったら
  20. あんなふうに
  21. 描けるようになるんだろう、
  22. って思っちゃいます。

scratchpad:
* target[0]: "YouTubeに"
  - source_tokens: `0: "유튜브 에"`
  - mapping_reason: Direct translation of platform name and location particle.
* target[1]: "絵を"
  - source_tokens: `1: "그림 을"`
  - mapping_reason: Object of the action.
* target[2]: "上げてる"
  - source_tokens: `2: "올리 는"`
  - mapping_reason: Verbal action of uploading.
* target[3]: "達人とか、"
  - source_tokens: `3: "고수 들이나"`
  - mapping_reason: Subject/agent (expert) and connective particle.
* target[4]: "街で"
  - source_tokens: `4: "거리 에서"`
  - mapping_reason: Location of the action.
* target[5]: "絵を"
  - source_tokens: `5: "그림 을"`
  - mapping_reason: Object of the action.
* target[6]: "描いてる"
  - source_tokens: `6: "그리 는"`
  - mapping_reason: Verbal action of drawing.
* target[7]: "人を"
  - source_tokens: `7: "사람 들을"`
  - mapping_reason: Object (people) of the observation.
* target[8]: "見ると、"
  - source_tokens: `8: "보면"`
  - mapping_reason: Conditional observation.
* target[9]: "あまり"
  - source_tokens: `9: "별로"`
  - mapping_reason: Adverbial degree.
* target[10]: "力入れずに"
  - source_tokens: `10: "힘들 이지", 11: "않고"`
  - mapping_reason: Negation of effort.
* target[11]: "ざっと描いてる"
  - source_tokens: `12: "대충", 13: "그려 도"`
  - mapping_reason: Manner of drawing (roughly/casually).
* target[12]: "ように見える"
  - source_tokens: `18: "같은데"`
  - mapping_reason: Appearance/impression.
* target[13]: "けど、"
  - source_tokens: `18: "같은데"`
  - mapping_reason: Contrastive conjunction.
* target[14]: "それでも"
  - source_tokens: `13: "그려 도"`
  - mapping_reason: Concessive meaning.
* target[15]: "見栄えよく"
  - source_tokens: `14: "보기", 15: "좋게"`
  - mapping_reason: Resulting quality (looking good).
* target[16]: "仕上がってるんですよね。"
  - source_tokens: `16: "완성 되는", 17: "것"`
  - mapping_reason: Completion of work.
* target[17]: "で、"
  - source_tokens: `29: "하게", 30: "됩니다."`
  - mapping_reason: Discourse flow leading to the internal thought.
* target[18]: "自分は"
  - source_tokens: `19: "나는"`
  - mapping_reason: Subject of the thought.
* target[19]: "いつになったら"
  - source_tokens: `20: "언제"`
  - mapping_reason: Interrogative time marker.
* target[20]: "あんなふうに"
  - source_tokens: `21: "좀", 22: "저렇게"`
  - mapping_reason: Manner of action (like that).
* target[21]: "描けるようになるんだろう、"
  - source_tokens: `23: "그림 을", 24: "그릴", 25: "수", 26: "있을까"`
  - mapping_reason: Potentiality and future state of ability.
* target[22]: "って思っちゃいます。"
  - source_tokens: `27: "하는", 28: "생각 을", 29: "하게", 30: "됩니다."`
  - mapping_reason: Expressing the internal thought.

result:
```html
0. <src>유튜브 에 </src> <tgt>YouTubeに</tgt>; start=0.00, end=1.00
1. <src>그림 을 </src> <tgt>絵を</tgt>; start=1.00, end=2.00
2. <src>올리 는 고수 들이나 </src> <tgt>上げてる達人とか、</tgt>; start=2.00, end=3.00
3. <src>거리 에서 그림 을 </src> <tgt>街で絵を</tgt>; start=3.00, end=4.00
4. <src>그리 는 사람 들을 보면 </src> <tgt>描いてる人を見ると、</tgt>; start=4.00, end=5.00
5. <src>별로 </src> <tgt>あまり</tgt>; start=5.00, end=6.00
6. <src>힘들 이지 않고 대충 그려 도 </src> <tgt>力入れずにざっと描いてる</tgt>; start=6.00, end=7.00
7. <src>보기 좋게 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>완성 되는 것 같은데 </src> <tgt>ように見えるけど、それでも見栄えよく仕上がってるんですよね。</tgt>; start=8.00, end=9.00
9. <src>나는 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>언제 좀 저렇게 그림 을 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>그릴 수 있을까 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>하는 생각 을 </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>하게 됩니다. </src> <tgt>で、自分はいつになったらあんなふうに描けるようになるんだろう、って思っちゃいます。</tgt>; start=13.00, end=13.24
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_G1hDgTWHSC8_W000002 ===

source:
- language: Korean
- transcription: 유튜브에 그림을 올리는 고수들이나 거리에서 그림을 그리는 사람들을 보면 별로 힘들이지 않고 대충 그려도 보기 좋게 완성되는 것 같은데 나는 언제 좀 저렇게 그림을 그릴 수 있을까 하는 생각을 하게 됩니다.
- source_tokens:
  0. 유튜브 에
  1. 그림 을
  2. 올리 는
  3. 고수 들이나
  4. 거리 에서
  5. 그림 을
  6. 그리 는
  7. 사람 들을
  8. 보면
  9. 별로
  10. 힘들 이지
  11. 않고
  12. 대충
  13. 그려 도
  14. 보기
  15. 좋게
  16. 완성 되는
  17. 것
  18. 같은데
  19. 나는
  20. 언제
  21. 좀
  22. 저렇게
  23. 그림 을
  24. 그릴
  25. 수
  26. 있을까
  27. 하는
  28. 생각 을
  29. 하게
  30. 됩니다.

target:
- language: Chinese
- translation: 看到那些在 YouTube 上发画的高手，或者在街头画画的人，总觉得他们好像不怎么费力，随手一画就很好看。我就在想，我什么时候也能画成那样呢。
- target_sense_units:
  0. 看到那些
  1. 在YouTube上发画的
  2. 高手，
  3. 或者
  4. 在街头画画的
  5. 人，
  6. 总觉得
  7. 他们好像
  8. 不怎么费力，
  9. 随手一画
  10. 就很好看。
  11. 我就在想，
  12. 我什么时候
  13. 也能
  14. 画成那样呢。

scratchpad:
* target[0]: "看到那些"
  - source_tokens: `8: "보면"`
  - mapping_reason: "보면" (seeing/watching) corresponds to the start of the observation process.
* target[1]: "在YouTube上发画的"
  - source_tokens: `0: "유튜브 에", 1: "그림 을", 2: "올리 는"`
  - mapping_reason: Direct translation of the relative clause describing the YouTube posters.
* target[2]: "高手，"
  - source_tokens: `3: "고수 들이나"`
  - mapping_reason: "고수" means expert/master.
* target[3]: "或者"
  - source_tokens: `3: "고수 들이나"`
  - mapping_reason: The "-나" suffix in "고수들이나" functions as "or".
* target[4]: "在街头画画的"
  - source_tokens: `4: "거리 에서", 5: "그림 을", 6: "그리 는"`
  - mapping_reason: Direct translation of the relative clause describing street artists.
* target[5]: "人，"
  - source_tokens: `7: "사람 들을"`
  - mapping_reason: "사람들" means people.
* target[6]: "总觉得"
  - source_tokens: `18: "같은데"`
  - mapping_reason: "같은데" (it seems that) expresses the subjective feeling/impression.
* target[7]: "他们好像"
  - source_tokens: `17: "것", 18: "같은데"`
  - mapping_reason: "것 같은데" functions as "it seems like".
* target[8]: "不怎么费力，"
  - source_tokens: `9: "별로", 10: "힘들 이지", 11: "않고"`
  - mapping_reason: "별로 힘들이지 않고" translates to "not putting much effort".
* target[9]: "随手一画"
  - source_tokens: `12: "대충", 13: "그려 도"`
  - mapping_reason: "대충 그려도" means drawing roughly/casually.
* target[10]: "就很好看。"
  - source_tokens: `14: "보기", 15: "좋게", 16: "완성 되는"`
  - mapping_reason: "보기 좋게 완성되는" translates to finishing in a good-looking way.
* target[11]: "我就在想，"
  - source_tokens: `19: "나는", 27: "하는", 28: "생각 을", 29: "하게", 30: "됩니다."`
  - mapping_reason: "나는 ... 생각을 하게 됩니다" (I come to think that).
* target[12]: "我什么时候"
  - source_tokens: `19: "나는", 20: "언제"`
  - mapping_reason: "나는 언제" (I when).
* target[13]: "也能"
  - source_tokens: `21: "좀", 25: "수", 26: "있을까"`
  - mapping_reason: "좀 ... 수 있을까" (can I eventually/maybe).
* target[14]: "画成那样呢。"
  - source_tokens: `22: "저렇게", 23: "그림 을", 24: "그릴"`
  - mapping_reason: "저렇게 그림을 그릴" (draw like that).

result:
```html
0. <src>유튜브 에 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>그림 을 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>올리 는 고수 들이나 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>거리 에서 그림 을 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>그리 는 사람 들을 보면 </src> <tgt>看到那些在YouTube上发画的高手，或者在街头画画的人，</tgt>; start=4.00, end=5.00
5. <src>별로 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>힘들 이지 않고 대충 그려 도 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>보기 좋게 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>완성 되는 것 같은데 </src> <tgt>总觉得他们好像不怎么费力，随手一画就很好看。</tgt>; start=8.00, end=9.00
9. <src>나는 </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>언제 좀 저렇게 그림 을 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>그릴 수 있을까 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>하는 생각 을 </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>하게 됩니다. </src> <tgt>我就在想，我什么时候也能画成那样呢。</tgt>; start=13.00, end=13.24
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_GxLlh9Eui8c_W000249 ===

source:
- language: Korean
- transcription: 돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.
- source_tokens:
  0. 돌파 하고
  1. 승리 해야
  2. 한다.
  3. 다만
  4. 배도에
  5. 죄까지
  6. 갈
  7. 수
  8. 있으니
  9. 하나님
  10. 앞에서
  11. 늘
  12. 겸손 하라는
  13. 메시지 를
  14. 전하 는
  15. 대신
  16. 진짜
  17. 거듭 난
  18. 성도 도
  19. 진짜
  20. 지옥 에
  21. 아주
  22. 잘
  23. 가니까
  24. 대부분
  25. 지옥
  26. 가니까.

target:
- language: Chinese
- translation: 必须突破并取得胜利。但可能陷入背道的罪。所以与其说要在神面前常保谦卑，不如说——真正重生的人，也确实很容易下地狱。因为大多数人都是下地狱的。
- target_sense_units:
  0. 必须突破
  1. 并取得胜利。
  2. 但
  3. 可能陷入
  4. 背道的罪。
  5. 所以
  6. 与其说
  7. 要在神面前
  8. 常保谦卑，
  9. 不如说——
  10. 真正重生的人，
  11. 也确实
  12. 很容易
  13. 下地狱。
  14. 因为
  15. 大多数人
  16. 都是
  17. 下地狱的。

scratchpad:
* target[0]: "必须突破"
  - source_tokens: `0: "돌파 하고"`
  - mapping_reason: "돌파" (breakthrough) + "해야 한다" (must)
* target[1]: "并取得胜利。"
  - source_tokens: `1: "승리 해야", 2: "한다."`
  - mapping_reason: "승리" (victory) + "해야 한다" (must)
* target[2]: "但"
  - source_tokens: `3: "다만"`
  - mapping_reason: "다만" (but/however)
* target[3]: "可能陷入"
  - source_tokens: `6: "갈", 7: "수", 8: "있으니"`
  - mapping_reason: "갈 수 있으니" (can go/fall into)
* target[4]: "背道的罪。"
  - source_tokens: `4: "배도에", 5: "죄까지"`
  - mapping_reason: "배도" (apostasy) + "죄" (sin)
* target[5]: "所以"
  - source_tokens: `8: "있으니"`
  - mapping_reason: "있으니" implies a conditional/consequential flow
* target[6]: "与其说"
  - source_tokens: `15: "대신"`
  - mapping_reason: "대신" (instead of)
* target[7]: "要在神面前"
  - source_tokens: `9: "하나님", 10: "앞에서"`
  - mapping_reason: "하나님 앞에서" (before God)
* target[8]: "常保谦卑，"
  - source_tokens: `11: "늘", 12: "겸손 하라는"`
  - mapping_reason: "늘 겸손 하라는" (always be humble)
* target[9]: "不如说——"
  - source_tokens: `13: "메시지 를", 14: "전하 는", 15: "대신"`
  - mapping_reason: "메시지를 전하는 대신" (instead of conveying the message)
* target[10]: "真正重生的人，"
  - source_tokens: `16: "진짜", 17: "거듭 난", 18: "성도 도"`
  - mapping_reason: "진짜 거듭난 성도도" (even truly reborn believers)
* target[11]: "也确实"
  - source_tokens: `19: "진짜"`
  - mapping_reason: "진짜" (truly/really)
* target[12]: "很容易"
  - source_tokens: `21: "아주", 22: "잘"`
  - mapping_reason: "아주 잘" (very well/easily)
* target[13]: "下地狱。"
  - source_tokens: `20: "지옥 에", 23: "가니까"`
  - mapping_reason: "지옥에 가니까" (go to hell)
* target[14]: "因为"
  - source_tokens: `23: "가니까"`
  - mapping_reason: "가니까" (because)
* target[15]: "大多数人"
  - source_tokens: `24: "대부분"`
  - mapping_reason: "대부분" (most/majority)
* target[16]: "都是"
  - source_tokens: `26: "가니까."`
  - mapping_reason: "가니까" implies the state of being
* target[17]: "下地狱的。"
  - source_tokens: `25: "지옥", 26: "가니까."`
  - mapping_reason: "지옥 가니까" (go to hell)

result:
```html
0. <src>돌파 하고 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>승리 해야 한다. </src> <tgt>必须突破并取得胜利。</tgt>; start=1.00, end=2.00
2. <src>다만 배도에 </src> <tgt>但</tgt>; start=2.00, end=3.00
3. <src>죄까지 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>갈 수 있으니 하나님 </src> <tgt>可能陷入背道的罪。所以</tgt>; start=4.00, end=5.00
5. <src>앞에서 늘 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>겸손 하라는 메시지 를 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>전하 는 대신 </src> <tgt>与其说要在神面前常保谦卑，不如说——</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>진짜 거듭 난 성도 도 </src> <tgt>真正重生的人，</tgt>; start=10.00, end=11.00
11. <src>진짜 지옥 에 </src> <tgt>也确实</tgt>; start=11.00, end=12.00
12. <src>아주 잘 가니까 </src> <tgt>很容易下地狱。因为</tgt>; start=12.00, end=13.00
13. <src>대부분 </src> <tgt>大多数人</tgt>; start=13.00, end=14.00
14. <src>지옥 가니까. </src> <tgt>都是下地狱的。</tgt>; start=14.00, end=14.30
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== KO_GxLlh9Eui8c_W000249 ===

source:
- language: Korean
- transcription: 돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.
- source_tokens:
  0. 돌파 하고
  1. 승리 해야
  2. 한다.
  3. 다만
  4. 배도에
  5. 죄까지
  6. 갈
  7. 수
  8. 있으니
  9. 하나님
  10. 앞에서
  11. 늘
  12. 겸손 하라는
  13. 메시지 를
  14. 전하 는
  15. 대신
  16. 진짜
  17. 거듭 난
  18. 성도 도
  19. 진짜
  20. 지옥 에
  21. 아주
  22. 잘
  23. 가니까
  24. 대부분
  25. 지옥
  26. 가니까.

target:
- language: English
- translation: We must break through and be victorious. But we can even fall into the sin of apostasy. So instead of just telling people to always be humble before God, we need to recognize this: even truly born-again believers can very easily go to hell. Because most people go to hell.
- target_sense_units:
  0. We must
  1. break through
  2. and be victorious.
  3. But we can even
  4. fall into
  5. the sin of
  6. apostasy.
  7. So instead of
  8. just telling people to
  9. always be humble
  10. before God,
  11. we need to
  12. recognize this:
  13. even truly born- again believers
  14. can very easily
  15. go to hell.
  16. Because most people
  17. go to hell.

scratchpad:
* target[0]: "We must"
  - source_tokens: `1: "승리 해야", 2: "한다."`
  - mapping_reason: Expresses the obligation/necessity derived from the verb ending.
* target[1]: "break through"
  - source_tokens: `0: "돌파 하고"`
  - mapping_reason: Direct lexical translation.
* target[2]: "and be victorious."
  - source_tokens: `1: "승리 해야"`
  - mapping_reason: Direct lexical translation.
* target[3]: "But we can even"
  - source_tokens: `3: "다만", 7: "수", 8: "있으니"`
  - mapping_reason: '다만' provides 'But', '수 있으니' provides the possibility 'can'.
* target[4]: "fall into"
  - source_tokens: `6: "갈"`
  - mapping_reason: Contextual translation of 'go' as 'fall into' in this theological context.
* target[5]: "the sin of"
  - source_tokens: `5: "죄까지"`
  - mapping_reason: Lexical content.
* target[6]: "apostasy."
  - source_tokens: `4: "배도에"`
  - mapping_reason: Lexical content.
* target[7]: "So instead of"
  - source_tokens: `15: "대신"`
  - mapping_reason: Lexical content.
* target[8]: "just telling people to"
  - source_tokens: `13: "메시지 를", 14: "전하 는"`
  - mapping_reason: '전하는 메시지' translates to 'telling (a message)'.
* target[9]: "always be humble"
  - source_tokens: `11: "늘", 12: "겸손 하라는"`
  - mapping_reason: Lexical content.
* target[10]: "before God,"
  - source_tokens: `9: "하나님", 10: "앞에서"`
  - mapping_reason: Lexical content.
* target[11]: "we need to"
  - source_tokens: `15: "대신"`
  - mapping_reason: Structural transition implied by the counter-factual contrast.
* target[12]: "recognize this:"
  - source_tokens: `12: "겸손 하라는"`
  - mapping_reason: Explicitation of the warning content.
* target[13]: "even truly born- again believers"
  - source_tokens: `16: "진짜", 17: "거듭 난", 18: "성도 도"`
  - mapping_reason: Lexical content.
* target[14]: "can very easily"
  - source_tokens: `21: "아주", 22: "잘"`
  - mapping_reason: Lexical content.
* target[15]: "go to hell."
  - source_tokens: `19: "진짜", 20: "지옥 에", 23: "가니까"`
  - mapping_reason: Lexical content.
* target[16]: "Because most people"
  - source_tokens: `24: "대부분"`
  - mapping_reason: Lexical content.
* target[17]: "go to hell."
  - source_tokens: `25: "지옥", 26: "가니까."`
  - mapping_reason: Lexical content.

result:
```html
0. <src>돌파 하고 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>승리 해야 한다. </src> <tgt>We must break through and be victorious.</tgt>; start=1.00, end=2.00
2. <src>다만 배도에 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>죄까지 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>갈 수 있으니 하나님 </src> <tgt>But we can even fall into the sin of apostasy.</tgt>; start=4.00, end=5.00
5. <src>앞에서 늘 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>겸손 하라는 메시지 를 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>전하 는 대신 </src> <tgt>So instead of just telling people to always be humble before God, we need to recognize this:</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>진짜 거듭 난 성도 도 </src> <tgt>even truly born- again believers</tgt>; start=10.00, end=11.00
11. <src>진짜 지옥 에 </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>아주 잘 가니까 </src> <tgt>can very easily go to hell.</tgt>; start=12.00, end=13.00
13. <src>대부분 </src> <tgt>Because most people</tgt>; start=13.00, end=14.00
14. <src>지옥 가니까. </src> <tgt>go to hell.</tgt>; start=14.00, end=14.30
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[0]
  - verdict: mapping_error
  - reason: "The modal 'must' is derived from '해야' (1), not '한다.' (2)."
  - replace_source_tokens: 1: "승리 해야"

* target[11]
  - verdict: mapping_error
  - reason: "The source token '한다.' is unrelated to the functional unit 'we need to'."
  - replace_source_tokens: 14: "전하 는"

* target[11]
  - verdict: mapping_error
  - reason: "The source token '한다.' (sentence ending) is not the anchor for the functional unit 'we need to', which serves to transition to the next clause."
  - replace_source_tokens: 14: "전하 는"

* target[12]
  - verdict: mapping_error
  - reason: "The source token '메시지 를' does not semantically map to the functional unit 'recognize this'. The shift in communication is anchored by the context of 'preaching' and 'instead of'."
  - replace_source_tokens: 14: "전하 는", 15: "대신"
  validation:
    scratchpad:
* target[0]: "We must"
  - source_tokens: `2: "한다."`
  - mapping_reason: Expresses obligation/necessity.
* target[1]: "break through"
  - source_tokens: `0: "돌파 하고"`
  - mapping_reason: Direct lexical mapping.
* target[2]: "and be victorious."
  - source_tokens: `1: "승리 해야"`
  - mapping_reason: Direct lexical mapping.
* target[3]: "But we can even"
  - source_tokens: `3: "다만", 7: "수", 8: "있으니"`
  - mapping_reason: Contrastive conjunction plus modality of possibility.
* target[4]: "fall into"
  - source_tokens: `6: "갈"`
  - mapping_reason: Lexical realization of the verb "to go" in the context of falling into sin.
* target[5]: "the sin of"
  - source_tokens: `5: "죄까지"`
  - mapping_reason: Lexical mapping.
* target[6]: "apostasy."
  - source_tokens: `4: "배도에"`
  - mapping_reason: Lexical mapping.
* target[7]: "So instead of"
  - source_tokens: `15: "대신"`
  - mapping_reason: Connective/prepositional contrast.
* target[8]: "just telling people to"
  - source_tokens: `13: "메시지 를", 14: "전하 는"`
  - mapping_reason: Lexical mapping of "delivering a message".
* target[9]: "always be humble"
  - source_tokens: `11: "늘", 12: "겸손 하라는"`
  - mapping_reason: Lexical mapping.
* target[10]: "before God,"
  - source_tokens: `9: "하나님", 10: "앞에서"`
  - mapping_reason: Lexical mapping.
* target[11]: "we need to"
  - source_tokens: `2: "한다."`
  - mapping_reason: Implicit necessity/requirement implied in the source structure.
* target[12]: "recognize this:"
  - source_tokens: `13: "메시지 를"`
  - mapping_reason: The content of the message is what needs to be recognized.
* target[13]: "even truly born- again believers"
  - source_tokens: `16: "진짜", 17: "거듭 난", 18: "성도 도"`
  - mapping_reason: Direct lexical mapping.
* target[14]: "can very easily"
  - source_tokens: `21: "아주", 22: "잘"`
  - mapping_reason: Lexical mapping for adverbial intensity.
* target[15]: "go to hell."
  - source_tokens: `19: "진짜", 20: "지옥 에", 23: "가니까"`
  - mapping_reason: Direct lexical mapping.
* target[16]: "Because most people"
  - source_tokens: `24: "대부분"`
  - mapping_reason: Lexical mapping.
* target[17]: "go to hell."
  - source_tokens: `25: "지옥", 26: "가니까."`
  - mapping_reason: Direct lexical mapping.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [0]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [3, 7, 8]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [6]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [15]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [13, 14]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [9, 10]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [2]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [13]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [16, 17, 18]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [21, 22]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [19, 20, 23]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [24]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [25, 26]
  }
]

- retry: 1/5
  status: failed_after_response
  reason: * target[11]
  - verdict: mapping_error
  - reason: "The target unit 'we need to' functions as a structural transition linked to '대신' (instead), not '전하는' (telling)."
  - replace_source_tokens: 15: "대신"

* target[12]
  - verdict: mapping_error
  - reason: "The tokens 13, 14, and 15 are linked to the preceding 'instead of' (대신) and 'telling' (전하는 메시지) phrases. The target unit 'recognize this:' is an explicitation of the following clause, which is better anchored by the instruction to be humble (12)."
  - replace_source_tokens: 12: "겸손 하라는"
  validation:
    scratchpad:
* target[0]: "We must"
  - source_tokens: `1: "승리 해야"`
  - mapping_reason: The modal "must" is derived from the obligation suffix "해야".
* target[1]: "break through"
  - source_tokens: `0: "돌파 하고"`
  - mapping_reason: Direct translation of "돌파".
* target[2]: "and be victorious."
  - source_tokens: `1: "승리 해야", 2: "한다."`
  - mapping_reason: "승리" provides the content, "한다" provides the sentence completion/assertion.
* target[3]: "But we can even"
  - source_tokens: `3: "다만", 7: "수", 8: "있으니"`
  - mapping_reason: "다만" (But), "수 있으니" (can).
* target[4]: "fall into"
  - source_tokens: `6: "갈"`
  - mapping_reason: "갈" (to go/fall into).
* target[5]: "the sin of"
  - source_tokens: `5: "죄까지"`
  - mapping_reason: "죄" (sin).
* target[6]: "apostasy."
  - source_tokens: `4: "배도에"`
  - mapping_reason: "배도" (apostasy).
* target[7]: "So instead of"
  - source_tokens: `15: "대신"`
  - mapping_reason: "대신" (instead of).
* target[8]: "just telling people to"
  - source_tokens: `13: "메시지 를", 14: "전하 는"`
  - mapping_reason: "메시지를 전하는" (telling/conveying a message).
* target[9]: "always be humble"
  - source_tokens: `11: "늘", 12: "겸손 하라는"`
  - mapping_reason: "늘" (always), "겸손 하라는" (be humble).
* target[10]: "before God,"
  - source_tokens: `9: "하나님", 10: "앞에서"`
  - mapping_reason: "하나님 앞에서" (before God).
* target[11]: "we need to"
  - source_tokens: `14: "전하 는"`
  - mapping_reason: This acts as the transition/functional shift from the previous clause to the new realization.
* target[12]: "recognize this:"
  - source_tokens: `13: "메시지 를", 14: "전하 는", 15: "대신"`
  - mapping_reason: The shift from the expected message to the new realization.
* target[13]: "even truly born- again believers"
  - source_tokens: `16: "진짜", 17: "거듭 난", 18: "성도 도"`
  - mapping_reason: "진짜" (truly), "거듭 난" (born-again), "성도 도" (believers).
* target[14]: "can very easily"
  - source_tokens: `21: "아주", 22: "잘"`
  - mapping_reason: "아주 잘" (very easily).
* target[15]: "go to hell."
  - source_tokens: `20: "지옥 에", 23: "가니까"`
  - mapping_reason: "지옥에 가니까" (go to hell).
* target[16]: "Because most people"
  - source_tokens: `24: "대부분"`
  - mapping_reason: "대부분" (most people).
* target[17]: "go to hell."
  - source_tokens: `25: "지옥", 26: "가니까."`
  - mapping_reason: "지옥 가니까" (go to hell).
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [0]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [1, 2]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [3, 7, 8]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [6]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [15]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [13, 14]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [9, 10]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [14]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [13, 14, 15]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [16, 17, 18]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [21, 22]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [20, 23]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [24]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [25, 26]
  }
]

- retry: 2/5
  status: succeeded
  reason: retry attempt succeeded

---
