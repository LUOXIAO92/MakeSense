# MakeSense 核心技术总结

## 1. 一句话结论

MakeSense 把语音翻译训练成一条受监督的流式决策轨迹。模型每收到一个音频窗口，就要回答一个小问题：现在该说什么，还是该等。

输出协议很简单：

```text
<src>...</src><tgt>...</tgt>
```

源侧可以释放转写，目标侧可以释放翻译。任何一侧证据不足，就写 `<|wait|>`。训练样本记录“第 1 个窗口怎么反应，第 2 个窗口怎么反应，第 3 个窗口怎么反应”。

这条轨迹模仿同传员的局部动作：听到一小段，判断源语能不能说；再判断目标语能不能说；如果目标语还依赖未来信息，就继续等。

请参照：

- `README.md`
- `src/core/build_conversation.py`
- `src/train/formatting.py`

## 2. 核心抽象：软算法提出策略，硬算法收束轨迹

MakeSense 的核心机制可以概括成三层：

1. prompt 写出同传策略。
2. validator 拒绝不能形成轨迹的输出。
3. deterministic builder 把通过检查的结构合成 `<src>` / `<tgt>` / `<|wait|>`。

prompt 是软算法。它用自然语言告诉 LLM 什么叫“可释放”。例如 pipeline 5 的 prompt 要求模型在窗口压力下释放“最小稳定意义单元”。这像同传员的经验规则：能说一个稳定片段，就别为了等完整句拖太久；稳定片段还没出现，但已经等不起，就释放一个可解释的局部片段。

validator 是硬算法。它跳过审美判断，只检查轨迹能不能用。举个简化例子：

```text
W0: {0: "By", 1: "default,"}
W1: {2: "if", 3: "you", 4: "create"}
```

prompt 可以建议模型把 “By default,” 作为一个 source release unit。validator 会检查这些 token 是否只出现一次、是否漏掉、是否等了太多非空窗口、是否把太长的 token 串塞进一个 release unit。模型如果连续等待，validator 会把问题渲染成窗口级错误，再送回 retry prompt。

这就是“软算法 + 硬算法”的分工：prompt 负责表达同传策略，validator 负责把策略压进可训练、可投射、可重试的结构。

请参照：

- `src/pipeline/prompts/time_pressure_segmentation.py`
- `src/pipeline/validators/transcription_segmentation_validator.py`
- `src/pipeline/providers/retry_error_rendering.py`

## 3. 源侧释放：从听到词到决定能不能说

pipeline 5 解决第一个核心问题：源侧什么时候释放转写。

普通文本切分会等更完整的句法结构。同传要先处理延迟。pipeline 5 的 prompt 把优先级写得很清楚：先满足窗口压力，再释放最小稳定意义单元，必要时做 latency-forced partial release。

看一个小例子：

```text
W0: {0: "By", 1: "default,"}
W1: {2: "if", 3: "you", 4: "create"}
W2: {5: "a", 6: "file"}
```

如果模型在 W0 不释放，它还可以等 W1，看 “By default, if you create” 是否形成更稳定结构。但它不能一直等到 W2 或更后面才说。validator 会重建每个窗口的输入和输出。如果非空窗口连续没有输出，它会报“等待过久”。如果模型把 `[0,1,2,3,4,5,6]` 都塞进一个 release unit，它会报 oversized。retry 时，LLM 会看到这些窗口级问题，只能重新给出更短、更早、更可释放的分组。

这里的关键在于切分策略。prompt 教 LLM 像同传员一样切，validator 用时间窗口约束它不能逃避延迟压力。

这一阶段产出 source sense units。后面的 builder 会根据每个 source unit 的结束时间，把它投射到对应窗口。如果当前窗口没有可释放 source unit，就输出 `<src><|wait|></src>`。

请参照：

- `examples/pipeline_5_asr_segmentation.py`
- `src/pipeline/prompts/time_pressure_segmentation.py`
- `src/pipeline/validators/transcription_segmentation_validator.py`
- `src/core/build_conversation.py`

## 4. 目标语重构：把完整句译文改成能边听边说的译文

pipeline 6 解决第二个核心问题：完整句译文常常不适合同传。

整句翻译会追求静态自然。它可能把关键谓语放在句尾，也可能把一串修饰语压在一个名词前。读起来没问题，边听边说就会卡住。模型需要把 raw translation 改成更线性、更容易逐段释放的目标语。

例子：

```text
raw translation:
The report on the policy changes announced by the committee yesterday explains the issue.
```

这句话把 “explains the issue” 放到最后。听众要等很久才知道主动作。pipeline 6 的 prompt 会要求 LLM 保留意义，但把目标语改成更适合同传的结构，例如先说主干，再补细节：

```text
The report explains the issue. It covers the policy changes announced by the committee yesterday.
```

validator 先用 token alignment 找 order-risk 区域：目标语某一段如果依赖很晚才出现的 source window，又挡住后面已经可用的信息，就触发检查。semantic checker 只看这个局部区域，并且只有在存在同样自然、同样忠实、source-window blocking 更低的改写时，才返回 `rewrite_recommend`。

`rewrite_recommend` 是窄信号。它表达的意思是：这个局部顺序会阻碍流式释放，并且有明确替代写法。这条反馈会进入 retry prompt，让主 LLM 重构目标语。

请参照：

- `examples/pipeline_6_translation_reconstruction.py`
- `src/pipeline/prompts/translation_reconstruction.py`
- `src/pipeline/validators/reconstruction_validator.py`

## 5. 目标侧切分：决定目标语以什么单位释放

pipeline 7 解决第三个核心问题：目标语重构后，系统还要知道目标侧以什么单位释放。

目标语不能按任意 token 切。一个 compact modifier-head 关系要尽量留在一起；一个固定表达也要留在一起。比如：

```text
target tokens:
0: "this"
1: "file"
2: "called"
3: "source/index"
```

`this file` 是紧密局部单位。模型如果切成 `[0] [1]`，目标语会碎。prompt 要求 LLM 切 minimal sense units，同时保持局部凝聚。合理切法可能是：

```text
[[0,1], [2,3]]
```

如果模型把太多 token 放进一个单位，例如把整段目标语都塞进 `[0,1,2,3,...]`，当前 validator 会按语言阈值报 oversized，并把错误送回 retry。

这里有一个必须写清楚的边界：prompt 要求完整覆盖、顺序、连续 span；当前 `pure_text_segmentation_validator.py` 只硬检查 oversized chunks。覆盖、顺序和连续性主要靠 prompt contract 约束，部分问题会在 pipeline 8 的 mapping validation 或 downstream readiness 中继续暴露。

这一步之后，目标语从“一整段字符串”变成一组可映射、可等待、可释放的 target sense units。

请参照：

- `examples/pipeline_7_pure_text_segmentation.py`
- `src/pipeline/prompts/pure_text_segmentation.py`
- `src/pipeline/validators/pure_text_segmentation_validator.py`

## 6. 目标证据映射：每个译文片段要等哪些源侧证据

pipeline 8 解决第四个核心问题：每个目标语片段要等哪些源侧证据。

同传中，目标语切好以后还要等证据。一个 target unit 可能依赖多个 source tokens。只有这些 source tokens 都已经通过源侧 release window 变得可用，目标语才能释放。

例子：

```text
source tokens:
0: "this"
1: "file"
2: "called"
3: "source/index"

target unit:
0: "this file"
```

这个 target unit 至少依赖 source token 0 和 1。另一个 target unit “called source/index” 可能依赖 2 和 3。mapping 结果服务 release timing：target[0] 要等 source[0] 和 source[1] ready；target[1] 要等 source[2] 和 source[3] ready。

还有更难的情况。目标语里的代词、连接词、解释性结构，可能没有一一对应的 source word。prompt 允许把这些 target-side functional units 映射到 reference、relation、discourse token。validator 不会因为某个 source token 重复出现就判错。它把重复 token、过大依赖、dependency frontier backjump 当成 suspicious triggers，再交给 semantic checker 判断。

hard validator 做三件事。它先检查 target ids 是否完整、source ids 是否有效。然后检查 mapping 能不能投射到下游 release windows。如果 source segmentation 漏了某个 word，validator 会报 upstream dependency error，防止 LLM 用虚构 source ids 掩盖前面的问题。最后 semantic checker 只在能给出明确替换 source tokens 时返回 `mapping_error`。

这一步给 target release timing 装上证据锁。目标语单位只有拿到自己依赖的 source evidence 后，才有资格输出。

请参照：

- `examples/pipeline_8_target_centric_mapping.py`
- `src/pipeline/prompts/target_centric_mapping.py`
- `src/pipeline/validators/target_centric_mapping_validator.py`

## 7. 确定性合成：把策略材料变成 `<src>/<tgt>/<|wait|>`

前面的 LLM stages 生成策略材料。最后一步交给确定性算法，把材料合成逐窗口标签。

源侧规则很直接。source sense unit 的最后一个 word 落入哪个 audio window，它就在哪个 window 释放。当前窗口没有可释放 source unit，就写：

```text
<src><|wait|></src>
```

目标侧要多算一层。系统先把 source token 映射到 timed source word，再把 source word 映射到 source release window。然后读取 target-source mapping，计算每个 target unit 的 ready window。

例子：

```text
target[3] depends on source token 8
source token 8 becomes ready at window 4
tolerance cadence allows target emission at window 5
```

target[3] 不能在 window 3 输出，也不能在 window 4 输出。它最早等到 source evidence ready 后，再等 cadence 允许。这个例子里，它在 window 5 才能释放。window 4 的目标侧仍然输出：

```text
<tgt><|wait|></tgt>
```

所以 LLM 不直接写最终轨迹。LLM 写 source units、target units 和 evidence mapping；builder 根据时间和 tolerance 生成训练标签。

请参照：

- `src/core/build_conversation.py`

## 8. 训练意义：模型学的是局部同传动作

最终训练样本是一段多轮对话：

```text
system: Translate to English, tolerance window size is 2
user: <audio chunk 1>
assistant: <src>...</src><tgt><|wait|></tgt>
user: <audio chunk 2>
assistant: <src><|wait|></src><tgt>...</tgt>
```

每轮 user 只给一个音频窗口。assistant 必须输出当前窗口下的源侧动作和目标侧动作。模型学习局部策略：听到这一秒后能说什么，应该等什么，什么时候把前面积累的目标语释放出来。

训练时，collator 把真实音频切成 chunks，并检查 chunk 数和输出 blocks 对齐。assistant-only loss 只训练 assistant 的输出。严格流式测试生成第 k 个 assistant turn 时，只给模型第 k 轮之前的 messages 和当前可见 audio chunks。模型看不到未来音频。

请参照：

- `src/data_loader/dataset.py`
- `src/train/formatting.py`
- `src/train/lora_trainer.py`
- `src/train/tester.py`

## 9. 收束段

MakeSense 没有让一个模型凭空生成整条同传轨迹。它把同传拆成四个可检查的问题：源侧何时释放，目标语如何重构，目标侧以什么单位释放，每个目标单位要等哪些源侧证据。

prompt 提供同传员式策略。validator 把策略限制在可用结构里。deterministic builder 把结构投射成逐窗口 `<src>`、`<tgt>` 和 `<|wait|>`。这三层合起来，才形成可以训练 omni model 的流式同传轨迹。
