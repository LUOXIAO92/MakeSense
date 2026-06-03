=== ZH_B00021_S06758_W000029 ===

source:
- language: Chinese
- transcription: 我仿佛看到了他们游走在太行山上的足迹，深一脚浅一脚；我仿佛听到了他们放歌太行山上的声音，时而高，时而低，时而欢快，时而呜咽。
- source_tokens:
  0. 我
  1. 仿
  2. 佛
  3. 看
  4. 到
  5. 了
  6. 他
  7. 们
  8. 游
  9. 走
  10. 在
  11. 太
  12. 行
  13. 山
  14. 上
  15. 的
  16. 足
  17. 迹，
  18. 深
  19. 一
  20. 脚
  21. 浅
  22. 一
  23. 脚；
  24. 我
  25. 仿
  26. 佛
  27. 听
  28. 到
  29. 了
  30. 他
  31. 们
  32. 放
  33. 歌
  34. 太
  35. 行
  36. 山
  37. 上
  38. 的
  39. 声
  40. 音，
  41. 时
  42. 而
  43. 高，
  44. 时
  45. 而
  46. 低，
  47. 时
  48. 而
  49. 欢
  50. 快，
  51. 时
  52. 而
  53. 呜
  54. 咽。

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
  - source_tokens: `0: "我", 1: "仿", 2: "佛"`
  - mapping_reason: Subject "I" and adverbial "seem" (仿佛).
* target[1]: "to see"
  - source_tokens: `3: "看", 4: "到", 5: "了"`
  - mapping_reason: Verb "see" (看到) with perfective aspect (了).
* target[2]: "their wandering footprints"
  - source_tokens: `6: "他", 7: "们", 8: "游", 9: "走", 16: "足", 17: "迹"`
  - mapping_reason: "their" (他们), "wandering" (游走), "footprints" (足迹).
* target[3]: "on the Taihang Mountains,"
  - source_tokens: `10: "在", 11: "太", 12: "行", 13: "山", 14: "上", 15: "的"`
  - mapping_reason: Prepositional phrase indicating location on Taihang Mountains.
* target[4]: "stumbling step by step;"
  - source_tokens: `18: "深", 19: "一", 20: "脚", 21: "浅", 22: "一", 23: "脚"`
  - mapping_reason: Idiomatic expression for uneven/stumbling steps.
* target[5]: "I seem"
  - source_tokens: `24: "我", 25: "仿", 26: "佛"`
  - mapping_reason: Subject "I" and adverbial "seem" (仿佛).
* target[6]: "to hear"
  - source_tokens: `27: "听", 28: "到", 29: "了"`
  - mapping_reason: Verb "hear" (听到) with perfective aspect (了).
* target[7]: "their songs"
  - source_tokens: `30: "他", 31: "们", 32: "放", 33: "歌", 39: "声", 40: "音"`
  - mapping_reason: "their" (他们), "songs" (放歌/声音).
* target[8]: "echoing in the Taihang Mountains,"
  - source_tokens: `34: "太", 35: "行", 36: "山", 37: "上", 38: "的"`
  - mapping_reason: Location of the sounds in Taihang Mountains.
* target[9]: "sometimes high,"
  - source_tokens: `41: "时", 42: "而", 43: "高"`
  - mapping_reason: Adverbial "sometimes" (时而) and adjective "high" (高).
* target[10]: "sometimes low,"
  - source_tokens: `44: "时", 45: "而", 46: "低"`
  - mapping_reason: Adverbial "sometimes" (时而) and adjective "low" (低).
* target[11]: "sometimes joyful,"
  - source_tokens: `47: "时", 48: "而", 49: "欢", 50: "快"`
  - mapping_reason: Adverbial "sometimes" (时而) and adjective "joyful" (欢快).
* target[12]: "sometimes sobbing."
  - source_tokens: `51: "时", 52: "而", 53: "呜", 54: "咽"`
  - mapping_reason: Adverbial "sometimes" (时而) and adjective "sobbing" (呜咽).

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
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同
  1. 样
  2. 也
  3. 是
  4. 针
  5. 对
  6. 要
  7. 留
  8. 意
  9. 金
  10. 钱
  11. 的
  12. 部
  13. 分，
  14. 我
  15. 们
  16. 从
  17. 这
  18. 里
  19. 呢
  20. 可
  21. 以
  22. 看
  23. 到
  24. 的
  25. 是
  26. 这
  27. 一
  28. 副
  29. 卡
  30. 片，
  31. 它
  32. 代
  33. 表
  34. 的
  35. 是
  36. 手。
  37. 那
  38. 么
  39. 手
  40. 的
  41. 时
  42. 候
  43. 呢，
  44. 通
  45. 常
  46. 它
  47. 非
  48. 常
  49. 的
  50. 直
  51. 白，
  52. 代
  53. 表
  54. 是
  55. 我
  56. 们
  57. 的
  58. 金
  59. 钱
  60. 呢，
  61. 可
  62. 能
  63. 就
  64. 尽
  65. 量
  66. 呢
  67. 不
  68. 要，
  69. 就
  70. 是
  71. 做
  72. 太
  73. 多
  74. 的
  75. 规
  76. 划，
  77. 尤
  78. 其
  79. 是
  80. 针
  81. 对
  82. 家
  83. 中
  84. 的
  85. 男
  86. 性
  87. 长
  88. 男。

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
  - source_tokens: `0: "同", 1: "样", 2: "也", 3: "是", 4: "针", 5: "对"`
  - mapping_reason: Translates the discourse marker and the initial topic-setting phrase.

* target[1]: "being careful with"
  - source_tokens: `6: "要", 7: "留", 8: "意"`
  - mapping_reason: Core meaning of paying attention/being careful.

* target[2]: "money,"
  - source_tokens: `9: "金", 10: "钱"`
  - mapping_reason: Subject of the care.

* target[3]: "what we see here is"
  - source_tokens: `14: "我", 15: "们", 16: "从", 17: "这", 18: "里", 20: "可", 21: "以", 22: "看", 23: "到", 25: "是"`
  - mapping_reason: Expresses the observation from the source text.

* target[4]: "this hand card."
  - source_tokens: `26: "这", 27: "一", 28: "副", 29: "卡", 30: "片", 36: "手"`
  - mapping_reason: Identifies the object being observed.

* target[5]: "The hand is"
  - source_tokens: `39: "手"`
  - mapping_reason: Subject of the following description.

* target[6]: "usually very straightforward—"
  - source_tokens: `44: "通", 45: "常", 47: "非", 48: "常", 49: "的", 50: "直", 51: "白"`
  - mapping_reason: Description of the hand symbol.

* target[7]: "it means that"
  - source_tokens: `52: "代", 53: "表", 54: "是"`
  - mapping_reason: Interpretation of the symbol.

* target[8]: "for our money,"
  - source_tokens: `55: "我", 56: "们", 57: "的", 58: "金", 59: "钱"`
  - mapping_reason: Context of the advice.

* target[9]: "maybe we shouldn't"
  - source_tokens: `61: "可", 62: "能", 67: "不", 68: "要"`
  - mapping_reason: Advice/suggestion.

* target[10]: "plan too much,"
  - source_tokens: `71: "做", 72: "太", 73: "多", 74: "的", 75: "规", 76: "划"`
  - mapping_reason: The action being cautioned against.

* target[11]: "especially when"
  - source_tokens: `77: "尤", 78: "其", 79: "是"`
  - mapping_reason: Discourse marker for emphasis.

* target[12]: "it comes to"
  - source_tokens: `80: "针", 81: "对"`
  - mapping_reason: Focus marker.

* target[13]: "the eldest male"
  - source_tokens: `85: "男", 86: "性", 87: "长", 88: "男"`
  - mapping_reason: Specific target of the caution.

* target[14]: "in the family."
  - source_tokens: `82: "家", 83: "中"`
  - mapping_reason: Location/scope of the eldest male.

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
  1. 仿
  2. 佛
  3. 看
  4. 到
  5. 了
  6. 他
  7. 们
  8. 游
  9. 走
  10. 在
  11. 太
  12. 行
  13. 山
  14. 上
  15. 的
  16. 足
  17. 迹，
  18. 深
  19. 一
  20. 脚
  21. 浅
  22. 一
  23. 脚；
  24. 我
  25. 仿
  26. 佛
  27. 听
  28. 到
  29. 了
  30. 他
  31. 们
  32. 放
  33. 歌
  34. 太
  35. 行
  36. 山
  37. 上
  38. 的
  39. 声
  40. 音，
  41. 时
  42. 而
  43. 高，
  44. 时
  45. 而
  46. 低，
  47. 时
  48. 而
  49. 欢
  50. 快，
  51. 时
  52. 而
  53. 呜
  54. 咽。

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
  - source_tokens: `11: "太", 12: "行", 13: "山", 8: "游", 9: "走"`
  - mapping_reason: "太行山" (11-13) and "游走" (8-9) correspond to the location and action.
* target[1]: "彼らの足跡が"
  - source_tokens: `6: "他", 7: "们", 16: "足", 17: "迹，"`
  - mapping_reason: "他们" (6-7) and "足迹" (16-17) constitute the subject and object.
* target[2]: "見えるようだ。"
  - source_tokens: `0: "我", 1: "仿", 2: "佛", 3: "看", 4: "到", 5: "了"`
  - mapping_reason: "我仿佛" (0-2) and "看到了" (3-5) express the perception.
* target[3]: "一歩"
  - source_tokens: `19: "一", 20: "脚"`
  - mapping_reason: "一脚" represents the first step.
* target[4]: "一歩、"
  - source_tokens: `22: "一", 23: "脚"`
  - mapping_reason: "一脚" represents the second step.
* target[5]: "深く"
  - source_tokens: `18: "深"`
  - mapping_reason: "深" maps to "深く".
* target[6]: "浅く。"
  - source_tokens: `21: "浅"`
  - mapping_reason: "浅" maps to "浅く".
* target[7]: "太行山に響く"
  - source_tokens: `34: "太", 35: "行", 36: "山", 32: "放", 33: "歌"`
  - mapping_reason: "太行山" (34-36) and "放歌" (32-33) describe the singing location and action.
* target[8]: "彼らの歌声が"
  - source_tokens: `30: "他", 31: "们", 39: "声", 40: "音，"`
  - mapping_reason: "他们" (30-31) and "声音" (39-40) constitute the subject and object.
* target[9]: "聞こえるようだ。"
  - source_tokens: `24: "我", 25: "仿", 26: "佛", 27: "听", 28: "到", 29: "了"`
  - mapping_reason: "我仿佛" (24-26) and "听到了" (27-29) express the perception.
* target[10]: "時には"
  - source_tokens: `41: "时", 42: "而"`
  - mapping_reason: "时而" maps to "時には".
* target[11]: "高く、"
  - source_tokens: `43: "高"`
  - mapping_reason: "高" maps to "高く".
* target[12]: "時には"
  - source_tokens: `44: "时", 45: "而"`
  - mapping_reason: "时而" maps to "時には".
* target[13]: "低く、"
  - source_tokens: `46: "低"`
  - mapping_reason: "低" maps to "低く".
* target[14]: "時には"
  - source_tokens: `47: "时", 48: "而"`
  - mapping_reason: "时而" maps to "時には".
* target[15]: "快活に、"
  - source_tokens: `49: "欢", 50: "快"`
  - mapping_reason: "欢快" maps to "快活に".
* target[16]: "時には"
  - source_tokens: `51: "时", 52: "而"`
  - mapping_reason: "时而" maps to "時には".
* target[17]: "咽び泣くように。"
  - source_tokens: `53: "呜", 54: "咽"`
  - mapping_reason: "呜咽" maps to "咽び泣く".

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
  2. 二
  3. 十
  4. 二
  5. 号，
  6. 美
  7. 国
  8. 证
  9. 券
  10. 交
  11. 易
  12. 委
  13. 员
  14. 会
  15. 宣
  16. 布
  17. 对
  18. 加
  19. 密
  20. 资
  21. 产
  22. 企
  23. 业
  24. 家
  25. 孙
  26. 宇
  27. 晨
  28. 及
  29. 其
  30. 三
  31. 家
  32. 全
  33. 资
  34. 公
  35. 司
  36. 提
  37. 起
  38. 诉
  39. 讼，
  40. 指
  41. 控
  42. 他
  43. 们
  44. 没
  45. 有
  46. 经
  47. 过
  48. 注
  49. 册
  50. 提
  51. 供
  52. 和
  53. 出
  54. 售
  55. 加
  56. 密
  57. 资
  58. 产
  59. 证
  60. 券
  61. Tronics
  62. 和
  63. BitTorrent。

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
  - source_tokens: `0: "三", 1: "月", 2: "二", 3: "十", 4: "二", 5: "号，"`
  - mapping_reason: Date expression.
* target[1]: "the U.S. Securities and Exchange Commission"
  - source_tokens: `6: "美", 7: "国", 8: "证", 9: "券", 10: "交", 11: "易", 12: "委", 13: "员", 14: "会"`
  - mapping_reason: Organization name.
* target[2]: "announced"
  - source_tokens: `15: "宣", 16: "布"`
  - mapping_reason: Main verb of announcement.
* target[3]: "it has filed"
  - source_tokens: `36: "提", 37: "起"`
  - mapping_reason: Action of filing.
* target[4]: "a lawsuit against"
  - source_tokens: `17: "对", 38: "诉", 39: "讼，"`
  - mapping_reason: Legal action and target.
* target[5]: "crypto- asset entrepreneur"
  - source_tokens: `18: "加", 19: "密", 20: "资", 21: "产", 22: "企", 23: "业", 24: "家"`
  - mapping_reason: Professional title/identity.
* target[6]: "Justin Sun"
  - source_tokens: `25: "孙", 26: "宇", 27: "晨"`
  - mapping_reason: Name of individual.
* target[7]: "and three of his"
  - source_tokens: `28: "及", 29: "其", 30: "三", 31: "家"`
  - mapping_reason: Conjunction and count.
* target[8]: "wholly- owned companies."
  - source_tokens: `32: "全", 33: "资", 34: "公", 35: "司"`
  - mapping_reason: Company description.
* target[9]: "The SEC"
  - source_tokens: `6: "美", 7: "国", 8: "证", 9: "券", 10: "交", 11: "易", 12: "委", 13: "员", 14: "会"`
  - mapping_reason: Reference back to the previously mentioned organization.
* target[10]: "accuses them of"
  - source_tokens: `40: "指", 41: "控", 42: "他", 43: "们"`
  - mapping_reason: Verb of accusation and object.
* target[11]: "offering and selling"
  - source_tokens: `50: "提", 51: "供", 52: "和", 53: "出", 54: "售"`
  - mapping_reason: The specific actions being accused.
* target[12]: "the unregistered crypto- asset securities"
  - source_tokens: `44: "没", 45: "有", 46: "经", 47: "过", 48: "注", 49: "册", 55: "加", 56: "密", 57: "资", 58: "产", 59: "证", 60: "券"`
  - mapping_reason: Description of the securities.
* target[13]: "Tronix and BitTorrent."
  - source_tokens: `61: "Tronics", 62: "和", 63: "BitTorrent。"`
  - mapping_reason: Specific asset names.

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
  2. 二
  3. 十
  4. 二
  5. 号，
  6. 美
  7. 国
  8. 证
  9. 券
  10. 交
  11. 易
  12. 委
  13. 员
  14. 会
  15. 宣
  16. 布
  17. 对
  18. 加
  19. 密
  20. 资
  21. 产
  22. 企
  23. 业
  24. 家
  25. 孙
  26. 宇
  27. 晨
  28. 及
  29. 其
  30. 三
  31. 家
  32. 全
  33. 资
  34. 公
  35. 司
  36. 提
  37. 起
  38. 诉
  39. 讼，
  40. 指
  41. 控
  42. 他
  43. 们
  44. 没
  45. 有
  46. 经
  47. 过
  48. 注
  49. 册
  50. 提
  51. 供
  52. 和
  53. 出
  54. 售
  55. 加
  56. 密
  57. 资
  58. 产
  59. 证
  60. 券
  61. Tronics
  62. 和
  63. BitTorrent。

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
  - source_tokens: `0: "三", 1: "月", 2: "二", 3: "十", 4: "二", 5: "号，"`
  - mapping_reason: Date expression.
* target[1]: "米証券取引委員会（SEC）が"
  - source_tokens: `6: "美", 7: "国", 8: "证", 9: "券", 10: "交", 11: "易", 12: "委", 13: "员", 14: "会"`
  - mapping_reason: Subject identification (SEC).
* target[2]: "暗号資産起業家の"
  - source_tokens: `18: "加", 19: "密", 20: "资", 21: "产", 22: "企", 23: "业", 24: "家"`
  - mapping_reason: Modifier for the subject of the lawsuit.
* target[3]: "孫宇晨（ジャスティン・サン）氏と"
  - source_tokens: `25: "孙", 26: "宇", 27: "晨", 28: "及"`
  - mapping_reason: Object of the lawsuit.
* target[4]: "その全額出資子会社"
  - source_tokens: `29: "其", 32: "全", 33: "资", 34: "公", 35: "司"`
  - mapping_reason: Object of the lawsuit.
* target[5]: "3社を"
  - source_tokens: `30: "三", 31: "家"`
  - mapping_reason: Quantity modifier for the companies.
* target[6]: "提訴しました。"
  - source_tokens: `36: "提", 37: "起", 38: "诉", 39: "讼，"`
  - mapping_reason: Verb of the lawsuit.
* target[7]: "未登録の"
  - source_tokens: `44: "没", 45: "有", 46: "经", 47: "过", 48: "注", 49: "册"`
  - mapping_reason: Status of the assets.
* target[8]: "暗号資産証券「Tronix」および「BitTorrent」を"
  - source_tokens: `55: "加", 56: "密", 57: "资", 58: "产", 59: "证", 60: "券", 61: "Tronics", 62: "和", 63: "BitTorrent。"`
  - mapping_reason: Objects provided/sold.
* target[9]: "提供・販売したとして、"
  - source_tokens: `50: "提", 51: "供", 52: "和", 53: "出", 54: "售"`
  - mapping_reason: Action performed (provide and sell).
* target[10]: "SECは"
  - source_tokens: `6: "美", 7: "国", 8: "证", 9: "券", 10: "交", 11: "易", 12: "委", 13: "员", 14: "会"`
  - mapping_reason: Referring back to the subject.
* target[11]: "発表しました。"
  - source_tokens: `15: "宣", 16: "布"`
  - mapping_reason: Main verb of the sentence (announced).

result:
```html
0. <src>三月二十二号，</src> <tgt>3月22日、</tgt>; start=0.00, end=1.00
1. <src><|wait|></src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>美国证券交易委员会</src> <tgt>米証券取引委員会（SEC）が</tgt>; start=2.00, end=3.00
3. <src>宣布对加密资产</src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>企业家孙宇晨</src> <tgt>暗号資産起業家の</tgt>; start=4.00, end=5.00
5. <src>及其</src> <tgt>孫宇晨（ジャスティン・サン）氏と</tgt>; start=5.00, end=6.00
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
=== ZH_B00021_S00398_W000012 ===

source:
- language: Chinese
- transcription: 三月二十二号，美国证券交易委员会宣布对加密资产企业家孙宇晨及其三家全资公司提起诉讼，指控他们没有经过注册提供和出售加密资产证券Tronics和BitTorrent。
- source_tokens:
  0. 三
  1. 月
  2. 二
  3. 十
  4. 二
  5. 号，
  6. 美
  7. 国
  8. 证
  9. 券
  10. 交
  11. 易
  12. 委
  13. 员
  14. 会
  15. 宣
  16. 布
  17. 对
  18. 加
  19. 密
  20. 资
  21. 产
  22. 企
  23. 业
  24. 家
  25. 孙
  26. 宇
  27. 晨
  28. 及
  29. 其
  30. 三
  31. 家
  32. 全
  33. 资
  34. 公
  35. 司
  36. 提
  37. 起
  38. 诉
  39. 讼，
  40. 指
  41. 控
  42. 他
  43. 们
  44. 没
  45. 有
  46. 经
  47. 过
  48. 注
  49. 册
  50. 提
  51. 供
  52. 和
  53. 出
  54. 售
  55. 加
  56. 密
  57. 资
  58. 产
  59. 证
  60. 券
  61. Tronics
  62. 和
  63. BitTorrent。

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
  - source_tokens: `0: "三", 1: "月", 2: "二", 3: "十", 4: "二", 5: "号，"`
  - mapping_reason: Date expression (March 22nd).
* target[1]: "미국 증권거래위원회( SEC) 는"
  - source_tokens: `6: "美", 7: "国", 8: "证", 9: "券", 10: "交", 11: "易", 12: "委", 13: "员", 14: "会"`
  - mapping_reason: Subject entity (SEC).
* target[2]: "암호화폐 기업가"
  - source_tokens: `18: "加", 19: "密", 20: "资", 21: "产", 22: "企", 23: "业", 24: "家"`
  - mapping_reason: Description of the individual.
* target[3]: "저스틴 선과"
  - source_tokens: `25: "孙", 26: "宇", 27: "晨", 28: "及"`
  - mapping_reason: Name of the individual and conjunction.
* target[4]: "그의"
  - source_tokens: `29: "其"`
  - mapping_reason: Possessive pronoun.
* target[5]: "100% 자회사"
  - source_tokens: `30: "三", 32: "全", 33: "资", 34: "公", 35: "司"`
  - mapping_reason: Description of the companies (100% owned).
* target[6]: "3곳을"
  - source_tokens: `30: "三", 31: "家"`
  - mapping_reason: Quantity of companies.
* target[7]: "상대로"
  - source_tokens: `17: "对"`
  - mapping_reason: Preposition indicating the target of the lawsuit.
* target[8]: "소송을"
  - source_tokens: `38: "诉", 39: "讼，"`
  - mapping_reason: Object of the lawsuit.
* target[9]: "제기했다고"
  - source_tokens: `36: "提", 37: "起"`
  - mapping_reason: Verb of the lawsuit action.
* target[10]: "발표했습니다."
  - source_tokens: `15: "宣", 16: "布"`
  - mapping_reason: Main verb of the sentence.
* target[11]: "이들은"
  - source_tokens: `42: "他", 43: "们"`
  - mapping_reason: Anaphoric reference to the accused.
* target[12]: "미등록 암호화폐 증권인"
  - source_tokens: `44: "没", 45: "有", 46: "经", 47: "过", 48: "注", 49: "册", 55: "加", 56: "密", 57: "资", 58: "产", 59: "证", 60: "券"`
  - mapping_reason: Description of the illegal assets.
* target[13]: "' 트론( Tronix) '"
  - source_tokens: `61: "Tronics"`
  - mapping_reason: Specific asset name.
* target[14]: "과"
  - source_tokens: `52: "和"`
  - mapping_reason: Conjunction.
* target[15]: "' 비트토렌트( BitTorrent) '"
  - source_tokens: `63: "BitTorrent。"`
  - mapping_reason: Specific asset name.
* target[16]: "를"
  - source_tokens: `62: "和"`
  - mapping_reason: Object marker for the assets.
* target[17]: "제공 및 판매한"
  - source_tokens: `50: "提", 51: "供", 52: "和", 53: "出", 54: "售"`
  - mapping_reason: Actions performed on the assets.
* target[18]: "혐의를"
  - source_tokens: `40: "指", 41: "控"`
  - mapping_reason: Allegation context.
* target[19]: "받고 있습니다."
  - source_tokens: `40: "指", 41: "控"`
  - mapping_reason: Realization of the accusation state.

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
=== ZH_B00021_S06758_W000029 ===

source:
- language: Chinese
- transcription: 我仿佛看到了他们游走在太行山上的足迹，深一脚浅一脚；我仿佛听到了他们放歌太行山上的声音，时而高，时而低，时而欢快，时而呜咽。
- source_tokens:
  0. 我
  1. 仿
  2. 佛
  3. 看
  4. 到
  5. 了
  6. 他
  7. 们
  8. 游
  9. 走
  10. 在
  11. 太
  12. 行
  13. 山
  14. 上
  15. 的
  16. 足
  17. 迹，
  18. 深
  19. 一
  20. 脚
  21. 浅
  22. 一
  23. 脚；
  24. 我
  25. 仿
  26. 佛
  27. 听
  28. 到
  29. 了
  30. 他
  31. 们
  32. 放
  33. 歌
  34. 太
  35. 行
  36. 山
  37. 上
  38. 的
  39. 声
  40. 音，
  41. 时
  42. 而
  43. 高，
  44. 时
  45. 而
  46. 低，
  47. 时
  48. 而
  49. 欢
  50. 快，
  51. 时
  52. 而
  53. 呜
  54. 咽。

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
  - source_tokens: `8: "游", 9: "走", 10: "在", 11: "太", 12: "行", 13: "山"`
  - mapping_reason: "游走在太行山" corresponds to "태항산을 누비는".

* target[1]: "그들의 발자취가"
  - source_tokens: `6: "他", 7: "们", 16: "足", 17: "迹，"`
  - mapping_reason: "他们的足迹" corresponds to "그들의 발자취".

* target[2]: "보이는 듯합니다."
  - source_tokens: `0: "我", 1: "仿", 2: "佛", 3: "看", 4: "到", 5: "了"`
  - mapping_reason: "我仿佛看到了" corresponds to "보이는 듯합니다".

* target[3]: "깊게 얕게 내딛는"
  - source_tokens: `18: "深", 19: "一", 20: "脚", 21: "浅", 22: "一", 23: "脚"`
  - mapping_reason: "深一脚浅一脚" describes the movement.

* target[4]: "그 발걸음이요."
  - source_tokens: `16: "足", 17: "迹，"`
  - mapping_reason: Refers back to the footsteps mentioned in the previous unit.

* target[5]: "태항산에"
  - source_tokens: `34: "太", 35: "行", 36: "山", 37: "上"`
  - mapping_reason: Location reference "太行山上".

* target[6]: "울려 퍼지는"
  - source_tokens: `32: "放", 33: "歌"`
  - mapping_reason: "放歌" (singing loudly) corresponds to "울려 퍼지는".

* target[7]: "그들의 노래 소리가"
  - source_tokens: `30: "他", 31: "们", 39: "声", 40: "音"`
  - mapping_reason: "他们的声音" corresponds to "그들의 노래 소리".

* target[8]: "들리는 듯합니다."
  - source_tokens: `24: "我", 25: "仿", 26: "佛", 27: "听", 28: "到", 29: "了"`
  - mapping_reason: "我仿佛听到了" corresponds to "들리는 듯합니다".

* target[9]: "때로는"
  - source_tokens: `41: "时", 42: "而"`
  - mapping_reason: "时而" corresponds to "때로는".

* target[10]: "높게,"
  - source_tokens: `43: "高"`
  - mapping_reason: "高" corresponds to "높게".

* target[11]: "때로는"
  - source_tokens: `44: "时", 45: "而"`
  - mapping_reason: "时而" corresponds to "때로는".

* target[12]: "낮게,"
  - source_tokens: `46: "低"`
  - mapping_reason: "低" corresponds to "낮게".

* target[13]: "때로는"
  - source_tokens: `47: "时", 48: "而"`
  - mapping_reason: "时而" corresponds to "때로는".

* target[14]: "즐겁게,"
  - source_tokens: `49: "欢", 50: "快"`
  - mapping_reason: "欢快" corresponds to "즐겁게".

* target[15]: "또"
  - source_tokens: `51: "时"`
  - mapping_reason: "时" (as part of the final "时而") is emphasized by "또".

* target[16]: "때로는"
  - source_tokens: `51: "时", 52: "而"`
  - mapping_reason: "时而" corresponds to "때로는".

* target[17]: "흐느끼듯 합니다."
  - source_tokens: `53: "呜", 54: "咽"`
  - mapping_reason: "呜咽" corresponds to "흐느끼듯 합니다".

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
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同
  1. 样
  2. 也
  3. 是
  4. 针
  5. 对
  6. 要
  7. 留
  8. 意
  9. 金
  10. 钱
  11. 的
  12. 部
  13. 分，
  14. 我
  15. 们
  16. 从
  17. 这
  18. 里
  19. 呢
  20. 可
  21. 以
  22. 看
  23. 到
  24. 的
  25. 是
  26. 这
  27. 一
  28. 副
  29. 卡
  30. 片，
  31. 它
  32. 代
  33. 表
  34. 的
  35. 是
  36. 手。
  37. 那
  38. 么
  39. 手
  40. 的
  41. 时
  42. 候
  43. 呢，
  44. 通
  45. 常
  46. 它
  47. 非
  48. 常
  49. 的
  50. 直
  51. 白，
  52. 代
  53. 表
  54. 是
  55. 我
  56. 们
  57. 的
  58. 金
  59. 钱
  60. 呢，
  61. 可
  62. 能
  63. 就
  64. 尽
  65. 量
  66. 呢
  67. 不
  68. 要，
  69. 就
  70. 是
  71. 做
  72. 太
  73. 多
  74. 的
  75. 规
  76. 划，
  77. 尤
  78. 其
  79. 是
  80. 针
  81. 对
  82. 家
  83. 中
  84. 的
  85. 男
  86. 性
  87. 长
  88. 男。

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
  - source_tokens: `9: "金", 10: "钱"`
  - mapping_reason: "金钱" (money)
* target[1]: "조심해야 하는"
  - source_tokens: `7: "留", 8: "意"`
  - mapping_reason: "留意" (pay attention/be careful)
* target[2]: "부분도"
  - source_tokens: `11: "的", 12: "部", 13: "分"`
  - mapping_reason: "的部分" (part)
* target[3]: "마찬가지예요."
  - source_tokens: `0: "同", 1: "样", 2: "也", 3: "是"`
  - mapping_reason: "同样也是" (the same/likewise)
* target[4]: "여기 이 카드를 보면,"
  - source_tokens: `16: "从", 17: "这", 18: "里", 26: "这", 27: "一", 28: "副", 29: "卡", 30: "片"`
  - mapping_reason: "从这里可以看到这一副卡片" (look at this card here)
* target[5]: "이건"
  - source_tokens: `31: "它"`
  - mapping_reason: "它" (it)
* target[6]: "손을"
  - source_tokens: `36: "手", 39: "手"`
  - mapping_reason: "手" (hand)
* target[7]: "상징해요."
  - source_tokens: `32: "代", 33: "表"`
  - mapping_reason: "代表" (represent/symbolize)
* target[8]: "손은"
  - source_tokens: `39: "手"`
  - mapping_reason: "手" (hand)
* target[9]: "보통"
  - source_tokens: `44: "通", 45: "常"`
  - mapping_reason: "通常" (usually)
* target[10]: "아주"
  - source_tokens: `47: "非", 48: "常"`
  - mapping_reason: "非常" (very)
* target[11]: "직설적이에요."
  - source_tokens: `50: "直", 51: "白"`
  - mapping_reason: "直白" (direct/straightforward)
* target[12]: "그래서"
  - source_tokens: `63: "就"`
  - mapping_reason: "conjunction/inference"
* target[13]: "돈에 대해서는"
  - source_tokens: `58: "金", 59: "钱"`
  - mapping_reason: "金钱" (money)
* target[14]: "너무 많은 계획을"
  - source_tokens: `72: "太", 73: "多", 75: "规", 76: "划"`
  - mapping_reason: "太多的规划" (too many plans)
* target[15]: "세우지 않는 게"
  - source_tokens: `67: "不", 68: "要"`
  - mapping_reason: "不要" (don't)
* target[16]: "좋다는 걸"
  - source_tokens: `64: "尽", 65: "量"`
  - mapping_reason: "尽量" (as much as possible/advisable)
* target[17]: "의미해요."
  - source_tokens: `52: "代", 53: "表"`
  - mapping_reason: "代表" (represent/mean)
* target[18]: "특히"
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: "尤其是" (especially)
* target[19]: "집안의 장남이라면"
  - source_tokens: `82: "家", 83: "中", 85: "男", 86: "性", 87: "长", 88: "男"`
  - mapping_reason: "家中的男性长男" (eldest son in the family)
* target[20]: "더욱 그렇습니다."
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: "尤其是" (emphasizing the preceding condition)

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
8. <src>手。</src> <tgt><|wait|></tgt>; start=8.00, end=9.00
9. <src>那么</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>手的时候呢，</src> <tgt>손을 상징해요. 손은</tgt>; start=10.00, end=11.00
11. <src>通常</src> <tgt>보통</tgt>; start=11.00, end=12.00
12. <src>它非常</src> <tgt>아주</tgt>; start=12.00, end=13.00
13. <src>的直白，</src> <tgt>직설적이에요.</tgt>; start=13.00, end=14.00
14. <src>代表是我们的金钱</src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>呢，</src> <tgt><|wait|></tgt>; start=15.00, end=16.00
16. <src>可能就尽量呢</src> <tgt>그래서 돈에 대해서는</tgt>; start=16.00, end=17.00
17. <src>不要，</src> <tgt><|wait|></tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>就是做太多</src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>的规划，</src> <tgt>너무 많은 계획을 세우지 않는 게 좋다는 걸 의미해요.</tgt>; start=20.00, end=21.00
21. <src>尤其是</src> <tgt>특히</tgt>; start=21.00, end=22.00
22. <src><|wait|></src> <tgt><|wait|></tgt>; start=22.00, end=23.00
23. <src>针对家中的男性</src> <tgt><|wait|></tgt>; start=23.00, end=24.00
24. <src>长男。</src> <tgt>집안의 장남이라면 더욱 그렇습니다.</tgt>; start=24.00, end=24.87
```

- max_empty_window_count: 3


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[20]
  - verdict: mapping_error
  - reason: "The target unit '더욱 그렇습니다' summarizes the preceding advice rather than mapping to the isolated token '是'."
  - replace_source_tokens: 77: "尤", 78: "其", 79: "是", 80: "针", 81: "对", 82: "家", 83: "中", 84: "的", 85: "男", 86: "性", 87: "长", 88: "男"
  validation:
    scratchpad:
* target[0]: "돈을"
  - source_tokens: `9: "金", 10: "钱"`
  - mapping_reason: "金钱" (money)
* target[1]: "조심해야 하는"
  - source_tokens: `7: "留", 8: "意"`
  - mapping_reason: "留意" (be careful/mindful)
* target[2]: "부분도"
  - source_tokens: `12: "部", 13: "分，"`
  - mapping_reason: "部分" (part/aspect)
* target[3]: "마찬가지예요."
  - source_tokens: `0: "同", 1: "样", 2: "也", 3: "是"`
  - mapping_reason: "同样也是" (likewise/the same)
* target[4]: "여기 이 카드를 보면,"
  - source_tokens: `16: "从", 17: "这", 18: "里", 26: "这", 27: "一", 28: "副", 29: "卡", 30: "片"`
  - mapping_reason: "从这里可以看到这一副卡片" (looking at this card from here)
* target[5]: "이건"
  - source_tokens: `31: "它"`
  - mapping_reason: "它" (it/this)
* target[6]: "손을"
  - source_tokens: `36: "手"`
  - mapping_reason: "手" (hand)
* target[7]: "상징해요."
  - source_tokens: `32: "代", 33: "表"`
  - mapping_reason: "代表" (represent/symbolize)
* target[8]: "손은"
  - source_tokens: `39: "手"`
  - mapping_reason: "手" (hand)
* target[9]: "보통"
  - source_tokens: `44: "通", 45: "常"`
  - mapping_reason: "通常" (usually)
* target[10]: "아주"
  - source_tokens: `47: "非", 48: "常"`
  - mapping_reason: "非常" (very)
* target[11]: "직설적이에요."
  - source_tokens: `50: "直", 51: "白"`
  - mapping_reason: "直白" (straightforward)
* target[12]: "그래서"
  - source_tokens: `52: "代", 53: "表"`
  - mapping_reason: "代表" (implies the meaning, serving as a connector here)
* target[13]: "돈에 대해서는"
  - source_tokens: `58: "金", 59: "钱"`
  - mapping_reason: "金钱" (money)
* target[14]: "너무 많은 계획을"
  - source_tokens: `72: "太", 73: "多", 75: "规", 76: "划"`
  - mapping_reason: "太多的规划" (too many plans)
* target[15]: "세우지 않는 게"
  - source_tokens: `67: "不", 68: "要"`
  - mapping_reason: "不要" (do not)
* target[16]: "좋다는 걸"
  - source_tokens: `61: "可", 62: "能"`
  - mapping_reason: "可能" (suggests preference/advisability)
* target[17]: "의미해요."
  - source_tokens: `32: "代", 33: "表"`
  - mapping_reason: "代表" (meaning/signify)
* target[18]: "특히"
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: "尤其是" (especially)
* target[19]: "집안의 장남이라면"
  - source_tokens: `82: "家", 83: "中", 85: "男", 86: "性", 87: "长", 88: "男"`
  - mapping_reason: "家中的男性长男" (eldest son in the family)
* target[20]: "더욱 그렇습니다."
  - source_tokens: `79: "是"`
  - mapping_reason: "是" (emphasizes the condition)
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 1, "source_token_ids": [7, 8]},
  {"target_senseunit_id": 2, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1, 2, 3]},
  {"target_senseunit_id": 4, "source_token_ids": [16, 17, 18, 26, 27, 28, 29, 30]},
  {"target_senseunit_id": 5, "source_token_ids": [31]},
  {"target_senseunit_id": 6, "source_token_ids": [36]},
  {"target_senseunit_id": 7, "source_token_ids": [32, 33]},
  {"target_senseunit_id": 8, "source_token_ids": [39]},
  {"target_senseunit_id": 9, "source_token_ids": [44, 45]},
  {"target_senseunit_id": 10, "source_token_ids": [47, 48]},
  {"target_senseunit_id": 11, "source_token_ids": [50, 51]},
  {"target_senseunit_id": 12, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 13, "source_token_ids": [58, 59]},
  {"target_senseunit_id": 14, "source_token_ids": [72, 73, 75, 76]},
  {"target_senseunit_id": 15, "source_token_ids": [67, 68]},
  {"target_senseunit_id": 16, "source_token_ids": [61, 62]},
  {"target_senseunit_id": 17, "source_token_ids": [32, 33]},
  {"target_senseunit_id": 18, "source_token_ids": [77, 78]},
  {"target_senseunit_id": 19, "source_token_ids": [82, 83, 85, 86, 87, 88]},
  {"target_senseunit_id": 20, "source_token_ids": [79]}
]

- retry: 1/5
  status: failed_after_response
  reason: * target[20]
  - verdict: mapping_error
  - reason: "The source token '是' does not translate to '더욱 그렇습니다'. The target phrase is a functional unit emphasizing the preceding context, specifically anchored by '尤其是' (especially)."
  - replace_source_tokens: 77: "尤", 78: "其"
  validation:
    scratchpad:
* target[0]: "돈을"
  - source_tokens: `9: "金", 10: "钱"`
  - mapping_reason: Direct object of "money".
* target[1]: "조심해야 하는"
  - source_tokens: `7: "留", 8: "意"`
  - mapping_reason: Meaning of "to be careful/pay attention".
* target[2]: "부분도"
  - source_tokens: `12: "部", 13: "分，"`
  - mapping_reason: Meaning of "part".
* target[3]: "마찬가지예요."
  - source_tokens: `0: "同", 1: "样", 2: "也", 3: "是"`
  - mapping_reason: Meaning of "likewise/same".
* target[4]: "여기 이 카드를 보면,"
  - source_tokens: `16: "从", 17: "这", 18: "里", 26: "这", 27: "一", 28: "副", 29: "卡", 30: "片，"`
  - mapping_reason: "From here" and "this card".
* target[5]: "이건"
  - source_tokens: `31: "它"`
  - mapping_reason: Pronoun referring to the card.
* target[6]: "손을"
  - source_tokens: `36: "手。"`
  - mapping_reason: Meaning of "hand".
* target[7]: "상징해요."
  - source_tokens: `32: "代", 33: "表"`
  - mapping_reason: Meaning of "represent/symbolize".
* target[8]: "손은"
  - source_tokens: `39: "手"`
  - mapping_reason: Subject "hand".
* target[9]: "보통"
  - source_tokens: `44: "通", 45: "常"`
  - mapping_reason: Meaning of "usually".
* target[10]: "아주"
  - source_tokens: `47: "非", 48: "常"`
  - mapping_reason: Meaning of "very".
* target[11]: "직설적이에요."
  - source_tokens: `50: "直", 51: "白，"`
  - mapping_reason: Meaning of "straightforward".
* target[12]: "그래서"
  - source_tokens: `69: "就", 70: "是"`
  - mapping_reason: Connective implying the consequence of the hand's straightforwardness.
* target[13]: "돈에 대해서는"
  - source_tokens: `58: "金", 59: "钱"`
  - mapping_reason: Topic of "money".
* target[14]: "너무 많은 계획을"
  - source_tokens: `72: "太", 73: "多", 75: "规", 76: "划，"`
  - mapping_reason: Meaning of "too many plans".
* target[15]: "세우지 않는 게"
  - source_tokens: `67: "不", 68: "要，"`
  - mapping_reason: Meaning of "don't/not to".
* target[16]: "좋다는 걸"
  - source_tokens: `64: "尽", 65: "量"`
  - mapping_reason: Implied suggestion/advice.
* target[17]: "의미해요."
  - source_tokens: `52: "代", 53: "表"`
  - mapping_reason: Meaning of "signify/mean".
* target[18]: "특히"
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: Meaning of "especially".
* target[19]: "집안의 장남이라면"
  - source_tokens: `80: "针", 81: "对", 82: "家", 83: "中", 84: "的", 85: "男", 86: "性", 87: "长", 88: "男"`
  - mapping_reason: Target demographic: male eldest son in the family.
* target[20]: "더욱 그렇습니다."
  - source_tokens: `79: "是"`
  - mapping_reason: Affirmation/emphasis on the previous condition.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 1, "source_token_ids": [7, 8]},
  {"target_senseunit_id": 2, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1, 2, 3]},
  {"target_senseunit_id": 4, "source_token_ids": [16, 17, 18, 26, 27, 28, 29, 30]},
  {"target_senseunit_id": 5, "source_token_ids": [31]},
  {"target_senseunit_id": 6, "source_token_ids": [36]},
  {"target_senseunit_id": 7, "source_token_ids": [32, 33]},
  {"target_senseunit_id": 8, "source_token_ids": [39]},
  {"target_senseunit_id": 9, "source_token_ids": [44, 45]},
  {"target_senseunit_id": 10, "source_token_ids": [47, 48]},
  {"target_senseunit_id": 11, "source_token_ids": [50, 51]},
  {"target_senseunit_id": 12, "source_token_ids": [69, 70]},
  {"target_senseunit_id": 13, "source_token_ids": [58, 59]},
  {"target_senseunit_id": 14, "source_token_ids": [72, 73, 75, 76]},
  {"target_senseunit_id": 15, "source_token_ids": [67, 68]},
  {"target_senseunit_id": 16, "source_token_ids": [64, 65]},
  {"target_senseunit_id": 17, "source_token_ids": [52, 53]},
  {"target_senseunit_id": 18, "source_token_ids": [77, 78]},
  {"target_senseunit_id": 19, "source_token_ids": [80, 81, 82, 83, 84, 85, 86, 87, 88]},
  {"target_senseunit_id": 20, "source_token_ids": [79]}
]

- retry: 2/5
  status: succeeded
  reason: retry attempt succeeded

---
=== ZH_UJBZXO0vtl8_W000127 ===

source:
- language: Chinese
- transcription: 同样也是针对要留意金钱的部分，我们从这里呢可以看到的是这一副卡片，它代表的是手。那么手的时候呢，通常它非常的直白，代表是我们的金钱呢，可能就尽量呢不要，就是做太多的规划，尤其是针对家中的男性长男。
- source_tokens:
  0. 同
  1. 样
  2. 也
  3. 是
  4. 针
  5. 对
  6. 要
  7. 留
  8. 意
  9. 金
  10. 钱
  11. 的
  12. 部
  13. 分，
  14. 我
  15. 们
  16. 从
  17. 这
  18. 里
  19. 呢
  20. 可
  21. 以
  22. 看
  23. 到
  24. 的
  25. 是
  26. 这
  27. 一
  28. 副
  29. 卡
  30. 片，
  31. 它
  32. 代
  33. 表
  34. 的
  35. 是
  36. 手。
  37. 那
  38. 么
  39. 手
  40. 的
  41. 时
  42. 候
  43. 呢，
  44. 通
  45. 常
  46. 它
  47. 非
  48. 常
  49. 的
  50. 直
  51. 白，
  52. 代
  53. 表
  54. 是
  55. 我
  56. 们
  57. 的
  58. 金
  59. 钱
  60. 呢，
  61. 可
  62. 能
  63. 就
  64. 尽
  65. 量
  66. 呢
  67. 不
  68. 要，
  69. 就
  70. 是
  71. 做
  72. 太
  73. 多
  74. 的
  75. 规
  76. 划，
  77. 尤
  78. 其
  79. 是
  80. 针
  81. 对
  82. 家
  83. 中
  84. 的
  85. 男
  86. 性
  87. 长
  88. 男。

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
  - source_tokens: `9: "金", 10: "钱"`
  - mapping_reason: Direct translation of "money".
* target[1]: "注意すべき"
  - source_tokens: `7: "留", 8: "意"`
  - mapping_reason: Direct translation of "pay attention to".
* target[2]: "点について"
  - source_tokens: `11: "的", 12: "部", 13: "分"`
  - mapping_reason: Corresponds to "the part regarding...".
* target[3]: "ですが、"
  - source_tokens: `19: "呢"`
  - mapping_reason: Discourse marker indicating a transition or topic shift.
* target[4]: "ここで"
  - source_tokens: `16: "从", 17: "这", 18: "里"`
  - mapping_reason: Spatial reference "from here".
* target[5]: "見えているのは"
  - source_tokens: `20: "可", 21: "以", 22: "看", 23: "到", 24: "的", 25: "是"`
  - mapping_reason: Translation of "what can be seen is".
* target[6]: "このカードです。"
  - source_tokens: `26: "这", 27: "一", 28: "副", 29: "卡", 30: "片"`
  - mapping_reason: Translation of "this card".
* target[7]: "これは"
  - source_tokens: `31: "它"`
  - mapping_reason: Subject pronoun "it".
* target[8]: "「手」を"
  - source_tokens: `36: "手"`
  - mapping_reason: Object "hand".
* target[9]: "表しています。"
  - source_tokens: `32: "代", 33: "表", 34: "的", 35: "是"`
  - mapping_reason: Translation of "represents".
* target[10]: "手というのは"
  - source_tokens: `39: "手", 40: "的", 41: "时", 42: "候", 43: "呢"`
  - mapping_reason: Topic marker "as for the hand".
* target[11]: "通常、"
  - source_tokens: `44: "通", 45: "常"`
  - mapping_reason: Translation of "usually".
* target[12]: "とても"
  - source_tokens: `47: "非", 48: "常", 49: "的"`
  - mapping_reason: Translation of "very".
* target[13]: "ストレートで、"
  - source_tokens: `50: "直", 51: "白"`
  - mapping_reason: Translation of "straightforward".
* target[14]: "お金に関しては"
  - source_tokens: `58: "金", 59: "钱", 60: "呢"`
  - mapping_reason: Topic "regarding money".
* target[15]: "あまり"
  - source_tokens: `67: "不", 68: "要"`
  - mapping_reason: Negative modifier "not too much".
* target[16]: "計画を"
  - source_tokens: `75: "规", 76: "划"`
  - mapping_reason: Object "plan".
* target[17]: "立てすぎない"
  - source_tokens: `72: "太", 73: "多", 74: "的"`
  - mapping_reason: Verb phrase "not make too many".
* target[18]: "方がいい"
  - source_tokens: `61: "可", 62: "能", 63: "就"`
  - mapping_reason: Suggestive modal structure "better to".
* target[19]: "ということを"
  - source_tokens: `69: "就", 70: "是", 71: "做"`
  - mapping_reason: Nominalizer for the preceding clause.
* target[20]: "示しています。"
  - source_tokens: `52: "代", 53: "表", 54: "是"`
  - mapping_reason: Translation of "indicates/represents".
* target[21]: "特に"
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: Translation of "especially".
* target[22]: "家庭の長男については"
  - source_tokens: `79: "是", 80: "针", 81: "对", 82: "家", 83: "中", 84: "的", 85: "男", 86: "性", 87: "长", 88: "男"`
  - mapping_reason: Target demographic "regarding the eldest son of the family".
* target[23]: "そうです。"
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: Confirmatory reference to the previous advice for the specific demographic.

result:
```html
0. <src>同样也是</src> <tgt><|wait|></tgt>; start=0.00, end=1.00
1. <src>针对要留意</src> <tgt><|wait|></tgt>; start=1.00, end=2.00
2. <src>金钱的部分，</src> <tgt>お金に注意すべき点について</tgt>; start=2.00, end=3.00
3. <src><|wait|></src> <tgt><|wait|></tgt>; start=3.00, end=4.00
4. <src>我们从这里呢</src> <tgt>ですが、ここで</tgt>; start=4.00, end=5.00
5. <src>可以看到的是</src> <tgt>見えているのは</tgt>; start=5.00, end=6.00
6. <src>这一副卡片，</src> <tgt>このカードです。</tgt>; start=6.00, end=7.00
7. <src>它代表的是</src> <tgt>これは</tgt>; start=7.00, end=8.00
8. <src>手。</src> <tgt>「手」を表しています。</tgt>; start=8.00, end=9.00
9. <src>那么</src> <tgt><|wait|></tgt>; start=9.00, end=10.00
10. <src>手的时候呢，</src> <tgt>手というのは</tgt>; start=10.00, end=11.00
11. <src>通常</src> <tgt>通常、</tgt>; start=11.00, end=12.00
12. <src>它非常</src> <tgt><|wait|></tgt>; start=12.00, end=13.00
13. <src>的直白，</src> <tgt>とてもストレートで、</tgt>; start=13.00, end=14.00
14. <src>代表是我们的金钱</src> <tgt><|wait|></tgt>; start=14.00, end=15.00
15. <src>呢，</src> <tgt>お金に関しては</tgt>; start=15.00, end=16.00
16. <src>可能就尽量呢</src> <tgt><|wait|></tgt>; start=16.00, end=17.00
17. <src>不要，</src> <tgt>あまり</tgt>; start=17.00, end=18.00
18. <src><|wait|></src> <tgt><|wait|></tgt>; start=18.00, end=19.00
19. <src>就是做太多</src> <tgt><|wait|></tgt>; start=19.00, end=20.00
20. <src>的规划，</src> <tgt>計画を立てすぎない方がいいということを示しています。</tgt>; start=20.00, end=21.00
21. <src>尤其是</src> <tgt>特に</tgt>; start=21.00, end=22.00
22. <src><|wait|></src> <tgt><|wait|></tgt>; start=22.00, end=23.00
23. <src>针对家中的男性</src> <tgt><|wait|></tgt>; start=23.00, end=24.00
24. <src>长男。</src> <tgt>家庭の長男についてはそうです。</tgt>; start=24.00, end=24.87
```

- max_empty_window_count: 2


attempts:

- retry: 0/5
  status: failed_after_response
  reason: * target[3]
  - verdict: mapping_error
  - reason: "The discourse connector 'ですが' (but/however) is a functional unit that does not map to '同样也是', which refers to the previous context. The source token '呢' (index 19) serves as the discourse-marking anchor."
  - replace_source_tokens: 19: "呢"

* target[23]
  - verdict: mapping_error
  - reason: "The target unit 'そうです。' refers to the preceding advice, while the mapped source tokens '尤其是针对' are clearly intended to introduce the specific demographic (the eldest son) mentioned in the next phrase."
  - replace_source_tokens: 77: "尤", 78: "其"
  validation:
    scratchpad:
* target[0]: "お金に"
  - source_tokens: `9: "金", 10: "钱"`
  - mapping_reason: Direct reference to money.
* target[1]: "注意すべき"
  - source_tokens: `7: "留", 8: "意"`
  - mapping_reason: Direct translation of "留意".
* target[2]: "点について"
  - source_tokens: `12: "部", 13: "分，"`
  - mapping_reason: "部分" refers to the point or aspect being discussed.
* target[3]: "ですが、"
  - source_tokens: `0: "同", 1: "样", 2: "也", 3: "是"`
  - mapping_reason: Discourse marker indicating continuation/relation to previous topic.
* target[4]: "ここで"
  - source_tokens: `16: "从", 17: "这", 18: "里"`
  - mapping_reason: "从这里" translates to "here".
* target[5]: "見えているのは"
  - source_tokens: `20: "可", 21: "以", 22: "看", 23: "到", 24: "的", 25: "是"`
  - mapping_reason: "可以看到的是" translates to "what is seen is".
* target[6]: "このカードです。"
  - source_tokens: `26: "这", 27: "一", 28: "副", 29: "卡", 30: "片，"`
  - mapping_reason: Direct reference to "这一副卡片".
* target[7]: "これは"
  - source_tokens: `31: "它"`
  - mapping_reason: Anaphoric reference to the card.
* target[8]: "「手」を"
  - source_tokens: `36: "手。"`
  - mapping_reason: The object being represented.
* target[9]: "表しています。"
  - source_tokens: `32: "代", 33: "表", 34: "的", 35: "是"`
  - mapping_reason: Verb of representation.
* target[10]: "手というのは"
  - source_tokens: `39: "手", 40: "的", 41: "时", 42: "候"`
  - mapping_reason: Topic marker for "hand".
* target[11]: "通常、"
  - source_tokens: `44: "通", 45: "常"`
  - mapping_reason: Direct translation of "通常".
* target[12]: "とても"
  - source_tokens: `47: "非", 48: "常"`
  - mapping_reason: Adverb of degree.
* target[13]: "ストレートで、"
  - source_tokens: `50: "直", 51: "白，"`
  - mapping_reason: Direct translation of "直白".
* target[14]: "お金に関しては"
  - source_tokens: `58: "金", 59: "钱"`
  - mapping_reason: Topic marker for money.
* target[15]: "あまり"
  - source_tokens: `64: "尽", 65: "量"`
  - mapping_reason: Qualifier for the extent of planning.
* target[16]: "計画を"
  - source_tokens: `75: "规", 76: "划，"`
  - mapping_reason: Direct translation of "规划".
* target[17]: "立てすぎない"
  - source_tokens: `67: "不", 68: "要，", 72: "太", 73: "多"`
  - mapping_reason: Negative instruction regarding excess planning.
* target[18]: "方がいい"
  - source_tokens: `61: "可", 62: "能", 63: "就"`
  - mapping_reason: Modal advice structure.
* target[19]: "ということを"
  - source_tokens: `52: "代", 53: "表", 54: "是"`
  - mapping_reason: Discourse connector linking the advice to the symbolic meaning.
* target[20]: "示しています。"
  - source_tokens: `69: "就", 70: "是"`
  - mapping_reason: Realization of the underlying meaning.
* target[21]: "特に"
  - source_tokens: `77: "尤", 78: "其"`
  - mapping_reason: Direct translation of "尤其是".
* target[22]: "家庭の長男については"
  - source_tokens: `82: "家", 83: "中", 84: "的", 85: "男", 86: "性", 87: "长", 88: "男。"`
  - mapping_reason: Specific demographic focus.
* target[23]: "そうです。"
  - source_tokens: `79: "是", 80: "针", 81: "对"`
  - mapping_reason: Affirmation of the scope of the previous point.
    result:
[
  {"target_senseunit_id": 0, "source_token_ids": [9, 10]},
  {"target_senseunit_id": 1, "source_token_ids": [7, 8]},
  {"target_senseunit_id": 2, "source_token_ids": [12, 13]},
  {"target_senseunit_id": 3, "source_token_ids": [0, 1, 2, 3]},
  {"target_senseunit_id": 4, "source_token_ids": [16, 17, 18]},
  {"target_senseunit_id": 5, "source_token_ids": [20, 21, 22, 23, 24, 25]},
  {"target_senseunit_id": 6, "source_token_ids": [26, 27, 28, 29, 30]},
  {"target_senseunit_id": 7, "source_token_ids": [31]},
  {"target_senseunit_id": 8, "source_token_ids": [36]},
  {"target_senseunit_id": 9, "source_token_ids": [32, 33, 34, 35]},
  {"target_senseunit_id": 10, "source_token_ids": [39, 40, 41, 42]},
  {"target_senseunit_id": 11, "source_token_ids": [44, 45]},
  {"target_senseunit_id": 12, "source_token_ids": [47, 48]},
  {"target_senseunit_id": 13, "source_token_ids": [50, 51]},
  {"target_senseunit_id": 14, "source_token_ids": [58, 59]},
  {"target_senseunit_id": 15, "source_token_ids": [64, 65]},
  {"target_senseunit_id": 16, "source_token_ids": [75, 76]},
  {"target_senseunit_id": 17, "source_token_ids": [67, 68, 72, 73]},
  {"target_senseunit_id": 18, "source_token_ids": [61, 62, 63]},
  {"target_senseunit_id": 19, "source_token_ids": [52, 53, 54]},
  {"target_senseunit_id": 20, "source_token_ids": [69, 70]},
  {"target_senseunit_id": 21, "source_token_ids": [77, 78]},
  {"target_senseunit_id": 22, "source_token_ids": [82, 83, 84, 85, 86, 87, 88]},
  {"target_senseunit_id": 23, "source_token_ids": [79, 80, 81]}
]

- retry: 1/5
  status: succeeded
  reason: retry attempt succeeded

---
