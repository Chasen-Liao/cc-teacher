# Memory 记忆系统

## 为什么需要 Memory？

LLM 本身无状态，每次调用都是独立的。Memory 让 Agent 记住对话历史，实现多轮交互。

```
无 Memory: 每个问题独立回答
有 Memory: 理解上下文，记住之前说过什么
```

## Memory 类型

### 1. ConversationBufferMemory

最简单的内存，直接保存完整对话历史：

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory)

chain.run("我叫张三")
chain.run("你记得我叫什么吗？")  # 输出: 你叫张三
```

### 2. ConversationBufferWindowMemory

只保留最近 k 轮对话，节省 token：

```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=5)  # 只保留最近5轮
```

### 3. ConversationSummaryMemory

对长对话进行摘要，节省 token：

```python
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(llm=llm)
```

### 4. VectorStoreRetrieverMemory

基于向量检索的记忆，可以记住任意相关的历史：

```python
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

vectorstore = Chroma(embedding_function=OpenAIEmbeddings())
memory = VectorStoreRetrieverMemory(vectorstore=vectorstore)
```

## 与 Agent 集成

```python
from langchain.agents import AgentType, initialize_agent

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory,  # 传入 memory
    verbose=True
)
```

## 手动管理 Memory

有时需要更精细的控制：

```python
# 保存自定义信息
memory.save_context(
    {"input": "用户说了什么"},
    {"output": "AI 回答了什么"}
)

# 加载历史
history = memory.load_memory_variables({})
```

## Memory 最佳实践

| 场景 | 推荐 Memory |
|-----|------------|
| 短对话 | BufferMemory |
| 长对话 | SummaryMemory |
| 精准检索 | VectorStoreRetrieverMemory |
| 混合需求 | 组合使用 |

## Token 限制

注意对话历史会消耗 token：

```python
# 估算 token
def estimate_tokens(messages):
    return sum(len(m.content) // 4 for m in messages)

# 设置最大 token
memory = ConversationBufferMemory(
    max_token_limit=2000
)
```
