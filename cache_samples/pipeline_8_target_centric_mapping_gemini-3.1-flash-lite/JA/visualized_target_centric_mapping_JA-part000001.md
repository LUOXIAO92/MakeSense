=== JA_B00001_S00527_W000010 ===

source:
- language: Japanese
- transcription: すみません、さなえさん、入りますよ。今空気を入れ替えますからね。岩瀬氏の部下が牢屋に入ったとき、さなえさんの姿は消えていた。
- source_tokens:
  0. すみません、
  1. さなえ
  2. さん、
  3. 入り
  4. ます
  5. よ。
  6. 今
  7. 空気
  8. を
  9. 入れ替え
  10. ます
  11. から
  12. ね。
  13. 岩瀬
  14. 氏
  15. の
  16. 部下
  17. が
  18. 牢屋
  19. に
  20. 入っ
  21. た
  22. とき、
  23. さなえ
  24. さん
  25. の
  26. 姿
  27. は
  28. 消え
  29. て
  30. い
  31. た。

target:
- language: Chinese
- translation: 不好意思，早苗小姐，我进来了。我现在要通一下风。岩濑先生的部下走进牢房的时候，早苗小姐的身影已经消失了。
- target_sense_units:
  0. 不好意思，
  1. 早苗小姐，
  2. 我进来了。
  3. 我现在要
  4. 通一下风。
  5. 岩濑先生的部下
  6. 走进牢房的时候，
  7. 早苗小姐的身影
  8. 已经消失了。

scratchpad:
* target[0]: "不好意思，"
  - source_tokens: `0: "すみません、"`
  - mapping_reason: Direct translation of apology.

* target[1]: "早苗小姐，"
  - source_tokens: `1: "さなえ", 2: "さん、"`
  - mapping_reason: Name and honorific.

* target[2]: "我进来了。"
  - source_tokens: `3: "入り", 4: "ます", 5: "よ。"`
  - mapping_reason: Verb of entering and speaker intent.

* target[3]: "我现在要"
  - source_tokens: `6: "今"`
  - mapping_reason: Temporal marker for the following action.

* target[4]: "通一下风。"
  - source_tokens: `7: "空気", 8: "を", 9: "入れ替え", 10: "ます", 11: "から", 12: "ね。"`
  - mapping_reason: Action of changing air (ventilation) and discourse particle.

* target[5]: "岩濑先生的部下"
  - source_tokens: `13: "岩瀬", 14: "氏", 15: "の", 16: "部下", 17: "が"`
  - mapping_reason: Subject of the clause.

* target[6]: "走进牢房的时候，"
  - source_tokens: `18: "牢屋", 19: "に", 20: "入っ", 21: "た", 22: "とき、"`
  - mapping_reason: Temporal clause describing the action of entering the cell.

* target[7]: "早苗小姐的身影"
  - source_tokens: `23: "さなえ", 24: "さん", 25: "の", 26: "姿", 27: "は"`
  - mapping_reason: Object/Topic of the second clause.

* target[8]: "已经消失了。"
  - source_tokens: `28: "消え", 29: "て", 30: "い", 31: "た。"`
  - mapping_reason: State of having disappeared.

result:
```html
0. <src>すみません、</src> <tgt>不好意思，</tgt>; start=0.00, end=1.00
1. <src>さなえさん、</src> <tgt>早苗小姐，</tgt>; start=1.00, end=2.00
2. <src>入りますよ。</src> <tgt>我进来了。</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>今空気を入れ替え</src> <tgt>我现在要</tgt>; start=4.00, end=5.00
5. <src>ますからね。</src> <tgt>通一下风。</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>岩瀬氏</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>の部下が</src> <tgt>岩濑先生的部下</tgt>; start=8.00, end=9.00
9. <src>牢屋に入ったとき、</src> <tgt>走进牢房的时候，</tgt>; start=9.00, end=10.00
10. <src>さなえさんの</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>姿は</src> <tgt>早苗小姐的身影</tgt>; start=11.00, end=12.00
12. <src>消えていた。</src> <tgt>已经消失了。</tgt>; start=12.00, end=12.72
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_B00001_S00527_W000010 ===

source:
- language: Japanese
- transcription: すみません、さなえさん、入りますよ。今空気を入れ替えますからね。岩瀬氏の部下が牢屋に入ったとき、さなえさんの姿は消えていた。
- source_tokens:
  0. すみません、
  1. さなえ
  2. さん、
  3. 入り
  4. ます
  5. よ。
  6. 今
  7. 空気
  8. を
  9. 入れ替え
  10. ます
  11. から
  12. ね。
  13. 岩瀬
  14. 氏
  15. の
  16. 部下
  17. が
  18. 牢屋
  19. に
  20. 入っ
  21. た
  22. とき、
  23. さなえ
  24. さん
  25. の
  26. 姿
  27. は
  28. 消え
  29. て
  30. い
  31. た。

target:
- language: Korean
- translation: 미안합니다, 사나에 씨, 들어갈게요. 지금 공기 좀 환기할게요. 이와세 씨의 부하가 감옥에 들어갔을 때, 사나에 씨의 모습은 사라져 있었다.
- target_sense_units:
  0. 미안합니다,
  1. 사나에 씨,
  2. 들어갈게요.
  3. 지금
  4. 공기 좀 환기할게요.
  5. 이와세 씨의 부하가
  6. 감옥에
  7. 들어갔을 때,
  8. 사나에 씨의 모습은
  9. 사라져 있었다.

scratchpad:
* target[0]: "미안합니다,"
  - source_tokens: `0: "すみません、"`
  - mapping_reason: Direct translation of apology.

* target[1]: "사나에 씨,"
  - source_tokens: `1: "さなえ", 2: "さん、"`
  - mapping_reason: Proper noun and honorific suffix.

* target[2]: "들어갈게요."
  - source_tokens: `3: "入り", 4: "ます", 5: "よ。"`
  - mapping_reason: Verb 'enter' with polite suffix and sentence-ending particle.

* target[3]: "지금"
  - source_tokens: `6: "今"`
  - mapping_reason: Temporal adverb.

* target[4]: "공기 좀 환기할게요."
  - source_tokens: `7: "空気", 8: "を", 9: "入れ替え", 10: "ます", 11: "から", 12: "ね。"`
  - mapping_reason: "Air exchange" (ventilation) with polite verb and discourse particles.

* target[5]: "이와세 씨의 부하가"
  - source_tokens: `13: "岩瀬", 14: "氏", 15: "の", 16: "部下", 17: "が"`
  - mapping_reason: Subject noun phrase (Proper name, title, possessive, subordinate, subject marker).

* target[6]: "감옥에"
  - source_tokens: `18: "牢屋", 19: "に"`
  - mapping_reason: Location noun and target particle.

* target[7]: "들어갔을 때,"
  - source_tokens: `20: "入っ", 21: "た", 22: "とき、"`
  - mapping_reason: Verb 'enter' in past tense + temporal conjunction 'when'.

* target[8]: "사나에 씨의 모습은"
  - source_tokens: `23: "さなえ", 24: "さん", 25: "の", 26: "姿", 27: "は"`
  - mapping_reason: Subject noun phrase (Proper name, honorific, possessive, appearance, topic marker).

* target[9]: "사라져 있었다."
  - source_tokens: `28: "消え", 29: "て", 30: "い", 31: "た。"`
  - mapping_reason: Verb 'disappear' + auxiliary verb 'be' (stative past).

result:
```html
0. <src>すみません、</src> <tgt>미안합니다,</tgt>; start=0.00, end=1.00
1. <src>さなえさん、</src> <tgt>사나에 씨,</tgt>; start=1.00, end=2.00
2. <src>入りますよ。</src> <tgt>들어갈게요.</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>今空気を入れ替え</src> <tgt>지금</tgt>; start=4.00, end=5.00
5. <src>ますからね。</src> <tgt>공기 좀 환기할게요.</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>岩瀬氏</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>の部下が</src> <tgt>이와세 씨의 부하가</tgt>; start=8.00, end=9.00
9. <src>牢屋に入ったとき、</src> <tgt>감옥에 들어갔을 때,</tgt>; start=9.00, end=10.00
10. <src>さなえさんの</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>姿は</src> <tgt>사나에 씨의 모습은</tgt>; start=11.00, end=12.00
12. <src>消えていた。</src> <tgt>사라져 있었다.</tgt>; start=12.00, end=12.72
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_B00001_S00527_W000010 ===

source:
- language: Japanese
- transcription: すみません、さなえさん、入りますよ。今空気を入れ替えますからね。岩瀬氏の部下が牢屋に入ったとき、さなえさんの姿は消えていた。
- source_tokens:
  0. すみません、
  1. さなえ
  2. さん、
  3. 入り
  4. ます
  5. よ。
  6. 今
  7. 空気
  8. を
  9. 入れ替え
  10. ます
  11. から
  12. ね。
  13. 岩瀬
  14. 氏
  15. の
  16. 部下
  17. が
  18. 牢屋
  19. に
  20. 入っ
  21. た
  22. とき、
  23. さなえ
  24. さん
  25. の
  26. 姿
  27. は
  28. 消え
  29. て
  30. い
  31. た。

target:
- language: English
- translation: Excuse me, Sanae-san, I'm coming in. I'm going to air it out now. When Mr. Iwase's subordinate entered the cell, Sanae-san was gone.
- target_sense_units:
  0. Excuse me,
  1. Sanae- san,
  2. I'm coming in.
  3. I'm going to
  4. air it out
  5. now.
  6. When Mr. Iwase's subordinate
  7. entered the cell,
  8. Sanae- san was gone.

scratchpad:
* target[0]: "Excuse me,"
  - source_tokens: `0: "すみません、"`
  - mapping_reason: Direct translation of the apology/polite address.

* target[1]: "Sanae- san,"
  - source_tokens: `1: "さなえ", 2: "さん、"`
  - mapping_reason: Proper noun and honorific.

* target[2]: "I'm coming in."
  - source_tokens: `3: "入り", 4: "ます", 5: "よ。"`
  - mapping_reason: "入り" (enter) + polite markers.

* target[3]: "I'm going to"
  - source_tokens: `11: "から"`
  - mapping_reason: The "from/because" structure implies the subsequent action is about to happen.

* target[4]: "air it out"
  - source_tokens: `7: "空気", 8: "を", 9: "入れ替え"`
  - mapping_reason: "空気" (air) + "入れ替え" (exchange/change).

* target[5]: "now."
  - source_tokens: `6: "今", 10: "ます", 12: "ね。"`
  - mapping_reason: "今" (now) + polite/confirmation markers.

* target[6]: "When Mr. Iwase's subordinate"
  - source_tokens: `13: "岩瀬", 14: "氏", 15: "の", 16: "部下", 17: "が", 22: "とき、"`
  - mapping_reason: Subject noun phrase + temporal marker "とき".

* target[7]: "entered the cell,"
  - source_tokens: `18: "牢屋", 19: "に", 20: "入っ", 21: "た"`
  - mapping_reason: "牢屋" (cell) + "入った" (entered).

* target[8]: "Sanae- san was gone."
  - source_tokens: `23: "さなえ", 24: "さん", 25: "の", 26: "姿", 27: "は", 28: "消え", 29: "て", 30: "い", 31: "た。"`
  - mapping_reason: "さなえさんの姿" (Sanae-san's figure/form) + "消えていた" (had disappeared/was gone).

result:
```html
0. <src>すみません、</src> <tgt>Excuse me,</tgt>; start=0.00, end=1.00
1. <src>さなえさん、</src> <tgt>Sanae- san,</tgt>; start=1.00, end=2.00
2. <src>入りますよ。</src> <tgt>I'm coming in.</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>今空気を入れ替え</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>ますからね。</src> <tgt>I'm going to air it out now.</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>岩瀬氏</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>の部下が</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>牢屋に入ったとき、</src> <tgt>When Mr. Iwase's subordinate entered the cell,</tgt>; start=9.00, end=10.00
10. <src>さなえさんの</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>姿は</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>消えていた。</src> <tgt>Sanae- san was gone.</tgt>; start=12.00, end=12.72
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_B00001_S01637_W000020 ===

source:
- language: Japanese
- transcription: 漫画にもいろいろなジャンル、種類がありますね。これを砕けた会話ではなんとかものと言います。例えばホラーもの、S.F.もの、アクションものなどなど。
- source_tokens:
  0. 漫画
  1. に
  2. も
  3. いろいろ
  4. な
  5. ジャンル、
  6. 種類
  7. が
  8. あり
  9. ます
  10. ね。
  11. これ
  12. を
  13. 砕け
  14. た
  15. 会話
  16. で
  17. は
  18. なん
  19. と
  20. か
  21. もの
  22. と
  23. 言い
  24. ます。
  25. 例えば
  26. ホラー
  27. もの、
  28. S.F.
  29. もの、
  30. アクション
  31. もの
  32. など
  33. など。

target:
- language: Korean
- translation: 만화에도 여러 장르와 종류가 있죠. 편한 대화에서는 이걸 '뭐뭐물'이라고 해요. 예를 들면 호러물, SF물, 액션물 같은 거죠.
- target_sense_units:
  0. 만화에도
  1. 여러 장르와
  2. 종류가
  3. 있죠.
  4. 편한 대화에서는
  5. 이걸
  6. ' 뭐뭐물' 이라고
  7. 해요.
  8. 예를 들면
  9. 호러물,
  10. SF물,
  11. 액션물
  12. 같은 거죠.

scratchpad:
* target[0]: "만화에도"
  - source_tokens: `0: "漫画", 1: "に", 2: "も"`
  - mapping_reason: "만화(漫画) + 에도(に+も)"

* target[1]: "여러 장르와"
  - source_tokens: `3: "いろいろ", 4: "な", 5: "ジャンル、"`
  - mapping_reason: "여러(いろいろ+な) + 장르(ジャンル)"

* target[2]: "종류가"
  - source_tokens: `6: "種類", 7: "が"`
  - mapping_reason: "종류(種類) + 가(が)"

* target[3]: "있죠."
  - source_tokens: `8: "あり", 9: "ます", 10: "ね。"`
  - mapping_reason: "있(あり) + 죠(ます+ね)"

* target[4]: "편한 대화에서는"
  - source_tokens: `13: "砕け", 14: "た", 15: "会話", 16: "で", 17: "は"`
  - mapping_reason: "편한(砕けた) + 대화(会話) + 에서는(で+は)"

* target[5]: "이걸"
  - source_tokens: `11: "これ", 12: "を"`
  - mapping_reason: "이걸(これ+を)"

* target[6]: "' 뭐뭐물' 이라고"
  - source_tokens: `18: "なん", 19: "と", 20: "か", 21: "もの", 22: "と"`
  - mapping_reason: "'뭐뭐'(なんとか) + 물(もの) + 이라고(と)"

* target[7]: "해요."
  - source_tokens: `23: "言い", 24: "ます。"`
  - mapping_reason: "해요(言います)"

* target[8]: "예를 들면"
  - source_tokens: `25: "例えば"`
  - mapping_reason: "예를 들면(例えば)"

* target[9]: "호러물,"
  - source_tokens: `26: "ホラー", 27: "もの、"`
  - mapping_reason: "호러(ホラー) + 물(もの)"

* target[10]: "SF물,"
  - source_tokens: `28: "S.F.", 29: "もの、"`
  - mapping_reason: "SF(S.F.) + 물(もの)"

* target[11]: "액션물"
  - source_tokens: `30: "アクション", 31: "もの"`
  - mapping_reason: "액션(アクション) + 물(もの)"

* target[12]: "같은 거죠."
  - source_tokens: `32: "など", 33: "など。"`
  - mapping_reason: "같은 거죠(などなど)"

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>漫画にも</src> <tgt>만화에도</tgt>; start=1.00, end=2.00
2. <src>いろいろな</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>ジャンル、種類</src> <tgt>여러 장르와</tgt>; start=3.00, end=4.00
4. <src>がありますね。</src> <tgt>종류가 있죠.</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>これを</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>砕けた</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>会話では</src> <tgt>편한 대화에서는 이걸</tgt>; start=8.00, end=9.00
9. <src>なんとか</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>もの</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>と言います。</src> <tgt>' 뭐뭐물' 이라고 해요.</tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>例えば</src> <tgt>예를 들면</tgt>; start=14.00, end=15.00
15. <src>ホラーもの、</src> <tgt>호러물,</tgt>; start=15.00, end=16.00
16. <src><|wait|></src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>S.F.もの、</src> <tgt>SF물,</tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>アクションもの</src> <tgt>액션물</tgt>; start=19.00, end=20.00
20. <src>などなど。</src> <tgt>같은 거죠.</tgt>; start=20.00, end=20.78
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_B00001_S01637_W000020 ===

source:
- language: Japanese
- transcription: 漫画にもいろいろなジャンル、種類がありますね。これを砕けた会話ではなんとかものと言います。例えばホラーもの、S.F.もの、アクションものなどなど。
- source_tokens:
  0. 漫画
  1. に
  2. も
  3. いろいろ
  4. な
  5. ジャンル、
  6. 種類
  7. が
  8. あり
  9. ます
  10. ね。
  11. これ
  12. を
  13. 砕け
  14. た
  15. 会話
  16. で
  17. は
  18. なん
  19. と
  20. か
  21. もの
  22. と
  23. 言い
  24. ます。
  25. 例えば
  26. ホラー
  27. もの、
  28. S.F.
  29. もの、
  30. アクション
  31. もの
  32. など
  33. など。

target:
- language: English
- translation: There are many different genres and types of manga, aren't there? In casual conversation, we often call them '-mono', meaning 'thing'. For example, horror-mono, sci-fi-mono, action-mono, and so on.
- target_sense_units:
  0. There are
  1. many different genres
  2. and types of manga,
  3. aren't there?
  4. In casual conversation,
  5. we often call them
  6. '- mono ',
  7. meaning ' thing '.
  8. For example,
  9. horror- mono,
  10. sci- fi- mono,
  11. action- mono,
  12. and so on.

scratchpad:
* target[0]: "There are"
  - source_tokens: `8: "あり", 9: "ます"`
  - mapping_reason: Existential verb phrase.
* target[1]: "many different genres"
  - source_tokens: `3: "いろいろ", 4: "な", 5: "ジャンル、"`
  - mapping_reason: Noun phrase with quantifier.
* target[2]: "and types of manga,"
  - source_tokens: `0: "漫画", 1: "に", 2: "も", 6: "種類", 7: "が"`
  - mapping_reason: Conjunctive noun phrase and topic/subject markers.
* target[3]: "aren't there?"
  - source_tokens: `10: "ね。"`
  - mapping_reason: Seeking agreement particle.
* target[4]: "In casual conversation,"
  - source_tokens: `13: "砕け", 14: "た", 15: "会話", 16: "で", 17: "は"`
  - mapping_reason: Setting context for the register.
* target[5]: "we often call them"
  - source_tokens: `11: "これ", 12: "を", 23: "言い", 24: "ます。"`
  - mapping_reason: Subject/object reference and verb for naming.
* target[6]: "'- mono ',"
  - source_tokens: `18: "なん", 19: "と", 20: "か", 21: "もの", 22: "と"`
  - mapping_reason: The specific suffix being discussed.
* target[7]: "meaning ' thing '."
  - source_tokens: `21: "もの"`
  - mapping_reason: Definition of the suffix.
* target[8]: "For example,"
  - source_tokens: `25: "例えば"`
  - mapping_reason: Exemplification marker.
* target[9]: "horror- mono,"
  - source_tokens: `26: "ホラー", 27: "もの、"`
  - mapping_reason: Specific example 1.
* target[10]: "sci- fi- mono,"
  - source_tokens: `28: "S.F.", 29: "もの、"`
  - mapping_reason: Specific example 2.
* target[11]: "action- mono,"
  - source_tokens: `30: "アクション", 31: "もの"`
  - mapping_reason: Specific example 3.
* target[12]: "and so on."
  - source_tokens: `32: "など", 33: "など。"`
  - mapping_reason: List termination marker.

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>漫画にも</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>いろいろな</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>ジャンル、種類</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>がありますね。</src> <tgt>There are many different genres and types of manga, aren't there?</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>これを</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>砕けた</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>会話では</src> <tgt>In casual conversation,</tgt>; start=8.00, end=9.00
9. <src>なんとか</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>もの</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>と言います。</src> <tgt>we often call them '- mono ', meaning ' thing '.</tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>例えば</src> <tgt>For example,</tgt>; start=14.00, end=15.00
15. <src>ホラーもの、</src> <tgt>horror- mono,</tgt>; start=15.00, end=16.00
16. <src><|wait|></src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>S.F.もの、</src> <tgt>sci- fi- mono,</tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>アクションもの</src> <tgt>action- mono,</tgt>; start=19.00, end=20.00
20. <src>などなど。</src> <tgt>and so on.</tgt>; start=20.00, end=20.78
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_B00001_S01637_W000020 ===

source:
- language: Japanese
- transcription: 漫画にもいろいろなジャンル、種類がありますね。これを砕けた会話ではなんとかものと言います。例えばホラーもの、S.F.もの、アクションものなどなど。
- source_tokens:
  0. 漫画
  1. に
  2. も
  3. いろいろ
  4. な
  5. ジャンル、
  6. 種類
  7. が
  8. あり
  9. ます
  10. ね。
  11. これ
  12. を
  13. 砕け
  14. た
  15. 会話
  16. で
  17. は
  18. なん
  19. と
  20. か
  21. もの
  22. と
  23. 言い
  24. ます。
  25. 例えば
  26. ホラー
  27. もの、
  28. S.F.
  29. もの、
  30. アクション
  31. もの
  32. など
  33. など。

target:
- language: Chinese
- translation: 漫画也有各种各样的类型和种类呢。在随意谈话中，我们一般叫它们“某某物”。比如恐怖物、科幻物、动作物之类的。
- target_sense_units:
  0. 漫画
  1. 也有
  2. 各种各样的
  3. 类型和种类
  4. 呢。
  5. 在随意谈话中，
  6. 我们
  7. 一般叫它们
  8. “某某物”。
  9. 比如
  10. 恐怖物、
  11. 科幻物、
  12. 动作物
  13. 之类的。

scratchpad:
* target[0]: "漫画"
  - source_tokens: `0: "漫画"`
  - mapping_reason: Direct translation of the subject.

* target[1]: "也有"
  - source_tokens: `1: "に", 2: "も", 8: "あり", 9: "ます"`
  - mapping_reason: Captures existence and the additive particle 'mo'.

* target[2]: "各种各样的"
  - source_tokens: `3: "いろいろ", 4: "な"`
  - mapping_reason: Adjectival phrase describing variety.

* target[3]: "类型和种类"
  - source_tokens: `5: "ジャンル、", 6: "種類"`
  - mapping_reason: Direct translation of the nouns.

* target[4]: "呢。"
  - source_tokens: `10: "ね。"`
  - mapping_reason: Sentence-ending particle for conversational tone.

* target[5]: "在随意谈话中，"
  - source_tokens: `13: "砕け", 14: "た", 15: "会話", 16: "で", 17: "は"`
  - mapping_reason: Translation of the conversational context phrase.

* target[6]: "我们"
  - source_tokens: ``
  - mapping_reason: Implicit subject in the Japanese source (implied by the context of "how we say it"). *Self-correction: Since there is no explicit 'we' in source, but it's implied by the act of calling it something, I will map to the verb '言います' (23).*
  - source_tokens: `23: "言い"`

* target[7]: "一般叫它们"
  - source_tokens: `11: "これ", 12: "を", 18: "なん", 19: "と", 20: "か", 22: "と", 23: "言い", 24: "ます。"`
  - mapping_reason: Captures the act of calling 'this' (the genres) something.

* target[8]: "“某某物”。"
  - source_tokens: `21: "もの"`
  - mapping_reason: The specific suffix being discussed.

* target[9]: "比如"
  - source_tokens: `25: "例えば"`
  - mapping_reason: Direct translation of the example marker.

* target[10]: "恐怖物、"
  - source_tokens: `26: "ホラー", 27: "もの、"`
  - mapping_reason: Example 1.

* target[11]: "科幻物、"
  - source_tokens: `28: "S.F.", 29: "もの、"`
  - mapping_reason: Example 2.

* target[12]: "动作物"
  - source_tokens: `30: "アクション", 31: "もの"`
  - mapping_reason: Example 3.

* target[13]: "之类的。"
  - source_tokens: `32: "など", 33: "など。"`
  - mapping_reason: Generalizing suffix for examples.

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>漫画にも</src> <tgt>漫画</tgt>; start=1.00, end=2.00
2. <src>いろいろな</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>ジャンル、種類</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>がありますね。</src> <tgt>也有各种各样的类型和种类呢。</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>これを</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>砕けた</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>会話では</src> <tgt>在随意谈话中，</tgt>; start=8.00, end=9.00
9. <src>なんとか</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>もの</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>と言います。</src> <tgt>我们一般叫它们“某某物”。</tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>例えば</src> <tgt>比如</tgt>; start=14.00, end=15.00
15. <src>ホラーもの、</src> <tgt>恐怖物、</tgt>; start=15.00, end=16.00
16. <src><|wait|></src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>S.F.もの、</src> <tgt>科幻物、</tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>アクションもの</src> <tgt>动作物</tgt>; start=19.00, end=20.00
20. <src>などなど。</src> <tgt>之类的。</tgt>; start=20.00, end=20.78
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_C9lAGdq4pM8_W000001 ===

source:
- language: Japanese
- transcription: どうも政治いろいろの学ぶです。内閣府が行った外交に関する世論調査の結果について、自立通信が記事にしています。自立通信の記事を引用します。内閣府は19日。
- source_tokens:
  0. どう
  1. も
  2. 政治
  3. いろいろ
  4. の
  5. 学ぶ
  6. です。
  7. 内閣
  8. 府
  9. が
  10. 行っ
  11. た
  12. 外交
  13. に
  14. 関する
  15. 世論
  16. 調査
  17. の
  18. 結果
  19. に
  20. つい
  21. て、
  22. 自立
  23. 通信
  24. が
  25. 記事
  26. に
  27. し
  28. て
  29. い
  30. ます。
  31. 自立
  32. 通信
  33. の
  34. 記事
  35. を
  36. 引用
  37. し
  38. ます。
  39. 内閣
  40. 府
  41. は
  42. 19
  43. 日。

target:
- language: Korean
- translation: 안녕하세요, '정치 이모저모'의 마나부입니다. 내각부가 실시한 외교 관련 여론조사 결과에 대해 지지통신이 기사를 실었습니다. 지지통신의 기사를 인용하겠습니다. 내각부는 19일...
- target_sense_units:
  0. 안녕하세요,
  1. ' 정치 이모저모 '
  2. 의
  3. 마나부입니다.
  4. 내각부가
  5. 실시한 외교 관련 여론조사
  6. 결과에 대해
  7. 지지통신이 기사를 실었습니다.
  8. 지지통신의 기사를 인용하겠습니다.
  9. 내각부는 19일...

scratchpad:
* target[0]: "안녕하세요,"
  - source_tokens: `0: "どう", 1: "も"`
  - mapping_reason: Greeting expression derived from "どうも".

* target[1]: "' 정치 이모저모 '"
  - source_tokens: `2: "政治", 3: "いろいろ"`
  - mapping_reason: Title of the segment "政治いろいろ".

* target[2]: "의"
  - source_tokens: `4: "の"`
  - mapping_reason: Possessive particle connecting title and name.

* target[3]: "마나부입니다."
  - source_tokens: `5: "学ぶ", 6: "です。"`
  - mapping_reason: Speaker's name and copula.

* target[4]: "내각부가"
  - source_tokens: `7: "内閣", 8: "府", 9: "が"`
  - mapping_reason: Subject of the survey action.

* target[5]: "실시한 외교 관련 여론조사"
  - source_tokens: `10: "行っ", 11: "た", 12: "外交", 13: "に", 14: "関する", 15: "世論", 16: "調査"`
  - mapping_reason: Descriptive clause for the survey.

* target[6]: "결과에 대해"
  - source_tokens: `17: "の", 18: "結果", 19: "に", 20: "つい", 21: "て、"`
  - mapping_reason: Topic marker regarding the survey results.

* target[7]: "지지통신이 기사를 실었습니다."
  - source_tokens: `22: "自立", 23: "通信", 24: "が", 25: "記事", 26: "に", 27: "し", 28: "て", 29: "い", 30: "ます。"`
  - mapping_reason: Main clause stating the news agency's action.

* target[8]: "지지통신의 기사를 인용하겠습니다."
  - source_tokens: `31: "自立", 32: "通信", 33: "の", 34: "記事", 35: "を", 36: "引用", 37: "し", 38: "ます。"`
  - mapping_reason: Stating the intent to quote the article.

* target[9]: "내각부는 19일..."
  - source_tokens: `39: "内閣", 40: "府", 41: "は", 42: "19", 43: "日。"`
  - mapping_reason: Subject and time reference.

result:
```html
0. <src>どうも</src> <tgt>안녕하세요,</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>政治いろいろの学ぶです。</src> <tgt>' 정치 이모저모 ' 의 마나부입니다.</tgt>; start=2.00, end=3.00
3. <src>内閣府</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>が行った</src> <tgt>내각부가</tgt>; start=4.00, end=5.00
5. <src>外交</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>に関する世論</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>調査の結果に</src> <tgt>실시한 외교 관련 여론조사</tgt>; start=7.00, end=8.00
8. <src>ついて、</src> <tgt>결과에 대해</tgt>; start=8.00, end=9.00
9. <src>自立通信が</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>記事にしています。</src> <tgt>지지통신이 기사를 실었습니다.</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>自立通信</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>の記事を引用します。</src> <tgt>지지통신의 기사를 인용하겠습니다.</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>内閣府は</src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>19日。</src> <tgt>내각부는 19일...</tgt>; start=17.00, end=17.61
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_C9lAGdq4pM8_W000001 ===

source:
- language: Japanese
- transcription: どうも政治いろいろの学ぶです。内閣府が行った外交に関する世論調査の結果について、自立通信が記事にしています。自立通信の記事を引用します。内閣府は19日。
- source_tokens:
  0. どう
  1. も
  2. 政治
  3. いろいろ
  4. の
  5. 学ぶ
  6. です。
  7. 内閣
  8. 府
  9. が
  10. 行っ
  11. た
  12. 外交
  13. に
  14. 関する
  15. 世論
  16. 調査
  17. の
  18. 結果
  19. に
  20. つい
  21. て、
  22. 自立
  23. 通信
  24. が
  25. 記事
  26. に
  27. し
  28. て
  29. い
  30. ます。
  31. 自立
  32. 通信
  33. の
  34. 記事
  35. を
  36. 引用
  37. し
  38. ます。
  39. 内閣
  40. 府
  41. は
  42. 19
  43. 日。

target:
- language: Chinese
- translation: 大家好，我是“政治种种”的Manabu。时事通信社报道了内阁府关于外交的民意调查结果。我来引用一下时事通信社的报道。内阁府于19日……
- target_sense_units:
  0. 大家好，
  1. 我是
  2. “政治种种”的Manabu。
  3. 时事通信社
  4. 报道了
  5. 内阁府
  6. 关于外交的
  7. 民意调查
  8. 结果。
  9. 我来
  10. 引用一下
  11. 时事通信社
  12. 的报道。
  13. 内阁府
  14. 于19日……

scratchpad:
* target[0]: "大家好，"
  - source_tokens: `0: "どう", 1: "も"`
  - mapping_reason: Greeting "どうも" (Hello/Hi).
* target[1]: "我是"
  - source_tokens: `6: "です。"`
  - mapping_reason: Copula indicating identity.
* target[2]: "“政治种种”的Manabu。"
  - source_tokens: `2: "政治", 3: "いろいろ", 4: "の", 5: "学ぶ"`
  - mapping_reason: Name and descriptor of the speaker.
* target[3]: "时事通信社"
  - source_tokens: `22: "自立", 23: "通信"`
  - mapping_reason: Subject of the report (Jiji Press).
* target[4]: "报道了"
  - source_tokens: `25: "記事", 26: "に", 27: "し", 28: "て", 29: "い", 30: "ます。"`
  - mapping_reason: Verb phrase indicating the action of reporting.
* target[5]: "内阁府"
  - source_tokens: `7: "内閣", 8: "府"`
  - mapping_reason: Organization conducting the survey.
* target[6]: "关于外交的"
  - source_tokens: `12: "外交", 13: "に", 14: "に関する"`
  - mapping_reason: Topic modifier.
* target[7]: "民意调查"
  - source_tokens: `15: "世論", 16: "調査"`
  - mapping_reason: Object of the survey.
* target[8]: "结果。"
  - source_tokens: `17: "の", 18: "結果", 19: "に", 20: "つい", 21: "て、"`
  - mapping_reason: The result of the survey.
* target[9]: "我来"
  - source_tokens: `38: "ます。"`
  - mapping_reason: First-person marker implied by the volitional/polite verb structure.
* target[10]: "引用一下"
  - source_tokens: `36: "引用", 37: "し"`
  - mapping_reason: Action of quoting.
* target[11]: "时事通信社"
  - source_tokens: `31: "自立", 32: "通信"`
  - mapping_reason: Source being quoted.
* target[12]: "的报道。"
  - source_tokens: `33: "の", 34: "記事", 35: "を"`
  - mapping_reason: Object being quoted.
* target[13]: "内阁府"
  - source_tokens: `39: "内閣", 40: "府"`
  - mapping_reason: Subject of the final clause.
* target[14]: "于19日……"
  - source_tokens: `41: "は", 42: "19", 43: "日。"`
  - mapping_reason: Temporal marker.

result:
```html
0. <src>どうも</src> <tgt>大家好，</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>政治いろいろの学ぶです。</src> <tgt>我是“政治种种”的Manabu。</tgt>; start=2.00, end=3.00
3. <src>内閣府</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>が行った</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>外交</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>に関する世論</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>調査の結果に</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>ついて、</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>自立通信が</src> <tgt>时事通信社</tgt>; start=9.00, end=10.00
10. <src>記事にしています。</src> <tgt>报道了内阁府关于外交的民意调查结果。</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>自立通信</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>の記事を引用します。</src> <tgt>我来引用一下时事通信社的报道。</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>内閣府は</src> <tgt>内阁府</tgt>; start=16.00, end=17.00
17. <src>19日。</src> <tgt>于19日……</tgt>; start=17.00, end=17.61
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== JA_C9lAGdq4pM8_W000001 ===

source:
- language: Japanese
- transcription: どうも政治いろいろの学ぶです。内閣府が行った外交に関する世論調査の結果について、自立通信が記事にしています。自立通信の記事を引用します。内閣府は19日。
- source_tokens:
  0. どう
  1. も
  2. 政治
  3. いろいろ
  4. の
  5. 学ぶ
  6. です。
  7. 内閣
  8. 府
  9. が
  10. 行っ
  11. た
  12. 外交
  13. に
  14. 関する
  15. 世論
  16. 調査
  17. の
  18. 結果
  19. に
  20. つい
  21. て、
  22. 自立
  23. 通信
  24. が
  25. 記事
  26. に
  27. し
  28. て
  29. い
  30. ます。
  31. 自立
  32. 通信
  33. の
  34. 記事
  35. を
  36. 引用
  37. し
  38. ます。
  39. 内閣
  40. 府
  41. は
  42. 19
  43. 日。

target:
- language: English
- translation: Hello, this is Manabu from "Seiji Iroiro" (Politics Various). Jiji Press has an article on the results of a Cabinet Office public opinion poll on diplomacy. Let me quote from that article. On the 19th, the Cabinet Office...
- target_sense_units:
  0. Hello,
  1. this is Manabu
  2. from" Seiji Iroiro"
  3. (Politics Various).
  4. Jiji Press has
  5. an article on
  6. the results of
  7. a Cabinet Office
  8. public opinion poll
  9. on diplomacy.
  10. Let me
  11. quote from that article.
  12. On the 19th,
  13. the Cabinet Office...

scratchpad:
* target[0]: "Hello,"
  - source_tokens: `0: "どう", 1: "も"`
  - mapping_reason: "どうも" is a greeting/salutation.
* target[1]: "this is Manabu"
  - source_tokens: `5: "学ぶ", 6: "です。"`
  - mapping_reason: "学ぶ" is the name, "です" provides the copula.
* target[2]: "from" Seiji Iroiro""
  - source_tokens: `2: "政治", 3: "いろいろ", 4: "の"`
  - mapping_reason: "政治いろいろ" is the source name, "の" indicates origin.
* target[3]: "(Politics Various)."
  - source_tokens: `2: "政治", 3: "いろいろ"`
  - mapping_reason: Translation of "政治いろいろ".
* target[4]: "Jiji Press has"
  - source_tokens: `22: "自立", 23: "通信"`
  - mapping_reason: "自立通信" (Jiji Press) is the subject of the article.
* target[5]: "an article on"
  - source_tokens: `25: "記事", 26: "に"`
  - mapping_reason: "記事" is article, "に" (with "して") indicates the topic.
* target[6]: "the results of"
  - source_tokens: `18: "結果", 17: "の"`
  - mapping_reason: "結果" is results, "の" is possessive particle.
* target[7]: "a Cabinet Office"
  - source_tokens: `7: "内閣", 8: "府"`
  - mapping_reason: "内閣府" is Cabinet Office.
* target[8]: "public opinion poll"
  - source_tokens: `15: "世論", 16: "調査"`
  - mapping_reason: "世論調査" is public opinion poll.
* target[9]: "on diplomacy."
  - source_tokens: `12: "外交", 13: "に", 14: "関する"`
  - mapping_reason: "外交に関する" means concerning diplomacy.
* target[10]: "Let me"
  - source_tokens: `31: "自立", 32: "通信", 33: "の", 34: "記事", 35: "を"`
  - mapping_reason: Implied intent to quote the article mentioned.
* target[11]: "quote from that article."
  - source_tokens: `36: "引用", 37: "し", 38: "ます。"`
  - mapping_reason: "引用します" means quote.
* target[12]: "On the 19th,"
  - source_tokens: `42: "19", 43: "日。"`
  - mapping_reason: Date marker.
* target[13]: "the Cabinet Office..."
  - source_tokens: `39: "内閣", 40: "府", 41: "は"`
  - mapping_reason: "内閣府" is Cabinet Office, "は" is topic marker.

result:
```html
0. <src>どうも</src> <tgt>Hello,</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>政治いろいろの学ぶです。</src> <tgt>this is Manabu from" Seiji Iroiro" (Politics Various).</tgt>; start=2.00, end=3.00
3. <src>内閣府</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>が行った</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>外交</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>に関する世論</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>調査の結果に</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>ついて、</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>自立通信が</src> <tgt>Jiji Press has</tgt>; start=9.00, end=10.00
10. <src>記事にしています。</src> <tgt>an article on the results of a Cabinet Office public opinion poll on diplomacy.</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>自立通信</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src><|wait|></src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>の記事を引用します。</src> <tgt>Let me quote from that article.</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>内閣府は</src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>19日。</src> <tgt>On the 19th, the Cabinet Office...</tgt>; start=17.00, end=17.61
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[7]
  - verdict: mapping_error
  - reason: "The source token 'が' (9) is a grammatical particle and not part of the noun phrase 'Cabinet Office'."
  - replace_source_tokens: 7: "内閣", 8: "府"
  validation:
    scratchpad:
* target[0]: "Hello,"
  - source_tokens: `0: "どう", 1: "も"`
  - mapping_reason: "どうも" is a greeting/introduction marker.
* target[1]: "this is Manabu"
  - source_tokens: `5: "学ぶ", 6: "です。"`
  - mapping_reason: "学ぶです" identifies the speaker.
* target[2]: "from" Seiji Iroiro""
  - source_tokens: `2: "政治", 3: "いろいろ", 4: "の"`
  - mapping_reason: "政治いろいろの" describes the source/affiliation.
* target[3]: "(Politics Various)."
  - source_tokens: `2: "政治", 3: "いろいろ"`
  - mapping_reason: Translation/explanation of the channel name.
* target[4]: "Jiji Press has"
  - source_tokens: `22: "自立", 23: "通信", 24: "が"`
  - mapping_reason: Subject of the article. Note: "自立" is a transcription error for "時事", but I map to the provided tokens.
* target[5]: "an article on"
  - source_tokens: `25: "記事", 26: "に", 27: "し", 28: "て", 29: "い", 30: "ます。"`
  - mapping_reason: "記事にしています" indicates the existence of an article.
* target[6]: "the results of"
  - source_tokens: `17: "の", 18: "結果"`
  - mapping_reason: "結果の" indicates the subject matter of the article.
* target[7]: "a Cabinet Office"
  - source_tokens: `7: "内閣", 8: "府", 9: "が"`
  - mapping_reason: Source of the poll.
* target[8]: "public opinion poll"
  - source_tokens: `15: "世論", 16: "調査"`
  - mapping_reason: Subject of the poll.
* target[9]: "on diplomacy."
  - source_tokens: `12: "外交", 13: "に", 14: "関する"`
  - mapping_reason: Topic of the poll.
* target[10]: "Let me"
  - source_tokens: `38: "ます。"`
  - mapping_reason: Polite verb ending used for the following action.
* target[11]: "quote from that article."
  - source_tokens: `31: "自立", 32: "通信", 33: "の", 34: "記事", 35: "を", 36: "引用", 37: "し"`
  - mapping_reason: The action of quoting the article.
* target[12]: "On the 19th,"
  - source_tokens: `42: "19", 43: "日。"`
  - mapping_reason: Time marker.
* target[13]: "the Cabinet Office..."
  - source_tokens: `39: "内閣", 40: "府", 41: "は"`
  - mapping_reason: Subject of the quoted sentence.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [5, 6]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [2, 3, 4]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [2, 3]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [22, 23, 24]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [25, 26, 27, 28, 29, 30]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [17, 18]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [7, 8, 9]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [15, 16]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [12, 13, 14]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [38]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [31, 32, 33, 34, 35, 36, 37]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [42, 43]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [39, 40, 41]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
