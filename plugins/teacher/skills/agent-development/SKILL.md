# Agent Development with LangChain v1.x

## 课程概述

本课程教授使用 LangChain v1.x 构建 AI Agent 应用。从基础概念到实战项目，帮助你掌握现代 AI 应用开发的核心技能。

## 课程大纲

### Module 1: LangChain 基础
- LangChain 核心概念与架构
- LangChain Expression Language (LCEL)
- Model I/O、Retrieval、Chains、Agents、Memory、Callbacks

### Module 2: Agent 核心
- ReAct 模式 (Reasoning + Acting)
- Tool Calling Agent 原理
- Agent 与 Tool 的交互流程
- 内置 Agent 类型对比

### Module 3: 工具系统 (Tools)
- 内置工具：Wikipedia、SerpAPI、Calculator
- 自定义 Tool 开发（@tool + BaseTool）
- Tool 输入验证与 Pydantic
- 多工具协作

### Module 4: 记忆系统 (Memory)
- ConversationBufferMemory
- ConversationBufferWindowMemory
- ConversationSummaryMemory
- VectorStoreRetrieverMemory
- 记忆持久化

### Module 5: Chains 链式调用
- LLMChain 基础
- SimpleSequentialChain
- SequentialChain
- RouterChain
- Chain 与 Agent 组合

### Module 6: RAG 检索增强生成
- RAG 架构与原理
- 文档加载与分割
- 向量数据库 (Chroma)
- RetrievalQA Chain
- RAG Agent

### Module 7: 实战项目
- 自主研究 Agent
- 对话式问答 Agent
- 多工具协作系统
- RAG 知识库问答

## 课程文件

```
skills/agent-development/
├── SKILL.md                    # 本文件
├── concepts/
│   ├── 01_langchain_basics.md  # LangChain 基础
│   ├── 02_agent_core.md        # Agent 核心
│   ├── 03_memory.md            # Memory 记忆
│   ├── 04_tools.md             # Tools 工具
│   ├── 05_chains.md            # Chains 链式
│   └── 06_rag.md               # RAG 检索
├── examples/
│   ├── 01_hello_agent.py       # Hello World Agent
│   ├── 02_research_agent.py    # 研究 Agent
│   ├── 03_custom_tool.py       # 自定义工具
│   ├── 04_memory_agent.py      # 记忆 Agent
│   └── 05_rag_agent.py         # RAG Agent
└── quizzes/
    ├── quiz1.md                # 基础测验
    └── quiz2.md                # 实战测验
```

## 学习路径

```
第1天 → Module 1-2: 理解 LangChain 和 Agent 核心概念
第2天 → Module 3-4: 掌握 Tools 和 Memory
第3天 → Module 5-6: Chains 和 RAG
第4天 → Module 7: 实战项目
```

## 前置要求

- Python 基础（变量、函数、类）
- 了解 API 调用基本概念
- (建议) 有一个 OpenAI API Key

## 环境安装

```bash
pip install langchain langchain-openai langchain-community
pip install chromadb  # 向量数据库
pip install pydantic   # 数据验证
```

## 参考资源

- [LangChain 官方文档](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LCEL 教程](https://python.langchain.com/docs/expression_language/)
