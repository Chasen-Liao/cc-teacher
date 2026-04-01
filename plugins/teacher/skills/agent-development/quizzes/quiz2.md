# 随堂测验 - Agent 开发实战

## Q1: Tool 定义

以下哪个是定义 Tool 的正确方式？

```python
# A
def search(query):
    return f"结果: {query}"

# B
@tool
def search(query: str) -> str:
    """搜索工具"""
    return f"结果: {query}"

# C
Tool(func=search, name="search", description="搜索")
```

**答案**: B 和 C 都正确，但使用方式不同：
- B 使用 `@tool` 装饰器，自动生成 name 和 schema
- C 直接实例化 Tool 类

A 缺少装饰器或 Tool 包装，无法被 Agent 识别。

---

## Q2: Memory 类型选择

根据场景选择最合适的 Memory 类型：

| 场景 | 选择 |
|-----|------|
| 短对话，5轮以内 | _______ |
| 长对话，需要节省 token | _______ |
| 需要检索历史中的相关信息 | _______ |

**答案**:
| 场景 | 选择 |
|-----|------|
| 短对话，5轮以内 | ConversationBufferMemory |
| 长对话，需要节省 token | ConversationSummaryMemory |
| 需要检索历史中的相关信息 | VectorStoreRetrieverMemory |

---

## Q3: RAG 工作流程排序

将 RAG 的工作流程按正确顺序排列：

1. ______
2. ______
3. ______
4. ______
5. ______

选项：
- A. 向量存储
- B. 文档分割
- C. 检索相关文档
- D. 生成答案
- E. 文档加载

**答案**: E → B → A → C → D
1. E. 文档加载 - 读取原始文档
2. B. 文档分割 - 切成小块
3. A. 向量存储 - 嵌入并存储
4. C. 检索相关文档 - 找到相关内容
5. D. 生成答案 - LLM 综合回答

---

## Q4: 代码调试

以下代码有什么问题？

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
agent = initialize_agent(
    tools, llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory
)
agent.run("我叫张三")
# 没有保存 memory 就退出了
```

**答案**: 问题是 **记忆没有持久化**。

程序退出后，memory 中的对话历史会丢失。下次启动 Agent 时无法记住之前的对话。

**解决方案**:
```python
# 使用 ChatMessageHistory 持久化
from langchain.memory import ChatMessageHistory
import pickle

history = ChatMessageHistory()
memory = ConversationBufferMemory(chat_memory=history)

# 对话结束后保存
with open("history.pkl", "wb") as f:
    pickle.dump(history, f)
```

---

## Q5: 实战应用

设计一个"新闻助手"Agent，需要：
1. 能搜索最新新闻
2. 能记住用户关注的领域
3. 能根据上下文回答后续问题

请写出核心代码结构。

**答案参考**:

```python
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory

# 1. 搜索工具
search_tool = Tool(name="search_news", func=search_news, description="搜索新闻")

# 2. 记忆组件
memory = ConversationBufferMemory(memory_key="chat_history")

# 3. 初始化 Agent
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# 使用示例
agent.run("我对 AI 领域的新闻感兴趣")
agent.run("最近有什么 AI 新闻吗？")  # 会结合之前的上下文
```
