=== ZH_NWf8Wc2GVvM_W000007 ===

source:
- language: Chinese
- transcription: 启示录和翡翠石板都曾经预测到，这十四万四千名光之工作者的到来，会在卡利年代结束时，将地球从黑暗势力的手中拯救出来。
- source_tokens:
  0. 启示
  1. 录
  2. 和
  3. 翡翠
  4. 石板
  5. 都
  6. 曾经
  7. 预测
  8. 到，
  9. 这
  10. 十四万
  11. 四千
  12. 名
  13. 光
  14. 之
  15. 工作
  16. 者
  17. 的
  18. 到来，
  19. 会
  20. 在
  21. 卡利
  22. 年代
  23. 结束
  24. 时，
  25. 将
  26. 地球
  27. 从
  28. 黑暗
  29. 势力
  30. 的
  31. 手中
  32. 拯救
  33. 出来。

target:
- language: Japanese
- translation: 『ヨハネの黙示録』と『エメラルド・タブレット』はどちらも、14万4000人のライトワーカーが到来して、カリ・ユガの終わりに地球を闇の勢力の手から救い出すだろうと予言していました。
- target_sense_units:
  0. 『ヨハネの黙示録』と
  1. 『エメラルド・タブレット』は
  2. どちらも、
  3. 14万4000人の
  4. ライトワーカーが
  5. 到来して、
  6. カリ・ユガの
  7. 終わりに
  8. 地球を
  9. 闇の
  10. 勢力の
  11. 手から
  12. 救い出すだろうと
  13. 予言していました。

scratchpad:
* target[0]: "『ヨハネの黙示録』と"
  - source_tokens: `0: "启示", 1: "录", 2: "和"`
  - mapping_reason: "启示录" maps to "ヨハネの黙示録" (Book of Revelation), "和" maps to "と".

* target[1]: "『エメラルド・タブレット』は"
  - source_tokens: `3: "翡翠", 4: "石板"`
  - mapping_reason: "翡翠石板" maps to "エメラルド・タブレット".

* target[2]: "どちらも、"
  - source_tokens: `5: "都"`
  - mapping_reason: "都" maps to "どちらも" (both).

* target[3]: "14万4000人の"
  - source_tokens: `10: "十四万", 11: "四千", 12: "名"`
  - mapping_reason: Numbers and classifier "名" map to "14万4000人".

* target[4]: "ライトワーカーが"
  - source_tokens: `13: "光", 14: "之", 15: "工作", 16: "者"`
  - mapping_reason: "光之工作者" maps to "ライトワーカー".

* target[5]: "到来して、"
  - source_tokens: `17: "的", 18: "到来，"`
  - mapping_reason: "到来" maps to "到来して".

* target[6]: "カリ・ユガの"
  - source_tokens: `21: "卡利", 22: "年代"`
  - mapping_reason: "卡利年代" maps to "カリ・ユガ" (Kali Yuga).

* target[7]: "終わりに"
  - source_tokens: `23: "结束", 24: "时，"`
  - mapping_reason: "结束时" maps to "終わりに".

* target[8]: "地球を"
  - source_tokens: `26: "地球"`
  - mapping_reason: "地球" maps to "地球".

* target[9]: "闇の"
  - source_tokens: `28: "黑暗"`
  - mapping_reason: "黑暗" maps to "闇".

* target[10]: "勢力の"
  - source_tokens: `29: "势力", 30: "的"`
  - mapping_reason: "势力的" maps to "勢力の".

* target[11]: "手から"
  - source_tokens: `31: "手中"`
  - mapping_reason: "手中" maps to "手から".

* target[12]: "救い出すだろうと"
  - source_tokens: `19: "会", 25: "将", 32: "拯救", 33: "出来。"`
  - mapping_reason: "会将...拯救出来" maps to "救い出すだろう".

* target[13]: "予言していました。"
  - source_tokens: `6: "曾经", 7: "预测", 8: "到，"`
  - mapping_reason: "曾经预测到" maps to "予言していました".

result:
```html
0. <src>启示录</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>和翡翠石板</src> <tgt>『ヨハネの黙示録』と『エメラルド・タブレット』は</tgt>; start=2.00, end=3.00
3. <src>都曾经预测到，</src> <tgt>どちらも、</tgt>; start=3.00, end=4.00
4. <src>这十四万四千名</src> <tgt>14万4000人の</tgt>; start=4.00, end=5.00
5. <src>光之工作者</src> <tgt>ライトワーカーが</tgt>; start=5.00, end=6.00
6. <src>的到来，</src> <tgt>到来して、</tgt>; start=6.00, end=7.00
7. <src>会在卡利年代</src> <tgt>カリ・ユガの</tgt>; start=7.00, end=8.00
8. <src>结束时，</src> <tgt>終わりに</tgt>; start=8.00, end=9.00
9. <src>将地球从</src> <tgt>地球を</tgt>; start=9.00, end=10.00
10. <src>黑暗势力的手中</src> <tgt>闇の勢力の手から</tgt>; start=10.00, end=11.00
11. <src>拯救出来。</src> <tgt>救い出すだろうと予言していました。</tgt>; start=11.00, end=11.80
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Y4xRc2amPxY_W000056 ===

source:
- language: Chinese
- transcription: 我们采用了以吃脂脂肪、肥肉和油为主的饮食结构以后呢，那给我们带来了巨大的好处。第一个好处呢，就是我们减肥了。
- source_tokens:
  0. 我们
  1. 采用
  2. 了
  3. 以
  4. 吃脂
  5. 脂肪、
  6. 肥肉
  7. 和
  8. 油
  9. 为
  10. 主
  11. 的
  12. 饮食
  13. 结构
  14. 以后
  15. 呢，
  16. 那
  17. 给
  18. 我们
  19. 带来
  20. 了
  21. 巨大
  22. 的
  23. 好处。
  24. 第一
  25. 个
  26. 好处
  27. 呢，
  28. 就是
  29. 我们
  30. 减肥
  31. 了。

target:
- language: Japanese
- translation: 脂質や脂身、油を主とした食事構造を取り入れた結果、私たちは大きなメリットを得ました。まずは、減量できたことです。
- target_sense_units:
  0. 脂質や
  1. 脂身、
  2. 油を
  3. 主とした
  4. 食事構造を
  5. 取り入れた
  6. 結果、
  7. 私たちは
  8. 大きなメリットを
  9. 得ました。
  10. まずは、
  11. 減量できた
  12. ことです。

scratchpad:
* target[0]: "脂質や"
  - source_tokens: `4: "吃脂", 5: "脂肪、"`
  - mapping_reason: Corresponds to the source terms for lipids/fats.
* target[1]: "脂身、"
  - source_tokens: `6: "肥肉"`
  - mapping_reason: Corresponds to fatty meat.
* target[2]: "油を"
  - source_tokens: `7: "和", 8: "油"`
  - mapping_reason: Corresponds to oil.
* target[3]: "主とした"
  - source_tokens: `9: "为", 10: "主"`
  - mapping_reason: Corresponds to the structure of "as the main".
* target[4]: "食事構造を"
  - source_tokens: `11: "的", 12: "饮食", 13: "结构"`
  - mapping_reason: Corresponds to dietary structure.
* target[5]: "取り入れた"
  - source_tokens: `0: "我们", 1: "采用", 2: "了"`
  - mapping_reason: Corresponds to the adoption/implementation of the diet.
* target[6]: "結果、"
  - source_tokens: `14: "以后", 15: "呢，"`
  - mapping_reason: Discourse marker for consequence/result.
* target[7]: "私たちは"
  - source_tokens: `18: "我们"`
  - mapping_reason: Subject of the benefit.
* target[8]: "大きなメリットを"
  - source_tokens: `21: "巨大", 22: "的", 23: "好处。"`
  - mapping_reason: Corresponds to huge benefits.
* target[9]: "得ました。"
  - source_tokens: `17: "给", 19: "带来", 20: "了"`
  - mapping_reason: Corresponds to the verb "brought/obtained".
* target[10]: "まずは、"
  - source_tokens: `24: "第一", 25: "个", 26: "好处", 27: "呢，"`
  - mapping_reason: Discourse marker for the first point.
* target[11]: "減量できた"
  - source_tokens: `29: "我们", 30: "减肥"`
  - mapping_reason: Corresponds to weight loss.
* target[12]: "ことです。"
  - source_tokens: `28: "就是", 31: "了。"`
  - mapping_reason: Grammatical structure for defining the first benefit.

result:
```html
0. <src>我们采用了</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>以吃脂脂肪、</src> <tgt>脂質や</tgt>; start=2.00, end=3.00
3. <src>肥肉和油</src> <tgt>脂身、油を</tgt>; start=3.00, end=4.00
4. <src>为主的饮食结构</src> <tgt>主とした食事構造を取り入れた</tgt>; start=4.00, end=5.00
5. <src>以后呢，</src> <tgt>結果、</tgt>; start=5.00, end=6.00
6. <src>那</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>给我们带来了巨大的好处。</src> <tgt>私たちは大きなメリットを得ました。</tgt>; start=7.00, end=8.00
8. <src>第一个</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>好处呢，</src> <tgt>まずは、</tgt>; start=9.00, end=10.00
10. <src>就是</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>我们减肥了。</src> <tgt>減量できたことです。</tgt>; start=11.00, end=11.36
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Y4xRc2amPxY_W000056 ===

source:
- language: Chinese
- transcription: 我们采用了以吃脂脂肪、肥肉和油为主的饮食结构以后呢，那给我们带来了巨大的好处。第一个好处呢，就是我们减肥了。
- source_tokens:
  0. 我们
  1. 采用
  2. 了
  3. 以
  4. 吃脂
  5. 脂肪、
  6. 肥肉
  7. 和
  8. 油
  9. 为
  10. 主
  11. 的
  12. 饮食
  13. 结构
  14. 以后
  15. 呢，
  16. 那
  17. 给
  18. 我们
  19. 带来
  20. 了
  21. 巨大
  22. 的
  23. 好处。
  24. 第一
  25. 个
  26. 好处
  27. 呢，
  28. 就是
  29. 我们
  30. 减肥
  31. 了。

target:
- language: English
- translation: We adopted a diet based on fats, fatty meat, and oil, and that brought us huge benefits. The first benefit is that we lost weight.
- target_sense_units:
  0. We
  1. adopted a diet
  2. based on
  3. fats, fatty meat, and oil,
  4. and that brought us
  5. huge benefits.
  6. The first benefit is
  7. that we lost weight.

scratchpad:
* target[0]: "We"
  - source_tokens: `0: "我们"`
  - mapping_reason: Subject reference.
* target[1]: "adopted a diet"
  - source_tokens: `1: "采用", 2: "了", 12: "饮食", 13: "结构"`
  - mapping_reason: Core action and object.
* target[2]: "based on"
  - source_tokens: `3: "以", 9: "为", 10: "主", 11: "的"`
  - mapping_reason: Structural relation defining the diet composition.
* target[3]: "fats, fatty meat, and oil,"
  - source_tokens: `4: "吃脂", 5: "脂肪、", 6: "肥肉", 7: "和", 8: "油"`
  - mapping_reason: Content components of the diet.
* target[4]: "and that brought us"
  - source_tokens: `14: "以后", 15: "呢，", 16: "那", 17: "给", 18: "我们", 19: "带来", 20: "了"`
  - mapping_reason: Consequence connective and causative verb phrase.
* target[5]: "huge benefits."
  - source_tokens: `21: "巨大", 22: "的", 23: "好处。"`
  - mapping_reason: Direct object of the benefit.
* target[6]: "The first benefit is"
  - source_tokens: `24: "第一", 25: "个", 26: "好处", 27: "呢，", 28: "就是"`
  - mapping_reason: Enumeration and copula.
* target[7]: "that we lost weight."
  - source_tokens: `29: "我们", 30: "减肥", 31: "了。"`
  - mapping_reason: Specific content of the benefit.

result:
```html
0. <src>我们采用了</src> <tgt>We</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>以吃脂脂肪、</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>肥肉和油</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>为主的饮食结构</src> <tgt>adopted a diet based on fats, fatty meat, and oil,</tgt>; start=4.00, end=5.00
5. <src>以后呢，</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>那</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>给我们带来了巨大的好处。</src> <tgt>and that brought us huge benefits.</tgt>; start=7.00, end=8.00
8. <src>第一个</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>好处呢，</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>就是</src> <tgt>The first benefit is</tgt>; start=10.00, end=11.00
11. <src>我们减肥了。</src> <tgt>that we lost weight.</tgt>; start=11.00, end=11.36
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_sQjhyfFvfLY_W000018 ===

source:
- language: Chinese
- transcription: 把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class，好，这个这一个那个物件的class，好。
- source_tokens:
  0. 把
  1. 它
  2. 丢进
  3. 去
  4. 之后
  5. 呢，
  6. 它
  7. 会
  8. 在
  9. 它
  10. 会
  11. 找到
  12. 这
  13. 一
  14. 个
  15. class，
  16. 把
  17. 它
  18. 转变
  19. 成
  20. 为
  21. 这
  22. 一
  23. 个
  24. class
  25. 的
  26. 的
  27. class，
  28. 好，
  29. 这
  30. 个
  31. 这
  32. 一
  33. 个
  34. 那
  35. 个
  36. 物件
  37. 的
  38. class，
  39. 好。

target:
- language: Korean
- translation: 그걸 넣고 나면, 그게, 그게 이 클래스를 찾아서, 이걸 이 클래스의 클래스로 바꿔줘요. 자, 이, 이, 그 객체의 클래스로. 자.
- target_sense_units:
  0. 그걸
  1. 넣고 나면,
  2. 그게,
  3. 그게
  4. 이 클래스를
  5. 찾아서,
  6. 이걸
  7. 이 클래스의 클래스로
  8. 바꿔줘요.
  9. 자,
  10. 이,
  11. 이,
  12. 그 객체의
  13. 클래스로.
  14. 자.

scratchpad:
* target[0]: "그걸"
  - source_tokens: `0: "把", 1: "它"`
  - mapping_reason: "把" (marker) + "它" (pronoun).

* target[1]: "넣고 나면,"
  - source_tokens: `2: "丢进", 3: "去", 4: "之后"`
  - mapping_reason: "丢进去" (put in) + "之后" (after).

* target[2]: "그게,"
  - source_tokens: `6: "它"`
  - mapping_reason: "它" (subject pronoun).

* target[3]: "그게"
  - source_tokens: `9: "它"`
  - mapping_reason: "它" (subject pronoun).

* target[4]: "이 클래스를"
  - source_tokens: `12: "这", 13: "一", 14: "个", 15: "class，"`
  - mapping_reason: "这一个" (this) + "class" (class).

* target[5]: "찾아서,"
  - source_tokens: `11: "找到"`
  - mapping_reason: "找到" (find).

* target[6]: "이걸"
  - source_tokens: `16: "把", 17: "它"`
  - mapping_reason: "把" (marker) + "它" (pronoun).

* target[7]: "이 클래스의 클래스로"
  - source_tokens: `21: "这", 22: "一", 23: "个", 24: "class", 25: "的", 26: "的", 27: "class，"`
  - mapping_reason: "这一个class" + "的" + "class".

* target[8]: "바꿔줘요."
  - source_tokens: `18: "转变", 19: "成", 20: "为"`
  - mapping_reason: "转变成为" (transform into).

* target[9]: "자,"
  - source_tokens: `28: "好，"`
  - mapping_reason: "好" (discourse marker).

* target[10]: "이,"
  - source_tokens: `29: "这", 30: "个"`
  - mapping_reason: "这一个" (this).

* target[11]: "이,"
  - source_tokens: `31: "这", 32: "一", 33: "个"`
  - mapping_reason: "这一个" (this).

* target[12]: "그 객체의"
  - source_tokens: `34: "那", 35: "个", 36: "物件", 37: "的"`
  - mapping_reason: "那个物件" (that object) + "的".

* target[13]: "클래스로."
  - source_tokens: `38: "class，"`
  - mapping_reason: "class".

* target[14]: "자."
  - source_tokens: `39: "好。"`
  - mapping_reason: "好" (discourse marker).

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>把它丢进去之后呢，它会在</src> <tgt>그걸 넣고 나면, 그게,</tgt>; start=1.00, end=2.00
2. <src>它会找到</src> <tgt>그게</tgt>; start=2.00, end=3.00
3. <src>这一个class，</src> <tgt>이 클래스를 찾아서,</tgt>; start=3.00, end=4.00
4. <src>把它转变成为</src> <tgt>이걸</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>这一个class</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>的的</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>class，</src> <tgt>이 클래스의 클래스로 바꿔줘요.</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>好，</src> <tgt>자,</tgt>; start=11.00, end=12.00
12. <src>这个</src> <tgt>이,</tgt>; start=12.00, end=13.00
13. <src>这一个</src> <tgt>이,</tgt>; start=13.00, end=14.00
14. <src>那个物件</src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>的class，</src> <tgt>그 객체의 클래스로.</tgt>; start=15.00, end=16.00
16. <src>好。</src> <tgt>자.</tgt>; start=16.00, end=16.32
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_NWf8Wc2GVvM_W000007 ===

source:
- language: Chinese
- transcription: 启示录和翡翠石板都曾经预测到，这十四万四千名光之工作者的到来，会在卡利年代结束时，将地球从黑暗势力的手中拯救出来。
- source_tokens:
  0. 启示
  1. 录
  2. 和
  3. 翡翠
  4. 石板
  5. 都
  6. 曾经
  7. 预测
  8. 到，
  9. 这
  10. 十四万
  11. 四千
  12. 名
  13. 光
  14. 之
  15. 工作
  16. 者
  17. 的
  18. 到来，
  19. 会
  20. 在
  21. 卡利
  22. 年代
  23. 结束
  24. 时，
  25. 将
  26. 地球
  27. 从
  28. 黑暗
  29. 势力
  30. 的
  31. 手中
  32. 拯救
  33. 出来。

target:
- language: Korean
- translation: 요한계시록과 에메랄드 타블렛은 모두 14만 4천 명의 빛의 일꾼들이 도래해서 칼리 유가의 끝에 지구를 어둠의 세력으로부터 구할 것이라고 예언했습니다.
- target_sense_units:
  0. 요한계시록과
  1. 에메랄드 타블렛은
  2. 모두
  3. 14만 4천 명의
  4. 빛의 일꾼들이
  5. 도래해서
  6. 칼리 유가의 끝에
  7. 지구를
  8. 어둠의 세력으로부터
  9. 구할 것이라고
  10. 예언했습니다.

scratchpad:
* target[0]: "요한계시록과"
  - source_tokens: `0: "启示", 1: "录", 2: "和"`
  - mapping_reason: "启示录" corresponds to "요한계시록", "和" corresponds to the conjunction particle "-과".

* target[1]: "에메랄드 타블렛은"
  - source_tokens: `3: "翡翠", 4: "石板"`
  - mapping_reason: "翡翠石板" corresponds to "에메랄드 타블렛".

* target[2]: "모두"
  - source_tokens: `5: "都"`
  - mapping_reason: "都" corresponds to "모두".

* target[3]: "14만 4천 명의"
  - source_tokens: `10: "十四万", 11: "四千", 12: "名"`
  - mapping_reason: Numerical values and classifier.

* target[4]: "빛의 일꾼들이"
  - source_tokens: `13: "光", 14: "之", 15: "工作", 16: "者"`
  - mapping_reason: "光之工作者" corresponds to "빛의 일꾼".

* target[5]: "도래해서"
  - source_tokens: `18: "到来"`
  - mapping_reason: "到来" corresponds to "도래".

* target[6]: "칼리 유가의 끝에"
  - source_tokens: `21: "卡利", 22: "年代", 23: "结束", 24: "时"`
  - mapping_reason: "卡利年代结束时" corresponds to "칼리 유가의 끝에".

* target[7]: "지구를"
  - source_tokens: `26: "地球"`
  - mapping_reason: "地球" corresponds to "지구".

* target[8]: "어둠의 세력으로부터"
  - source_tokens: `28: "黑暗", 29: "势力", 27: "从"`
  - mapping_reason: "从黑暗势力" corresponds to "어둠의 세력으로부터".

* target[9]: "구할 것이라고"
  - source_tokens: `32: "拯救", 33: "出来", 19: "会"`
  - mapping_reason: "会...拯救出来" corresponds to "구할 것이다".

* target[10]: "예언했습니다."
  - source_tokens: `7: "预测", 8: "到"`
  - mapping_reason: "预测到" corresponds to "예언했습니다".

result:
```html
0. <src>启示录</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>和翡翠石板</src> <tgt>요한계시록과 에메랄드 타블렛은</tgt>; start=2.00, end=3.00
3. <src>都曾经预测到，</src> <tgt>모두</tgt>; start=3.00, end=4.00
4. <src>这十四万四千名</src> <tgt>14만 4천 명의</tgt>; start=4.00, end=5.00
5. <src>光之工作者</src> <tgt>빛의 일꾼들이</tgt>; start=5.00, end=6.00
6. <src>的到来，</src> <tgt>도래해서</tgt>; start=6.00, end=7.00
7. <src>会在卡利年代</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>结束时，</src> <tgt>칼리 유가의 끝에</tgt>; start=8.00, end=9.00
9. <src>将地球从</src> <tgt>지구를</tgt>; start=9.00, end=10.00
10. <src>黑暗势力的手中</src> <tgt>어둠의 세력으로부터</tgt>; start=10.00, end=11.00
11. <src>拯救出来。</src> <tgt>구할 것이라고 예언했습니다.</tgt>; start=11.00, end=11.80
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Y4xRc2amPxY_W000024 ===

source:
- language: Chinese
- transcription: 就会消耗我们身体骨骼当中的矿物质，更多的靠物矿物质。所以呢，这个肥胖人往往都会有这种关节和软组织的问题，就是因为什么？就是消耗了太多的矿物质。
- source_tokens:
  0. 就
  1. 会
  2. 消耗
  3. 我们
  4. 身体
  5. 骨骼
  6. 当中
  7. 的
  8. 矿
  9. 物质，
  10. 更多
  11. 的
  12. 靠物
  13. 矿
  14. 物质。
  15. 所以
  16. 呢，
  17. 这
  18. 个
  19. 肥胖
  20. 人
  21. 往往
  22. 都会
  23. 有
  24. 这
  25. 种
  26. 关节
  27. 和
  28. 软
  29. 组织
  30. 的
  31. 问题，
  32. 就是
  33. 因为
  34. 什么？
  35. 就是
  36. 消耗
  37. 了
  38. 太多
  39. 的
  40. 矿
  41. 物质。

target:
- language: Korean
- translation: 우리 몸 뼈 속의 미네랄을 소모하게 되고, 미네랄에 더 의존하게 됩니다. 그래서 비만인 사람들은 관절이나 연조직 문제를 겪는 경우가 많은데, 그 이유는 뭘까요? 미네랄을 너무 많이 소모했기 때문입니다.
- target_sense_units:
  0. 우리 몸
  1. 뼈 속의
  2. 미네랄을
  3. 소모하게 되고,
  4. 미네랄에
  5. 더 의존하게 됩니다.
  6. 그래서
  7. 비만인 사람들은
  8. 관절이나
  9. 연조직 문제를
  10. 겪는 경우가
  11. 많은데,
  12. 그 이유는
  13. 뭘까요?
  14. 미네랄을
  15. 너무 많이 소모했기 때문입니다.

scratchpad:
* target[0]: "우리 몸"
  - source_tokens: `3: "我们", 4: "身体"`
  - mapping_reason: "우리" maps to "我们", "몸" maps to "身体".
* target[1]: "뼈 속의"
  - source_tokens: `5: "骨骼", 6: "当中", 7: "的"`
  - mapping_reason: "뼈" maps to "骨骼", "속의" maps to "当中" + "的".
* target[2]: "미네랄을"
  - source_tokens: `8: "矿", 9: "物质，"`
  - mapping_reason: "미네랄" (mineral) maps to "矿物质".
* target[3]: "소모하게 되고,"
  - source_tokens: `0: "就", 1: "会", 2: "消耗"`
  - mapping_reason: "소모" maps to "消耗", "하게 되고" maps to the connective "就" + "会".
* target[4]: "미네랄에"
  - source_tokens: `13: "矿", 14: "物质。"`
  - mapping_reason: "미네랄" maps to "矿物质".
* target[5]: "더 의존하게 됩니다."
  - source_tokens: `10: "更多", 11: "的", 12: "靠物"`
  - mapping_reason: "더" maps to "更多" + "的", "의존하게 됩니다" maps to "靠物".
* target[6]: "그래서"
  - source_tokens: `15: "所以", 16: "呢，"`
  - mapping_reason: "그래서" maps to "所以" + "呢".
* target[7]: "비만인 사람들은"
  - source_tokens: `17: "这", 18: "个", 19: "肥胖", 20: "人"`
  - mapping_reason: "비만인 사람" maps to "肥胖" + "人", "들은" maps to "这个".
* target[8]: "관절이나"
  - source_tokens: `26: "关节", 27: "和"`
  - mapping_reason: "관절" maps to "关节", "이나" maps to "和".
* target[9]: "연조직 문제를"
  - source_tokens: `28: "软", 29: "组织", 30: "的", 31: "问题，"`
  - mapping_reason: "연조직" maps to "软组织", "문제" maps to "问题".
* target[10]: "겪는 경우가"
  - source_tokens: `23: "有", 24: "这", 25: "种"`
  - mapping_reason: "겪는 경우" maps to the existential "有" + "这种".
* target[11]: "많은데,"
  - source_tokens: `21: "往往", 22: "都会"`
  - mapping_reason: "많은데" maps to the frequency/habitual aspect "往往" + "都会".
* target[12]: "그 이유는"
  - source_tokens: `32: "就是", 33: "因为"`
  - mapping_reason: "이유" maps to "因为", "그" maps to "就是".
* target[13]: "뭘까요?"
  - source_tokens: `34: "什么？"`
  - mapping_reason: "뭘까요" maps to "什么".
* target[14]: "미네랄을"
  - source_tokens: `40: "矿", 41: "物质。"`
  - mapping_reason: "미네랄" maps to "矿物质".
* target[15]: "너무 많이 소모했기 때문입니다."
  - source_tokens: `35: "就是", 36: "消耗", 37: "了", 38: "太多", 39: "的"`
  - mapping_reason: "너무 많이" maps to "太多", "소모했기 때문" maps to "就是" + "消耗" + "了".

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>就会消耗我们</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>身体骨骼当中</src> <tgt>우리 몸</tgt>; start=3.00, end=4.00
4. <src>的矿物质，</src> <tgt>뼈 속의 미네랄을 소모하게 되고,</tgt>; start=4.00, end=5.00
5. <src>更多的靠物矿物质。</src> <tgt>미네랄에 더 의존하게 됩니다.</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>所以呢，</src> <tgt>그래서</tgt>; start=7.00, end=8.00
8. <src>这个肥胖人</src> <tgt>비만인 사람들은</tgt>; start=8.00, end=9.00
9. <src>往往都会有</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>这种关节</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>和软组织的问题，</src> <tgt>관절이나 연조직 문제를 겪는 경우가 많은데,</tgt>; start=13.00, end=14.00
14. <src>就是因为什么？</src> <tgt>그 이유는 뭘까요?</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>就是消耗了太多的矿物质。</src> <tgt>미네랄을 너무 많이 소모했기 때문입니다.</tgt>; start=16.00, end=16.84
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_NWf8Wc2GVvM_W000007 ===

source:
- language: Chinese
- transcription: 启示录和翡翠石板都曾经预测到，这十四万四千名光之工作者的到来，会在卡利年代结束时，将地球从黑暗势力的手中拯救出来。
- source_tokens:
  0. 启示
  1. 录
  2. 和
  3. 翡翠
  4. 石板
  5. 都
  6. 曾经
  7. 预测
  8. 到，
  9. 这
  10. 十四万
  11. 四千
  12. 名
  13. 光
  14. 之
  15. 工作
  16. 者
  17. 的
  18. 到来，
  19. 会
  20. 在
  21. 卡利
  22. 年代
  23. 结束
  24. 时，
  25. 将
  26. 地球
  27. 从
  28. 黑暗
  29. 势力
  30. 的
  31. 手中
  32. 拯救
  33. 出来。

target:
- language: English
- translation: The Book of Revelation and the Emerald Tablets both predicted that these 144,000 lightworkers would arrive and save the Earth from the hands of dark forces at the end of the Kali Yuga.
- target_sense_units:
  0. The Book of Revelation
  1. and the Emerald Tablets
  2. both predicted
  3. that these 144,000 lightworkers
  4. would arrive
  5. and save the Earth
  6. from the hands of
  7. dark forces
  8. at the end of
  9. the Kali Yuga.

scratchpad:
* target[0]: "The Book of Revelation"
  - source_tokens: `0: "启示", 1: "录"`
  - mapping_reason: Direct translation of "启示录".

* target[1]: "and the Emerald Tablets"
  - source_tokens: `2: "和", 3: "翡翠", 4: "石板"`
  - mapping_reason: "和" (and), "翡翠" (Emerald), "石板" (Tablets).

* target[2]: "both predicted"
  - source_tokens: `5: "都", 6: "曾经", 7: "预测", 8: "到，"`
  - mapping_reason: "都" (both), "曾经预测到" (predicted).

* target[3]: "that these 144,000 lightworkers"
  - source_tokens: `9: "这", 10: "十四万", 11: "四千", 12: "名", 13: "光", 14: "之", 15: "工作", 16: "者"`
  - mapping_reason: "这" (these), "十四万四千" (144,000), "名" (classifier), "光之工作者" (lightworkers).

* target[4]: "would arrive"
  - source_tokens: `18: "到来，", 19: "会"`
  - mapping_reason: "到来" (arrive), "会" (would).

* target[5]: "and save the Earth"
  - source_tokens: `25: "将", 26: "地球", 32: "拯救"`
  - mapping_reason: "将" (indicates object, part of save structure), "地球" (Earth), "拯救" (save).

* target[6]: "from the hands of"
  - source_tokens: `27: "从", 31: "手中"`
  - mapping_reason: "从" (from), "手中" (hands of).

* target[7]: "dark forces"
  - source_tokens: `28: "黑暗", 29: "势力", 30: "的"`
  - mapping_reason: "黑暗" (dark), "势力" (forces), "的" (possessive modifier).

* target[8]: "at the end of"
  - source_tokens: `20: "在", 24: "时，", 23: "结束"`
  - mapping_reason: "在...时" (at...the time of), "结束" (end).

* target[9]: "the Kali Yuga."
  - source_tokens: `21: "卡利", 22: "年代"`
  - mapping_reason: "卡利年代" (Kali Yuga).

result:
```html
0. <src>启示录</src> <tgt>The Book of Revelation</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>和翡翠石板</src> <tgt>and the Emerald Tablets</tgt>; start=2.00, end=3.00
3. <src>都曾经预测到，</src> <tgt>both predicted</tgt>; start=3.00, end=4.00
4. <src>这十四万四千名</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>光之工作者</src> <tgt>that these 144,000 lightworkers</tgt>; start=5.00, end=6.00
6. <src>的到来，</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>会在卡利年代</src> <tgt>would arrive</tgt>; start=7.00, end=8.00
8. <src>结束时，</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>将地球从</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>黑暗势力的手中</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>拯救出来。</src> <tgt>and save the Earth from the hands of dark forces at the end of the Kali Yuga.</tgt>; start=11.00, end=11.80
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_sQjhyfFvfLY_W000018 ===

source:
- language: Chinese
- transcription: 把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class，好，这个这一个那个物件的class，好。
- source_tokens:
  0. 把
  1. 它
  2. 丢进
  3. 去
  4. 之后
  5. 呢，
  6. 它
  7. 会
  8. 在
  9. 它
  10. 会
  11. 找到
  12. 这
  13. 一
  14. 个
  15. class，
  16. 把
  17. 它
  18. 转变
  19. 成
  20. 为
  21. 这
  22. 一
  23. 个
  24. class
  25. 的
  26. 的
  27. class，
  28. 好，
  29. 这
  30. 个
  31. 这
  32. 一
  33. 个
  34. 那
  35. 个
  36. 物件
  37. 的
  38. class，
  39. 好。

target:
- language: English
- translation: Once you put it in, it will find this class, and turn it into this class's class. Right, this object's class. Right.
- target_sense_units:
  0. Once you put it in,
  1. it will find
  2. this class,
  3. and turn it into
  4. this class's class.
  5. Right, this object's class.
  6. Right.

scratchpad:
* target[0]: "Once you put it in,"
  - source_tokens: `0: "把", 1: "它", 2: "丢进", 3: "去", 4: "之后", 5: "呢，"`
  - mapping_reason: "把它丢进去" maps to "put it in", "之后" maps to "Once", "呢" acts as a discourse marker for the temporal clause.

* target[1]: "it will find"
  - source_tokens: `6: "它", 7: "会", 11: "找到"`
  - mapping_reason: "它" (it), "会" (will), "找到" (find).

* target[2]: "this class,"
  - source_tokens: `12: "这", 13: "一", 14: "个", 15: "class，"`
  - mapping_reason: "这一个" (this), "class" (class).

* target[3]: "and turn it into"
  - source_tokens: `16: "把", 17: "它", 18: "转变", 19: "成", 20: "为"`
  - mapping_reason: "把" (and/marker), "它" (it), "转变成为" (turn into).

* target[4]: "this class's class."
  - source_tokens: `21: "这", 22: "一", 23: "个", 24: "class", 25: "的", 26: "的", 27: "class，"`
  - mapping_reason: "这一个" (this), "class" (class), "的" (possessive), "class" (class).

* target[5]: "Right, this object's class."
  - source_tokens: `28: "好，", 29: "这", 30: "个", 31: "这", 32: "一", 33: "个", 34: "那", 35: "个", 36: "物件", 37: "的", 38: "class，"`
  - mapping_reason: "好" (Right), "这一个那个物件的class" (this object's class).

* target[6]: "Right."
  - source_tokens: `39: "好。"`
  - mapping_reason: "好" (Right).

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>把它丢进去之后呢，它会在</src> <tgt>Once you put it in,</tgt>; start=1.00, end=2.00
2. <src>它会找到</src> <tgt>it will find</tgt>; start=2.00, end=3.00
3. <src>这一个class，</src> <tgt>this class,</tgt>; start=3.00, end=4.00
4. <src>把它转变成为</src> <tgt>and turn it into</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>这一个class</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>的的</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>class，</src> <tgt>this class's class.</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>好，</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>这个</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>这一个</src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>那个物件</src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>的class，</src> <tgt>Right, this object's class.</tgt>; start=15.00, end=16.00
16. <src>好。</src> <tgt>Right.</tgt>; start=16.00, end=16.32
```

- max_empty_window_count: 5


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Y4xRc2amPxY_W000056 ===

source:
- language: Chinese
- transcription: 我们采用了以吃脂脂肪、肥肉和油为主的饮食结构以后呢，那给我们带来了巨大的好处。第一个好处呢，就是我们减肥了。
- source_tokens:
  0. 我们
  1. 采用
  2. 了
  3. 以
  4. 吃脂
  5. 脂肪、
  6. 肥肉
  7. 和
  8. 油
  9. 为
  10. 主
  11. 的
  12. 饮食
  13. 结构
  14. 以后
  15. 呢，
  16. 那
  17. 给
  18. 我们
  19. 带来
  20. 了
  21. 巨大
  22. 的
  23. 好处。
  24. 第一
  25. 个
  26. 好处
  27. 呢，
  28. 就是
  29. 我们
  30. 减肥
  31. 了。

target:
- language: Korean
- translation: 우리는 지방과 기름진 고기, 그리고 기름 위주의 식단을 채택했습니다. 그 이후에 엄청난 이점이 생겼는데, 첫 번째는 바로 체중이 줄었다는 점입니다.
- target_sense_units:
  0. 우리는
  1. 지방과
  2. 기름진 고기,
  3. 그리고
  4. 기름 위주의 식단을
  5. 채택했습니다.
  6. 그 이후에
  7. 엄청난 이점이
  8. 생겼는데,
  9. 첫 번째는
  10. 바로
  11. 체중이
  12. 줄었다는 점입니다.

scratchpad:
* target[0]: "우리는"
  - source_tokens: `0: "我们"`
  - mapping_reason: Subject reference.
* target[1]: "지방과"
  - source_tokens: `5: "脂肪、"`
  - mapping_reason: Lexical content "fat".
* target[2]: "기름진 고기,"
  - source_tokens: `6: "肥肉"`
  - mapping_reason: Lexical content "fatty meat".
* target[3]: "그리고"
  - source_tokens: `7: "和"`
  - mapping_reason: Conjunction.
* target[4]: "기름 위주의 식단을"
  - source_tokens: `4: "吃脂", 8: "油", 9: "为", 10: "主", 12: "饮食", 13: "结构"`
  - mapping_reason: Describes the dietary structure based on oil/fat.
* target[5]: "채택했습니다."
  - source_tokens: `1: "采用", 2: "了"`
  - mapping_reason: Verb phrase "adopted".
* target[6]: "그 이후에"
  - source_tokens: `14: "以后", 15: "呢，"`
  - mapping_reason: Temporal marker.
* target[7]: "엄청난 이점이"
  - source_tokens: `21: "巨大", 22: "的", 23: "好处。"`
  - mapping_reason: "Huge benefits".
* target[8]: "생겼는데,"
  - source_tokens: `16: "那", 17: "给", 18: "我们", 19: "带来", 20: "了"`
  - mapping_reason: Causative structure "brought to us".
* target[9]: "첫 번째는"
  - source_tokens: `24: "第一", 25: "个", 26: "好处", 27: "呢，"`
  - mapping_reason: "First benefit".
* target[10]: "바로"
  - source_tokens: `28: "就是"`
  - mapping_reason: Emphatic marker.
* target[11]: "체중이"
  - source_tokens: `29: "我们", 30: "减肥"`
  - mapping_reason: Subject of weight loss.
* target[12]: "줄었다는 점입니다."
  - source_tokens: `31: "了。"`
  - mapping_reason: Completion marker indicating weight loss occurred.

result:
```html
0. <src>我们采用了</src> <tgt>우리는</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>以吃脂脂肪、</src> <tgt>지방과</tgt>; start=2.00, end=3.00
3. <src>肥肉和油</src> <tgt>기름진 고기, 그리고</tgt>; start=3.00, end=4.00
4. <src>为主的饮食结构</src> <tgt>기름 위주의 식단을 채택했습니다.</tgt>; start=4.00, end=5.00
5. <src>以后呢，</src> <tgt>그 이후에</tgt>; start=5.00, end=6.00
6. <src>那</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>给我们带来了巨大的好处。</src> <tgt>엄청난 이점이 생겼는데,</tgt>; start=7.00, end=8.00
8. <src>第一个</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>好处呢，</src> <tgt>첫 번째는</tgt>; start=9.00, end=10.00
10. <src>就是</src> <tgt>바로</tgt>; start=10.00, end=11.00
11. <src>我们减肥了。</src> <tgt>체중이 줄었다는 점입니다.</tgt>; start=11.00, end=11.36
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_sQjhyfFvfLY_W000018 ===

source:
- language: Chinese
- transcription: 把它丢进去之后呢，它会在它会找到这一个class，把它转变成为这一个class的的class，好，这个这一个那个物件的class，好。
- source_tokens:
  0. 把
  1. 它
  2. 丢进
  3. 去
  4. 之后
  5. 呢，
  6. 它
  7. 会
  8. 在
  9. 它
  10. 会
  11. 找到
  12. 这
  13. 一
  14. 个
  15. class，
  16. 把
  17. 它
  18. 转变
  19. 成
  20. 为
  21. 这
  22. 一
  23. 个
  24. class
  25. 的
  26. 的
  27. class，
  28. 好，
  29. 这
  30. 个
  31. 这
  32. 一
  33. 个
  34. 那
  35. 个
  36. 物件
  37. 的
  38. class，
  39. 好。

target:
- language: Japanese
- translation: それを中に入れたら、それが、そのクラスを見つけて、それをこのクラスのクラスに変換します。そう、この、この、あのオブジェクトのクラスに。はい。
- target_sense_units:
  0. それを
  1. 中に
  2. 入れたら、
  3. それが、
  4. そのクラスを
  5. 見つけて、
  6. それを
  7. このクラスのクラスに
  8. 変換します。
  9. そう、
  10. この、
  11. この、
  12. あのオブジェクトのクラスに。
  13. はい。

scratchpad:
* target[0]: "それを"
  - source_tokens: `1: "它"`
  - mapping_reason: Direct object reference "it".

* target[1]: "中に"
  - source_tokens: `2: "丢进"`
  - mapping_reason: Directional/locative component of "put into".

* target[2]: "入れたら、"
  - source_tokens: `2: "丢进", 3: "去", 4: "之后", 5: "呢，"`
  - mapping_reason: Verb "put" + temporal conditional "after".

* target[3]: "それが、"
  - source_tokens: `6: "它"`
  - mapping_reason: Subject reference "it".

* target[4]: "そのクラスを"
  - source_tokens: `12: "这", 13: "一", 14: "个", 15: "class，"`
  - mapping_reason: Object reference "this class".

* target[5]: "見つけて、"
  - source_tokens: `11: "找到"`
  - mapping_reason: Verb "find".

* target[6]: "それを"
  - source_tokens: `17: "它"`
  - mapping_reason: Direct object reference "it" (to be transformed).

* target[7]: "このクラスのクラスに"
  - source_tokens: `21: "这", 22: "一", 23: "个", 24: "class", 25: "的", 26: "的", 27: "class，"`
  - mapping_reason: Target state "into this class's class".

* target[8]: "変換します。"
  - source_tokens: `18: "转变", 19: "成", 20: "为"`
  - mapping_reason: Verb "transform into".

* target[9]: "そう、"
  - source_tokens: `28: "好，"`
  - mapping_reason: Discourse marker "right/okay".

* target[10]: "この、"
  - source_tokens: `29: "这", 30: "个"`
  - mapping_reason: Demonstrative reference.

* target[11]: "この、"
  - source_tokens: `31: "这", 32: "一", 33: "个"`
  - mapping_reason: Demonstrative reference (repeated).

* target[12]: "あのオブジェクトのクラスに。"
  - source_tokens: `34: "那", 35: "个", 36: "物件", 37: "的", 38: "class，"`
  - mapping_reason: Reference to "that object's class".

* target[13]: "はい。"
  - source_tokens: `39: "好。"`
  - mapping_reason: Discourse marker "okay/yes".

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>把它丢进去之后呢，它会在</src> <tgt>それを中に入れたら、それが、</tgt>; start=1.00, end=2.00
2. <src>它会找到</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>这一个class，</src> <tgt>そのクラスを見つけて、</tgt>; start=3.00, end=4.00
4. <src>把它转变成为</src> <tgt>それを</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>这一个class</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>的的</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>class，</src> <tgt>このクラスのクラスに変換します。</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>好，</src> <tgt>そう、</tgt>; start=11.00, end=12.00
12. <src>这个</src> <tgt>この、</tgt>; start=12.00, end=13.00
13. <src>这一个</src> <tgt>この、</tgt>; start=13.00, end=14.00
14. <src>那个物件</src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>的class，</src> <tgt>あのオブジェクトのクラスに。</tgt>; start=15.00, end=16.00
16. <src>好。</src> <tgt>はい。</tgt>; start=16.00, end=16.32
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_VJeW1Z4n0Qc_W000018 ===

source:
- language: Chinese
- transcription: 然后在洋馆的后面呢，其实有三排的，就是可以DIY互动的工作室跟体验的店家。但是因为今天我来的时间刚好是连假的最后一天，又是礼拜一，蛮多店都没开的，再加上洋馆也没有开放，所以我今天真的就是来这里单纯的逛逛。
- source_tokens:
  0. 然后
  1. 在
  2. 洋
  3. 馆
  4. 的
  5. 后面
  6. 呢，
  7. 其实
  8. 有
  9. 三
  10. 排
  11. 的，
  12. 就是
  13. 可以
  14. DIY
  15. 互动
  16. 的
  17. 工作
  18. 室
  19. 跟
  20. 体验
  21. 的
  22. 店家。
  23. 但是
  24. 因为
  25. 今天
  26. 我来
  27. 的
  28. 时间
  29. 刚好
  30. 是
  31. 连假
  32. 的
  33. 最后
  34. 一
  35. 天，
  36. 又是
  37. 礼拜
  38. 一，
  39. 蛮多
  40. 店
  41. 都
  42. 没开
  43. 的，
  44. 再
  45. 加上
  46. 洋
  47. 馆
  48. 也
  49. 没有
  50. 开放，
  51. 所以
  52. 我
  53. 今天
  54. 真的
  55. 就是
  56. 来
  57. 这里
  58. 单纯
  59. 的
  60. 逛逛。

target:
- language: Japanese
- translation: 洋館の裏には、DIY体験ができる工房やショップが3列並んでいます。ただ、今日は連休の最終日で月曜日ということもあって、閉まっているお店が結構多くて、それに洋館も開いていないので、本当にただぶらぶら歩きに来た感じです。
- target_sense_units:
  0. 洋館の裏には、
  1. DIY体験ができる
  2. 工房やショップが
  3. 3列
  4. 並んでいます。
  5. ただ、
  6. 今日は
  7. 連休の
  8. 最終日で
  9. 月曜日
  10. ということもあって、
  11. 閉まっている
  12. お店が
  13. 結構
  14. 多くて、
  15. それに
  16. 洋館も
  17. 開いていない
  18. ので、
  19. 本当に
  20. ただ
  21. ぶらぶら
  22. 歩きに来た
  23. 感じです。

scratchpad:
* target[0]: "洋館の裏には、"
  - source_tokens: `1: "在", 2: "洋", 3: "馆", 4: "的", 5: "后面"`
  - mapping_reason: Location expression "behind the Western-style building".

* target[1]: "DIY体験ができる"
  - source_tokens: `13: "可以", 14: "DIY", 15: "互动", 20: "体验"`
  - mapping_reason: "DIY" and "experience" (体验) capabilities.

* target[2]: "工房やショップが"
  - source_tokens: `17: "工作", 18: "室", 19: "跟", 22: "店家"`
  - mapping_reason: "Studios" (工作+室) and "shops" (店家).

* target[3]: "3列"
  - source_tokens: `9: "三", 10: "排"`
  - mapping_reason: Quantity "three rows".

* target[4]: "並んでいます。"
  - source_tokens: `8: "有"`
  - mapping_reason: Existence verb indicating the layout of the rows.

* target[5]: "ただ、"
  - source_tokens: `23: "但是"`
  - mapping_reason: Adversative conjunction.

* target[6]: "今日は"
  - source_tokens: `25: "今天"`
  - mapping_reason: Time reference.

* target[7]: "連休の"
  - source_tokens: `31: "连假"`
  - mapping_reason: Holiday period.

* target[8]: "最終日で"
  - source_tokens: `33: "最后", 34: "一", 35: "天"`
  - mapping_reason: Last day of the holiday.

* target[9]: "月曜日"
  - source_tokens: `37: "礼拜", 38: "一"`
  - mapping_reason: Day of the week (Monday).

* target[10]: "ということもあって、"
  - source_tokens: `24: "因为", 36: "又是"`
  - mapping_reason: Causal/reasoning structure.

* target[11]: "閉まっている"
  - source_tokens: `42: "没开"`
  - mapping_reason: Shops not open.

* target[12]: "お店が"
  - source_tokens: `40: "店"`
  - mapping_reason: Subject (shops).

* target[13]: "結構"
  - source_tokens: `39: "蛮多"`
  - mapping_reason: Degree modifier (many/quite a few).

* target[14]: "多くて、"
  - source_tokens: `39: "蛮多"`
  - mapping_reason: Quantity modifier (many).

* target[15]: "それに"
  - source_tokens: `44: "再", 45: "加上"`
  - mapping_reason: Additive conjunction (furthermore).

* target[16]: "洋館も"
  - source_tokens: `46: "洋", 47: "馆", 48: "也"`
  - mapping_reason: Subject (Western-style building) + additive "also".

* target[17]: "開いていない"
  - source_tokens: `49: "没有", 50: "开放"`
  - mapping_reason: Building not open.

* target[18]: "ので、"
  - source_tokens: `51: "所以"`
  - mapping_reason: Causal marker.

* target[19]: "本当に"
  - source_tokens: `54: "真的"`
  - mapping_reason: Emphasis.

* target[20]: "ただ"
  - source_tokens: `55: "就是", 58: "单纯"`
  - mapping_reason: Limitation to "just/simply".

* target[21]: "ぶらぶら"
  - source_tokens: `60: "逛逛"`
  - mapping_reason: Manner of walking (strolling).

* target[22]: "歩きに来た"
  - source_tokens: `56: "来", 57: "这里"`
  - mapping_reason: Action of coming here.

* target[23]: "感じです。"
  - source_tokens: `59: "的"`
  - mapping_reason: Nominalizer indicating the state or impression of the situation.

result:
```html
0. <src>然后</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>在洋馆的后面</src> <tgt>洋館の裏には、</tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>呢，其实有三排</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>的，</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>就是可以DIY</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>互动的工作室</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>跟体验的店家。</src> <tgt>DIY体験ができる工房やショップが3列並んでいます。</tgt>; start=8.00, end=9.00
9. <src>但是</src> <tgt>ただ、</tgt>; start=9.00, end=10.00
10. <src>因为今天我来的时间</src> <tgt>今日は</tgt>; start=10.00, end=11.00
11. <src>刚好是连假的</src> <tgt>連休の</tgt>; start=11.00, end=12.00
12. <src>最后一天，</src> <tgt>最終日で</tgt>; start=12.00, end=13.00
13. <src>又是礼拜一，</src> <tgt>月曜日ということもあって、</tgt>; start=13.00, end=14.00
14. <src>蛮多店都没开的，</src> <tgt>閉まっているお店が結構多くて、</tgt>; start=14.00, end=15.00
15. <src>再加上洋馆</src> <tgt>それに</tgt>; start=15.00, end=16.00
16. <src>也没有开放，</src> <tgt>洋館も開いていない</tgt>; start=16.00, end=17.00
17. <src>所以</src> <tgt>ので、</tgt>; start=17.00, end=18.00
18. <src>我今天真的就是</src> <tgt>本当に</tgt>; start=18.00, end=19.00
19. <src>来这里单纯的</src> <tgt>ただ</tgt>; start=19.00, end=20.00
20. <src>逛逛。</src> <tgt>ぶらぶら歩きに来た感じです。</tgt>; start=20.00, end=20.97
```

- max_empty_window_count: 6


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_VJeW1Z4n0Qc_W000018 ===

source:
- language: Chinese
- transcription: 然后在洋馆的后面呢，其实有三排的，就是可以DIY互动的工作室跟体验的店家。但是因为今天我来的时间刚好是连假的最后一天，又是礼拜一，蛮多店都没开的，再加上洋馆也没有开放，所以我今天真的就是来这里单纯的逛逛。
- source_tokens:
  0. 然后
  1. 在
  2. 洋
  3. 馆
  4. 的
  5. 后面
  6. 呢，
  7. 其实
  8. 有
  9. 三
  10. 排
  11. 的，
  12. 就是
  13. 可以
  14. DIY
  15. 互动
  16. 的
  17. 工作
  18. 室
  19. 跟
  20. 体验
  21. 的
  22. 店家。
  23. 但是
  24. 因为
  25. 今天
  26. 我来
  27. 的
  28. 时间
  29. 刚好
  30. 是
  31. 连假
  32. 的
  33. 最后
  34. 一
  35. 天，
  36. 又是
  37. 礼拜
  38. 一，
  39. 蛮多
  40. 店
  41. 都
  42. 没开
  43. 的，
  44. 再
  45. 加上
  46. 洋
  47. 馆
  48. 也
  49. 没有
  50. 开放，
  51. 所以
  52. 我
  53. 今天
  54. 真的
  55. 就是
  56. 来
  57. 这里
  58. 单纯
  59. 的
  60. 逛逛。

target:
- language: English
- translation: And behind the Western-style house, there are actually three rows of studios and experience shops where you can do DIY activities. But I came on the last day of the long weekend, and it's a Monday, so quite a few shops are closed. Plus, the Western-style house isn't open either, so I'm really just here for a stroll today.
- target_sense_units:
  0. And behind
  1. the Western- style house,
  2. there are actually
  3. three rows of
  4. studios and experience shops
  5. where you can do
  6. DIY activities.
  7. But I
  8. came on
  9. the last day of
  10. the long weekend,
  11. and it's a Monday,
  12. so quite a few
  13. shops are closed.
  14. Plus,
  15. the Western- style house
  16. isn't open either,
  17. so I'm
  18. really just
  19. here for
  20. a stroll today.

scratchpad:
* target[0]: "And behind"
  - source_tokens: `0: "然后", 1: "在", 5: "后面"`
  - mapping_reason: Connective "然后" and locative markers "在...后面".
* target[1]: "the Western- style house,"
  - source_tokens: `2: "洋", 3: "馆"`
  - mapping_reason: Noun phrase representing the landmark.
* target[2]: "there are actually"
  - source_tokens: `7: "其实", 8: "有"`
  - mapping_reason: Existence marker with stance "其实".
* target[3]: "three rows of"
  - source_tokens: `9: "三", 10: "排"`
  - mapping_reason: Quantity and classifier.
* target[4]: "studios and experience shops"
  - source_tokens: `17: "工作", 18: "室", 19: "跟", 20: "体验", 22: "店家"`
  - mapping_reason: Core noun entities.
* target[5]: "where you can do"
  - source_tokens: `12: "就是", 13: "可以"`
  - mapping_reason: Relative clause structure and modality.
* target[6]: "DIY activities."
  - source_tokens: `14: "DIY", 15: "互动"`
  - mapping_reason: Activity description.
* target[7]: "But I"
  - source_tokens: `23: "但是", 26: "我来"`
  - mapping_reason: Contrastive conjunction and subject.
* target[8]: "came on"
  - source_tokens: `26: "我来", 28: "时间"`
  - mapping_reason: Verb of arrival and timing.
* target[9]: "the last day of"
  - source_tokens: `33: "最后", 34: "一", 35: "天"`
  - mapping_reason: Temporal specification.
* target[10]: "the long weekend,"
  - source_tokens: `31: "连假"`
  - mapping_reason: Temporal context.
* target[11]: "and it's a Monday,"
  - source_tokens: `36: "又是", 37: "礼拜", 38: "一"`
  - mapping_reason: Additional temporal condition.
* target[12]: "so quite a few"
  - source_tokens: `39: "蛮多"`
  - mapping_reason: Quantifier of shops.
* target[13]: "shops are closed."
  - source_tokens: `40: "店", 41: "都", 42: "没开"`
  - mapping_reason: Subject and state of closure.
* target[14]: "Plus,"
  - source_tokens: `44: "再", 45: "加上"`
  - mapping_reason: Additive conjunction.
* target[15]: "the Western- style house"
  - source_tokens: `46: "洋", 47: "馆"`
  - mapping_reason: Reference to landmark.
* target[16]: "isn't open either,"
  - source_tokens: `48: "也", 49: "没有", 50: "开放"`
  - mapping_reason: Negative state and additive "either".
* target[17]: "so I'm"
  - source_tokens: `51: "所以", 52: "我"`
  - mapping_reason: Resultative conjunction and subject.
* target[18]: "really just"
  - source_tokens: `54: "真的", 55: "就是", 58: "单纯"`
  - mapping_reason: Adverbial stance and limitation.
* target[19]: "here for"
  - source_tokens: `56: "来", 57: "这里"`
  - mapping_reason: Location and intent.
* target[20]: "a stroll today."
  - source_tokens: `25: "今天", 60: "逛逛"`
  - mapping_reason: Action and temporal frame.

result:
```html
0. <src>然后</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>在洋馆的后面</src> <tgt>And behind the Western- style house,</tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>呢，其实有三排</src> <tgt>there are actually three rows of</tgt>; start=3.00, end=4.00
4. <src>的，</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>就是可以DIY</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>互动的工作室</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>跟体验的店家。</src> <tgt>studios and experience shops where you can do DIY activities.</tgt>; start=8.00, end=9.00
9. <src>但是</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>因为今天我来的时间</src> <tgt>But I came on</tgt>; start=10.00, end=11.00
11. <src>刚好是连假的</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>最后一天，</src> <tgt>the last day of the long weekend,</tgt>; start=12.00, end=13.00
13. <src>又是礼拜一，</src> <tgt>and it's a Monday,</tgt>; start=13.00, end=14.00
14. <src>蛮多店都没开的，</src> <tgt>so quite a few shops are closed.</tgt>; start=14.00, end=15.00
15. <src>再加上洋馆</src> <tgt>Plus, the Western- style house</tgt>; start=15.00, end=16.00
16. <src>也没有开放，</src> <tgt>isn't open either,</tgt>; start=16.00, end=17.00
17. <src>所以</src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>我今天真的就是</src> <tgt>so I'm</tgt>; start=18.00, end=19.00
19. <src>来这里单纯的</src> <tgt>really just here for</tgt>; start=19.00, end=20.00
20. <src>逛逛。</src> <tgt>a stroll today.</tgt>; start=20.00, end=20.97
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Q0a8pjeI4HA_W000054 ===

source:
- language: Chinese
- transcription: 那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命、在招命喽。换句话说，荧幕前的各位朋友。
- source_tokens:
  0. 那
  1. 你
  2. 就
  3. 可以
  4. 变成
  5. 那百
  6. 分
  7. 之
  8. 二十
  9. 的
  10. 人，
  11. 去
  12. 成就
  13. 不
  14. 一样
  15. 的
  16. 人生，
  17. 可以
  18. 知命、
  19. 懂
  20. 命、
  21. 用
  22. 命、
  23. 在
  24. 招命
  25. 喽。
  26. 换
  27. 句
  28. 话
  29. 说，
  30. 荧幕
  31. 前
  32. 的
  33. 各位
  34. 朋友。

target:
- language: English
- translation: Then you can become part of that 20%—the ones who achieve a different life. You can know your fate, understand it, use it, and create it. In other words, to all my friends in front of the screen.
- target_sense_units:
  0. Then you can
  1. become part of
  2. that 20%—
  3. the ones who
  4. achieve a different life.
  5. You can know
  6. your fate,
  7. understand it,
  8. use it,
  9. and create it.
  10. In other words,
  11. to all my friends
  12. in front of
  13. the screen.

scratchpad:
* target[0]: "Then you can"
  - source_tokens: `0: "那", 1: "你", 2: "就", 3: "可以"`
  - mapping_reason: Direct translation of discourse marker "那", subject "你", connective "就", and modal "可以".
* target[1]: "become part of"
  - source_tokens: `4: "变成"`
  - mapping_reason: Lexical realization of "变成".
* target[2]: "that 20%—"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十"`
  - mapping_reason: Numerical expression "那百分之二十".
* target[3]: "the ones who"
  - source_tokens: `9: "的", 10: "人，"`
  - mapping_reason: Nominalization "的" and head noun "人".
* target[4]: "achieve a different life."
  - source_tokens: `11: "去", 12: "成就", 13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: Verb "成就" and object phrase "不一样的人生".
* target[5]: "You can know"
  - source_tokens: `17: "可以", 18: "知命、"`
  - mapping_reason: Modal "可以" and verb "知".
* target[6]: "your fate,"
  - source_tokens: `18: "知命、"`
  - mapping_reason: Object "命" of "知".
* target[7]: "understand it,"
  - source_tokens: `19: "懂", 20: "命、"`
  - mapping_reason: Verb "懂" and object "命".
* target[8]: "use it,"
  - source_tokens: `21: "用", 22: "命、"`
  - mapping_reason: Verb "用" and object "命".
* target[9]: "and create it."
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: Verb phrase "招命" (interpreted as create/summon fate) and final particle "喽".
* target[10]: "In other words,"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Fixed expression "换句话说".
* target[11]: "to all my friends"
  - source_tokens: `33: "各位", 34: "朋友。"`
  - mapping_reason: Noun phrase "各位朋友".
* target[12]: "in front of"
  - source_tokens: `30: "荧幕", 31: "前"`
  - mapping_reason: Prepositional phrase "荧幕前".
* target[13]: "the screen."
  - source_tokens: `30: "荧幕", 32: "的"`
  - mapping_reason: Object "荧幕" modified by "的".

result:
```html
0. <src>那你就可以</src> <tgt>Then you can</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>变成那百分之二十</src> <tgt>become part of that 20%—</tgt>; start=2.00, end=3.00
3. <src>的人，去成就</src> <tgt>the ones who</tgt>; start=3.00, end=4.00
4. <src>不一样的人生，可以</src> <tgt>achieve a different life.</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>知命、懂命、用命、</src> <tgt>You can know your fate, understand it, use it,</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>在招命喽。</src> <tgt>and create it.</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>换句话说，</src> <tgt>In other words,</tgt>; start=10.00, end=11.00
11. <src>荧幕前的各位朋友。</src> <tgt>to all my friends in front of the screen.</tgt>; start=11.00, end=11.73
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Y4xRc2amPxY_W000024 ===

source:
- language: Chinese
- transcription: 就会消耗我们身体骨骼当中的矿物质，更多的靠物矿物质。所以呢，这个肥胖人往往都会有这种关节和软组织的问题，就是因为什么？就是消耗了太多的矿物质。
- source_tokens:
  0. 就
  1. 会
  2. 消耗
  3. 我们
  4. 身体
  5. 骨骼
  6. 当中
  7. 的
  8. 矿
  9. 物质，
  10. 更多
  11. 的
  12. 靠物
  13. 矿
  14. 物质。
  15. 所以
  16. 呢，
  17. 这
  18. 个
  19. 肥胖
  20. 人
  21. 往往
  22. 都会
  23. 有
  24. 这
  25. 种
  26. 关节
  27. 和
  28. 软
  29. 组织
  30. 的
  31. 问题，
  32. 就是
  33. 因为
  34. 什么？
  35. 就是
  36. 消耗
  37. 了
  38. 太多
  39. 的
  40. 矿
  41. 物质。

target:
- language: English
- translation: It depletes the minerals in our bones—it relies more on minerals. That's why people with obesity often have joint and soft tissue problems. Why? Because too many minerals have been used up.
- target_sense_units:
  0. It depletes
  1. the minerals in our bones—
  2. it relies
  3. more on minerals.
  4. That's why
  5. people with obesity
  6. often have
  7. joint and soft tissue problems.
  8. Why?
  9. Because too many minerals
  10. have been used up.

scratchpad:
* target[0]: "It depletes"
  - source_tokens: `0: "就", 1: "会", 2: "消耗"`
  - mapping_reason: Expresses the action of depletion (消耗) along with the conditional/future aspect (就会).

* target[1]: "the minerals in our bones—"
  - source_tokens: `3: "我们", 4: "身体", 5: "骨骼", 6: "当中", 7: "的", 8: "矿", 9: "物质，"`
  - mapping_reason: Specifies the object (minerals) and location (bones).

* target[2]: "it relies"
  - source_tokens: `12: "靠物"`
  - mapping_reason: Corresponds to the verb "靠" (rely).

* target[3]: "more on minerals."
  - source_tokens: `10: "更多", 11: "的", 13: "矿", 14: "物质。"`
  - mapping_reason: Specifies the degree and the object of reliance.

* target[4]: "That's why"
  - source_tokens: `15: "所以", 16: "呢，"`
  - mapping_reason: Expresses the causal link (所以).

* target[5]: "people with obesity"
  - source_tokens: `17: "这", 18: "个", 19: "肥胖", 20: "人"`
  - mapping_reason: Subject of the consequence clause.

* target[6]: "often have"
  - source_tokens: `21: "往往", 22: "都会", 23: "有"`
  - mapping_reason: Frequency and existence of the condition.

* target[7]: "joint and soft tissue problems."
  - source_tokens: `24: "这", 25: "种", 26: "关节", 27: "和", 28: "软", 29: "组织", 30: "的", 31: "问题，"`
  - mapping_reason: Specifies the subject matter of the problems.

* target[8]: "Why?"
  - source_tokens: `32: "就是", 33: "因为", 34: "什么？"`
  - mapping_reason: Question word and context.

* target[9]: "Because too many minerals"
  - source_tokens: `38: "太多", 39: "的", 40: "矿", 41: "物质。"`
  - mapping_reason: Causal subject of the final explanation.

* target[10]: "have been used up."
  - source_tokens: `36: "消耗", 37: "了"`
  - mapping_reason: The verbal action of depletion.

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>就会消耗我们</src> <tgt>It depletes</tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>身体骨骼当中</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>的矿物质，</src> <tgt>the minerals in our bones—</tgt>; start=4.00, end=5.00
5. <src>更多的靠物矿物质。</src> <tgt>it relies more on minerals.</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>所以呢，</src> <tgt>That's why</tgt>; start=7.00, end=8.00
8. <src>这个肥胖人</src> <tgt>people with obesity</tgt>; start=8.00, end=9.00
9. <src>往往都会有</src> <tgt>often have</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>这种关节</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>和软组织的问题，</src> <tgt>joint and soft tissue problems.</tgt>; start=13.00, end=14.00
14. <src>就是因为什么？</src> <tgt>Why?</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>就是消耗了太多的矿物质。</src> <tgt>Because too many minerals have been used up.</tgt>; start=16.00, end=16.84
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[9]
  - verdict: mapping_error
  - reason: "The target unit 'Because too many minerals' does not include the verbal action '消耗' (depleted/used up), which is correctly shifted to the next unit."
  - replace_source_tokens: 38: "太多", 39: "的", 40: "矿", 41: "物质。"
  validation:
    scratchpad:
* target[0]: "It depletes"
  - source_tokens: `0: "就", 1: "会", 2: "消耗"`
  - mapping_reason: "就" (then/it), "会" (will/depletes), "消耗" (deplete).

* target[1]: "the minerals in our bones—"
  - source_tokens: `3: "我们", 4: "身体", 5: "骨骼", 6: "当中", 7: "的", 8: "矿", 9: "物质，"`
  - mapping_reason: "我们" (our), "身体" (body/implied), "骨骼" (bones), "当中" (in), "矿物质" (minerals).

* target[2]: "it relies"
  - source_tokens: `12: "靠物"`
  - mapping_reason: "靠" (rely).

* target[3]: "more on minerals."
  - source_tokens: `10: "更多", 11: "的", 13: "矿", 14: "物质。"`
  - mapping_reason: "更多" (more), "矿物质" (minerals).

* target[4]: "That's why"
  - source_tokens: `15: "所以", 16: "呢，"`
  - mapping_reason: "所以" (so/that's why).

* target[5]: "people with obesity"
  - source_tokens: `17: "这", 18: "个", 19: "肥胖", 20: "人"`
  - mapping_reason: "这个" (these/the), "肥胖人" (obese people).

* target[6]: "often have"
  - source_tokens: `21: "往往", 22: "都会", 23: "有"`
  - mapping_reason: "往往" (often), "都会" (all/always/have), "有" (have).

* target[7]: "joint and soft tissue problems."
  - source_tokens: `24: "这", 25: "种", 26: "关节", 27: "和", 28: "软", 29: "组织", 30: "的", 31: "问题，"`
  - mapping_reason: "这种" (this kind of), "关节" (joint), "和" (and), "软组织" (soft tissue), "问题" (problems).

* target[8]: "Why?"
  - source_tokens: `32: "就是", 33: "因为", 34: "什么？"`
  - mapping_reason: "就是因为什么" (is because what/why).

* target[9]: "Because too many minerals"
  - source_tokens: `35: "就是", 36: "消耗", 37: "了", 38: "太多", 39: "的", 40: "矿", 41: "物质。"`
  - mapping_reason: "消耗" (used up), "太多" (too many), "矿物质" (minerals).

* target[10]: "have been used up."
  - source_tokens: `36: "消耗", 37: "了"`
  - mapping_reason: "消耗了" (have been used up/depleted).
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [3, 4, 5, 6, 7, 8, 9]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [12]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [10, 11, 13, 14]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [17, 18, 19, 20]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [21, 22, 23]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [24, 25, 26, 27, 28, 29, 30, 31]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [32, 33, 34]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [35, 36, 37, 38, 39, 40, 41]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [36, 37]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_VJeW1Z4n0Qc_W000018 ===

source:
- language: Chinese
- transcription: 然后在洋馆的后面呢，其实有三排的，就是可以DIY互动的工作室跟体验的店家。但是因为今天我来的时间刚好是连假的最后一天，又是礼拜一，蛮多店都没开的，再加上洋馆也没有开放，所以我今天真的就是来这里单纯的逛逛。
- source_tokens:
  0. 然后
  1. 在
  2. 洋
  3. 馆
  4. 的
  5. 后面
  6. 呢，
  7. 其实
  8. 有
  9. 三
  10. 排
  11. 的，
  12. 就是
  13. 可以
  14. DIY
  15. 互动
  16. 的
  17. 工作
  18. 室
  19. 跟
  20. 体验
  21. 的
  22. 店家。
  23. 但是
  24. 因为
  25. 今天
  26. 我来
  27. 的
  28. 时间
  29. 刚好
  30. 是
  31. 连假
  32. 的
  33. 最后
  34. 一
  35. 天，
  36. 又是
  37. 礼拜
  38. 一，
  39. 蛮多
  40. 店
  41. 都
  42. 没开
  43. 的，
  44. 再
  45. 加上
  46. 洋
  47. 馆
  48. 也
  49. 没有
  50. 开放，
  51. 所以
  52. 我
  53. 今天
  54. 真的
  55. 就是
  56. 来
  57. 这里
  58. 单纯
  59. 的
  60. 逛逛。

target:
- language: Korean
- translation: 그리고 양관 뒤편에는 사실 DIY 체험을 할 수 있는 공방이랑 매장들이 세 줄로 있어요. 하지만 제가 온 오늘이 마침 연휴 마지막 날인 데다 월요일이라 문을 닫은 가게가 꽤 많더라고요. 게다가 양관도 개방하지 않아서, 오늘은 그냥 가볍게 둘러보러 왔어요.
- target_sense_units:
  0. 그리고
  1. 양관 뒤편에는
  2. 사실
  3. DIY 체험을
  4. 할 수 있는
  5. 공방이랑
  6. 매장들이
  7. 세 줄로
  8. 있어요.
  9. 하지만
  10. 제가
  11. 온 오늘이
  12. 마침
  13. 연휴 마지막 날인 데다
  14. 월요일이라
  15. 문을
  16. 닫은 가게가
  17. 꽤
  18. 많더라고요.
  19. 게다가
  20. 양관도
  21. 개방하지 않아서,
  22. 오늘은
  23. 그냥
  24. 가볍게
  25. 둘러보러
  26. 왔어요.

scratchpad:
* target[0]: "그리고"
  - source_tokens: `0: "然后"`
  - mapping_reason: Connective "and/then"
* target[1]: "양관 뒤편에는"
  - source_tokens: `1: "在", 2: "洋", 3: "馆", 4: "的", 5: "后面"`
  - mapping_reason: Location "behind the Western-style building"
* target[2]: "사실"
  - source_tokens: `7: "其实"`
  - mapping_reason: Adverb "actually"
* target[3]: "DIY 체험을"
  - source_tokens: `14: "DIY", 15: "互动", 20: "体验"`
  - mapping_reason: DIY and interactive experience
* target[4]: "할 수 있는"
  - source_tokens: `13: "可以"`
  - mapping_reason: Ability modifier
* target[5]: "공방이랑"
  - source_tokens: `17: "工", 18: "作", 19: "室", 19: "跟"`
  - mapping_reason: Workshop and ...
* target[6]: "매장들이"
  - source_tokens: `22: "店家"`
  - mapping_reason: Shops
* target[7]: "세 줄로"
  - source_tokens: `9: "三", 10: "排"`
  - mapping_reason: Three rows
* target[8]: "있어요."
  - source_tokens: `8: "有"`
  - mapping_reason: Existence verb
* target[9]: "하지만"
  - source_tokens: `23: "但是"`
  - mapping_reason: Contrastive conjunction
* target[10]: "제가"
  - source_tokens: `52: "我"`
  - mapping_reason: Subject pronoun
* target[11]: "온 오늘이"
  - source_tokens: `25: "今天", 26: "我来", 27: "的", 28: "时间"`
  - mapping_reason: The day I came
* target[12]: "마침"
  - source_tokens: `29: "刚好"`
  - mapping_reason: Coincidence adverb
* target[13]: "연휴 마지막 날인 데다"
  - source_tokens: `31: "连假", 32: "的", 33: "最后", 34: "一", 35: "天"`
  - mapping_reason: Last day of the holiday
* target[14]: "월요일이라"
  - source_tokens: `36: "又是", 37: "礼拜", 38: "一"`
  - mapping_reason: It's also Monday
* target[15]: "문을"
  - source_tokens: `42: "没开"`
  - mapping_reason: Door/store closure state
* target[16]: "닫은 가게가"
  - source_tokens: `40: "店", 41: "都", 42: "没开"`
  - mapping_reason: Closed stores
* target[17]: "꽤"
  - source_tokens: `39: "蛮多"`
  - mapping_reason: Quantifier "quite a few"
* target[18]: "많더라고요."
  - source_tokens: `39: "蛮多"`
  - mapping_reason: Verb state "are many"
* target[19]: "게다가"
  - source_tokens: `44: "再", 45: "加上"`
  - mapping_reason: Additional reason
* target[20]: "양관도"
  - source_tokens: `46: "洋", 47: "馆", 48: "也"`
  - mapping_reason: Western-style building also
* target[21]: "개방하지 않아서,"
  - source_tokens: `49: "没有", 50: "开放"`
  - mapping_reason: Not open
* target[22]: "오늘은"
  - source_tokens: `53: "今天"`
  - mapping_reason: Today
* target[23]: "그냥"
  - source_tokens: `55: "就是"`
  - mapping_reason: Just/simply
* target[24]: "가볍게"
  - source_tokens: `58: "单纯"`
  - mapping_reason: Simply/lightly
* target[25]: "둘러보러"
  - source_tokens: `56: "来", 57: "这里", 60: "逛逛"`
  - mapping_reason: Come here to browse
* target[26]: "왔어요."
  - source_tokens: `56: "来"`
  - mapping_reason: Came

result:
```html
0. <src>然后</src> <tgt>그리고</tgt>; start=0.00, end=1.00
1. <src>在洋馆的后面</src> <tgt>양관 뒤편에는</tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>呢，其实有三排</src> <tgt>사실</tgt>; start=3.00, end=4.00
4. <src>的，</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>就是可以DIY</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>互动的工作室</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>跟体验的店家。</src> <tgt>DIY 체험을 할 수 있는 공방이랑 매장들이 세 줄로 있어요.</tgt>; start=8.00, end=9.00
9. <src>但是</src> <tgt>하지만</tgt>; start=9.00, end=10.00
10. <src>因为今天我来的时间</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>刚好是连假的</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>最后一天，</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>又是礼拜一，</src> <tgt><|wait|></tgt>; start=13.00, end=14.00
14. <src>蛮多店都没开的，</src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>再加上洋馆</src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>也没有开放，</src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>所以</src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src>我今天真的就是</src> <tgt>제가 온 오늘이 마침 연휴 마지막 날인 데다 월요일이라 문을 닫은 가게가 꽤 많더라고요. 게다가 양관도 개방하지 않아서, 오늘은 그냥</tgt>; start=18.00, end=19.00
19. <src>来这里单纯的</src> <tgt>가볍게</tgt>; start=19.00, end=20.00
20. <src>逛逛。</src> <tgt>둘러보러 왔어요.</tgt>; start=20.00, end=20.97
```

- max_empty_window_count: 8


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_Q0a8pjeI4HA_W000054 ===

source:
- language: Chinese
- transcription: 那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命、在招命喽。换句话说，荧幕前的各位朋友。
- source_tokens:
  0. 那
  1. 你
  2. 就
  3. 可以
  4. 变成
  5. 那百
  6. 分
  7. 之
  8. 二十
  9. 的
  10. 人，
  11. 去
  12. 成就
  13. 不
  14. 一样
  15. 的
  16. 人生，
  17. 可以
  18. 知命、
  19. 懂
  20. 命、
  21. 用
  22. 命、
  23. 在
  24. 招命
  25. 喽。
  26. 换
  27. 句
  28. 话
  29. 说，
  30. 荧幕
  31. 前
  32. 的
  33. 各位
  34. 朋友。

target:
- language: Korean
- translation: 그럼 당신은 상위 20%가 되어 남다른 인생을 이루는 겁니다. 자신의 운명을 알고, 이해하고, 활용하고, 더 나아가 운명을 개척하는 것이죠. 다시 말해, 화면 앞에 계신 여러분.
- target_sense_units:
  0. 그럼
  1. 당신은
  2. 상위 20%가 되어
  3. 남다른 인생을
  4. 이루는 겁니다.
  5. 자신의 운명을
  6. 알고,
  7. 이해하고,
  8. 활용하고,
  9. 더 나아가
  10. 운명을
  11. 개척하는 것이죠.
  12. 다시 말해,
  13. 화면 앞에
  14. 계신 여러분.

scratchpad:
* target[0]: "그럼"
  - source_tokens: `0: "那"`
  - mapping_reason: Discourse connective indicating consequence.
* target[1]: "당신은"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject pronoun.
* target[2]: "상위 20%가 되어"
  - source_tokens: `2: "就", 3: "可以", 4: "变成", 5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Transformation into the top 20% group.
* target[3]: "남다른 인생을"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: Object of achievement (different life).
* target[4]: "이루는 겁니다."
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: Action of achieving the life.
* target[5]: "자신의 운명을"
  - source_tokens: `18: "知命、"`
  - mapping_reason: The object "命" (fate/destiny) associated with the first verb.
* target[6]: "알고,"
  - source_tokens: `18: "知命、"`
  - mapping_reason: Verb "知" (know).
* target[7]: "이해하고,"
  - source_tokens: `19: "懂", 20: "命、"`
  - mapping_reason: Verb "懂" (understand) and its object.
* target[8]: "활용하고,"
  - source_tokens: `21: "用", 22: "命、"`
  - mapping_reason: Verb "用" (use/utilize) and its object.
* target[9]: "더 나아가"
  - source_tokens: `23: "在"`
  - mapping_reason: Progressive/further action marker.
* target[10]: "운명을"
  - source_tokens: `24: "招命"`
  - mapping_reason: Object "命" (fate) for the final verb.
* target[11]: "개척하는 것이죠."
  - source_tokens: `24: "招命", 25: "喽。"`
  - mapping_reason: Verb "招" (summon/create/pioneer) and sentence ending particle.
* target[12]: "다시 말해,"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse marker for restatement.
* target[13]: "화면 앞에"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的"`
  - mapping_reason: Location reference.
* target[14]: "계신 여러분."
  - source_tokens: `33: "各位", 34: "朋友。"`
  - mapping_reason: Address to the audience.

result:
```html
0. <src>那你就可以</src> <tgt>그럼 당신은</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>变成那百分之二十</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>的人，去成就</src> <tgt>상위 20%가 되어</tgt>; start=3.00, end=4.00
4. <src>不一样的人生，可以</src> <tgt>남다른 인생을 이루는 겁니다.</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>知命、懂命、用命、</src> <tgt>자신의 운명을 알고, 이해하고, 활용하고,</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>在招命喽。</src> <tgt>더 나아가 운명을 개척하는 것이죠.</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>换句话说，</src> <tgt>다시 말해,</tgt>; start=10.00, end=11.00
11. <src>荧幕前的各位朋友。</src> <tgt>화면 앞에 계신 여러분.</tgt>; start=11.00, end=11.73
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[5]
  - verdict: mapping_error
  - reason: "The mapping includes verbs (知, 懂, 用, 招) that are translated in subsequent units, instead of just the noun '命'."
  - replace_source_tokens: 18: "知命、", 20: "命、", 22: "命、", 24: "招命"
  validation:
    scratchpad:
* target[0]: "그럼"
  - source_tokens: `0: "那"`
  - mapping_reason: Discourse marker indicating sequence/consequence.

* target[1]: "당신은"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject pronoun.

* target[2]: "상위 20%가 되어"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人"`
  - mapping_reason: Numerical modifier for the group.

* target[3]: "남다른 인생을"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生"`
  - mapping_reason: Direct object noun phrase describing life.

* target[4]: "이루는 겁니다."
  - source_tokens: `2: "就", 3: "可以", 4: "变成", 11: "去", 12: "成就"`
  - mapping_reason: Verb phrase indicating achievement/becoming.

* target[5]: "자신의 운명을"
  - source_tokens: `18: "知命", 20: "命", 22: "命", 24: "招命"`
  - mapping_reason: The object "fate" referenced throughout the list.

* target[6]: "알고,"
  - source_tokens: `18: "知"`
  - mapping_reason: First verb in the list (know).

* target[7]: "이해하고,"
  - source_tokens: `19: "懂"`
  - mapping_reason: Second verb in the list (understand).

* target[8]: "활용하고,"
  - source_tokens: `21: "用"`
  - mapping_reason: Third verb in the list (use).

* target[9]: "더 나아가"
  - source_tokens: `23: "在"`
  - mapping_reason: Progressive/advancing connective.

* target[10]: "운명을"
  - source_tokens: `24: "命"`
  - mapping_reason: The object "fate" for the final verb.

* target[11]: "개척하는 것이죠."
  - source_tokens: `24: "招", 25: "喽"`
  - mapping_reason: Final verb (create/summon) and sentence-ending tone.

* target[12]: "다시 말해,"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说"`
  - mapping_reason: Discourse connective (in other words).

* target[13]: "화면 앞에"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的"`
  - mapping_reason: Locative phrase.

* target[14]: "계신 여러분."
  - source_tokens: `33: "各位", 34: "朋友"`
  - mapping_reason: Address term for the audience.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [0]},
  {"target_senseunit_id": 1, "source_token_ids": [1]},
  {"target_senseunit_id": 2, "source_token_ids": [5, 6, 7, 8, 9, 10]},
  {"target_senseunit_id": 3, "source_token_ids": [13, 14, 15, 16]},
  {"target_senseunit_id": 4, "source_token_ids": [2, 3, 4, 11, 12]},
  {"target_senseunit_id": 5, "source_token_ids": [18, 20, 22, 24]},
  {"target_senseunit_id": 6, "source_token_ids": [18]},
  {"target_senseunit_id": 7, "source_token_ids": [19]},
  {"target_senseunit_id": 8, "source_token_ids": [21]},
  {"target_senseunit_id": 9, "source_token_ids": [23]},
  {"target_senseunit_id": 10, "source_token_ids": [24]},
  {"target_senseunit_id": 11, "source_token_ids": [24, 25]},
  {"target_senseunit_id": 12, "source_token_ids": [26, 27, 28, 29]},
  {"target_senseunit_id": 13, "source_token_ids": [30, 31, 32]},
  {"target_senseunit_id": 14, "source_token_ids": [33, 34]}
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_Y4xRc2amPxY_W000024 ===

source:
- language: Chinese
- transcription: 就会消耗我们身体骨骼当中的矿物质，更多的靠物矿物质。所以呢，这个肥胖人往往都会有这种关节和软组织的问题，就是因为什么？就是消耗了太多的矿物质。
- source_tokens:
  0. 就
  1. 会
  2. 消耗
  3. 我们
  4. 身体
  5. 骨骼
  6. 当中
  7. 的
  8. 矿
  9. 物质，
  10. 更多
  11. 的
  12. 靠物
  13. 矿
  14. 物质。
  15. 所以
  16. 呢，
  17. 这
  18. 个
  19. 肥胖
  20. 人
  21. 往往
  22. 都会
  23. 有
  24. 这
  25. 种
  26. 关节
  27. 和
  28. 软
  29. 组织
  30. 的
  31. 问题，
  32. 就是
  33. 因为
  34. 什么？
  35. 就是
  36. 消耗
  37. 了
  38. 太多
  39. 的
  40. 矿
  41. 物质。

target:
- language: Japanese
- translation: 私たちの骨のミネラルを消費してしまいます。ミネラルに頼る部分が大きくなってしまうんです。だから、肥満の人は関節や軟部組織にトラブルが出やすいんです。なぜかというと、ミネラルを消費しすぎてしまうからです。
- target_sense_units:
  0. 私たちの
  1. 骨の
  2. ミネラルを
  3. 消費してしまいます。
  4. ミネラルに
  5. 頼る部分が
  6. 大きくなってしまうんです。
  7. だから、
  8. 肥満の人は
  9. 関節や軟部組織に
  10. トラブルが
  11. 出やすいんです。
  12. なぜかというと、
  13. ミネラルを
  14. 消費しすぎてしまう
  15. からです。

scratchpad:
* target[0]: "私たちの"
  - source_tokens: `3: "我们"`
  - mapping_reason: Possessive pronoun referring to the human body.
* target[1]: "骨の"
  - source_tokens: `5: "骨骼"`
  - mapping_reason: Anatomical location.
* target[2]: "ミネラルを"
  - source_tokens: `8: "矿", 9: "物质，"`
  - mapping_reason: Object of consumption.
* target[3]: "消費してしまいます。"
  - source_tokens: `0: "就", 1: "会", 2: "消耗"`
  - mapping_reason: Verb phrase indicating consumption.
* target[4]: "ミネラルに"
  - source_tokens: `13: "矿", 14: "物质。"`
  - mapping_reason: Subject of reliance.
* target[5]: "頼る部分が"
  - source_tokens: `10: "更多", 11: "的", 12: "靠物"`
  - mapping_reason: Dependence on minerals.
* target[6]: "大きくなってしまうんです。"
  - source_tokens: `10: "更多"`
  - mapping_reason: Amplifying the degree of dependence.
* target[7]: "だから、"
  - source_tokens: `15: "所以", 16: "呢，"`
  - mapping_reason: Discourse connective for consequence.
* target[8]: "肥満の人は"
  - source_tokens: `17: "这", 18: "个", 19: "肥胖", 20: "人"`
  - mapping_reason: Subject of the consequence.
* target[9]: "関節や軟部組織に"
  - source_tokens: `26: "关节", 27: "和", 28: "软", 29: "组织"`
  - mapping_reason: Affected body parts.
* target[10]: "トラブルが"
  - source_tokens: `31: "问题，"`
  - mapping_reason: The negative outcome.
* target[11]: "出やすいんです。"
  - source_tokens: `21: "往往", 22: "都会", 23: "有"`
  - mapping_reason: Tendency/frequency of occurrence.
* target[12]: "なぜかというと、"
  - source_tokens: `32: "就是", 33: "因为", 34: "什么？"`
  - mapping_reason: Rhetorical question introducing explanation.
* target[13]: "ミネラルを"
  - source_tokens: `40: "矿", 41: "物质。"`
  - mapping_reason: Object of excessive consumption.
* target[14]: "消費しすぎてしまう"
  - source_tokens: `36: "消耗", 37: "了", 38: "太多"`
  - mapping_reason: Excessive consumption action.
* target[15]: "からです。"
  - source_tokens: `33: "因为"`
  - mapping_reason: Causal explanation marker.

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>就会消耗我们</src> <tgt>私たちの</tgt>; start=1.00, end=2.00
2. <src><|wait|></src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>身体骨骼当中</src> <tgt>骨の</tgt>; start=3.00, end=4.00
4. <src>的矿物质，</src> <tgt>ミネラルを消費してしまいます。</tgt>; start=4.00, end=5.00
5. <src>更多的靠物矿物质。</src> <tgt>ミネラルに頼る部分が大きくなってしまうんです。</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>所以呢，</src> <tgt>だから、</tgt>; start=7.00, end=8.00
8. <src>这个肥胖人</src> <tgt>肥満の人は</tgt>; start=8.00, end=9.00
9. <src>往往都会有</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>这种关节</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src><|wait|></src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>和软组织的问题，</src> <tgt>関節や軟部組織にトラブルが出やすいんです。</tgt>; start=13.00, end=14.00
14. <src>就是因为什么？</src> <tgt>なぜかというと、</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>就是消耗了太多的矿物质。</src> <tgt>ミネラルを消費しすぎてしまうからです。</tgt>; start=16.00, end=16.84
```

- max_empty_window_count: 4


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[15]
  - verdict: mapping_error
  - reason: "The target unit 'からです。' functions as a causal explanation, which is explicitly provided by the source token '因为' (33), not '就是' (35)."
  - replace_source_tokens: 33: "因为"
  validation:
    scratchpad:
* target[0]: "私たちの"
  - source_tokens: `3: "我们"`
  - mapping_reason: Possessive pronoun referring to "us".
* target[1]: "骨の"
  - source_tokens: `5: "骨骼"`
  - mapping_reason: Noun specifying the location of the minerals.
* target[2]: "ミネラルを"
  - source_tokens: `8: "矿", 9: "物质，"`
  - mapping_reason: Object of the consumption.
* target[3]: "消費してしまいます。"
  - source_tokens: `0: "就", 1: "会", 2: "消耗"`
  - mapping_reason: Verbal action of consumption with modality.
* target[4]: "ミネラルに"
  - source_tokens: `13: "矿", 14: "物质。"`
  - mapping_reason: The substance being relied upon.
* target[5]: "頼る部分が"
  - source_tokens: `10: "更多", 11: "的", 12: "靠物"`
  - mapping_reason: The increased reliance/dependency.
* target[6]: "大きくなってしまうんです。"
  - source_tokens: `10: "更多"`
  - mapping_reason: The extent of the reliance.
* target[7]: "だから、"
  - source_tokens: `15: "所以"`
  - mapping_reason: Causal discourse marker.
* target[8]: "肥満の人は"
  - source_tokens: `17: "这", 18: "个", 19: "肥胖", 20: "人"`
  - mapping_reason: Subject of the sentence.
* target[9]: "関節や軟部組織に"
  - source_tokens: `26: "关节", 27: "和", 28: "软", 29: "组织"`
  - mapping_reason: Target areas affected by the condition.
* target[10]: "トラブルが"
  - source_tokens: `31: "问题，"`
  - mapping_reason: The issue/problem experienced.
* target[11]: "出やすいんです。"
  - source_tokens: `21: "往往", 22: "都会", 23: "有"`
  - mapping_reason: Verb/modal indicating likelihood of occurrence.
* target[12]: "なぜかというと、"
  - source_tokens: `32: "就是", 33: "因为", 34: "什么？"`
  - mapping_reason: Rhetorical question introducing the cause.
* target[13]: "ミネラルを"
  - source_tokens: `40: "矿", 41: "物质。"`
  - mapping_reason: Object of the final explanation.
* target[14]: "消費しすぎてしまう"
  - source_tokens: `36: "消耗", 37: "了", 38: "太多"`
  - mapping_reason: The excessive consumption.
* target[15]: "からです。"
  - source_tokens: `35: "就是"`
  - mapping_reason: Confirmation of the cause.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [3]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [8, 9]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [10, 11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [10]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [15]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [17, 18, 19, 20]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [31]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [21, 22, 23]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [32, 33, 34]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [40, 41]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [36, 37, 38]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [35]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_Yu84L6YIP6A_W000010 ===

source:
- language: Chinese
- transcription: 说，我当时我只是看到月轮，我就跟师傅熊老师嘛，是我的师傅，我就汇报。二师傅，我成了。他说你成了什么了？我说我看到一个大月亮了，亮亮的，你看啊，一堂光。他说你成了个屁，哈哈哈哈哈！他就跟我说话不客气啊，你那个叫成了。
- source_tokens:
  0. 说，
  1. 我
  2. 当时
  3. 我
  4. 只
  5. 是
  6. 看到
  7. 月轮，
  8. 我
  9. 就
  10. 跟
  11. 师傅
  12. 熊
  13. 老师
  14. 嘛，
  15. 是
  16. 我
  17. 的
  18. 师傅，
  19. 我
  20. 就
  21. 汇报。
  22. 二
  23. 师傅，
  24. 我
  25. 成
  26. 了。
  27. 他
  28. 说
  29. 你
  30. 成
  31. 了
  32. 什么
  33. 了？
  34. 我
  35. 说
  36. 我
  37. 看到
  38. 一
  39. 个
  40. 大
  41. 月
  42. 亮
  43. 了，
  44. 亮
  45. 亮
  46. 的，
  47. 你
  48. 看
  49. 啊，
  50. 一
  51. 堂
  52. 光。
  53. 他
  54. 说
  55. 你
  56. 成
  57. 了
  58. 个
  59. 屁，
  60. 哈哈哈哈哈！
  61. 他
  62. 就
  63. 跟
  64. 我
  65. 说话
  66. 不
  67. 客气
  68. 啊，
  69. 你
  70. 那
  71. 个
  72. 叫成
  73. 了。

target:
- language: English
- translation: So, at the time, I just saw the moon—the full moon—and I reported it to my master, Master Xiong. He's my master. I said, "Master, I've succeeded!" He asked, "Succeeded at what?" I said, "I saw a big moon, bright and shining, look, a whole hall of light." He said, "You've succeeded at nothing, my foot!" Hahahaha! He doesn't hold back when he talks to me. "You call that success?"
- target_sense_units:
  0. So, at the time,
  1. I just saw the moon—
  2. the full moon—
  3. and I reported it
  4. to my master,
  5. Master Xiong.
  6. He's my master.
  7. I said,"
  8. Master,
  9. I've succeeded!"
  10. He asked,"
  11. Succeeded at what?"
  12. I said,"
  13. I saw a big moon,
  14. bright and shining,
  15. look,
  16. a whole hall of light."
  17. He said,"
  18. You've succeeded at nothing,
  19. my foot!"
  20. Hahahaha!
  21. He doesn't hold back
  22. when he talks to me."
  23. You call that success?"

scratchpad:
* target[0]: "So, at the time,"
  - source_tokens: `0: "说，", 2: "当时"`
  - mapping_reason: Discourse marker "说" and temporal marker "当时".
* target[1]: "I just saw the moon—"
  - source_tokens: `1: "我", 3: "我", 4: "只", 5: "是", 6: "看到", 7: "月轮，"`
  - mapping_reason: Subject, adverbial "just", and verb "saw" with object "moon".
* target[2]: "the full moon—"
  - source_tokens: `7: "月轮，"`
  - mapping_reason: Clarification of "月轮".
* target[3]: "and I reported it"
  - source_tokens: `8: "我", 9: "就", 21: "汇报。"`
  - mapping_reason: Subject and verb "reported".
* target[4]: "to my master,"
  - source_tokens: `10: "跟", 11: "师傅"`
  - mapping_reason: Recipient of the report.
* target[5]: "Master Xiong."
  - source_tokens: `12: "熊", 13: "老师"`
  - mapping_reason: Name of the master.
* target[6]: "He's my master."
  - source_tokens: `15: "是", 16: "我", 17: "的", 18: "师傅，"`
  - mapping_reason: Affirmation of the relationship.
* target[7]: "I said,"
  - source_tokens: `19: "我", 20: "就"`
  - mapping_reason: Speaker introduction.
* target[8]: "Master,"
  - source_tokens: `23: "师傅，"`
  - mapping_reason: Address term.
* target[9]: "I've succeeded!"
  - source_tokens: `24: "我", 25: "成", 26: "了。"`
  - mapping_reason: Statement of success.
* target[10]: "He asked,"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Attribution of the question.
* target[11]: "Succeeded at what?"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了？"`
  - mapping_reason: Question about the success.
* target[12]: "I said,"
  - source_tokens: `34: "我", 35: "说"`
  - mapping_reason: Attribution of the response.
* target[13]: "I saw a big moon,"
  - source_tokens: `36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Description of the vision.
* target[14]: "bright and shining,"
  - source_tokens: `42: "亮", 43: "了，", 44: "亮", 45: "亮", 46: "的，"`
  - mapping_reason: Descriptors of the moon.
* target[15]: "look,"
  - source_tokens: `47: "你", 48: "看", 49: "啊，"`
  - mapping_reason: Imperative attention getter.
* target[16]: "a whole hall of light."
  - source_tokens: `50: "一", 51: "堂", 52: "光。"`
  - mapping_reason: Visual description.
* target[17]: "He said,"
  - source_tokens: `53: "他", 54: "说"`
  - mapping_reason: Attribution of the retort.
* target[18]: "You've succeeded at nothing,"
  - source_tokens: `55: "你", 56: "成", 57: "了", 58: "个", 59: "屁，"`
  - mapping_reason: Negation of success.
* target[19]: "my foot!"
  - source_tokens: `59: "屁，"`
  - mapping_reason: Expression of dismissal.
* target[20]: "Hahahaha!"
  - source_tokens: `60: "哈哈哈哈哈！"`
  - mapping_reason: Laughter.
* target[21]: "He doesn't hold back"
  - source_tokens: `61: "他", 62: "就", 63: "跟", 64: "我", 65: "说话", 66: "不", 67: "客气"`
  - mapping_reason: Characterization of his speech style.
* target[22]: "when he talks to me."
  - source_tokens: `63: "跟", 64: "我", 65: "说话", 68: "啊，"`
  - mapping_reason: Context of the speech style.
* target[23]: "You call that success?"
  - source_tokens: `69: "你", 70: "那", 71: "个", 72: "叫成", 73: "了。"`
  - mapping_reason: Rhetorical question about success.

result:
```html
0. <src>说，我当时</src> <tgt>So, at the time,</tgt>; start=0.00, end=1.00
1. <src>我只是看到</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>月轮，</src> <tgt>I just saw the moon— the full moon—</tgt>; start=2.00, end=3.00
3. <src>我就跟师傅</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>熊老师嘛，是我的</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>师傅，我就汇报。</src> <tgt>and I reported it to my master, Master Xiong. He's my master. I said,"</tgt>; start=5.00, end=6.00
6. <src>二师傅，</src> <tgt>Master,</tgt>; start=6.00, end=7.00
7. <src>我成了。他说你成了</src> <tgt>I've succeeded!" He asked,"</tgt>; start=7.00, end=8.00
8. <src>什么了？</src> <tgt>Succeeded at what?"</tgt>; start=8.00, end=9.00
9. <src>我说我看到一个</src> <tgt>I said,"</tgt>; start=9.00, end=10.00
10. <src>大月亮了，</src> <tgt>I saw a big moon,</tgt>; start=10.00, end=11.00
11. <src>亮亮的，你看</src> <tgt>bright and shining,</tgt>; start=11.00, end=12.00
12. <src>啊，</src> <tgt>look,</tgt>; start=12.00, end=13.00
13. <src>一堂光。他说</src> <tgt>a whole hall of light." He said,"</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>你成了个屁，</src> <tgt>You've succeeded at nothing, my foot!"</tgt>; start=15.00, end=16.00
16. <src>哈哈哈哈哈！他就跟我</src> <tgt>Hahahaha!</tgt>; start=16.00, end=17.00
17. <src>说话不客气</src> <tgt>He doesn't hold back</tgt>; start=17.00, end=18.00
18. <src>啊，</src> <tgt>when he talks to me."</tgt>; start=18.00, end=19.00
19. <src>你那个叫成了。</src> <tgt>You call that success?"</tgt>; start=19.00, end=19.80
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[8]
  - verdict: mapping_error
  - reason: "The source token '二' is not part of the title 'Master' and is likely extraneous to this mapping."
  - replace_source_tokens: 23: "师傅，"
  validation:
    scratchpad:
* target[0]: "So, at the time,"
  - source_tokens: `0: "说，", 2: "当时"`
  - mapping_reason: Discourse marker and temporal setting.
* target[1]: "I just saw the moon—"
  - source_tokens: `1: "我", 4: "只", 5: "是", 6: "看到", 7: "月轮，"`
  - mapping_reason: Subject, adverbial "just", and verb-object.
* target[2]: "the full moon—"
  - source_tokens: `7: "月轮，"`
  - mapping_reason: Clarification of "moon" as "full moon".
* target[3]: "and I reported it"
  - source_tokens: `8: "我", 9: "就", 21: "汇报。"`
  - mapping_reason: Subject and verb of reporting.
* target[4]: "to my master,"
  - source_tokens: `10: "跟", 11: "师傅"`
  - mapping_reason: Recipient of report.
* target[5]: "Master Xiong."
  - source_tokens: `12: "熊", 13: "老师"`
  - mapping_reason: Name of the master.
* target[6]: "He's my master."
  - source_tokens: `15: "是", 16: "我", 17: "的", 18: "师傅，"`
  - mapping_reason: Identity statement.
* target[7]: "I said,"
  - source_tokens: `19: "我", 28: "说"`
  - mapping_reason: Speech attribution.
* target[8]: "Master,"
  - source_tokens: `22: "二", 23: "师傅，"`
  - mapping_reason: Address term.
* target[9]: "I've succeeded!""
  - source_tokens: `24: "我", 25: "成", 26: "了。"`
  - mapping_reason: Statement of success.
* target[10]: "He asked,"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Speech attribution.
* target[11]: "Succeeded at what?""
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了？"`
  - mapping_reason: Question about success.
* target[12]: "I said,""
  - source_tokens: `34: "我", 35: "说"`
  - mapping_reason: Speech attribution.
* target[13]: "I saw a big moon,"
  - source_tokens: `36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Description of vision.
* target[14]: "bright and shining,"
  - source_tokens: `42: "亮", 44: "亮", 45: "亮", 46: "的，"`
  - mapping_reason: Adjectival description.
* target[15]: "look,"
  - source_tokens: `47: "你", 48: "看", 49: "啊，"`
  - mapping_reason: Attention-getting marker.
* target[16]: "a whole hall of light.""
  - source_tokens: `50: "一", 51: "堂", 52: "光。"`
  - mapping_reason: Metaphorical description.
* target[17]: "He said,""
  - source_tokens: `53: "他", 54: "说"`
  - mapping_reason: Speech attribution.
* target[18]: "You've succeeded at nothing,"
  - source_tokens: `55: "你", 56: "成", 57: "了", 58: "个"`
  - mapping_reason: Negation of success.
* target[19]: "my foot!""
  - source_tokens: `59: "屁，"`
  - mapping_reason: Expletive/dismissal.
* target[20]: "Hahahaha!"
  - source_tokens: `60: "哈哈哈哈哈！"`
  - mapping_reason: Laughter.
* target[21]: "He doesn't hold back"
  - source_tokens: `61: "他", 62: "就", 66: "不", 67: "客气"`
  - mapping_reason: Description of manner.
* target[22]: "when he talks to me.""
  - source_tokens: `63: "跟", 64: "我", 65: "说话", 68: "啊，"`
  - mapping_reason: Context of speaking.
* target[23]: "You call that success?""
  - source_tokens: `69: "你", 70: "那", 71: "个", 72: "叫成", 73: "了。"`
  - mapping_reason: Rhetorical question about success.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [0, 2]},
  {"target_senseunit_id": 1, "source_token_ids": [1, 4, 5, 6, 7]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [8, 9, 21]},
  {"target_senseunit_id": 4, "source_token_ids": [10, 11]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 6, "source_token_ids": [15, 16, 17, 18]},
  {"target_senseunit_id": 7, "source_token_ids": [19, 28]},
  {"target_senseunit_id": 8, "source_token_ids": [22, 23]},
  {"target_senseunit_id": 9, "source_token_ids": [24, 25, 26]},
  {"target_senseunit_id": 10, "source_token_ids": [27, 28]},
  {"target_senseunit_id": 11, "source_token_ids": [29, 30, 31, 32, 33]},
  {"target_senseunit_id": 12, "source_token_ids": [34, 35]},
  {"target_senseunit_id": 13, "source_token_ids": [36, 37, 38, 39, 40, 41]},
  {"target_senseunit_id": 14, "source_token_ids": [42, 44, 45, 46]},
  {"target_senseunit_id": 15, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 16, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 17, "source_token_ids": [53, 54]},
  {"target_senseunit_id": 18, "source_token_ids": [55, 56, 57, 58]},
  {"target_senseunit_id": 19, "source_token_ids": [59]},
  {"target_senseunit_id": 20, "source_token_ids": [60]},
  {"target_senseunit_id": 21, "source_token_ids": [61, 62, 66, 67]},
  {"target_senseunit_id": 22, "source_token_ids": [63, 64, 65, 68]},
  {"target_senseunit_id": 23, "source_token_ids": [69, 70, 71, 72, 73]}
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_Q0a8pjeI4HA_W000054 ===

source:
- language: Chinese
- transcription: 那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命、在招命喽。换句话说，荧幕前的各位朋友。
- source_tokens:
  0. 那
  1. 你
  2. 就
  3. 可以
  4. 变成
  5. 那百
  6. 分
  7. 之
  8. 二十
  9. 的
  10. 人，
  11. 去
  12. 成就
  13. 不
  14. 一样
  15. 的
  16. 人生，
  17. 可以
  18. 知命、
  19. 懂
  20. 命、
  21. 用
  22. 命、
  23. 在
  24. 招命
  25. 喽。
  26. 换
  27. 句
  28. 话
  29. 说，
  30. 荧幕
  31. 前
  32. 的
  33. 各位
  34. 朋友。

target:
- language: Japanese
- translation: そうすれば、あなたは20%の人になり、異なる人生を切り開くんです。運命を知って、理解して、活用して、自ら創り出していくんです。つまり、画面の前の皆さん。
- target_sense_units:
  0. そうすれば、
  1. あなたは
  2. 20%の人に
  3. なり、
  4. 異なる人生を
  5. 切り開くんです。
  6. 運命を
  7. 知って、
  8. 理解して、
  9. 活用して、
  10. 自ら創り出していくんです。
  11. つまり、
  12. 画面の前の皆さん。

scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 1: "你", 2: "就"`
  - mapping_reason: Connective structure "那...就" indicating "if so/then".
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject pronoun.
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Object noun phrase representing the specific group.
* target[3]: "なり、"
  - source_tokens: `4: "变成"`
  - mapping_reason: Verb meaning to become.
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: Object noun phrase "different life".
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: Verb phrase "to achieve/carve out".
* target[6]: "運命を"
  - source_tokens: `18: "知命、", 20: "命、", 22: "命、", 24: "招命"`
  - mapping_reason: Shared object "fate" implied by the following four verb sense units.
* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: Verb "to know".
* target[8]: "理解して、"
  - source_tokens: `19: "懂"`
  - mapping_reason: Verb "to understand".
* target[9]: "活用して、"
  - source_tokens: `21: "用"`
  - mapping_reason: Verb "to use/utilize".
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: Verb phrase "to create/summon fate".
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse connective "in other words".
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: Addressee phrase.

result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

errors:
* target[6]
  - verdict: mapping_error
  - reason: "The target sense unit '運命を' is a single noun phrase representing the object of the following verbs; mapping it to all four occurrences of the character '命' is redundant and structurally incorrect."
  - replace_source_tokens: 20: "命、"

attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[0]
  - verdict: mapping_error
  - reason: "The source token '你' (you) is the subject of the next target unit and does not belong to the 'so/then' discourse connector."
  - replace_source_tokens: 0: "那", 2: "就"

* target[6]
  - verdict: mapping_error
  - reason: "The target unit '運命を' represents the shared object of the following verbs. Mapping the entire source verb phrases to the target noun is semantically imprecise; the mapping should ideally point to the constituent '命' tokens if possible, or be acknowledged as an anchor for the subsequent verbs."
  - replace_source_tokens: 18: "知命、", 20: "命、", 22: "命、", 24: "招命"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 1: "你", 2: "就"`
  - mapping_reason: "那 (then) + 你 (you) + 就 (just/then) form the conditional consequence."
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: "Subject pronoun."
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: "Numerical quantifier phrase and noun."
* target[3]: "なり、"
  - source_tokens: `4: "变成"`
  - mapping_reason: "Verb of becoming."
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: "Object of the achievement."
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: "Action of achieving/creating."
* target[6]: "運命を"
  - source_tokens: `18: "命、", 20: "命、", 22: "命、", 24: "命"`
  - mapping_reason: "The object 'fate' (命) is implied in each verb phrase."
* target[7]: "知って、"
  - source_tokens: `17: "可以", 18: "知命、"`
  - mapping_reason: "Verb 'to know' (知)."
* target[8]: "理解して、"
  - source_tokens: `19: "懂"`
  - mapping_reason: "Verb 'to understand' (懂)."
* target[9]: "活用して、"
  - source_tokens: `21: "用"`
  - mapping_reason: "Verb 'to use' (用)."
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: "Verb 'to summon/create fate' (招命) with modal tone."
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: "Discourse marker 'in other words'."
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: "Address to audience."
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [17, 18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

- retry: 1/5
  status: failed_after_response
  reason: * target[6]
  - verdict: mapping_error
  - reason: "The target sense unit '運命を' functions as the shared object for the subsequent verbs. Assigning all '命' tokens here is redundant and logically incorrect as they are anchors for the actions '知', '懂', '用', '招'."
  - replace_source_tokens: 18: "知命、"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 2: "就"`
  - mapping_reason: "那" (so) and "就" (then/consequence) function as the discourse marker for the conditional result.

* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: "你" is the subject (you).

* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Direct translation of "the 20% of people".

* target[3]: "なり、"
  - source_tokens: `3: "可以", 4: "变成"`
  - mapping_reason: "变成" (become) with the potential auxiliary "可以".

* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: "不一样的人生" (different life).

* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: "去成就" (to achieve/open up).

* target[6]: "運命を"
  - source_tokens: `18: "知命、", 20: "命、", 22: "命、", 24: "招命"`
  - mapping_reason: The object "命" is shared across the four verbs in the source.

* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: "知" (know).

* target[8]: "理解して、"
  - source_tokens: `19: "懂", 20: "命、"`
  - mapping_reason: "懂" (understand).

* target[9]: "活用して、"
  - source_tokens: `21: "用", 22: "命、"`
  - mapping_reason: "用" (use/utilize).

* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: "招命" (create/invite destiny) and the sentence-final particle.

* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: "换句话说" (in other words/in short).

* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: "荧幕前的各位朋友" (friends in front of the screen).
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [3, 4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19, 20]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21, 22]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

- retry: 2/5
  status: failed_after_response
  reason: * target[6]
  - verdict: mapping_error
  - reason: "The target unit '運命を' acts as a shared object for the subsequent verbs. Mapping all occurrences of '命' (18, 20, 22, 24) to this single target unit is incorrect; it should be anchored to the first instance of '命' (in '知命') which introduces the object."
  - replace_source_tokens: 18: "知命、"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 2: "就"`
  - mapping_reason: "Connective discourse marker derived from 那 and 就."
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: "Subject pronoun."
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: "Numerical quantifier phrase and noun."
* target[3]: "なり、"
  - source_tokens: `3: "可以", 4: "变成"`
  - mapping_reason: "Verb phrase 'become'."
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: "Adjective and noun object."
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: "Verb 'achieve/open up'."
* target[6]: "運命を"
  - source_tokens: `18: "知命、", 20: "命、", 22: "命、", 24: "招命"`
  - mapping_reason: "Shared object '命' (fate) for the following sequence of verbs."
* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: "Verb 'to know'."
* target[8]: "理解して、"
  - source_tokens: `19: "懂"`
  - mapping_reason: "Verb 'to understand'."
* target[9]: "活用して、"
  - source_tokens: `21: "用"`
  - mapping_reason: "Verb 'to use/utilize'."
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: "Verb 'to create/recruit fate' with aspectual marker."
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: "Discourse connective 'in other words'."
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: "Addressee noun phrase."
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [3, 4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

- retry: 3/5
  status: failed_after_response
  reason: * target[0]
  - verdict: mapping_error
  - reason: "The source token 1 '你' is the subject of the following clause and is not part of the conditional '那...就' mapping."
  - replace_source_tokens: 0: "那", 2: "就"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 1: "你", 2: "就"`
  - mapping_reason: Discourse connective and subject/condition marker.
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject reference.
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Quantifier and noun phrase.
* target[3]: "なり、"
  - source_tokens: `4: "变成"`
  - mapping_reason: Verb of transformation.
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: Object noun phrase.
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: Verb phrase for achievement.
* target[6]: "運命を"
  - source_tokens: `18: "知命、"`
  - mapping_reason: Object of the following sequence of verbs.
* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: First verb in the sequence.
* target[8]: "理解して、"
  - source_tokens: `19: "懂", 20: "命、"`
  - mapping_reason: Second verb in the sequence.
* target[9]: "活用して、"
  - source_tokens: `21: "用", 22: "命、"`
  - mapping_reason: Third verb in the sequence.
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: Final verb phrase in the sequence.
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse marker for restatement.
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: Addressee noun phrase.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19, 20]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21, 22]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

- retry: 4/5
  status: failed_after_response
  reason: * target[6]
  - verdict: mapping_error
  - reason: "The target unit '運命を' acts as the shared object for the subsequent verbs. Mapping it to all four compound verb tokens is redundant and incorrect. It should be anchored to the '命' component found in the source verbs."
  - replace_source_tokens: 18: "知命、"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 2: "就"`
  - mapping_reason: "那...就" forms the conditional structure "if so/then".
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject pronoun.
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Quantifier and noun phrase.
* target[3]: "なり、"
  - source_tokens: `3: "可以", 4: "变成"`
  - mapping_reason: Modal verb and main verb "become".
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: Adjectival phrase modifying noun.
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: Main verb phrase "achieve/open up".
* target[6]: "運命を"
  - source_tokens: `18: "知命、", 20: "命、", 22: "命、", 24: "招命"`
  - mapping_reason: Object of the following verbs.
* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: Verb "know".
* target[8]: "理解して、"
  - source_tokens: `19: "懂", 20: "命、"`
  - mapping_reason: Verb "understand".
* target[9]: "活用して、"
  - source_tokens: `21: "用", 22: "命、"`
  - mapping_reason: Verb "use/apply".
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: Verb "create/summon fate" and sentence particle.
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse connective "in other words".
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: Noun phrase referring to the audience.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [3, 4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19, 20]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21, 22]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

- retry: 5/5
  status: failed_after_response
  reason: * target[6]
  - verdict: mapping_error
  - reason: "The target sense unit '運命を' is a single noun phrase representing the object of the following verbs; mapping it to all four occurrences of the character '命' is redundant and structurally incorrect."
  - replace_source_tokens: 20: "命、"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 1: "你", 2: "就"`
  - mapping_reason: Connective structure "那...就" indicating "if so/then".
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject pronoun.
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Object noun phrase representing the specific group.
* target[3]: "なり、"
  - source_tokens: `4: "变成"`
  - mapping_reason: Verb meaning to become.
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: Object noun phrase "different life".
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: Verb phrase "to achieve/carve out".
* target[6]: "運命を"
  - source_tokens: `18: "知命、", 20: "命、", 22: "命、", 24: "招命"`
  - mapping_reason: Shared object "fate" implied by the following four verb sense units.
* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: Verb "to know".
* target[8]: "理解して、"
  - source_tokens: `19: "懂"`
  - mapping_reason: Verb "to understand".
* target[9]: "活用して、"
  - source_tokens: `21: "用"`
  - mapping_reason: Verb "to use/utilize".
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: Verb phrase "to create/summon fate".
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse connective "in other words".
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: Addressee phrase.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

---
=== ZH_Yu84L6YIP6A_W000010 ===

source:
- language: Chinese
- transcription: 说，我当时我只是看到月轮，我就跟师傅熊老师嘛，是我的师傅，我就汇报。二师傅，我成了。他说你成了什么了？我说我看到一个大月亮了，亮亮的，你看啊，一堂光。他说你成了个屁，哈哈哈哈哈！他就跟我说话不客气啊，你那个叫成了。
- source_tokens:
  0. 说，
  1. 我
  2. 当时
  3. 我
  4. 只
  5. 是
  6. 看到
  7. 月轮，
  8. 我
  9. 就
  10. 跟
  11. 师傅
  12. 熊
  13. 老师
  14. 嘛，
  15. 是
  16. 我
  17. 的
  18. 师傅，
  19. 我
  20. 就
  21. 汇报。
  22. 二
  23. 师傅，
  24. 我
  25. 成
  26. 了。
  27. 他
  28. 说
  29. 你
  30. 成
  31. 了
  32. 什么
  33. 了？
  34. 我
  35. 说
  36. 我
  37. 看到
  38. 一
  39. 个
  40. 大
  41. 月
  42. 亮
  43. 了，
  44. 亮
  45. 亮
  46. 的，
  47. 你
  48. 看
  49. 啊，
  50. 一
  51. 堂
  52. 光。
  53. 他
  54. 说
  55. 你
  56. 成
  57. 了
  58. 个
  59. 屁，
  60. 哈哈哈哈哈！
  61. 他
  62. 就
  63. 跟
  64. 我
  65. 说话
  66. 不
  67. 客气
  68. 啊，
  69. 你
  70. 那
  71. 个
  72. 叫成
  73. 了。

target:
- language: Japanese
- translation: その時、月輪が見えたんで、師匠の熊先生に報告したんです。「師匠、できました！」って。そしたら師匠が「何ができたんだ？」って聞くから、「大きな月が見えたんです。キラキラしてて、見てください、光に満ちてるんです！」って答えたんです。そしたら師匠が「できたも何も、ちゃんちゃらおかしいわ！」って大笑いして。私に対してはいつも遠慮がないんです。「そんなんじゃ、できたうちに入らへんぞ」って。
- target_sense_units:
  0. その時、
  1. 月輪が
  2. 見えたんで、
  3. 師匠の熊先生に
  4. 報告したんです。
  5. 「師匠、
  6. できました！」
  7. って。
  8. そしたら
  9. 師匠が
  10. 「何ができたんだ？」
  11. って
  12. 聞くから、
  13. 「大きな月が見えたんです。
  14. キラキラしてて、
  15. 見てください、
  16. 光に満ちてるんです！」
  17. って
  18. 答えたんです。
  19. そしたら
  20. 師匠が
  21. 「できたも何も、
  22. ちゃんちゃらおかしいわ！」
  23. って
  24. 大笑いして。
  25. 私に対しては
  26. いつも
  27. 遠慮がないんです。
  28. 「そんなんじゃ、
  29. できたうちに
  30. 入らへんぞ」
  31. って。

scratchpad:
* target[0]: "その時、"
  - source_tokens: `2: "当时"`
  - mapping_reason: Temporal marker.
* target[1]: "月輪が"
  - source_tokens: `7: "月轮，"`
  - mapping_reason: Object of vision.
* target[2]: "見えたんで、"
  - source_tokens: `4: "只", 5: "是", 6: "看到"`
  - mapping_reason: Action of seeing.
* target[3]: "師匠の熊先生に"
  - source_tokens: `11: "师傅", 12: "熊", 13: "老师"`
  - mapping_reason: Recipient of report (Master Xiong).
* target[4]: "報告したんです。"
  - source_tokens: `21: "汇报。"`
  - mapping_reason: Action of reporting.
* target[5]: "「師匠、"
  - source_tokens: `23: "师傅"`
  - mapping_reason: Direct address to Master.
* target[6]: "できました！」"
  - source_tokens: `25: "成", 26: "了。"`
  - mapping_reason: Achievement claim.
* target[7]: "って。"
  - source_tokens: `0: "说，"`
  - mapping_reason: Discourse marker for quotation.
* target[8]: "そしたら"
  - source_tokens: `9: "就"`
  - mapping_reason: Sequential discourse connector.
* target[9]: "師匠が"
  - source_tokens: `27: "他"`
  - mapping_reason: Subject of the response (Master).
* target[10]: "「何ができたんだ？」"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了？"`
  - mapping_reason: Question about the achievement.
* target[11]: "って"
  - source_tokens: `28: "说"`
  - mapping_reason: Verb of saying.
* target[12]: "聞くから、"
  - source_tokens: `28: "说"`
  - mapping_reason: Verb of asking/saying.
* target[13]: "「大きな月が見えたんです。"
  - source_tokens: `36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Description of vision.
* target[14]: "キラキラしてて、"
  - source_tokens: `44: "亮", 45: "亮"`
  - mapping_reason: Description of light.
* target[15]: "見てください、"
  - source_tokens: `47: "你", 48: "看"`
  - mapping_reason: Directing attention.
* target[16]: "光に満ちてるんです！」"
  - source_tokens: `50: "一", 51: "堂", 52: "光。"`
  - mapping_reason: Description of light.
* target[17]: "って"
  - source_tokens: `35: "说"`
  - mapping_reason: Discourse marker for quotation.
* target[18]: "答えたんです。"
  - source_tokens: `35: "说"`
  - mapping_reason: Verb of answering.
* target[19]: "そしたら"
  - source_tokens: `53: "他"`
  - mapping_reason: Sequential discourse connector.
* target[20]: "師匠が"
  - source_tokens: `53: "他"`
  - mapping_reason: Subject of the response.
* target[21]: "「できたも何も、"
  - source_tokens: `55: "你", 56: "成", 57: "了"`
  - mapping_reason: Dismissive reference to achievement.
* target[22]: "ちゃんちゃらおかしいわ！」"
  - source_tokens: `58: "个", 59: "屁"`
  - mapping_reason: Dismissive slang/idiom.
* target[23]: "って"
  - source_tokens: `54: "说"`
  - mapping_reason: Discourse marker for quotation.
* target[24]: "大笑いして。"
  - source_tokens: `60: "哈哈哈哈哈！"`
  - mapping_reason: Action of laughing.
* target[25]: "私に対しては"
  - source_tokens: `64: "我"`
  - mapping_reason: Reference to self.
* target[26]: "いつも"
  - source_tokens: `62: "就"`
  - mapping_reason: Frequency/habitual marker.
* target[27]: "遠慮がないんです。"
  - source_tokens: `66: "不", 67: "客气"`
  - mapping_reason: Description of the master's attitude.
* target[28]: "「そんなんじゃ、"
  - source_tokens: `69: "你", 70: "那", 71: "个"`
  - mapping_reason: Reference to previous claim.
* target[29]: "できたうちに"
  - source_tokens: `72: "叫成"`
  - mapping_reason: Reference to achievement.
* target[30]: "入らへんぞ」"
  - source_tokens: `73: "了。"`
  - mapping_reason: Negation of status.
* target[31]: "って。"
  - source_tokens: `65: "说话"`
  - mapping_reason: Discourse marker for final quote.

result:
```html
0. <src>说，我当时</src> <tgt>その時、</tgt>; start=0.00, end=1.00
1. <src>我只是看到</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>月轮，</src> <tgt>月輪が見えたんで、</tgt>; start=2.00, end=3.00
3. <src>我就跟师傅</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>熊老师嘛，是我的</src> <tgt>師匠の熊先生に</tgt>; start=4.00, end=5.00
5. <src>师傅，我就汇报。</src> <tgt>報告したんです。</tgt>; start=5.00, end=6.00
6. <src>二师傅，</src> <tgt>「師匠、</tgt>; start=6.00, end=7.00
7. <src>我成了。他说你成了</src> <tgt>できました！」って。そしたら師匠が</tgt>; start=7.00, end=8.00
8. <src>什么了？</src> <tgt>「何ができたんだ？」って聞くから、</tgt>; start=8.00, end=9.00
9. <src>我说我看到一个</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>大月亮了，</src> <tgt>「大きな月が見えたんです。</tgt>; start=10.00, end=11.00
11. <src>亮亮的，你看</src> <tgt>キラキラしてて、見てください、</tgt>; start=11.00, end=12.00
12. <src>啊，</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>一堂光。他说</src> <tgt>光に満ちてるんです！」って答えたんです。そしたら師匠が</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>你成了个屁，</src> <tgt>「できたも何も、ちゃんちゃらおかしいわ！」って</tgt>; start=15.00, end=16.00
16. <src>哈哈哈哈哈！他就跟我</src> <tgt>大笑いして。私に対してはいつも</tgt>; start=16.00, end=17.00
17. <src>说话不客气</src> <tgt>遠慮がないんです。</tgt>; start=17.00, end=18.00
18. <src>啊，</src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>你那个叫成了。</src> <tgt>「そんなんじゃ、できたうちに入らへんぞ」って。</tgt>; start=19.00, end=19.80
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[9]
  - verdict: mapping_error
  - reason: "The source token '他' (27) is a pronoun, whereas '師匠' (master) is the explicit noun. The correct source tokens for '師匠' are the ones identifying the master."
  - replace_source_tokens: 11: "师傅", 12: "熊", 13: "老师"

* target[31]
  - verdict: mapping_error
  - reason: "The target unit 'って。' is a quotative particle closing the preceding direct speech, not a translation of '说话'. It should be anchored to the end of the speech segment."
  - replace_source_tokens: 73: "了。"
  validation:
    scratchpad:
* target[0]: "その時、"
  - source_tokens: `2: "当时"`
  - mapping_reason: Time marker.
* target[1]: "月輪が"
  - source_tokens: `7: "月轮，"`
  - mapping_reason: Object of vision.
* target[2]: "見えたんで、"
  - source_tokens: `4: "只", 5: "是", 6: "看到"`
  - mapping_reason: Action of seeing.
* target[3]: "師匠の熊先生に"
  - source_tokens: `10: "跟", 11: "师傅", 12: "熊", 13: "老师"`
  - mapping_reason: Recipient of report.
* target[4]: "報告したんです。"
  - source_tokens: `21: "汇报。"`
  - mapping_reason: Action of reporting.
* target[5]: "「師匠、"
  - source_tokens: `23: "师傅，"`
  - mapping_reason: Address term.
* target[6]: "できました！」"
  - source_tokens: `25: "成", 26: "了。"`
  - mapping_reason: Status report.
* target[7]: "って。"
  - source_tokens: `0: "说，"`
  - mapping_reason: Speech marker.
* target[8]: "そしたら"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Discourse progression.
* target[9]: "師匠が"
  - source_tokens: `27: "他"`
  - mapping_reason: Speaker reference.
* target[10]: "「何ができたんだ？」"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了？"`
  - mapping_reason: Question about state.
* target[11]: "って"
  - source_tokens: `28: "说"`
  - mapping_reason: Speech marker.
* target[12]: "聞くから、"
  - source_tokens: `28: "说"`
  - mapping_reason: Speech marker.
* target[13]: "「大きな月が見えたんです。"
  - source_tokens: `34: "我", 35: "说", 36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Content of response.
* target[14]: "キラキラしてて、"
  - source_tokens: `44: "亮", 45: "亮", 46: "的，"`
  - mapping_reason: Description of appearance.
* target[15]: "見てください、"
  - source_tokens: `47: "你", 48: "看", 49: "啊，"`
  - mapping_reason: Directing attention.
* target[16]: "光に満ちてるんです！」"
  - source_tokens: `50: "一", 51: "堂", 52: "光。"`
  - mapping_reason: Description of appearance.
* target[17]: "って"
  - source_tokens: `35: "说"`
  - mapping_reason: Speech marker.
* target[18]: "答えたんです。"
  - source_tokens: `35: "说"`
  - mapping_reason: Speech marker.
* target[19]: "そしたら"
  - source_tokens: `53: "他", 54: "说"`
  - mapping_reason: Discourse progression.
* target[20]: "師匠が"
  - source_tokens: `53: "他"`
  - mapping_reason: Speaker reference.
* target[21]: "「できたも何も、"
  - source_tokens: `55: "你", 56: "成", 57: "了"`
  - mapping_reason: Referring back to "cheng le".
* target[22]: "ちゃんちゃらおかしいわ！」"
  - source_tokens: `58: "个", 59: "屁，"`
  - mapping_reason: Dismissive evaluation.
* target[23]: "って"
  - source_tokens: `54: "说"`
  - mapping_reason: Speech marker.
* target[24]: "大笑いして。"
  - source_tokens: `60: "哈哈哈哈哈！"`
  - mapping_reason: Reaction.
* target[25]: "私に対しては"
  - source_tokens: `64: "我"`
  - mapping_reason: Target of behavior.
* target[26]: "いつも"
  - source_tokens: `62: "就"`
  - mapping_reason: Habitual marker.
* target[27]: "遠慮がないんです。"
  - source_tokens: `66: "不", 67: "客气", 68: "啊，"`
  - mapping_reason: Characterization of behavior.
* target[28]: "「そんなんじゃ、"
  - source_tokens: `69: "你", 70: "那", 71: "个"`
  - mapping_reason: Referring to state.
* target[29]: "できたうちに"
  - source_tokens: `72: "叫成", 73: "了。"`
  - mapping_reason: Condition for success.
* target[30]: "入らへんぞ」"
  - source_tokens: `72: "叫成", 73: "了。"`
  - mapping_reason: Negative evaluation of success.
* target[31]: "って。"
  - source_tokens: `65: "说话"`
  - mapping_reason: Speech marker.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [2]},
  {"target_senseunit_id": 1, "source_token_ids": [7]},
  {"target_senseunit_id": 2, "source_token_ids": [4, 5, 6]},
  {"target_senseunit_id": 3, "source_token_ids": [10, 11, 12, 13]},
  {"target_senseunit_id": 4, "source_token_ids": [21]},
  {"target_senseunit_id": 5, "source_token_ids": [23]},
  {"target_senseunit_id": 6, "source_token_ids": [25, 26]},
  {"target_senseunit_id": 7, "source_token_ids": [0]},
  {"target_senseunit_id": 8, "source_token_ids": [27, 28]},
  {"target_senseunit_id": 9, "source_token_ids": [27]},
  {"target_senseunit_id": 10, "source_token_ids": [29, 30, 31, 32, 33]},
  {"target_senseunit_id": 11, "source_token_ids": [28]},
  {"target_senseunit_id": 12, "source_token_ids": [28]},
  {"target_senseunit_id": 13, "source_token_ids": [34, 35, 36, 37, 38, 39, 40, 41]},
  {"target_senseunit_id": 14, "source_token_ids": [44, 45, 46]},
  {"target_senseunit_id": 15, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 16, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 17, "source_token_ids": [35]},
  {"target_senseunit_id": 18, "source_token_ids": [35]},
  {"target_senseunit_id": 19, "source_token_ids": [53, 54]},
  {"target_senseunit_id": 20, "source_token_ids": [53]},
  {"target_senseunit_id": 21, "source_token_ids": [55, 56, 57]},
  {"target_senseunit_id": 22, "source_token_ids": [58, 59]},
  {"target_senseunit_id": 23, "source_token_ids": [54]},
  {"target_senseunit_id": 24, "source_token_ids": [60]},
  {"target_senseunit_id": 25, "source_token_ids": [64]},
  {"target_senseunit_id": 26, "source_token_ids": [62]},
  {"target_senseunit_id": 27, "source_token_ids": [66, 67, 68]},
  {"target_senseunit_id": 28, "source_token_ids": [69, 70, 71]},
  {"target_senseunit_id": 29, "source_token_ids": [72, 73]},
  {"target_senseunit_id": 30, "source_token_ids": [72, 73]},
  {"target_senseunit_id": 31, "source_token_ids": [65]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[8]
  - verdict: mapping_error
  - reason: "The target sense unit 'そしたら' acts as a discourse connector following the teacher's reaction, not a translation of the reporting verb '说'. It is better anchored by the subject and verb indicating the transition to the next speaker's turn."
  - replace_source_tokens: 27: "他", 28: "说"
  validation:
    scratchpad:
* target[0]: "その時、"
  - source_tokens: `2: "当时"`
  - mapping_reason: Time marker.
* target[1]: "月輪が"
  - source_tokens: `7: "月轮，"`
  - mapping_reason: Object of vision.
* target[2]: "見えたんで、"
  - source_tokens: `4: "只", 5: "是", 6: "看到"`
  - mapping_reason: Verb of vision and causal connective.
* target[3]: "師匠の熊先生に"
  - source_tokens: `11: "师傅", 12: "熊", 13: "老师"`
  - mapping_reason: Indirect object (the master).
* target[4]: "報告したんです。"
  - source_tokens: `21: "汇报。"`
  - mapping_reason: Action of reporting.
* target[5]: "「師匠、"
  - source_tokens: `23: "师傅，"`
  - mapping_reason: Address term.
* target[6]: "できました！」"
  - source_tokens: `25: "成", 26: "了。"`
  - mapping_reason: Achievement state.
* target[7]: "って。"
  - source_tokens: `28: "说"`
  - mapping_reason: Quotative marker for speech.
* target[8]: "そしたら"
  - source_tokens: `28: "说"`
  - mapping_reason: Discourse connective linking the response.
* target[9]: "師匠が"
  - source_tokens: `27: "他"`
  - mapping_reason: Subject of the response (the master).
* target[10]: "「何ができたんだ？」"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了？"`
  - mapping_reason: Question about the achievement.
* target[11]: "って"
  - source_tokens: `28: "说"`
  - mapping_reason: Quotative marker.
* target[12]: "聞くから、"
  - source_tokens: `35: "说"`
  - mapping_reason: Connective indicating the response to the question.
* target[13]: "「大きな月が見えたんです。"
  - source_tokens: `36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月", 42: "亮", 43: "了，"`
  - mapping_reason: Description of the vision.
* target[14]: "キラキラしてて、"
  - source_tokens: `44: "亮", 45: "亮", 46: "的，"`
  - mapping_reason: Appearance description.
* target[15]: "見てください、"
  - source_tokens: `47: "你", 48: "看", 49: "啊，"`
  - mapping_reason: Imperative to look.
* target[16]: "光に満ちてるんです！」"
  - source_tokens: `50: "一", 51: "堂", 52: "光。"`
  - mapping_reason: Description of light.
* target[17]: "って"
  - source_tokens: `54: "说"`
  - mapping_reason: Quotative marker.
* target[18]: "答えたんです。"
  - source_tokens: `35: "说"`
  - mapping_reason: Verb of answering.
* target[19]: "そしたら"
  - source_tokens: `53: "他"`
  - mapping_reason: Discourse connective.
* target[20]: "師匠が"
  - source_tokens: `53: "他"`
  - mapping_reason: Subject of the retort.
* target[21]: "「できたも何も、"
  - source_tokens: `56: "成", 57: "了"`
  - mapping_reason: Negation of achievement.
* target[22]: "ちゃんちゃらおかしいわ！」"
  - source_tokens: `58: "个", 59: "屁，"`
  - mapping_reason: Dismissive retort.
* target[23]: "って"
  - source_tokens: `54: "说"`
  - mapping_reason: Quotative marker.
* target[24]: "大笑いして。"
  - source_tokens: `60: "哈哈哈哈哈！"`
  - mapping_reason: Laughter.
* target[25]: "私に対しては"
  - source_tokens: `64: "我"`
  - mapping_reason: Target of the master's behavior.
* target[26]: "いつも"
  - source_tokens: `62: "就"`
  - mapping_reason: Adverbial frequency/manner.
* target[27]: "遠慮がないんです。"
  - source_tokens: `65: "说话", 66: "不", 67: "客气", 68: "啊"`
  - mapping_reason: Description of the master's manner.
* target[28]: "「そんなんじゃ、"
  - source_tokens: `69: "你", 70: "那", 71: "个"`
  - mapping_reason: Condition for achievement.
* target[29]: "できたうちに"
  - source_tokens: `72: "叫成"`
  - mapping_reason: Achievement classification.
* target[30]: "入らへんぞ」"
  - source_tokens: `73: "了。"`
  - mapping_reason: Finality of the negative assessment.
* target[31]: "って。"
  - source_tokens: `73: "了。"`
  - mapping_reason: Quotative marker for final speech.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [2]},
  {"target_senseunit_id": 1, "source_token_ids": [7]},
  {"target_senseunit_id": 2, "source_token_ids": [4, 5, 6]},
  {"target_senseunit_id": 3, "source_token_ids": [11, 12, 13]},
  {"target_senseunit_id": 4, "source_token_ids": [21]},
  {"target_senseunit_id": 5, "source_token_ids": [23]},
  {"target_senseunit_id": 6, "source_token_ids": [25, 26]},
  {"target_senseunit_id": 7, "source_token_ids": [28]},
  {"target_senseunit_id": 8, "source_token_ids": [28]},
  {"target_senseunit_id": 9, "source_token_ids": [27]},
  {"target_senseunit_id": 10, "source_token_ids": [29, 30, 31, 32, 33]},
  {"target_senseunit_id": 11, "source_token_ids": [28]},
  {"target_senseunit_id": 12, "source_token_ids": [35]},
  {"target_senseunit_id": 13, "source_token_ids": [36, 37, 38, 39, 40, 41, 42, 43]},
  {"target_senseunit_id": 14, "source_token_ids": [44, 45, 46]},
  {"target_senseunit_id": 15, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 16, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 17, "source_token_ids": [54]},
  {"target_senseunit_id": 18, "source_token_ids": [35]},
  {"target_senseunit_id": 19, "source_token_ids": [53]},
  {"target_senseunit_id": 20, "source_token_ids": [53]},
  {"target_senseunit_id": 21, "source_token_ids": [56, 57]},
  {"target_senseunit_id": 22, "source_token_ids": [58, 59]},
  {"target_senseunit_id": 23, "source_token_ids": [54]},
  {"target_senseunit_id": 24, "source_token_ids": [60]},
  {"target_senseunit_id": 25, "source_token_ids": [64]},
  {"target_senseunit_id": 26, "source_token_ids": [62]},
  {"target_senseunit_id": 27, "source_token_ids": [65, 66, 67, 68]},
  {"target_senseunit_id": 28, "source_token_ids": [69, 70, 71]},
  {"target_senseunit_id": 29, "source_token_ids": [72]},
  {"target_senseunit_id": 30, "source_token_ids": [73]},
  {"target_senseunit_id": 31, "source_token_ids": [73]}
]

- retry: 2/5
  status: failed_after_response
  reason: * target[9]
  - verdict: mapping_error
  - reason: "The source token '他' (27) is a pronoun referring to the master, but the target '師匠' (Master) is explicitly identified as '师傅' (11) in the source text. Mapping to the pronoun is less accurate than mapping to the noun."
  - replace_source_tokens: 11: "师傅"
  validation:
    scratchpad:
* target[0]: "その時、"
  - source_tokens: `2: "当时"`
  - mapping_reason: Temporal marker.
* target[1]: "月輪が"
  - source_tokens: `7: "月轮，"`
  - mapping_reason: Object of vision.
* target[2]: "見えたんで、"
  - source_tokens: `6: "看到"`
  - mapping_reason: Verb of vision.
* target[3]: "師匠の熊先生に"
  - source_tokens: `10: "跟", 11: "师傅", 12: "熊", 13: "老师"`
  - mapping_reason: Indirect object (recipient).
* target[4]: "報告したんです。"
  - source_tokens: `21: "汇报。"`
  - mapping_reason: Main verb of reporting.
* target[5]: "「師匠、"
  - source_tokens: `22: "二", 23: "师傅，"`
  - mapping_reason: Address term.
* target[6]: "できました！」"
  - source_tokens: `24: "我", 25: "成", 26: "了。"`
  - mapping_reason: The achievement claimed.
* target[7]: "って。"
  - source_tokens: `35: "说"`
  - mapping_reason: Quotative marker.
* target[8]: "そしたら"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Discourse connector indicating transition to next speaker's turn.
* target[9]: "師匠が"
  - source_tokens: `27: "他"`
  - mapping_reason: Subject of the inquiry.
* target[10]: "「何ができたんだ？」"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了？"`
  - mapping_reason: Content of the question.
* target[11]: "って"
  - source_tokens: `35: "说"`
  - mapping_reason: Quotative marker.
* target[12]: "聞くから、"
  - source_tokens: `28: "说"`
  - mapping_reason: Verb of asking/inquiring.
* target[13]: "「大きな月が見えたんです。"
  - source_tokens: `36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Content of the response.
* target[14]: "キラキラしてて、"
  - source_tokens: `42: "亮", 44: "亮", 45: "亮", 46: "的，"`
  - mapping_reason: Descriptive modifier.
* target[15]: "見てください、"
  - source_tokens: `47: "你", 48: "看", 49: "啊，"`
  - mapping_reason: Directive to look.
* target[16]: "光に満ちてるんです！」"
  - source_tokens: `50: "一", 51: "堂", 52: "光。"`
  - mapping_reason: Description of the scene.
* target[17]: "って"
  - source_tokens: `54: "说"`
  - mapping_reason: Quotative marker.
* target[18]: "答えたんです。"
  - source_tokens: `34: "我", 35: "说"`
  - mapping_reason: Verb of answering.
* target[19]: "そしたら"
  - source_tokens: `53: "他", 54: "说"`
  - mapping_reason: Discourse connector for the next turn.
* target[20]: "師匠が"
  - source_tokens: `53: "他"`
  - mapping_reason: Subject of the retort.
* target[21]: "「できたも何も、"
  - source_tokens: `56: "成", 57: "了"`
  - mapping_reason: Refuting the achievement.
* target[22]: "ちゃんちゃらおかしいわ！」"
  - source_tokens: `58: "个", 59: "屁，"`
  - mapping_reason: The derogatory retort.
* target[23]: "って"
  - source_tokens: `54: "说"`
  - mapping_reason: Quotative marker.
* target[24]: "大笑いして。"
  - source_tokens: `60: "哈哈哈哈哈！"`
  - mapping_reason: Physical reaction.
* target[25]: "私に対しては"
  - source_tokens: `63: "跟", 64: "我"`
  - mapping_reason: Target of the behavior.
* target[26]: "いつも"
  - source_tokens: `62: "就"`
  - mapping_reason: Habitual aspect.
* target[27]: "遠慮がないんです。"
  - source_tokens: `65: "说话", 66: "不", 67: "客气", 68: "啊，"`
  - mapping_reason: Description of the teacher's manner.
* target[28]: "「そんなんじゃ、"
  - source_tokens: `69: "你", 70: "那", 71: "个"`
  - mapping_reason: Referring to the previous claim.
* target[29]: "できたうちに"
  - source_tokens: `72: "叫成"`
  - mapping_reason: Qualification of achievement.
* target[30]: "入らへんぞ」"
  - source_tokens: `73: "了。"`
  - mapping_reason: Negative conclusion.
* target[31]: "って。"
  - source_tokens: `65: "说话"`
  - mapping_reason: Quotative marker.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [2]},
  {"target_senseunit_id": 1, "source_token_ids": [7]},
  {"target_senseunit_id": 2, "source_token_ids": [6]},
  {"target_senseunit_id": 3, "source_token_ids": [10, 11, 12, 13]},
  {"target_senseunit_id": 4, "source_token_ids": [21]},
  {"target_senseunit_id": 5, "source_token_ids": [22, 23]},
  {"target_senseunit_id": 6, "source_token_ids": [24, 25, 26]},
  {"target_senseunit_id": 7, "source_token_ids": [35]},
  {"target_senseunit_id": 8, "source_token_ids": [27, 28]},
  {"target_senseunit_id": 9, "source_token_ids": [27]},
  {"target_senseunit_id": 10, "source_token_ids": [29, 30, 31, 32, 33]},
  {"target_senseunit_id": 11, "source_token_ids": [35]},
  {"target_senseunit_id": 12, "source_token_ids": [28]},
  {"target_senseunit_id": 13, "source_token_ids": [36, 37, 38, 39, 40, 41]},
  {"target_senseunit_id": 14, "source_token_ids": [42, 44, 45, 46]},
  {"target_senseunit_id": 15, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 16, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 17, "source_token_ids": [54]},
  {"target_senseunit_id": 18, "source_token_ids": [34, 35]},
  {"target_senseunit_id": 19, "source_token_ids": [53, 54]},
  {"target_senseunit_id": 20, "source_token_ids": [53]},
  {"target_senseunit_id": 21, "source_token_ids": [56, 57]},
  {"target_senseunit_id": 22, "source_token_ids": [58, 59]},
  {"target_senseunit_id": 23, "source_token_ids": [54]},
  {"target_senseunit_id": 24, "source_token_ids": [60]},
  {"target_senseunit_id": 25, "source_token_ids": [63, 64]},
  {"target_senseunit_id": 26, "source_token_ids": [62]},
  {"target_senseunit_id": 27, "source_token_ids": [65, 66, 67, 68]},
  {"target_senseunit_id": 28, "source_token_ids": [69, 70, 71]},
  {"target_senseunit_id": 29, "source_token_ids": [72]},
  {"target_senseunit_id": 30, "source_token_ids": [73]},
  {"target_senseunit_id": 31, "source_token_ids": [65]}
]

- retry: 3/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_Yu84L6YIP6A_W000010 ===

source:
- language: Chinese
- transcription: 说，我当时我只是看到月轮，我就跟师傅熊老师嘛，是我的师傅，我就汇报。二师傅，我成了。他说你成了什么了？我说我看到一个大月亮了，亮亮的，你看啊，一堂光。他说你成了个屁，哈哈哈哈哈！他就跟我说话不客气啊，你那个叫成了。
- source_tokens:
  0. 说，
  1. 我
  2. 当时
  3. 我
  4. 只
  5. 是
  6. 看到
  7. 月轮，
  8. 我
  9. 就
  10. 跟
  11. 师傅
  12. 熊
  13. 老师
  14. 嘛，
  15. 是
  16. 我
  17. 的
  18. 师傅，
  19. 我
  20. 就
  21. 汇报。
  22. 二
  23. 师傅，
  24. 我
  25. 成
  26. 了。
  27. 他
  28. 说
  29. 你
  30. 成
  31. 了
  32. 什么
  33. 了？
  34. 我
  35. 说
  36. 我
  37. 看到
  38. 一
  39. 个
  40. 大
  41. 月
  42. 亮
  43. 了，
  44. 亮
  45. 亮
  46. 的，
  47. 你
  48. 看
  49. 啊，
  50. 一
  51. 堂
  52. 光。
  53. 他
  54. 说
  55. 你
  56. 成
  57. 了
  58. 个
  59. 屁，
  60. 哈哈哈哈哈！
  61. 他
  62. 就
  63. 跟
  64. 我
  65. 说话
  66. 不
  67. 客气
  68. 啊，
  69. 你
  70. 那
  71. 个
  72. 叫成
  73. 了。

target:
- language: Korean
- translation: 그때 저는 그냥 달무리를 보고는, 제 스승님이신 슝 선생님께 '스승님, 저 해냈어요!'라고 말씀드렸죠. 그러니까 스승님께서 '뭘 해냈다는 거야?' 하셔서, '커다란 달을 봤어요, 아주 밝게 빛나고, 보세요, 방 안이 온통 빛이에요'라고 했죠. 그랬더니 스승님께서 '뭘 해내긴 개뿔! 하하하하!' 하시더라고요. 정말 말을 가차 없이 하셔요. '그걸 해낸 거라고?' 하시면서요.
- target_sense_units:
  0. 그때
  1. 저는
  2. 그냥 달무리를 보고는,
  3. 제 스승님이신
  4. 슝 선생님께
  5. ' 스승님,
  6. 저 해냈어요!
  7. '
  8. 라고 말씀드렸죠.
  9. 그러니까
  10. 스승님께서
  11. ' 뭘 해냈다는
  12. 거야? '
  13. 하셔서,
  14. ' 커다란 달을 봤어요,
  15. 아주 밝게 빛나고,
  16. 보세요,
  17. 방 안이 온통 빛이에요
  18. '
  19. 라고 했죠.
  20. 그랬더니
  21. 스승님께서
  22. ' 뭘 해내긴 개뿔!
  23. 하하하하! '
  24. 하시더라고요.
  25. 정말 말을
  26. 가차 없이
  27. 하셔요.
  28. ' 그걸 해낸 거라고?
  29. '
  30. 하시면서요.

scratchpad:
* target[0]: "그때"
  - source_tokens: `2: "当时"`
  - mapping_reason: Temporal marker referring to the past moment.
* target[1]: "저는"
  - source_tokens: `1: "我"`
  - mapping_reason: Subject pronoun.
* target[2]: "그냥 달무리를 보고는,"
  - source_tokens: `4: "只", 5: "是", 6: "看到", 7: "月轮"`
  - mapping_reason: Action of seeing the halo/moon-ring.
* target[3]: "제 스승님이신"
  - source_tokens: `15: "是", 16: "我", 17: "的", 18: "师傅"`
  - mapping_reason: Identification of the teacher.
* target[4]: "슝 선생님께"
  - source_tokens: `12: "熊", 13: "老师"`
  - mapping_reason: Name/Title of the teacher.
* target[5]: "' 스승님,"
  - source_tokens: `23: "师傅"`
  - mapping_reason: Direct address to the teacher.
* target[6]: "저 해냈어요!"
  - source_tokens: `24: "我", 25: "成", 26: "了"`
  - mapping_reason: Expression of achievement.
* target[7]: "'"
  - source_tokens: `21: "汇报"`
  - mapping_reason: Punctuation marking the end of the direct quote.
* target[8]: "라고 말씀드렸죠."
  - source_tokens: `20: "就", 21: "汇报"`
  - mapping_reason: Reporting the speech.
* target[9]: "그러니까"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Discourse connector for the master's response.
* target[10]: "스승님께서"
  - source_tokens: `27: "他"`
  - mapping_reason: Subject of the response.
* target[11]: "' 뭘 해냈다는"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么"`
  - mapping_reason: Question about the achievement.
* target[12]: "거야? '"
  - source_tokens: `33: "了"`
  - mapping_reason: Interrogative sentence ending.
* target[13]: "하셔서,"
  - source_tokens: `28: "说"`
  - mapping_reason: Reporting the master's question.
* target[14]: "' 커다란 달을 봤어요,"
  - source_tokens: `34: "我", 35: "说", 36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Reporting the vision of the moon.
* target[15]: "아주 밝게 빛나고,"
  - source_tokens: `42: "亮", 43: "了", 44: "亮", 45: "亮", 46: "的"`
  - mapping_reason: Description of brightness.
* target[16]: "보세요,"
  - source_tokens: `47: "你", 48: "看", 49: "啊"`
  - mapping_reason: Invitation to look.
* target[17]: "방 안이 온통 빛이에요"
  - source_tokens: `50: "一", 51: "堂", 52: "光"`
  - mapping_reason: Description of the light filling the space.
* target[18]: "'"
  - source_tokens: `54: "说"`
  - mapping_reason: End of the quote segment.
* target[19]: "라고 했죠."
  - source_tokens: `35: "说"`
  - mapping_reason: Reporting the speech.
* target[20]: "그랬더니"
  - source_tokens: `53: "他"`
  - mapping_reason: Transition to the master's reaction.
* target[21]: "스승님께서"
  - source_tokens: `53: "他"`
  - mapping_reason: Subject of the next action.
* target[22]: "' 뭘 해내긴 개뿔!"
  - source_tokens: `55: "你", 56: "成", 57: "了", 58: "个", 59: "屁"`
  - mapping_reason: Derisive response.
* target[23]: "하하하하! '"
  - source_tokens: `60: "哈哈哈哈哈"`
  - mapping_reason: Laughter.
* target[24]: "하시더라고요."
  - source_tokens: `54: "说"`
  - mapping_reason: Reporting the master's speech.
* target[25]: "정말 말을"
  - source_tokens: `61: "他", 65: "说话"`
  - mapping_reason: Comment on the master's manner of speaking.
* target[26]: "가차 없이"
  - source_tokens: `66: "不", 67: "客气", 68: "啊"`
  - mapping_reason: Description of the bluntness.
* target[27]: "하셔요."
  - source_tokens: `65: "说话"`
  - mapping_reason: The act of speaking.
* target[28]: "' 그걸 해낸 거라고?"
  - source_tokens: `69: "你", 70: "那", 71: "个", 72: "叫成"`
  - mapping_reason: Re-questioning the achievement.
* target[29]: "'"
  - source_tokens: `73: "了"`
  - mapping_reason: Closing quote of the final sentence.
* target[30]: "하시면서요."
  - source_tokens: `65: "说话"`
  - mapping_reason: Concluding the reporting of the master's speech.

result:
```html
0. <src>说，我当时</src> <tgt>그때 저는</tgt>; start=0.00, end=1.00
1. <src>我只是看到</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>月轮，</src> <tgt>그냥 달무리를 보고는,</tgt>; start=2.00, end=3.00
3. <src>我就跟师傅</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>熊老师嘛，是我的</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>师傅，我就汇报。</src> <tgt>제 스승님이신 슝 선생님께</tgt>; start=5.00, end=6.00
6. <src>二师傅，</src> <tgt>' 스승님,</tgt>; start=6.00, end=7.00
7. <src>我成了。他说你成了</src> <tgt>저 해냈어요! ' 라고 말씀드렸죠. 그러니까 스승님께서</tgt>; start=7.00, end=8.00
8. <src>什么了？</src> <tgt>' 뭘 해냈다는 거야? ' 하셔서,</tgt>; start=8.00, end=9.00
9. <src>我说我看到一个</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>大月亮了，</src> <tgt>' 커다란 달을 봤어요,</tgt>; start=10.00, end=11.00
11. <src>亮亮的，你看</src> <tgt>아주 밝게 빛나고,</tgt>; start=11.00, end=12.00
12. <src>啊，</src> <tgt>보세요,</tgt>; start=12.00, end=13.00
13. <src>一堂光。他说</src> <tgt>방 안이 온통 빛이에요 ' 라고 했죠. 그랬더니 스승님께서</tgt>; start=13.00, end=14.00
14. <src><|wait|></src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>你成了个屁，</src> <tgt>' 뭘 해내긴 개뿔!</tgt>; start=15.00, end=16.00
16. <src>哈哈哈哈哈！他就跟我</src> <tgt>하하하하! ' 하시더라고요.</tgt>; start=16.00, end=17.00
17. <src>说话不客气</src> <tgt>정말 말을</tgt>; start=17.00, end=18.00
18. <src>啊，</src> <tgt>가차 없이 하셔요.</tgt>; start=18.00, end=19.00
19. <src>你那个叫成了。</src> <tgt>' 그걸 해낸 거라고? ' 하시면서요.</tgt>; start=19.00, end=19.80
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[30]
  - verdict: mapping_error
  - reason: "The target unit '하시면서요.' functions as a speech tag for the final remark in the dialogue (72-73), not the general description of the teacher's speaking style (65)."
  - replace_source_tokens: 72: "叫成", 73: "了"
  validation:
    scratchpad:
* target[0]: "그때"
  - source_tokens: `2: "当时"`
  - mapping_reason: Temporal marker
* target[1]: "저는"
  - source_tokens: `1: "我"`
  - mapping_reason: Subject
* target[2]: "그냥 달무리를 보고는,"
  - source_tokens: `4: "只", 5: "是", 6: "看到", 7: "月轮"`
  - mapping_reason: Action of seeing the moon halo
* target[3]: "제 스승님이신"
  - source_tokens: `15: "是", 16: "我", 17: "的", 18: "师傅"`
  - mapping_reason: Appositive description of teacher
* target[4]: "슝 선생님께"
  - source_tokens: `12: "熊", 13: "老师"`
  - mapping_reason: Indirect object (teacher)
* target[5]: "' 스승님,"
  - source_tokens: `23: "师傅"`
  - mapping_reason: Address term
* target[6]: "저 해냈어요!"
  - source_tokens: `24: "我", 25: "成", 26: "了"`
  - mapping_reason: Reporting success
* target[7]: "'"
  - source_tokens: `21: "汇报"`
  - mapping_reason: Quote closure/reporting verb marker
* target[8]: "라고 말씀드렸죠."
  - source_tokens: `8: "我", 9: "就", 10: "跟", 11: "师傅", 21: "汇报"`
  - mapping_reason: Reported speech verb
* target[9]: "그러니까"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Discourse connective (transition to response)
* target[10]: "스승님께서"
  - source_tokens: `27: "他"`
  - mapping_reason: Subject of the response
* target[11]: "' 뭘 해냈다는"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么", 33: "了"`
  - mapping_reason: Question about success
* target[12]: "거야? '"
  - source_tokens: `28: "说"`
  - mapping_reason: Quote marker
* target[13]: "하셔서,"
  - source_tokens: `28: "说"`
  - mapping_reason: Reporting verb
* target[14]: "' 커다란 달을 봤어요,"
  - source_tokens: `34: "我", 35: "说", 36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Describing the moon
* target[15]: "아주 밝게 빛나고,"
  - source_tokens: `42: "亮", 44: "亮", 45: "亮", 46: "的"`
  - mapping_reason: Describing brightness
* target[16]: "보세요,"
  - source_tokens: `47: "你", 48: "看", 49: "啊"`
  - mapping_reason: Directing attention
* target[17]: "방 안이 온통 빛이에요"
  - source_tokens: `50: "一", 51: "堂", 52: "光"`
  - mapping_reason: Describing the light
* target[18]: "'"
  - source_tokens: `35: "说"`
  - mapping_reason: Quote closure
* target[19]: "라고 했죠."
  - source_tokens: `35: "说"`
  - mapping_reason: Reporting verb
* target[20]: "그랬더니"
  - source_tokens: `53: "他"`
  - mapping_reason: Transition to response
* target[21]: "스승님께서"
  - source_tokens: `53: "他"`
  - mapping_reason: Subject
* target[22]: "' 뭘 해내긴 개뿔!"
  - source_tokens: `55: "你", 56: "成", 57: "了", 58: "个", 59: "屁"`
  - mapping_reason: Dismissive response
* target[23]: "하하하하! '"
  - source_tokens: `60: "哈哈哈哈哈"`
  - mapping_reason: Laughter
* target[24]: "하시더라고요."
  - source_tokens: `54: "说"`
  - mapping_reason: Reporting verb
* target[25]: "정말 말을"
  - source_tokens: `61: "他", 62: "就", 63: "跟", 64: "我", 65: "说话"`
  - mapping_reason: Manner of speaking
* target[26]: "가차 없이"
  - source_tokens: `66: "不", 67: "客气", 68: "啊"`
  - mapping_reason: Adverbial description of harshness
* target[27]: "하셔요."
  - source_tokens: `65: "说话"`
  - mapping_reason: Verb
* target[28]: "' 그걸 해낸 거라고?"
  - source_tokens: `69: "你", 70: "那", 71: "个", 72: "叫成", 73: "了"`
  - mapping_reason: Rhetorical question
* target[29]: "'"
  - source_tokens: `65: "说话"`
  - mapping_reason: Quote closure
* target[30]: "하시면서요."
  - source_tokens: `65: "说话"`
  - mapping_reason: Reporting verb
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [2]},
  {"target_senseunit_id": 1, "source_token_ids": [1]},
  {"target_senseunit_id": 2, "source_token_ids": [4, 5, 6, 7]},
  {"target_senseunit_id": 3, "source_token_ids": [15, 16, 17, 18]},
  {"target_senseunit_id": 4, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 5, "source_token_ids": [23]},
  {"target_senseunit_id": 6, "source_token_ids": [24, 25, 26]},
  {"target_senseunit_id": 7, "source_token_ids": [21]},
  {"target_senseunit_id": 8, "source_token_ids": [8, 9, 10, 11, 21]},
  {"target_senseunit_id": 9, "source_token_ids": [27, 28]},
  {"target_senseunit_id": 10, "source_token_ids": [27]},
  {"target_senseunit_id": 11, "source_token_ids": [29, 30, 31, 32, 33]},
  {"target_senseunit_id": 12, "source_token_ids": [28]},
  {"target_senseunit_id": 13, "source_token_ids": [28]},
  {"target_senseunit_id": 14, "source_token_ids": [34, 35, 36, 37, 38, 39, 40, 41]},
  {"target_senseunit_id": 15, "source_token_ids": [42, 44, 45, 46]},
  {"target_senseunit_id": 16, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 17, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 18, "source_token_ids": [35]},
  {"target_senseunit_id": 19, "source_token_ids": [35]},
  {"target_senseunit_id": 20, "source_token_ids": [53]},
  {"target_senseunit_id": 21, "source_token_ids": [53]},
  {"target_senseunit_id": 22, "source_token_ids": [55, 56, 57, 58, 59]},
  {"target_senseunit_id": 23, "source_token_ids": [60]},
  {"target_senseunit_id": 24, "source_token_ids": [54]},
  {"target_senseunit_id": 25, "source_token_ids": [61, 62, 63, 64, 65]},
  {"target_senseunit_id": 26, "source_token_ids": [66, 67, 68]},
  {"target_senseunit_id": 27, "source_token_ids": [65]},
  {"target_senseunit_id": 28, "source_token_ids": [69, 70, 71, 72, 73]},
  {"target_senseunit_id": 29, "source_token_ids": [65]},
  {"target_senseunit_id": 30, "source_token_ids": [65]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[27]
  - verdict: mapping_error
  - reason: "The target unit '하셔요' is a verbal predicate derived from '说话' (65), not the particles '就' (62) or '跟' (63)."
  - replace_source_tokens: 65: "说话"
  validation:
    scratchpad:
* target[0]: "그때"
  - source_tokens: `2: "当时"`
  - mapping_reason: Temporal marker
* target[1]: "저는"
  - source_tokens: `1: "我"`
  - mapping_reason: Subject
* target[2]: "그냥 달무리를 보고는,"
  - source_tokens: `4: "只", 5: "是", 6: "看到", 7: "月轮"`
  - mapping_reason: Action description
* target[3]: "제 스승님이신"
  - source_tokens: `15: "是", 16: "我", 17: "的", 18: "师傅"`
  - mapping_reason: Appositive description
* target[4]: "슝 선생님께"
  - source_tokens: `10: "跟", 12: "熊", 13: "老师", 14: "嘛"`
  - mapping_reason: Indirect object
* target[5]: "' 스승님,"
  - source_tokens: `22: "二", 23: "师傅"`
  - mapping_reason: Direct address
* target[6]: "저 해냈어요!"
  - source_tokens: `24: "我", 25: "成", 26: "了"`
  - mapping_reason: Reported speech content
* target[7]: "'"
  - source_tokens: `21: "汇报"`
  - mapping_reason: Quotation boundary
* target[8]: "라고 말씀드렸죠."
  - source_tokens: `8: "我", 9: "就", 21: "汇报"`
  - mapping_reason: Reporting verb
* target[9]: "그러니까"
  - source_tokens: `27: "他", 28: "说"`
  - mapping_reason: Discourse connector
* target[10]: "스승님께서"
  - source_tokens: `27: "他"`
  - mapping_reason: Subject of reported speech
* target[11]: "' 뭘 해냈다는"
  - source_tokens: `29: "你", 30: "成", 31: "了", 32: "什么"`
  - mapping_reason: Reported speech content
* target[12]: "거야? '"
  - source_tokens: `33: "了"`
  - mapping_reason: Question marker
* target[13]: "하셔서,"
  - source_tokens: `28: "说"`
  - mapping_reason: Reporting verb
* target[14]: "' 커다란 달을 봤어요,"
  - source_tokens: `34: "我", 35: "说", 36: "我", 37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: Reported speech content
* target[15]: "아주 밝게 빛나고,"
  - source_tokens: `42: "亮", 43: "了", 44: "亮", 45: "亮", 46: "的"`
  - mapping_reason: Description
* target[16]: "보세요,"
  - source_tokens: `47: "你", 48: "看", 49: "啊"`
  - mapping_reason: Imperative
* target[17]: "방 안이 온통 빛이에요"
  - source_tokens: `50: "一", 51: "堂", 52: "光"`
  - mapping_reason: Description
* target[18]: "'"
  - source_tokens: `35: "说"`
  - mapping_reason: Quotation boundary
* target[19]: "라고 했죠."
  - source_tokens: `35: "说"`
  - mapping_reason: Reporting verb
* target[20]: "그랬더니"
  - source_tokens: `53: "他", 54: "说"`
  - mapping_reason: Discourse connector
* target[21]: "스승님께서"
  - source_tokens: `53: "他"`
  - mapping_reason: Subject
* target[22]: "' 뭘 해내긴 개뿔!"
  - source_tokens: `55: "你", 56: "成", 57: "了", 58: "个", 59: "屁"`
  - mapping_reason: Reported speech content
* target[23]: "하하하하! '"
  - source_tokens: `60: "哈哈哈哈哈"`
  - mapping_reason: Laughter
* target[24]: "하시더라고요."
  - source_tokens: `54: "说"`
  - mapping_reason: Reporting verb
* target[25]: "정말 말을"
  - source_tokens: `61: "他", 64: "我", 65: "说话"`
  - mapping_reason: Manner description
* target[26]: "가차 없이"
  - source_tokens: `66: "不", 67: "客气", 68: "啊"`
  - mapping_reason: Manner description
* target[27]: "하셔요."
  - source_tokens: `62: "就", 63: "跟"`
  - mapping_reason: Verb
* target[28]: "' 그걸 해낸 거라고?"
  - source_tokens: `69: "你", 70: "那", 71: "个", 72: "叫成"`
  - mapping_reason: Reported speech content
* target[29]: "'"
  - source_tokens: `73: "了"`
  - mapping_reason: Quotation boundary
* target[30]: "하시면서요."
  - source_tokens: `72: "叫成", 73: "了"`
  - mapping_reason: Reporting verb for final remark
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [2]},
  {"target_senseunit_id": 1, "source_token_ids": [1]},
  {"target_senseunit_id": 2, "source_token_ids": [4, 5, 6, 7]},
  {"target_senseunit_id": 3, "source_token_ids": [15, 16, 17, 18]},
  {"target_senseunit_id": 4, "source_token_ids": [10, 12, 13, 14]},
  {"target_senseunit_id": 5, "source_token_ids": [22, 23]},
  {"target_senseunit_id": 6, "source_token_ids": [24, 25, 26]},
  {"target_senseunit_id": 7, "source_token_ids": [21]},
  {"target_senseunit_id": 8, "source_token_ids": [8, 9, 21]},
  {"target_senseunit_id": 9, "source_token_ids": [27, 28]},
  {"target_senseunit_id": 10, "source_token_ids": [27]},
  {"target_senseunit_id": 11, "source_token_ids": [29, 30, 31, 32]},
  {"target_senseunit_id": 12, "source_token_ids": [33]},
  {"target_senseunit_id": 13, "source_token_ids": [28]},
  {"target_senseunit_id": 14, "source_token_ids": [34, 35, 36, 37, 38, 39, 40, 41]},
  {"target_senseunit_id": 15, "source_token_ids": [42, 43, 44, 45, 46]},
  {"target_senseunit_id": 16, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 17, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 18, "source_token_ids": [35]},
  {"target_senseunit_id": 19, "source_token_ids": [35]},
  {"target_senseunit_id": 20, "source_token_ids": [53, 54]},
  {"target_senseunit_id": 21, "source_token_ids": [53]},
  {"target_senseunit_id": 22, "source_token_ids": [55, 56, 57, 58, 59]},
  {"target_senseunit_id": 23, "source_token_ids": [60]},
  {"target_senseunit_id": 24, "source_token_ids": [54]},
  {"target_senseunit_id": 25, "source_token_ids": [61, 64, 65]},
  {"target_senseunit_id": 26, "source_token_ids": [66, 67, 68]},
  {"target_senseunit_id": 27, "source_token_ids": [62, 63]},
  {"target_senseunit_id": 28, "source_token_ids": [69, 70, 71, 72]},
  {"target_senseunit_id": 29, "source_token_ids": [73]},
  {"target_senseunit_id": 30, "source_token_ids": [72, 73]}
]

- retry: 2/5
  status: failed_after_response
  reason: * target[9]
  - verdict: mapping_error
  - reason: "The discourse connector '그러니까' functions as a transition between the speaker's report and the master's response; it is anchored to the verb '说' (said) following '他' (he)."
  - replace_source_tokens: 27: "他", 28: "说"

* target[29]
  - verdict: mapping_error
  - reason: "The closing quote is a structural punctuation mark related to the dialogue in target[28], not a translation of '说话'. It should be anchored to the final sentence's completion."
  - replace_source_tokens: 73: "了"
  validation:
    scratchpad:
* target[0]: "그때"
  - source_tokens: `2: "当时"`
  - mapping_reason: temporal adverb
* target[1]: "저는"
  - source_tokens: `1: "我"`
  - mapping_reason: subject pronoun
* target[2]: "그냥 달무리를 보고는,"
  - source_tokens: `4: "只", 5: "是", 6: "看到", 7: "月轮"`
  - mapping_reason: action description
* target[3]: "제 스승님이신"
  - source_tokens: `15: "是", 16: "我", 17: "的", 18: "师傅"`
  - mapping_reason: possessive reference
* target[4]: "슝 선생님께"
  - source_tokens: `10: "跟", 12: "熊", 13: "老师"`
  - mapping_reason: indirect object
* target[5]: "' 스승님,"
  - source_tokens: `23: "师傅"`
  - mapping_reason: direct address
* target[6]: "저 해냈어요!"
  - source_tokens: `25: "成", 26: "了"`
  - mapping_reason: reported speech content
* target[7]: "'"
  - source_tokens: `21: "汇报"`
  - mapping_reason: quotation boundary/reporting verb
* target[8]: "라고 말씀드렸죠."
  - source_tokens: `21: "汇报"`
  - mapping_reason: reporting verb
* target[9]: "그러니까"
  - source_tokens: `27: "他"`
  - mapping_reason: discourse connective indicating response
* target[10]: "스승님께서"
  - source_tokens: `27: "他"`
  - mapping_reason: subject of response
* target[11]: "' 뭘 해냈다는"
  - source_tokens: `30: "成", 31: "了", 32: "什么", 33: "了"`
  - mapping_reason: reported question
* target[12]: "거야? '"
  - source_tokens: `28: "说"`
  - mapping_reason: reporting verb
* target[13]: "하셔서,"
  - source_tokens: `28: "说"`
  - mapping_reason: reporting verb
* target[14]: "' 커다란 달을 봤어요,"
  - source_tokens: `37: "看到", 38: "一", 39: "个", 40: "大", 41: "月"`
  - mapping_reason: reported description
* target[15]: "아주 밝게 빛나고,"
  - source_tokens: `42: "亮", 44: "亮", 45: "亮"`
  - mapping_reason: descriptive modifier
* target[16]: "보세요,"
  - source_tokens: `47: "你", 48: "看", 49: "啊"`
  - mapping_reason: imperative
* target[17]: "방 안이 온통 빛이에요"
  - source_tokens: `50: "一", 51: "堂", 52: "光"`
  - mapping_reason: descriptive state
* target[18]: "'"
  - source_tokens: `35: "说"`
  - mapping_reason: reporting verb boundary
* target[19]: "라고 했죠."
  - source_tokens: `35: "说"`
  - mapping_reason: reporting verb
* target[20]: "그랬더니"
  - source_tokens: `53: "他"`
  - mapping_reason: discourse connective
* target[21]: "스승님께서"
  - source_tokens: `53: "他"`
  - mapping_reason: subject of response
* target[22]: "' 뭘 해내긴 개뿔!"
  - source_tokens: `56: "成", 57: "了", 58: "个", 59: "屁"`
  - mapping_reason: reported exclamation
* target[23]: "하하하하! '"
  - source_tokens: `60: "哈哈哈哈哈"`
  - mapping_reason: laughter
* target[24]: "하시더라고요."
  - source_tokens: `54: "说"`
  - mapping_reason: reporting verb
* target[25]: "정말 말을"
  - source_tokens: `65: "说话"`
  - mapping_reason: verb phrase
* target[26]: "가차 없이"
  - source_tokens: `66: "不", 67: "客气"`
  - mapping_reason: manner adverb
* target[27]: "하셔요."
  - source_tokens: `65: "说话"`
  - mapping_reason: verbal predicate
* target[28]: "' 그걸 해낸 거라고?"
  - source_tokens: `72: "叫成", 73: "了"`
  - mapping_reason: reported rhetorical question
* target[29]: "'"
  - source_tokens: `65: "说话"`
  - mapping_reason: reporting boundary
* target[30]: "하시면서요."
  - source_tokens: `65: "说话"`
  - mapping_reason: reporting verb
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [2]},
  {"target_senseunit_id": 1, "source_token_ids": [1]},
  {"target_senseunit_id": 2, "source_token_ids": [4, 5, 6, 7]},
  {"target_senseunit_id": 3, "source_token_ids": [15, 16, 17, 18]},
  {"target_senseunit_id": 4, "source_token_ids": [10, 12, 13]},
  {"target_senseunit_id": 5, "source_token_ids": [23]},
  {"target_senseunit_id": 6, "source_token_ids": [25, 26]},
  {"target_senseunit_id": 7, "source_token_ids": [21]},
  {"target_senseunit_id": 8, "source_token_ids": [21]},
  {"target_senseunit_id": 9, "source_token_ids": [27]},
  {"target_senseunit_id": 10, "source_token_ids": [27]},
  {"target_senseunit_id": 11, "source_token_ids": [30, 31, 32, 33]},
  {"target_senseunit_id": 12, "source_token_ids": [28]},
  {"target_senseunit_id": 13, "source_token_ids": [28]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39, 40, 41]},
  {"target_senseunit_id": 15, "source_token_ids": [42, 44, 45]},
  {"target_senseunit_id": 16, "source_token_ids": [47, 48, 49]},
  {"target_senseunit_id": 17, "source_token_ids": [50, 51, 52]},
  {"target_senseunit_id": 18, "source_token_ids": [35]},
  {"target_senseunit_id": 19, "source_token_ids": [35]},
  {"target_senseunit_id": 20, "source_token_ids": [53]},
  {"target_senseunit_id": 21, "source_token_ids": [53]},
  {"target_senseunit_id": 22, "source_token_ids": [56, 57, 58, 59]},
  {"target_senseunit_id": 23, "source_token_ids": [60]},
  {"target_senseunit_id": 24, "source_token_ids": [54]},
  {"target_senseunit_id": 25, "source_token_ids": [65]},
  {"target_senseunit_id": 26, "source_token_ids": [66, 67]},
  {"target_senseunit_id": 27, "source_token_ids": [65]},
  {"target_senseunit_id": 28, "source_token_ids": [72, 73]},
  {"target_senseunit_id": 29, "source_token_ids": [65]},
  {"target_senseunit_id": 30, "source_token_ids": [65]}
]

- retry: 3/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_Q0a8pjeI4HA_W000054 ===

source:
- language: Chinese
- transcription: 那你就可以变成那百分之二十的人，去成就不一样的人生，可以知命、懂命、用命、在招命喽。换句话说，荧幕前的各位朋友。
- source_tokens:
  0. 那
  1. 你
  2. 就
  3. 可以
  4. 变成
  5. 那百
  6. 分
  7. 之
  8. 二十
  9. 的
  10. 人，
  11. 去
  12. 成就
  13. 不
  14. 一样
  15. 的
  16. 人生，
  17. 可以
  18. 知命、
  19. 懂
  20. 命、
  21. 用
  22. 命、
  23. 在
  24. 招命
  25. 喽。
  26. 换
  27. 句
  28. 话
  29. 说，
  30. 荧幕
  31. 前
  32. 的
  33. 各位
  34. 朋友。

target:
- language: Japanese
- translation: そうすれば、あなたは20%の人になり、異なる人生を切り開くんです。運命を知って、理解して、活用して、自ら創り出していくんです。つまり、画面の前の皆さん。
- target_sense_units:
  0. そうすれば、
  1. あなたは
  2. 20%の人に
  3. なり、
  4. 異なる人生を
  5. 切り開くんです。
  6. 運命を
  7. 知って、
  8. 理解して、
  9. 活用して、
  10. 自ら創り出していくんです。
  11. つまり、
  12. 画面の前の皆さん。

scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 2: "就"`
  - mapping_reason: "那" (that) + "就" (then) function as the conditional connective.
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject "你" (you).
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: Provides the specific group "20% of people".
* target[3]: "なり、"
  - source_tokens: `3: "可以", 4: "变成"`
  - mapping_reason: "变成" (become) with modal "可以" (can).
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: "不一样的人生" (different life).
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: "去成就" (go and achieve/carve out).
* target[6]: "運命を"
  - source_tokens: `18: "知命、"`
  - mapping_reason: The root noun "命" (fate/life) is extracted from "知命".
* target[7]: "知って、"
  - source_tokens: `18: "知命、"`
  - mapping_reason: The verb "知" (know).
* target[8]: "理解して、"
  - source_tokens: `19: "懂", 20: "命、"`
  - mapping_reason: The verb "懂" (understand).
* target[9]: "活用して、"
  - source_tokens: `21: "用", 22: "命、"`
  - mapping_reason: The verb "用" (use/utilize).
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: "在招命" (actively inviting/creating fate) with the final particle "喽".
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse connective "换句话说" (in other words).
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: "荧幕前的各位朋友" (friends in front of the screen).

result:
```html
0. <src>那你就可以</src> <tgt>そうすれば、あなたは</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>变成那百分之二十</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>的人，去成就</src> <tgt>20%の人になり、</tgt>; start=3.00, end=4.00
4. <src>不一样的人生，可以</src> <tgt>異なる人生を切り開くんです。</tgt>; start=4.00, end=5.00
5. <src><|wait|></src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>知命、懂命、用命、</src> <tgt>運命を知って、理解して、活用して、</tgt>; start=6.00, end=7.00
7. <src><|wait|></src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>在招命喽。</src> <tgt>自ら創り出していくんです。</tgt>; start=8.00, end=9.00
9. <src><|wait|></src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>换句话说，</src> <tgt>つまり、</tgt>; start=10.00, end=11.00
11. <src>荧幕前的各位朋友。</src> <tgt>画面の前の皆さん。</tgt>; start=11.00, end=11.73
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[0]
  - verdict: mapping_error
  - reason: "The source token '你' (you) is the subject for the next unit and does not belong to the translation of 'そうすれば'."
  - replace_source_tokens: 0: "那", 2: "就"

* target[6]
  - verdict: mapping_error
  - reason: "The target unit '運命を' is the object '命', not the entire verb-object phrases listed. It should be mapped to the relevant '命' token(s)."
  - replace_source_tokens: 18: "知命、"
  validation:
    scratchpad:
* target[0]: "そうすれば、"
  - source_tokens: `0: "那", 1: "你", 2: "就"`
  - mapping_reason: Connective "那...就" indicating consequence.
* target[1]: "あなたは"
  - source_tokens: `1: "你"`
  - mapping_reason: Subject reference.
* target[2]: "20%の人に"
  - source_tokens: `5: "那百", 6: "分", 7: "之", 8: "二十", 9: "的", 10: "人，"`
  - mapping_reason: The target group "20% of people".
* target[3]: "なり、"
  - source_tokens: `4: "变成"`
  - mapping_reason: Verb "become".
* target[4]: "異なる人生を"
  - source_tokens: `13: "不", 14: "一样", 15: "的", 16: "人生，"`
  - mapping_reason: The object "different life".
* target[5]: "切り開くんです。"
  - source_tokens: `11: "去", 12: "成就"`
  - mapping_reason: Verb phrase "achieve/carve out".
* target[6]: "運命を"
  - source_tokens: `18: "知命、", 20: "命、", 22: "命、", 24: "招命"`
  - mapping_reason: The object "fate" shared across the list of verbs.
* target[7]: "知って、"
  - source_tokens: `17: "可以", 18: "知命、"`
  - mapping_reason: First verb in the sequence.
* target[8]: "理解して、"
  - source_tokens: `19: "懂"`
  - mapping_reason: Second verb in the sequence.
* target[9]: "活用して、"
  - source_tokens: `21: "用"`
  - mapping_reason: Third verb in the sequence.
* target[10]: "自ら創り出していくんです。"
  - source_tokens: `23: "在", 24: "招命", 25: "喽。"`
  - mapping_reason: Final verb phrase and sentence-ending nuance.
* target[11]: "つまり、"
  - source_tokens: `26: "换", 27: "句", 28: "话", 29: "说，"`
  - mapping_reason: Discourse connective "in other words".
* target[12]: "画面の前の皆さん。"
  - source_tokens: `30: "荧幕", 31: "前", 32: "的", 33: "各位", 34: "朋友。"`
  - mapping_reason: Addressee phrase.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [1]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [5, 6, 7, 8, 9, 10]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [13, 14, 15, 16]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [18, 20, 22, 24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [17, 18]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [19]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [23, 24, 25]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [26, 27, 28, 29]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [30, 31, 32, 33, 34]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
