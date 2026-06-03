=== KO_E7ZEWK_4k08_W000004 ===

source:
- language: Korean
- transcription: 그러나 하나님의 백성의 믿음은 어떻게 강해질 수 있을까? 엄마, 엄마도 있다. 어떻게 강해질 수 있을까? 볼까요? 둘, 셋.
- source_tokens:
  0. 그러나
  1. 하나님
  2. 의
  3. 백성
  4. 의
  5. 믿음
  6. 은
  7. 어떻게
  8. 강해
  9. 질
  10. 수
  11. 있을까?
  12. 엄마,
  13. 엄마
  14. 도
  15. 있다.
  16. 어떻게
  17. 강해
  18. 질
  19. 수
  20. 있을까?
  21. 볼까요?
  22. 둘,
  23. 셋.

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
  - source_tokens: `0: "그러나", 7: "어떻게"`
  - mapping_reason: "그러나" provides the contrastive "But", and "어떻게" provides the interrogative "how".

* target[1]: "the faith of God's people"
  - source_tokens: `1: "하나님", 2: "의", 3: "백성", 4: "의", 5: "믿음", 6: "은"`
  - mapping_reason: Maps the possessive structure of God's people and the subject "faith".

* target[2]: "become stronger?"
  - source_tokens: `8: "강해", 9: "질", 10: "수", 11: "있을까?"`
  - mapping_reason: The verbal phrase for becoming strong and the interrogative ending.

* target[3]: "Mom– Mom is here too."
  - source_tokens: `12: "엄마,", 13: "엄마", 14: "도", 15: "있다."`
  - mapping_reason: Direct translation of the segment referring to mom's presence.

* target[4]: "How can it become stronger?"
  - source_tokens: `16: "어떻게", 17: "강해", 18: "질", 19: "수", 20: "있을까?"`
  - mapping_reason: Repeating the question about faith strength.

* target[5]: "Let's see?"
  - source_tokens: `21: "볼까요?"`
  - mapping_reason: Direct translation of the invitation to look/see.

* target[6]: "Two, three."
  - source_tokens: `22: "둘,", 23: "셋."`
  - mapping_reason: Direct translation of the counting sequence.

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
  1. 하나님
  2. 의
  3. 백성
  4. 의
  5. 믿음
  6. 은
  7. 어떻게
  8. 강해
  9. 질
  10. 수
  11. 있을까?
  12. 엄마,
  13. 엄마
  14. 도
  15. 있다.
  16. 어떻게
  17. 강해
  18. 질
  19. 수
  20. 있을까?
  21. 볼까요?
  22. 둘,
  23. 셋.

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
  - mapping_reason: Direct translation of the conjunction.

* target[1]: "神の"
  - source_tokens: `1: "하나님", 2: "의"`
  - mapping_reason: Possessive relation (God's).

* target[2]: "民の"
  - source_tokens: `3: "백성", 4: "의"`
  - mapping_reason: Possessive relation (people's).

* target[3]: "信仰は"
  - source_tokens: `5: "믿음", 6: "은"`
  - mapping_reason: Subject/Topic (faith).

* target[4]: "どうすれば"
  - source_tokens: `7: "어떻게"`
  - mapping_reason: Interrogative adverb (how).

* target[5]: "強くなれるのでしょうか？"
  - source_tokens: `8: "강해", 9: "질", 10: "수", 11: "있을까?"`
  - mapping_reason: Predicate verb phrase (can become strong).

* target[6]: "ママ、"
  - source_tokens: `12: "엄마,"`
  - mapping_reason: Direct address.

* target[7]: "ママも"
  - source_tokens: `13: "엄마", 14: "도"`
  - mapping_reason: Subject with additive particle (also).

* target[8]: "いるね。"
  - source_tokens: `15: "있다."`
  - mapping_reason: Existential verb (exists).

* target[9]: "どうすれば"
  - source_tokens: `16: "어떻게"`
  - mapping_reason: Interrogative adverb (how).

* target[10]: "強くなれるのでしょうか？"
  - source_tokens: `17: "강해", 18: "질", 19: "수", 20: "있을까?"`
  - mapping_reason: Predicate verb phrase (can become strong).

* target[11]: "見てみましょうか？"
  - source_tokens: `21: "볼까요?"`
  - mapping_reason: Suggestive/Interrogative verb (let's see).

* target[12]: "に、"
  - source_tokens: `22: "둘,"`
  - mapping_reason: Number (two).

* target[13]: "さん。"
  - source_tokens: `23: "셋."`
  - mapping_reason: Number (three).

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
=== KO_E7ZEWK_4k08_W000004 ===

source:
- language: Korean
- transcription: 그러나 하나님의 백성의 믿음은 어떻게 강해질 수 있을까? 엄마, 엄마도 있다. 어떻게 강해질 수 있을까? 볼까요? 둘, 셋.
- source_tokens:
  0. 그러나
  1. 하나님
  2. 의
  3. 백성
  4. 의
  5. 믿음
  6. 은
  7. 어떻게
  8. 강해
  9. 질
  10. 수
  11. 있을까?
  12. 엄마,
  13. 엄마
  14. 도
  15. 있다.
  16. 어떻게
  17. 강해
  18. 질
  19. 수
  20. 있을까?
  21. 볼까요?
  22. 둘,
  23. 셋.

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
  - mapping_reason: Connective "but/however"
* target[1]: "上帝子民的信心"
  - source_tokens: `1: "하나님", 2: "의", 3: "백성", 4: "의", 5: "믿음", 6: "은"`
  - mapping_reason: Noun phrase "faith of God's people" including particles
* target[2]: "要怎么"
  - source_tokens: `7: "어떻게"`
  - mapping_reason: Interrogative adverb "how"
* target[3]: "变得更坚强呢？"
  - source_tokens: `8: "강해", 9: "질", 10: "수", 11: "있을까?"`
  - mapping_reason: Predicate "become stronger" including modal and question endings
* target[4]: "妈妈，"
  - source_tokens: `12: "엄마,"`
  - mapping_reason: Address term "mom"
* target[5]: "妈妈也在呢。"
  - source_tokens: `13: "엄마", 14: "도", 15: "있다."`
  - mapping_reason: Subject "mom" with additive particle and existence verb
* target[6]: "要怎么"
  - source_tokens: `16: "어떻게"`
  - mapping_reason: Interrogative adverb "how"
* target[7]: "变得更坚强呢？"
  - source_tokens: `17: "강해", 18: "질", 19: "수", 20: "있을까?"`
  - mapping_reason: Predicate "become stronger" including modal and question endings
* target[8]: "我们来看看？"
  - source_tokens: `21: "볼까요?"`
  - mapping_reason: Propositive verb "let's see"
* target[9]: "二，"
  - source_tokens: `22: "둘,"`
  - mapping_reason: Number "two"
* target[10]: "三。"
  - source_tokens: `23: "셋."`
  - mapping_reason: Number "three"

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
  4. 중요
  5. 합니다,
  6. 여러분.
  7. 파밍을
  8. 열심히
  9. 해주세요.
  10. 어
  11. 발소리
  12. 난다.
  13. 어
  14. 당황
  15. 한
  16. 척하
  17. 면서
  18. 이렇게
  19. 파밍해주면
  20. 됩니다,
  21. 여러분.

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
  - mapping_reason: "일단" functions as an introductory discourse marker, synonymous with "まず".

* target[1]: "PUBGは"
  - source_tokens: `1: "배그는"`
  - mapping_reason: Direct translation of "배그" (PUBG) with the topic marker.

* target[2]: "ファームが"
  - source_tokens: `2: "파밍이"`
  - mapping_reason: Direct translation of "파밍" (farming/looting) with the subject marker.

* target[3]: "一番重要です、"
  - source_tokens: `3: "제일", 4: "중요", 5: "합니다,"`
  - mapping_reason: "제일" (most), "중요" (important), and the verb ending "합니다" form the predicate.

* target[4]: "皆さん。"
  - source_tokens: `6: "여러분."`
  - mapping_reason: Direct address to the audience.

* target[5]: "一生懸命"
  - source_tokens: `8: "열심히"`
  - mapping_reason: Direct translation of "열심히" (diligently/hard).

* target[6]: "ファームしてください。"
  - source_tokens: `7: "파밍을", 9: "해주세요."`
  - mapping_reason: "파밍을" (farming) as object and "해주세요" (please do) as the imperative verb.

* target[7]: "あ、"
  - source_tokens: `10: "어"`
  - mapping_reason: Interjection expressing realization.

* target[8]: "こうやって"
  - source_tokens: `18: "이렇게"`
  - mapping_reason: "이렇게" means "like this" (こうやって).

* target[9]: "ファームすればいいんですよ。"
  - source_tokens: `19: "파밍해주면", 20: "됩니다,"`
  - mapping_reason: "파밍해주면 됩니다" expresses the condition and suggestion for the action.

* target[10]: "慌てたふりをしながらね、"
  - source_tokens: `14: "당황", 15: "한", 16: "척하", 17: "면서"`
  - mapping_reason: "당황한 척하면서" means "while pretending to be flustered/panicked".

* target[11]: "皆さん。"
  - source_tokens: `21: "여러분."`
  - mapping_reason: Final direct address to the audience.

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
  6. 서로
  7. 까지
  8. 뜯고
  9. 싸움
  10. 을
  11. 해야
  12. 만이
  13. 되는
  14. 사람
  15. 이잖아.
  16. 그러면
  17. 어떻게
  18. 이제
  19. 이게
  20. BJ
  21. 궁합은
  22. 어떻게
  23. 한
  24. 사람
  25. 이
  26. 어떻게
  27. 어?

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
  - source_tokens: `0: "악인네는"`
  - mapping_reason: "悪人" (악인) + "同士" (네/group)

* target[1]: "「出せ」と"
  - source_tokens: `2: "내놔"`
  - mapping_reason: "내놔" (give/hand over)

* target[2]: "言い合っていたら、"
  - source_tokens: `1: "서로", 3: "하니까"`
  - mapping_reason: "서로" (each other) + "하니까" (doing/saying)

* target[3]: "お互いに"
  - source_tokens: `6: "서로"`
  - mapping_reason: "서로" (each other)

* target[4]: "奪い合って"
  - source_tokens: `8: "뜯고"`
  - mapping_reason: "뜯고" (tearing/stealing/taking)

* target[5]: "喧嘩する"
  - source_tokens: `9: "싸움"`
  - mapping_reason: "싸움" (fight)

* target[6]: "しかない"
  - source_tokens: `11: "해야", 12: "만이"`
  - mapping_reason: "해야만이" (must do/only way)

* target[7]: "人たち"
  - source_tokens: `14: "사람"`
  - mapping_reason: "사람" (person/people)

* target[8]: "ですよね。"
  - source_tokens: `13: "되는", 15: "이잖아."`
  - mapping_reason: "되는" (become/is) + "이잖아" (affirmation)

* target[9]: "じゃあ、"
  - source_tokens: `16: "그러면"`
  - mapping_reason: "그러면" (then/so)

* target[10]: "このBJの"
  - source_tokens: `19: "이게", 20: "BJ"`
  - mapping_reason: "이게" (this) + "BJ"

* target[11]: "相性っていうのは、"
  - source_tokens: `21: "궁합은"`
  - mapping_reason: "궁합" (compatibility/chemistry)

* target[12]: "一人が"
  - source_tokens: `23: "한", 24: "사람", 25: "이"`
  - mapping_reason: "한 사람" (one person)

* target[13]: "どうやって……？"
  - source_tokens: `17: "어떻게", 22: "어떻게", 26: "어떻게", 27: "어?"`
  - mapping_reason: "어떻게" (how) + filler/hesitation "어?"

result:
```html
0. <src>악인네는 </src> <tgt>悪人同士が</tgt>; start=0.00, end=1.00
1. <src>서로 내놔 하니까 </src> <tgt>「出せ」と言い合っていたら、</tgt>; start=1.00, end=2.00
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
=== KO_G1hDgTWHSC8_W000038 ===

source:
- language: Korean
- transcription: 자기 그림을 그리면서 카피할 때 머리 속에 기억해두고 메모해둔 표현 방법을 그대로 실제 적용하면서 그림을 그립니다. 그러면 그림 그리는 실력이 빠르게 좋아집니다.
- source_tokens:
  0. 자기
  1. 그림
  2. 을
  3. 그리
  4. 면서
  5. 카피할
  6. 때
  7. 머리
  8. 속에
  9. 기억
  10. 해두고
  11. 메모
  12. 해둔
  13. 표현
  14. 방법
  15. 을
  16. 그대로
  17. 실제
  18. 적용
  19. 하면서
  20. 그림
  21. 을
  22. 그립
  23. 니다.
  24. 그러면
  25. 그림
  26. 그리
  27. 는
  28. 실력
  29. 이
  30. 빠르
  31. 게
  32. 좋아집니다.

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
  - mapping_reason: "Self-referential pronoun"
* target[1]: "絵を"
  - source_tokens: `1: "그림", 2: "을"`
  - mapping_reason: "Object of drawing"
* target[2]: "描きながら"
  - source_tokens: `3: "그리", 4: "면서"`
  - mapping_reason: "Simultaneous action"
* target[3]: "模写をする"
  - source_tokens: `5: "카피할"`
  - mapping_reason: "Copying/tracing action"
* target[4]: "ときは、"
  - source_tokens: `6: "때"`
  - mapping_reason: "Temporal condition"
* target[5]: "頭の中で"
  - source_tokens: `7: "머리", 8: "속에"`
  - mapping_reason: "Mental location"
* target[6]: "覚えて"
  - source_tokens: `9: "기억", 10: "해두고"`
  - mapping_reason: "Memory action"
* target[7]: "メモしておいた"
  - source_tokens: `11: "메모", 12: "해둔"`
  - mapping_reason: "Note-taking action"
* target[8]: "表現方法を、"
  - source_tokens: `13: "표현", 14: "방법", 15: "을"`
  - mapping_reason: "Method of expression"
* target[9]: "そのまま"
  - source_tokens: `16: "그대로"`
  - mapping_reason: "As it is"
* target[10]: "実際に"
  - source_tokens: `17: "실제"`
  - mapping_reason: "In reality"
* target[11]: "使って"
  - source_tokens: `18: "적용", 19: "하면서"`
  - mapping_reason: "Application/use"
* target[12]: "描いています。"
  - source_tokens: `20: "그림", 21: "을", 22: "그립", 23: "니다."`
  - mapping_reason: "Main action of drawing"
* target[13]: "そうすると、"
  - source_tokens: `24: "그러면"`
  - mapping_reason: "Consequence connective"
* target[14]: "絵を"
  - source_tokens: `25: "그림"`
  - mapping_reason: "Object of drawing skill"
* target[15]: "描く実力が"
  - source_tokens: `26: "그리", 27: "는", 28: "실력", 29: "이"`
  - mapping_reason: "Drawing ability"
* target[16]: "どんどん"
  - source_tokens: `30: "빠르", 31: "게"`
  - mapping_reason: "Adverbial speed/progression"
* target[17]: "上達します。"
  - source_tokens: `32: "좋아집니다."`
  - mapping_reason: "Improvement"

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
  3. 우리
  4. 가
  5. 뉴욕
  6. 에
  7. 살고
  8. 있으니까
  9. 좀
  10. 뉴욕
  11. 과
  12. 뉴저지
  13. 지역
  14. 의
  15. 유명
  16. 한
  17. 곳을
  18. 소개
  19. 해드릴
  20. 수도
  21. 있어요.
  22. 그렇
  23. 죠,
  24. 그렇
  25. 죠.
  26. 직접
  27. 그
  28. 현장
  29. 에
  30. 가서
  31. 저희
  32. 들이
  33. 이제
  34. 체험
  35. 도
  36. 해보고
  37. 소개
  38. 도
  39. 해드리고
  40. 그런
  41. 프로그램
  42. 도
  43. 만들
  44. 기획
  45. 이고요.
  46. 어
  47. 뉴욕
  48. 미니
  49. 스에
  50. 대한
  51. 설명
  52. 을
  53. 좀
  54. 해주시죠.

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
  - mapping_reason: Discourse connective
* target[1]: "あ、"
  - source_tokens: `1: "아"`
  - mapping_reason: Filler/discourse marker
* target[2]: "私たちは"
  - source_tokens: `3: "우리", 4: "가"`
  - mapping_reason: Subject pronoun
* target[3]: "ニューヨークに"
  - source_tokens: `5: "뉴욕", 6: "에"`
  - mapping_reason: Locative
* target[4]: "住んでいるので、"
  - source_tokens: `7: "살고", 8: "있으니까"`
  - mapping_reason: Reason/cause state
* target[5]: "ニューヨークや"
  - source_tokens: `10: "뉴욕", 11: "과"`
  - mapping_reason: Location noun and conjunction
* target[6]: "ニュージャージー地域の"
  - source_tokens: `12: "뉴저지", 13: "지역", 14: "의"`
  - mapping_reason: Location noun and genitive
* target[7]: "有名な場所を"
  - source_tokens: `15: "유명", 16: "한", 17: "곳을"`
  - mapping_reason: Object noun phrase
* target[8]: "ご紹介することもできます。"
  - source_tokens: `18: "소개", 19: "해드릴", 20: "수도", 21: "있어요."`
  - mapping_reason: Verb phrase with potential modality
* target[9]: "そうですね、"
  - source_tokens: `22: "그렇", 23: "죠,"`
  - mapping_reason: Agreement marker
* target[10]: "その通りです。"
  - source_tokens: `24: "그렇", 25: "죠."`
  - mapping_reason: Confirmation marker
* target[11]: "実際に"
  - source_tokens: `26: "직접"`
  - mapping_reason: Adverb (directly/actually)
* target[12]: "その現場に"
  - source_tokens: `27: "그", 28: "현장", 29: "에"`
  - mapping_reason: Locative noun phrase
* target[13]: "行きます。"
  - source_tokens: `30: "가서"`
  - mapping_reason: Verb (go)
* target[14]: "そこで"
  - source_tokens: `33: "이제"`
  - mapping_reason: Temporal/situational discourse marker
* target[15]: "体験して"
  - source_tokens: `34: "체험", 35: "도", 36: "해보고"`
  - mapping_reason: Verb phrase
* target[16]: "ご紹介するような"
  - source_tokens: `37: "소개", 38: "도", 39: "해드리고"`
  - mapping_reason: Verb phrase
* target[17]: "番組も"
  - source_tokens: `41: "프로그램", 42: "도"`
  - mapping_reason: Noun with particle
* target[18]: "企画しています。"
  - source_tokens: `40: "그런", 43: "만들", 44: "기획", 45: "이고요."`
  - mapping_reason: Verb phrase (planning/making)
* target[19]: "えー、"
  - source_tokens: `46: "어"`
  - mapping_reason: Filler
* target[20]: "ニューヨーク・ミニスについて"
  - source_tokens: `47: "뉴욕", 48: "미니", 49: "스에", 50: "대한"`
  - mapping_reason: Topic noun phrase
* target[21]: "少し"
  - source_tokens: `53: "좀"`
  - mapping_reason: Adverb (a little)
* target[22]: "説明していただけますか？"
  - source_tokens: `51: "설명", 52: "을", 54: "해주시죠."`
  - mapping_reason: Request verb phrase

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
=== KO_E9GzA6TOlV4_W000007 ===

source:
- language: Korean
- transcription: 일단 배그는 파밍이 제일 중요합니다, 여러분. 파밍을 열심히 해주세요. 어 발소리 난다. 어 당황한 척하면서 이렇게 파밍해주면 됩니다, 여러분.
- source_tokens:
  0. 일단
  1. 배그는
  2. 파밍이
  3. 제일
  4. 중요
  5. 합니다,
  6. 여러분.
  7. 파밍을
  8. 열심히
  9. 해주세요.
  10. 어
  11. 발소리
  12. 난다.
  13. 어
  14. 당황
  15. 한
  16. 척하
  17. 면서
  18. 이렇게
  19. 파밍해주면
  20. 됩니다,
  21. 여러분.

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
  - mapping_reason: Discourse marker for sequence.
* target[1]: "looting is"
  - source_tokens: `2: "파밍이"`
  - mapping_reason: Subject of the sentence.
* target[2]: "the most important thing"
  - source_tokens: `3: "제일", 4: "중요", 5: "합니다,"`
  - mapping_reason: Superlative importance predicate.
* target[3]: "in PUBG,"
  - source_tokens: `1: "배그는"`
  - mapping_reason: Contextual domain.
* target[4]: "guys."
  - source_tokens: `6: "여러분."`
  - mapping_reason: Direct address.
* target[5]: "Make sure"
  - source_tokens: `9: "해주세요."`
  - mapping_reason: Imperative/request marker.
* target[6]: "you loot hard."
  - source_tokens: `7: "파밍을", 8: "열심히"`
  - mapping_reason: Action and adverbial modifier.
* target[7]: "Oh,"
  - source_tokens: `10: "어"`
  - mapping_reason: Interjection.
* target[8]: "I hear footsteps."
  - source_tokens: `11: "발소리", 12: "난다."`
  - mapping_reason: Perception of sound.
* target[9]: "Oh,"
  - source_tokens: `13: "어"`
  - mapping_reason: Interjection.
* target[10]: "just keep looting"
  - source_tokens: `19: "파밍해주면", 20: "됩니다,"`
  - mapping_reason: Continued action instruction.
* target[11]: "like this,"
  - source_tokens: `18: "이렇게"`
  - mapping_reason: Manner of action.
* target[12]: "guys,"
  - source_tokens: `21: "여러분."`
  - mapping_reason: Direct address.
* target[13]: "while acting like"
  - source_tokens: `16: "척하", 17: "면서"`
  - mapping_reason: Simultaneous action/pretense.
* target[14]: "you're panicked."
  - source_tokens: `14: "당황", 15: "한"`
  - mapping_reason: State of panic.

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
  6. 서로
  7. 까지
  8. 뜯고
  9. 싸움
  10. 을
  11. 해야
  12. 만이
  13. 되는
  14. 사람
  15. 이잖아.
  16. 그러면
  17. 어떻게
  18. 이제
  19. 이게
  20. BJ
  21. 궁합은
  22. 어떻게
  23. 한
  24. 사람
  25. 이
  26. 어떻게
  27. 어?

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
  - mapping_reason: "악인네" (bad people) is the subject, "는" sets the topic/condition.

* target[1]: "telling each other"
  - source_tokens: `1: "서로"`
  - mapping_reason: "서로" (each other) is the object of the communication.

* target[2]: "to hand it over,"
  - source_tokens: `2: "내놔", 3: "하니까"`
  - mapping_reason: "내놔" (hand it over) is the content of the demand, "하니까" provides the "if/when" context.

* target[3]: "doesn't that mean"
  - source_tokens: `13: "되는", 14: "사람", 15: "이잖아."`
  - mapping_reason: The structure "사람이잖아" implies the rhetorical question/conclusion "doesn't that mean...".

* target[4]: "they have to"
  - source_tokens: `11: "해야", 12: "만이"`
  - mapping_reason: "해야만이" (have to/must) defines the necessity.

* target[5]: "tear each other apart"
  - source_tokens: `6: "서로", 7: "까지", 8: "뜯고"`
  - mapping_reason: "서로" (each other) + "뜯고" (tear apart).

* target[6]: "and fight to get anywhere?"
  - source_tokens: `9: "싸움", 10: "을"`
  - mapping_reason: "싸움을" (fight) represents the conflict action.

* target[7]: "So then,"
  - source_tokens: `16: "그러면"`
  - mapping_reason: "그러면" (so then) is the connective.

* target[8]: "how does this BJ chemistry"
  - source_tokens: `19: "이게", 20: "BJ", 21: "궁합은"`
  - mapping_reason: "이게" (this) + "BJ" + "궁합은" (chemistry).

* target[9]: "work?"
  - source_tokens: `17: "어떻게", 22: "어떻게"`
  - mapping_reason: "어떻게" (how) functions as the interrogative for "work".

* target[10]: "How can one person...?"
  - source_tokens: `23: "한", 24: "사람", 25: "이", 26: "어떻게", 27: "어?"`
  - mapping_reason: "한 사람" (one person) + "어떻게" (how) + "어?" (filler/trailing question).

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
=== KO_G1hDgTWHSC8_W000038 ===

source:
- language: Korean
- transcription: 자기 그림을 그리면서 카피할 때 머리 속에 기억해두고 메모해둔 표현 방법을 그대로 실제 적용하면서 그림을 그립니다. 그러면 그림 그리는 실력이 빠르게 좋아집니다.
- source_tokens:
  0. 자기
  1. 그림
  2. 을
  3. 그리
  4. 면서
  5. 카피할
  6. 때
  7. 머리
  8. 속에
  9. 기억
  10. 해두고
  11. 메모
  12. 해둔
  13. 표현
  14. 방법
  15. 을
  16. 그대로
  17. 실제
  18. 적용
  19. 하면서
  20. 그림
  21. 을
  22. 그립
  23. 니다.
  24. 그러면
  25. 그림
  26. 그리
  27. 는
  28. 실력
  29. 이
  30. 빠르
  31. 게
  32. 좋아집니다.

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
  - source_tokens: `0: "자기", 1: "그림", 2: "을", 3: "그리", 4: "면서"`
  - mapping_reason: "자기" (自己的) + "그림을 그리면서" (画画的时候/画自己的画)

* target[1]: "做临摹的时候，"
  - source_tokens: `5: "카피할", 6: "때"`
  - mapping_reason: "카피할" (临摹) + "때" (的时候)

* target[2]: "会把"
  - source_tokens: `23: "니다."`
  - mapping_reason: Indicates the habitual/future tense (会) implied in the declarative sentence structure.

* target[3]: "脑子里"
  - source_tokens: `7: "머리", 8: "속에"`
  - mapping_reason: "머리 속에" (脑子里)

* target[4]: "记住和记下来"
  - source_tokens: `9: "기억", 10: "해두고", 11: "메모", 12: "해둔"`
  - mapping_reason: "기억해두고" (记住) + "메모해둔" (记下来)

* target[5]: "的表现手法"
  - source_tokens: `13: "표현", 14: "방법", 15: "을"`
  - mapping_reason: "표현 방법" (表现手法)

* target[6]: "直接用到"
  - source_tokens: `16: "그대로", 18: "적용", 19: "하면서"`
  - mapping_reason: "그대로" (直接) + "적용하면서" (用到)

* target[7]: "实际画中。"
  - source_tokens: `17: "실제", 20: "그림", 21: "을", 22: "그립"`
  - mapping_reason: "실제" (实际) + "그림을 그립" (画中)

* target[8]: "这样"
  - source_tokens: `24: "그러면"`
  - mapping_reason: "그러면" (这样)

* target[9]: "画画的水平"
  - source_tokens: `25: "그림", 26: "그리", 27: "는", 28: "실력", 29: "이"`
  - mapping_reason: "그림 그리는 실력" (画画的水平)

* target[10]: "就会提高"
  - source_tokens: `32: "좋아집니다."`
  - mapping_reason: "좋아집니다" (提高)

* target[11]: "得很快。"
  - source_tokens: `30: "빠르", 31: "게"`
  - mapping_reason: "빠르게" (很快)

result:
```html
0. <src>자기 그림 을 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>그리 면서 카피할 때 </src> <tgt>画自己的画、做临摹的时候，</tgt>; start=1.00, end=2.00
2. <src>머리 속에 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>기억 해두고 메모 해둔 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>표현 방법 을 </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>그대로 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>실제 적용 하면서 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>그림 을 그립 니다. </src> <tgt>会把脑子里记住和记下来的表现手法直接用到实际画中。</tgt>; start=7.00, end=8.00
8. <src>그러면 </src> <tgt>这样</tgt>; start=8.00, end=9.00
9. <src>그림 그리 는 실력 이 </src> <tgt>画画的水平</tgt>; start=9.00, end=10.00
10. <src>빠르 게 </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>좋아집니다. </src> <tgt>就会提高得很快。</tgt>; start=11.00, end=11.14
```

- max_empty_window_count: 5


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
  3. 이해
  4. 하셔야
  5. 될
  6. 부분
  7. 의
  8. 측면
  9. 이
  10. 있어서
  11. 여러분
  12. 들이
  13. 잘
  14. 한번
  15. 보시고
  16. 아주
  17. 이렇게
  18. 하니까
  19. 행이
  20. 병합이
  21. 되는구나
  22. 이렇게
  23. 느끼
  24. 셨으면
  25. 좋겠습니다.
  26. 말로
  27. 하려니까
  28. 너무
  29. 힘드
  30. 네요.
  31. 자,
  32. 그다음
  33. 여기
  34. 는
  35. 합계
  36. 라고
  37. 되어
  38. 있는
  39. 부분
  40. 은
  41. 여기
  42. 있는
  43. 이
  44. 각각
  45. 의
  46. 칸
  47. 세
  48. 개의
  49. 칸을

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
  - source_tokens: `6: "부분", 7: "의", 4: "하셔야", 5: "될"`
  - mapping_reason: Maps to the "part" (부분) and the modality "need to" (하셔야 될).

* target[1]: "大家直观地理解。"
  - source_tokens: `11: "여러분", 12: "들이", 2: "직관적으로", 3: "이해"`
  - mapping_reason: Maps to the audience (여러분들) and the action/manner (직관적으로 이해).

* target[2]: "希望大家"
  - source_tokens: `25: "좋겠습니다.", 11: "여러분", 12: "들이"`
  - mapping_reason: "좋겠습니다" conveys the "hope/wish" directed at the audience.

* target[3]: "仔细看看，"
  - source_tokens: `13: "잘", 14: "한번", 15: "보시고"`
  - mapping_reason: "잘 한번 보시고" corresponds to "carefully look at".

* target[4]: "感受一下"
  - source_tokens: `23: "느끼", 24: "셨으면"`
  - mapping_reason: Corresponds to "느끼셨으면" (feel/experience).

* target[5]: "“原来这样"
  - source_tokens: `17: "이렇게", 18: "하니까"`
  - mapping_reason: "이렇게 하니까" (doing it like this) conveys the "so it is like this" (原来这样) realization.

* target[6]: "行就会合并啊”。"
  - source_tokens: `19: "행이", 20: "병합이", 21: "되는구나"`
  - mapping_reason: "행이 병합이 되는구나" (rows are merged).

* target[7]: "光靠说"
  - source_tokens: `26: "말로", 27: "하려니까"`
  - mapping_reason: "말로 하려니까" (trying to say it with words).

* target[8]: "真的太难了。"
  - source_tokens: `28: "너무", 29: "힘드", 30: "네요."`
  - mapping_reason: "너무 힘드네요" (really too difficult).

* target[9]: "好，"
  - source_tokens: `31: "자,"`
  - mapping_reason: Discourse marker "자" (well/now).

* target[10]: "接下来，"
  - source_tokens: `32: "그다음"`
  - mapping_reason: "그다음" (next).

* target[11]: "这里写着"
  - source_tokens: `33: "여기", 37: "되어", 38: "있는"`
  - mapping_reason: "여기... 되어 있는" (what is written here).

* target[12]: "“合计”的部分，"
  - source_tokens: `35: "합계", 39: "부분", 40: "은"`
  - mapping_reason: "합계... 부분은" (the part that is 'sum').

* target[13]: "是将"
  - source_tokens: `41: "여기", 42: "있는"`
  - mapping_reason: Refers to the contents located here.

* target[14]: "这里的"
  - source_tokens: `43: "이", 44: "각각", 45: "의"`
  - mapping_reason: "이 각각의" (each of these).

* target[15]: "每一个格子，"
  - source_tokens: `46: "칸"`
  - mapping_reason: "칸" (cell/grid).

* target[16]: "也就是"
  - source_tokens: `47: "세"`
  - mapping_reason: The count "three".

* target[17]: "这三个格子……"
  - source_tokens: `48: "개의", 49: "칸을"`
  - mapping_reason: "개의 칸을" (number of cells).

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
15. <src>여기 있는 이 </src> <tgt>是将</tgt>; start=15.00, end=16.00
16. <src>각각 의 </src> <tgt>这里的</tgt>; start=16.00, end=17.00
17. <src>칸 세 개의 </src> <tgt>每一个格子，也就是</tgt>; start=17.00, end=18.00
18. <src>칸을 </src> <tgt>这三个格子……</tgt>; start=18.00, end=18.40
```

- max_empty_window_count: 5


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
  1. 그림
  2. 을
  3. 그리
  4. 면서
  5. 카피할
  6. 때
  7. 머리
  8. 속에
  9. 기억
  10. 해두고
  11. 메모
  12. 해둔
  13. 표현
  14. 방법
  15. 을
  16. 그대로
  17. 실제
  18. 적용
  19. 하면서
  20. 그림
  21. 을
  22. 그립
  23. 니다.
  24. 그러면
  25. 그림
  26. 그리
  27. 는
  28. 실력
  29. 이
  30. 빠르
  31. 게
  32. 좋아집니다.

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
  - source_tokens: `5: "카피할", 6: "때"`
  - mapping_reason: "카피할" (copy) + "때" (when)

* target[1]: "while drawing"
  - source_tokens: `3: "그리", 4: "면서"`
  - mapping_reason: "그리" (draw) + "면서" (while)

* target[2]: "my own pictures,"
  - source_tokens: `0: "자기", 1: "그림", 2: "을"`
  - mapping_reason: "자기" (my own) + "그림" (pictures) + object marker "을"

* target[3]: "I directly apply"
  - source_tokens: `16: "그대로", 17: "실제", 18: "적용", 19: "하면서"`
  - mapping_reason: "그대로" (directly/as is) + "실제" (actual/in practice) + "적용" (apply) + "하면서" (while/as I do)

* target[4]: "the techniques"
  - source_tokens: `13: "표현", 14: "방법", 15: "을"`
  - mapping_reason: "표현" (expression) + "방법" (method/technique) + object marker "을"

* target[5]: "I've memorized"
  - source_tokens: `7: "머리", 8: "속에", 9: "기억", 10: "해두고"`
  - mapping_reason: "머리 속에" (in my head) + "기억" (memory) + "해두고" (have stored/memorized)

* target[6]: "or noted down."
  - source_tokens: `11: "메모", 12: "해둔"`
  - mapping_reason: "메모" (note) + "해둔" (have done/noted down)

* target[7]: "This helps improve"
  - source_tokens: `24: "그러면", 27: "는", 28: "실력", 32: "좋아집니다."`
  - mapping_reason: "그러면" (then/this) + "실력" (skill) + "좋아집니다" (improves)

* target[8]: "my drawing skills"
  - source_tokens: `25: "그림", 26: "그리", 28: "실력", 29: "이"`
  - mapping_reason: "그림" (drawing) + "그리" (draw) + "실력" (skill)

* target[9]: "quickly."
  - source_tokens: `30: "빠르", 31: "게"`
  - mapping_reason: "빠르" (fast) + "게" (adverbial marker/quickly)

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
=== KO_GxLlh9Eui8c_W000249 ===

source:
- language: Korean
- transcription: 돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.
- source_tokens:
  0. 돌파
  1. 하고
  2. 승리
  3. 해야
  4. 한다.
  5. 다만
  6. 배도에
  7. 죄까지
  8. 갈
  9. 수
  10. 있으니
  11. 하나님
  12. 앞에서
  13. 늘
  14. 겸손
  15. 하라는
  16. 메시지
  17. 를
  18. 전하
  19. 는
  20. 대신
  21. 진짜
  22. 거듭
  23. 난
  24. 성도
  25. 도
  26. 진짜
  27. 지옥
  28. 에
  29. 아주
  30. 잘
  31. 가니까
  32. 대부분
  33. 지옥
  34. 가니까.

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
  - source_tokens: `0: "돌파", 1: "하고"`
  - mapping_reason: "돌파" (breakthrough) + "하고" (and/conjunctive)
* target[1]: "勝利しなければならない。"
  - source_tokens: `2: "승리", 3: "해야", 4: "한다."`
  - mapping_reason: "승리" (victory) + "해야 한다" (must do)
* target[2]: "ただ、"
  - source_tokens: `5: "다만"`
  - mapping_reason: "다만" (however/only)
* target[3]: "背教の罪に"
  - source_tokens: `6: "배도에", 7: "죄까지"`
  - mapping_reason: "배도" (apostasy) + "죄" (sin)
* target[4]: "至る可能性もある。"
  - source_tokens: `8: "갈", 9: "수", 10: "있으니"`
  - mapping_reason: "갈 수 있으니" (can reach/go to)
* target[5]: "だから"
  - source_tokens: `10: "있으니"`
  - mapping_reason: "있으니" (implies consequence/so)
* target[6]: "「神の前で"
  - source_tokens: `11: "하나님", 12: "앞에서"`
  - mapping_reason: "하나님 앞에서" (before God)
* target[7]: "常に謙遜であるべきだ」"
  - source_tokens: `13: "늘", 14: "겸손", 15: "하라는"`
  - mapping_reason: "늘 겸손 하라는" (to be always humble)
* target[8]: "というメッセージを"
  - source_tokens: `16: "메시지", 17: "를"`
  - mapping_reason: "메시지를" (message + object marker)
* target[9]: "伝える代わりに、"
  - source_tokens: `18: "전하", 19: "는", 20: "대신"`
  - mapping_reason: "전하는 대신" (instead of conveying)
* target[10]: "本当に"
  - source_tokens: `21: "진짜"`
  - mapping_reason: "진짜" (truly/really)
* target[11]: "生まれ変わった聖徒も"
  - source_tokens: `22: "거듭", 23: "난", 24: "성도", 25: "도"`
  - mapping_reason: "거듭난 성도도" (also born-again saints)
* target[12]: "本当に"
  - source_tokens: `26: "진짜"`
  - mapping_reason: "진짜" (truly/really)
* target[13]: "地獄にとてもよく行く。"
  - source_tokens: `27: "지옥", 28: "에", 29: "아주", 30: "잘", 31: "가니까"`
  - mapping_reason: "지옥에 아주 잘 가니까" (go to hell very well)
* target[14]: "なぜなら、"
  - source_tokens: `31: "가니까"`
  - mapping_reason: "가니까" (because)
* target[15]: "ほとんどの人が"
  - source_tokens: `32: "대부분"`
  - mapping_reason: "대부분" (most people)
* target[16]: "地獄に行くからだ。"
  - source_tokens: `33: "지옥", 34: "가니까."`
  - mapping_reason: "지옥 가니까" (because they go to hell)

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
  3. 우리
  4. 가
  5. 뉴욕
  6. 에
  7. 살고
  8. 있으니까
  9. 좀
  10. 뉴욕
  11. 과
  12. 뉴저지
  13. 지역
  14. 의
  15. 유명
  16. 한
  17. 곳을
  18. 소개
  19. 해드릴
  20. 수도
  21. 있어요.
  22. 그렇
  23. 죠,
  24. 그렇
  25. 죠.
  26. 직접
  27. 그
  28. 현장
  29. 에
  30. 가서
  31. 저희
  32. 들이
  33. 이제
  34. 체험
  35. 도
  36. 해보고
  37. 소개
  38. 도
  39. 해드리고
  40. 그런
  41. 프로그램
  42. 도
  43. 만들
  44. 기획
  45. 이고요.
  46. 어
  47. 뉴욕
  48. 미니
  49. 스에
  50. 대한
  51. 설명
  52. 을
  53. 좀
  54. 해주시죠.

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
  - source_tokens: `0: "그리고", 1: "아", 8: "있으니까"`
  - mapping_reason: Connective "그리고", filler "아", and causal suffix "있으니까".
* target[1]: "we live in"
  - source_tokens: `3: "우리", 4: "가", 7: "살고"`
  - mapping_reason: Subject "우리" and verb "살고".
* target[2]: "New York,"
  - source_tokens: `5: "뉴욕", 6: "에"`
  - mapping_reason: Location "뉴욕" and particle "에".
* target[3]: "we could also introduce"
  - source_tokens: `9: "좀", 18: "소개", 19: "해드릴", 20: "수도", 21: "있어요."`
  - mapping_reason: Modal potential "수도 있어요", hedge "좀", and verb "소개해드릴".
* target[4]: "some famous spots"
  - source_tokens: `15: "유명", 16: "한", 17: "곳을"`
  - mapping_reason: Adjective "유명한" and noun "곳을".
* target[5]: "in the New York"
  - source_tokens: `10: "뉴욕"`
  - mapping_reason: Specific location "뉴욕".
* target[6]: "and New Jersey area."
  - source_tokens: `11: "과", 12: "뉴저지", 13: "지역", 14: "의"`
  - mapping_reason: Conjunction "과", noun "뉴저지", and "지역의".
* target[7]: "Right, exactly."
  - source_tokens: `22: "그렇", 23: "죠,", 24: "그렇", 25: "죠."`
  - mapping_reason: Affirmation/agreement "그렇죠".
* target[8]: "We're planning to"
  - source_tokens: `43: "만들", 44: "기획", 45: "이고요."`
  - mapping_reason: Planning/intention "기획이고요".
* target[9]: "make a program."
  - source_tokens: `41: "프로그램", 42: "도"`
  - mapping_reason: Object "프로그램".
* target[10]: "We'll actually go to the sites,"
  - source_tokens: `26: "직접", 27: "그", 28: "현장", 29: "에", 30: "가서"`
  - mapping_reason: Adverb "직접", location "현장에", and verb "가서".
* target[11]: "experience them ourselves,"
  - source_tokens: `31: "저희", 32: "들이", 34: "체험", 35: "도", 36: "해보고"`
  - mapping_reason: Subject "저희들이", verb "체험해보고".
* target[12]: "and introduce them to you."
  - source_tokens: `33: "이제", 37: "소개", 38: "도", 39: "해드리고"`
  - mapping_reason: Verb "소개해드리고".
* target[13]: "Uh, could you explain"
  - source_tokens: `46: "어", 51: "설명", 54: "해주시죠."`
  - mapping_reason: Filler "어", noun "설명", and request "해주시죠".
* target[14]: "what ' New York Minis '"
  - source_tokens: `47: "뉴욕", 48: "미니", 49: "스에", 50: "대한"`
  - mapping_reason: Topic "뉴욕 미니스에 대한".
* target[15]: "is?"
  - source_tokens: `52: "을"`
  - mapping_reason: Object particle marking the target of explanation.

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
=== KO_G7RmVIWMrHo_W000018 ===

source:
- language: Korean
- transcription: 제가 좀 직관적으로 이해하셔야 될 부분의 측면이 있어서 여러분들이 잘 한번 보시고 아주 이렇게 하니까 행이 병합이 되는구나 이렇게 느끼셨으면 좋겠습니다. 말로 하려니까 너무 힘드네요. 자, 그다음 여기는 합계라고 되어 있는 부분은 여기 있는 이 각각의 칸 세 개의 칸을
- source_tokens:
  0. 제가
  1. 좀
  2. 직관적으로
  3. 이해
  4. 하셔야
  5. 될
  6. 부분
  7. 의
  8. 측면
  9. 이
  10. 있어서
  11. 여러분
  12. 들이
  13. 잘
  14. 한번
  15. 보시고
  16. 아주
  17. 이렇게
  18. 하니까
  19. 행이
  20. 병합이
  21. 되는구나
  22. 이렇게
  23. 느끼
  24. 셨으면
  25. 좋겠습니다.
  26. 말로
  27. 하려니까
  28. 너무
  29. 힘드
  30. 네요.
  31. 자,
  32. 그다음
  33. 여기
  34. 는
  35. 합계
  36. 라고
  37. 되어
  38. 있는
  39. 부분
  40. 은
  41. 여기
  42. 있는
  43. 이
  44. 각각
  45. 의
  46. 칸
  47. 세
  48. 개의
  49. 칸을

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
  - mapping_reason: Direct lexical translation.
* target[1]: "理解していただきたい"
  - source_tokens: `3: "이해", 4: "하셔야", 5: "될"`
  - mapping_reason: Semantic equivalent of "understanding that you should do".
* target[2]: "点が"
  - source_tokens: `6: "부분", 7: "의", 8: "측면"`
  - mapping_reason: "부분의 측면" corresponds to "point/aspect".
* target[3]: "ありまして、"
  - source_tokens: `9: "이", 10: "있어서"`
  - mapping_reason: Existence/causal connection.
* target[4]: "皆さん"
  - source_tokens: `11: "여러분", 12: "들이"`
  - mapping_reason: Direct address.
* target[5]: "よく"
  - source_tokens: `13: "잘"`
  - mapping_reason: Adverbial modifier.
* target[6]: "見て、"
  - source_tokens: `14: "한번", 15: "보시고"`
  - mapping_reason: "한번 보시고" translates to "take a look".
* target[7]: "「こうやると"
  - source_tokens: `16: "아주", 17: "이렇게", 18: "하니까"`
  - mapping_reason: Explains the action taken.
* target[8]: "行が"
  - source_tokens: `19: "행이"`
  - mapping_reason: Direct noun translation.
* target[9]: "結合されるんだな」"
  - source_tokens: `20: "병합이", 21: "되는구나"`
  - mapping_reason: "병합" (merging) -> "結合" (merging).
* target[10]: "と"
  - source_tokens: `22: "이렇게"`
  - mapping_reason: Quotative marker for the preceding thought.
* target[11]: "感じていただければ"
  - source_tokens: `23: "느끼", 24: "셨으면"`
  - mapping_reason: Verb expressing feeling/realization.
* target[12]: "と思います。"
  - source_tokens: `25: "좋겠습니다."`
  - mapping_reason: Expresses speaker's desire/hope.
* target[13]: "言葉で"
  - source_tokens: `26: "말로"`
  - mapping_reason: Literal translation.
* target[14]: "説明する"
  - source_tokens: `27: "하려니까"`
  - mapping_reason: Contextual translation of "trying to do (by speaking)".
* target[15]: "のは"
  - source_tokens: `27: "하려니까"`
  - mapping_reason: Nominalizer for the action of speaking.
* target[16]: "本当に"
  - source_tokens: `28: "너무"`
  - mapping_reason: Intensifier.
* target[17]: "難しい"
  - source_tokens: `29: "힘드"`
  - mapping_reason: Adjective meaning difficult.
* target[18]: "ですね。"
  - source_tokens: `30: "네요."`
  - mapping_reason: Sentence ending particle.
* target[19]: "さて、"
  - source_tokens: `31: "자,"`
  - mapping_reason: Discourse marker.
* target[20]: "次は"
  - source_tokens: `32: "그다음"`
  - mapping_reason: Temporal/spatial sequence.
* target[21]: "「合計」と"
  - source_tokens: `35: "합계", 36: "라고"`
  - mapping_reason: Noun and quotation marker.
* target[22]: "書かれている"
  - source_tokens: `37: "되어", 38: "있는"`
  - mapping_reason: Passive state description.
* target[23]: "部分"
  - source_tokens: `39: "부분"`
  - mapping_reason: Direct noun translation.
* target[24]: "ですが、"
  - source_tokens: `40: "은"`
  - mapping_reason: Topic marker indicating contrast/transition.
* target[25]: "ここに"
  - source_tokens: `33: "여기", 34: "는", 41: "여기"`
  - mapping_reason: Locative reference.
* target[26]: "ある"
  - source_tokens: `42: "있는"`
  - mapping_reason: Existence verb.
* target[27]: "それぞれのマス、"
  - source_tokens: `43: "이", 44: "각각", 45: "의", 46: "칸"`
  - mapping_reason: "each cell".
* target[28]: "この3つのマス"
  - source_tokens: `47: "세", 48: "개의", 49: "칸을"`
  - mapping_reason: "three cells".
* target[29]: "を……"
  - source_tokens: `49: "칸을"`
  - mapping_reason: Object marker.

result:
```html
0. <src>제가 좀 직관적으로 </src> <tgt>直感的に</tgt>; start=0.00, end=1.00
1. <src>이해 하셔야 될 </src> <tgt>理解していただきたい</tgt>; start=1.00, end=2.00
2. <src>부분 의 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>측면 이 있어서 </src> <tgt>点がありまして、</tgt>; start=3.00, end=4.00
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
=== KO_E9GzA6TOlV4_W000007 ===

source:
- language: Korean
- transcription: 일단 배그는 파밍이 제일 중요합니다, 여러분. 파밍을 열심히 해주세요. 어 발소리 난다. 어 당황한 척하면서 이렇게 파밍해주면 됩니다, 여러분.
- source_tokens:
  0. 일단
  1. 배그는
  2. 파밍이
  3. 제일
  4. 중요
  5. 합니다,
  6. 여러분.
  7. 파밍을
  8. 열심히
  9. 해주세요.
  10. 어
  11. 발소리
  12. 난다.
  13. 어
  14. 당황
  15. 한
  16. 척하
  17. 면서
  18. 이렇게
  19. 파밍해주면
  20. 됩니다,
  21. 여러분.

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
  - mapping_reason: Discourse marker indicating priority.
* target[1]: "大家，"
  - source_tokens: `6: "여러분."`
  - mapping_reason: Address term for the audience.
* target[2]: "在绝地求生里"
  - source_tokens: `1: "배그는"`
  - mapping_reason: Topic marker indicating the game context.
* target[3]: "搜集物资"
  - source_tokens: `2: "파밍이"`
  - mapping_reason: Subject of the sentence ("farming").
* target[4]: "最重要。"
  - source_tokens: `3: "제일", 4: "중요", 5: "합니다,"`
  - mapping_reason: Predicate expressing superlative importance.
* target[5]: "请"
  - source_tokens: `9: "해주세요."`
  - mapping_reason: Politeness/imperative marker.
* target[6]: "努力搜集物资。"
  - source_tokens: `7: "파밍을", 8: "열심히", 9: "해주세요."`
  - mapping_reason: Core action and modifier.
* target[7]: "哦，"
  - source_tokens: `10: "어"`
  - mapping_reason: Interjection.
* target[8]: "有脚步声。"
  - source_tokens: `11: "발소리", 12: "난다."`
  - mapping_reason: Observation of sound.
* target[9]: "哦，"
  - source_tokens: `13: "어"`
  - mapping_reason: Interjection.
* target[10]: "大家，"
  - source_tokens: `21: "여러분."`
  - mapping_reason: Address term for the audience.
* target[11]: "装作很慌张的样子，"
  - source_tokens: `14: "당황", 15: "한", 16: "척하", 17: "면서"`
  - mapping_reason: Manner/adverbial clause describing the action.
* target[12]: "像这样"
  - source_tokens: `18: "이렇게"`
  - mapping_reason: Manner reference.
* target[13]: "搜集物资"
  - source_tokens: `19: "파밍해주면"`
  - mapping_reason: Core action.
* target[14]: "就行了。"
  - source_tokens: `19: "파밍해주면", 20: "됩니다,"`
  - mapping_reason: Modal expression indicating sufficiency.

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
=== KO_GxLlh9Eui8c_W000249 ===

source:
- language: Korean
- transcription: 돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.
- source_tokens:
  0. 돌파
  1. 하고
  2. 승리
  3. 해야
  4. 한다.
  5. 다만
  6. 배도에
  7. 죄까지
  8. 갈
  9. 수
  10. 있으니
  11. 하나님
  12. 앞에서
  13. 늘
  14. 겸손
  15. 하라는
  16. 메시지
  17. 를
  18. 전하
  19. 는
  20. 대신
  21. 진짜
  22. 거듭
  23. 난
  24. 성도
  25. 도
  26. 진짜
  27. 지옥
  28. 에
  29. 아주
  30. 잘
  31. 가니까
  32. 대부분
  33. 지옥
  34. 가니까.

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
  - source_tokens: `3: "해야", 4: "한다."`
  - mapping_reason: Expresses obligation (must).
* target[1]: "break through"
  - source_tokens: `0: "돌파", 1: "하고"`
  - mapping_reason: Core action of breaking through.
* target[2]: "and be victorious."
  - source_tokens: `2: "승리"`
  - mapping_reason: Core action of being victorious.
* target[3]: "But we can even"
  - source_tokens: `5: "다만", 9: "수", 10: "있으니"`
  - mapping_reason: Contrastive conjunction and possibility.
* target[4]: "fall into"
  - source_tokens: `8: "갈"`
  - mapping_reason: Motion towards/falling into a state.
* target[5]: "the sin of"
  - source_tokens: `7: "죄까지"`
  - mapping_reason: Identifying the state as sin.
* target[6]: "apostasy."
  - source_tokens: `6: "배도에"`
  - mapping_reason: The specific state of apostasy.
* target[7]: "So instead of"
  - source_tokens: `20: "대신"`
  - mapping_reason: Contrastive discourse marker.
* target[8]: "just telling people to"
  - source_tokens: `15: "하라는", 16: "메시지", 17: "를", 18: "전하", 19: "는"`
  - mapping_reason: Delivering the message to people.
* target[9]: "always be humble"
  - source_tokens: `13: "늘", 14: "겸손"`
  - mapping_reason: Content of the message.
* target[10]: "before God,"
  - source_tokens: `11: "하나님", 12: "앞에서"`
  - mapping_reason: Location/context of humility.
* target[11]: "we need to"
  - source_tokens: `3: "해야", 4: "한다."`
  - mapping_reason: Implicit obligation/necessity introduced by the speaker.
* target[12]: "recognize this:"
  - source_tokens: `16: "메시지"`
  - mapping_reason: Shifting from the previous message to the new realization.
* target[13]: "even truly born- again believers"
  - source_tokens: `21: "진짜", 22: "거듭", 23: "난", 24: "성도", 25: "도"`
  - mapping_reason: Subject of the clause.
* target[14]: "can very easily"
  - source_tokens: `26: "진짜", 29: "아주", 30: "잘"`
  - mapping_reason: Modifiers of the action.
* target[15]: "go to hell."
  - source_tokens: `27: "지옥", 28: "에", 31: "가니까"`
  - mapping_reason: Predicate of the clause.
* target[16]: "Because most people"
  - source_tokens: `32: "대부분"`
  - mapping_reason: Causal explanation and subject.
* target[17]: "go to hell."
  - source_tokens: `33: "지옥", 34: "가니까."`
  - mapping_reason: Predicate of the causal clause.

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
  3. 우리
  4. 가
  5. 뉴욕
  6. 에
  7. 살고
  8. 있으니까
  9. 좀
  10. 뉴욕
  11. 과
  12. 뉴저지
  13. 지역
  14. 의
  15. 유명
  16. 한
  17. 곳을
  18. 소개
  19. 해드릴
  20. 수도
  21. 있어요.
  22. 그렇
  23. 죠,
  24. 그렇
  25. 죠.
  26. 직접
  27. 그
  28. 현장
  29. 에
  30. 가서
  31. 저희
  32. 들이
  33. 이제
  34. 체험
  35. 도
  36. 해보고
  37. 소개
  38. 도
  39. 해드리고
  40. 그런
  41. 프로그램
  42. 도
  43. 만들
  44. 기획
  45. 이고요.
  46. 어
  47. 뉴욕
  48. 미니
  49. 스에
  50. 대한
  51. 설명
  52. 을
  53. 좀
  54. 해주시죠.

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
  - mapping_reason: Discourse connective "And".
* target[1]: "因为"
  - source_tokens: `8: "있으니까"`
  - mapping_reason: Causality marker.
* target[2]: "我们住在纽约嘛，"
  - source_tokens: `3: "우리", 4: "가", 5: "뉴욕", 6: "에", 7: "살고"`
  - mapping_reason: Subject "we" and location "living in New York".
* target[3]: "所以"
  - source_tokens: `8: "있으니까"`
  - mapping_reason: Resultative marker derived from the "because" clause.
* target[4]: "也可以"
  - source_tokens: `9: "좀", 20: "수도", 21: "있어요"`
  - mapping_reason: Possibility/suggestion marker.
* target[5]: "给大家介绍"
  - source_tokens: `18: "소개", 19: "해드릴"`
  - mapping_reason: Action of introducing to others.
* target[6]: "一些纽约和新泽西"
  - source_tokens: `10: "뉴욕", 11: "과", 12: "뉴저지", 13: "지역"`
  - mapping_reason: Location scope.
* target[7]: "有名的景点。"
  - source_tokens: `15: "유명", 16: "한", 17: "곳을"`
  - mapping_reason: Object of introduction (famous places).
* target[8]: "对，"
  - source_tokens: `22: "그렇", 23: "죠"`
  - mapping_reason: Affirmation.
* target[9]: "没错。"
  - source_tokens: `24: "그렇", 25: "죠"`
  - mapping_reason: Affirmation.
* target[10]: "我们还打算"
  - source_tokens: `31: "저희", 32: "들이", 43: "만들", 44: "기획", 45: "이고요"`
  - mapping_reason: Subject "we" and intent/plan.
* target[11]: "做一些节目，"
  - source_tokens: `41: "프로그램", 42: "도"`
  - mapping_reason: Content of the plan (program).
* target[12]: "亲自去现场体验，"
  - source_tokens: `26: "직접", 28: "현장", 29: "에", 30: "가서", 34: "체험", 35: "도", 36: "해보고"`
  - mapping_reason: Description of the activity.
* target[13]: "然后"
  - source_tokens: `33: "이제"`
  - mapping_reason: Sequence marker.
* target[14]: "给大家介绍。"
  - source_tokens: `37: "소개", 38: "도", 39: "해드리고"`
  - mapping_reason: Second part of the activity (introducing).
* target[15]: "呃，"
  - source_tokens: `46: "어"`
  - mapping_reason: Filler.
* target[16]: "那"
  - source_tokens: `50: "대한"`
  - mapping_reason: Topic transition.
* target[17]: "请介绍一下"
  - source_tokens: `51: "설명", 52: "을", 53: "좀", 54: "해주시죠"`
  - mapping_reason: Request for introduction.
* target[18]: "“纽约迷你”吧。"
  - source_tokens: `47: "뉴욕", 48: "미니", 49: "스에"`
  - mapping_reason: Topic of the request.

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
14. <src>만들 기획 이고요. 어 </src> <tgt>我们还打算做一些节目，亲自去现场体验，然后给大家介绍。呃，</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>뉴욕 미니 스에 대한 설명 을 </src> <tgt>那</tgt>; start=16.00, end=17.00
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
  0. 유튜브
  1. 에
  2. 그림
  3. 을
  4. 올리
  5. 는
  6. 고수
  7. 들이나
  8. 거리
  9. 에서
  10. 그림
  11. 을
  12. 그리
  13. 는
  14. 사람
  15. 들을
  16. 보면
  17. 별로
  18. 힘들
  19. 이지
  20. 않고
  21. 대충
  22. 그려
  23. 도
  24. 보기
  25. 좋게
  26. 완성
  27. 되는
  28. 것
  29. 같은데
  30. 나는
  31. 언제
  32. 좀
  33. 저렇게
  34. 그림
  35. 을
  36. 그릴
  37. 수
  38. 있을까
  39. 하는
  40. 생각
  41. 을
  42. 하게
  43. 됩니다.

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
  - source_tokens: `16: "보면"`
  - mapping_reason: The verb "보면" (see) acts as the conditional/temporal frame for the observation.
* target[1]: "the pros"
  - source_tokens: `6: "고수", 7: "들이나"`
  - mapping_reason: "고수" means pros/experts; "들이나" is the plural marker and conjunction.
* target[2]: "on YouTube"
  - source_tokens: `0: "유튜브", 1: "에"`
  - mapping_reason: Location "유튜브" plus locative particle "에".
* target[3]: "or people"
  - source_tokens: `14: "사람", 15: "들을"`
  - mapping_reason: "사람" (people) with plural/object marker.
* target[4]: "drawing on the street,"
  - source_tokens: `8: "거리", 9: "에서", 10: "그림", 11: "을", 12: "그리", 13: "는"`
  - mapping_reason: Describes the activity ("그림을 그리는") at a location ("거리에서").
* target[5]: "it seems like"
  - source_tokens: `29: "같은데"`
  - mapping_reason: "같은데" provides the appearance/seeming aspect.
* target[6]: "they don't even try"
  - source_tokens: `17: "별로", 18: "힘들", 19: "이지", 20: "않고"`
  - mapping_reason: "별로 힘들이지 않고" translates to not trying hard.
* target[7]: "that hard–"
  - source_tokens: `17: "별로", 18: "힘들"`
  - mapping_reason: "별로 힘들" conveys the degree of effort.
* target[8]: "even a rough sketch"
  - source_tokens: `21: "대충", 22: "그려", 23: "도"`
  - mapping_reason: "대충 그려도" means even if drawn roughly/sketch-like.
* target[9]: "turns out"
  - source_tokens: `26: "완성", 27: "되는"`
  - mapping_reason: "완성되는" (becoming completed/turning out).
* target[10]: "looking great."
  - source_tokens: `24: "보기", 25: "좋게"`
  - mapping_reason: "보기 좋게" means looking good/great.
* target[11]: "Then I"
  - source_tokens: `30: "나는"`
  - mapping_reason: Subject "나는" marks the shift to the speaker's internal state.
* target[12]: "find myself"
  - source_tokens: `42: "하게", 43: "됩니다."`
  - mapping_reason: The auxiliary structure "하게 됩니다" indicates the speaker falling into a state of thought.
* target[13]: "wondering when"
  - source_tokens: `31: "언제", 39: "하는", 40: "생각", 41: "을"`
  - mapping_reason: "언제 ... 하는 생각을" captures the wondering about the timing.
* target[14]: "I'll ever"
  - source_tokens: `32: "좀"`
  - mapping_reason: "좀" acts as an adverbial intensifier/wishful marker here.
* target[15]: "be able to"
  - source_tokens: `37: "수", 38: "있을까"`
  - mapping_reason: "수 있을까" expresses potential/ability.
* target[16]: "draw like that."
  - source_tokens: `33: "저렇게", 34: "그림", 35: "을", 36: "그릴"`
  - mapping_reason: "저렇게 그림을 그릴" means to draw in that manner.

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
=== KO_G1hDgTWHSC8_W000002 ===

source:
- language: Korean
- transcription: 유튜브에 그림을 올리는 고수들이나 거리에서 그림을 그리는 사람들을 보면 별로 힘들이지 않고 대충 그려도 보기 좋게 완성되는 것 같은데 나는 언제 좀 저렇게 그림을 그릴 수 있을까 하는 생각을 하게 됩니다.
- source_tokens:
  0. 유튜브
  1. 에
  2. 그림
  3. 을
  4. 올리
  5. 는
  6. 고수
  7. 들이나
  8. 거리
  9. 에서
  10. 그림
  11. 을
  12. 그리
  13. 는
  14. 사람
  15. 들을
  16. 보면
  17. 별로
  18. 힘들
  19. 이지
  20. 않고
  21. 대충
  22. 그려
  23. 도
  24. 보기
  25. 좋게
  26. 완성
  27. 되는
  28. 것
  29. 같은데
  30. 나는
  31. 언제
  32. 좀
  33. 저렇게
  34. 그림
  35. 을
  36. 그릴
  37. 수
  38. 있을까
  39. 하는
  40. 생각
  41. 을
  42. 하게
  43. 됩니다.

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
  - source_tokens: `16: "보면"`
  - mapping_reason: "보면" (seeing/watching) corresponds to the start of the observation process.
* target[1]: "在YouTube上发画的"
  - source_tokens: `0: "유튜브", 1: "에", 2: "그림", 3: "을", 4: "올리", 5: "는"`
  - mapping_reason: Covers the platform and the action of uploading drawings.
* target[2]: "高手，"
  - source_tokens: `6: "고수"`
  - mapping_reason: Direct translation of "고수" (expert/master).
* target[3]: "或者"
  - source_tokens: `7: "들이나"`
  - mapping_reason: "이나" functions as the conjunction "or".
* target[4]: "在街头画画的"
  - source_tokens: `8: "거리", 9: "에서", 10: "그림", 11: "을", 12: "그리", 13: "는"`
  - mapping_reason: Covers the location (street) and the action (drawing).
* target[5]: "人，"
  - source_tokens: `14: "사람", 15: "들을"`
  - mapping_reason: Direct translation of "사람들" (people).
* target[6]: "总觉得"
  - source_tokens: `16: "보면"`
  - mapping_reason: "보면" sets the context for the following perception/thought.
* target[7]: "他们好像"
  - source_tokens: `28: "것", 29: "같은데"`
  - mapping_reason: "것 같은데" indicates the speaker's perception/supposition.
* target[8]: "不怎么费力，"
  - source_tokens: `17: "별로", 18: "힘들", 19: "이지", 20: "않고"`
  - mapping_reason: Direct translation of "별로 힘들지 않고" (not particularly difficult).
* target[9]: "随手一画"
  - source_tokens: `21: "대충", 22: "그려"`
  - mapping_reason: "대충 그려" (drawing roughly/casually).
* target[10]: "就很好看。"
  - source_tokens: `23: "도", 24: "보기", 25: "좋게", 26: "완성", 27: "되는"`
  - mapping_reason: "보기 좋게 완성되는" (completing nicely).
* target[11]: "我就在想，"
  - source_tokens: `30: "나는", 39: "하는", 40: "생각", 41: "을", 42: "하게", 43: "됩니다."`
  - mapping_reason: The speaker's reflection ("나는 ... 생각을 하게 됩니다").
* target[12]: "我什么时候"
  - source_tokens: `31: "언제"`
  - mapping_reason: Direct translation of "언제" (when).
* target[13]: "也能"
  - source_tokens: `32: "좀", 37: "수", 38: "있을까"`
  - mapping_reason: Expresses the potential/capability ("수 있을까").
* target[14]: "画成那样呢。"
  - source_tokens: `33: "저렇게", 34: "그림", 35: "을", 36: "그릴"`
  - mapping_reason: "저렇게 그림을 그릴" (drawing like that).

result:
```html
0. <src>유튜브 에 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>그림 을 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>올리 는 고수 들이나 </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>거리 에서 그림 을 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>그리 는 사람 들을 보면 </src> <tgt>看到那些在YouTube上发画的高手，或者在街头画画的人，总觉得</tgt>; start=4.00, end=5.00
5. <src>별로 </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>힘들 이지 않고 대충 그려 도 </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>보기 좋게 </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>완성 되는 것 같은데 </src> <tgt>他们好像不怎么费力，随手一画就很好看。</tgt>; start=8.00, end=9.00
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
=== KO_G1hDgTWHSC8_W000002 ===

source:
- language: Korean
- transcription: 유튜브에 그림을 올리는 고수들이나 거리에서 그림을 그리는 사람들을 보면 별로 힘들이지 않고 대충 그려도 보기 좋게 완성되는 것 같은데 나는 언제 좀 저렇게 그림을 그릴 수 있을까 하는 생각을 하게 됩니다.
- source_tokens:
  0. 유튜브
  1. 에
  2. 그림
  3. 을
  4. 올리
  5. 는
  6. 고수
  7. 들이나
  8. 거리
  9. 에서
  10. 그림
  11. 을
  12. 그리
  13. 는
  14. 사람
  15. 들을
  16. 보면
  17. 별로
  18. 힘들
  19. 이지
  20. 않고
  21. 대충
  22. 그려
  23. 도
  24. 보기
  25. 좋게
  26. 완성
  27. 되는
  28. 것
  29. 같은데
  30. 나는
  31. 언제
  32. 좀
  33. 저렇게
  34. 그림
  35. 을
  36. 그릴
  37. 수
  38. 있을까
  39. 하는
  40. 생각
  41. 을
  42. 하게
  43. 됩니다.

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
  - source_tokens: `0: "유튜브", 1: "에"`
  - mapping_reason: YouTube platform location.
* target[1]: "絵を"
  - source_tokens: `2: "그림", 3: "을"`
  - mapping_reason: Object of uploading.
* target[2]: "上げてる"
  - source_tokens: `4: "올리", 5: "는"`
  - mapping_reason: Action of uploading.
* target[3]: "達人とか、"
  - source_tokens: `6: "고수", 7: "들이나"`
  - mapping_reason: Experts/masters and the connective "or/and".
* target[4]: "街で"
  - source_tokens: `8: "거리", 9: "에서"`
  - mapping_reason: Street location.
* target[5]: "絵を"
  - source_tokens: `10: "그림", 11: "을"`
  - mapping_reason: Object of drawing.
* target[6]: "描いてる"
  - source_tokens: `12: "그리", 13: "는"`
  - mapping_reason: Action of drawing.
* target[7]: "人を"
  - source_tokens: `14: "사람", 15: "들을"`
  - mapping_reason: People being observed.
* target[8]: "見ると、"
  - source_tokens: `16: "보면"`
  - mapping_reason: Conditional observation.
* target[9]: "あまり"
  - source_tokens: `17: "별로"`
  - mapping_reason: Negation modifier (not much).
* target[10]: "力入れずに"
  - source_tokens: `18: "힘들", 19: "이지", 20: "않고"`
  - mapping_reason: Without putting in effort.
* target[11]: "ざっと描いてる"
  - source_tokens: `21: "대충", 22: "그려"`
  - mapping_reason: Drawing roughly.
* target[12]: "ように見える"
  - source_tokens: `29: "같은데"`
  - mapping_reason: Appearance/impression.
* target[13]: "けど、"
  - source_tokens: `29: "같은데"`
  - mapping_reason: Contrastive conjunction.
* target[14]: "それでも"
  - source_tokens: `23: "도"`
  - mapping_reason: Concessive meaning.
* target[15]: "見栄えよく"
  - source_tokens: `24: "보기", 25: "좋게"`
  - mapping_reason: Good appearance.
* target[16]: "仕上がってるんですよね。"
  - source_tokens: `26: "완성", 27: "되는", 28: "것"`
  - mapping_reason: Completion of the drawing.
* target[17]: "で、"
  - source_tokens: `43: "됩니다."`
  - mapping_reason: Discourse connective linking the observation to the personal thought.
* target[18]: "自分は"
  - source_tokens: `30: "나는"`
  - mapping_reason: Subject of the thought.
* target[19]: "いつになったら"
  - source_tokens: `31: "언제", 32: "좀"`
  - mapping_reason: Time query.
* target[20]: "あんなふうに"
  - source_tokens: `33: "저렇게"`
  - mapping_reason: Manner of action.
* target[21]: "描けるようになるんだろう、"
  - source_tokens: `34: "그림", 35: "을", 36: "그릴", 37: "수", 38: "있을까"`
  - mapping_reason: Ability to draw.
* target[22]: "って思っちゃいます。"
  - source_tokens: `39: "하는", 40: "생각", 41: "을", 42: "하게", 43: "됩니다."`
  - mapping_reason: The act of thinking.

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
  6. 서로
  7. 까지
  8. 뜯고
  9. 싸움
  10. 을
  11. 해야
  12. 만이
  13. 되는
  14. 사람
  15. 이잖아.
  16. 그러면
  17. 어떻게
  18. 이제
  19. 이게
  20. BJ
  21. 궁합은
  22. 어떻게
  23. 한
  24. 사람
  25. 이
  26. 어떻게
  27. 어?

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
  - source_tokens: `0: "악인네는", 1: "서로"`
  - mapping_reason: "악인네" (evil people) combined with "서로" (each other) establishes the subject context.
* target[1]: "互相要求对方"
  - source_tokens: `1: "서로", 2: "내놔", 3: "하니까"`
  - mapping_reason: "서로" (each other) + "내놔" (give it out/demand) + "하니까" (because they do).
* target[2]: "拿出来，"
  - source_tokens: `2: "내놔"`
  - mapping_reason: Direct realization of the verb "내놔".
* target[3]: "那"
  - source_tokens: `4: "그러면"`
  - mapping_reason: "그러면" functions as a discourse connective (then/so).
* target[4]: "他们不就是"
  - source_tokens: `13: "되는", 14: "사람", 15: "이잖아."`
  - mapping_reason: "사람이잖아" (they are people who are...) implies the identity/definition of the subject.
* target[5]: "那种"
  - source_tokens: `0: "악인네는"`
  - mapping_reason: "악인네" (that kind of evil people) defines the type referred to.
* target[6]: "非得互相撕扯、打架"
  - source_tokens: `6: "서로", 7: "까지", 8: "뜯고", 9: "싸움"`
  - mapping_reason: "서로" (each other) + "뜯고" (tear) + "싸움" (fight) + "까지" (even/to that extent).
* target[7]: "才能解决"
  - source_tokens: `11: "해야", 12: "만이"`
  - mapping_reason: "해야만이" (must do to succeed/resolve).
* target[8]: "的人吗？"
  - source_tokens: `13: "되는", 14: "사람", 15: "이잖아."`
  - mapping_reason: "되는 사람" (person who becomes/is) + question ending "이잖아".
* target[9]: "那"
  - source_tokens: `16: "그러면"`
  - mapping_reason: "그러면" as a discourse transition.
* target[10]: "现在"
  - source_tokens: `18: "이제"`
  - mapping_reason: "이제" (now).
* target[11]: "这个"
  - source_tokens: `19: "이게"`
  - mapping_reason: "이게" (this).
* target[12]: "BJ的相性啊，"
  - source_tokens: `20: "BJ", 21: "궁합은"`
  - mapping_reason: "BJ" + "궁합" (compatibility/chemistry).
* target[13]: "一个人"
  - source_tokens: `23: "한", 24: "사람", 25: "이"`
  - mapping_reason: "한 사람" (one person).
* target[14]: "怎么……？"
  - source_tokens: `22: "어떻게", 26: "어떻게", 27: "어?"`
  - mapping_reason: "어떻게" (how) + filler "어?".

result:
```html
0. <src>악인네는 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>서로 내놔 하니까 </src> <tgt>恶人之间互相要求对方拿出来，</tgt>; start=1.00, end=2.00
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
  status: failed_after_response
  reason: * target[5]
  - verdict: mapping_error
  - reason: "那种 (that kind of) refers to the type of people described previously (악인), not the head noun 사람 (person) which is handled later."
  - replace_source_tokens: 0: "악인네는"
  validation:
    scratchpad:
* target[0]: "恶人之间"
  - source_tokens: `0: "악인네는", 1: "서로"`
  - mapping_reason: "악인네는" (evil people) + "서로" (between/each other)

* target[1]: "互相要求对方"
  - source_tokens: `1: "서로", 2: "내놔", 3: "하니까"`
  - mapping_reason: "서로" (each other) + "내놔" (give it out) + "하니까" (because they say/demand)

* target[2]: "拿出来，"
  - source_tokens: `2: "내놔"`
  - mapping_reason: Direct translation of "내놔" (bring/give out)

* target[3]: "那"
  - source_tokens: `4: "그러면"`
  - mapping_reason: "그러면" (then/in that case)

* target[4]: "他们不就是"
  - source_tokens: `13: "되는", 14: "사람", 15: "이잖아."`
  - mapping_reason: "사람이잖아" (are people who...) implies "they are"

* target[5]: "那种"
  - source_tokens: `14: "사람"`
  - mapping_reason: "사람" (person/type)

* target[6]: "非得互相撕扯、打架"
  - source_tokens: `6: "서로", 7: "까지", 8: "뜯고", 9: "싸움"`
  - mapping_reason: "서로" (each other) + "뜯고" (tear/rip) + "싸움" (fight) + "까지" (even/to the extent of)

* target[7]: "才能解决"
  - source_tokens: `11: "해야", 12: "만이", 13: "되는"`
  - mapping_reason: "해야만이 되는" (must do to become/be resolved)

* target[8]: "的人吗？"
  - source_tokens: `14: "사람", 15: "이잖아."`
  - mapping_reason: "사람" (person) + "이잖아" (isn't it)

* target[9]: "那"
  - source_tokens: `16: "그러면"`
  - mapping_reason: "그러면" (then)

* target[10]: "现在"
  - source_tokens: `18: "이제"`
  - mapping_reason: "이제" (now)

* target[11]: "这个"
  - source_tokens: `19: "이게"`
  - mapping_reason: "이게" (this)

* target[12]: "BJ的相性啊，"
  - source_tokens: `20: "BJ", 21: "궁합은"`
  - mapping_reason: "BJ" + "궁합" (compatibility/chemistry)

* target[13]: "一个人"
  - source_tokens: `23: "한", 24: "사람", 25: "이"`
  - mapping_reason: "한 사람" (one person)

* target[14]: "怎么……？"
  - source_tokens: `17: "어떻게", 22: "어떻게", 26: "어떻게", 27: "어?"`
  - mapping_reason: "어떻게" (how) + "어?" (what/how)
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1, 2, 3]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [2]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [14]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [6, 7, 8, 9]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [11, 12, 13]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [14, 15]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [16]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [20, 21]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [17, 22, 26, 27]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== KO_G7RmVIWMrHo_W000018 ===

source:
- language: Korean
- transcription: 제가 좀 직관적으로 이해하셔야 될 부분의 측면이 있어서 여러분들이 잘 한번 보시고 아주 이렇게 하니까 행이 병합이 되는구나 이렇게 느끼셨으면 좋겠습니다. 말로 하려니까 너무 힘드네요. 자, 그다음 여기는 합계라고 되어 있는 부분은 여기 있는 이 각각의 칸 세 개의 칸을
- source_tokens:
  0. 제가
  1. 좀
  2. 직관적으로
  3. 이해
  4. 하셔야
  5. 될
  6. 부분
  7. 의
  8. 측면
  9. 이
  10. 있어서
  11. 여러분
  12. 들이
  13. 잘
  14. 한번
  15. 보시고
  16. 아주
  17. 이렇게
  18. 하니까
  19. 행이
  20. 병합이
  21. 되는구나
  22. 이렇게
  23. 느끼
  24. 셨으면
  25. 좋겠습니다.
  26. 말로
  27. 하려니까
  28. 너무
  29. 힘드
  30. 네요.
  31. 자,
  32. 그다음
  33. 여기
  34. 는
  35. 합계
  36. 라고
  37. 되어
  38. 있는
  39. 부분
  40. 은
  41. 여기
  42. 있는
  43. 이
  44. 각각
  45. 의
  46. 칸
  47. 세
  48. 개의
  49. 칸을

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
  - source_tokens: `0: "제가", 6: "부분"`
  - mapping_reason: "제가" (I/something) and "부분" (part/something) function as the subject and referent.
* target[1]: "you need to understand intuitively."
  - source_tokens: `2: "직관적으로", 3: "이해", 4: "하셔야", 5: "될"`
  - mapping_reason: Direct translation of the Korean phrase.
* target[2]: "So I hope"
  - source_tokens: `25: "좋겠습니다."`
  - mapping_reason: Expresses the speaker's wish.
* target[3]: "you take a good look"
  - source_tokens: `13: "잘", 14: "한번", 15: "보시고"`
  - mapping_reason: Direct translation of the look/observe instruction.
* target[4]: "and really feel,"
  - source_tokens: `16: "아주", 23: "느끼", 24: "셨으면"`
  - mapping_reason: Expresses the feeling/realization.
* target[5]: "' Oh, so this is"
  - source_tokens: `17: "이렇게", 18: "하니까"`
  - mapping_reason: Expresses the realization of the method.
* target[6]: "how you merge rows."
  - source_tokens: `19: "행이", 20: "병합이", 21: "되는구나"`
  - mapping_reason: Describes the merging process.
* target[7]: "' It's so hard"
  - source_tokens: `28: "너무", 29: "힘드", 30: "네요."`
  - mapping_reason: Expresses difficulty.
* target[8]: "to explain this in words."
  - source_tokens: `26: "말로", 27: "하려니까"`
  - mapping_reason: Explains the medium of the difficulty.
* target[9]: "Okay, next, the part"
  - source_tokens: `31: "자,", 32: "그다음", 39: "부분"`
  - mapping_reason: Discourse marker and subject indicator.
* target[10]: "labeled ' Total '"
  - source_tokens: `35: "합계", 36: "라고", 37: "되어", 38: "있는"`
  - mapping_reason: Describes the label of the part.
* target[11]: "is meant for"
  - source_tokens: `39: "부분", 40: "은"`
  - mapping_reason: The 'part' (부분) + topic marker (은) indicates the definition/purpose of the subject.
* target[12]: "these three individual cells..."
  - source_tokens: `41: "여기", 42: "있는", 43: "이", 44: "각각", 45: "의", 46: "칸", 47: "세", 48: "개의", 49: "칸을"`
  - mapping_reason: Direct translation of the target objects.

result:
```html
0. <src>제가 좀 직관적으로 </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>이해 하셔야 될 </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>부분 의 </src> <tgt>There's something here you need to understand intuitively.</tgt>; start=2.00, end=3.00
3. <src>측면 이 있어서 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
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

- max_empty_window_count: 7


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[11]
  - verdict: mapping_error
  - reason: "The source tokens '여기' (here) and '는' (topic marker) do not correspond to the functional phrase 'is meant for'. The target unit serves as a bridge, and these source tokens are contextually irrelevant."
  - replace_source_tokens: 39: "부분", 40: "은"
  validation:
    scratchpad:
* target[0]: "There's something here"
  - source_tokens: `6: "부분", 7: "의", 8: "측면", 9: "이", 10: "있어서"`
  - mapping_reason: Expresses the existence of a specific aspect/part.
* target[1]: "you need to understand intuitively."
  - source_tokens: `0: "제가", 1: "좀", 2: "직관적으로", 3: "이해", 4: "하셔야", 5: "될"`
  - mapping_reason: Describes the requirement to understand intuitively.
* target[2]: "So I hope"
  - source_tokens: `24: "셨으면", 25: "좋겠습니다."`
  - mapping_reason: Expresses the speaker's wish/hope.
* target[3]: "you take a good look"
  - source_tokens: `11: "여러분", 12: "들이", 13: "잘", 14: "한번", 15: "보시고"`
  - mapping_reason: Encourages the audience to look closely.
* target[4]: "and really feel,"
  - source_tokens: `16: "아주", 23: "느끼"`
  - mapping_reason: Encourages the audience to feel/perceive.
* target[5]: "' Oh, so this is"
  - source_tokens: `17: "이렇게", 18: "하니까"`
  - mapping_reason: Explains the realization of "this is how".
* target[6]: "how you merge rows."
  - source_tokens: `19: "행이", 20: "병합이", 21: "되는구나"`
  - mapping_reason: Describes the action of merging rows.
* target[7]: "' It's so hard"
  - source_tokens: `28: "너무", 29: "힘드", 30: "네요."`
  - mapping_reason: Expresses difficulty.
* target[8]: "to explain this in words."
  - source_tokens: `26: "말로", 27: "하려니까"`
  - mapping_reason: Specifies the difficulty is in verbal explanation.
* target[9]: "Okay, next, the part"
  - source_tokens: `31: "자,", 32: "그다음", 39: "부분", 40: "은"`
  - mapping_reason: Discourse marker and subject identification.
* target[10]: "labeled ' Total '"
  - source_tokens: `35: "합계", 36: "라고", 37: "되어", 38: "있는"`
  - mapping_reason: Describes the label of the part.
* target[11]: "is meant for"
  - source_tokens: `33: "여기", 34: "는"`
  - mapping_reason: Indicates the target/reference of the part.
* target[12]: "these three individual cells..."
  - source_tokens: `41: "여기", 42: "있는", 43: "이", 44: "각각", 45: "의", 46: "칸", 47: "세", 48: "개의", 49: "칸을"`
  - mapping_reason: Identifies the specific cells being referenced.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [0, 1, 2, 3, 4, 5]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [24, 25]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [11, 12, 13, 14, 15]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [16, 23]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [17, 18]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [19, 20, 21]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [28, 29, 30]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [26, 27]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [31, 32, 39, 40]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [35, 36, 37, 38]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [33, 34]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [41, 42, 43, 44, 45, 46, 47, 48, 49]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== KO_GxLlh9Eui8c_W000249 ===

source:
- language: Korean
- transcription: 돌파하고 승리해야 한다. 다만 배도에 죄까지 갈 수 있으니 하나님 앞에서 늘 겸손하라는 메시지를 전하는 대신 진짜 거듭난 성도도 진짜 지옥에 아주 잘 가니까 대부분 지옥 가니까.
- source_tokens:
  0. 돌파
  1. 하고
  2. 승리
  3. 해야
  4. 한다.
  5. 다만
  6. 배도에
  7. 죄까지
  8. 갈
  9. 수
  10. 있으니
  11. 하나님
  12. 앞에서
  13. 늘
  14. 겸손
  15. 하라는
  16. 메시지
  17. 를
  18. 전하
  19. 는
  20. 대신
  21. 진짜
  22. 거듭
  23. 난
  24. 성도
  25. 도
  26. 진짜
  27. 지옥
  28. 에
  29. 아주
  30. 잘
  31. 가니까
  32. 대부분
  33. 지옥
  34. 가니까.

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
  - source_tokens: `0: "돌파", 3: "해야", 4: "한다."`
  - mapping_reason: "돌파" (breakthrough) + modality "해야 한다" (must).
* target[1]: "并取得胜利。"
  - source_tokens: `1: "하고", 2: "승리"`
  - mapping_reason: "하고" (and) + "승리" (victory).
* target[2]: "但"
  - source_tokens: `5: "다만"`
  - mapping_reason: "다만" (but).
* target[3]: "可能陷入"
  - source_tokens: `8: "갈", 9: "수", 10: "있으니"`
  - mapping_reason: "갈 수 있으니" (can go/fall into).
* target[4]: "背道的罪。"
  - source_tokens: `6: "배도에", 7: "죄까지"`
  - mapping_reason: "배도에" (apostasy) + "죄까지" (to the sin of).
* target[5]: "所以"
  - source_tokens: `5: "다만"`
  - mapping_reason: The source implies a contrastive transition "다만" which frames the following shift in message.
* target[6]: "与其说"
  - source_tokens: `20: "대신"`
  - mapping_reason: "대신" (instead of).
* target[7]: "要在神面前"
  - source_tokens: `11: "하나님", 12: "앞에서"`
  - mapping_reason: "하나님 앞에서" (before God).
* target[8]: "常保谦卑，"
  - source_tokens: `13: "늘", 14: "겸손", 15: "하라는"`
  - mapping_reason: "늘 겸손하라는" (to always be humble).
* target[9]: "不如说——"
  - source_tokens: `20: "대신"`
  - mapping_reason: "대신" (instead of/rather).
* target[10]: "真正重生的人，"
  - source_tokens: `21: "진짜", 22: "거듭", 23: "난", 24: "성도", 25: "도"`
  - mapping_reason: "진짜 거듭난 성도도" (even truly born-again saints).
* target[11]: "也确实"
  - source_tokens: `26: "진짜"`
  - mapping_reason: "진짜" (truly/indeed).
* target[12]: "很容易"
  - source_tokens: `29: "아주", 30: "잘"`
  - mapping_reason: "아주 잘" (very well/easily).
* target[13]: "下地狱。"
  - source_tokens: `27: "지옥", 28: "에", 31: "가니까"`
  - mapping_reason: "지옥에 가니까" (go to hell).
* target[14]: "因为"
  - source_tokens: `31: "가니까."`
  - mapping_reason: Causal marker from the final clause.
* target[15]: "大多数人"
  - source_tokens: `32: "대부분"`
  - mapping_reason: "대부분" (majority).
* target[16]: "都是"
  - source_tokens: `34: "가니까."`
  - mapping_reason: Copula/existential implication in the final clause.
* target[17]: "下地狱的。"
  - source_tokens: `33: "지옥", 34: "가니까."`
  - mapping_reason: "지옥 가니까" (go to hell).

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
  status: failed_after_response
  reason: * target[5]
  - verdict: mapping_error
  - reason: "The source token '있으니' is a verb suffix, not a discourse connector. The actual discourse marker is '다만'."
  - replace_source_tokens: 5: "다만"
  validation:
    scratchpad:
* target[0]: "必须突破"
  - source_tokens: `0: "돌파", 3: "해야", 4: "한다."`
  - mapping_reason: "突破" corresponds to "돌파", "必须" corresponds to "해야 한다."
* target[1]: "并取得胜利。"
  - source_tokens: `1: "하고", 2: "승리"`
  - mapping_reason: "并" corresponds to "하고", "取得胜利" corresponds to "승리".
* target[2]: "但"
  - source_tokens: `5: "다만"`
  - mapping_reason: "다만" translates to "但".
* target[3]: "可能陷入"
  - source_tokens: `8: "갈", 9: "수", 10: "있으니"`
  - mapping_reason: "갈 수 있으니" indicates the possibility of falling into something.
* target[4]: "背道的罪。"
  - source_tokens: `6: "배도에", 7: "죄까지"`
  - mapping_reason: "배도" and "죄" correspond to "背道" and "罪".
* target[5]: "所以"
  - source_tokens: `10: "있으니"`
  - mapping_reason: The causal structure "있으니" implies the following consequence.
* target[6]: "与其说"
  - source_tokens: `20: "대신"`
  - mapping_reason: "대신" introduces the contrastive "instead of".
* target[7]: "要在神面前"
  - source_tokens: `11: "하나님", 12: "앞에서"`
  - mapping_reason: "하나님 앞에서" translates to "在神面前".
* target[8]: "常保谦卑，"
  - source_tokens: `13: "늘", 14: "겸손", 15: "하라는"`
  - mapping_reason: "늘 겸손하라는" translates to "常保谦卑".
* target[9]: "不如说——"
  - source_tokens: `16: "메시지", 17: "를", 18: "전하", 19: "는", 20: "대신"`
  - mapping_reason: The phrase "메시지를 전하는 대신" functions as the "instead of/rather than" structure.
* target[10]: "真正重生的人，"
  - source_tokens: `21: "진짜", 22: "거듭", 23: "난", 24: "성도", 25: "도"`
  - mapping_reason: "진짜 거듭난 성도도" translates to "真正重生的人也".
* target[11]: "也确实"
  - source_tokens: `26: "진짜"`
  - mapping_reason: "진짜" acts as an intensifier "确实".
* target[12]: "很容易"
  - source_tokens: `29: "아주", 30: "잘"`
  - mapping_reason: "아주 잘" translates to "很容易".
* target[13]: "下地狱。"
  - source_tokens: `27: "지옥", 28: "에", 31: "가니까"`
  - mapping_reason: "지옥에 가니까" translates to "下地狱".
* target[14]: "因为"
  - source_tokens: `31: "가니까"`
  - mapping_reason: The suffix "-니까" indicates a reason.
* target[15]: "大多数人"
  - source_tokens: `32: "대부분"`
  - mapping_reason: "대부분" translates to "大多数人".
* target[16]: "都是"
  - source_tokens: `34: "가니까."`
  - mapping_reason: Expresses the state of the subject.
* target[17]: "下地狱的。"
  - source_tokens: `33: "지옥", 34: "가니까."`
  - mapping_reason: "지옥 가니까" translates to "下地狱".
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 3, 4]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1, 2]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [8, 9, 10]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [6, 7]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [10]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [20]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [13, 14, 15]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [16, 17, 18, 19, 20]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [21, 22, 23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [29, 30]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [27, 28, 31]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [31]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [32]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [34]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [33, 34]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
