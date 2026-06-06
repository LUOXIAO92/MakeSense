=== EN_nIpxsCym-BM_W000211 ===

source:
- language: English
- transcription: By default, if you create a file called source/index, it's then going to push whatever you put in that file, any imports you use, things like that, out to
- source_tokens:
  0. By
  1. default,
  2. if
  3. you
  4. create
  5. a
  6. file
  7. called
  8. source/index,
  9. it's
  10. then
  11. going
  12. to
  13. push
  14. whatever
  15. you
  16. put
  17. in
  18. that
  19. file,
  20. any
  21. imports
  22. you
  23. use,
  24. things
  25. like
  26. that,
  27. out
  28. to

target:
- language: Chinese
- translation: 默认情况下，如果你创建一个名为 source/index 的文件，它就会把你放在该文件里的任何内容、你用的任何导入、等等，推送到
- target_sense_units:
  0. 默认情况下，
  1. 如果
  2. 你创建
  3. 一个
  4. 名为
  5. source/index的
  6. 文件，
  7. 它就会
  8. 把你
  9. 放在
  10. 该文件里的
  11. 任何内容、
  12. 你用的
  13. 任何导入、
  14. 等等，
  15. 推送到

scratchpad:
* target[0]: "默认情况下，"
  - source_tokens: `0: "By", 1: "default,"`
  - mapping_reason: Direct translation of "By default".

* target[1]: "如果"
  - source_tokens: `2: "if"`
  - mapping_reason: Direct translation of "if".

* target[2]: "你创建"
  - source_tokens: `3: "you", 4: "create"`
  - mapping_reason: Subject "you" and verb "create".

* target[3]: "一个"
  - source_tokens: `5: "a"`
  - mapping_reason: Indefinite article "a".

* target[4]: "名为"
  - source_tokens: `7: "called"`
  - mapping_reason: Translation of "called" as naming verb.

* target[5]: "source/index的"
  - source_tokens: `8: "source/index,"`
  - mapping_reason: The file name token.

* target[6]: "文件，"
  - source_tokens: `6: "file"`
  - mapping_reason: The noun "file".

* target[7]: "它就会"
  - source_tokens: `9: "it's", 10: "then"`
  - mapping_reason: "It" (subject) + "then" (temporal/logical sequence).

* target[8]: "把你"
  - source_tokens: `15: "you"`
  - mapping_reason: The object "you" (in "you put").

* target[9]: "放在"
  - source_tokens: `16: "put"`
  - mapping_reason: The verb "put".

* target[10]: "该文件里的"
  - source_tokens: `17: "in", 18: "that", 19: "file,"`
  - mapping_reason: Prepositional phrase modifying the content.

* target[11]: "任何内容、"
  - source_tokens: `14: "whatever"`
  - mapping_reason: The pronoun "whatever".

* target[12]: "你用的"
  - source_tokens: `22: "you", 23: "use,"`
  - mapping_reason: Relative clause "you use".

* target[13]: "任何导入、"
  - source_tokens: `20: "any", 21: "imports"`
  - mapping_reason: The noun phrase "any imports".

* target[14]: "等等，"
  - source_tokens: `24: "things", 25: "like", 26: "that,"`
  - mapping_reason: Idiomatic translation of "things like that".

* target[15]: "推送到"
  - source_tokens: `11: "going", 12: "to", 13: "push", 27: "out", 28: "to"`
  - mapping_reason: Phrasal verb "push out to" and auxiliary "going to".

result:
```html
0. <src>By default, </src> <tgt>默认情况下，</tgt>; start=0.00, end=1.00
1. <src>if you create </src> <tgt>如果你创建</tgt>; start=1.00, end=2.00
2. <src>a file </src> <tgt>一个</tgt>; start=2.00, end=3.00
3. <src>called source/index, </src> <tgt>名为source/index的文件，</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>it's then going to push </src> <tgt>它就会</tgt>; start=5.00, end=6.00
6. <src>whatever you put in </src> <tgt>把你放在</tgt>; start=6.00, end=7.00
7. <src>that file, </src> <tgt>该文件里的任何内容、</tgt>; start=7.00, end=8.00
8. <src>any imports you use, </src> <tgt>你用的任何导入、</tgt>; start=8.00, end=9.00
9. <src>things like that, </src> <tgt>等等，</tgt>; start=9.00, end=10.00
10. <src>out to </src> <tgt>推送到</tgt>; start=10.00, end=10.78
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nIpxsCym-BM_W000211 ===

source:
- language: English
- transcription: By default, if you create a file called source/index, it's then going to push whatever you put in that file, any imports you use, things like that, out to
- source_tokens:
  0. By
  1. default,
  2. if
  3. you
  4. create
  5. a
  6. file
  7. called
  8. source/index,
  9. it's
  10. then
  11. going
  12. to
  13. push
  14. whatever
  15. you
  16. put
  17. in
  18. that
  19. file,
  20. any
  21. imports
  22. you
  23. use,
  24. things
  25. like
  26. that,
  27. out
  28. to

target:
- language: Korean
- translation: 기본적으로 source/index라는 파일을 만들면, 그 파일에 넣은 내용, 사용하는 임포트, 그런 것들을 모두
- target_sense_units:
  0. 기본적으로
  1. source/index라는
  2. 파일을
  3. 만들면,
  4. 그 파일에
  5. 넣은 내용,
  6. 사용하는 임포트,
  7. 그런 것들을
  8. 모두

scratchpad:
* target[0]: "기본적으로"
  - source_tokens: `0: "By", 1: "default,"`
  - mapping_reason: Direct translation of "By default".

* target[1]: "source/index라는"
  - source_tokens: `8: "source/index," 7: "called"`
  - mapping_reason: "source/index" is the name, "called" provides the naming relation.

* target[2]: "파일을"
  - source_tokens: `6: "file"`
  - mapping_reason: Direct translation of "file".

* target[3]: "만들면,"
  - source_tokens: `2: "if", 4: "create"`
  - mapping_reason: "if" provides the conditional, "create" is the action.

* target[4]: "그 파일에"
  - source_tokens: `18: "that", 19: "file,"`
  - mapping_reason: Direct translation of "that file".

* target[5]: "넣은 내용,"
  - source_tokens: `14: "whatever", 15: "you", 16: "put"`
  - mapping_reason: "whatever you put" corresponds to the content placed in the file.

* target[6]: "사용하는 임포트,"
  - source_tokens: `21: "imports", 22: "you", 23: "use,"`
  - mapping_reason: "imports you use" corresponds to the imports utilized.

* target[7]: "그런 것들을"
  - source_tokens: `24: "things", 25: "like", 26: "that,"`
  - mapping_reason: "things like that" corresponds to the phrase.

* target[8]: "모두"
  - source_tokens: `14: "whatever"`
  - mapping_reason: "whatever" implies "all" of the mentioned items.

result:
```html
0. <src>By default, </src> <tgt>기본적으로</tgt>; start=0.00, end=1.00
1. <src>if you create </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>a file </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>called source/index, </src> <tgt>source/index라는 파일을 만들면,</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>it's then going to push </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>whatever you put in </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>that file, </src> <tgt>그 파일에 넣은 내용,</tgt>; start=7.00, end=8.00
8. <src>any imports you use, </src> <tgt>사용하는 임포트,</tgt>; start=8.00, end=9.00
9. <src>things like that, </src> <tgt>그런 것들을 모두</tgt>; start=9.00, end=10.00
10. <src>out to </src> <tgt><|wait|></tgt>; start=10.00, end=10.78
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_n_UNfbRo_MQ_W000005 ===

source:
- language: English
- transcription: But the Commonwealth Department of Agriculture, Fisheries and Forestry had the foresight to identify the need for Australia to be ahead of the game and well coordinated, and so developed the Australian Animal Welfare Strategy eight years ago.
- source_tokens:
  0. But
  1. the
  2. Commonwealth
  3. Department
  4. of
  5. Agriculture,
  6. Fisheries
  7. and
  8. Forestry
  9. had
  10. the
  11. foresight
  12. to
  13. identify
  14. the
  15. need
  16. for
  17. Australia
  18. to
  19. be
  20. ahead
  21. of
  22. the
  23. game
  24. and
  25. well
  26. coordinated,
  27. and
  28. so
  29. developed
  30. the
  31. Australian
  32. Animal
  33. Welfare
  34. Strategy
  35. eight
  36. years
  37. ago.

target:
- language: Chinese
- translation: 但联邦农业、渔业和林业部具有远见卓识，认识到澳大利亚需要抢占先机并保持协调一致。因此，八年前制定了《澳大利亚动物福利战略》。
- target_sense_units:
  0. 但
  1. 联邦农业、
  2. 渔业和林业部
  3. 具有远见卓识，
  4. 认识到
  5. 澳大利亚需要抢占先机
  6. 并
  7. 保持协调一致。
  8. 因此，
  9. 八年前
  10. 制定了
  11. 《澳大利亚动物福利战略》。

scratchpad:
* target[0]: "但"
  - source_tokens: `0: "But"`
  - mapping_reason: Contrastive conjunction.

* target[1]: "联邦农业、"
  - source_tokens: `1: "the", 2: "Commonwealth", 3: "Department", 4: "of", 5: "Agriculture,"`
  - mapping_reason: Proper noun phrase component.

* target[2]: "渔业和林业部"
  - source_tokens: `6: "Fisheries", 7: "and", 8: "Forestry"`
  - mapping_reason: Proper noun phrase component.

* target[3]: "具有远见卓识，"
  - source_tokens: `9: "had", 10: "the", 11: "foresight"`
  - mapping_reason: Predicate expressing foresight.

* target[4]: "认识到"
  - source_tokens: `13: "identify", 14: "the", 15: "need"`
  - mapping_reason: Cognitive action of identifying a requirement.

* target[5]: "澳大利亚需要抢占先机"
  - source_tokens: `17: "Australia", 18: "to", 19: "be", 20: "ahead", 21: "of", 22: "the", 23: "game"`
  - mapping_reason: Condition/goal identified for Australia.

* target[6]: "并"
  - source_tokens: `24: "and"`
  - mapping_reason: Conjunction.

* target[7]: "保持协调一致。"
  - source_tokens: `25: "well", 26: "coordinated,"`
  - mapping_reason: State of being well-coordinated.

* target[8]: "因此，"
  - source_tokens: `27: "and", 28: "so"`
  - mapping_reason: Resultative discourse marker.

* target[9]: "八年前"
  - source_tokens: `35: "eight", 36: "years", 37: "ago."`
  - mapping_reason: Temporal adjunct.

* target[10]: "制定了"
  - source_tokens: `29: "developed"`
  - mapping_reason: Action of development.

* target[11]: "《澳大利亚动物福利战略》。"
  - source_tokens: `30: "the", 31: "Australian", 32: "Animal", 33: "Welfare", 34: "Strategy"`
  - mapping_reason: Object of the development action.

result:
```html
0. <src>But the Commonwealth </src> <tgt>但</tgt>; start=0.00, end=1.00
1. <src>Department of Agriculture, </src> <tgt>联邦农业、</tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>Fisheries and Forestry </src> <tgt>渔业和林业部</tgt>; start=3.00, end=4.00
4. <src>had the foresight to </src> <tgt>具有远见卓识，</tgt>; start=4.00, end=5.00
5. <src>identify the need for </src> <tgt>认识到</tgt>; start=5.00, end=6.00
6. <src>Australia to be </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>ahead of the game </src> <tgt>澳大利亚需要抢占先机</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>and well coordinated, </src> <tgt>并保持协调一致。</tgt>; start=9.00, end=10.00
10. <src>and so developed the </src> <tgt>因此，</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Australian Animal Welfare Strategy </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt>八年前制定了《澳大利亚动物福利战略》。</tgt>; start=13.00, end=13.66
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nIpxsCym-BM_W000211 ===

source:
- language: English
- transcription: By default, if you create a file called source/index, it's then going to push whatever you put in that file, any imports you use, things like that, out to
- source_tokens:
  0. By
  1. default,
  2. if
  3. you
  4. create
  5. a
  6. file
  7. called
  8. source/index,
  9. it's
  10. then
  11. going
  12. to
  13. push
  14. whatever
  15. you
  16. put
  17. in
  18. that
  19. file,
  20. any
  21. imports
  22. you
  23. use,
  24. things
  25. like
  26. that,
  27. out
  28. to

target:
- language: Japanese
- translation: デフォルトでは、source/index というファイルを作成すると、そのファイルに入れたものや、使っているインポートなど、すべてが
- target_sense_units:
  0. デフォルトでは、
  1. source/index
  2. という
  3. ファイルを
  4. 作成すると、
  5. そのファイルに
  6. 入れた
  7. ものや、
  8. 使っている
  9. インポートなど、
  10. すべてが

scratchpad:
* target[0]: "デフォルトでは、"
  - source_tokens: `0: "By", 1: "default,"`
  - mapping_reason: Standard translation of the phrase "By default".

* target[1]: "source/index"
  - source_tokens: `8: "source/index,"`
  - mapping_reason: Direct reference to the file path.

* target[2]: "という"
  - source_tokens: `7: "called"`
  - mapping_reason: "called" functions as the identifier marker "という".

* target[3]: "ファイルを"
  - source_tokens: `6: "file"`
  - mapping_reason: Core noun indicating the file object.

* target[4]: "作成すると、"
  - source_tokens: `2: "if", 3: "you", 4: "create"`
  - mapping_reason: Conditional structure mapping to "if you create".

* target[5]: "そのファイルに"
  - source_tokens: `18: "that", 19: "file,"`
  - mapping_reason: Reference to the previously mentioned file.

* target[6]: "入れた"
  - source_tokens: `16: "put"`
  - mapping_reason: Verb indicating content placement.

* target[7]: "ものや、"
  - source_tokens: `14: "whatever"`
  - mapping_reason: "whatever" translates to "things/content" (もの).

* target[8]: "使っている"
  - source_tokens: `23: "use,"`
  - mapping_reason: Verb indicating usage of imports.

* target[9]: "インポートなど、"
  - source_tokens: `21: "imports"`
  - mapping_reason: Core noun "imports" plus the "etc" marker derived from "things like that".

* target[10]: "すべてが"
  - source_tokens: `14: "whatever", 20: "any", 24: "things", 25: "like", 26: "that,"`
  - mapping_reason: The collective scope of the items being pushed, derived from the list structure.

result:
```html
0. <src>By default, </src> <tgt>デフォルトでは、</tgt>; start=0.00, end=1.00
1. <src>if you create </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>a file </src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>called source/index, </src> <tgt>source/indexというファイルを作成すると、</tgt>; start=3.00, end=4.00
4. <src><|wait|></src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>it's then going to push </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>whatever you put in </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>that file, </src> <tgt>そのファイルに入れたものや、</tgt>; start=7.00, end=8.00
8. <src>any imports you use, </src> <tgt>使っているインポートなど、</tgt>; start=8.00, end=9.00
9. <src>things like that, </src> <tgt>すべてが</tgt>; start=9.00, end=10.00
10. <src>out to </src> <tgt><|wait|></tgt>; start=10.00, end=10.78
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nCDIj7Cde90_W000000 ===

source:
- language: English
- transcription: I'm sorry for not making a video in three hours, but I wanted to tell you I am very sorry that I had to hit three other people like in the same place within less than ten minutes. I also thought that I could be banned from that location because I was being aggressive to them, and this meant.
- source_tokens:
  0. I'm
  1. sorry
  2. for
  3. not
  4. making
  5. a
  6. video
  7. in
  8. three
  9. hours,
  10. but
  11. I
  12. wanted
  13. to
  14. tell
  15. you
  16. I
  17. am
  18. very
  19. sorry
  20. that
  21. I
  22. had
  23. to
  24. hit
  25. three
  26. other
  27. people
  28. like
  29. in
  30. the
  31. same
  32. place
  33. within
  34. less
  35. than
  36. ten
  37. minutes.
  38. I
  39. also
  40. thought
  41. that
  42. I
  43. could
  44. be
  45. banned
  46. from
  47. that
  48. location
  49. because
  50. I
  51. was
  52. being
  53. aggressive
  54. to
  55. them,
  56. and
  57. this
  58. meant.

target:
- language: Chinese
- translation: 很抱歉三个小时没发视频了。但我得告诉你们，我很抱歉在不到十分钟内，在同一个地方撞到了另外三个人。我还以为我会被那个地方禁入，因为我对他们表现得很有攻击性。这意味着。
- target_sense_units:
  0. 很抱歉
  1. 三个小时
  2. 没发视频了。
  3. 但
  4. 我得告诉你们，
  5. 我很抱歉
  6. 在不到十分钟内，
  7. 在同一个地方
  8. 撞到了
  9. 另外三个人。
  10. 我还以为
  11. 我会
  12. 被那个地方禁入，
  13. 因为
  14. 我对他们
  15. 表现得
  16. 很有攻击性。
  17. 这意味着。

scratchpad:
* target[0]: "很抱歉"
  - source_tokens: `0: "I'm", 1: "sorry"`
  - mapping_reason: Expresses the speaker's apology.
* target[1]: "三个小时"
  - source_tokens: `8: "three", 9: "hours,"`
  - mapping_reason: Time duration modifier.
* target[2]: "没发视频了。"
  - source_tokens: `2: "for", 3: "not", 4: "making", 5: "a", 6: "video"`
  - mapping_reason: The action that was not performed.
* target[3]: "但"
  - source_tokens: `10: "but"`
  - mapping_reason: Contrastive conjunction.
* target[4]: "我得告诉你们，"
  - source_tokens: `11: "I", 12: "wanted", 13: "to", 14: "tell", 15: "you"`
  - mapping_reason: Communicative intent.
* target[5]: "我很抱歉"
  - source_tokens: `16: "I", 17: "am", 18: "very", 19: "sorry"`
  - mapping_reason: Second apology.
* target[6]: "在不到十分钟内，"
  - source_tokens: `33: "within", 34: "less", 35: "than", 36: "ten", 37: "minutes."`
  - mapping_reason: Time frame of the incident.
* target[7]: "在同一个地方"
  - source_tokens: `29: "in", 30: "the", 31: "same", 32: "place"`
  - mapping_reason: Location of the incident.
* target[8]: "撞到了"
  - source_tokens: `24: "hit"`
  - mapping_reason: Core action.
* target[9]: "另外三个人。"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: Objects of the action.
* target[10]: "我还以为"
  - source_tokens: `38: "I", 39: "also", 40: "thought"`
  - mapping_reason: Speaker's belief.
* target[11]: "我会"
  - source_tokens: `43: "could"`
  - mapping_reason: Modal indicating possibility.
* target[12]: "被那个地方禁入，"
  - source_tokens: `44: "be", 45: "banned", 46: "from", 47: "that", 48: "location"`
  - mapping_reason: Consequence of being banned.
* target[13]: "因为"
  - source_tokens: `49: "because"`
  - mapping_reason: Causal conjunction.
* target[14]: "我对他们"
  - source_tokens: `50: "I", 54: "to", 55: "them,"`
  - mapping_reason: Target of the behavior.
* target[15]: "表现得"
  - source_tokens: `51: "was", 52: "being"`
  - mapping_reason: Manner of behavior.
* target[16]: "很有攻击性。"
  - source_tokens: `53: "aggressive"`
  - mapping_reason: Descriptor of behavior.
* target[17]: "这意味着。"
  - source_tokens: `56: "and", 57: "this", 58: "meant."`
  - mapping_reason: Concluding clause.

result:
```html
0. <src>I'm sorry </src> <tgt>很抱歉</tgt>; start=0.00, end=1.00
1. <src>for not making a video </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>in three hours, </src> <tgt>三个小时没发视频了。</tgt>; start=2.00, end=3.00
3. <src>but I wanted to </src> <tgt>但</tgt>; start=3.00, end=4.00
4. <src>tell you </src> <tgt>我得告诉你们，</tgt>; start=4.00, end=5.00
5. <src>I am very sorry </src> <tgt>我很抱歉</tgt>; start=5.00, end=6.00
6. <src>that I had to </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>hit three other people </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>like </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>in the same place </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>within less than ten minutes. </src> <tgt>在不到十分钟内，在同一个地方撞到了另外三个人。</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>I also thought that I could </src> <tgt>我还以为我会</tgt>; start=15.00, end=16.00
16. <src>be banned from </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>that location </src> <tgt>被那个地方禁入，</tgt>; start=17.00, end=18.00
18. <src>because I was </src> <tgt>因为</tgt>; start=18.00, end=19.00
19. <src>being aggressive </src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>to them, </src> <tgt>我对他们表现得很有攻击性。</tgt>; start=20.00, end=21.00
21. <src><|wait|></src> <tgt><|wait|></tgt>; start=21.00, end=22.00
22. <src>and this meant. </src> <tgt>这意味着。</tgt>; start=22.00, end=22.20
```

- max_empty_window_count: 7


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nvdVVhi8VpA_W000110 ===

source:
- language: English
- transcription: Um, 42% of the way through the course, so as you can see, each pie slice represents a different topic, and they have a little bit more to learn in in matter, and a little bit more in atoms and ions and molecules. But you know, so this is telling you that.
- source_tokens:
  0. Um,
  1. 42%
  2. of
  3. the
  4. way
  5. through
  6. the
  7. course,
  8. so
  9. as
  10. you
  11. can
  12. see,
  13. each
  14. pie
  15. slice
  16. represents
  17. a
  18. different
  19. topic,
  20. and
  21. they
  22. have
  23. a
  24. little
  25. bit
  26. more
  27. to
  28. learn
  29. in
  30. in
  31. matter,
  32. and
  33. a
  34. little
  35. bit
  36. more
  37. in
  38. atoms
  39. and
  40. ions
  41. and
  42. molecules.
  43. But
  44. you
  45. know,
  46. so
  47. this
  48. is
  49. telling
  50. you
  51. that.

target:
- language: Chinese
- translation: 嗯，课程已经进行了42%，正如你们所见，每一块饼图代表一个不同的主题，他们在物质方面还有一点需要学习，在原子、离子和分子方面也还有一点。但你知道，说白了，这就是在告诉大家这点。
- target_sense_units:
  0. 嗯，
  1. 课程已经进行了42%，
  2. 正如你们所见，
  3. 每一块饼图
  4. 代表一个
  5. 不同的主题，
  6. 他们
  7. 在物质方面
  8. 还有一点
  9. 需要学习，
  10. 在原子、离子
  11. 和分子方面
  12. 也还有一点。
  13. 但
  14. 你知道，
  15. 说白了，
  16. 这就是
  17. 在告诉大家这点。

scratchpad:
* target[0]: "嗯，"
  - source_tokens: `0: "Um,"`
  - mapping_reason: Direct discourse marker translation.

* target[1]: "课程已经进行了42%，"
  - source_tokens: `1: "42%", 2: "of", 3: "the", 4: "way", 5: "through", 6: "the", 7: "course,"`
  - mapping_reason: Expresses the progress state of the course.

* target[2]: "正如你们所见，"
  - source_tokens: `9: "as", 10: "you", 11: "can", 12: "see,"`
  - mapping_reason: Direct translation of the observation clause.

* target[3]: "每一块饼图"
  - source_tokens: `13: "each", 14: "pie", 15: "slice"`
  - mapping_reason: Subject of the sentence representing the segments.

* target[4]: "代表一个"
  - source_tokens: `16: "represents", 17: "a"`
  - mapping_reason: Verb and indefinite article.

* target[5]: "不同的主题，"
  - source_tokens: `18: "different", 19: "topic,"`
  - mapping_reason: Object of the representation.

* target[6]: "他们"
  - source_tokens: `21: "they"`
  - mapping_reason: Subject reference to students.

* target[7]: "在物质方面"
  - source_tokens: `29: "in", 31: "matter,"`
  - mapping_reason: Prepositional phrase specifying the subject area.

* target[8]: "还有一点"
  - source_tokens: `23: "a", 24: "little", 25: "bit", 26: "more"`
  - mapping_reason: Quantity of material remaining.

* target[9]: "需要学习，"
  - source_tokens: `27: "to", 28: "learn"`
  - mapping_reason: Verbal action required.

* target[10]: "在原子、离子"
  - source_tokens: `37: "in", 38: "atoms", 39: "and", 40: "ions"`
  - mapping_reason: Second subject area.

* target[11]: "和分子方面"
  - source_tokens: `41: "and", 42: "molecules."`
  - mapping_reason: Final part of the second subject area.

* target[12]: "也还有一点。"
  - source_tokens: `33: "a", 34: "little", 35: "bit", 36: "more"`
  - mapping_reason: Quantity of remaining material for the second area.

* target[13]: "但"
  - source_tokens: `43: "But"`
  - mapping_reason: Contrastive conjunction.

* target[14]: "你知道，"
  - source_tokens: `44: "you", 45: "know,"`
  - mapping_reason: Discourse marker.

* target[15]: "说白了，"
  - source_tokens: `8: "so", 46: "so"`
  - mapping_reason: Discourse filler/connector conveying summary intent.

* target[16]: "这就是"
  - source_tokens: `47: "this", 48: "is"`
  - mapping_reason: Demonstrative subject and verb.

* target[17]: "在告诉大家这点。"
  - source_tokens: `49: "telling", 50: "you", 51: "that."`
  - mapping_reason: Verb and object indicating the communicative purpose.

result:
```html
0. <src>Um, </src> <tgt>嗯，</tgt>; start=0.00, end=1.00
1. <src>42% of the way through </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>the course, </src> <tgt>课程已经进行了42%，</tgt>; start=2.00, end=3.00
3. <src>so as you can see, </src> <tgt>正如你们所见，</tgt>; start=3.00, end=4.00
4. <src>each pie slice </src> <tgt>每一块饼图</tgt>; start=4.00, end=5.00
5. <src>represents </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>a different topic, and </src> <tgt>代表一个不同的主题，</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>they have </src> <tgt>他们</tgt>; start=8.00, end=9.00
9. <src>a little bit more to learn </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>in in matter, and </src> <tgt>在物质方面还有一点需要学习，</tgt>; start=10.00, end=11.00
11. <src>a little bit more </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>in atoms and ions </src> <tgt>在原子、离子</tgt>; start=12.00, end=13.00
13. <src>and molecules. </src> <tgt>和分子方面也还有一点。</tgt>; start=13.00, end=14.00
14. <src>But you </src> <tgt>但</tgt>; start=14.00, end=15.00
15. <src>know, so this is </src> <tgt>你知道，说白了，这就是</tgt>; start=15.00, end=16.00
16. <src>telling you that. </src> <tgt>在告诉大家这点。</tgt>; start=16.00, end=16.94
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nsPdq5m1h0y_W000029 ===

source:
- language: English
- transcription: We get the mass by taking the number of protons, which is always 35 for bromine, and we add it to the number of neutrons, which is new for this isotope. So 35 plus 47 is a mass of 82.
- source_tokens:
  0. We
  1. get
  2. the
  3. mass
  4. by
  5. taking
  6. the
  7. number
  8. of
  9. protons,
  10. which
  11. is
  12. always
  13. 35
  14. for
  15. bromine,
  16. and
  17. we
  18. add
  19. it
  20. to
  21. the
  22. number
  23. of
  24. neutrons,
  25. which
  26. is
  27. new
  28. for
  29. this
  30. isotope.
  31. So
  32. 35
  33. plus
  34. 47
  35. is
  36. a
  37. mass
  38. of
  39. 82.

target:
- language: Korean
- translation: 질량은 양성자 수(브롬의 경우 항상 35개)와 중성자 수를 더해서 구합니다. 이 동위 원소의 중성자 수는 새로운 값입니다. 따라서 35 더하기 47은 질량 82가 됩니다.
- target_sense_units:
  0. 질량은
  1. 양성자 수(
  2. 브롬의 경우
  3. 항상 35개 )와
  4. 중성자 수를
  5. 더해서
  6. 구합니다.
  7. 이 동위 원소의
  8. 중성자 수는
  9. 새로운 값입니다.
  10. 따라서
  11. 35 더하기 47은
  12. 질량 82가
  13. 됩니다.

scratchpad:
* target[0]: "질량은"
  - source_tokens: `2: "the", 3: "mass"`
  - mapping_reason: Represents the subject 'mass'.

* target[1]: "양성자 수("
  - source_tokens: `6: "the", 7: "number", 8: "of", 9: "protons,"`
  - mapping_reason: Represents the count of protons.

* target[2]: "브롬의 경우"
  - source_tokens: `14: "for", 15: "bromine,"`
  - mapping_reason: Specifies the context of bromine.

* target[3]: "항상 35개 )와"
  - source_tokens: `10: "which", 11: "is", 12: "always", 13: "35", 16: "and"`
  - mapping_reason: Provides the constant value 35 and the conjunction.

* target[4]: "중성자 수를"
  - source_tokens: `21: "the", 22: "number", 23: "of", 24: "neutrons,"`
  - mapping_reason: Represents the count of neutrons.

* target[5]: "더해서"
  - source_tokens: `18: "add"`
  - mapping_reason: Represents the addition operation.

* target[6]: "구합니다."
  - source_tokens: `0: "We", 1: "get", 4: "by", 5: "taking"`
  - mapping_reason: Represents the method of calculation.

* target[7]: "이 동위 원소의"
  - source_tokens: `29: "this", 30: "isotope."`
  - mapping_reason: Specifies the subject isotope.

* target[8]: "중성자 수는"
  - source_tokens: `21: "the", 22: "number", 23: "of", 24: "neutrons,"`
  - mapping_reason: Refers back to the count of neutrons.

* target[9]: "새로운 값입니다."
  - source_tokens: `25: "which", 26: "is", 27: "new"`
  - mapping_reason: Describes the neutron count as new.

* target[10]: "따라서"
  - source_tokens: `31: "So"`
  - mapping_reason: Logical connective.

* target[11]: "35 더하기 47은"
  - source_tokens: `32: "35", 33: "plus", 34: "47"`
  - mapping_reason: Mathematical operation.

* target[12]: "질량 82가"
  - source_tokens: `37: "mass", 39: "82."`
  - mapping_reason: Resulting mass value.

* target[13]: "됩니다."
  - source_tokens: `35: "is", 36: "a", 38: "of"`
  - mapping_reason: Copula/verb structure connecting the result.

result:
```html
0. <src>We get the mass </src> <tgt>질량은</tgt>; start=0.00, end=1.00
1. <src>by taking the number of </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>protons, </src> <tgt>양성자 수(</tgt>; start=2.00, end=3.00
3. <src>which is always 35 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>for bromine, </src> <tgt>브롬의 경우</tgt>; start=4.00, end=5.00
5. <src>and we add </src> <tgt>항상 35개 )와</tgt>; start=5.00, end=6.00
6. <src>it to the number of </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>neutrons, </src> <tgt>중성자 수를 더해서 구합니다.</tgt>; start=7.00, end=8.00
8. <src>which is new </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>for this isotope. So </src> <tgt>이 동위 원소의 중성자 수는 새로운 값입니다. 따라서</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>35 plus 47 </src> <tgt>35 더하기 47은</tgt>; start=11.00, end=12.00
12. <src>is a mass of </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>82. </src> <tgt>질량 82가 됩니다.</tgt>; start=13.00, end=13.53
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_n_UNfbRo_MQ_W000005 ===

source:
- language: English
- transcription: But the Commonwealth Department of Agriculture, Fisheries and Forestry had the foresight to identify the need for Australia to be ahead of the game and well coordinated, and so developed the Australian Animal Welfare Strategy eight years ago.
- source_tokens:
  0. But
  1. the
  2. Commonwealth
  3. Department
  4. of
  5. Agriculture,
  6. Fisheries
  7. and
  8. Forestry
  9. had
  10. the
  11. foresight
  12. to
  13. identify
  14. the
  15. need
  16. for
  17. Australia
  18. to
  19. be
  20. ahead
  21. of
  22. the
  23. game
  24. and
  25. well
  26. coordinated,
  27. and
  28. so
  29. developed
  30. the
  31. Australian
  32. Animal
  33. Welfare
  34. Strategy
  35. eight
  36. years
  37. ago.

target:
- language: Korean
- translation: 하지만 연방 농림수산부는 선견지명을 발휘하여 호주가 선제적으로 대응하고 잘 조정되어야 할 필요성을 파악했으며, 이에 따라 8년 전에 '호주 동물 복지 전략'을 수립했습니다.
- target_sense_units:
  0. 하지만
  1. 연방 농림수산부는
  2. 선견지명을
  3. 발휘하여
  4. 호주가
  5. 선제적으로
  6. 대응하고
  7. 잘 조정되어야 할
  8. 필요성을
  9. 파악했으며,
  10. 이에 따라
  11. 8년 전에
  12. ' 호주 동물
  13. 복지 전략 ' 을
  14. 수립했습니다.

scratchpad:
* target[0]: "하지만"
  - source_tokens: `0: "But"`
  - mapping_reason: Contrastive conjunction.
* target[1]: "연방 농림수산부는"
  - source_tokens: `1: "the", 2: "Commonwealth", 3: "Department", 4: "of", 5: "Agriculture,", 6: "Fisheries", 7: "and", 8: "Forestry"`
  - mapping_reason: Subject entity name.
* target[2]: "선견지명을"
  - source_tokens: `11: "foresight"`
  - mapping_reason: Direct object of the foresight act.
* target[3]: "발휘하여"
  - source_tokens: `9: "had", 10: "the"`
  - mapping_reason: Verb phrase indicating possession/exercise of foresight.
* target[4]: "호주가"
  - source_tokens: `17: "Australia"`
  - mapping_reason: Subject of the subordinate clause.
* target[5]: "선제적으로"
  - source_tokens: `20: "ahead", 21: "of", 22: "the", 23: "game"`
  - mapping_reason: Idiomatic expression for being proactive.
* target[6]: "대응하고"
  - source_tokens: `18: "to", 19: "be"`
  - mapping_reason: Verbal component of the state of being ahead.
* target[7]: "잘 조정되어야 할"
  - source_tokens: `25: "well", 26: "coordinated,"`
  - mapping_reason: Adjectival modifier.
* target[8]: "필요성을"
  - source_tokens: `14: "the", 15: "need"`
  - mapping_reason: Object of the identification.
* target[9]: "파악했으며,"
  - source_tokens: `12: "to", 13: "identify"`
  - mapping_reason: Main verb of the first clause.
* target[10]: "이에 따라"
  - source_tokens: `27: "and", 28: "so"`
  - mapping_reason: Consequential discourse marker.
* target[11]: "8년 전에"
  - source_tokens: `35: "eight", 36: "years", 37: "ago."`
  - mapping_reason: Temporal modifier.
* target[12]: "' 호주 동물"
  - source_tokens: `31: "Australian", 32: "Animal"`
  - mapping_reason: Part of the strategy title.
* target[13]: "복지 전략 ' 을"
  - source_tokens: `33: "Welfare", 34: "Strategy"`
  - mapping_reason: Part of the strategy title.
* target[14]: "수립했습니다."
  - source_tokens: `29: "developed"`
  - mapping_reason: Main verb of the second clause.

result:
```html
0. <src>But the Commonwealth </src> <tgt>하지만</tgt>; start=0.00, end=1.00
1. <src>Department of Agriculture, </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>Fisheries and Forestry </src> <tgt>연방 농림수산부는</tgt>; start=3.00, end=4.00
4. <src>had the foresight to </src> <tgt>선견지명을 발휘하여</tgt>; start=4.00, end=5.00
5. <src>identify the need for </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>Australia to be </src> <tgt>호주가</tgt>; start=6.00, end=7.00
7. <src>ahead of the game </src> <tgt>선제적으로 대응하고</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>and well coordinated, </src> <tgt>잘 조정되어야 할 필요성을 파악했으며,</tgt>; start=9.00, end=10.00
10. <src>and so developed the </src> <tgt>이에 따라</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Australian Animal Welfare Strategy </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt>8년 전에 ' 호주 동물 복지 전략 ' 을 수립했습니다.</tgt>; start=13.00, end=13.66
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nN_EW5TiHKQ_W000023 ===

source:
- language: English
- transcription: Who can help you way more than I can. I really appreciate my trans followers when they tell me that they value my opinion on books, or when they tell me that they read a book because of me. Like I have gotten so many DMs from people saying, "Hey, I read Stay Gold because of you, and it was so good," and that honestly makes me so happy.
- source_tokens:
  0. Who
  1. can
  2. help
  3. you
  4. way
  5. more
  6. than
  7. I
  8. can.
  9. I
  10. really
  11. appreciate
  12. my
  13. trans
  14. followers
  15. when
  16. they
  17. tell
  18. me
  19. that
  20. they
  21. value
  22. my
  23. opinion
  24. on
  25. books,
  26. or
  27. when
  28. they
  29. tell
  30. me
  31. that
  32. they
  33. read
  34. a
  35. book
  36. because
  37. of
  38. me.
  39. Like
  40. I
  41. have
  42. gotten
  43. so
  44. many
  45. DMs
  46. from
  47. people
  48. saying,"
  49. Hey,
  50. I
  51. read
  52. Stay
  53. Gold
  54. because
  55. of
  56. you,
  57. and
  58. it
  59. was
  60. so
  61. good,"
  62. and
  63. that
  64. honestly
  65. makes
  66. me
  67. so
  68. happy.

target:
- language: Chinese
- translation: 他们比我更能帮到你。我真的很感激我的跨性别粉丝，他们告诉我他们很看重我对书的看法，或者说他们因为我读了一本书。我收到过很多私信，有人说：“嘿，我因为你读了《Stay Gold》，书真的很好看，”这真的让我特别开心。
- target_sense_units:
  0. 他们
  1. 比我
  2. 更能帮到你。
  3. 我
  4. 真的很感激
  5. 我的跨性别粉丝，
  6. 他们告诉我
  7. 他们很看重
  8. 我对书的看法，
  9. 或者说
  10. 他们
  11. 因为我
  12. 读了一本书。
  13. 我收到过
  14. 很多私信，
  15. 有人说：
  16. “嘿，
  17. 我
  18. 因为你
  19. 读了《StayGold》，
  20. 书
  21. 真的很好看，”
  22. 这真的
  23. 让我特别开心。

scratchpad:
* target[0]: "他们"
  - source_tokens: `0: "Who"`
  - mapping_reason: "Who" acts as the pronoun subject referring to the group (they).
* target[1]: "比我"
  - source_tokens: `6: "than", 7: "I"`
  - mapping_reason: Comparative structure.
* target[2]: "更能帮到你。"
  - source_tokens: `1: "can", 2: "help", 3: "you", 4: "way", 5: "more"`
  - mapping_reason: Modality and action of helping.
* target[3]: "我"
  - source_tokens: `9: "I"`
  - mapping_reason: Subject pronoun.
* target[4]: "真的很感激"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: Adverb and verb of appreciation.
* target[5]: "我的跨性别粉丝，"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: Object of appreciation.
* target[6]: "他们告诉我"
  - source_tokens: `15: "when", 16: "they", 17: "tell", 18: "me"`
  - mapping_reason: Reporting clause.
* target[7]: "他们很看重"
  - source_tokens: `19: "that", 20: "they", 21: "value"`
  - mapping_reason: Reported clause content.
* target[8]: "我对书的看法，"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books"`
  - mapping_reason: Direct object of value.
* target[9]: "或者说"
  - source_tokens: `26: "or"`
  - mapping_reason: Discourse connective.
* target[10]: "他们"
  - source_tokens: `28: "they"`
  - mapping_reason: Subject of the second reported clause.
* target[11]: "因为我"
  - source_tokens: `36: "because", 37: "of", 38: "me"`
  - mapping_reason: Reason clause.
* target[12]: "读了一本书。"
  - source_tokens: `33: "read", 34: "a", 35: "book"`
  - mapping_reason: Action performed.
* target[13]: "我收到过"
  - source_tokens: `40: "I", 41: "have", 42: "gotten"`
  - mapping_reason: Subject and verb of reception.
* target[14]: "很多私信，"
  - source_tokens: `43: "so", 44: "many", 45: "DMs"`
  - mapping_reason: Object of reception.
* target[15]: "有人说："
  - source_tokens: `46: "from", 47: "people", 48: "saying,"`
  - mapping_reason: Attribution of the quote.
* target[16]: "“嘿，"
  - source_tokens: `49: "Hey,"`
  - mapping_reason: Greeting.
* target[17]: "我"
  - source_tokens: `50: "I"`
  - mapping_reason: Subject of quote.
* target[18]: "因为你"
  - source_tokens: `54: "because", 55: "of", 56: "you"`
  - mapping_reason: Reason clause.
* target[19]: "读了《StayGold》，"
  - source_tokens: `51: "read", 52: "Stay", 53: "Gold"`
  - mapping_reason: Action of reading.
* target[20]: "书"
  - source_tokens: `58: "it"`
  - mapping_reason: Referring to the book mentioned in the quote.
* target[21]: "真的很好看，”"
  - source_tokens: `59: "was", 60: "so", 61: "good,"`
  - mapping_reason: Descriptive assessment.
* target[22]: "这真的"
  - source_tokens: `62: "and", 63: "that", 64: "honestly"`
  - mapping_reason: Discourse connective and adverbial emphasis.
* target[23]: "让我特别开心。"
  - source_tokens: `65: "makes", 66: "me", 67: "so", 68: "happy."`
  - mapping_reason: Resulting emotional state.

result:
```html
0. <src>Who can help </src> <tgt>他们</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>you way more than I can. </src> <tgt>比我更能帮到你。</tgt>; start=2.00, end=3.00
3. <src>I really appreciate </src> <tgt>我真的很感激</tgt>; start=3.00, end=4.00
4. <src>my trans followers </src> <tgt>我的跨性别粉丝，</tgt>; start=4.00, end=5.00
5. <src>when they tell me that </src> <tgt>他们告诉我</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>they value my opinion on books, </src> <tgt>他们很看重我对书的看法，</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>or when they tell me </src> <tgt>或者说他们</tgt>; start=9.00, end=10.00
10. <src>that they read a book </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>because of me. </src> <tgt>因为我读了一本书。</tgt>; start=11.00, end=12.00
12. <src>Like I have </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>gotten so many DMs </src> <tgt>我收到过很多私信，</tgt>; start=13.00, end=14.00
14. <src>from people saying," </src> <tgt>有人说：</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>Hey, I read Stay Gold because of you, and it </src> <tgt>“嘿，我因为你读了《StayGold》，书</tgt>; start=16.00, end=17.00
17. <src>was so good," </src> <tgt>真的很好看，”</tgt>; start=17.00, end=18.00
18. <src>and that honestly makes </src> <tgt>这真的</tgt>; start=18.00, end=19.00
19. <src>me so happy. </src> <tgt>让我特别开心。</tgt>; start=19.00, end=19.81
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[12]
  - verdict: mapping_error
  - reason: "The target unit only reflects 'read a book', while the mapping incorrectly includes the preceding verb phrase 'tell me that they'."
  - replace_source_tokens: 33: "read", 34: "a", 35: "book"
  validation:
    scratchpad:
* target[0]: "他们"
  - source_tokens: `0: "Who"`
  - mapping_reason: "Who" acts as the subject referring to the people who can help, translated as "they" (他们).
* target[1]: "比我"
  - source_tokens: `6: "than", 7: "I"`
  - mapping_reason: Comparative structure "than I".
* target[2]: "更能帮到你。"
  - source_tokens: `1: "can", 2: "help", 3: "you", 4: "way", 5: "more"`
  - mapping_reason: "can help you way more".
* target[3]: "我"
  - source_tokens: `9: "I"`
  - mapping_reason: Subject "I".
* target[4]: "真的很感激"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: "really appreciate".
* target[5]: "我的跨性别粉丝，"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: "my trans followers".
* target[6]: "他们告诉我"
  - source_tokens: `15: "when", 16: "they", 17: "tell", 18: "me"`
  - mapping_reason: "when they tell me".
* target[7]: "他们很看重"
  - source_tokens: `19: "that", 20: "they", 21: "value"`
  - mapping_reason: "that they value".
* target[8]: "我对书的看法，"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: "my opinion on books".
* target[9]: "或者说"
  - source_tokens: `26: "or"`
  - mapping_reason: "or".
* target[10]: "他们"
  - source_tokens: `28: "they"`
  - mapping_reason: "they" (implied subject).
* target[11]: "因为我"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: "because of me".
* target[12]: "读了一本书。"
  - source_tokens: `29: "tell", 30: "me", 31: "that", 32: "they", 33: "read", 34: "a", 35: "book"`
  - mapping_reason: "tell me that they read a book".
* target[13]: "我收到过"
  - source_tokens: `40: "I", 41: "have", 42: "gotten"`
  - mapping_reason: "I have gotten".
* target[14]: "很多私信，"
  - source_tokens: `43: "so", 44: "many", 45: "DMs"`
  - mapping_reason: "so many DMs".
* target[15]: "有人说："
  - source_tokens: `46: "from", 47: "people", 48: "saying,"`
  - mapping_reason: "from people saying".
* target[16]: "“嘿，"
  - source_tokens: `49: "Hey,"`
  - mapping_reason: "Hey".
* target[17]: "我"
  - source_tokens: `50: "I"`
  - mapping_reason: "I".
* target[18]: "因为你"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: "because of you".
* target[19]: "读了《StayGold》，"
  - source_tokens: `51: "read", 52: "Stay", 53: "Gold"`
  - mapping_reason: "read Stay Gold".
* target[20]: "书"
  - source_tokens: `58: "it"`
  - mapping_reason: "it" (referring to the book).
* target[21]: "真的很好看，”"
  - source_tokens: `57: "and", 59: "was", 60: "so", 61: "good,"`
  - mapping_reason: "and it was so good".
* target[22]: "这真的"
  - source_tokens: `62: "and", 63: "that", 64: "honestly"`
  - mapping_reason: "and that honestly".
* target[23]: "让我特别开心。"
  - source_tokens: `65: "makes", 66: "me", 67: "so", 68: "happy."`
  - mapping_reason: "makes me so happy".
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [0]},
  {"target_senseunit_id": 1, "source_token_ids": [6, 7]},
  {"target_senseunit_id": 2, "source_token_ids": [1, 2, 3, 4, 5]},
  {"target_senseunit_id": 3, "source_token_ids": [9]},
  {"target_senseunit_id": 4, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 6, "source_token_ids": [15, 16, 17, 18]},
  {"target_senseunit_id": 7, "source_token_ids": [19, 20, 21]},
  {"target_senseunit_id": 8, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 9, "source_token_ids": [26]},
  {"target_senseunit_id": 10, "source_token_ids": [28]},
  {"target_senseunit_id": 11, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 12, "source_token_ids": [29, 30, 31, 32, 33, 34, 35]},
  {"target_senseunit_id": 13, "source_token_ids": [40, 41, 42]},
  {"target_senseunit_id": 14, "source_token_ids": [43, 44, 45]},
  {"target_senseunit_id": 15, "source_token_ids": [46, 47, 48]},
  {"target_senseunit_id": 16, "source_token_ids": [49]},
  {"target_senseunit_id": 17, "source_token_ids": [50]},
  {"target_senseunit_id": 18, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 19, "source_token_ids": [51, 52, 53]},
  {"target_senseunit_id": 20, "source_token_ids": [58]},
  {"target_senseunit_id": 21, "source_token_ids": [57, 59, 60, 61]},
  {"target_senseunit_id": 22, "source_token_ids": [62, 63, 64]},
  {"target_senseunit_id": 23, "source_token_ids": [65, 66, 67, 68]}
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== EN_nvdVVhi8VpA_W000110 ===

source:
- language: English
- transcription: Um, 42% of the way through the course, so as you can see, each pie slice represents a different topic, and they have a little bit more to learn in in matter, and a little bit more in atoms and ions and molecules. But you know, so this is telling you that.
- source_tokens:
  0. Um,
  1. 42%
  2. of
  3. the
  4. way
  5. through
  6. the
  7. course,
  8. so
  9. as
  10. you
  11. can
  12. see,
  13. each
  14. pie
  15. slice
  16. represents
  17. a
  18. different
  19. topic,
  20. and
  21. they
  22. have
  23. a
  24. little
  25. bit
  26. more
  27. to
  28. learn
  29. in
  30. in
  31. matter,
  32. and
  33. a
  34. little
  35. bit
  36. more
  37. in
  38. atoms
  39. and
  40. ions
  41. and
  42. molecules.
  43. But
  44. you
  45. know,
  46. so
  47. this
  48. is
  49. telling
  50. you
  51. that.

target:
- language: Korean
- translation: 음, 코스의 42% 정도 진행했는데요, 보시다시피 각 파이 조각은 서로 다른 주제를 나타내고, 물질에 대해 조금 더 배워야 하고, 원자, 이온, 분자에 대해서도 조금 더 배워야 해요. 그런데, 음, 이건 그걸 알려주는 거예요.
- target_sense_units:
  0. 음,
  1. 코스의 42% 정도
  2. 진행했는데요,
  3. 보시다시피
  4. 각 파이 조각은
  5. 서로 다른 주제를
  6. 나타내고,
  7. 물질에 대해
  8. 조금 더 배워야 하고,
  9. 원자, 이온, 분자에 대해서도
  10. 조금 더 배워야 해요.
  11. 그런데,
  12. 음,
  13. 이건
  14. 그걸
  15. 알려주는 거예요.

scratchpad:
* target[0]: "음,"
  - source_tokens: `0: "Um,"`
  - mapping_reason: Direct discourse marker translation.
* target[1]: "코스의 42% 정도"
  - source_tokens: `1: "42%", 2: "of", 3: "the", 4: "way", 5: "through", 7: "course,"`
  - mapping_reason: Quantifier and scope of progress.
* target[2]: "진행했는데요,"
  - source_tokens: `8: "so"`
  - mapping_reason: Discourse connective indicating progress/state.
* target[3]: "보시다시피"
  - source_tokens: `9: "as", 10: "you", 11: "can", 12: "see,"`
  - mapping_reason: Evidential/discourse marker.
* target[4]: "각 파이 조각은"
  - source_tokens: `13: "each", 14: "pie", 15: "slice"`
  - mapping_reason: Subject of the clause.
* target[5]: "서로 다른 주제를"
  - source_tokens: `18: "different", 19: "topic,"`
  - mapping_reason: Object of representation.
* target[6]: "나타내고,"
  - source_tokens: `16: "represents", 20: "and"`
  - mapping_reason: Verb and connective.
* target[7]: "물질에 대해"
  - source_tokens: `29: "in", 31: "matter,"`
  - mapping_reason: Topic of learning.
* target[8]: "조금 더 배워야 하고,"
  - source_tokens: `23: "a", 24: "little", 25: "bit", 26: "more", 27: "to", 28: "learn", 32: "and"`
  - mapping_reason: Learning requirement.
* target[9]: "원자, 이온, 분자에 대해서도"
  - source_tokens: `38: "atoms", 39: "and", 40: "ions", 41: "and", 42: "molecules."`
  - mapping_reason: Additional learning topics.
* target[10]: "조금 더 배워야 해요."
  - source_tokens: `33: "a", 34: "little", 35: "bit", 36: "more", 27: "to", 28: "learn"`
  - mapping_reason: Repetition of learning requirement.
* target[11]: "그런데,"
  - source_tokens: `43: "But"`
  - mapping_reason: Contrastive discourse marker.
* target[12]: "음,"
  - source_tokens: `44: "you", 45: "know,"`
  - mapping_reason: Fillers/discourse markers.
* target[13]: "이건"
  - source_tokens: `47: "this"`
  - mapping_reason: Subject reference.
* target[14]: "그걸"
  - source_tokens: `51: "that."`
  - mapping_reason: Object reference.
* target[15]: "알려주는 거예요."
  - source_tokens: `48: "is", 49: "telling", 50: "you"`
  - mapping_reason: Main verb phrase.

result:
```html
0. <src>Um, </src> <tgt>음,</tgt>; start=0.00, end=1.00
1. <src>42% of the way through </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>the course, </src> <tgt>코스의 42% 정도</tgt>; start=2.00, end=3.00
3. <src>so as you can see, </src> <tgt>진행했는데요, 보시다시피</tgt>; start=3.00, end=4.00
4. <src>each pie slice </src> <tgt>각 파이 조각은</tgt>; start=4.00, end=5.00
5. <src>represents </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>a different topic, and </src> <tgt>서로 다른 주제를 나타내고,</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>they have </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>a little bit more to learn </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>in in matter, and </src> <tgt>물질에 대해 조금 더 배워야 하고,</tgt>; start=10.00, end=11.00
11. <src>a little bit more </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>in atoms and ions </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>and molecules. </src> <tgt>원자, 이온, 분자에 대해서도 조금 더 배워야 해요.</tgt>; start=13.00, end=14.00
14. <src>But you </src> <tgt>그런데,</tgt>; start=14.00, end=15.00
15. <src>know, so this is </src> <tgt>음, 이건</tgt>; start=15.00, end=16.00
16. <src>telling you that. </src> <tgt>그걸 알려주는 거예요.</tgt>; start=16.00, end=16.94
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nsPdq5m1h0y_W000029 ===

source:
- language: English
- transcription: We get the mass by taking the number of protons, which is always 35 for bromine, and we add it to the number of neutrons, which is new for this isotope. So 35 plus 47 is a mass of 82.
- source_tokens:
  0. We
  1. get
  2. the
  3. mass
  4. by
  5. taking
  6. the
  7. number
  8. of
  9. protons,
  10. which
  11. is
  12. always
  13. 35
  14. for
  15. bromine,
  16. and
  17. we
  18. add
  19. it
  20. to
  21. the
  22. number
  23. of
  24. neutrons,
  25. which
  26. is
  27. new
  28. for
  29. this
  30. isotope.
  31. So
  32. 35
  33. plus
  34. 47
  35. is
  36. a
  37. mass
  38. of
  39. 82.

target:
- language: Chinese
- translation: 我们通过质子数加上中子数来得到质量，对于溴来说，质子数总是35，而中子数对于这种同位素是新的。所以35加47等于质量82。
- target_sense_units:
  0. 我们通过质子数
  1. 加上中子数
  2. 来得到质量，
  3. 对于溴来说，
  4. 质子数总是35，
  5. 而
  6. 中子数
  7. 对于这种同位素
  8. 是新的。
  9. 所以
  10. 35加47
  11. 等于
  12. 质量82。

scratchpad:
* target[0]: "我们通过质子数"
  - source_tokens: `0: "We", 4: "by", 7: "number", 9: "protons,"`
  - mapping_reason: Represents the subject and the first component of the calculation method.

* target[1]: "加上中子数"
  - source_tokens: `18: "add", 22: "number", 24: "neutrons,"`
  - mapping_reason: Represents the second component of the calculation method.

* target[2]: "来得到质量，"
  - source_tokens: `1: "get", 2: "the", 3: "mass"`
  - mapping_reason: Represents the result of the calculation.

* target[3]: "对于溴来说，"
  - source_tokens: `14: "for", 15: "bromine,"`
  - mapping_reason: Represents the specification of the element.

* target[4]: "质子数总是35，"
  - source_tokens: `7: "number", 9: "protons,", 11: "is", 12: "always", 13: "35"`
  - mapping_reason: Represents the proton count constant.

* target[5]: "而"
  - source_tokens: `16: "and"`
  - mapping_reason: Represents the contrastive conjunction.

* target[6]: "中子数"
  - source_tokens: `22: "number", 24: "neutrons,"`
  - mapping_reason: Represents the neutron count subject.

* target[7]: "对于这种同位素"
  - source_tokens: `28: "for", 29: "this", 30: "isotope."`
  - mapping_reason: Represents the specific isotope context.

* target[8]: "是新的。"
  - source_tokens: `26: "is", 27: "new"`
  - mapping_reason: Represents the status of the neutron count.

* target[9]: "所以"
  - source_tokens: `31: "So"`
  - mapping_reason: Represents the logical conclusion marker.

* target[10]: "35加47"
  - source_tokens: `32: "35", 33: "plus", 34: "47"`
  - mapping_reason: Represents the numerical calculation.

* target[11]: "等于"
  - source_tokens: `35: "is"`
  - mapping_reason: Represents the equality relation.

* target[12]: "质量82。"
  - source_tokens: `37: "mass", 38: "of", 39: "82."`
  - mapping_reason: Represents the final result.

result:
```html
0. <src>We get the mass </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>by taking the number of </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>protons, </src> <tgt>我们通过质子数</tgt>; start=2.00, end=3.00
3. <src>which is always 35 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>for bromine, </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>and we add </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>it to the number of </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>neutrons, </src> <tgt>加上中子数来得到质量，对于溴来说，质子数总是35，而中子数</tgt>; start=7.00, end=8.00
8. <src>which is new </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>for this isotope. So </src> <tgt>对于这种同位素是新的。所以</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>35 plus 47 </src> <tgt>35加47</tgt>; start=11.00, end=12.00
12. <src>is a mass of </src> <tgt>等于</tgt>; start=12.00, end=13.00
13. <src>82. </src> <tgt>质量82。</tgt>; start=13.00, end=13.53
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nN_EW5TiHKQ_W000023 ===

source:
- language: English
- transcription: Who can help you way more than I can. I really appreciate my trans followers when they tell me that they value my opinion on books, or when they tell me that they read a book because of me. Like I have gotten so many DMs from people saying, "Hey, I read Stay Gold because of you, and it was so good," and that honestly makes me so happy.
- source_tokens:
  0. Who
  1. can
  2. help
  3. you
  4. way
  5. more
  6. than
  7. I
  8. can.
  9. I
  10. really
  11. appreciate
  12. my
  13. trans
  14. followers
  15. when
  16. they
  17. tell
  18. me
  19. that
  20. they
  21. value
  22. my
  23. opinion
  24. on
  25. books,
  26. or
  27. when
  28. they
  29. tell
  30. me
  31. that
  32. they
  33. read
  34. a
  35. book
  36. because
  37. of
  38. me.
  39. Like
  40. I
  41. have
  42. gotten
  43. so
  44. many
  45. DMs
  46. from
  47. people
  48. saying,"
  49. Hey,
  50. I
  51. read
  52. Stay
  53. Gold
  54. because
  55. of
  56. you,
  57. and
  58. it
  59. was
  60. so
  61. good,"
  62. and
  63. that
  64. honestly
  65. makes
  66. me
  67. so
  68. happy.

target:
- language: Japanese
- translation: 彼らの方が私よりずっと力になれるんです。本当に感謝してるんです、トランスジェンダーのフォロワーさんたちに。彼らが私の本の感想を大事にしてくれてるって言ってくれたり、私のおかげで本を読んだって言ってくれたりするんです。それに、たくさんDMをもらってるんです。「ねえ、あなたのおかげで『Stay Gold』を読んだんだけど、すごく良かったよ」って。それが本当に嬉しいんです。
- target_sense_units:
  0. 彼らの方が
  1. 私より
  2. ずっと
  3. 力になれるんです。
  4. 本当に
  5. 感謝してるんです、
  6. トランスジェンダーのフォロワーさんたちに。
  7. 彼らが
  8. 私の本の感想を
  9. 大事にしてくれてる
  10. って言ってくれたり、
  11. 私のおかげで
  12. 本を読んだ
  13. って言ってくれたり
  14. するんです。
  15. それに、
  16. たくさん
  17. DMを
  18. もらってるんです。
  19. 「ねえ、
  20. あなたのおかげで
  21. 『StayGold』を
  22. 読んだんだけど、
  23. すごく
  24. 良かったよ」
  25. って。
  26. それが
  27. 本当に
  28. 嬉しいんです。

scratchpad:
* target[0]: "彼らの方が"
  - source_tokens: `0: "Who"`
  - mapping_reason: Refers to the subject "Who" (the people being compared).
* target[1]: "私より"
  - source_tokens: `7: "I"`
  - mapping_reason: The subject of comparison "I".
* target[2]: "ずっと"
  - source_tokens: `4: "way"`
  - mapping_reason: Intensifier for the comparison.
* target[3]: "力になれるんです。"
  - source_tokens: `1: "can", 2: "help", 3: "you", 5: "more", 6: "than", 8: "can."`
  - mapping_reason: The predicate "can help you more than I can".
* target[4]: "本当に"
  - source_tokens: `10: "really"`
  - mapping_reason: Intensifier for appreciation.
* target[5]: "感謝してるんです、"
  - source_tokens: `11: "appreciate"`
  - mapping_reason: Core verb of appreciation.
* target[6]: "トランスジェンダーのフォロワーさんたちに。"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: The object of appreciation.
* target[7]: "彼らが"
  - source_tokens: `16: "they"`
  - mapping_reason: Subject of the first clause.
* target[8]: "私の本の感想を"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: The content of the opinion.
* target[9]: "大事にしてくれてる"
  - source_tokens: `21: "value"`
  - mapping_reason: The verb indicating valuing the opinion.
* target[10]: "って言ってくれたり、"
  - source_tokens: `15: "when", 17: "tell", 18: "me", 19: "that"`
  - mapping_reason: Reporting verb structure.
* target[11]: "私のおかげで"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: Causal phrase.
* target[12]: "本を読んだ"
  - source_tokens: `33: "read", 34: "a", 35: "book"`
  - mapping_reason: Action performed.
* target[13]: "って言ってくれたり"
  - source_tokens: `27: "when", 29: "tell", 30: "me", 31: "that"`
  - mapping_reason: Reporting verb structure.
* target[14]: "するんです。"
  - source_tokens: `20: "they", 32: "they"`
  - mapping_reason: Plural subject markers for the repeated actions.
* target[15]: "それに、"
  - source_tokens: `39: "Like"`
  - mapping_reason: Discourse connective.
* target[16]: "たくさん"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: Quantity modifier.
* target[17]: "DMを"
  - source_tokens: `45: "DMs"`
  - mapping_reason: Object of receiving.
* target[18]: "もらってるんです。"
  - source_tokens: `40: "I", 41: "have", 42: "gotten", 46: "from", 47: "people", 48: "saying,"`
  - mapping_reason: Verb of receiving and context.
* target[19]: "「ねえ、"
  - source_tokens: `49: "Hey,"`
  - mapping_reason: Direct quote opener.
* target[20]: "あなたのおかげで"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: Causal phrase.
* target[21]: "『StayGold』を"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: Book title.
* target[22]: "読んだんだけど、"
  - source_tokens: `50: "I", 51: "read", 57: "and"`
  - mapping_reason: Action performed and conjunction.
* target[23]: "すごく"
  - source_tokens: `60: "so"`
  - mapping_reason: Intensifier.
* target[24]: "良かったよ」"
  - source_tokens: `58: "it", 59: "was", 61: "good,"`
  - mapping_reason: Evaluation of the book.
* target[25]: "って。"
  - source_tokens: `48: "saying,"`
  - mapping_reason: Closing the quote.
* target[26]: "それが"
  - source_tokens: `63: "that"`
  - mapping_reason: Subject reference.
* target[27]: "本当に"
  - source_tokens: `64: "honestly"`
  - mapping_reason: Adverb of truth/intensity.
* target[28]: "嬉しいんです。"
  - source_tokens: `65: "makes", 66: "me", 67: "so", 68: "happy."`
  - mapping_reason: Emotional result.

result:
```html
0. <src>Who can help </src> <tgt>彼らの方が</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>you way more than I can. </src> <tgt>私よりずっと力になれるんです。</tgt>; start=2.00, end=3.00
3. <src>I really appreciate </src> <tgt>本当に感謝してるんです、</tgt>; start=3.00, end=4.00
4. <src>my trans followers </src> <tgt>トランスジェンダーのフォロワーさんたちに。</tgt>; start=4.00, end=5.00
5. <src>when they tell me that </src> <tgt>彼らが</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>they value my opinion on books, </src> <tgt>私の本の感想を大事にしてくれてるって言ってくれたり、</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>or when they tell me </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>that they read a book </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>because of me. </src> <tgt>私のおかげで本を読んだって言ってくれたりするんです。</tgt>; start=11.00, end=12.00
12. <src>Like I have </src> <tgt>それに、</tgt>; start=12.00, end=13.00
13. <src>gotten so many DMs </src> <tgt>たくさんDMを</tgt>; start=13.00, end=14.00
14. <src>from people saying," </src> <tgt>もらってるんです。</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>Hey, I read Stay Gold because of you, and it </src> <tgt>「ねえ、あなたのおかげで『StayGold』を読んだんだけど、</tgt>; start=16.00, end=17.00
17. <src>was so good," </src> <tgt>すごく良かったよ」って。</tgt>; start=17.00, end=18.00
18. <src>and that honestly makes </src> <tgt>それが本当に</tgt>; start=18.00, end=19.00
19. <src>me so happy. </src> <tgt>嬉しいんです。</tgt>; start=19.00, end=19.81
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nvdVVhi8VpA_W000110 ===

source:
- language: English
- transcription: Um, 42% of the way through the course, so as you can see, each pie slice represents a different topic, and they have a little bit more to learn in in matter, and a little bit more in atoms and ions and molecules. But you know, so this is telling you that.
- source_tokens:
  0. Um,
  1. 42%
  2. of
  3. the
  4. way
  5. through
  6. the
  7. course,
  8. so
  9. as
  10. you
  11. can
  12. see,
  13. each
  14. pie
  15. slice
  16. represents
  17. a
  18. different
  19. topic,
  20. and
  21. they
  22. have
  23. a
  24. little
  25. bit
  26. more
  27. to
  28. learn
  29. in
  30. in
  31. matter,
  32. and
  33. a
  34. little
  35. bit
  36. more
  37. in
  38. atoms
  39. and
  40. ions
  41. and
  42. molecules.
  43. But
  44. you
  45. know,
  46. so
  47. this
  48. is
  49. telling
  50. you
  51. that.

target:
- language: Japanese
- translation: ええと、コースの42%まで進んだところです。ご覧の通り、パイの各スライスは異なるトピックを表しています。物質についてはもう少し学ぶ必要があります。それから、原子やイオン、分子についてももう少し学ぶ必要があります。でも、そうですね、これはそのことを示しているんです。
- target_sense_units:
  0. ええと、
  1. コースの42%まで
  2. 進んだところです。
  3. ご覧の通り、
  4. パイの
  5. 各スライスは
  6. 異なるトピックを
  7. 表しています。
  8. 物質については
  9. もう少し
  10. 学ぶ必要が
  11. あります。
  12. それから、
  13. 原子やイオン、
  14. 分子についても
  15. もう少し
  16. 学ぶ必要が
  17. あります。
  18. でも、
  19. そうですね、
  20. これは
  21. そのことを
  22. 示しているんです。

scratchpad:
* target[0]: "ええと、"
  - source_tokens: `0: "Um,"`
  - mapping_reason: Discourse marker.
* target[1]: "コースの42%まで"
  - source_tokens: `1: "42%", 2: "of", 3: "the", 4: "way", 5: "through", 6: "the", 7: "course,"`
  - mapping_reason: Progress measurement.
* target[2]: "進んだところです。"
  - source_tokens: `4: "way", 5: "through"`
  - mapping_reason: Completion state.
* target[3]: "ご覧の通り、"
  - source_tokens: `9: "as", 10: "you", 11: "can", 12: "see,"`
  - mapping_reason: Directing attention.
* target[4]: "パイの"
  - source_tokens: `14: "pie"`
  - mapping_reason: Subject of the visual aid.
* target[5]: "各スライスは"
  - source_tokens: `13: "each", 15: "slice"`
  - mapping_reason: Individual components.
* target[6]: "異なるトピックを"
  - source_tokens: `18: "different", 19: "topic,"`
  - mapping_reason: Content of slices.
* target[7]: "表しています。"
  - source_tokens: `16: "represents"`
  - mapping_reason: Relation between slice and topic.
* target[8]: "物質については"
  - source_tokens: `31: "matter,"`
  - mapping_reason: Topic of study.
* target[9]: "もう少し"
  - source_tokens: `23: "a", 24: "little", 25: "bit", 26: "more"`
  - mapping_reason: Extent of learning.
* target[10]: "学ぶ必要が"
  - source_tokens: `27: "to", 28: "learn"`
  - mapping_reason: Action required.
* target[11]: "あります。"
  - source_tokens: `22: "have"`
  - mapping_reason: Modal necessity.
* target[12]: "それから、"
  - source_tokens: `32: "and"`
  - mapping_reason: Connective.
* target[13]: "原子やイオン、"
  - source_tokens: `38: "atoms", 39: "and", 40: "ions"`
  - mapping_reason: Topics.
* target[14]: "分子についても"
  - source_tokens: `41: "and", 42: "molecules."`
  - mapping_reason: Topic.
* target[15]: "もう少し"
  - source_tokens: `33: "a", 34: "little", 35: "bit", 36: "more"`
  - mapping_reason: Extent of learning.
* target[16]: "学ぶ必要が"
  - source_tokens: `27: "to", 28: "learn"`
  - mapping_reason: Action required (implied from previous clause).
* target[17]: "あります。"
  - source_tokens: `22: "have"`
  - mapping_reason: Modal necessity (implied from previous clause).
* target[18]: "でも、"
  - source_tokens: `43: "But"`
  - mapping_reason: Contrastive conjunction.
* target[19]: "そうですね、"
  - source_tokens: `44: "you", 45: "know,"`
  - mapping_reason: Discourse filler/hedging.
* target[20]: "これは"
  - source_tokens: `47: "this"`
  - mapping_reason: Subject reference.
* target[21]: "そのことを"
  - source_tokens: `51: "that."`
  - mapping_reason: Reference to previous statement.
* target[22]: "示しているんです。"
  - source_tokens: `48: "is", 49: "telling", 50: "you"`
  - mapping_reason: Communicative action.

result:
```html
0. <src>Um, </src> <tgt>ええと、</tgt>; start=0.00, end=1.00
1. <src>42% of the way through </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>the course, </src> <tgt>コースの42%まで進んだところです。</tgt>; start=2.00, end=3.00
3. <src>so as you can see, </src> <tgt>ご覧の通り、</tgt>; start=3.00, end=4.00
4. <src>each pie slice </src> <tgt>パイの各スライスは</tgt>; start=4.00, end=5.00
5. <src>represents </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>a different topic, and </src> <tgt>異なるトピックを表しています。</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>they have </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>a little bit more to learn </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>in in matter, and </src> <tgt>物質についてはもう少し学ぶ必要があります。それから、</tgt>; start=10.00, end=11.00
11. <src>a little bit more </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>in atoms and ions </src> <tgt>原子やイオン、</tgt>; start=12.00, end=13.00
13. <src>and molecules. </src> <tgt>分子についてももう少し学ぶ必要があります。</tgt>; start=13.00, end=14.00
14. <src>But you </src> <tgt>でも、</tgt>; start=14.00, end=15.00
15. <src>know, so this is </src> <tgt>そうですね、これは</tgt>; start=15.00, end=16.00
16. <src>telling you that. </src> <tgt>そのことを示しているんです。</tgt>; start=16.00, end=16.94
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_nsPdq5m1h0y_W000029 ===

source:
- language: English
- transcription: We get the mass by taking the number of protons, which is always 35 for bromine, and we add it to the number of neutrons, which is new for this isotope. So 35 plus 47 is a mass of 82.
- source_tokens:
  0. We
  1. get
  2. the
  3. mass
  4. by
  5. taking
  6. the
  7. number
  8. of
  9. protons,
  10. which
  11. is
  12. always
  13. 35
  14. for
  15. bromine,
  16. and
  17. we
  18. add
  19. it
  20. to
  21. the
  22. number
  23. of
  24. neutrons,
  25. which
  26. is
  27. new
  28. for
  29. this
  30. isotope.
  31. So
  32. 35
  33. plus
  34. 47
  35. is
  36. a
  37. mass
  38. of
  39. 82.

target:
- language: Japanese
- translation: 質量を求めるには、陽子の数に中性子の数を加えます。臭素の陽子の数は常に35で、この同位体の中性子の数は47です。ですから35足す47で質量は82です。
- target_sense_units:
  0. 質量を求めるには、
  1. 陽子の数に
  2. 中性子の数を
  3. 加えます。
  4. 臭素の
  5. 陽子の数は
  6. 常に
  7. 35で、
  8. この同位体の
  9. 中性子の数は
  10. 47です。
  11. ですから
  12. 35足す47で
  13. 質量は
  14. 82です。

scratchpad:
* target[0]: "質量を求めるには、"
  - source_tokens: `1: "get", 2: "the", 3: "mass", 4: "by", 5: "taking"`
  - mapping_reason: Expresses the method to obtain the mass.
* target[1]: "陽子の数に"
  - source_tokens: `7: "number", 8: "of", 9: "protons,"`
  - mapping_reason: Identifies the first operand (protons).
* target[2]: "中性子の数を"
  - source_tokens: `22: "number", 23: "of", 24: "neutrons,"`
  - mapping_reason: Identifies the second operand (neutrons).
* target[3]: "加えます。"
  - source_tokens: `18: "add"`
  - mapping_reason: The operation to perform (addition).
* target[4]: "臭素の"
  - source_tokens: `15: "bromine,"`
  - mapping_reason: Specifies the element bromine.
* target[5]: "陽子の数は"
  - source_tokens: `7: "number", 8: "of", 9: "protons,"`
  - mapping_reason: Refers to the number of protons.
* target[6]: "常に"
  - source_tokens: `12: "always"`
  - mapping_reason: Frequency/constant condition.
* target[7]: "35で、"
  - source_tokens: `13: "35"`
  - mapping_reason: The value for protons.
* target[8]: "この同位体の"
  - source_tokens: `29: "this", 30: "isotope."`
  - mapping_reason: Specifies the isotope in question.
* target[9]: "中性子の数は"
  - source_tokens: `22: "number", 23: "of", 24: "neutrons,"`
  - mapping_reason: Refers to the number of neutrons.
* target[10]: "47です。"
  - source_tokens: `34: "47"`
  - mapping_reason: The value for neutrons for this isotope.
* target[11]: "ですから"
  - source_tokens: `31: "So"`
  - mapping_reason: Logical inference/connective.
* target[12]: "35足す47で"
  - source_tokens: `32: "35", 33: "plus", 34: "47"`
  - mapping_reason: The calculation step.
* target[13]: "質量は"
  - source_tokens: `3: "mass"`
  - mapping_reason: The subject of the result.
* target[14]: "82です。"
  - source_tokens: `39: "82."`
  - mapping_reason: The result of the calculation.

result:
```html
0. <src>We get the mass </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>by taking the number of </src> <tgt>質量を求めるには、</tgt>; start=1.00, end=2.00
2. <src>protons, </src> <tgt>陽子の数に</tgt>; start=2.00, end=3.00
3. <src>which is always 35 </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>for bromine, </src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>and we add </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>it to the number of </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>neutrons, </src> <tgt>中性子の数を加えます。臭素の陽子の数は常に35で、</tgt>; start=7.00, end=8.00
8. <src>which is new </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>for this isotope. So </src> <tgt>この同位体の中性子の数は</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>35 plus 47 </src> <tgt>47です。ですから35足す47で質量は</tgt>; start=11.00, end=12.00
12. <src>is a mass of </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>82. </src> <tgt>82です。</tgt>; start=13.00, end=13.53
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== EN_n_UNfbRo_MQ_W000005 ===

source:
- language: English
- transcription: But the Commonwealth Department of Agriculture, Fisheries and Forestry had the foresight to identify the need for Australia to be ahead of the game and well coordinated, and so developed the Australian Animal Welfare Strategy eight years ago.
- source_tokens:
  0. But
  1. the
  2. Commonwealth
  3. Department
  4. of
  5. Agriculture,
  6. Fisheries
  7. and
  8. Forestry
  9. had
  10. the
  11. foresight
  12. to
  13. identify
  14. the
  15. need
  16. for
  17. Australia
  18. to
  19. be
  20. ahead
  21. of
  22. the
  23. game
  24. and
  25. well
  26. coordinated,
  27. and
  28. so
  29. developed
  30. the
  31. Australian
  32. Animal
  33. Welfare
  34. Strategy
  35. eight
  36. years
  37. ago.

target:
- language: Japanese
- translation: しかし、連邦農林水産省は先見の明を持ち、オーストラリアが先手を打ち適切に連携する必要性を認識し、8年前に「オーストラリア動物福祉戦略」を策定しました。
- target_sense_units:
  0. しかし、
  1. 連邦農林水産省は
  2. 先見の明を持ち、
  3. オーストラリアが
  4. 先手を打ち
  5. 適切に
  6. 連携する必要性を
  7. 認識し、
  8. 8年前に
  9. 「オーストラリア動物福祉戦略」を
  10. 策定し
  11. ました。

scratchpad:
* target[0]: "しかし、"
  - source_tokens: `0: "But"`
  - mapping_reason: Contrastive conjunction.
* target[1]: "連邦農林水産省は"
  - source_tokens: `1: "the", 2: "Commonwealth", 3: "Department", 4: "of", 5: "Agriculture,", 6: "Fisheries", 7: "and", 8: "Forestry"`
  - mapping_reason: Subject entity.
* target[2]: "先見の明を持ち、"
  - source_tokens: `9: "had", 10: "the", 11: "foresight"`
  - mapping_reason: Verb phrase expressing foresight.
* target[3]: "オーストラリアが"
  - source_tokens: `17: "Australia"`
  - mapping_reason: Subject of the embedded clause.
* target[4]: "先手を打ち"
  - source_tokens: `20: "ahead", 21: "of", 22: "the", 23: "game"`
  - mapping_reason: Idiomatic expression for being ahead.
* target[5]: "適切に"
  - source_tokens: `25: "well"`
  - mapping_reason: Adverbial modifier.
* target[6]: "連携する必要性を"
  - source_tokens: `12: "to", 13: "identify", 14: "the", 15: "need", 26: "coordinated,"`
  - mapping_reason: Object of recognition (need for coordination).
* target[7]: "認識し、"
  - source_tokens: `13: "identify"`
  - mapping_reason: Main verb of the embedded clause.
* target[8]: "8年前に"
  - source_tokens: `35: "eight", 36: "years", 37: "ago."`
  - mapping_reason: Temporal adjunct.
* target[9]: "「オーストラリア動物福祉戦略」を"
  - source_tokens: `30: "the", 31: "Australian", 32: "Animal", 33: "Welfare", 34: "Strategy"`
  - mapping_reason: Direct object entity.
* target[10]: "策定し"
  - source_tokens: `29: "developed"`
  - mapping_reason: Main verb.
* target[11]: "ました。"
  - source_tokens: `29: "developed"`
  - mapping_reason: Past tense marker realization of the verb.

result:
```html
0. <src>But the Commonwealth </src> <tgt>しかし、</tgt>; start=0.00, end=1.00
1. <src>Department of Agriculture, </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>Fisheries and Forestry </src> <tgt>連邦農林水産省は</tgt>; start=3.00, end=4.00
4. <src>had the foresight to </src> <tgt>先見の明を持ち、</tgt>; start=4.00, end=5.00
5. <src>identify the need for </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>Australia to be </src> <tgt>オーストラリアが</tgt>; start=6.00, end=7.00
7. <src>ahead of the game </src> <tgt>先手を打ち</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>and well coordinated, </src> <tgt>適切に連携する必要性を認識し、</tgt>; start=9.00, end=10.00
10. <src>and so developed the </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Australian Animal Welfare Strategy </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt>8年前に「オーストラリア動物福祉戦略」を策定しました。</tgt>; start=13.00, end=13.66
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[11]
  - verdict: mapping_error
  - reason: "The past tense marker 'ました。' is a functional unit of the verb 'developed' (source 29), not the discourse connector 'so' (source 28)."
  - replace_source_tokens: 29: "developed"
  validation:
    scratchpad:
* target[0]: "しかし、"
  - source_tokens: `0: "But"`
  - mapping_reason: Contrastive conjunction.

* target[1]: "連邦農林水産省は"
  - source_tokens: `1: "the", 2: "Commonwealth", 3: "Department", 4: "of", 5: "Agriculture,", 6: "Fisheries", 7: "and", 8: "Forestry"`
  - mapping_reason: Full name of the government entity.

* target[2]: "先見の明を持ち、"
  - source_tokens: `9: "had", 10: "the", 11: "foresight"`
  - mapping_reason: Idiomatic expression for having foresight.

* target[3]: "オーストラリアが"
  - source_tokens: `17: "Australia"`
  - mapping_reason: Subject of the subordinate clause.

* target[4]: "先手を打ち"
  - source_tokens: `20: "ahead", 21: "of", 22: "the", 23: "game"`
  - mapping_reason: Idiomatic expression for being ahead of the game.

* target[5]: "適切に"
  - source_tokens: `25: "well"`
  - mapping_reason: Adverbial modifier for coordination.

* target[6]: "連携する必要性を"
  - source_tokens: `26: "coordinated,", 15: "need"`
  - mapping_reason: Core noun phrase "need for... coordination".

* target[7]: "認識し、"
  - source_tokens: `12: "to", 13: "identify"`
  - mapping_reason: Verb meaning to recognize/identify.

* target[8]: "8年前に"
  - source_tokens: `35: "eight", 36: "years", 37: "ago."`
  - mapping_reason: Temporal adjunct.

* target[9]: "「オーストラリア動物福祉戦略」を"
  - source_tokens: `31: "Australian", 32: "Animal", 33: "Welfare", 34: "Strategy"`
  - mapping_reason: Name of the strategy.

* target[10]: "策定し"
  - source_tokens: `29: "developed"`
  - mapping_reason: Main verb of the second clause.

* target[11]: "ました。"
  - source_tokens: `28: "so"`
  - mapping_reason: Discourse marker indicating result/consequence.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1, 2, 3, 4, 5, 6, 7, 8]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [9, 10, 11]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [17]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [20, 21, 22, 23]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [25]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [26, 15]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [12, 13]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [35, 36, 37]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [31, 32, 33, 34]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [29]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [28]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== EN_nCDIj7Cde90_W000000 ===

source:
- language: English
- transcription: I'm sorry for not making a video in three hours, but I wanted to tell you I am very sorry that I had to hit three other people like in the same place within less than ten minutes. I also thought that I could be banned from that location because I was being aggressive to them, and this meant.
- source_tokens:
  0. I'm
  1. sorry
  2. for
  3. not
  4. making
  5. a
  6. video
  7. in
  8. three
  9. hours,
  10. but
  11. I
  12. wanted
  13. to
  14. tell
  15. you
  16. I
  17. am
  18. very
  19. sorry
  20. that
  21. I
  22. had
  23. to
  24. hit
  25. three
  26. other
  27. people
  28. like
  29. in
  30. the
  31. same
  32. place
  33. within
  34. less
  35. than
  36. ten
  37. minutes.
  38. I
  39. also
  40. thought
  41. that
  42. I
  43. could
  44. be
  45. banned
  46. from
  47. that
  48. location
  49. because
  50. I
  51. was
  52. being
  53. aggressive
  54. to
  55. them,
  56. and
  57. this
  58. meant.

target:
- language: Korean
- translation: 3시간 동안 영상을 올리지 못해 죄송합니다. 하지만 말씀드리고 싶었던 건, 정말 죄송하다는 거예요. 10분도 안 되는 시간 동안 같은 장소에서 다른 세 사람을 때려야 했어요. 그리고 그들에게 공격적으로 행동해서 그 장소에서 출입 금지를 당할 수도 있겠다고 생각했는데, 이건...
- target_sense_units:
  0. 3시간 동안
  1. 영상을 올리지 못해
  2. 죄송합니다.
  3. 하지만
  4. 말씀드리고 싶었던 건,
  5. 정말 죄송하다는 거예요.
  6. 10분도
  7. 안 되는
  8. 시간 동안
  9. 같은 장소에서
  10. 다른 세 사람을
  11. 때려야 했어요.
  12. 그리고
  13. 그들에게
  14. 공격적으로
  15. 행동해서
  16. 그 장소에서
  17. 출입 금지를
  18. 당할 수도 있겠다고
  19. 생각했는데,
  20. 이건...

scratchpad:
* target[0]: "3시간 동안"
  - source_tokens: `8: "three", 9: "hours,"`
  - mapping_reason: Time duration expression.
* target[1]: "영상을 올리지 못해"
  - source_tokens: `4: "making", 5: "a", 6: "video", 3: "not"`
  - mapping_reason: Negative action of making a video.
* target[2]: "죄송합니다."
  - source_tokens: `0: "I'm", 1: "sorry", 2: "for"`
  - mapping_reason: Apology for the preceding action.
* target[3]: "하지만"
  - source_tokens: `10: "but"`
  - mapping_reason: Contrastive conjunction.
* target[4]: "말씀드리고 싶었던 건,"
  - source_tokens: `11: "I", 12: "wanted", 13: "to", 14: "tell", 15: "you"`
  - mapping_reason: Communicative intent.
* target[5]: "정말 죄송하다는 거예요."
  - source_tokens: `16: "I", 17: "am", 18: "very", 19: "sorry", 20: "that"`
  - mapping_reason: Expression of sincere apology.
* target[6]: "10분도"
  - source_tokens: `36: "ten", 37: "minutes."`
  - mapping_reason: Time quantity.
* target[7]: "안 되는"
  - source_tokens: `33: "within", 34: "less", 35: "than"`
  - mapping_reason: Negation of time threshold.
* target[8]: "시간 동안"
  - source_tokens: `37: "minutes."`
  - mapping_reason: Contextual time duration.
* target[9]: "같은 장소에서"
  - source_tokens: `30: "the", 31: "same", 32: "place"`
  - mapping_reason: Location specification.
* target[10]: "다른 세 사람을"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: Object of the action.
* target[11]: "때려야 했어요."
  - source_tokens: `21: "I", 22: "had", 23: "to", 24: "hit", 28: "like"`
  - mapping_reason: Obligatory action performed.
* target[12]: "그리고"
  - source_tokens: `38: "I"`
  - mapping_reason: Discourse progression (connective).
* target[13]: "그들에게"
  - source_tokens: `54: "to", 55: "them,"`
  - mapping_reason: Recipient of aggression.
* target[14]: "공격적으로"
  - source_tokens: `53: "aggressive"`
  - mapping_reason: Manner of action.
* target[15]: "행동해서"
  - source_tokens: `50: "I", 51: "was", 52: "being"`
  - mapping_reason: Behavioral state.
* target[16]: "그 장소에서"
  - source_tokens: `46: "from", 47: "that", 48: "location"`
  - mapping_reason: Location of potential ban.
* target[17]: "출입 금지를"
  - source_tokens: `45: "banned"`
  - mapping_reason: Resulting state (ban).
* target[18]: "당할 수도 있겠다고"
  - source_tokens: `43: "could", 44: "be"`
  - mapping_reason: Possibility of the outcome.
* target[19]: "생각했는데,"
  - source_tokens: `39: "also", 40: "thought", 41: "that"`
  - mapping_reason: Cognitive state.
* target[20]: "이건..."
  - source_tokens: `56: "and", 57: "this", 58: "meant."`
  - mapping_reason: Referring to the implication.

result:
```html
0. <src>I'm sorry </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>for not making a video </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>in three hours, </src> <tgt>3시간 동안 영상을 올리지 못해 죄송합니다.</tgt>; start=2.00, end=3.00
3. <src>but I wanted to </src> <tgt>하지만</tgt>; start=3.00, end=4.00
4. <src>tell you </src> <tgt>말씀드리고 싶었던 건,</tgt>; start=4.00, end=5.00
5. <src>I am very sorry </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>that I had to </src> <tgt>정말 죄송하다는 거예요.</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>hit three other people </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>like </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>in the same place </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>within less than ten minutes. </src> <tgt>10분도 안 되는 시간 동안 같은 장소에서 다른 세 사람을 때려야 했어요.</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>I also thought that I could </src> <tgt>그리고</tgt>; start=15.00, end=16.00
16. <src>be banned from </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>that location </src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>because I was </src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>being aggressive </src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>to them, </src> <tgt>그들에게 공격적으로 행동해서 그 장소에서 출입 금지를 당할 수도 있겠다고 생각했는데,</tgt>; start=20.00, end=21.00
21. <src><|wait|></src> <tgt><|wait|></tgt>; start=21.00, end=22.00
22. <src>and this meant. </src> <tgt>이건...</tgt>; start=22.00, end=22.20
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: failed_after_response
  reason: JSON Format Error: Unterminated string starting at: line 12 column 4 (char 625)
  validation:
    scratchpad:
* target[0]: "3시간 동안"
  - source_tokens: `8: "three", 9: "hours,"`
  - mapping_reason: Time duration expression.
* target[1]: "영상을 올리지 못해"
  - source_tokens: `3: "not", 4: "making", 5: "a", 6: "video"`
  - mapping_reason: Reason for being sorry (not making a video).
* target[2]: "죄송합니다."
  - source_tokens: `0: "I'm", 1: "sorry"`
  - mapping_reason: Expression of apology.
* target[3]: "하지만"
  - source_tokens: `10: "but"`
  - mapping_reason: Contrastive conjunction.
* target[4]: "말씀드리고 싶었던 건,"
  - source_tokens: `11: "I", 12: "wanted", 13: "to", 14: "tell", 15: "you"`
  - mapping_reason: Intent to communicate.
* target[5]: "정말 죄송하다는 거예요."
  - source_tokens: `16: "I", 17: "am", 18: "very", 19: "sorry"`
  - mapping_reason: Intensified apology.
* target[6]: "10분도"
  - source_tokens: `36: "ten", 37: "minutes."`
  - mapping_reason: Time quantity.
* target[7]: "안 되는"
  - source_tokens: `33: "within", 34: "less", 35: "than"`
  - mapping_reason: Negation/limitation of time.
* target[8]: "시간 동안"
  - source_tokens: `37: "minutes."`
  - mapping_reason: Temporal duration context.
* target[9]: "같은 장소에서"
  - source_tokens: `30: "the", 31: "same", 32: "place"`
  - mapping_reason: Location context.
* target[10]: "다른 세 사람을"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: Affected entities.
* target[11]: "때려야 했어요."
  - source_tokens: `21: "I", 22: "had", 23: "to", 24: "hit"`
  - mapping_reason: Action performed (obligation).
* target[12]: "그리고"
  - source_tokens: `39: "also"`
  - mapping_reason: Additive conjunction.
* target[13]: "그들에게"
  - source_tokens: `54: "to", 55: "them,"`
  - mapping_reason: Recipient of aggression.
* target[14]: "공격적으로"
  - source_tokens: `53: "aggressive"`
  - mapping_reason: Manner of behavior.
* target[15]: "행동해서"
  - source_tokens: `51: "was", 52: "being"`
  - mapping_reason: Verb/action of being aggressive.
* target[16]: "그 장소에서"
  - source_tokens: `46: "from", 47: "that", 48: "location"`
  - mapping_reason: Location of ban.
* target[17]: "출입 금지를"
  - source_tokens: `45: "banned"`
  - mapping_reason: Consequence (ban).
* target[18]: "당할 수도 있겠다고"
  - source_tokens: `43: "could", 44: "be"`
  - mapping_reason: Possibility/modal.
* target[19]: "생각했는데,"
  - source_tokens: `40: "thought", 41: "that"`
  - mapping_reason: Cognitive state.
* target[20]: "이건..."
  - source_tokens: `56: "and", 57: "this", 58: "meant."`
  - mapping_reason: Concluding reference.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [8, 9]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4, 5, 6]},
  {"target_senseunit_id": 2, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 3, "source_token_ids": [10]},
  {"target_senseunit_id": 4, "source_token_ids": [11, 12, 13, 14, 15]},
  {"target_senseunit_id": 5, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 6, "source_token_ids": [36, 37]},
  {"target_senseunit_id": 7, "source_token_ids": [33, 34, 35]},
  {"target_senseunit_id": 8, "source_token_ids": [37]},
  {"target_senseunit_id": 9, "source_token_ids": [30, 31, 32]},
  {"

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== EN_nCDIj7Cde90_W000000 ===

source:
- language: English
- transcription: I'm sorry for not making a video in three hours, but I wanted to tell you I am very sorry that I had to hit three other people like in the same place within less than ten minutes. I also thought that I could be banned from that location because I was being aggressive to them, and this meant.
- source_tokens:
  0. I'm
  1. sorry
  2. for
  3. not
  4. making
  5. a
  6. video
  7. in
  8. three
  9. hours,
  10. but
  11. I
  12. wanted
  13. to
  14. tell
  15. you
  16. I
  17. am
  18. very
  19. sorry
  20. that
  21. I
  22. had
  23. to
  24. hit
  25. three
  26. other
  27. people
  28. like
  29. in
  30. the
  31. same
  32. place
  33. within
  34. less
  35. than
  36. ten
  37. minutes.
  38. I
  39. also
  40. thought
  41. that
  42. I
  43. could
  44. be
  45. banned
  46. from
  47. that
  48. location
  49. because
  50. I
  51. was
  52. being
  53. aggressive
  54. to
  55. them,
  56. and
  57. this
  58. meant.

target:
- language: Japanese
- translation: 3時間動画を上げられなくてごめん。でも言いたかったのは、10分も経たないうちに同じ場所で他の3人を叩いちゃったこと、それが本当に申し訳ないってこと。相手に攻撃的になったから、その場所から出入り禁止になるかもとも思った。つまり、これは…
- target_sense_units:
  0. 3時間動画を
  1. 上げられなくて
  2. ごめん。
  3. でも
  4. 言いたかったのは、
  5. 10分も経たないうちに
  6. 同じ場所で
  7. 他の3人を
  8. 叩いちゃった
  9. こと、
  10. それが
  11. 本当に
  12. 申し訳ない
  13. ってこと。
  14. 相手に
  15. 攻撃的になったから、
  16. その場所から
  17. 出入り禁止になる
  18. かもとも
  19. 思った。
  20. つまり、
  21. これ
  22. は…

scratchpad:
* target[0]: "3時間動画を"
  - source_tokens: `7: "three", 8: "hours", 5: "a", 6: "video"`
  - mapping_reason: "3 hours" and "a video" (object of the action)
* target[1]: "上げられなくて"
  - source_tokens: `3: "not", 4: "making"`
  - mapping_reason: "not making" (inability to upload/make)
* target[2]: "ごめん。"
  - source_tokens: `0: "I'm", 1: "sorry"`
  - mapping_reason: "I'm sorry"
* target[3]: "でも"
  - source_tokens: `10: "but"`
  - mapping_reason: "but"
* target[4]: "言いたかったのは、"
  - source_tokens: `12: "wanted", 13: "to", 14: "tell", 15: "you"`
  - mapping_reason: "wanted to tell you"
* target[5]: "10分も経たないうちに"
  - source_tokens: `33: "within", 34: "less", 35: "than", 36: "ten", 37: "minutes."`
  - mapping_reason: "within less than ten minutes"
* target[6]: "同じ場所で"
  - source_tokens: `30: "the", 31: "same", 32: "place"`
  - mapping_reason: "in the same place"
* target[7]: "他の3人を"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: "three other people"
* target[8]: "叩いちゃった"
  - source_tokens: `24: "hit"`
  - mapping_reason: "hit"
* target[9]: "こと、"
  - source_tokens: `22: "had", 23: "to"`
  - mapping_reason: "nominalizer for the event of having to hit"
* target[10]: "それが"
  - source_tokens: `20: "that"`
  - mapping_reason: "that (referring to the event)"
* target[11]: "本当に"
  - source_tokens: `18: "very"`
  - mapping_reason: "very"
* target[12]: "申し訳ない"
  - source_tokens: `19: "sorry"`
  - mapping_reason: "sorry"
* target[13]: "ってこと。"
  - source_tokens: `20: "that"`
  - mapping_reason: "nominalizer/discourse connector (that)"
* target[14]: "相手に"
  - source_tokens: `54: "to", 55: "them,"`
  - mapping_reason: "to them"
* target[15]: "攻撃的になったから、"
  - source_tokens: `49: "because", 51: "was", 52: "being", 53: "aggressive"`
  - mapping_reason: "because I was being aggressive"
* target[16]: "その場所から"
  - source_tokens: `46: "from", 47: "that", 48: "location"`
  - mapping_reason: "from that location"
* target[17]: "出入り禁止になる"
  - source_tokens: `44: "be", 45: "banned"`
  - mapping_reason: "be banned"
* target[18]: "かもとも"
  - source_tokens: `43: "could"`
  - mapping_reason: "could (possibility)"
* target[19]: "思った。"
  - source_tokens: `38: "I", 39: "also", 40: "thought"`
  - mapping_reason: "I also thought"
* target[20]: "つまり、"
  - source_tokens: `58: "meant."`
  - mapping_reason: "meant (discourse marker)"
* target[21]: "これ"
  - source_tokens: `57: "this"`
  - mapping_reason: "this"
* target[22]: "は…"
  - source_tokens: `58: "meant."`
  - mapping_reason: "meant (implied structure)"

result:
```html
0. <src>I'm sorry </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>for not making a video </src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>in three hours, </src> <tgt>3時間動画を上げられなくてごめん。</tgt>; start=2.00, end=3.00
3. <src>but I wanted to </src> <tgt>でも</tgt>; start=3.00, end=4.00
4. <src>tell you </src> <tgt>言いたかったのは、</tgt>; start=4.00, end=5.00
5. <src>I am very sorry </src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>that I had to </src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>hit three other people </src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>like </src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>in the same place </src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>within less than ten minutes. </src> <tgt>10分も経たないうちに同じ場所で他の3人を叩いちゃったこと、それが本当に申し訳ないってこと。</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>I also thought that I could </src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>be banned from </src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>that location </src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>because I was </src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>being aggressive </src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>to them, </src> <tgt>相手に攻撃的になったから、その場所から出入り禁止になるかもとも思った。</tgt>; start=20.00, end=21.00
21. <src><|wait|></src> <tgt><|wait|></tgt>; start=21.00, end=22.00
22. <src>and this meant. </src> <tgt>つまり、これは…</tgt>; start=22.00, end=22.20
```

- max_empty_window_count: 8


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[10]
  - verdict: mapping_error
  - reason: "The target sense unit 'それが' (that [thing]) refers to the action of hitting people (the clause starting at source token 22), not the pronoun 'I' (source token 21)."
  - replace_source_tokens: 22: "had", 23: "to", 24: "hit", 25: "three", 26: "other", 27: "people"
  validation:
    scratchpad:
* target[0]: "3時間動画を"
  - source_tokens: `8: "three", 9: "hours,", 5: "a", 6: "video"`
  - mapping_reason: Time duration and object of the action.
* target[1]: "上げられなくて"
  - source_tokens: `3: "not", 4: "making"`
  - mapping_reason: Negated action of making (uploading) the video.
* target[2]: "ごめん。"
  - source_tokens: `0: "I'm", 1: "sorry"`
  - mapping_reason: Apology expression.
* target[3]: "でも"
  - source_tokens: `10: "but"`
  - mapping_reason: Contrastive conjunction.
* target[4]: "言いたかったのは、"
  - source_tokens: `12: "wanted", 13: "to", 14: "tell", 15: "you"`
  - mapping_reason: Intent to communicate.
* target[5]: "10分も経たないうちに"
  - source_tokens: `33: "within", 34: "less", 35: "than", 36: "ten", 37: "minutes."`
  - mapping_reason: Time constraint.
* target[6]: "同じ場所で"
  - source_tokens: `30: "the", 31: "same", 32: "place"`
  - mapping_reason: Location specification.
* target[7]: "他の3人を"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: Object of the action.
* target[8]: "叩いちゃった"
  - source_tokens: `24: "hit"`
  - mapping_reason: The action performed.
* target[9]: "こと、"
  - source_tokens: `20: "that"`
  - mapping_reason: Nominalizer for the clause.
* target[10]: "それが"
  - source_tokens: `21: "I"`
  - mapping_reason: Subject reference (implied by the apologetic clause structure).
* target[11]: "本当に"
  - source_tokens: `18: "very"`
  - mapping_reason: Intensifier.
* target[12]: "申し訳ない"
  - source_tokens: `19: "sorry"`
  - mapping_reason: Apology state.
* target[13]: "ってこと。"
  - source_tokens: `20: "that"`
  - mapping_reason: Closing nominalizer for the apology clause.
* target[14]: "相手に"
  - source_tokens: `54: "to", 55: "them,"`
  - mapping_reason: Recipient of aggression.
* target[15]: "攻撃的になったから、"
  - source_tokens: `51: "was", 52: "being", 53: "aggressive", 49: "because"`
  - mapping_reason: Cause of the potential ban.
* target[16]: "その場所から"
  - source_tokens: `46: "from", 47: "that", 48: "location"`
  - mapping_reason: Origin of the ban.
* target[17]: "出入り禁止になる"
  - source_tokens: `45: "banned"`
  - mapping_reason: Resulting state.
* target[18]: "かもとも"
  - source_tokens: `43: "could"`
  - mapping_reason: Possibility marker.
* target[19]: "思った。"
  - source_tokens: `40: "thought"`
  - mapping_reason: Cognitive state.
* target[20]: "つまり、"
  - source_tokens: `57: "this"`
  - mapping_reason: Discourse marker for explanation.
* target[21]: "これ"
  - source_tokens: `57: "this"`
  - mapping_reason: Subject of the final unfinished thought.
* target[22]: "は…"
  - source_tokens: `58: "meant."`
  - mapping_reason: Verb indicating meaning/implication.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5, 6, 8, 9]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 3, "source_token_ids": [10]},
  {"target_senseunit_id": 4, "source_token_ids": [12, 13, 14, 15]},
  {"target_senseunit_id": 5, "source_token_ids": [33, 34, 35, 36, 37]},
  {"target_senseunit_id": 6, "source_token_ids": [30, 31, 32]},
  {"target_senseunit_id": 7, "source_token_ids": [25, 26, 27]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [20]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [18]},
  {"target_senseunit_id": 12, "source_token_ids": [19]},
  {"target_senseunit_id": 13, "source_token_ids": [20]},
  {"target_senseunit_id": 14, "source_token_ids": [54, 55]},
  {"target_senseunit_id": 15, "source_token_ids": [49, 51, 52, 53]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47, 48]},
  {"target_senseunit_id": 17, "source_token_ids": [45]},
  {"target_senseunit_id": 18, "source_token_ids": [43]},
  {"target_senseunit_id": 19, "source_token_ids": [40]},
  {"target_senseunit_id": 20, "source_token_ids": [57]},
  {"target_senseunit_id": 21, "source_token_ids": [57]},
  {"target_senseunit_id": 22, "source_token_ids": [58]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[10]
  - verdict: mapping_error
  - reason: "The target unit 'それが' (that is) acts as a pronoun referring to the preceding event. It does not represent the components of the event (hitting three people) itself, but rather the demonstrative 'that' (index 20) referring back to that event."
  - replace_source_tokens: 20: "that"
  validation:
    scratchpad:
* target[0]: "3時間動画を"
  - source_tokens: `8: "three", 9: "hours,", 5: "a", 6: "video"`
  - mapping_reason: "three hours" and "a video"
* target[1]: "上げられなくて"
  - source_tokens: `3: "not", 4: "making"`
  - mapping_reason: "not making" (negation of action)
* target[2]: "ごめん。"
  - source_tokens: `0: "I'm", 1: "sorry"`
  - mapping_reason: "I'm sorry"
* target[3]: "でも"
  - source_tokens: `10: "but"`
  - mapping_reason: "but"
* target[4]: "言いたかったのは、"
  - source_tokens: `12: "wanted", 13: "to", 14: "tell"`
  - mapping_reason: "wanted to tell"
* target[5]: "10分も経たないうちに"
  - source_tokens: `33: "within", 34: "less", 35: "than", 36: "ten", 37: "minutes."`
  - mapping_reason: "within less than ten minutes"
* target[6]: "同じ場所で"
  - source_tokens: `29: "in", 30: "the", 31: "same", 32: "place"`
  - mapping_reason: "in the same place"
* target[7]: "他の3人を"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: "three other people"
* target[8]: "叩いちゃった"
  - source_tokens: `22: "had", 23: "to", 24: "hit"`
  - mapping_reason: "had to hit"
* target[9]: "こと、"
  - source_tokens: `20: "that"`
  - mapping_reason: "that (nominalizer)"
* target[10]: "それが"
  - source_tokens: `22: "had", 23: "to", 24: "hit", 25: "three", 26: "other", 27: "people"`
  - mapping_reason: "refers to the act of hitting others"
* target[11]: "本当に"
  - source_tokens: `18: "very"`
  - mapping_reason: "very"
* target[12]: "申し訳ない"
  - source_tokens: `19: "sorry"`
  - mapping_reason: "sorry"
* target[13]: "ってこと。"
  - source_tokens: `20: "that"`
  - mapping_reason: "that (complementizer)"
* target[14]: "相手に"
  - source_tokens: `54: "to", 55: "them,"`
  - mapping_reason: "to them"
* target[15]: "攻撃的になったから、"
  - source_tokens: `49: "because", 51: "was", 52: "being", 53: "aggressive"`
  - mapping_reason: "because I was being aggressive"
* target[16]: "その場所から"
  - source_tokens: `46: "from", 47: "that", 48: "location"`
  - mapping_reason: "from that location"
* target[17]: "出入り禁止になる"
  - source_tokens: `44: "be", 45: "banned"`
  - mapping_reason: "be banned"
* target[18]: "かもとも"
  - source_tokens: `43: "could"`
  - mapping_reason: "could (possibility)"
* target[19]: "思った。"
  - source_tokens: `39: "also", 40: "thought"`
  - mapping_reason: "also thought"
* target[20]: "つまり、"
  - source_tokens: `57: "this"`
  - mapping_reason: "this (introductory discourse marker)"
* target[21]: "これ"
  - source_tokens: `57: "this"`
  - mapping_reason: "this"
* target[22]: "は…"
  - source_tokens: `58: "meant."`
  - mapping_reason: "meant"
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [8, 9, 5, 6]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 3, "source_token_ids": [10]},
  {"target_senseunit_id": 4, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 5, "source_token_ids": [33, 34, 35, 36, 37]},
  {"target_senseunit_id": 6, "source_token_ids": [29, 30, 31, 32]},
  {"target_senseunit_id": 7, "source_token_ids": [25, 26, 27]},
  {"target_senseunit_id": 8, "source_token_ids": [22, 23, 24]},
  {"target_senseunit_id": 9, "source_token_ids": [20]},
  {"target_senseunit_id": 10, "source_token_ids": [22, 23, 24, 25, 26, 27]},
  {"target_senseunit_id": 11, "source_token_ids": [18]},
  {"target_senseunit_id": 12, "source_token_ids": [19]},
  {"target_senseunit_id": 13, "source_token_ids": [20]},
  {"target_senseunit_id": 14, "source_token_ids": [54, 55]},
  {"target_senseunit_id": 15, "source_token_ids": [49, 51, 52, 53]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47, 48]},
  {"target_senseunit_id": 17, "source_token_ids": [44, 45]},
  {"target_senseunit_id": 18, "source_token_ids": [43]},
  {"target_senseunit_id": 19, "source_token_ids": [39, 40]},
  {"target_senseunit_id": 20, "source_token_ids": [57]},
  {"target_senseunit_id": 21, "source_token_ids": [57]},
  {"target_senseunit_id": 22, "source_token_ids": [58]}
]

- retry: 2/5
  status: failed_after_response
  reason: * target[13]
  - verdict: mapping_error
  - reason: "The target sense unit 'ってこと' acts as a nominalizer/discourse connector for the previous clause, which is anchored by 'that' (source token 20), not 'I am'."
  - replace_source_tokens: 20: "that"
  validation:
    scratchpad:
* target[0]: "3時間動画を"
  - source_tokens: `7: "three", 8: "hours", 5: "a", 6: "video"`
  - mapping_reason: "three hours" and "a video"
* target[1]: "上げられなくて"
  - source_tokens: `3: "not", 4: "making"`
  - mapping_reason: "not making"
* target[2]: "ごめん。"
  - source_tokens: `0: "I'm", 1: "sorry", 2: "for"`
  - mapping_reason: "I'm sorry for"
* target[3]: "でも"
  - source_tokens: `10: "but"`
  - mapping_reason: "but"
* target[4]: "言いたかったのは、"
  - source_tokens: `12: "wanted", 13: "to", 14: "tell", 15: "you"`
  - mapping_reason: "wanted to tell you"
* target[5]: "10分も経たないうちに"
  - source_tokens: `33: "within", 34: "less", 35: "than", 36: "ten", 37: "minutes."`
  - mapping_reason: "within less than ten minutes"
* target[6]: "同じ場所で"
  - source_tokens: `30: "the", 31: "same", 32: "place"`
  - mapping_reason: "in the same place"
* target[7]: "他の3人を"
  - source_tokens: `25: "three", 26: "other", 27: "people"`
  - mapping_reason: "three other people"
* target[8]: "叩いちゃった"
  - source_tokens: `24: "hit"`
  - mapping_reason: "hit"
* target[9]: "こと、"
  - source_tokens: `22: "had", 23: "to"`
  - mapping_reason: "nominalizer for the action 'had to hit'"
* target[10]: "それが"
  - source_tokens: `20: "that"`
  - mapping_reason: "demonstrative pronoun referring back to the preceding event"
* target[11]: "本当に"
  - source_tokens: `18: "very"`
  - mapping_reason: "very"
* target[12]: "申し訳ない"
  - source_tokens: `19: "sorry"`
  - mapping_reason: "sorry"
* target[13]: "ってこと。"
  - source_tokens: `16: "I", 17: "am"`
  - mapping_reason: "complementizer structure for 'I am sorry'"
* target[14]: "相手に"
  - source_tokens: `55: "them,"`
  - mapping_reason: "referring to the people hit"
* target[15]: "攻撃的になったから、"
  - source_tokens: `49: "because", 51: "was", 52: "being", 53: "aggressive", 54: "to"`
  - mapping_reason: "because I was being aggressive to"
* target[16]: "その場所から"
  - source_tokens: `47: "that", 48: "location"`
  - mapping_reason: "from that location"
* target[17]: "出入り禁止になる"
  - source_tokens: `44: "banned", 45: "from"`
  - mapping_reason: "be banned from"
* target[18]: "かもとも"
  - source_tokens: `43: "could"`
  - mapping_reason: "could (modal possibility)"
* target[19]: "思った。"
  - source_tokens: `38: "I", 39: "also", 40: "thought", 41: "that"`
  - mapping_reason: "I also thought that"
* target[20]: "つまり、"
  - source_tokens: `56: "and"`
  - mapping_reason: "discourse connective"
* target[21]: "これ"
  - source_tokens: `57: "this"`
  - mapping_reason: "this"
* target[22]: "は…"
  - source_tokens: `58: "meant."`
  - mapping_reason: "meant"
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5, 6, 7, 8]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [0, 1, 2]},
  {"target_senseunit_id": 3, "source_token_ids": [10]},
  {"target_senseunit_id": 4, "source_token_ids": [12, 13, 14, 15]},
  {"target_senseunit_id": 5, "source_token_ids": [33, 34, 35, 36, 37]},
  {"target_senseunit_id": 6, "source_token_ids": [30, 31, 32]},
  {"target_senseunit_id": 7, "source_token_ids": [25, 26, 27]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [20]},
  {"target_senseunit_id": 11, "source_token_ids": [18]},
  {"target_senseunit_id": 12, "source_token_ids": [19]},
  {"target_senseunit_id": 13, "source_token_ids": [16, 17]},
  {"target_senseunit_id": 14, "source_token_ids": [55]},
  {"target_senseunit_id": 15, "source_token_ids": [49, 51, 52, 53, 54]},
  {"target_senseunit_id": 16, "source_token_ids": [47, 48]},
  {"target_senseunit_id": 17, "source_token_ids": [44, 45]},
  {"target_senseunit_id": 18, "source_token_ids": [43]},
  {"target_senseunit_id": 19, "source_token_ids": [38, 39, 40, 41]},
  {"target_senseunit_id": 20, "source_token_ids": [56]},
  {"target_senseunit_id": 21, "source_token_ids": [57]},
  {"target_senseunit_id": 22, "source_token_ids": [58]}
]

- retry: 3/5
  status: succeeded
  reason: retry attempt succeeded

---
=== EN_nN_EW5TiHKQ_W000023 ===

source:
- language: English
- transcription: Who can help you way more than I can. I really appreciate my trans followers when they tell me that they value my opinion on books, or when they tell me that they read a book because of me. Like I have gotten so many DMs from people saying, "Hey, I read Stay Gold because of you, and it was so good," and that honestly makes me so happy.
- source_tokens:
  0. Who
  1. can
  2. help
  3. you
  4. way
  5. more
  6. than
  7. I
  8. can.
  9. I
  10. really
  11. appreciate
  12. my
  13. trans
  14. followers
  15. when
  16. they
  17. tell
  18. me
  19. that
  20. they
  21. value
  22. my
  23. opinion
  24. on
  25. books,
  26. or
  27. when
  28. they
  29. tell
  30. me
  31. that
  32. they
  33. read
  34. a
  35. book
  36. because
  37. of
  38. me.
  39. Like
  40. I
  41. have
  42. gotten
  43. so
  44. many
  45. DMs
  46. from
  47. people
  48. saying,"
  49. Hey,
  50. I
  51. read
  52. Stay
  53. Gold
  54. because
  55. of
  56. you,
  57. and
  58. it
  59. was
  60. so
  61. good,"
  62. and
  63. that
  64. honestly
  65. makes
  66. me
  67. so
  68. happy.

target:
- language: Korean
- translation: 저보다 훨씬 더 도움을 줄 수 있는 분들이 있어요. 제 트랜스젠더 팔로워분들께 정말 감사해요, 그분들이 제 책에 대한 의견을 소중히 여긴다고 말해주거나 저 때문에 책을 읽었다고 말해줄 때요. 사람들에게서 "덕분에 스테이 골드를 읽었는데 정말 좋았어요" 같은 DM을 정말 많이 받았는데, 그게 저를 정말 행복하게 해요.
- target_sense_units:
  0. 저보다
  1. 훨씬 더
  2. 도움을
  3. 줄 수 있는
  4. 분들이
  5. 있어요.
  6. 제 트랜스젠더 팔로워분들께
  7. 정말 감사해요,
  8. 그분들이
  9. 제 책에 대한 의견을
  10. 소중히 여긴다고
  11. 말해주거나
  12. 저 때문에
  13. 책을
  14. 읽었다고
  15. 말해줄 때요.
  16. 사람들에게서"
  17. 덕분에
  18. 스테이 골드를
  19. 읽었는데
  20. 정말 좋았어요"
  21. 같은 DM을
  22. 정말 많이
  23. 받았는데,
  24. 그게
  25. 저를
  26. 정말
  27. 행복하게 해요.

scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`
  - mapping_reason: Represents the comparison base "than I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: Intensifier for the comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Object of the help action.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: Potential modality for the help action.
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: Subject/Agent of the helping action (relative pronoun).
* target[5]: "있어요."
  - source_tokens: `1: "can", 2: "help"`
  - mapping_reason: Existential completion of the predicate "can help".
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: Addressee/Recipient of the appreciation.
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: Expression of gratitude.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Subject of the reported clauses.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: Object of the valuing action.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb of valuing.
* target[11]: "말해주거나"
  - source_tokens: `17: "tell", 18: "me"`
  - mapping_reason: First reporting verb.
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: Causative agent.
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: Object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Verb of reading.
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when", 27: "when", 29: "tell", 30: "me"`
  - mapping_reason: Temporal condition for the appreciation.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: Source of the DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: Attribution of cause for reading.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: Title of the book read.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Verb of reading.
* target[20]: "정말 좋았어요\""
  - source_tokens: `59: "was", 60: "so", 61: "good,"`
  - mapping_reason: Positive assessment.
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: The object received.
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: Quantity of DMs.
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: Verb of receiving.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Subject of the effect.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Experiencer of the happiness.
* target[26]: "정말"
  - source_tokens: `67: "so"`
  - mapping_reason: Intensifier for happy.
* target[27]: "행복하게 해요."
  - source_tokens: `64: "honestly", 65: "makes", 68: "happy."`
  - mapping_reason: Causative emotional result.

result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [1, 2]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 27, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [59, 60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [67]},
  {"target_senseunit_id": 27, "source_token_ids": [64, 65, 68]}
]

errors:
* target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun, while '분들이' functions as the subject of a declarative statement in the target context. The mapping is semantically mismatched."
  - replace_source_tokens: 0: "Who"

attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun, while '분들이' (people) functions as the subject of the declarative sentence. The correct source anchor is 'people'."
  - replace_source_tokens: 47: "people"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`, `6: "than"`
  - mapping_reason: Comparative structure "than I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way"`, `5: "more"`
  - mapping_reason: Intensifier for comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Core noun/object of helping.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: Modal verb expressing ability.
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: Subject reference (Who).
* target[5]: "있어요."
  - source_tokens: `8: "can."`
  - mapping_reason: Existence/predicate completion.
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my"`, `13: "trans"`, `14: "followers"`
  - mapping_reason: Addressee/beneficiary of appreciation.
* target[7]: "정말 감사해요,"
  - source_tokens: `9: "I"`, `10: "really"`, `11: "appreciate"`
  - mapping_reason: Subject, intensifier, and verb of appreciation.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Anaphoric reference to followers.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my"`, `23: "opinion"`, `24: "on"`, `25: "books,"`
  - mapping_reason: Object of the opinion.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb of valuation.
* target[11]: "말해주거나"
  - source_tokens: `17: "tell"`, `18: "me"`, `26: "or"`
  - mapping_reason: Reporting verb and disjunctive connective.
* target[12]: "저 때문에"
  - source_tokens: `36: "because"`, `37: "of"`, `38: "me."`
  - mapping_reason: Causal phrase.
* target[13]: "책을"
  - source_tokens: `34: "a"`, `35: "book"`
  - mapping_reason: Object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Verb of reading.
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when"`, `27: "when"`, `29: "tell"`, `30: "me"`
  - mapping_reason: Temporal condition/reporting verb.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from"`, `47: "people"`
  - mapping_reason: Source of the DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because"`, `55: "of"`, `56: "you,"`
  - mapping_reason: Causal/attribution phrase.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay"`, `53: "Gold"`
  - mapping_reason: Title of the book.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Verb of reading.
* target[20]: "정말 좋았어요\""
  - source_tokens: `58: "it"`, `59: "was"`, `60: "so"`, `61: "good,\""`
  - mapping_reason: Evaluation of the book.
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`, `48: "saying,\""`
  - mapping_reason: Object of receiving.
* target[22]: "정말 많이"
  - source_tokens: `43: "so"`, `44: "many"`
  - mapping_reason: Quantity of DMs.
* target[23]: "받았는데,"
  - source_tokens: `41: "have"`, `42: "gotten"`
  - mapping_reason: Main verb of receiving.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Subject of the final clause.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Object of happiness.
* target[26]: "정말"
  - source_tokens: `67: "so"`
  - mapping_reason: Intensifier of happiness.
* target[27]: "행복하게 해요."
  - source_tokens: `64: "honestly"`, `65: "makes"`, `68: "happy."`
  - mapping_reason: Causative verb and emotional state.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [6, 7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [8]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [9, 10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [34, 35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 27, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [58, 59, 60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45, 48]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [67]},
  {"target_senseunit_id": 27, "source_token_ids": [64, 65, 68]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun and does not directly translate to the noun '분들이' (people/individuals), which acts as the subject of the target sentence."
  - replace_source_tokens: 0: "Who"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`
  - mapping_reason: "I" (subject of comparison)
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: "way more" (intensifier of comparison)
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: "help" (noun object)
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: "can" (potential modality)
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: "Who" (referring to the people who can help)
* target[5]: "있어요."
  - source_tokens: `8: "can."`
  - mapping_reason: "can" (existence/potentiality in context)
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: "my trans followers"
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: "really appreciate"
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: "they" (anaphora)
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: "my opinion on books"
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: "value"
* target[11]: "말해주거나"
  - source_tokens: `17: "tell", 18: "me", 26: "or"`
  - mapping_reason: "tell me... or"
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: "because of me"
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: "book"
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: "read"
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when", 27: "when", 29: "tell", 30: "me"`
  - mapping_reason: "when they tell me"
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: "from people"
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: "because of you"
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: "Stay Gold"
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: "read"
* target[20]: "정말 좋았어요\""
  - source_tokens: `59: "was", 60: "so", 61: "good,"`
  - mapping_reason: "was so good"
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs", 48: "saying,"`
  - mapping_reason: "DMs saying"
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: "so many"
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: "have gotten"
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: "that"
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: "me"
* target[26]: "정말"
  - source_tokens: `64: "honestly", 67: "so"`
  - mapping_reason: "honestly / so"
* target[27]: "행복하게 해요."
  - source_tokens: `65: "makes", 68: "happy."`
  - mapping_reason: "makes me happy"
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [8]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 27, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [59, 60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45, 48]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [64, 67]},
  {"target_senseunit_id": 27, "source_token_ids": [65, 68]}
]

- retry: 2/5
  status: failed_after_response
  reason: * target[5]
  - verdict: mapping_error
  - reason: "The target unit '있어요' (exist) is the main verb of the first sentence, relating to the ability to help, not the pronoun 'you'."
  - replace_source_tokens: 0: "Who", 1: "can", 2: "help"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`
  - mapping_reason: "I" (subject of comparison)
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: intensifier for comparison
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: core verb object
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can", 8: "can"`
  - mapping_reason: modal capacity
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: interrogative pronoun functioning as indefinite pronoun (someone/people)
* target[5]: "있어요."
  - source_tokens: `3: "you"`
  - mapping_reason: existential predicate implied by the context of "Who can help you"
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: indirect object of gratitude
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: expression of gratitude
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: subject pronoun referring to followers
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: object of opinion
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: verb expressing valuing
* target[11]: "말해주거나"
  - source_tokens: `17: "tell", 26: "or"`
  - mapping_reason: verb of saying and disjunctive connector
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: causal modifier
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: object of reading
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: verb of reading
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when", 29: "tell", 30: "me"`
  - mapping_reason: temporal clause marker and verb
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: source of DMs
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: causal modifier
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: book title
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: verb of reading
* target[20]: "정말 좋았어요\""
  - source_tokens: `60: "so", 61: "good,\""`
  - mapping_reason: evaluative adjective
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: direct object
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: quantifier
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: main verb of receiving
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: demonstrative pronoun
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: object of feeling
* target[26]: "정말"
  - source_tokens: `67: "so"`
  - mapping_reason: intensifier
* target[27]: "행복하게 해요."
  - source_tokens: `64: "honestly", 65: "makes", 68: "happy."`
  - mapping_reason: causative verb and adjective
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1, 8]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [3]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [67]},
  {"target_senseunit_id": 27, "source_token_ids": [64, 65, 68]}
]

- retry: 3/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun and does not correspond to the noun '분들이' (people), which refers to the people who can help."
  - replace_source_tokens: 47: "people"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`
  - mapping_reason: "I" (comparison base)
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: "way more"
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: "help"
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: "can"
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: "Who"
* target[5]: "있어요."
  - source_tokens: `0: "Who", 1: "can", 2: "help"`
  - mapping_reason: "Existential/predicative structure of 'Who can help'"
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: "my trans followers"
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: "really appreciate"
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: "they"
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: "my opinion on books"
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: "value"
* target[11]: "말해주거나"
  - source_tokens: `17: "tell", 26: "or"`
  - mapping_reason: "tell... or"
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: "because of me"
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: "book"
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: "read"
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when", 29: "tell"`
  - mapping_reason: "when... tell"
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: "from people"
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: "because of you"
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: "Stay Gold"
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: "read"
* target[20]: "정말 좋았어요\""
  - source_tokens: `59: "was", 60: "so", 61: "good,"`
  - mapping_reason: "was so good"
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: "DMs"
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: "so many"
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: "have gotten"
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: "that"
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: "me"
* target[26]: "정말"
  - source_tokens: `67: "so"`
  - mapping_reason: "so"
* target[27]: "행복하게 해요."
  - source_tokens: `64: "honestly", 65: "makes", 68: "happy."`
  - mapping_reason: "honestly makes happy"
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [0, 1, 2]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 29]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [59, 60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [67]},
  {"target_senseunit_id": 27, "source_token_ids": [64, 65, 68]}
]

- retry: 4/5
  status: failed_after_response
  reason: * target[5]
  - verdict: mapping_error
  - reason: "The target unit '있어요' (existential) corresponds to the completion of the 'can help' predicate, not the interrogative 'Who'."
  - replace_source_tokens: 1: "can", 2: "help"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`, `6: "than"`
  - mapping_reason: Comparison with "I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way"`, `5: "more"`
  - mapping_reason: Intensifier for comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Core object of help.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`, `8: "can."`
  - mapping_reason: Modal verb expressing ability.
* target[4]: "분들이"
  - source_tokens: `47: "people"`
  - mapping_reason: Subject of the existence clause, referring to the people who can help.
* target[5]: "있어요."
  - source_tokens: `0: "Who"`
  - mapping_reason: "Who" in this context functions as an existential quantification (there are people who...).
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my"`, `13: "trans"`, `14: "followers"`
  - mapping_reason: Addressee of appreciation.
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really"`, `11: "appreciate"`
  - mapping_reason: Expression of gratitude.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Anaphoric reference to followers.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my"`, `23: "opinion"`, `24: "on"`, `25: "books,"`
  - mapping_reason: Object of value.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb meaning to value/cherish.
* target[11]: "말해주거나"
  - source_tokens: `17: "tell"`, `18: "me"`
  - mapping_reason: Communication verb.
* target[12]: "저 때문에"
  - source_tokens: `36: "because"`, `37: "of"`, `38: "me."`
  - mapping_reason: Causal relation.
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: Object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Verb meaning to read.
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when"`, `27: "when"`, `29: "tell"`, `30: "me"`
  - mapping_reason: Temporal condition for appreciation.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from"`, `47: "people"`
  - mapping_reason: Source of DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because"`, `55: "of"`, `56: "you,"`
  - mapping_reason: Causal relation.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay"`, `53: "Gold"`
  - mapping_reason: Book title.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Verb meaning to read.
* target[20]: "정말 좋았어요\""
  - source_tokens: `60: "so"`, `61: "good,"`
  - mapping_reason: Assessment of the book.
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: Medium of communication.
* target[22]: "정말 많이"
  - source_tokens: `43: "so"`, `44: "many"`
  - mapping_reason: Quantity of DMs.
* target[23]: "받았는데,"
  - source_tokens: `41: "have"`, `42: "gotten"`
  - mapping_reason: Verb meaning to receive.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Demonstrative reference to the previous event.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Experiencer of happiness.
* target[26]: "정말"
  - source_tokens: `64: "honestly"`, `67: "so"`
  - mapping_reason: Intensifier.
* target[27]: "행복하게 해요."
  - source_tokens: `65: "makes"`, `68: "happy."`
  - mapping_reason: Resulting state.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7, 6]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1, 8]},
  {"target_senseunit_id": 4, "source_token_ids": [47]},
  {"target_senseunit_id": 5, "source_token_ids": [0]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 27, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [64, 67]},
  {"target_senseunit_id": 27, "source_token_ids": [65, 68]}
]

- retry: 5/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun, while '분들이' functions as the subject of a declarative statement in the target context. The mapping is semantically mismatched."
  - replace_source_tokens: 0: "Who"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`
  - mapping_reason: Represents the comparison base "than I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: Intensifier for the comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Object of the help action.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: Potential modality for the help action.
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: Subject/Agent of the helping action (relative pronoun).
* target[5]: "있어요."
  - source_tokens: `1: "can", 2: "help"`
  - mapping_reason: Existential completion of the predicate "can help".
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: Addressee/Recipient of the appreciation.
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: Expression of gratitude.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Subject of the reported clauses.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: Object of the valuing action.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb of valuing.
* target[11]: "말해주거나"
  - source_tokens: `17: "tell", 18: "me"`
  - mapping_reason: First reporting verb.
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: Causative agent.
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: Object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Verb of reading.
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when", 27: "when", 29: "tell", 30: "me"`
  - mapping_reason: Temporal condition for the appreciation.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: Source of the DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: Attribution of cause for reading.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: Title of the book read.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Verb of reading.
* target[20]: "정말 좋았어요\""
  - source_tokens: `59: "was", 60: "so", 61: "good,"`
  - mapping_reason: Positive assessment.
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: The object received.
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: Quantity of DMs.
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: Verb of receiving.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Subject of the effect.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Experiencer of the happiness.
* target[26]: "정말"
  - source_tokens: `67: "so"`
  - mapping_reason: Intensifier for happy.
* target[27]: "행복하게 해요."
  - source_tokens: `64: "honestly", 65: "makes", 68: "happy."`
  - mapping_reason: Causative emotional result.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [1, 2]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 27, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [59, 60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [67]},
  {"target_senseunit_id": 27, "source_token_ids": [64, 65, 68]}
]

---
=== EN_nN_EW5TiHKQ_W000023 ===

source:
- language: English
- transcription: Who can help you way more than I can. I really appreciate my trans followers when they tell me that they value my opinion on books, or when they tell me that they read a book because of me. Like I have gotten so many DMs from people saying, "Hey, I read Stay Gold because of you, and it was so good," and that honestly makes me so happy.
- source_tokens:
  0. Who
  1. can
  2. help
  3. you
  4. way
  5. more
  6. than
  7. I
  8. can.
  9. I
  10. really
  11. appreciate
  12. my
  13. trans
  14. followers
  15. when
  16. they
  17. tell
  18. me
  19. that
  20. they
  21. value
  22. my
  23. opinion
  24. on
  25. books,
  26. or
  27. when
  28. they
  29. tell
  30. me
  31. that
  32. they
  33. read
  34. a
  35. book
  36. because
  37. of
  38. me.
  39. Like
  40. I
  41. have
  42. gotten
  43. so
  44. many
  45. DMs
  46. from
  47. people
  48. saying,"
  49. Hey,
  50. I
  51. read
  52. Stay
  53. Gold
  54. because
  55. of
  56. you,
  57. and
  58. it
  59. was
  60. so
  61. good,"
  62. and
  63. that
  64. honestly
  65. makes
  66. me
  67. so
  68. happy.

target:
- language: Korean
- translation: 저보다 훨씬 더 도움을 줄 수 있는 분들이 있어요. 제 트랜스젠더 팔로워분들께 정말 감사해요, 그분들이 제 책에 대한 의견을 소중히 여긴다고 말해주거나 저 때문에 책을 읽었다고 말해줄 때요. 사람들에게서 "덕분에 스테이 골드를 읽었는데 정말 좋았어요" 같은 DM을 정말 많이 받았는데, 그게 저를 정말 행복하게 해요.
- target_sense_units:
  0. 저보다
  1. 훨씬 더
  2. 도움을
  3. 줄 수 있는
  4. 분들이
  5. 있어요.
  6. 제 트랜스젠더 팔로워분들께
  7. 정말 감사해요,
  8. 그분들이
  9. 제 책에 대한 의견을
  10. 소중히 여긴다고
  11. 말해주거나
  12. 저 때문에
  13. 책을
  14. 읽었다고
  15. 말해줄 때요.
  16. 사람들에게서"
  17. 덕분에
  18. 스테이 골드를
  19. 읽었는데
  20. 정말 좋았어요"
  21. 같은 DM을
  22. 정말 많이
  23. 받았는데,
  24. 그게
  25. 저를
  26. 정말
  27. 행복하게 해요.

scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`, `6: "than"`
  - mapping_reason: "저(I) + 보다(than)"
* target[1]: "훨씬 더"
  - source_tokens: `4: "way"`, `5: "more"`
  - mapping_reason: "훨씬(way) 더(more)"
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: "도움(help)"
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: "수 있는(can)"
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: "Who (interrogative used as relative pronoun/subject)"
* target[5]: "있어요."
  - source_tokens: `1: "can"`, `2: "help"`
  - mapping_reason: "existential potential sense derived from 'can help'"
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my"`, `13: "trans"`, `14: "followers"`
  - mapping_reason: "my(제) trans(트랜스젠더) followers(팔로워분들께)"
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really"`, `11: "appreciate"`
  - mapping_reason: "really(정말) appreciate(감사해요)"
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: "they(그분들이)"
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my"`, `23: "opinion"`, `24: "on"`, `25: "books,"`
  - mapping_reason: "my(제) opinion(의견) on(대한) books(책)"
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: "value(소중히 여기다)"
* target[11]: "말해주거나"
  - source_tokens: `17: "tell"`, `18: "me"`, `26: "or"`
  - mapping_reason: "tell me(말해주다) + or(거나)"
* target[12]: "저 때문에"
  - source_tokens: `38: "me"`, `36: "because"`, `37: "of"`
  - mapping_reason: "because of me(저 때문에)"
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: "book(책)"
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: "read(읽다)"
* target[15]: "말해줄 때요."
  - source_tokens: `29: "tell"`, `30: "me"`, `15: "when"`
  - mapping_reason: "when(때) they tell me(말해주다)"
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from"`, `47: "people"`
  - mapping_reason: "from people(사람들에게서)"
* target[17]: "덕분에"
  - source_tokens: `54: "because"`, `55: "of"`, `56: "you,"`
  - mapping_reason: "because of you(덕분에)"
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay"`, `53: "Gold"`
  - mapping_reason: "Stay Gold(스테이 골드)"
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: "read(읽다)"
* target[20]: "정말 좋았어요\""
  - source_tokens: `60: "so"`, `61: "good,"`
  - mapping_reason: "so good(정말 좋았어요)"
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: "DM(DM)"
* target[22]: "정말 많이"
  - source_tokens: `43: "so"`, `44: "many"`
  - mapping_reason: "so many(정말 많이)"
* target[23]: "받았는데,"
  - source_tokens: `42: "gotten"`
  - mapping_reason: "gotten(받다)"
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: "that(그게)"
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: "me(저를)"
* target[26]: "정말"
  - source_tokens: `64: "honestly"`, `67: "so"`
  - mapping_reason: "honestly/so(정말)"
* target[27]: "행복하게 해요."
  - source_tokens: `65: "makes"`, `68: "happy."`
  - mapping_reason: "makes happy(행복하게 하다)"

result:
```html
0. <src>Who can help </src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>you way more than I can. </src> <tgt>저보다 훨씬 더 도움을 줄 수 있는 분들이 있어요.</tgt>; start=2.00, end=3.00
3. <src>I really appreciate </src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>my trans followers </src> <tgt>제 트랜스젠더 팔로워분들께 정말 감사해요,</tgt>; start=4.00, end=5.00
5. <src>when they tell me that </src> <tgt>그분들이</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>they value my opinion on books, </src> <tgt>제 책에 대한 의견을 소중히 여긴다고</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>or when they tell me </src> <tgt>말해주거나</tgt>; start=9.00, end=10.00
10. <src>that they read a book </src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>because of me. </src> <tgt>저 때문에 책을 읽었다고 말해줄 때요.</tgt>; start=11.00, end=12.00
12. <src>Like I have </src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>gotten so many DMs </src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>from people saying," </src> <tgt>사람들에게서"</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>Hey, I read Stay Gold because of you, and it </src> <tgt>덕분에 스테이 골드를 읽었는데</tgt>; start=16.00, end=17.00
17. <src>was so good," </src> <tgt>정말 좋았어요" 같은 DM을 정말 많이 받았는데,</tgt>; start=17.00, end=18.00
18. <src>and that honestly makes </src> <tgt>그게</tgt>; start=18.00, end=19.00
19. <src>me so happy. </src> <tgt>저를 정말 행복하게 해요.</tgt>; start=19.00, end=19.81
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun, whereas '분들이' is a noun phrase (honorific 'people') that functions as the subject of the existential sentence. The correct source tokens for this sense unit include the subject and the predicate components of the first sentence."
  - replace_source_tokens: 0: "Who", 1: "can", 2: "help", 3: "you"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I", 6: "than"`
  - mapping_reason: Represents the comparative base "than I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: Intensifier for the comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Core object of help.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: Modal ability.
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: Subject/referent of the relative clause.
* target[5]: "있어요."
  - source_tokens: `3: "you"`
  - mapping_reason: Existential assertion of the referents.
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: Addressees of gratitude.
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: Expression of appreciation.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Subject of the subordinate clause.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books,"`
  - mapping_reason: Content of the opinion.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb of valuation.
* target[11]: "말해주거나"
  - source_tokens: `15: "when", 17: "tell", 18: "me", 19: "that", 26: "or"`
  - mapping_reason: Communicative action and conjunction.
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me."`
  - mapping_reason: Causative agent.
* target[13]: "책을"
  - source_tokens: `34: "a", 35: "book"`
  - mapping_reason: Direct object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Action of reading.
* target[15]: "말해줄 때요."
  - source_tokens: `27: "when", 28: "they", 29: "tell", 30: "me", 31: "that"`
  - mapping_reason: Temporal condition and communicative action.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: Source of the DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you,"`
  - mapping_reason: Attribution of credit.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: Specific book title.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Action of reading.
* target[20]: "정말 좋았어요\""
  - source_tokens: `60: "so", 61: "good,"`
  - mapping_reason: Evaluative description.
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs", 48: "saying,\""`
  - mapping_reason: Object of receipt.
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: Quantifier.
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: Action of receiving.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Anaphoric reference to the situation.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Experiencer.
* target[26]: "정말"
  - source_tokens: `64: "honestly", 67: "so"`
  - mapping_reason: Intensifier.
* target[27]: "행복하게 해요."
  - source_tokens: `65: "makes", 68: "happy."`
  - mapping_reason: Causative emotional state.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [7, 6]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [3]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [15, 17, 18, 19, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [34, 35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [27, 28, 29, 30, 31]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47, 48]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [64, 67]},
  {"target_senseunit_id": 27, "source_token_ids": [65, 68]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The target unit '분들이' (people) is not a translation of 'Who'. It corresponds to the implied subject of the existential clause."
  - replace_source_tokens: 4: "way"

* target[5]
  - verdict: mapping_error
  - reason: "The mapping for '있어요' (there are) using 'Who can help' is structurally mismatched as the target is a declarative statement and the source is an interrogative."
  - replace_source_tokens: 0: "Who", 1: "can", 2: "help"

* target[21]
  - verdict: mapping_error
  - reason: "The source tokens 'so' and 'many' are quantifier modifiers that belong to the following target unit, not to the noun phrase 'DM'."
  - replace_source_tokens: 45: "DMs"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `7: "I"`, `6: "than"`
  - mapping_reason: Represents the comparative base "than I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way"`, `5: "more"`
  - mapping_reason: Intensifier for the comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Object of the helping action.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: Modal verb expressing ability/possibility.
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: The subject of the existential clause, mapping to the interrogative pronoun used as an indefinite pronoun here.
* target[5]: "있어요."
  - source_tokens: `0: "Who"`, `3: "you"`
  - mapping_reason: Existential predicate implied by the context of "Who can help you".
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my"`, `13: "trans"`, `14: "followers"`
  - mapping_reason: Target audience/beneficiary of appreciation.
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really"`, `11: "appreciate"`
  - mapping_reason: Expression of gratitude.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Subject of the subordinate clause.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my"`, `23: "opinion"`, `24: "on"`, `25: "books,"`
  - mapping_reason: Object of the value/opinion clause.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb expressing valuing opinion.
* target[11]: "말해주거나"
  - source_tokens: `17: "tell"`, `18: "me"`, `26: "or"`
  - mapping_reason: Reporting verb and conjunction.
* target[12]: "저 때문에"
  - source_tokens: `36: "because"`, `37: "of"`, `38: "me."`
  - mapping_reason: Causative phrase.
* target[13]: "책을"
  - source_tokens: `35: "book"`
  - mapping_reason: Object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Verb of reading.
* target[15]: "말해줄 때요."
  - source_tokens: `29: "tell"`, `30: "me"`, `15: "when"`
  - mapping_reason: Reporting verb and temporal clause marker.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from"`, `47: "people"`
  - mapping_reason: Source of the DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because"`, `55: "of"`, `56: "you,"`
  - mapping_reason: Causative phrase.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay"`, `53: "Gold"`
  - mapping_reason: Book title.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Verb of reading.
* target[20]: "정말 좋았어요\""
  - source_tokens: `59: "was"`, `60: "so"`, `61: "good,"`
  - mapping_reason: Evaluative predicate.
* target[21]: "같은 DM을"
  - source_tokens: `43: "so"`, `44: "many"`, `45: "DMs"`
  - mapping_reason: Object of reception.
* target[22]: "정말 많이"
  - source_tokens: `43: "so"`, `44: "many"`
  - mapping_reason: Quantifier.
* target[23]: "받았는데,"
  - source_tokens: `41: "have"`, `42: "gotten"`
  - mapping_reason: Verb of receiving.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Subject of the second main clause.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Object of the feeling.
* target[26]: "정말"
  - source_tokens: `67: "so"`
  - mapping_reason: Intensifier.
* target[27]: "행복하게 해요."
  - source_tokens: `64: "honestly"`, `65: "makes"`, `68: "happy."`
  - mapping_reason: Causative emotional predicate.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [6, 7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [0, 3]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [29, 30, 15]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [59, 60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [43, 44, 45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [67]},
  {"target_senseunit_id": 27, "source_token_ids": [64, 65, 68]}
]

- retry: 2/5
  status: failed_after_response
  reason: * target[4]
  - verdict: mapping_error
  - reason: "The source token 'Who' is an interrogative pronoun, while '분들이' is a noun phrase. They do not match semantically."
  - replace_source_tokens: 0: "Who"

* target[5]
  - verdict: mapping_error
  - reason: "The source token 'Who' does not represent the existential verb '있어요'."
  - replace_source_tokens: 1: "can", 2: "help"
  validation:
    scratchpad:
* target[0]: "저보다"
  - source_tokens: `6: "than", 7: "I"`
  - mapping_reason: Comparative structure "than I".
* target[1]: "훨씬 더"
  - source_tokens: `4: "way", 5: "more"`
  - mapping_reason: Intensifier for comparison.
* target[2]: "도움을"
  - source_tokens: `2: "help"`
  - mapping_reason: Core object of help.
* target[3]: "줄 수 있는"
  - source_tokens: `1: "can"`
  - mapping_reason: Modal capability.
* target[4]: "분들이"
  - source_tokens: `0: "Who"`
  - mapping_reason: Subject of the existential clause referring to "Who".
* target[5]: "있어요."
  - source_tokens: `0: "Who", 1: "can", 2: "help"`
  - mapping_reason: Existential predicate derived from the interrogative clause.
* target[6]: "제 트랜스젠더 팔로워분들께"
  - source_tokens: `12: "my", 13: "trans", 14: "followers"`
  - mapping_reason: Addressee of appreciation.
* target[7]: "정말 감사해요,"
  - source_tokens: `10: "really", 11: "appreciate"`
  - mapping_reason: Expression of gratitude.
* target[8]: "그분들이"
  - source_tokens: `16: "they"`
  - mapping_reason: Anaphoric reference to followers.
* target[9]: "제 책에 대한 의견을"
  - source_tokens: `22: "my", 23: "opinion", 24: "on", 25: "books"`
  - mapping_reason: Object of value.
* target[10]: "소중히 여긴다고"
  - source_tokens: `21: "value"`
  - mapping_reason: Verb of valuing.
* target[11]: "말해주거나"
  - source_tokens: `17: "tell", 18: "me", 26: "or"`
  - mapping_reason: First speech act verb and conjunction.
* target[12]: "저 때문에"
  - source_tokens: `36: "because", 37: "of", 38: "me"`
  - mapping_reason: Causal relation.
* target[13]: "책을"
  - source_tokens: `34: "a", 35: "book"`
  - mapping_reason: Object of reading.
* target[14]: "읽었다고"
  - source_tokens: `33: "read"`
  - mapping_reason: Verb of reading.
* target[15]: "말해줄 때요."
  - source_tokens: `15: "when", 27: "when", 29: "tell", 30: "me"`
  - mapping_reason: Temporal condition.
* target[16]: "사람들에게서\""
  - source_tokens: `46: "from", 47: "people"`
  - mapping_reason: Source of the DMs.
* target[17]: "덕분에"
  - source_tokens: `54: "because", 55: "of", 56: "you"`
  - mapping_reason: Causal attribution.
* target[18]: "스테이 골드를"
  - source_tokens: `52: "Stay", 53: "Gold"`
  - mapping_reason: Title of the book.
* target[19]: "읽었는데"
  - source_tokens: `51: "read"`
  - mapping_reason: Verb of reading in quoted speech.
* target[20]: "정말 좋았어요\""
  - source_tokens: `60: "so", 61: "good"`
  - mapping_reason: Evaluation of the book.
* target[21]: "같은 DM을"
  - source_tokens: `45: "DMs"`
  - mapping_reason: Object of receiving.
* target[22]: "정말 많이"
  - source_tokens: `43: "so", 44: "many"`
  - mapping_reason: Quantifier for DMs.
* target[23]: "받았는데,"
  - source_tokens: `41: "have", 42: "gotten"`
  - mapping_reason: Verb of receiving.
* target[24]: "그게"
  - source_tokens: `63: "that"`
  - mapping_reason: Subject referring to the previous clause.
* target[25]: "저를"
  - source_tokens: `66: "me"`
  - mapping_reason: Object of happiness.
* target[26]: "정말"
  - source_tokens: `64: "honestly", 67: "so"`
  - mapping_reason: Intensifier.
* target[27]: "행복하게 해요."
  - source_tokens: `65: "makes", 68: "happy"`
  - mapping_reason: Resultative state.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [6, 7]},
  {"target_senseunit_id": 1, "source_token_ids": [4, 5]},
  {"target_senseunit_id": 2, "source_token_ids": [2]},
  {"target_senseunit_id": 3, "source_token_ids": [1]},
  {"target_senseunit_id": 4, "source_token_ids": [0]},
  {"target_senseunit_id": 5, "source_token_ids": [0, 1, 2]},
  {"target_senseunit_id": 6, "source_token_ids": [12, 13, 14]},
  {"target_senseunit_id": 7, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 8, "source_token_ids": [16]},
  {"target_senseunit_id": 9, "source_token_ids": [22, 23, 24, 25]},
  {"target_senseunit_id": 10, "source_token_ids": [21]},
  {"target_senseunit_id": 11, "source_token_ids": [17, 18, 26]},
  {"target_senseunit_id": 12, "source_token_ids": [36, 37, 38]},
  {"target_senseunit_id": 13, "source_token_ids": [34, 35]},
  {"target_senseunit_id": 14, "source_token_ids": [33]},
  {"target_senseunit_id": 15, "source_token_ids": [15, 27, 29, 30]},
  {"target_senseunit_id": 16, "source_token_ids": [46, 47]},
  {"target_senseunit_id": 17, "source_token_ids": [54, 55, 56]},
  {"target_senseunit_id": 18, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 19, "source_token_ids": [51]},
  {"target_senseunit_id": 20, "source_token_ids": [60, 61]},
  {"target_senseunit_id": 21, "source_token_ids": [45]},
  {"target_senseunit_id": 22, "source_token_ids": [43, 44]},
  {"target_senseunit_id": 23, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 24, "source_token_ids": [63]},
  {"target_senseunit_id": 25, "source_token_ids": [66]},
  {"target_senseunit_id": 26, "source_token_ids": [64, 67]},
  {"target_senseunit_id": 27, "source_token_ids": [65, 68]}
]

- retry: 3/5
  status: succeeded
  reason: retry attempt succeeded

---
