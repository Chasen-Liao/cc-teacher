# 随堂测验 - LangChain 基础

## Q1: LangChain 六大核心模块

LangChain 包含哪六大核心模块？请列举。

**答案**:
1. **Model I/O** - 与 LLM 模型交互
2. **Retrieval** - 从外部数据源检索
3. **Chains** - 组件串联流水线
4. **Agents** - 自主决策智能体
5. **Memory** - 跨对话记忆
6. **Callbacks** - 日志监控

---

## Q2: LCEL 语法

以下代码的输出是什么？

```python
prompt | llm | output_parser
```

**答案**: 这是一个 LCEL 链式调用声明，表示：
1. prompt 作为输入
2. 经过 llm 处理
3. 再经过 output_parser 解析输出

**注意**: 这是声明式语法，实际执行需要调用 `.invoke()`

---

## Q3: Agent 与 Chain 的区别

简述 Agent 和 Chain 的主要区别。

**答案**:

| 特性 | Chain | Agent |
|-----|-------|-------|
| 执行方式 | 固定流程 | 动态决策 |
| 工具调用 | 手动 | 自动 |
| 循环控制 | 无 | 有 |
| 适用场景 | 确定性任务 | 开放性任务 |

---

## Q4: 代码补全

完成以下代码，创建一个简单的 Agent：

```python
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool

# 初始化 Agent，agent 参数应该填什么？
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=______,  # 填什么？
    verbose=True
)
```

**答案**: `AgentType.ZERO_SHOT_REACT_DESCRIPTION`

这是最常用的 Agent 类型，适合通用任务。

---

## Q5: 判断题

以下说法是否正确？

1. LLM 本身有记忆功能，可以记住之前的对话
2. LCEL 中的 `|` 符号表示管道操作
3. 一个 Agent 必须至少有一个 Tool

**答案**:
1. ❌ 错误 - LLM 本身无状态，记忆需要通过 Memory 组件实现
2. ✅ 正确 - `|` 是 LCEL 的管道操作符
3. ✅ 正确 - Agent 通过调用 Tool 与外界交互，没有 Tool 的 Agent 无法执行有意义的任务
