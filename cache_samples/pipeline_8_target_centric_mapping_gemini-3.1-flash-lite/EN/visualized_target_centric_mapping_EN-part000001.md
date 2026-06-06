=== EN_B00016_S00442_W000017 ===

source:
- language: English
- transcription: This here returned undefined, and so then the second one got returned. While here, in this one, this value was 20, and so it is this 20 that immediately got returned.
- source_tokens:
  0. This
  1. here
  2. returned
  3. undefined,
  4. and
  5. so
  6. then
  7. the
  8. second
  9. one
  10. got
  11. returned.
  12. While
  13. here,
  14. in
  15. this
  16. one,
  17. this
  18. value
  19. was
  20. 20,
  21. and
  22. so
  23. it
  24. is
  25. this
  26. 20
  27. that
  28. immediately
  29. got
  30. returned.

target:
- language: Japanese
- translation: こちらは undefined を返したので、結果として2番目の方が返りました。一方こちらのケースは、値が 20 だったので、この 20 がすぐに返っています。
- target_sense_units:
  0. こちらは
  1. undefinedを
  2. 返したので、
  3. 結果として
  4. 2番目の方が
  5. 返りました。
  6. 一方
  7. こちらのケースは、
  8. 値が
  9. 20だったので、
  10. この20が
  11. すぐに
  12. 返っています。

scratchpad:
* target[0]: "こちらは"
  - source_tokens: `0: "This", 1: "here"`
  - mapping_reason: Subject reference to the first item.
* target[1]: "undefinedを"
  - source_tokens: `3: "undefined,"`
  - mapping_reason: Object of the return action.
* target[2]: "返したので、"
  - source_tokens: `2: "returned", 5: "so"`
  - mapping_reason: Causative return action.
* target[3]: "結果として"
  - source_tokens: `6: "then"`
  - mapping_reason: Sequential/resultative connective.
* target[4]: "2番目の方が"
  - source_tokens: `7: "the", 8: "second", 9: "one"`
  - mapping_reason: Identifying the second item.
* target[5]: "返りました。"
  - source_tokens: `10: "got", 11: "returned."`
  - mapping_reason: The second return action.
* target[6]: "一方"
  - source_tokens: `12: "While"`
  - mapping_reason: Contrastive conjunction.
* target[7]: "こちらのケースは、"
  - source_tokens: `13: "here,", 14: "in", 15: "this", 16: "one,"`
  - mapping_reason: Locative/contextual reference.
* target[8]: "値が"
  - source_tokens: `18: "value"`
  - mapping_reason: Subject of the state.
* target[9]: "20だったので、"
  - source_tokens: `19: "was", 20: "20,", 21: "and", 22: "so"`
  - mapping_reason: State value and causative connective.
* target[10]: "この20が"
  - source_tokens: `25: "this", 26: "20"`
  - mapping_reason: Specific reference to the value.
* target[11]: "すぐに"
  - source_tokens: `28: "immediately"`
  - mapping_reason: Temporal modifier.
* target[12]: "返っています。"
  - source_tokens: `27: "that", 29: "got", 30: "returned."`
  - mapping_reason: The final return action.

result:
```html
0. <src>This here </src> <tgt>こちらは</tgt>; start=0.00, end=1.00
1. <src>returned undefined, and so </src> <tgt>undefinedを返したので、</tgt>; start=1.00, end=2.00
2. <src>then the second one </src> <tgt>結果として2番目の方が</tgt>; start=2.00, end=3.00
3. <src>got returned. </src> <tgt>返りました。</tgt>; start=3.00, end=4.00
4. <src>While here, </src> <tgt>一方</tgt>; start=4.00, end=5.00
5. <src>in this one, </src> <tgt>こちらのケースは、</tgt>; start=5.00, end=6.00
6. <src>this value was </src> <tgt>値が</tgt>; start=6.00, end=7.00
7. <src>20, </src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>and so it is this </src> <tgt>20だったので、</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>20 that immediately got returned. </src> <tgt>この20がすぐに返っています。</tgt>; start=10.00, end=10.65
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_B00016_S00442_W000017 ===

source:
- language: English
- transcription: This here returned undefined, and so then the second one got returned. While here, in this one, this value was 20, and so it is this 20 that immediately got returned.
- source_tokens:
  0. This
  1. here
  2. returned
  3. undefined,
  4. and
  5. so
  6. then
  7. the
  8. second
  9. one
  10. got
  11. returned.
  12. While
  13. here,
  14. in
  15. this
  16. one,
  17. this
  18. value
  19. was
  20. 20,
  21. and
  22. so
  23. it
  24. is
  25. this
  26. 20
  27. that
  28. immediately
  29. got
  30. returned.

target:
- language: Korean
- translation: 여기서는 undefined가 반환됐고, 그래서 두 번째 것이 반환됐습니다. 반면에 여기는 값이 20이었습니다. 그래서 바로 이 20이 반환됐습니다.
- target_sense_units:
  0. 여기서는
  1. undefined가
  2. 반환됐고,
  3. 그래서
  4. 두 번째
  5. 것이
  6. 반환됐습니다.
  7. 반면에
  8. 여기는
  9. 값이
  10. 20이었습니다.
  11. 그래서
  12. 바로
  13. 이 20이
  14. 반환됐습니다.

scratchpad:
* target[0]: "여기서는"
  - source_tokens: `0: "This", 1: "here"`
  - mapping_reason: Represents "This here" with a topic marker.
* target[1]: "undefined가"
  - source_tokens: `3: "undefined,"`
  - mapping_reason: The subject "undefined".
* target[2]: "반환됐고,"
  - source_tokens: `2: "returned"`
  - mapping_reason: The verb "returned" with conjunctive ending.
* target[3]: "그래서"
  - source_tokens: `4: "and", 5: "so"`
  - mapping_reason: Conjunction "and so".
* target[4]: "두 번째"
  - source_tokens: `8: "second"`
  - mapping_reason: Ordinal modifier.
* target[5]: "것이"
  - source_tokens: `9: "one"`
  - mapping_reason: Head noun.
* target[6]: "반환됐습니다."
  - source_tokens: `10: "got", 11: "returned."`
  - mapping_reason: Passive construction "got returned".
* target[7]: "반면에"
  - source_tokens: `12: "While"`
  - mapping_reason: Contrastive conjunction.
* target[8]: "여기는"
  - source_tokens: `13: "here,"`
  - mapping_reason: Location marker.
* target[9]: "값이"
  - source_tokens: `18: "value"`
  - mapping_reason: Subject "value".
* target[10]: "20이었습니다."
  - source_tokens: `19: "was", 20: "20,"`
  - mapping_reason: Predicate "was 20".
* target[11]: "그래서"
  - source_tokens: `21: "and", 22: "so"`
  - mapping_reason: Conjunction "and so".
* target[12]: "바로"
  - source_tokens: `28: "immediately"`
  - mapping_reason: Emphatic adverb.
* target[13]: "이 20이"
  - source_tokens: `25: "this", 26: "20"`
  - mapping_reason: Specific noun phrase.
* target[14]: "반환됐습니다."
  - source_tokens: `27: "that", 29: "got", 30: "returned."`
  - mapping_reason: Passive verb phrase.

result:
```html
0. <src>This here </src> <tgt>여기서는</tgt>; start=0.00, end=1.00
1. <src>returned undefined, and so </src> <tgt>undefined가 반환됐고, 그래서</tgt>; start=1.00, end=2.00
2. <src>then the second one </src> <tgt>두 번째 것이</tgt>; start=2.00, end=3.00
3. <src>got returned. </src> <tgt>반환됐습니다.</tgt>; start=3.00, end=4.00
4. <src>While here, </src> <tgt>반면에 여기는</tgt>; start=4.00, end=5.00
5. <src>in this one, </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>this value was </src> <tgt>값이</tgt>; start=6.00, end=7.00
7. <src>20, </src> <tgt>20이었습니다.</tgt>; start=7.00, end=8.00
8. <src>and so it is this </src> <tgt>그래서</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>20 that immediately got returned. </src> <tgt>바로 이 20이 반환됐습니다.</tgt>; start=10.00, end=10.65
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_oINupCbfGEo_W000003 ===

source:
- language: English
- transcription: Images show the surface of Charon is mostly covered by water ice. We saw steep cliffs and a giant canyon near the equator that stretches more than 600 miles. Scientists also found organic materials on its icy surface.
- source_tokens:
  0. Images
  1. show
  2. the
  3. surface
  4. of
  5. Charon
  6. is
  7. mostly
  8. covered
  9. by
  10. water
  11. ice.
  12. We
  13. saw
  14. steep
  15. cliffs
  16. and
  17. a
  18. giant
  19. canyon
  20. near
  21. the
  22. equator
  23. that
  24. stretches
  25. more
  26. than
  27. 600
  28. miles.
  29. Scientists
  30. also
  31. found
  32. organic
  33. materials
  34. on
  35. its
  36. icy
  37. surface.

target:
- language: Chinese
- translation: 图像显示，卡戎的表面大部分被水冰覆盖。我们看到了陡峭的悬崖，还有一个巨大的峡谷，它位于赤道附近，绵延超过600英里。科学家还在它的冰冷表面上发现了有机物质。
- target_sense_units:
  0. 图像显示，
  1. 卡戎的表面
  2. 大部分
  3. 被水冰覆盖。
  4. 我们看到了
  5. 陡峭的悬崖，
  6. 还有一个
  7. 巨大的峡谷，
  8. 它
  9. 位于赤道附近，
  10. 绵延
  11. 超过600英里。
  12. 科学家
  13. 还
  14. 在它的
  15. 冰冷表面上
  16. 发现了
  17. 有机物质。

scratchpad:
* target[0]: "图像显示，"
  - source_tokens: `0: "Images", 1: "show"`
  - mapping_reason: Subject and verb indicating source of information.
* target[1]: "卡戎的表面"
  - source_tokens: `5: "Charon", 3: "surface", 4: "of"`
  - mapping_reason: Possessive relation between Charon and its surface.
* target[2]: "大部分"
  - source_tokens: `7: "mostly"`
  - mapping_reason: Adverbial modifier of coverage.
* target[3]: "被水冰覆盖。"
  - source_tokens: `8: "covered", 9: "by", 10: "water", 11: "ice."`
  - mapping_reason: Passive construction describing the state of the surface.
* target[4]: "我们看到了"
  - source_tokens: `12: "We", 13: "saw"`
  - mapping_reason: Subject and verb of observation.
* target[5]: "陡峭的悬崖，"
  - source_tokens: `14: "steep", 15: "cliffs"`
  - mapping_reason: Noun phrase describing the observed features.
* target[6]: "还有一个"
  - source_tokens: `16: "and", 17: "a"`
  - mapping_reason: Conjunction and indefinite article.
* target[7]: "巨大的峡谷，"
  - source_tokens: `18: "giant", 19: "canyon"`
  - mapping_reason: Noun phrase describing the observed feature.
* target[8]: "它"
  - source_tokens: `23: "that"`
  - mapping_reason: Relative pronoun referring to the canyon.
* target[9]: "位于赤道附近，"
  - source_tokens: `20: "near", 21: "the", 22: "equator"`
  - mapping_reason: Locative phrase describing the canyon's position.
* target[10]: "绵延"
  - source_tokens: `24: "stretches"`
  - mapping_reason: Verb describing the extent of the canyon.
* target[11]: "超过600英里。"
  - source_tokens: `25: "more", 26: "than", 27: "600", 28: "miles."`
  - mapping_reason: Quantitative phrase describing length.
* target[12]: "科学家"
  - source_tokens: `29: "Scientists"`
  - mapping_reason: Subject of the second observation.
* target[13]: "还"
  - source_tokens: `30: "also"`
  - mapping_reason: Additive discourse marker.
* target[14]: "在它的"
  - source_tokens: `34: "on", 35: "its"`
  - mapping_reason: Preposition and possessive pronoun indicating location.
* target[15]: "冰冷表面上"
  - source_tokens: `36: "icy", 37: "surface."`
  - mapping_reason: Noun phrase specifying the location of organic materials.
* target[16]: "发现了"
  - source_tokens: `31: "found"`
  - mapping_reason: Verb of observation.
* target[17]: "有机物质。"
  - source_tokens: `32: "organic", 33: "materials"`
  - mapping_reason: Direct object of the finding action.

result:
```html
0. <src>Images show </src> <tgt>图像显示，</tgt>; start=0.00, end=1.00
1. <src>the surface of Charon </src> <tgt>卡戎的表面</tgt>; start=1.00, end=2.00
2. <src>is mostly covered </src> <tgt>大部分</tgt>; start=2.00, end=3.00
3. <src>by water ice. </src> <tgt>被水冰覆盖。</tgt>; start=3.00, end=4.00
4. <src>We saw </src> <tgt>我们看到了</tgt>; start=4.00, end=5.00
5. <src>steep cliffs and </src> <tgt>陡峭的悬崖，</tgt>; start=5.00, end=6.00
6. <src>a giant canyon </src> <tgt>还有一个巨大的峡谷，</tgt>; start=6.00, end=7.00
7. <src>near the equator that </src> <tgt>它位于赤道附近，</tgt>; start=7.00, end=8.00
8. <src>stretches more than </src> <tgt>绵延</tgt>; start=8.00, end=9.00
9. <src>600 miles. </src> <tgt>超过600英里。</tgt>; start=9.00, end=10.00
10. <src>Scientists </src> <tgt>科学家</tgt>; start=10.00, end=11.00
11. <src>also found </src> <tgt>还</tgt>; start=11.00, end=12.00
12. <src>organic materials </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>on its icy surface. </src> <tgt>在它的冰冷表面上发现了有机物质。</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=14.01
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_B00016_S00602_W000000 ===

source:
- language: English
- transcription: My grandfather was a World War II aviator, and my great uncle was an Air Force pilot who was shot down over Vietnam and spent five years in the Hanoi Hilton with John McCain and.
- source_tokens:
  0. My
  1. grandfather
  2. was
  3. a
  4. World
  5. War
  6. II
  7. aviator,
  8. and
  9. my
  10. great
  11. uncle
  12. was
  13. an
  14. Air
  15. Force
  16. pilot
  17. who
  18. was
  19. shot
  20. down
  21. over
  22. Vietnam
  23. and
  24. spent
  25. five
  26. years
  27. in
  28. the
  29. Hanoi
  30. Hilton
  31. with
  32. John
  33. McCain
  34. and.

target:
- language: Chinese
- translation: 我祖父是二战时期的飞行员，而我的伯祖父曾是一名空军飞行员，他在越南上空被击落，并在河内希尔顿监狱与约翰·麦凯恩一起度过了五年，还有……
- target_sense_units:
  0. 我祖父是
  1. 二战时期的飞行员，
  2. 而
  3. 我的伯祖父
  4. 曾是
  5. 一名空军飞行员，
  6. 他
  7. 在越南上空
  8. 被击落，
  9. 并
  10. 在河内希尔顿监狱
  11. 与约翰·麦凯恩一起
  12. 度过了
  13. 五年，
  14. 还有……

scratchpad:
* target[0]: "我祖父是"
  - source_tokens: `0: "My", 1: "grandfather", 2: "was"`
  - mapping_reason: Subject "My grandfather" and copula "was".
* target[1]: "二战时期的飞行员，"
  - source_tokens: `4: "World", 5: "War", 6: "II", 7: "aviator,"`
  - mapping_reason: Noun phrase describing the grandfather's role.
* target[2]: "而"
  - source_tokens: `8: "and"`
  - mapping_reason: Conjunction indicating contrast/continuation.
* target[3]: "我的伯祖父"
  - source_tokens: `9: "my", 10: "great", 11: "uncle"`
  - mapping_reason: Subject of the second clause.
* target[4]: "曾是"
  - source_tokens: `12: "was"`
  - mapping_reason: Copula indicating past state.
* target[5]: "一名空军飞行员，"
  - source_tokens: `13: "an", 14: "Air", 15: "Force", 16: "pilot"`
  - mapping_reason: Noun phrase describing the uncle's role.
* target[6]: "他"
  - source_tokens: `17: "who"`
  - mapping_reason: Relative pronoun referring to the uncle.
* target[7]: "在越南上空"
  - source_tokens: `21: "over", 22: "Vietnam"`
  - mapping_reason: Locative modifier.
* target[8]: "被击落，"
  - source_tokens: `18: "was", 19: "shot", 20: "down"`
  - mapping_reason: Passive verbal action.
* target[9]: "并"
  - source_tokens: `23: "and"`
  - mapping_reason: Conjunction linking the two actions of the uncle.
* target[10]: "在河内希尔顿监狱"
  - source_tokens: `27: "in", 28: "the", 29: "Hanoi", 30: "Hilton"`
  - mapping_reason: Locative modifier.
* target[11]: "与约翰·麦凯恩一起"
  - source_tokens: `31: "with", 32: "John", 33: "McCain"`
  - mapping_reason: Comitative modifier.
* target[12]: "度过了"
  - source_tokens: `24: "spent"`
  - mapping_reason: Main verb of the second action.
* target[13]: "五年，"
  - source_tokens: `25: "five", 26: "years"`
  - mapping_reason: Duration modifier.
* target[14]: "还有……"
  - source_tokens: `34: "and."`
  - mapping_reason: Discourse marker indicating an incomplete list.

result:
```html
0. <src>My grandfather was </src> <tgt>我祖父是</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>a World War II aviator, </src> <tgt>二战时期的飞行员，</tgt>; start=2.00, end=3.00
3. <src>and my great uncle </src> <tgt>而我的伯祖父</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>was an Air Force pilot </src> <tgt>曾是一名空军飞行员，</tgt>; start=5.00, end=6.00
6. <src>who was shot down </src> <tgt>他</tgt>; start=6.00, end=7.00
7. <src>over Vietnam </src> <tgt>在越南上空被击落，</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>and spent five years </src> <tgt>并</tgt>; start=9.00, end=10.00
10. <src>in the Hanoi Hilton </src> <tgt>在河内希尔顿监狱</tgt>; start=10.00, end=11.00
11. <src>with John McCain and. </src> <tgt>与约翰·麦凯恩一起度过了五年，还有……</tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=12.03
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_B00016_S00602_W000000 ===

source:
- language: English
- transcription: My grandfather was a World War II aviator, and my great uncle was an Air Force pilot who was shot down over Vietnam and spent five years in the Hanoi Hilton with John McCain and.
- source_tokens:
  0. My
  1. grandfather
  2. was
  3. a
  4. World
  5. War
  6. II
  7. aviator,
  8. and
  9. my
  10. great
  11. uncle
  12. was
  13. an
  14. Air
  15. Force
  16. pilot
  17. who
  18. was
  19. shot
  20. down
  21. over
  22. Vietnam
  23. and
  24. spent
  25. five
  26. years
  27. in
  28. the
  29. Hanoi
  30. Hilton
  31. with
  32. John
  33. McCain
  34. and.

target:
- language: Korean
- translation: 제 할아버지는 제2차 세계대전 당시 비행사셨고, 큰할아버지는 공군 조종사셨는데 베트남 상공에서 격추되어 존 매케인과 함께 하노이 힐튼에서 5년을 보내셨어요, 그리고...
- target_sense_units:
  0. 제 할아버지는
  1. 제2차 세계대전 당시
  2. 비행사셨고,
  3. 큰할아버지는
  4. 공군
  5. 조종사셨는데
  6. 베트남 상공에서
  7. 격추되어
  8. 존 매케인과
  9. 함께
  10. 하노이 힐튼에서
  11. 5년을
  12. 보내셨어요,
  13. 그리고...

scratchpad:
* target[0]: "제 할아버지는"
  - source_tokens: `0: "My", 1: "grandfather"`
  - mapping_reason: Subject reference (My grandfather).
* target[1]: "제2차 세계대전 당시"
  - source_tokens: `4: "World", 5: "War", 6: "II"`
  - mapping_reason: Temporal modifier identifying the period.
* target[2]: "비행사셨고,"
  - source_tokens: `2: "was", 3: "a", 7: "aviator,"`
  - mapping_reason: Predicate describing the grandfather's role and the conjunction "and".
* target[3]: "큰할아버지는"
  - source_tokens: `9: "my", 10: "great", 11: "uncle"`
  - mapping_reason: Subject reference (my great uncle).
* target[4]: "공군"
  - source_tokens: `14: "Air", 15: "Force"`
  - mapping_reason: Branch of service.
* target[5]: "조종사셨는데"
  - source_tokens: `12: "was", 13: "an", 16: "pilot", 17: "who"`
  - mapping_reason: Predicate describing the uncle's role and relative clause connector.
* target[6]: "베트남 상공에서"
  - source_tokens: `21: "over", 22: "Vietnam"`
  - mapping_reason: Location of the event.
* target[7]: "격추되어"
  - source_tokens: `18: "was", 19: "shot", 20: "down"`
  - mapping_reason: Action (shot down).
* target[8]: "존 매케인과"
  - source_tokens: `32: "John", 33: "McCain"`
  - mapping_reason: Person mentioned.
* target[9]: "함께"
  - source_tokens: `31: "with"`
  - mapping_reason: Accompaniment relation.
* target[10]: "하노이 힐튼에서"
  - source_tokens: `27: "in", 28: "the", 29: "Hanoi", 30: "Hilton"`
  - mapping_reason: Location of imprisonment.
* target[11]: "5년을"
  - source_tokens: `25: "five", 26: "years"`
  - mapping_reason: Duration.
* target[12]: "보내셨어요,"
  - source_tokens: `23: "and", 24: "spent"`
  - mapping_reason: Predicate (spent).
* target[13]: "그리고..."
  - source_tokens: `34: "and."`
  - mapping_reason: Final conjunction.

result:
```html
0. <src>My grandfather was </src> <tgt>제 할아버지는</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>a World War II aviator, </src> <tgt>제2차 세계대전 당시 비행사셨고,</tgt>; start=2.00, end=3.00
3. <src>and my great uncle </src> <tgt>큰할아버지는</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>was an Air Force pilot </src> <tgt>공군</tgt>; start=5.00, end=6.00
6. <src>who was shot down </src> <tgt>조종사셨는데</tgt>; start=6.00, end=7.00
7. <src>over Vietnam </src> <tgt>베트남 상공에서 격추되어</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>and spent five years </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>in the Hanoi Hilton </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>with John McCain and. </src> <tgt>존 매케인과 함께 하노이 힐튼에서 5년을 보내셨어요, 그리고...</tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=12.03
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_B00016_S00442_W000017 ===

source:
- language: English
- transcription: This here returned undefined, and so then the second one got returned. While here, in this one, this value was 20, and so it is this 20 that immediately got returned.
- source_tokens:
  0. This
  1. here
  2. returned
  3. undefined,
  4. and
  5. so
  6. then
  7. the
  8. second
  9. one
  10. got
  11. returned.
  12. While
  13. here,
  14. in
  15. this
  16. one,
  17. this
  18. value
  19. was
  20. 20,
  21. and
  22. so
  23. it
  24. is
  25. this
  26. 20
  27. that
  28. immediately
  29. got
  30. returned.

target:
- language: Chinese
- translation: 这里返回了 undefined。所以接着返回了第二个。而在这一处，这个值是 20。所以立即返回的就是这个 20。
- target_sense_units:
  0. 这里返回了undefined。
  1. 所以
  2. 接着
  3. 返回了第二个。
  4. 而
  5. 在这一处，
  6. 这个值
  7. 是20。
  8. 所以
  9. 立即返回的
  10. 就是这个20。

scratchpad:
* target[0]: "这里返回了undefined。"
  - source_tokens: `0: "This", 1: "here", 2: "returned", 3: "undefined,"`
  - mapping_reason: Direct translation of the first clause.
* target[1]: "所以"
  - source_tokens: `4: "and", 5: "so"`
  - mapping_reason: Connective indicating consequence.
* target[2]: "接着"
  - source_tokens: `6: "then"`
  - mapping_reason: Temporal sequence marker.
* target[3]: "返回了第二个。"
  - source_tokens: `7: "the", 8: "second", 9: "one", 10: "got", 11: "returned."`
  - mapping_reason: Action of returning the second item.
* target[4]: "而"
  - source_tokens: `12: "While"`
  - mapping_reason: Contrastive conjunction.
* target[5]: "在这一处，"
  - source_tokens: `13: "here,", 14: "in", 15: "this", 16: "one,"`
  - mapping_reason: Locative modifier.
* target[6]: "这个值"
  - source_tokens: `17: "this", 18: "value"`
  - mapping_reason: Subject of the second state description.
* target[7]: "是20。"
  - source_tokens: `19: "was", 20: "20,"`
  - mapping_reason: State description.
* target[8]: "所以"
  - source_tokens: `21: "and", 22: "so"`
  - mapping_reason: Consequence connective.
* target[9]: "立即返回的"
  - source_tokens: `28: "immediately", 29: "got", 30: "returned."`
  - mapping_reason: Action and timing modifier.
* target[10]: "就是这个20。"
  - source_tokens: `23: "it", 24: "is", 25: "this", 26: "20", 27: "that"`
  - mapping_reason: Identifying the specific value returned.

result:
```html
0. <src>This here </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>returned undefined, and so </src> <tgt>这里返回了undefined。所以</tgt>; start=1.00, end=2.00
2. <src>then the second one </src> <tgt>接着</tgt>; start=2.00, end=3.00
3. <src>got returned. </src> <tgt>返回了第二个。</tgt>; start=3.00, end=4.00
4. <src>While here, </src> <tgt>而</tgt>; start=4.00, end=5.00
5. <src>in this one, </src> <tgt>在这一处，</tgt>; start=5.00, end=6.00
6. <src>this value was </src> <tgt>这个值</tgt>; start=6.00, end=7.00
7. <src>20, </src> <tgt>是20。</tgt>; start=7.00, end=8.00
8. <src>and so it is this </src> <tgt>所以</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>20 that immediately got returned. </src> <tgt>立即返回的就是这个20。</tgt>; start=10.00, end=10.65
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_B00016_S00602_W000000 ===

source:
- language: English
- transcription: My grandfather was a World War II aviator, and my great uncle was an Air Force pilot who was shot down over Vietnam and spent five years in the Hanoi Hilton with John McCain and.
- source_tokens:
  0. My
  1. grandfather
  2. was
  3. a
  4. World
  5. War
  6. II
  7. aviator,
  8. and
  9. my
  10. great
  11. uncle
  12. was
  13. an
  14. Air
  15. Force
  16. pilot
  17. who
  18. was
  19. shot
  20. down
  21. over
  22. Vietnam
  23. and
  24. spent
  25. five
  26. years
  27. in
  28. the
  29. Hanoi
  30. Hilton
  31. with
  32. John
  33. McCain
  34. and.

target:
- language: Japanese
- translation: 私の祖父は第二次世界大戦の飛行士で、大叔父は空軍のパイロットでした。ベトナム上空で撃墜されて、ジョン・マケインと共にハノイ・ヒルトンで5年間を過ごして、そして。
- target_sense_units:
  0. 私の
  1. 祖父は
  2. 第二次世界大戦の
  3. 飛行士で、
  4. 大叔父は
  5. 空軍の
  6. パイロットでした。
  7. ベトナム上空で
  8. 撃墜されて、
  9. ジョン・マケインと
  10. 共に
  11. ハノイ・ヒルトンで
  12. 5年間を
  13. 過ごして、
  14. そして。

scratchpad:
* target[0]: "私の"
  - source_tokens: `0: "My"`
  - mapping_reason: possessive pronoun
* target[1]: "祖父は"
  - source_tokens: `1: "grandfather", 2: "was"`
  - mapping_reason: subject and copula relation
* target[2]: "第二次世界大戦の"
  - source_tokens: `4: "World", 5: "War", 6: "II"`
  - mapping_reason: modifier identifying the war
* target[3]: "飛行士で、"
  - source_tokens: `3: "a", 7: "aviator,"`
  - mapping_reason: noun phrase and conjunctive form
* target[4]: "大叔父は"
  - source_tokens: `9: "my", 10: "great", 11: "uncle"`
  - mapping_reason: subject noun phrase
* target[5]: "空軍の"
  - source_tokens: `14: "Air", 15: "Force"`
  - mapping_reason: modifier for pilot
* target[6]: "パイロットでした。"
  - source_tokens: `12: "was", 13: "an", 16: "pilot"`
  - mapping_reason: predicate noun phrase
* target[7]: "ベトナム上空で"
  - source_tokens: `21: "over", 22: "Vietnam"`
  - mapping_reason: location modifier
* target[8]: "撃墜されて、"
  - source_tokens: `18: "was", 19: "shot", 20: "down"`
  - mapping_reason: passive verb phrase
* target[9]: "ジョン・マケインと"
  - source_tokens: `32: "John", 33: "McCain"`
  - mapping_reason: proper noun phrase
* target[10]: "共に"
  - source_tokens: `31: "with"`
  - mapping_reason: associative preposition
* target[11]: "ハノイ・ヒルトンで"
  - source_tokens: `29: "Hanoi", 30: "Hilton"`
  - mapping_reason: location noun phrase
* target[12]: "5年間を"
  - source_tokens: `25: "five", 26: "years"`
  - mapping_reason: duration noun phrase
* target[13]: "過ごして、"
  - source_tokens: `24: "spent"`
  - mapping_reason: main verb
* target[14]: "そして。"
  - source_tokens: `8: "and", 23: "and", 34: "and."`
  - mapping_reason: discourse connective

result:
```html
0. <src>My grandfather was </src> <tgt>私の祖父は</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>a World War II aviator, </src> <tgt>第二次世界大戦の飛行士で、</tgt>; start=2.00, end=3.00
3. <src>and my great uncle </src> <tgt>大叔父は</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>was an Air Force pilot </src> <tgt>空軍のパイロットでした。</tgt>; start=5.00, end=6.00
6. <src>who was shot down </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>over Vietnam </src> <tgt>ベトナム上空で撃墜されて、</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>and spent five years </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>in the Hanoi Hilton </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>with John McCain and. </src> <tgt>ジョン・マケインと共にハノイ・ヒルトンで5年間を過ごして、そして。</tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=12.03
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_oINupCbfGEo_W000003 ===

source:
- language: English
- transcription: Images show the surface of Charon is mostly covered by water ice. We saw steep cliffs and a giant canyon near the equator that stretches more than 600 miles. Scientists also found organic materials on its icy surface.
- source_tokens:
  0. Images
  1. show
  2. the
  3. surface
  4. of
  5. Charon
  6. is
  7. mostly
  8. covered
  9. by
  10. water
  11. ice.
  12. We
  13. saw
  14. steep
  15. cliffs
  16. and
  17. a
  18. giant
  19. canyon
  20. near
  21. the
  22. equator
  23. that
  24. stretches
  25. more
  26. than
  27. 600
  28. miles.
  29. Scientists
  30. also
  31. found
  32. organic
  33. materials
  34. on
  35. its
  36. icy
  37. surface.

target:
- language: Japanese
- translation: 画像によると、カロンの表面は大部分が氷で覆われています。私たちは切り立った崖と、赤道付近にある巨大な峡谷を確認しました。その峡谷は600マイル以上にわたって広がっています。科学者たちは、その氷の表面に有機物も発見しています。
- target_sense_units:
  0. 画像によると、
  1. カロンの表面は
  2. 大部分が
  3. 氷で
  4. 覆われています。
  5. 私たちは
  6. 切り立った崖と、
  7. 赤道付近にある
  8. 巨大な峡谷を
  9. 確認しました。
  10. その峡谷は
  11. 600マイル以上にわたって
  12. 広がっています。
  13. 科学者たちは、
  14. その氷の表面に
  15. 有機物も
  16. 発見しています。

scratchpad:
* target[0]: "画像によると、"
  - source_tokens: `0: "Images", 1: "show"`
  - mapping_reason: "Images" provides the source of information, "show" provides the evidential link.
* target[1]: "カロンの表面は"
  - source_tokens: `3: "surface", 4: "of", 5: "Charon"`
  - mapping_reason: Specifies the subject and location.
* target[2]: "大部分が"
  - source_tokens: `7: "mostly"`
  - mapping_reason: Quantifier describing the coverage.
* target[3]: "氷で"
  - source_tokens: `10: "water", 11: "ice."`
  - mapping_reason: The material covering the surface.
* target[4]: "覆われています。"
  - source_tokens: `6: "is", 8: "covered", 9: "by"`
  - mapping_reason: The state of being covered.
* target[5]: "私たちは"
  - source_tokens: `12: "We"`
  - mapping_reason: Subject of the observation.
* target[6]: "切り立った崖と、"
  - source_tokens: `14: "steep", 15: "cliffs"`
  - mapping_reason: Object of observation.
* target[7]: "赤道付近にある"
  - source_tokens: `20: "near", 21: "the", 22: "equator"`
  - mapping_reason: Location of the canyon.
* target[8]: "巨大な峡谷を"
  - source_tokens: `18: "giant", 19: "canyon"`
  - mapping_reason: Object of observation.
* target[9]: "確認しました。"
  - source_tokens: `13: "saw"`
  - mapping_reason: The action of observing.
* target[10]: "その峡谷は"
  - source_tokens: `19: "canyon"`
  - mapping_reason: Refers back to the canyon.
* target[11]: "600マイル以上にわたって"
  - source_tokens: `25: "more", 26: "than", 27: "600", 28: "miles."`
  - mapping_reason: Extent of the canyon.
* target[12]: "広がっています。"
  - source_tokens: `23: "that", 24: "stretches"`
  - mapping_reason: The action describing the extent.
* target[13]: "科学者たちは、"
  - source_tokens: `29: "Scientists"`
  - mapping_reason: Subject of the finding.
* target[14]: "その氷の表面に"
  - source_tokens: `35: "its", 36: "icy", 37: "surface."`
  - mapping_reason: Location of discovery.
* target[15]: "有機物も"
  - source_tokens: `30: "also", 32: "organic", 33: "materials"`
  - mapping_reason: The object discovered (including 'also').
* target[16]: "発見しています。"
  - source_tokens: `31: "found"`
  - mapping_reason: The action of discovery.

result:
```html
0. <src>Images show </src> <tgt>画像によると、</tgt>; start=0.00, end=1.00
1. <src>the surface of Charon </src> <tgt>カロンの表面は</tgt>; start=1.00, end=2.00
2. <src>is mostly covered </src> <tgt>大部分が</tgt>; start=2.00, end=3.00
3. <src>by water ice. </src> <tgt>氷で覆われています。</tgt>; start=3.00, end=4.00
4. <src>We saw </src> <tgt>私たちは</tgt>; start=4.00, end=5.00
5. <src>steep cliffs and </src> <tgt>切り立った崖と、</tgt>; start=5.00, end=6.00
6. <src>a giant canyon </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>near the equator that </src> <tgt>赤道付近にある巨大な峡谷を確認しました。その峡谷は</tgt>; start=7.00, end=8.00
8. <src>stretches more than </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>600 miles. </src> <tgt>600マイル以上にわたって広がっています。</tgt>; start=9.00, end=10.00
10. <src>Scientists </src> <tgt>科学者たちは、</tgt>; start=10.00, end=11.00
11. <src>also found </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>organic materials </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>on its icy surface. </src> <tgt>その氷の表面に有機物も発見しています。</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=14.01
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_oINupCbfGEo_W000003 ===

source:
- language: English
- transcription: Images show the surface of Charon is mostly covered by water ice. We saw steep cliffs and a giant canyon near the equator that stretches more than 600 miles. Scientists also found organic materials on its icy surface.
- source_tokens:
  0. Images
  1. show
  2. the
  3. surface
  4. of
  5. Charon
  6. is
  7. mostly
  8. covered
  9. by
  10. water
  11. ice.
  12. We
  13. saw
  14. steep
  15. cliffs
  16. and
  17. a
  18. giant
  19. canyon
  20. near
  21. the
  22. equator
  23. that
  24. stretches
  25. more
  26. than
  27. 600
  28. miles.
  29. Scientists
  30. also
  31. found
  32. organic
  33. materials
  34. on
  35. its
  36. icy
  37. surface.

target:
- language: Korean
- translation: 이미지에 따르면 카론의 표면은 대부분 얼음으로 덮여 있습니다. 우리는 가파른 절벽을 보았고, 적도 근처에는 거대한 협곡이 있었습니다. 그 협곡은 600마일 이상 뻗어 있습니다. 과학자들은 또한 얼음 표면에서 유기 물질을 발견했습니다.
- target_sense_units:
  0. 이미지에 따르면
  1. 카론의 표면은
  2. 대부분
  3. 얼음으로
  4. 덮여 있습니다.
  5. 우리는
  6. 가파른 절벽을
  7. 보았고,
  8. 적도 근처에는
  9. 거대한 협곡이
  10. 있었습니다.
  11. 그 협곡은
  12. 600마일 이상
  13. 뻗어 있습니다.
  14. 과학자들은
  15. 또한
  16. 얼음 표면에서
  17. 유기 물질을
  18. 발견했습니다.

scratchpad:
* target[0]: "이미지에 따르면"
  - source_tokens: `0: "Images", 1: "show"`
  - mapping_reason: The phrase "Images show" provides the source of information.
* target[1]: "카론의 표면은"
  - source_tokens: `5: "Charon", 3: "surface"`
  - mapping_reason: Specifies the subject (Charon's surface).
* target[2]: "대부분"
  - source_tokens: `7: "mostly"`
  - mapping_reason: Quantifier describing the coverage.
* target[3]: "얼음으로"
  - source_tokens: `10: "water", 11: "ice."`
  - mapping_reason: The material covering the surface.
* target[4]: "덮여 있습니다."
  - source_tokens: `6: "is", 8: "covered", 9: "by"`
  - mapping_reason: The state of the surface being covered.
* target[5]: "우리는"
  - source_tokens: `12: "We"`
  - mapping_reason: The subject of the observation.
* target[6]: "가파른 절벽을"
  - source_tokens: `14: "steep", 15: "cliffs"`
  - mapping_reason: The object observed.
* target[7]: "보았고,"
  - source_tokens: `13: "saw"`
  - mapping_reason: The action of observing.
* target[8]: "적도 근처에는"
  - source_tokens: `20: "near", 21: "the", 22: "equator"`
  - mapping_reason: Location of the canyon.
* target[9]: "거대한 협곡이"
  - source_tokens: `18: "giant", 19: "canyon"`
  - mapping_reason: The subject described as existing.
* target[10]: "있었습니다."
  - source_tokens: `19: "canyon"`
  - mapping_reason: Indicates the state/existence of the canyon.
* target[11]: "그 협곡은"
  - source_tokens: `19: "canyon"`
  - mapping_reason: Anaphoric reference to the canyon.
* target[12]: "600마일 이상"
  - source_tokens: `25: "more", 26: "than", 27: "600", 28: "miles."`
  - mapping_reason: Measurement of the stretch.
* target[13]: "뻗어 있습니다."
  - source_tokens: `24: "stretches"`
  - mapping_reason: The action of the canyon stretching.
* target[14]: "과학자들은"
  - source_tokens: `29: "Scientists"`
  - mapping_reason: The subject of the research.
* target[15]: "또한"
  - source_tokens: `30: "also"`
  - mapping_reason: Discourse connective indicating addition.
* target[16]: "얼음 표면에서"
  - source_tokens: `35: "its", 36: "icy", 37: "surface."`
  - mapping_reason: Location of the discovery.
* target[17]: "유기 물질을"
  - source_tokens: `32: "organic", 33: "materials"`
  - mapping_reason: The object discovered.
* target[18]: "발견했습니다."
  - source_tokens: `31: "found"`
  - mapping_reason: The action of discovering.

result:
```html
0. <src>Images show </src> <tgt>이미지에 따르면</tgt>; start=0.00, end=1.00
1. <src>the surface of Charon </src> <tgt>카론의 표면은</tgt>; start=1.00, end=2.00
2. <src>is mostly covered </src> <tgt>대부분</tgt>; start=2.00, end=3.00
3. <src>by water ice. </src> <tgt>얼음으로 덮여 있습니다.</tgt>; start=3.00, end=4.00
4. <src>We saw </src> <tgt>우리는</tgt>; start=4.00, end=5.00
5. <src>steep cliffs and </src> <tgt>가파른 절벽을 보았고,</tgt>; start=5.00, end=6.00
6. <src>a giant canyon </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>near the equator that </src> <tgt>적도 근처에는 거대한 협곡이 있었습니다. 그 협곡은</tgt>; start=7.00, end=8.00
8. <src>stretches more than </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>600 miles. </src> <tgt>600마일 이상 뻗어 있습니다.</tgt>; start=9.00, end=10.00
10. <src>Scientists </src> <tgt>과학자들은</tgt>; start=10.00, end=11.00
11. <src>also found </src> <tgt>또한</tgt>; start=11.00, end=12.00
12. <src>organic materials </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>on its icy surface. </src> <tgt>얼음 표면에서 유기 물질을 발견했습니다.</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=14.01
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[10]
  - verdict: mapping_error
  - reason: "The target unit '있었습니다' (existed) describes the state of the canyon (19), not the act of seeing (13)."
  - replace_source_tokens: 19: "canyon"
  validation:
    scratchpad:
* target[0]: "이미지에 따르면"
  - source_tokens: `0: "Images", 1: "show"`
  - mapping_reason: "Images" provides the subject, "show" implies the evidential source "according to".

* target[1]: "카론의 표면은"
  - source_tokens: `5: "Charon", 3: "surface"`
  - mapping_reason: Core noun phrase identifying the subject.

* target[2]: "대부분"
  - source_tokens: `7: "mostly"`
  - mapping_reason: Adverbial quantifier.

* target[3]: "얼음으로"
  - source_tokens: `10: "water", 11: "ice."`
  - mapping_reason: Lexical content of the material.

* target[4]: "덮여 있습니다."
  - source_tokens: `8: "covered", 9: "by"`
  - mapping_reason: Passive verb phrase describing the state.

* target[5]: "우리는"
  - source_tokens: `12: "We"`
  - mapping_reason: Subject pronoun.

* target[6]: "가파른 절벽을"
  - source_tokens: `14: "steep", 15: "cliffs"`
  - mapping_reason: Direct object phrase.

* target[7]: "보았고,"
  - source_tokens: `13: "saw"`
  - mapping_reason: Verb of perception.

* target[8]: "적도 근처에는"
  - source_tokens: `20: "near", 21: "the", 22: "equator"`
  - mapping_reason: Locative modifier.

* target[9]: "거대한 협곡이"
  - source_tokens: `18: "giant", 19: "canyon"`
  - mapping_reason: Subject of the second clause.

* target[10]: "있었습니다."
  - source_tokens: `13: "saw"`
  - mapping_reason: Existence/perception verb in the context of the second clause.

* target[11]: "그 협곡은"
  - source_tokens: `19: "canyon"`
  - mapping_reason: Anaphoric reference to the canyon.

* target[12]: "600마일 이상"
  - source_tokens: `25: "more", 26: "than", 27: "600", 28: "miles."`
  - mapping_reason: Quantified distance measurement.

* target[13]: "뻗어 있습니다."
  - source_tokens: `23: "that", 24: "stretches"`
  - mapping_reason: Verb describing the extent.

* target[14]: "과학자들은"
  - source_tokens: `29: "Scientists"`
  - mapping_reason: Subject of the final sentence.

* target[15]: "또한"
  - source_tokens: `30: "also"`
  - mapping_reason: Additive discourse marker.

* target[16]: "얼음 표면에서"
  - source_tokens: `35: "its", 36: "icy", 37: "surface."`
  - mapping_reason: Locative phrase referencing the surface.

* target[17]: "유기 물질을"
  - source_tokens: `32: "organic", 33: "materials"`
  - mapping_reason: Direct object.

* target[18]: "발견했습니다."
  - source_tokens: `31: "found"`
  - mapping_reason: Main verb of the final sentence.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [5, 3]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [7]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [10, 11]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [8, 9]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [14, 15]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [13]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [20, 21, 22]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [18, 19]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [13]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [25, 26, 27, 28]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [23, 24]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [29]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [30]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [35, 36, 37]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [32, 33]
  },
  {
    "target_senseunit_id": 18,
    "source_token_ids": [31]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== EN_oxvGebm2jXu_W000008 ===

source:
- language: English
- transcription: Harvard Business School professor Laura Huang has also done quite a bit of research when it comes to our "quote unquote" gut instincts, and she discusses the results in her book *Edge: Turning Adversity into Advantage*. She explains how these instincts can lead to some terrible decisions in both work and normal life.
- source_tokens:
  0. Harvard
  1. Business
  2. School
  3. professor
  4. Laura
  5. Huang
  6. has
  7. also
  8. done
  9. quite
  10. a
  11. bit
  12. of
  13. research
  14. when
  15. it
  16. comes
  17. to
  18. our"
  19. quote
  20. unquote"
  21. gut
  22. instincts,
  23. and
  24. she
  25. discusses
  26. the
  27. results
  28. in
  29. her
  30. book*
  31. Edge:
  32. Turning
  33. Adversity
  34. into
  35. Advantage*.
  36. She
  37. explains
  38. how
  39. these
  40. instincts
  41. can
  42. lead
  43. to
  44. some
  45. terrible
  46. decisions
  47. in
  48. both
  49. work
  50. and
  51. normal
  52. life.

target:
- language: Japanese
- translation: ハーバード・ビジネス・スクールのローラ・ファン教授は、いわゆる「直感」について多くの研究を行いました。そして、その成果を著書『Edge: Turning Adversity into Advantage（逆境を力に変える）』の中で論じています。彼女は、こうした直感が仕事や日常生活で、いかにひどい決断につながる可能性があるかを説明しています。
- target_sense_units:
  0. ハーバード・ビジネス・スクールの
  1. ローラ・ファン教授は、
  2. いわゆる「直感」
  3. について
  4. 多くの研究を
  5. 行いました。
  6. そして、
  7. その成果を
  8. 著書
  9. 『Edge:TurningAdversityintoAdvantage
  10. （逆境を力に変える）』
  11. の中で
  12. 論じています。
  13. 彼女は、
  14. こうした
  15. 直感が
  16. 仕事や日常生活で、
  17. いかに
  18. ひどい決断につながる
  19. 可能性があるか
  20. を説明しています。

scratchpad:
* target[0]: "ハーバード・ビジネス・スクールの"
  - source_tokens: `0: "Harvard", 1: "Business", 2: "School"`
  - mapping_reason: Proper noun phrase for the institution.
* target[1]: "ローラ・ファン教授は、"
  - source_tokens: `3: "professor", 4: "Laura", 5: "Huang"`
  - mapping_reason: Proper name and title.
* target[2]: "いわゆる「直感」"
  - source_tokens: `18: "our"", 19: "quote", 20: "unquote"", 21: "gut", 22: "instincts,"`
  - mapping_reason: Translation of "quote unquote gut instincts".
* target[3]: "について"
  - source_tokens: `14: "when", 15: "it", 16: "comes", 17: "to"`
  - mapping_reason: Idiomatic translation of "when it comes to".
* target[4]: "多くの研究を"
  - source_tokens: `9: "quite", 10: "a", 11: "bit", 12: "of", 13: "research"`
  - mapping_reason: Quantifier and noun phrase.
* target[5]: "行いました。"
  - source_tokens: `6: "has", 8: "done"`
  - mapping_reason: Verb phrase for research.
* target[6]: "そして、"
  - source_tokens: `7: "also", 23: "and"`
  - mapping_reason: Connective discourse marker.
* target[7]: "その成果を"
  - source_tokens: `26: "the", 27: "results"`
  - mapping_reason: Object reference.
* target[8]: "著書"
  - source_tokens: `30: "book*"`
  - mapping_reason: Noun for book.
* target[9]: "『Edge:TurningAdversityintoAdvantage"
  - source_tokens: `31: "Edge:", 32: "Turning", 33: "Adversity", 34: "into", 35: "Advantage*."`
  - mapping_reason: Book title.
* target[10]: "（逆境を力に変える）』"
  - source_tokens: `31: "Edge:", 32: "Turning", 33: "Adversity", 34: "into", 35: "Advantage*."`
  - mapping_reason: Translation of book title content.
* target[11]: "の中で"
  - source_tokens: `28: "in"`
  - mapping_reason: Preposition.
* target[12]: "論じています。"
  - source_tokens: `25: "discusses"`
  - mapping_reason: Verb for discussing results.
* target[13]: "彼女は、"
  - source_tokens: `24: "she", 36: "She"`
  - mapping_reason: Pronoun reference.
* target[14]: "こうした"
  - source_tokens: `39: "these"`
  - mapping_reason: Demonstrative adjective.
* target[15]: "直感が"
  - source_tokens: `40: "instincts"`
  - mapping_reason: Noun for instincts.
* target[16]: "仕事や日常生活で、"
  - source_tokens: `47: "in", 48: "both", 49: "work", 50: "and", 51: "normal", 52: "life."`
  - mapping_reason: Context of decisions.
* target[17]: "いかに"
  - source_tokens: `38: "how"`
  - mapping_reason: Manner adverb.
* target[18]: "ひどい決断につながる"
  - source_tokens: `42: "lead", 43: "to", 44: "some", 45: "terrible", 46: "decisions"`
  - mapping_reason: Verb phrase and object.
* target[19]: "可能性があるか"
  - source_tokens: `41: "can"`
  - mapping_reason: Modal verb for possibility.
* target[20]: "を説明しています。"
  - source_tokens: `37: "explains"`
  - mapping_reason: Verb for explanation.

result:
```html
0. <src>Harvard Business School </src> <tgt>ハーバード・ビジネス・スクールの</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>professor Laura Huang </src> <tgt>ローラ・ファン教授は、</tgt>; start=2.00, end=3.00
3. <src>has also done quite a bit of </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>research when it comes to </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>our" quote unquote" gut instincts, </src> <tgt>いわゆる「直感」について多くの研究を行いました。</tgt>; start=6.00, end=7.00
7. <src>and she discusses </src> <tgt>そして、</tgt>; start=7.00, end=8.00
8. <src>the results </src> <tgt>その成果を</tgt>; start=8.00, end=9.00
9. <src>in her book* Edge: </src> <tgt>著書</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>Turning Adversity into </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Advantage*. </src> <tgt>『Edge:TurningAdversityintoAdvantage（逆境を力に変える）』の中で論じています。</tgt>; start=12.00, end=13.00
13. <src>She explains how </src> <tgt>彼女は、</tgt>; start=13.00, end=14.00
14. <src>these instincts can lead to </src> <tgt>こうした直感が</tgt>; start=14.00, end=15.00
15. <src>some terrible decisions </src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src><|wait|></src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>in both work and </src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>normal life. </src> <tgt>仕事や日常生活で、いかにひどい決断につながる可能性があるかを説明しています。</tgt>; start=18.00, end=18.33
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_oxvGebm2jXu_W000008 ===

source:
- language: English
- transcription: Harvard Business School professor Laura Huang has also done quite a bit of research when it comes to our "quote unquote" gut instincts, and she discusses the results in her book *Edge: Turning Adversity into Advantage*. She explains how these instincts can lead to some terrible decisions in both work and normal life.
- source_tokens:
  0. Harvard
  1. Business
  2. School
  3. professor
  4. Laura
  5. Huang
  6. has
  7. also
  8. done
  9. quite
  10. a
  11. bit
  12. of
  13. research
  14. when
  15. it
  16. comes
  17. to
  18. our"
  19. quote
  20. unquote"
  21. gut
  22. instincts,
  23. and
  24. she
  25. discusses
  26. the
  27. results
  28. in
  29. her
  30. book*
  31. Edge:
  32. Turning
  33. Adversity
  34. into
  35. Advantage*.
  36. She
  37. explains
  38. how
  39. these
  40. instincts
  41. can
  42. lead
  43. to
  44. some
  45. terrible
  46. decisions
  47. in
  48. both
  49. work
  50. and
  51. normal
  52. life.

target:
- language: Korean
- translation: 하버드 비즈니스 스쿨의 로라 황 교수는 이른바 '직감'에 대해 또한 상당한 연구를 수행해 왔습니다. 그리고 그 결과를 그녀의 저서 *Edge: Turning Adversity into Advantage(역경을 기회로 바꾸는 법)*에서 논하고 있습니다. 그녀는 이러한 직감이 직장과 일상생활 모두에서 어떻게 끔찍한 결정으로 이어질 수 있는지 설명합니다.
- target_sense_units:
  0. 하버드 비즈니스 스쿨의
  1. 로라 황 교수는
  2. 이른바
  3. ' 직감' 에 대해
  4. 또한
  5. 상당한 연구를
  6. 수행해 왔습니다.
  7. 그리고
  8. 그 결과를
  9. 그녀의 저서*
  10. Edge:
  11. Turning Adversity into Advantage(
  12. 역경을 기회로 바꾸는
  13. 법) *에서
  14. 논하고 있습니다.
  15. 그녀는
  16. 이러한 직감이
  17. 직장과 일상생활 모두에서
  18. 어떻게
  19. 끔찍한 결정으로
  20. 이어질 수 있는지
  21. 설명합니다.

scratchpad:
* target[0]: "하버드 비즈니스 스쿨의"
  - source_tokens: `0: "Harvard", 1: "Business", 2: "School"`
  - mapping_reason: Direct translation of the institution name.
* target[1]: "로라 황 교수는"
  - source_tokens: `3: "professor", 4: "Laura", 5: "Huang"`
  - mapping_reason: Name and title.
* target[2]: "이른바"
  - source_tokens: `18: "our"", 19: "quote", 20: "unquote""`
  - mapping_reason: Translation of "quote unquote".
* target[3]: "' 직감' 에 대해"
  - source_tokens: `21: "gut", 22: "instincts,"`
  - mapping_reason: Translation of "gut instincts".
* target[4]: "또한"
  - source_tokens: `7: "also"`
  - mapping_reason: Adverbial modifier.
* target[5]: "상당한 연구를"
  - source_tokens: `9: "quite", 10: "a", 11: "bit", 12: "of", 13: "research"`
  - mapping_reason: Translation of "quite a bit of research".
* target[6]: "수행해 왔습니다."
  - source_tokens: `6: "has", 8: "done"`
  - mapping_reason: Present perfect verb phrase.
* target[7]: "그리고"
  - source_tokens: `23: "and"`
  - mapping_reason: Conjunction.
* target[8]: "그 결과를"
  - source_tokens: `26: "the", 27: "results"`
  - mapping_reason: Direct object of discussion.
* target[9]: "그녀의 저서*"
  - source_tokens: `29: "her", 30: "book*"`
  - mapping_reason: Possessive and noun.
* target[10]: "Edge:"
  - source_tokens: `31: "Edge:"`
  - mapping_reason: Book title part.
* target[11]: "Turning Adversity into Advantage("
  - source_tokens: `32: "Turning", 33: "Adversity", 34: "into", 35: "Advantage*."`
  - mapping_reason: Book title part.
* target[12]: "역경을 기회로 바꾸는"
  - source_tokens: `32: "Turning", 33: "Adversity", 34: "into", 35: "Advantage*."`
  - mapping_reason: Semantic translation of the book title.
* target[13]: "법) *에서"
  - source_tokens: `35: "Advantage*."`
  - mapping_reason: Translation of the book title suffix and preposition.
* target[14]: "논하고 있습니다."
  - source_tokens: `25: "discusses"`
  - mapping_reason: Main verb.
* target[15]: "그녀는"
  - source_tokens: `36: "She"`
  - mapping_reason: Subject pronoun.
* target[16]: "이러한 직감이"
  - source_tokens: `39: "these", 40: "instincts"`
  - mapping_reason: Demonstrative and noun.
* target[17]: "직장과 일상생활 모두에서"
  - source_tokens: `48: "both", 49: "work", 50: "and", 51: "normal", 52: "life."`
  - mapping_reason: Translation of "both work and normal life".
* target[18]: "어떻게"
  - source_tokens: `38: "how"`
  - mapping_reason: Interrogative adverb.
* target[19]: "끔찍한 결정으로"
  - source_tokens: `45: "terrible", 46: "decisions"`
  - mapping_reason: Adjective and noun.
* target[20]: "이어질 수 있는지"
  - source_tokens: `41: "can", 42: "lead", 43: "to"`
  - mapping_reason: Modal verb and phrasal verb.
* target[21]: "설명합니다."
  - source_tokens: `37: "explains"`
  - mapping_reason: Main verb.

result:
```html
0. <src>Harvard Business School </src> <tgt>하버드 비즈니스 스쿨의</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>professor Laura Huang </src> <tgt>로라 황 교수는</tgt>; start=2.00, end=3.00
3. <src>has also done quite a bit of </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>research when it comes to </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>our" quote unquote" gut instincts, </src> <tgt>이른바 ' 직감' 에 대해 또한 상당한 연구를 수행해 왔습니다.</tgt>; start=6.00, end=7.00
7. <src>and she discusses </src> <tgt>그리고</tgt>; start=7.00, end=8.00
8. <src>the results </src> <tgt>그 결과를</tgt>; start=8.00, end=9.00
9. <src>in her book* Edge: </src> <tgt>그녀의 저서* Edge:</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>Turning Adversity into </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Advantage*. </src> <tgt>Turning Adversity into Advantage( 역경을 기회로 바꾸는 법) *에서 논하고 있습니다.</tgt>; start=12.00, end=13.00
13. <src>She explains how </src> <tgt>그녀는</tgt>; start=13.00, end=14.00
14. <src>these instincts can lead to </src> <tgt>이러한 직감이</tgt>; start=14.00, end=15.00
15. <src>some terrible decisions </src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src><|wait|></src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>in both work and </src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>normal life. </src> <tgt>직장과 일상생활 모두에서 어떻게 끔찍한 결정으로 이어질 수 있는지 설명합니다.</tgt>; start=18.00, end=18.33
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_oxvGebm2jXu_W000008 ===

source:
- language: English
- transcription: Harvard Business School professor Laura Huang has also done quite a bit of research when it comes to our "quote unquote" gut instincts, and she discusses the results in her book *Edge: Turning Adversity into Advantage*. She explains how these instincts can lead to some terrible decisions in both work and normal life.
- source_tokens:
  0. Harvard
  1. Business
  2. School
  3. professor
  4. Laura
  5. Huang
  6. has
  7. also
  8. done
  9. quite
  10. a
  11. bit
  12. of
  13. research
  14. when
  15. it
  16. comes
  17. to
  18. our"
  19. quote
  20. unquote"
  21. gut
  22. instincts,
  23. and
  24. she
  25. discusses
  26. the
  27. results
  28. in
  29. her
  30. book*
  31. Edge:
  32. Turning
  33. Adversity
  34. into
  35. Advantage*.
  36. She
  37. explains
  38. how
  39. these
  40. instincts
  41. can
  42. lead
  43. to
  44. some
  45. terrible
  46. decisions
  47. in
  48. both
  49. work
  50. and
  51. normal
  52. life.

target:
- language: Chinese
- translation: 哈佛商学院教授劳拉·黄（Laura Huang）对“所谓”的直觉也做了不少研究，并在她的书《优势：化逆境为机遇》里讨论了相关结果。她解释了这些直觉如何在工作和日常生活中导致一些糟糕的决策。
- target_sense_units:
  0. 哈佛商学院教授
  1. 劳拉·黄（LauraHuang）
  2. 对
  3. “所谓”的直觉
  4. 也
  5. 做了不少研究，
  6. 并
  7. 在她的书
  8. 《优势：化逆境为机遇》
  9. 里
  10. 讨论了相关结果。
  11. 她解释
  12. 了
  13. 这些直觉
  14. 如何
  15. 在工作
  16. 和
  17. 日常生活
  18. 中
  19. 导致一些糟糕的决策。

scratchpad:
* target[0]: "哈佛商学院教授"
  - source_tokens: `0: "Harvard", 1: "Business", 2: "School", 3: "professor"`
  - mapping_reason: Direct translation of the title and institution.
* target[1]: "劳拉·黄（LauraHuang）"
  - source_tokens: `4: "Laura", 5: "Huang"`
  - mapping_reason: Proper name of the person.
* target[2]: "对"
  - source_tokens: `14: "when", 15: "it", 16: "comes", 17: "to"`
  - mapping_reason: Prepositional phrase mapping "when it comes to" to "对".
* target[3]: "“所谓”的直觉"
  - source_tokens: `18: "our"", 19: "quote", 20: "unquote"", 21: "gut", 22: "instincts,"`
  - mapping_reason: "quote unquote" maps to "所谓", "gut instincts" maps to "直觉".
* target[4]: "也"
  - source_tokens: `7: "also"`
  - mapping_reason: Adverbial marker.
* target[5]: "做了不少研究，"
  - source_tokens: `8: "done", 9: "quite", 10: "a", 11: "bit", 12: "of", 13: "research"`
  - mapping_reason: Verb phrase "done quite a bit of research".
* target[6]: "并"
  - source_tokens: `23: "and"`
  - mapping_reason: Conjunction.
* target[7]: "在她的书"
  - source_tokens: `28: "in", 29: "her", 30: "book*"`
  - mapping_reason: Prepositional phrase indicating location.
* target[8]: "《优势：化逆境为机遇》"
  - source_tokens: `31: "Edge:", 32: "Turning", 33: "Adversity", 34: "into", 35: "Advantage*."`
  - mapping_reason: Title of the book.
* target[9]: "里"
  - source_tokens: `28: "in"`
  - mapping_reason: Spatial particle indicating inside the book.
* target[10]: "讨论了相关结果。"
  - source_tokens: `25: "discusses", 26: "the", 27: "results"`
  - mapping_reason: Verb and object.
* target[11]: "她解释"
  - source_tokens: `36: "She", 37: "explains"`
  - mapping_reason: Subject and verb.
* target[12]: "了"
  - source_tokens: `37: "explains"`
  - mapping_reason: Aspect marker for completed action.
* target[13]: "这些直觉"
  - source_tokens: `39: "these", 40: "instincts"`
  - mapping_reason: Demonstrative and noun.
* target[14]: "如何"
  - source_tokens: `38: "how"`
  - mapping_reason: Interrogative/relative adverb.
* target[15]: "在工作"
  - source_tokens: `47: "in", 49: "work"`
  - mapping_reason: Prepositional phrase.
* target[16]: "和"
  - source_tokens: `48: "both", 50: "and"`
  - mapping_reason: Conjunction.
* target[17]: "日常生活"
  - source_tokens: `51: "normal", 52: "life."`
  - mapping_reason: Adjective and noun.
* target[18]: "中"
  - source_tokens: `47: "in"`
  - mapping_reason: Spatial/temporal marker.
* target[19]: "导致一些糟糕的决策。"
  - source_tokens: `41: "can", 42: "lead", 43: "to", 44: "some", 45: "terrible", 46: "decisions"`
  - mapping_reason: Verb phrase and object.

result:
```html
0. <src>Harvard Business School </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>professor Laura Huang </src> <tgt>哈佛商学院教授劳拉·黄（LauraHuang）</tgt>; start=2.00, end=3.00
3. <src>has also done quite a bit of </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>research when it comes to </src> <tgt>对</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>our" quote unquote" gut instincts, </src> <tgt>“所谓”的直觉也做了不少研究，</tgt>; start=6.00, end=7.00
7. <src>and she discusses </src> <tgt>并</tgt>; start=7.00, end=8.00
8. <src>the results </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>in her book* Edge: </src> <tgt>在她的书</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>Turning Adversity into </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Advantage*. </src> <tgt>《优势：化逆境为机遇》里讨论了相关结果。</tgt>; start=12.00, end=13.00
13. <src>She explains how </src> <tgt>她解释了</tgt>; start=13.00, end=14.00
14. <src>these instincts can lead to </src> <tgt>这些直觉如何</tgt>; start=14.00, end=15.00
15. <src>some terrible decisions </src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src><|wait|></src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>in both work and </src> <tgt>在工作和</tgt>; start=17.00, end=18.00
18. <src>normal life. </src> <tgt>日常生活中导致一些糟糕的决策。</tgt>; start=18.00, end=18.33
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
