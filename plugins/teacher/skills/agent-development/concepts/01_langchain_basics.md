# LangChain 基础概念

## 什么是 LangChain？

LangChain 是一个用于构建 LLM 应用的框架，它将 LLM 与外部数据源、工具、记忆系统连接起来，实现复杂的 AI 应用。

### 核心价值

```
LLM（大脑）+ Tools（手脚）+ Memory（记忆）= Agent（智能体）
```

## LangChain 六大模块

### 1. Model I/O
与 LLM 模型交互的接口
```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-4")
response = llm.invoke([HumanMessage(content="Hello!")])
```

### 2. Retrieval
从外部数据源检索信息
```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
```

### 3. Chains
将多个组件串联成流水线
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template("{input}"))
```

### 4. Agents
能够自主决策和执行动作的智能体
```python
from langchain.agents import Agent, Tool
agent = Agent(tools=tools, llm=llm)
```

### 5. Memory
跨对话的持久化记忆
```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
```

### 6. Callbacks
日志、监控、流式输出
```python
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
```

## LangChain Expression Language (LCEL)

LCEL 是 LangChain v1.x 的声明式语法，让 chain 定义更简洁：

```python
chain = prompt | llm | output_parser
```

### 为什么用 LCEL？

| 传统方式 | LCEL 方式 |
|---------|----------|
| 显式调用 `chain.run()` | 链式 `|` 操作符 |
| 手动管理配置 | 自动配置 |
| 难以组合 | 易组合复用 |

### 简单示例

```python
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

prompt = ChatPromptTemplate.from_template("用一句话解释{topic}")
chain = prompt | llm | StrOutputParser()

result = chain.invoke({"topic": "LangChain"})
```

## 安装 LangChain

```bash
pip install langchain langchain-openai langchain-community
```

## 环境变量配置

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```
