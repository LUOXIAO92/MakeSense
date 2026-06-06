=== ZH_B00021_S06758_W000029 ===

source:
- language: Chinese
- transcription: 我仿佛看到了他们游走在太行山上的足迹，深一脚浅一脚；我仿佛听到了他们放歌太行山上的声音，时而高，时而低，时而欢快，时而呜咽。
- source_tokens:
  0. 我
  1. 仿佛
  2. 看到
  3. 了
  4. 他们
  5. 游走
  6. 在
  7. 太行
  8. 山
  9. 上
  10. 的
  11. 足迹，
  12. 深
  13. 一
  14. 脚
  15. 浅
  16. 一
  17. 脚；
  18. 我
  19. 仿佛
  20. 听到
  21. 了
  22. 他们
  23. 放歌
  24. 太行
  25. 山
  26. 上
  27. 的
  28. 声音，
  29. 时
  30. 而
  31. 高，
  32. 时
  33. 而
  34. 低，
  35. 时
  36. 而
  37. 欢快，
  38. 时
  39. 而
  40. 呜
  41. 咽。

target:
- language: English
- translation: I seem to see their wandering footprints on the Taihang Mountains, stumbling step by step; I seem to hear their songs echoing in the Taihang Mountains, sometimes high, sometimes low, sometimes joyful, sometimes sobbing.
- target_sense_units:
  0. I seem
  1. to see
  2. their wandering footprints
  3. on the Taihang Mountains,
  4. stumbling step by step;
  5. I seem
  6. to hear
  7. their songs
  8. echoing in the Taihang Mountains,
  9. sometimes high,
  10. sometimes low,
  11. sometimes joyful,
  12. sometimes sobbing.

scratchpad:
* target[0]: "I seem"
  - source_tokens: `0: "我", 1: "仿佛"`
  - mapping_reason: Subject and modal adverbial for perception.
* target[1]: "to see"
  - source_tokens: `2: "看到", 3: "了"`
  - mapping_reason: Main verb of perception.
* target[2]: "their wandering footprints"
  - source_tokens: `4: "他们", 5: "游走", 10: "的", 11: "足迹，"`
  - mapping_reason: Object of perception with modifier.
* target[3]: "on the Taihang Mountains,"
  - source_tokens: `6: "在", 7: "太行", 8: "山", 9: "上"`
  - mapping_reason: Location modifier.
* target[4]: "stumbling step by step;"
  - source_tokens: `12: "深", 13: "一", 14: "脚", 15: "浅", 16: "一", 17: "脚；"`
  - mapping_reason: Descriptive phrase for the footprints.
* target[5]: "I seem"
  - source_tokens: `18: "我", 19: "仿佛"`
  - mapping_reason: Subject and modal adverbial for perception.
* target[6]: "to hear"
  - source_tokens: `20: "听到", 21: "了"`
  - mapping_reason: Main verb of perception.
* target[7]: "their songs"
  - source_tokens: `22: "他们", 23: "放歌", 28: "声音，"`
  - mapping_reason: Object of perception.
* target[8]: "echoing in the Taihang Mountains,"
  - source_tokens: `24: "太行", 25: "山", 26: "上", 27: "的"`
  - mapping_reason: Location modifier for the songs.
* target[9]: "sometimes high,"
  - source_tokens: `29: "时", 30: "而", 31: "高，"`
  - mapping_reason: Descriptive modifier.
* target[10]: "sometimes low,"
  - source_tokens: `32: "时", 33: "而", 34: "低，"`
  - mapping_reason: Descriptive modifier.
* target[11]: "sometimes joyful,"
  - source_tokens: `35: "时", 36: "而", 37: "欢快，"`
  - mapping_reason: Descriptive modifier.
* target[12]: "sometimes sobbing."
  - source_tokens: `38: "时", 39: "而", 40: "呜", 41: "咽。"`
  - mapping_reason: Descriptive modifier.

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>我仿佛看到了</src> <tgt>I seem to see</tgt>; start=1.00, end=2.00
2. <src>他们游走</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>在太行山上</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>的足迹，</src> <tgt>their wandering footprints on the Taihang Mountains,</tgt>; start=4.00, end=5.00
5. <src>深一脚</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>浅一脚；</src> <tgt>stumbling step by step;</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>我仿佛听到了他们</src> <tgt>I seem to hear</tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>放歌太行山上</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>的声音，</src> <tgt>their songs echoing in the Taihang Mountains,</tgt>; start=12.00, end=13.00
13. <src>时而高，</src> <tgt>sometimes high,</tgt>; start=13.00, end=14.00
14. <src>时而低，</src> <tgt>sometimes low,</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>时而欢快，</src> <tgt>sometimes joyful,</tgt>; start=16.00, end=17.00
17. <src>时而呜咽。</src> <tgt>sometimes sobbing.</tgt>; start=17.00, end=17.84
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_B00021_S06758_W000029 ===

source:
- language: Chinese
- transcription: 我仿佛看到了他们游走在太行山上的足迹，深一脚浅一脚；我仿佛听到了他们放歌太行山上的声音，时而高，时而低，时而欢快，时而呜咽。
- source_tokens:
  0. 我
  1. 仿佛
  2. 看到
  3. 了
  4. 他们
  5. 游走
  6. 在
  7. 太行
  8. 山
  9. 上
  10. 的
  11. 足迹，
  12. 深
  13. 一
  14. 脚
  15. 浅
  16. 一
  17. 脚；
  18. 我
  19. 仿佛
  20. 听到
  21. 了
  22. 他们
  23. 放歌
  24. 太行
  25. 山
  26. 上
  27. 的
  28. 声音，
  29. 时
  30. 而
  31. 高，
  32. 时
  33. 而
  34. 低，
  35. 时
  36. 而
  37. 欢快，
  38. 时
  39. 而
  40. 呜
  41. 咽。

target:
- language: Japanese
- translation: 太行山を彷徨う彼らの足跡が見えるようだ。一歩一歩、深く浅く。太行山に響く彼らの歌声が聞こえるようだ。時には高く、時には低く、時には快活に、時には咽び泣くように。
- target_sense_units:
  0. 太行山を彷徨う
  1. 彼らの足跡が
  2. 見えるようだ。
  3. 一歩
  4. 一歩、
  5. 深く
  6. 浅く。
  7. 太行山に響く
  8. 彼らの歌声が
  9. 聞こえるようだ。
  10. 時には
  11. 高く、
  12. 時には
  13. 低く、
  14. 時には
  15. 快活に、
  16. 時には
  17. 咽び泣くように。

scratchpad:
* target[0]: "太行山を彷徨う"
  - source_tokens: `5: "游走", 6: "在", 7: "太行", 8: "山"`
  - mapping_reason: Represents the action of wandering in the Taihang Mountains.
* target[1]: "彼らの足跡が"
  - source_tokens: `4: "他们", 10: "的", 11: "足迹，"`
  - mapping_reason: Represents their footprints.
* target[2]: "見えるようだ。"
  - source_tokens: `0: "我", 1: "仿佛", 2: "看到", 3: "了"`
  - mapping_reason: Represents the perception of seeing (as if).
* target[3]: "一歩"
  - source_tokens: `13: "一", 14: "脚"`
  - mapping_reason: Represents one step.
* target[4]: "一歩、"
  - source_tokens: `16: "一", 17: "脚；"`
  - mapping_reason: Represents another step.
* target[5]: "深く"
  - source_tokens: `12: "深"`
  - mapping_reason: Represents depth.
* target[6]: "浅く。"
  - source_tokens: `15: "浅"`
  - mapping_reason: Represents shallowness.
* target[7]: "太行山に響く"
  - source_tokens: `23: "放歌", 24: "太行", 25: "山"`
  - mapping_reason: Represents singing/echoing in the Taihang Mountains.
* target[8]: "彼らの歌声が"
  - source_tokens: `22: "他们", 27: "的", 28: "声音，"`
  - mapping_reason: Represents their voices.
* target[9]: "聞こえるようだ。"
  - source_tokens: `18: "我", 19: "仿佛", 20: "听到", 21: "了"`
  - mapping_reason: Represents the perception of hearing (as if).
* target[10]: "時には"
  - source_tokens: `29: "时", 30: "而"`
  - mapping_reason: Represents temporal variation (sometimes).
* target[11]: "高く、"
  - source_tokens: `31: "高，"`
  - mapping_reason: Represents high pitch.
* target[12]: "時には"
  - source_tokens: `32: "时", 33: "而"`
  - mapping_reason: Represents temporal variation (sometimes).
* target[13]: "低く、"
  - source_tokens: `34: "低，"`
  - mapping_reason: Represents low pitch.
* target[14]: "時には"
  - source_tokens: `35: "时", 36: "而"`
  - mapping_reason: Represents temporal variation (sometimes).
* target[15]: "快活に、"
  - source_tokens: `37: "欢快，"`
  - mapping_reason: Represents joyful tone.
* target[16]: "時には"
  - source_tokens: `38: "时", 39: "而"`
  - mapping_reason: Represents temporal variation (sometimes).
* target[17]: "咽び泣くように。"
  - source_tokens: `40: "呜", 41: "咽。"`
  - mapping_reason: Represents sobbing tone.

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>我仿佛看到了</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>他们游走</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>在太行山上</src> <tgt>太行山を彷徨う</tgt>; start=3.00, end=4.00
4. <src>的足迹，</src> <tgt>彼らの足跡が見えるようだ。</tgt>; start=4.00, end=5.00
5. <src>深一脚</src> <tgt>一歩</tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>浅一脚；</src> <tgt>一歩、深く浅く。</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>我仿佛听到了他们</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>放歌太行山上</src> <tgt>太行山に響く</tgt>; start=11.00, end=12.00
12. <src>的声音，</src> <tgt>彼らの歌声が聞こえるようだ。</tgt>; start=12.00, end=13.00
13. <src>时而高，</src> <tgt>時には高く、</tgt>; start=13.00, end=14.00
14. <src>时而低，</src> <tgt>時には低く、</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>时而欢快，</src> <tgt>時には快活に、</tgt>; start=16.00, end=17.00
17. <src>时而呜咽。</src> <tgt>時には咽び泣くように。</tgt>; start=17.00, end=17.84
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_B00021_S00398_W000012 ===

source:
- language: Chinese
- transcription: 三月二十二号，美国证券交易委员会宣布对加密资产企业家孙宇晨及其三家全资公司提起诉讼，指控他们没有经过注册提供和出售加密资产证券Tronics和BitTorrent。
- source_tokens:
  0. 三
  1. 月
  2. 二十二
  3. 号，
  4. 美国
  5. 证券
  6. 交易
  7. 委员
  8. 会
  9. 宣布
  10. 对
  11. 加密
  12. 资产
  13. 企业
  14. 家
  15. 孙
  16. 宇晨
  17. 及
  18. 其
  19. 三
  20. 家
  21. 全资
  22. 公司
  23. 提起
  24. 诉讼，
  25. 指控
  26. 他们
  27. 没有
  28. 经过
  29. 注册
  30. 提供
  31. 和
  32. 出售
  33. 加密
  34. 资产
  35. 证券
  36. Tronics
  37. 和
  38. BitTorrent。

target:
- language: Japanese
- translation: 3月22日、米証券取引委員会（SEC）が暗号資産起業家の孫宇晨（ジャスティン・サン）氏とその全額出資子会社3社を提訴しました。未登録の暗号資産証券「Tronix」および「BitTorrent」を提供・販売したとして、SECは発表しました。
- target_sense_units:
  0. 3月22日、
  1. 米証券取引委員会（SEC）が
  2. 暗号資産起業家の
  3. 孫宇晨（ジャスティン・サン）氏と
  4. その全額出資子会社
  5. 3社を
  6. 提訴しました。
  7. 未登録の
  8. 暗号資産証券「Tronix」および「BitTorrent」を
  9. 提供・販売したとして、
  10. SECは
  11. 発表しました。

scratchpad:
* target[0]: "3月22日、"
  - source_tokens: `0: "三", 1: "月", 2: "二十二", 3: "号，"`
  - mapping_reason: Date expression.

* target[1]: "米証券取引委員会（SEC）が"
  - source_tokens: `4: "美国", 5: "证券", 6: "交易", 7: "委员", 8: "会"`
  - mapping_reason: Subject of the legal action.

* target[2]: "暗号資産起業家の"
  - source_tokens: `11: "加密", 12: "资产", 13: "企业", 14: "家"`
  - mapping_reason: Descriptor for the individual.

* target[3]: "孫宇晨（ジャスティン・サン）氏と"
  - source_tokens: `15: "孙", 16: "宇晨"`
  - mapping_reason: The individual being sued.

* target[4]: "その全額出資子会社"
  - source_tokens: `18: "其", 21: "全资", 22: "公司"`
  - mapping_reason: The entities owned by the individual.

* target[5]: "3社を"
  - source_tokens: `19: "三", 20: "家"`
  - mapping_reason: Quantity of entities.

* target[6]: "提訴しました。"
  - source_tokens: `23: "提起", 24: "诉讼，"`
  - mapping_reason: Legal action verb.

* target[7]: "未登録の"
  - source_tokens: `27: "没有", 28: "经过", 29: "注册"`
  - mapping_reason: Lack of registration condition.

* target[8]: "暗号資産証券「Tronix」および「BitTorrent」を"
  - source_tokens: `33: "加密", 34: "资产", 35: "证券", 36: "Tronics", 37: "和", 38: "BitTorrent。"`
  - mapping_reason: The subject of the offering.

* target[9]: "提供・販売したとして、"
  - source_tokens: `30: "提供", 31: "和", 32: "出售", 25: "指控"`
  - mapping_reason: The allegation of offering and selling.

* target[10]: "SECは"
  - source_tokens: `4: "美国", 5: "证券", 6: "交易", 7: "委员", 8: "会"`
  - mapping_reason: The entity making the announcement.

* target[11]: "発表しました。"
  - source_tokens: `9: "宣布"`
  - mapping_reason: The action of announcing.

result:
```html
0. <src>三月二十二号，</src> <tgt>3月22日、</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>美国证券交易委员会</src> <tgt>米証券取引委員会（SEC）が</tgt>; start=2.00, end=3.00
3. <src>宣布对加密资产</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>企业家孙宇晨</src> <tgt>暗号資産起業家の孫宇晨（ジャスティン・サン）氏と</tgt>; start=4.00, end=5.00
5. <src>及其</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>三家全资公司</src> <tgt>その全額出資子会社3社を</tgt>; start=6.00, end=7.00
7. <src>提起诉讼，</src> <tgt>提訴しました。</tgt>; start=7.00, end=8.00
8. <src>指控他们没有经过注册</src> <tgt>未登録の</tgt>; start=8.00, end=9.00
9. <src>提供和出售</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>加密资产证券</src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Tronics和BitTorrent。</src> <tgt>暗号資産証券「Tronix」および「BitTorrent」を提供・販売したとして、SECは発表しました。</tgt>; start=12.00, end=12.51
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同样
  1. 也是
  2. 针对
  3. 要
  4. 留意
  5. 金钱
  6. 的
  7. 部分，
  8. 我们
  9. 从
  10. 这里
  11. 呢
  12. 可以
  13. 看到
  14. 的
  15. 是
  16. 这
  17. 一
  18. 副
  19. 卡片，
  20. 它
  21. 代表
  22. 的
  23. 是
  24. 手。
  25. 那么
  26. 手
  27. 的
  28. 时候
  29. 呢，
  30. 通常
  31. 它
  32. 非常
  33. 的
  34. 直白，
  35. 代表
  36. 是
  37. 我们
  38. 的
  39. 金钱
  40. 呢，
  41. 可能
  42. 就
  43. 尽量
  44. 呢
  45. 不要，
  46. 就是
  47. 做
  48. 太多
  49. 的
  50. 规划，
  51. 尤其
  52. 是
  53. 针对
  54. 家中
  55. 的
  56. 男性
  57. 长男。

target:
- language: English
- translation: Now, regarding being careful with money, what we see here is this hand card. The hand is usually very straightforward—it means that for our money, maybe we shouldn't plan too much, especially when it comes to the eldest male in the family.
- target_sense_units:
  0. Now, regarding
  1. being careful with
  2. money,
  3. what we see here is
  4. this hand card.
  5. The hand is
  6. usually very straightforward—
  7. it means that
  8. for our money,
  9. maybe we shouldn't
  10. plan too much,
  11. especially when
  12. it comes to
  13. the eldest male
  14. in the family.

scratchpad:
* target[0]: "Now, regarding"
  - source_tokens: `0: "同样", 1: "也是", 2: "针对"`
  - mapping_reason: "同样也是" (Now/also) + "针对" (regarding)

* target[1]: "being careful with"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: "要留意" (need to pay attention to/be careful with)

* target[2]: "money,"
  - source_tokens: `5: "金钱"`
  - mapping_reason: "金钱" (money)

* target[3]: "what we see here is"
  - source_tokens: `8: "我们", 9: "从", 10: "这里", 11: "呢", 12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: "我们从这里可以看到的是" (what we see here is)

* target[4]: "this hand card."
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片", 24: "手"`
  - mapping_reason: "这一副卡片" (this card) + "手" (hand)

* target[5]: "The hand is"
  - source_tokens: `26: "手"`
  - mapping_reason: "手" (The hand)

* target[6]: "usually very straightforward—"
  - source_tokens: `30: "通常", 31: "它", 32: "非常", 33: "的", 34: "直白"`
  - mapping_reason: "通常它非常直白" (usually very straightforward)

* target[7]: "it means that"
  - source_tokens: `21: "代表", 22: "的", 23: "是", 35: "代表", 36: "是"`
  - mapping_reason: "代表的是" (it means that)

* target[8]: "for our money,"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱"`
  - mapping_reason: "我们的金钱" (our money)

* target[9]: "maybe we shouldn't"
  - source_tokens: `41: "可能", 43: "尽量", 45: "不要"`
  - mapping_reason: "可能" (maybe) + "尽量不要" (shouldn't)

* target[10]: "plan too much,"
  - source_tokens: `47: "做", 48: "太多", 49: "的", 50: "规划"`
  - mapping_reason: "做太多的规划" (plan too much)

* target[11]: "especially when"
  - source_tokens: `51: "尤其", 52: "是"`
  - mapping_reason: "尤其是" (especially)

* target[12]: "it comes to"
  - source_tokens: `53: "针对"`
  - mapping_reason: "针对" (regarding/when it comes to)

* target[13]: "the eldest male"
  - source_tokens: `56: "男性", 57: "长男"`
  - mapping_reason: "男性长男" (eldest male)

* target[14]: "in the family."
  - source_tokens: `54: "家中"`
  - mapping_reason: "家中" (in the family)

result:
```html
0. <src>同样也是</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>针对要留意</src> <tgt>Now, regarding being careful with</tgt>; start=1.00, end=2.00
2. <src>金钱的部分，</src> <tgt>money,</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>我们从这里呢</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>可以看到的是</src> <tgt>what we see here is</tgt>; start=5.00, end=6.00
6. <src>这一副卡片，</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>它代表的是</src> <tgt><|wait|></tgt>; start=7.00, end=8.00
8. <src>手。</src> <tgt>this hand card.</tgt>; start=8.00, end=9.00
9. <src>那么</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>手的时候呢，</src> <tgt>The hand is</tgt>; start=10.00, end=11.00
11. <src>通常</src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>它非常</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>的直白，</src> <tgt>usually very straightforward—</tgt>; start=13.00, end=14.00
14. <src>代表是我们的金钱</src> <tgt>it means that for our money,</tgt>; start=14.00, end=15.00
15. <src>呢，</src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>可能就尽量呢</src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>不要，</src> <tgt>maybe we shouldn't</tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>就是做太多</src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>的规划，</src> <tgt>plan too much,</tgt>; start=20.00, end=21.00
21. <src>尤其是</src> <tgt>especially when</tgt>; start=21.00, end=22.00
22. <src><|wait|></src> <tgt><|wait|></tgt>; start=22.00, end=23.00
23. <src>针对家中的男性</src> <tgt>it comes to</tgt>; start=23.00, end=24.00
24. <src>长男。</src> <tgt>the eldest male in the family.</tgt>; start=24.00, end=24.87
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_B00021_S06758_W000029 ===

source:
- language: Chinese
- transcription: 我仿佛看到了他们游走在太行山上的足迹，深一脚浅一脚；我仿佛听到了他们放歌太行山上的声音，时而高，时而低，时而欢快，时而呜咽。
- source_tokens:
  0. 我
  1. 仿佛
  2. 看到
  3. 了
  4. 他们
  5. 游走
  6. 在
  7. 太行
  8. 山
  9. 上
  10. 的
  11. 足迹，
  12. 深
  13. 一
  14. 脚
  15. 浅
  16. 一
  17. 脚；
  18. 我
  19. 仿佛
  20. 听到
  21. 了
  22. 他们
  23. 放歌
  24. 太行
  25. 山
  26. 上
  27. 的
  28. 声音，
  29. 时
  30. 而
  31. 高，
  32. 时
  33. 而
  34. 低，
  35. 时
  36. 而
  37. 欢快，
  38. 时
  39. 而
  40. 呜
  41. 咽。

target:
- language: Korean
- translation: 태항산을 누비는 그들의 발자취가 보이는 듯합니다. 깊게 얕게 내딛는 그 발걸음이요. 태항산에 울려 퍼지는 그들의 노래 소리가 들리는 듯합니다. 때로는 높게, 때로는 낮게, 때로는 즐겁게, 또 때로는 흐느끼듯 합니다.
- target_sense_units:
  0. 태항산을 누비는
  1. 그들의 발자취가
  2. 보이는 듯합니다.
  3. 깊게 얕게 내딛는
  4. 그 발걸음이요.
  5. 태항산에
  6. 울려 퍼지는
  7. 그들의 노래 소리가
  8. 들리는 듯합니다.
  9. 때로는
  10. 높게,
  11. 때로는
  12. 낮게,
  13. 때로는
  14. 즐겁게,
  15. 또
  16. 때로는
  17. 흐느끼듯 합니다.

scratchpad:
* target[0]: "태항산을 누비는"
  - source_tokens: `7: "太行", 8: "山", 6: "在", 5: "游走"`
  - mapping_reason: "太行山" (7,8) is the location, "游走" (5) is the action, "在" (6) links them.
* target[1]: "그들의 발자취가"
  - source_tokens: `4: "他们", 11: "足迹"`
  - mapping_reason: "他们" (4) refers to "그들의", "足迹" (11) is "발자취".
* target[2]: "보이는 듯합니다."
  - source_tokens: `0: "我", 1: "仿佛", 2: "看到", 3: "了"`
  - mapping_reason: "我" (0) is the subject of perception, "仿佛" (1) is "듯합니다", "看到" (2) and "了" (3) form "보이는".
* target[3]: "깊게 얕게 내딛는"
  - source_tokens: `12: "深", 13: "一", 14: "脚", 15: "浅", 16: "一", 17: "脚"`
  - mapping_reason: Direct mapping of the phrase "深一脚浅一脚".
* target[4]: "그 발걸음이요."
  - source_tokens: `11: "足迹"`
  - mapping_reason: Refers back to the "足迹" (11) mentioned previously.
* target[5]: "태항산에"
  - source_tokens: `24: "太行", 25: "山", 26: "上"`
  - mapping_reason: Location of the sound.
* target[6]: "울려 퍼지는"
  - source_tokens: `23: "放歌"`
  - mapping_reason: "放歌" implies singing/resounding.
* target[7]: "그들의 노래 소리가"
  - source_tokens: `22: "他们", 28: "声音"`
  - mapping_reason: "他们" (22) is "그들의", "声音" (28) is "노래 소리" (in context of 放歌).
* target[8]: "들리는 듯합니다."
  - source_tokens: `18: "我", 19: "仿佛", 20: "听到", 21: "了"`
  - mapping_reason: "我" (18) is subject, "仿佛" (19) is "듯합니다", "听到" (20) and "了" (21) form "들리는".
* target[9]: "때로는"
  - source_tokens: `29: "时", 30: "而"`
  - mapping_reason: "时而" maps to "때로는".
* target[10]: "높게,"
  - source_tokens: `31: "高"`
  - mapping_reason: "高" maps to "높게".
* target[11]: "때로는"
  - source_tokens: `32: "时", 33: "而"`
  - mapping_reason: "时而" maps to "때로는".
* target[12]: "낮게,"
  - source_tokens: `34: "低"`
  - mapping_reason: "低" maps to "낮게".
* target[13]: "때로는"
  - source_tokens: `35: "时", 36: "而"`
  - mapping_reason: "时而" maps to "때로는".
* target[14]: "즐겁게,"
  - source_tokens: `37: "欢快"`
  - mapping_reason: "欢快" maps to "즐겁게".
* target[15]: "또"
  - source_tokens: `38: "时"`
  - mapping_reason: Connective "또" maps to the next "时".
* target[16]: "때로는"
  - source_tokens: `39: "而"`
  - mapping_reason: "而" maps to "때로는".
* target[17]: "흐느끼듯 합니다."
  - source_tokens: `40: "呜", 41: "咽"`
  - mapping_reason: "呜咽" maps to "흐느끼듯 합니다".

result:
```html
0. <src><|wait|></src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>我仿佛看到了</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>他们游走</src> <tgt><|wait|></tgt>; start=2.00, end=3.00
3. <src>在太行山上</src> <tgt>태항산을 누비는</tgt>; start=3.00, end=4.00
4. <src>的足迹，</src> <tgt>그들의 발자취가 보이는 듯합니다.</tgt>; start=4.00, end=5.00
5. <src>深一脚</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src><|wait|></src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>浅一脚；</src> <tgt>깊게 얕게 내딛는 그 발걸음이요.</tgt>; start=7.00, end=8.00
8. <src><|wait|></src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>我仿佛听到了他们</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src><|wait|></src> <tgt><|wait|></tgt>; start=10.00, end=11.00
11. <src>放歌太行山上</src> <tgt>태항산에 울려 퍼지는</tgt>; start=11.00, end=12.00
12. <src>的声音，</src> <tgt>그들의 노래 소리가 들리는 듯합니다.</tgt>; start=12.00, end=13.00
13. <src>时而高，</src> <tgt>때로는 높게,</tgt>; start=13.00, end=14.00
14. <src>时而低，</src> <tgt>때로는 낮게,</tgt>; start=14.00, end=15.00
15. <src><|wait|></src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>时而欢快，</src> <tgt>때로는 즐겁게,</tgt>; start=16.00, end=17.00
17. <src>时而呜咽。</src> <tgt>또 때로는 흐느끼듯 합니다.</tgt>; start=17.00, end=17.84
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_B00021_S00398_W000012 ===

source:
- language: Chinese
- transcription: 三月二十二号，美国证券交易委员会宣布对加密资产企业家孙宇晨及其三家全资公司提起诉讼，指控他们没有经过注册提供和出售加密资产证券Tronics和BitTorrent。
- source_tokens:
  0. 三
  1. 月
  2. 二十二
  3. 号，
  4. 美国
  5. 证券
  6. 交易
  7. 委员
  8. 会
  9. 宣布
  10. 对
  11. 加密
  12. 资产
  13. 企业
  14. 家
  15. 孙
  16. 宇晨
  17. 及
  18. 其
  19. 三
  20. 家
  21. 全资
  22. 公司
  23. 提起
  24. 诉讼，
  25. 指控
  26. 他们
  27. 没有
  28. 经过
  29. 注册
  30. 提供
  31. 和
  32. 出售
  33. 加密
  34. 资产
  35. 证券
  36. Tronics
  37. 和
  38. BitTorrent。

target:
- language: English
- translation: On March 22nd, the U.S. Securities and Exchange Commission announced it has filed a lawsuit against crypto-asset entrepreneur Justin Sun and three of his wholly-owned companies. The SEC accuses them of offering and selling the unregistered crypto-asset securities Tronix and BitTorrent.
- target_sense_units:
  0. On March 22nd,
  1. the U.S. Securities and Exchange Commission
  2. announced
  3. it has filed
  4. a lawsuit against
  5. crypto- asset entrepreneur
  6. Justin Sun
  7. and three of his
  8. wholly- owned companies.
  9. The SEC
  10. accuses them of
  11. offering and selling
  12. the unregistered crypto- asset securities
  13. Tronix and BitTorrent.

scratchpad:
* target[0]: "On March 22nd,"
  - source_tokens: `0: "三", 1: "月", 2: "二十二", 3: "号，"`
  - mapping_reason: Temporal expression.
* target[1]: "the U.S. Securities and Exchange Commission"
  - source_tokens: `4: "美国", 5: "证券", 6: "交易", 7: "委员", 8: "会"`
  - mapping_reason: Subject entity.
* target[2]: "announced"
  - source_tokens: `9: "宣布"`
  - mapping_reason: Main verb.
* target[3]: "it has filed"
  - source_tokens: `23: "提起"`
  - mapping_reason: Action of filing.
* target[4]: "a lawsuit against"
  - source_tokens: `10: "对", 24: "诉讼，"`
  - mapping_reason: Legal action and target preposition.
* target[5]: "crypto- asset entrepreneur"
  - source_tokens: `11: "加密", 12: "资产", 13: "企业", 14: "家"`
  - mapping_reason: Description of the defendant.
* target[6]: "Justin Sun"
  - source_tokens: `15: "孙", 16: "宇晨"`
  - mapping_reason: Name of the defendant.
* target[7]: "and three of his"
  - source_tokens: `17: "及", 18: "其", 19: "三", 20: "家"`
  - mapping_reason: Conjunction and count of companies.
* target[8]: "wholly- owned companies."
  - source_tokens: `21: "全资", 22: "公司"`
  - mapping_reason: Description of the companies.
* target[9]: "The SEC"
  - source_tokens: `4: "美国", 5: "证券", 6: "交易", 7: "委员", 8: "会"`
  - mapping_reason: Reference to the previously mentioned entity.
* target[10]: "accuses them of"
  - source_tokens: `25: "指控", 26: "他们"`
  - mapping_reason: Secondary verb and object pronoun.
* target[11]: "offering and selling"
  - source_tokens: `30: "提供", 31: "和", 32: "出售"`
  - mapping_reason: Alleged illegal actions.
* target[12]: "the unregistered crypto- asset securities"
  - source_tokens: `27: "没有", 28: "经过", 29: "注册", 33: "加密", 34: "资产", 35: "证券"`
  - mapping_reason: Description of the assets and legal status.
* target[13]: "Tronix and BitTorrent."
  - source_tokens: `36: "Tronics", 37: "和", 38: "BitTorrent。"`
  - mapping_reason: Names of the securities.

result:
```html
0. <src>三月二十二号，</src> <tgt>On March 22nd,</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>美国证券交易委员会</src> <tgt>the U.S. Securities and Exchange Commission</tgt>; start=2.00, end=3.00
3. <src>宣布对加密资产</src> <tgt>announced</tgt>; start=3.00, end=4.00
4. <src>企业家孙宇晨</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>及其</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>三家全资公司</src> <tgt><|wait|></tgt>; start=6.00, end=7.00
7. <src>提起诉讼，</src> <tgt>it has filed a lawsuit against crypto- asset entrepreneur Justin Sun and three of his wholly- owned companies. The SEC</tgt>; start=7.00, end=8.00
8. <src>指控他们没有经过注册</src> <tgt>accuses them of</tgt>; start=8.00, end=9.00
9. <src>提供和出售</src> <tgt>offering and selling</tgt>; start=9.00, end=10.00
10. <src>加密资产证券</src> <tgt>the unregistered crypto- asset securities</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Tronics和BitTorrent。</src> <tgt>Tronix and BitTorrent.</tgt>; start=12.00, end=12.51
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_B00021_S00398_W000012 ===

source:
- language: Chinese
- transcription: 三月二十二号，美国证券交易委员会宣布对加密资产企业家孙宇晨及其三家全资公司提起诉讼，指控他们没有经过注册提供和出售加密资产证券Tronics和BitTorrent。
- source_tokens:
  0. 三
  1. 月
  2. 二十二
  3. 号，
  4. 美国
  5. 证券
  6. 交易
  7. 委员
  8. 会
  9. 宣布
  10. 对
  11. 加密
  12. 资产
  13. 企业
  14. 家
  15. 孙
  16. 宇晨
  17. 及
  18. 其
  19. 三
  20. 家
  21. 全资
  22. 公司
  23. 提起
  24. 诉讼，
  25. 指控
  26. 他们
  27. 没有
  28. 经过
  29. 注册
  30. 提供
  31. 和
  32. 出售
  33. 加密
  34. 资产
  35. 证券
  36. Tronics
  37. 和
  38. BitTorrent。

target:
- language: Korean
- translation: 3월 22일, 미국 증권거래위원회(SEC)는 암호화폐 기업가 저스틴 선과 그의 100% 자회사 3곳을 상대로 소송을 제기했다고 발표했습니다. 이들은 미등록 암호화폐 증권인 '트론(Tronix)'과 '비트토렌트(BitTorrent)'를 제공 및 판매한 혐의를 받고 있습니다.
- target_sense_units:
  0. 3월 22일,
  1. 미국 증권거래위원회( SEC) 는
  2. 암호화폐 기업가
  3. 저스틴 선과
  4. 그의
  5. 100% 자회사
  6. 3곳을
  7. 상대로
  8. 소송을
  9. 제기했다고
  10. 발표했습니다.
  11. 이들은
  12. 미등록 암호화폐 증권인
  13. ' 트론( Tronix) '
  14. 과
  15. ' 비트토렌트( BitTorrent) '
  16. 를
  17. 제공 및 판매한
  18. 혐의를
  19. 받고 있습니다.

scratchpad:
* target[0]: "3월 22일,"
  - source_tokens: `0: "三", 1: "月", 2: "二十二", 3: "号，"`
  - mapping_reason: Date expression.
* target[1]: "미국 증권거래위원회( SEC) 는"
  - source_tokens: `4: "美国", 5: "证券", 6: "交易", 7: "委员", 8: "会"`
  - mapping_reason: Subject of the sentence.
* target[2]: "암호화폐 기업가"
  - source_tokens: `11: "加密", 12: "资产", 13: "企业", 14: "家"`
  - mapping_reason: Descriptor for the subject of the lawsuit.
* target[3]: "저스틴 선과"
  - source_tokens: `15: "孙", 16: "宇晨", 17: "及"`
  - mapping_reason: Target of the lawsuit.
* target[4]: "그의"
  - source_tokens: `18: "其"`
  - mapping_reason: Possessive pronoun.
* target[5]: "100% 자회사"
  - source_tokens: `21: "全资", 22: "公司"`
  - mapping_reason: Description of the companies.
* target[6]: "3곳을"
  - source_tokens: `19: "三", 20: "家"`
  - mapping_reason: Quantity of the companies.
* target[7]: "상대로"
  - source_tokens: `10: "对"`
  - mapping_reason: Preposition indicating the object of the lawsuit.
* target[8]: "소송을"
  - source_tokens: `24: "诉讼，"`
  - mapping_reason: Object of the legal action.
* target[9]: "제기했다고"
  - source_tokens: `23: "提起"`
  - mapping_reason: Verb of the legal action.
* target[10]: "발표했습니다."
  - source_tokens: `9: "宣布"`
  - mapping_reason: Main verb of the first sentence.
* target[11]: "이들은"
  - source_tokens: `26: "他们"`
  - mapping_reason: Pronoun referring to the accused.
* target[12]: "미등록 암호화폐 증권인"
  - source_tokens: `27: "没有", 28: "经过", 29: "注册", 33: "加密", 34: "资产", 35: "证券"`
  - mapping_reason: Description of the illegal assets.
* target[13]: "' 트론( Tronix) '"
  - source_tokens: `36: "Tronics"`
  - mapping_reason: Specific asset name.
* target[14]: "과"
  - source_tokens: `31: "和"`
  - mapping_reason: Conjunction.
* target[15]: "' 비트토렌트( BitTorrent) '"
  - source_tokens: `38: "BitTorrent。"`
  - mapping_reason: Specific asset name.
* target[16]: "를"
  - source_tokens: `37: "和"`
  - mapping_reason: Particle for the object.
* target[17]: "제공 및 판매한"
  - source_tokens: `30: "提供", 31: "和", 32: "出售"`
  - mapping_reason: Actions performed by the accused.
* target[18]: "혐의를"
  - source_tokens: `25: "指控"`
  - mapping_reason: Legal allegation.
* target[19]: "받고 있습니다."
  - source_tokens: `25: "指控"`
  - mapping_reason: State of being accused.

result:
```html
0. <src>三月二十二号，</src> <tgt>3월 22일,</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>美国证券交易委员会</src> <tgt>미국 증권거래위원회( SEC) 는</tgt>; start=2.00, end=3.00
3. <src>宣布对加密资产</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>企业家孙宇晨</src> <tgt>암호화폐 기업가</tgt>; start=4.00, end=5.00
5. <src>及其</src> <tgt>저스틴 선과 그의</tgt>; start=5.00, end=6.00
6. <src>三家全资公司</src> <tgt>100% 자회사 3곳을 상대로</tgt>; start=6.00, end=7.00
7. <src>提起诉讼，</src> <tgt>소송을 제기했다고 발표했습니다.</tgt>; start=7.00, end=8.00
8. <src>指控他们没有经过注册</src> <tgt>이들은</tgt>; start=8.00, end=9.00
9. <src>提供和出售</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>加密资产证券</src> <tgt>미등록 암호화폐 증권인</tgt>; start=10.00, end=11.00
11. <src><|wait|></src> <tgt><|wait|></tgt>; start=11.00, end=12.00
12. <src>Tronics和BitTorrent。</src> <tgt>' 트론( Tronix) ' 과 ' 비트토렌트( BitTorrent) ' 를 제공 및 판매한 혐의를 받고 있습니다.</tgt>; start=12.00, end=12.51
```

- max_empty_window_count: 1


attempts:

- retry: 0/5
  status: succeeded
  reason: initial attempt succeeded

---
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同样
  1. 也是
  2. 针对
  3. 要
  4. 留意
  5. 金钱
  6. 的
  7. 部分，
  8. 我们
  9. 从
  10. 这里
  11. 呢
  12. 可以
  13. 看到
  14. 的
  15. 是
  16. 这
  17. 一
  18. 副
  19. 卡片，
  20. 它
  21. 代表
  22. 的
  23. 是
  24. 手。
  25. 那么
  26. 手
  27. 的
  28. 时候
  29. 呢，
  30. 通常
  31. 它
  32. 非常
  33. 的
  34. 直白，
  35. 代表
  36. 是
  37. 我们
  38. 的
  39. 金钱
  40. 呢，
  41. 可能
  42. 就
  43. 尽量
  44. 呢
  45. 不要，
  46. 就是
  47. 做
  48. 太多
  49. 的
  50. 规划，
  51. 尤其
  52. 是
  53. 针对
  54. 家中
  55. 的
  56. 男性
  57. 长男。

target:
- language: Korean
- translation: 돈을 조심해야 하는 부분도 마찬가지예요. 여기 이 카드를 보면, 이건 손을 상징해요. 손은 보통 아주 직설적이에요. 그래서 돈에 대해서는 너무 많은 계획을 세우지 않는 게 좋다는 걸 의미해요. 특히 집안의 장남이라면 더욱 그렇습니다.
- target_sense_units:
  0. 돈을
  1. 조심해야 하는
  2. 부분도
  3. 마찬가지예요.
  4. 여기 이 카드를 보면,
  5. 이건
  6. 손을
  7. 상징해요.
  8. 손은
  9. 보통
  10. 아주
  11. 직설적이에요.
  12. 그래서
  13. 돈에 대해서는
  14. 너무 많은 계획을
  15. 세우지 않는 게
  16. 좋다는 걸
  17. 의미해요.
  18. 특히
  19. 집안의 장남이라면
  20. 더욱 그렇습니다.

scratchpad:
* target[0]: "돈을"
  - source_tokens: `5: "金钱"`
  - mapping_reason: "Refers to money."
* target[1]: "조심해야 하는"
  - source_tokens: `4: "留意"`
  - mapping_reason: "Refers to being careful/mindful."
* target[2]: "부분도"
  - source_tokens: `7: "部分"`
  - mapping_reason: "Refers to the part/aspect."
* target[3]: "마찬가지예요."
  - source_tokens: `0: "同样", 1: "也是", 2: "针对"`
  - mapping_reason: "Refers to the same aspect/topic."
* target[4]: "여기 이 카드를 보면,"
  - source_tokens: `9: "从", 10: "这里", 13: "看到", 16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: "Refers to seeing the card here."
* target[5]: "이건"
  - source_tokens: `20: "它"`
  - mapping_reason: "Refers to the card."
* target[6]: "손을"
  - source_tokens: `24: "手"`
  - mapping_reason: "Refers to the hand."
* target[7]: "상징해요."
  - source_tokens: `21: "代表"`
  - mapping_reason: "Refers to representing something."
* target[8]: "손은"
  - source_tokens: `26: "手"`
  - mapping_reason: "Refers to the hand again."
* target[9]: "보통"
  - source_tokens: `30: "通常"`
  - mapping_reason: "Refers to usually."
* target[10]: "아주"
  - source_tokens: `32: "非常"`
  - mapping_reason: "Refers to very."
* target[11]: "직설적이에요."
  - source_tokens: `34: "直白"`
  - mapping_reason: "Refers to being straightforward."
* target[12]: "그래서"
  - source_tokens: `25: "那么"`
  - mapping_reason: "Refers to the connector 'so/then'."
* target[13]: "돈에 대해서는"
  - source_tokens: `37: "我们", 39: "金钱"`
  - mapping_reason: "Refers to our money."
* target[14]: "너무 많은 계획을"
  - source_tokens: `48: "太多", 50: "规划"`
  - mapping_reason: "Refers to too many plans."
* target[15]: "세우지 않는 게"
  - source_tokens: `45: "不要", 47: "做"`
  - mapping_reason: "Refers to not doing (the plans)."
* target[16]: "좋다는 걸"
  - source_tokens: `45: "不要", 47: "做", 48: "太多", 50: "规划"`
  - mapping_reason: "Summarizes the advice against planning."
* target[17]: "의미해요."
  - source_tokens: `35: "代表"`
  - mapping_reason: "Refers to meaning/representing."
* target[18]: "특히"
  - source_tokens: `51: "尤其"`
  - mapping_reason: "Refers to especially."
* target[19]: "집안의 장남이라면"
  - source_tokens: `53: "针对", 54: "家中", 56: "男性", 57: "长男"`
  - mapping_reason: "Refers to the eldest son of the household."
* target[20]: "더욱 그렇습니다."
  - source_tokens: `51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: "Reinforces the advice specifically for the eldest son."

result:
```html
0. <src>同样也是</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>针对要留意</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>金钱的部分，</src> <tgt>돈을 조심해야 하는 부분도 마찬가지예요.</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>我们从这里呢</src> <tgt><|wait|></tgt>; start=4.00, end=5.00
5. <src>可以看到的是</src> <tgt><|wait|></tgt>; start=5.00, end=6.00
6. <src>这一副卡片，</src> <tgt>여기 이 카드를 보면,</tgt>; start=6.00, end=7.00
7. <src>它代表的是</src> <tgt>이건</tgt>; start=7.00, end=8.00
8. <src>手。</src> <tgt>손을 상징해요.</tgt>; start=8.00, end=9.00
9. <src>那么</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>手的时候呢，</src> <tgt>손은</tgt>; start=10.00, end=11.00
11. <src>通常</src> <tgt>보통</tgt>; start=11.00, end=12.00
12. <src>它非常</src> <tgt>아주</tgt>; start=12.00, end=13.00
13. <src>的直白，</src> <tgt>직설적이에요. 그래서</tgt>; start=13.00, end=14.00
14. <src>代表是我们的金钱</src> <tgt>돈에 대해서는</tgt>; start=14.00, end=15.00
15. <src>呢，</src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>可能就尽量呢</src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>不要，</src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>就是做太多</src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>的规划，</src> <tgt>너무 많은 계획을 세우지 않는 게 좋다는 걸 의미해요.</tgt>; start=20.00, end=21.00
21. <src>尤其是</src> <tgt>특히</tgt>; start=21.00, end=22.00
22. <src><|wait|></src> <tgt><|wait|></tgt>; start=22.00, end=23.00
23. <src>针对家中的男性</src> <tgt><|wait|></tgt>; start=23.00, end=24.00
24. <src>长男。</src> <tgt>집안의 장남이라면 더욱 그렇습니다.</tgt>; start=24.00, end=24.87
```

- max_empty_window_count: 5


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[16]
  - verdict: mapping_error
  - reason: "The target unit '좋다는 걸' summarizes the advice against planning, which is better captured by the source tokens describing the planning action rather than just the modifier '尽量'."
  - replace_source_tokens: 45: "不要", 47: "做", 48: "太多", 50: "规划"

* target[20]
  - verdict: mapping_error
  - reason: "The target unit '더욱 그렇습니다.' encompasses the context of the advice for the eldest son, which is covered by tokens 51-57. Token 52 alone is insufficient."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"
  validation:
    scratchpad:
* target[0]: "돈을"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Core object of the target unit.
* target[1]: "조심해야 하는"
  - source_tokens: `4: "留意"`
  - mapping_reason: Verb meaning 'to be careful/pay attention'.
* target[2]: "부분도"
  - source_tokens: `7: "部分，"`
  - mapping_reason: Refers to the aspect/part mentioned.
* target[3]: "마찬가지예요."
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Indicates similarity/likewise.
* target[4]: "여기 이 카드를 보면,"
  - source_tokens: `9: "从", 10: "这里", 16: "这", 17: "一", 18: "副", 19: "卡片，", 13: "看到"`
  - mapping_reason: Location and visual reference.
* target[5]: "이건"
  - source_tokens: `20: "它"`
  - mapping_reason: Pronoun referring to the card.
* target[6]: "손을"
  - source_tokens: `24: "手。"`
  - mapping_reason: Symbol being represented.
* target[7]: "상징해요."
  - source_tokens: `21: "代表"`
  - mapping_reason: Verb meaning 'to represent/symbolize'.
* target[8]: "손은"
  - source_tokens: `26: "手"`
  - mapping_reason: Subject of the next clause.
* target[9]: "보통"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb of frequency.
* target[10]: "아주"
  - source_tokens: `32: "非常"`
  - mapping_reason: Degree adverb.
* target[11]: "직설적이에요."
  - source_tokens: `34: "直白，"`
  - mapping_reason: Adjective describing the hand.
* target[12]: "그래서"
  - source_tokens: `25: "那么"`
  - mapping_reason: Discourse connective indicating consequence.
* target[13]: "돈에 대해서는"
  - source_tokens: `39: "金钱"`
  - mapping_reason: Topic of the advice.
* target[14]: "너무 많은 계획을"
  - source_tokens: `48: "太多", 50: "规划，"`
  - mapping_reason: Content of the financial plan.
* target[15]: "세우지 않는 게"
  - source_tokens: `45: "不要，", 47: "做"`
  - mapping_reason: Negative instruction/action.
* target[16]: "좋다는 걸"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Suggestion/preference.
* target[17]: "의미해요."
  - source_tokens: `35: "代表"`
  - mapping_reason: Verb meaning 'to mean/signify'.
* target[18]: "특히"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis marker.
* target[19]: "집안의 장남이라면"
  - source_tokens: `54: "家中", 56: "男性", 57: "长男。"`
  - mapping_reason: Target demographic for the specific advice.
* target[20]: "더욱 그렇습니다."
  - source_tokens: `52: "是"`
  - mapping_reason: Emphatic confirmation.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [4]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [7]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [0, 1]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [9, 10, 13, 16, 17, 18, 19]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [20]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [24]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [21]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [26]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [30]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [32]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [34]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [25]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [39]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [48, 50]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [45, 47]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [43]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [35]
  },
  {
    "target_senseunit_id": 18,
    "source_token_ids": [51]
  },
  {
    "target_senseunit_id": 19,
    "source_token_ids": [54, 56, 57]
  },
  {
    "target_senseunit_id": 20,
    "source_token_ids": [52]
  }
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同样
  1. 也是
  2. 针对
  3. 要
  4. 留意
  5. 金钱
  6. 的
  7. 部分，
  8. 我们
  9. 从
  10. 这里
  11. 呢
  12. 可以
  13. 看到
  14. 的
  15. 是
  16. 这
  17. 一
  18. 副
  19. 卡片，
  20. 它
  21. 代表
  22. 的
  23. 是
  24. 手。
  25. 那么
  26. 手
  27. 的
  28. 时候
  29. 呢，
  30. 通常
  31. 它
  32. 非常
  33. 的
  34. 直白，
  35. 代表
  36. 是
  37. 我们
  38. 的
  39. 金钱
  40. 呢，
  41. 可能
  42. 就
  43. 尽量
  44. 呢
  45. 不要，
  46. 就是
  47. 做
  48. 太多
  49. 的
  50. 规划，
  51. 尤其
  52. 是
  53. 针对
  54. 家中
  55. 的
  56. 男性
  57. 长男。

target:
- language: Japanese
- translation: お金に注意すべき点についてですが、ここで見えているのはこのカードです。これは「手」を表しています。手というのは通常、とてもストレートで、お金に関してはあまり計画を立てすぎない方がいいということを示しています。特に家庭の長男についてはそうです。
- target_sense_units:
  0. お金に
  1. 注意すべき
  2. 点について
  3. ですが、
  4. ここで
  5. 見えているのは
  6. このカードです。
  7. これは
  8. 「手」を
  9. 表しています。
  10. 手というのは
  11. 通常、
  12. とても
  13. ストレートで、
  14. お金に関しては
  15. あまり
  16. 計画を
  17. 立てすぎない
  18. 方がいい
  19. ということを
  20. 示しています。
  21. 特に
  22. 家庭の長男については
  23. そうです。

scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Topic of money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Obligation to pay attention.
* target[2]: "点について"
  - source_tokens: `7: "部分，"`
  - mapping_reason: Refers to the specific aspect/part.
* target[3]: "ですが、"
  - source_tokens: `11: "呢"`
  - mapping_reason: Discourse transition marker.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Locative reference.
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: Act of seeing/observing.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片，"`
  - mapping_reason: Object identified as a card.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Anaphoric subject.
* target[8]: "「手」を"
  - source_tokens: `24: "手。"`
  - mapping_reason: Object of representation.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: Verb of representation.
* target[10]: "手というのは"
  - source_tokens: `26: "手", 27: "的", 28: "时候"`
  - mapping_reason: Topic marker regarding the "hand" symbol.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverbial frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Intensifier.
* target[13]: "ストレートで、"
  - source_tokens: `33: "的", 34: "直白，"`
  - mapping_reason: Descriptive quality.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱", 40: "呢，"`
  - mapping_reason: Setting the topic to money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Limitation on degree.
* target[16]: "計画を"
  - source_tokens: `50: "规划，"`
  - mapping_reason: Object of planning.
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要，", 48: "太多", 49: "的"`
  - mapping_reason: Negative instruction on planning.
* target[18]: "方がいい"
  - source_tokens: `41: "可能", 42: "就"`
  - mapping_reason: Modal advice.
* target[19]: "ということを"
  - source_tokens: `47: "做"`
  - mapping_reason: Nominalizer/connective for the clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Verb of indication.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis.
* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group reference.
* target[23]: "そうです。"
  - source_tokens: `52: "是"`
  - mapping_reason: Affirmation/reference back to the previous advice.

result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [11]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13, 14, 15]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26, 27, 28]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39, 40]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 48, 49]},
  {"target_senseunit_id": 18, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 19, "source_token_ids": [47]},
  {"target_senseunit_id": 20, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [52]}
]

errors:
* target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです' acts as a summary/reference to the advice concerning the eldest son, not just the copula '是'."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"

attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです' refers to the advice regarding the eldest son; mapping only to the copula '是' misses the necessary semantic context."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Direct reference to money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Translation of "need to pay attention".
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: Refers to the aspect/point.
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Discourse marker indicating continuation/topic shift.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Locative reference.
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: Verb phrase for seeing.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: Subject reference.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Pronoun reference.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: Direct object.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: Verb phrase for representing.
* target[10]: "手というのは"
  - source_tokens: `26: "手"`
  - mapping_reason: Topic marker.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb of frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Intensifier.
* target[13]: "ストレートで、"
  - source_tokens: `34: "直白"`
  - mapping_reason: Descriptive adjective.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱"`
  - mapping_reason: Subject/Topic regarding money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Adverb for minimizing/limiting.
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: Object of planning.
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要", 47: "做", 48: "太多"`
  - mapping_reason: Verb phrase for not over-planning.
* target[18]: "方がいい"
  - source_tokens: `41: "可能"`
  - mapping_reason: Suggestion/modal marker.
* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Subordinating structure.
* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: Verb indicating meaning.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis marker.
* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group.
* target[23]: "そうです。"
  - source_tokens: `52: "是"`
  - mapping_reason: Confirmation/reference to the previous statement.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13, 14, 15]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 47, 48]},
  {"target_senseunit_id": 18, "source_token_ids": [41]},
  {"target_senseunit_id": 19, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [52]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです' is a discourse marker referring back to the previous advice, not a translation of '尤其'. '尤其' is already used in target 21."
  - replace_source_tokens: 25: "那么"

* target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' is a discourse marker/anaphora referring back to the advice, not the specific content about the eldest son (51-57), which is already handled in the previous unit."
  - replace_source_tokens: 46: "就是"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: "Refers to the topic of money."

* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: "Refers to the need to pay attention."

* target[2]: "点について"
  - source_tokens: `7: "部分，"`
  - mapping_reason: "Corresponds to the aspect/part mentioned."

* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是", 2: "针对"`
  - mapping_reason: "Connective discourse indicating the continuation of the topic."

* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: "Location reference."

* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: "Visual perception verb phrase."

* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片，"`
  - mapping_reason: "Identification of the object (card)."

* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: "Subject pronoun referring to the card."

* target[8]: "「手」を"
  - source_tokens: `24: "手。"`
  - mapping_reason: "The symbol 'hand'."

* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: "Verb of representation."

* target[10]: "手というのは"
  - source_tokens: `26: "手", 27: "的", 28: "时候"`
  - mapping_reason: "Topic marker for 'hand' context."

* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: "Adverb of frequency."

* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: "Degree adverb."

* target[13]: "ストレートで、"
  - source_tokens: `33: "的", 34: "直白，"`
  - mapping_reason: "Descriptive adjective."

* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱"`
  - mapping_reason: "Topic regarding money."

* target[15]: "あまり"
  - source_tokens: `43: "尽量", 45: "不要，"`
  - mapping_reason: "Negative advice marker."

* target[16]: "計画を"
  - source_tokens: `48: "太多", 50: "规划，"`
  - mapping_reason: "Direct object of planning."

* target[17]: "立てすぎない"
  - source_tokens: `47: "做"`
  - mapping_reason: "Verb for making plans."

* target[18]: "方がいい"
  - source_tokens: `41: "可能", 42: "就"`
  - mapping_reason: "Modal expression for advice."

* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: "Nominalizer for the preceding clause."

* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: "Verb of indication."

* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: "Emphasis marker."

* target[22]: "家庭の長男については"
  - source_tokens: `52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: "Specific target group."

* target[23]: "そうです。"
  - source_tokens: `51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: "Confirmation/agreement regarding the advice for the eldest son."
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [3, 4]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [7]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [0, 1, 2]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [9, 10]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [12, 13, 14, 15]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [16, 17, 18, 19]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [20]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [24]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21, 22, 23]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [26, 27, 28]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [30]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [32]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [33, 34]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [37, 38, 39]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [43, 45]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [48, 50]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [47]
  },
  {
    "target_senseunit_id": 18,
    "source_token_ids": [41, 42]
  },
  {
    "target_senseunit_id": 19,
    "source_token_ids": [35, 36]
  },
  {
    "target_senseunit_id": 20,
    "source_token_ids": [35]
  },
  {
    "target_senseunit_id": 21,
    "source_token_ids": [51]
  },
  {
    "target_senseunit_id": 22,
    "source_token_ids": [52, 53, 54, 55, 56, 57]
  },
  {
    "target_senseunit_id": 23,
    "source_token_ids": [51, 52, 53, 54, 55, 56, 57]
  }
]

- retry: 2/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' refers to the advice about the eldest son (tokens 51-57), not the filler '就是' (46)."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男。"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Core noun "money".
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Verbal phrase "should pay attention".
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: Noun "part/point".
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Connective indicating continuation of the topic.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Locative reference.
* target[5]: "見えているのは"
  - source_tokens: `11: "呢", 12: "可以", 13: "看到"`
  - mapping_reason: Verbal expression "can see".
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: Noun phrase "this card".
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Pronoun referring to the card.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: Noun "hand".
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 23: "是"`
  - mapping_reason: Verb "represents".
* target[10]: "手というのは"
  - source_tokens: `26: "手", 27: "的", 28: "时候"`
  - mapping_reason: Subject topic "as for the hand".
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb "usually".
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Degree adverb "very".
* target[13]: "ストレートで、"
  - source_tokens: `33: "的", 34: "直白"`
  - mapping_reason: Adjective "straightforward".
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱", 40: "呢"`
  - mapping_reason: Topic "regarding money".
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Adverb "not too much/as much as possible".
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: Noun "plan".
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要", 47: "做", 48: "太多"`
  - mapping_reason: Verb phrase "not do too much".
* target[18]: "方がいい"
  - source_tokens: `41: "可能"`
  - mapping_reason: Modal suggestion "better to".
* target[19]: "ということを"
  - source_tokens: `49: "的"`
  - mapping_reason: Nominalizer for the preceding clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Verb "shows/represents".
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Adverb "especially".
* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Target group "regarding the eldest son in the family".
* target[23]: "そうです。"
  - source_tokens: `46: "就是"`
  - mapping_reason: Discourse marker confirming the previous advice applies to this group.
    result:
[
  {
    "target_senseunit_id": 0,
    "source_token_ids": [5]
  },
  {
    "target_senseunit_id": 1,
    "source_token_ids": [3, 4]
  },
  {
    "target_senseunit_id": 2,
    "source_token_ids": [7]
  },
  {
    "target_senseunit_id": 3,
    "source_token_ids": [0, 1]
  },
  {
    "target_senseunit_id": 4,
    "source_token_ids": [9, 10]
  },
  {
    "target_senseunit_id": 5,
    "source_token_ids": [11, 12, 13]
  },
  {
    "target_senseunit_id": 6,
    "source_token_ids": [16, 17, 18, 19]
  },
  {
    "target_senseunit_id": 7,
    "source_token_ids": [20]
  },
  {
    "target_senseunit_id": 8,
    "source_token_ids": [24]
  },
  {
    "target_senseunit_id": 9,
    "source_token_ids": [21, 23]
  },
  {
    "target_senseunit_id": 10,
    "source_token_ids": [26, 27, 28]
  },
  {
    "target_senseunit_id": 11,
    "source_token_ids": [30]
  },
  {
    "target_senseunit_id": 12,
    "source_token_ids": [32]
  },
  {
    "target_senseunit_id": 13,
    "source_token_ids": [33, 34]
  },
  {
    "target_senseunit_id": 14,
    "source_token_ids": [37, 38, 39, 40]
  },
  {
    "target_senseunit_id": 15,
    "source_token_ids": [43]
  },
  {
    "target_senseunit_id": 16,
    "source_token_ids": [50]
  },
  {
    "target_senseunit_id": 17,
    "source_token_ids": [45, 47, 48]
  },
  {
    "target_senseunit_id": 18,
    "source_token_ids": [41]
  },
  {
    "target_senseunit_id": 19,
    "source_token_ids": [49]
  },
  {
    "target_senseunit_id": 20,
    "source_token_ids": [35, 36]
  },
  {
    "target_senseunit_id": 21,
    "source_token_ids": [51]
  },
  {
    "target_senseunit_id": 22,
    "source_token_ids": [53, 54, 55, 56, 57]
  },
  {
    "target_senseunit_id": 23,
    "source_token_ids": [46]
  }
]

- retry: 3/5
  status: failed_after_response
  reason: * target[18]
  - verdict: mapping_error
  - reason: "The target sense unit '方がいい' (should/better not) corresponds to the modal advice '不要' (don't) at index 45, not the discourse particle '呢' at index 44."
  - replace_source_tokens: 45: "不要"

* target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' is a discourse marker referring back to the advice, not a translation of the specific noun phrase describing the eldest son. The provided source tokens for this unit are redundant as they are already mapped to target[21] and target[22]."
  - replace_source_tokens: 46: "就是"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Core noun for money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Modal and verb for attention.
* target[2]: "点について"
  - source_tokens: `6: "的", 7: "部分"`
  - mapping_reason: Topic marker regarding the point/part.
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Discourse connective indicating continuation of topic.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Location reference.
* target[5]: "見えているのは"
  - source_tokens: `11: "呢", 12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: Perception verb phrase.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: Subject noun phrase.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Anaphoric subject.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: Object noun.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: Verb of representation.
* target[10]: "手というのは"
  - source_tokens: `25: "那么", 26: "手", 27: "的", 28: "时候", 29: "呢"`
  - mapping_reason: Topic introduction.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Frequency adverb.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Degree adverb.
* target[13]: "ストレートで、"
  - source_tokens: `31: "它", 33: "的", 34: "直白"`
  - mapping_reason: Descriptive adjective.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱", 40: "呢"`
  - mapping_reason: Topic regarding money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Adverb of degree (limitation).
* target[16]: "計画を"
  - source_tokens: `47: "做", 48: "太多", 49: "的", 50: "规划"`
  - mapping_reason: Object noun phrase.
* target[17]: "立てすぎない"
  - source_tokens: `41: "可能", 42: "就", 45: "不要"`
  - mapping_reason: Verb phrase for negation of planning.
* target[18]: "方がいい"
  - source_tokens: `44: "呢"`
  - mapping_reason: Modal suggestion.
* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Nominalizer for the preceding clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: Verb meaning "to show/represent".
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis adverb.
* target[22]: "家庭の長男については"
  - source_tokens: `52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group.
* target[23]: "そうです。"
  - source_tokens: `51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Confirming the application of the previous advice to the specific group.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [6, 7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [11, 12, 13, 14, 15]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [25, 26, 27, 28, 29]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [31, 33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39, 40]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [47, 48, 49, 50]},
  {"target_senseunit_id": 17, "source_token_ids": [41, 42, 45]},
  {"target_senseunit_id": 18, "source_token_ids": [44]},
  {"target_senseunit_id": 19, "source_token_ids": [36]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [52, 53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [51, 52, 53, 54, 55, 56, 57]}
]

- retry: 4/5
  status: failed_after_response
  reason: * target[3]
  - verdict: mapping_error
  - reason: "The target discourse connector 'ですが、' does not realize the semantic content of '同样', '也是', or '针对'. It functions as a transition marker, best mapped to the modal particle '呢' (index 11)."
  - replace_source_tokens: 11: "呢"

* target[23]
  - verdict: mapping_error
  - reason: "The target unit acts as a summary reference to the advice about the eldest son (tokens 51-57), not the discourse marker '就是' (46)."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Topic of money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Advice to pay attention to.
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: Referring to the aspect/part.
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是", 2: "针对"`
  - mapping_reason: Discourse connector for shifting topics/adding context.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Location reference.
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到"`
  - mapping_reason: Visual observation.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: Identification of the object.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Subject pronoun.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: Object reference.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 23: "是"`
  - mapping_reason: Representation verb.
* target[10]: "手というのは"
  - source_tokens: `26: "手"`
  - mapping_reason: Topic marker for the object.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb of frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Degree adverb.
* target[13]: "ストレートで、"
  - source_tokens: `34: "直白"`
  - mapping_reason: Adjective describing clarity.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱"`
  - mapping_reason: Topic regarding money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Adverb of limitation.
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: Object of the action.
* target[17]: "立てすぎない"
  - source_tokens: `47: "做", 48: "太多"`
  - mapping_reason: Negative action of over-planning.
* target[18]: "方がいい"
  - source_tokens: `45: "不要"`
  - mapping_reason: Modal advice.
* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Nominalizer for the preceding clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: Verb of indication.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis marker.
* target[22]: "家庭の長男については"
  - source_tokens: `54: "家中", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group.
* target[23]: "そうです。"
  - source_tokens: `46: "就是"`
  - mapping_reason: Confirmation marker.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1, 2]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [47, 48]},
  {"target_senseunit_id": 18, "source_token_ids": [45]},
  {"target_senseunit_id": 19, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [54, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [46]}
]

- retry: 5/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです' acts as a summary/reference to the advice concerning the eldest son, not just the copula '是'."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Topic of money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Obligation to pay attention.
* target[2]: "点について"
  - source_tokens: `7: "部分，"`
  - mapping_reason: Refers to the specific aspect/part.
* target[3]: "ですが、"
  - source_tokens: `11: "呢"`
  - mapping_reason: Discourse transition marker.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Locative reference.
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: Act of seeing/observing.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片，"`
  - mapping_reason: Object identified as a card.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Anaphoric subject.
* target[8]: "「手」を"
  - source_tokens: `24: "手。"`
  - mapping_reason: Object of representation.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: Verb of representation.
* target[10]: "手というのは"
  - source_tokens: `26: "手", 27: "的", 28: "时候"`
  - mapping_reason: Topic marker regarding the "hand" symbol.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverbial frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Intensifier.
* target[13]: "ストレートで、"
  - source_tokens: `33: "的", 34: "直白，"`
  - mapping_reason: Descriptive quality.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱", 40: "呢，"`
  - mapping_reason: Setting the topic to money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Limitation on degree.
* target[16]: "計画を"
  - source_tokens: `50: "规划，"`
  - mapping_reason: Object of planning.
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要，", 48: "太多", 49: "的"`
  - mapping_reason: Negative instruction on planning.
* target[18]: "方がいい"
  - source_tokens: `41: "可能", 42: "就"`
  - mapping_reason: Modal advice.
* target[19]: "ということを"
  - source_tokens: `47: "做"`
  - mapping_reason: Nominalizer/connective for the clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Verb of indication.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis.
* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group reference.
* target[23]: "そうです。"
  - source_tokens: `52: "是"`
  - mapping_reason: Affirmation/reference back to the previous advice.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [11]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13, 14, 15]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26, 27, 28]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39, 40]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 48, 49]},
  {"target_senseunit_id": 18, "source_token_ids": [41, 42]},
  {"target_senseunit_id": 19, "source_token_ids": [47]},
  {"target_senseunit_id": 20, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [52]}
]

---
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同样
  1. 也是
  2. 针对
  3. 要
  4. 留意
  5. 金钱
  6. 的
  7. 部分，
  8. 我们
  9. 从
  10. 这里
  11. 呢
  12. 可以
  13. 看到
  14. 的
  15. 是
  16. 这
  17. 一
  18. 副
  19. 卡片，
  20. 它
  21. 代表
  22. 的
  23. 是
  24. 手。
  25. 那么
  26. 手
  27. 的
  28. 时候
  29. 呢，
  30. 通常
  31. 它
  32. 非常
  33. 的
  34. 直白，
  35. 代表
  36. 是
  37. 我们
  38. 的
  39. 金钱
  40. 呢，
  41. 可能
  42. 就
  43. 尽量
  44. 呢
  45. 不要，
  46. 就是
  47. 做
  48. 太多
  49. 的
  50. 规划，
  51. 尤其
  52. 是
  53. 针对
  54. 家中
  55. 的
  56. 男性
  57. 长男。

target:
- language: Japanese
- translation: お金に注意すべき点についてですが、ここで見えているのはこのカードです。これは「手」を表しています。手というのは通常、とてもストレートで、お金に関してはあまり計画を立てすぎない方がいいということを示しています。特に家庭の長男についてはそうです。
- target_sense_units:
  0. お金に
  1. 注意すべき
  2. 点について
  3. ですが、
  4. ここで
  5. 見えているのは
  6. このカードです。
  7. これは
  8. 「手」を
  9. 表しています。
  10. 手というのは
  11. 通常、
  12. とても
  13. ストレートで、
  14. お金に関しては
  15. あまり
  16. 計画を
  17. 立てすぎない
  18. 方がいい
  19. ということを
  20. 示しています。
  21. 特に
  22. 家庭の長男については
  23. そうです。

scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: target refers to money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: target refers to needing to pay attention.
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: target refers to the aspect/point.
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: target provides a connective/discourse marker for the same topic.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: target refers to the location/source.
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到"`
  - mapping_reason: target refers to the act of seeing.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: target refers to the card.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: target refers to the subject (card).
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: target refers to the hand.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 23: "是"`
  - mapping_reason: target refers to the representative meaning.
* target[10]: "手というのは"
  - source_tokens: `26: "手"`
  - mapping_reason: target refers to the hand as the topic.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: target refers to the frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: target refers to the degree.
* target[13]: "ストレートで、"
  - source_tokens: `34: "直白"`
  - mapping_reason: target refers to the directness.
* target[14]: "お金に関しては"
  - source_tokens: `39: "金钱"`
  - mapping_reason: target refers to the topic of money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: target refers to the extent limitation.
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: target refers to planning.
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要", 48: "太多"`
  - mapping_reason: target refers to not doing too much.
* target[18]: "方がいい"
  - source_tokens: `47: "做"`
  - mapping_reason: target refers to the advice/action.
* target[19]: "ということを"
  - source_tokens: `35: "代表"`
  - mapping_reason: target refers to the semantic implication.
* target[20]: "示しています。"
  - source_tokens: `36: "是"`
  - mapping_reason: target refers to the indication.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: target refers to the emphasis.
* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 56: "男性", 57: "长男"`
  - mapping_reason: target refers to the specific target group.
* target[23]: "そうです。"
  - source_tokens: `51: "尤其"`
  - mapping_reason: target acts as an anaphoric confirmation of the previous statement applied to the specific group emphasized by "尤其".

result:
```html
0. <src>同样也是</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>针对要留意</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>金钱的部分，</src> <tgt>お金に注意すべき点についてですが、</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>我们从这里呢</src> <tgt>ここで</tgt>; start=4.00, end=5.00
5. <src>可以看到的是</src> <tgt>見えているのは</tgt>; start=5.00, end=6.00
6. <src>这一副卡片，</src> <tgt>このカードです。</tgt>; start=6.00, end=7.00
7. <src>它代表的是</src> <tgt>これは</tgt>; start=7.00, end=8.00
8. <src>手。</src> <tgt>「手」を表しています。</tgt>; start=8.00, end=9.00
9. <src>那么</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>手的时候呢，</src> <tgt>手というのは</tgt>; start=10.00, end=11.00
11. <src>通常</src> <tgt>通常、</tgt>; start=11.00, end=12.00
12. <src>它非常</src> <tgt>とても</tgt>; start=12.00, end=13.00
13. <src>的直白，</src> <tgt>ストレートで、</tgt>; start=13.00, end=14.00
14. <src>代表是我们的金钱</src> <tgt>お金に関しては</tgt>; start=14.00, end=15.00
15. <src>呢，</src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>可能就尽量呢</src> <tgt>あまり</tgt>; start=16.00, end=17.00
17. <src>不要，</src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>就是做太多</src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>的规划，</src> <tgt>計画を立てすぎない方がいいということを示しています。</tgt>; start=20.00, end=21.00
21. <src>尤其是</src> <tgt>特に</tgt>; start=21.00, end=22.00
22. <src><|wait|></src> <tgt><|wait|></tgt>; start=22.00, end=23.00
23. <src>针对家中的男性</src> <tgt><|wait|></tgt>; start=23.00, end=24.00
24. <src>长男。</src> <tgt>家庭の長男についてはそうです。</tgt>; start=24.00, end=24.87
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' acts as a discourse connector/reference to the previous advice, not as a mapping to the preposition '针对'."
  - replace_source_tokens: 51: "尤其", 52: "是"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Direct translation of "money".

* target[1]: "注意すべき"
  - source_tokens: `4: "留意"`
  - mapping_reason: Direct translation of "pay attention to".

* target[2]: "点について"
  - source_tokens: `7: "部分，"`
  - mapping_reason: Corresponds to "part/aspect".

* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Discourse marker indicating continuation/topic shift.

* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Location reference "from here".

* target[5]: "見えているのは"
  - source_tokens: `11: "呢", 12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: "What we can see is".

* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片，"`
  - mapping_reason: "This (set of) card(s)".

* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Anaphoric reference to the card.

* target[8]: "「手」を"
  - source_tokens: `24: "手。"`
  - mapping_reason: The object "hand".

* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: "Represents/stands for".

* target[10]: "手というのは"
  - source_tokens: `26: "手", 27: "的", 28: "时候"`
  - mapping_reason: Topic marker "as for the hand".

* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Direct translation.

* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Direct translation.

* target[13]: "ストレートで、"
  - source_tokens: `33: "的", 34: "直白，"`
  - mapping_reason: Direct translation of "straightforward".

* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱", 40: "呢"`
  - mapping_reason: Topic "as for money".

* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: "As much as possible" (in negative context).

* target[16]: "計画を"
  - source_tokens: `49: "的", 50: "规划，"`
  - mapping_reason: Direct translation.

* target[17]: "立てすぎない"
  - source_tokens: `45: "不要，", 46: "就是", 47: "做", 48: "太多"`
  - mapping_reason: "Don't do too much".

* target[18]: "方がいい"
  - source_tokens: `41: "可能"`
  - mapping_reason: Modal suggestion.

* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Nominalizer for the preceding clause.

* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: "Indicates/shows".

* target[21]: "特に"
  - source_tokens: `51: "尤其", 52: "是"`
  - mapping_reason: Direct translation.

* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男。"`
  - mapping_reason: "Regarding the eldest son in the family".

* target[23]: "そうです。"
  - source_tokens: `53: "针对"`
  - mapping_reason: Affirmation of the scope/target.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [11, 12, 13, 14, 15]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26, 27, 28]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39, 40]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [49, 50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 46, 47, 48]},
  {"target_senseunit_id": 18, "source_token_ids": [41]},
  {"target_senseunit_id": 19, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51, 52]},
  {"target_senseunit_id": 22, "source_token_ids": [53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [53]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[19]
  - verdict: mapping_error
  - reason: "The source token '的' (attributive particle) is incorrectly mapped to the discourse nominalizer 'ということを'. This target unit serves as a structural completion for the advice clause."
  - replace_source_tokens: 44: "呢", 45: "不要"

* target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' refers to the advice regarding the eldest son, not just the words '尤其' and '是'."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Core noun for financial focus.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Modal necessity and verb for paying attention.
* target[2]: "点について"
  - source_tokens: `7: "部分，"`
  - mapping_reason: Refers to the specific aspect/part mentioned.
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Discourse connective indicating continuation of the same topic.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Location reference.
* target[5]: "見えているのは"
  - source_tokens: `11: "呢", 12: "可以", 13: "看到"`
  - mapping_reason: Visual observation verb phrase.
* target[6]: "このカードです。"
  - source_tokens: `14: "的", 15: "是", 16: "这", 17: "一", 18: "副", 19: "卡片，"`
  - mapping_reason: Identification of the card object.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Pronoun referring to the card.
* target[8]: "「手」を"
  - source_tokens: `24: "手。"`
  - mapping_reason: Core noun representing the object.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: Verb meaning to represent/symbolize.
* target[10]: "手というのは"
  - source_tokens: `25: "那么", 26: "手", 27: "的", 28: "时候", 29: "呢，"`
  - mapping_reason: Topic marker and noun reference.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb of frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Intensifier.
* target[13]: "ストレートで、"
  - source_tokens: `31: "它", 33: "的", 34: "直白，"`
  - mapping_reason: Adjective describing the meaning.
* target[14]: "お金に関しては"
  - source_tokens: `35: "代表", 36: "是", 37: "我们", 38: "的", 39: "金钱", 40: "呢，"`
  - mapping_reason: Topic regarding money.
* target[15]: "あまり"
  - source_tokens: `43: "尽量", 45: "不要，"`
  - mapping_reason: Adverbial modifier for restriction.
* target[16]: "計画を"
  - source_tokens: `47: "做", 48: "太多", 49: "的", 50: "规划，"`
  - mapping_reason: Noun for planning.
* target[17]: "立てすぎない"
  - source_tokens: `41: "可能", 42: "就", 44: "呢", 46: "就是"`
  - mapping_reason: Verb phrase for not planning too much.
* target[18]: "方がいい"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Advice/recommendation structure.
* target[19]: "ということを"
  - source_tokens: `49: "的"`
  - mapping_reason: Nominalizer for the clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: Verb for indicating/showing.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis adverb.
* target[22]: "家庭の長男については"
  - source_tokens: `52: "是", 54: "家中", 55: "的", 56: "男性", 57: "长男。"`
  - mapping_reason: Specific target group.
* target[23]: "そうです。"
  - source_tokens: `51: "尤其", 52: "是"`
  - mapping_reason: Discourse reference confirming the application to the specific group mentioned.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [11, 12, 13]},
  {"target_senseunit_id": 6, "source_token_ids": [14, 15, 16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [25, 26, 27, 28, 29]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [31, 33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [35, 36, 37, 38, 39, 40]},
  {"target_senseunit_id": 15, "source_token_ids": [43, 45]},
  {"target_senseunit_id": 16, "source_token_ids": [47, 48, 49, 50]},
  {"target_senseunit_id": 17, "source_token_ids": [41, 42, 44, 46]},
  {"target_senseunit_id": 18, "source_token_ids": [43]},
  {"target_senseunit_id": 19, "source_token_ids": [49]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [52, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [51, 52]}
]

- retry: 2/5
  status: failed_after_response
  reason: * target[3]
  - verdict: mapping_error
  - reason: "The source tokens 0-2 are part of the preceding semantic unit (attention to money), while 'ですが、' functions as a discourse transition, best anchored by the modal particle '呢' (11)."
  - replace_source_tokens: 11: "呢"

* target[18]
  - verdict: mapping_error
  - reason: "The target unit '方がいい' (should/better) expresses the advice derived from '不要' (don't) and '规划' (plan), not the particle '呢'."
  - replace_source_tokens: 43: "尽量", 45: "不要", 47: "做", 50: "规划"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Topic of the advice regarding money.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Modal and verb for paying attention.
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: Noun representing the aspect or point.
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是", 2: "针对"`
  - mapping_reason: Connective indicating continuation of the topic.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Locative reference.
* target[5]: "見えているのは"
  - source_tokens: `11: "呢", 12: "可以", 13: "看到", 14: "的", 15: "是"`
  - mapping_reason: Verb phrase indicating visual observation.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: Subject of the observation.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Pronoun referring to the card.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: Object of the representation.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: Verb indicating representation.
* target[10]: "手というのは"
  - source_tokens: `25: "那么", 26: "手", 27: "的", 28: "时候", 29: "呢"`
  - mapping_reason: Topic marker for "hand".
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb of frequency.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Degree adverb.
* target[13]: "ストレートで、"
  - source_tokens: `31: "它", 33: "的", 34: "直白"`
  - mapping_reason: Adjective describing the hand's symbolism.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱", 40: "呢"`
  - mapping_reason: Topic marker regarding money.
* target[15]: "あまり"
  - source_tokens: `41: "可能", 42: "就", 43: "尽量"`
  - mapping_reason: Adverb of degree (minimalizing).
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: Object of planning.
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要", 46: "就是", 47: "做", 48: "太多", 49: "的"`
  - mapping_reason: Verb phrase for not planning too much.
* target[18]: "方がいい"
  - source_tokens: `44: "呢"`
  - mapping_reason: Modal for advice.
* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Nominalizer for the advice clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: Verb indicating the meaning.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Adverb for emphasis.
* target[22]: "家庭の長男については"
  - source_tokens: `52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group for the advice.
* target[23]: "そうです。"
  - source_tokens: `51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Confirmation of the advice applying to the specific target.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1, 2]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [11, 12, 13, 14, 15]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [25, 26, 27, 28, 29]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [31, 33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39, 40]},
  {"target_senseunit_id": 15, "source_token_ids": [41, 42, 43]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 46, 47, 48, 49]},
  {"target_senseunit_id": 18, "source_token_ids": [44]},
  {"target_senseunit_id": 19, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [52, 53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [51, 52, 53, 54, 55, 56, 57]}
]

- retry: 3/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit functions as a summary/confirmation of the preceding clause (51-57), making the single token '是' (52) an insufficient anchor."
  - replace_source_tokens: 51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Direct object of attention.
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: Lexical meaning of "should pay attention".
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: Refers to the aspect/part mentioned.
* target[3]: "ですが、"
  - source_tokens: `11: "呢"`
  - mapping_reason: Discourse marker for transition.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: Spatial reference.
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到"`
  - mapping_reason: Lexical meaning of observing/seeing.
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: Identification of the object.
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Anaphoric reference.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: Subject of representation.
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 23: "是"`
  - mapping_reason: Verb of representation.
* target[10]: "手というのは"
  - source_tokens: `26: "手"`
  - mapping_reason: Topic marker for the symbol.
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Frequency adverb.
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Degree adverb.
* target[13]: "ストレートで、"
  - source_tokens: `34: "直白"`
  - mapping_reason: Adjective describing the symbol.
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱"`
  - mapping_reason: Scope of the advice.
* target[15]: "あまり"
  - source_tokens: `48: "太多"`
  - mapping_reason: Quantifier indicating "too much".
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: Object of the planning action.
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要", 47: "做"`
  - mapping_reason: Negative action marker.
* target[18]: "方がいい"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Modal suggestion/advice.
* target[19]: "ということを"
  - source_tokens: `35: "代表"`
  - mapping_reason: Linking the previous clause to the representation.
* target[20]: "示しています。"
  - source_tokens: `36: "是"`
  - mapping_reason: Copula/verb indicating meaning.
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Emphasis marker.
* target[22]: "家庭の長男については"
  - source_tokens: `54: "家中", 56: "男性", 57: "长男"`
  - mapping_reason: Specific target group.
* target[23]: "そうです。"
  - source_tokens: `52: "是"`
  - mapping_reason: Affirmation/reference to the previous state.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [11]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39]},
  {"target_senseunit_id": 15, "source_token_ids": [48]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 47]},
  {"target_senseunit_id": 18, "source_token_ids": [43]},
  {"target_senseunit_id": 19, "source_token_ids": [35]},
  {"target_senseunit_id": 20, "source_token_ids": [36]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [54, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [52]}
]

- retry: 4/5
  status: failed_after_response
  reason: * target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' functions as an anaphoric confirmation and does not realize the entire descriptive phrase about the eldest son, which is already covered by the preceding units."
  - replace_source_tokens: 51: "尤其"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `5: "金钱"`
  - mapping_reason: Core topic "money".
* target[1]: "注意すべき"
  - source_tokens: `3: "要", 4: "留意"`
  - mapping_reason: "要留意" (should pay attention to).
* target[2]: "点について"
  - source_tokens: `7: "部分"`
  - mapping_reason: "部分" (part/aspect).
* target[3]: "ですが、"
  - source_tokens: `0: "同样", 1: "也是"`
  - mapping_reason: Discourse marker for continuity/addition.
* target[4]: "ここで"
  - source_tokens: `9: "从", 10: "这里"`
  - mapping_reason: "从这里" (from here).
* target[5]: "見えているのは"
  - source_tokens: `12: "可以", 13: "看到"`
  - mapping_reason: "可以看到" (can see).
* target[6]: "このカードです。"
  - source_tokens: `16: "这", 17: "一", 18: "副", 19: "卡片"`
  - mapping_reason: "这一副卡片" (this card).
* target[7]: "これは"
  - source_tokens: `20: "它"`
  - mapping_reason: Anaphoric reference to the card.
* target[8]: "「手」を"
  - source_tokens: `24: "手"`
  - mapping_reason: The object "hand".
* target[9]: "表しています。"
  - source_tokens: `21: "代表", 22: "的", 23: "是"`
  - mapping_reason: "代表的是" (represents).
* target[10]: "手というのは"
  - source_tokens: `26: "手"`
  - mapping_reason: Topic marker "hand".
* target[11]: "通常、"
  - source_tokens: `30: "通常"`
  - mapping_reason: Adverb "usually".
* target[12]: "とても"
  - source_tokens: `32: "非常"`
  - mapping_reason: Adverb "very".
* target[13]: "ストレートで、"
  - source_tokens: `33: "的", 34: "直白"`
  - mapping_reason: "非常直白" (very straightforward).
* target[14]: "お金に関しては"
  - source_tokens: `37: "我们", 38: "的", 39: "金钱"`
  - mapping_reason: "我们的金钱" (our money).
* target[15]: "あまり"
  - source_tokens: `43: "尽量"`
  - mapping_reason: Adverb "as much as possible" (in negative context).
* target[16]: "計画を"
  - source_tokens: `50: "规划"`
  - mapping_reason: Noun "plan".
* target[17]: "立てすぎない"
  - source_tokens: `45: "不要", 48: "太多"`
  - mapping_reason: "不要太多" (not too much).
* target[18]: "方がいい"
  - source_tokens: `41: "可能", 47: "做"`
  - mapping_reason: Modal suggestion.
* target[19]: "ということを"
  - source_tokens: `35: "代表", 36: "是"`
  - mapping_reason: Subordinating conjunction for the preceding clause.
* target[20]: "示しています。"
  - source_tokens: `35: "代表"`
  - mapping_reason: "代表" (represents/indicates).
* target[21]: "特に"
  - source_tokens: `51: "尤其"`
  - mapping_reason: Adverb "especially".
* target[22]: "家庭の長男については"
  - source_tokens: `53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Target group "family's eldest son".
* target[23]: "そうです。"
  - source_tokens: `51: "尤其", 52: "是", 53: "针对", 54: "家中", 55: "的", 56: "男性", 57: "长男"`
  - mapping_reason: Summary/confirmation of the preceding clause regarding the eldest son.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [5]},
  {"target_senseunit_id": 1, "source_token_ids": [3, 4]},
  {"target_senseunit_id": 2, "source_token_ids": [7]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1]},
  {"target_senseunit_id": 4, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 5, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 6, "source_token_ids": [16, 17, 18, 19]},
  {"target_senseunit_id": 7, "source_token_ids": [20]},
  {"target_senseunit_id": 8, "source_token_ids": [24]},
  {"target_senseunit_id": 9, "source_token_ids": [21, 22, 23]},
  {"target_senseunit_id": 10, "source_token_ids": [26]},
  {"target_senseunit_id": 11, "source_token_ids": [30]},
  {"target_senseunit_id": 12, "source_token_ids": [32]},
  {"target_senseunit_id": 13, "source_token_ids": [33, 34]},
  {"target_senseunit_id": 14, "source_token_ids": [37, 38, 39]},
  {"target_senseunit_id": 15, "source_token_ids": [43]},
  {"target_senseunit_id": 16, "source_token_ids": [50]},
  {"target_senseunit_id": 17, "source_token_ids": [45, 48]},
  {"target_senseunit_id": 18, "source_token_ids": [41, 47]},
  {"target_senseunit_id": 19, "source_token_ids": [35, 36]},
  {"target_senseunit_id": 20, "source_token_ids": [35]},
  {"target_senseunit_id": 21, "source_token_ids": [51]},
  {"target_senseunit_id": 22, "source_token_ids": [53, 54, 55, 56, 57]},
  {"target_senseunit_id": 23, "source_token_ids": [51, 52, 53, 54, 55, 56, 57]}
]

- retry: 5/5
  status: succeeded
  reason: retry attempt succeeded

---
