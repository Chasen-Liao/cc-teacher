# cc-teacher

Claude Code 交互式教学插件，专注于 **AI Agent 开发**，使用 **LangChain v1.x** 框架。

## 教学理念

通过「**概念解释 → 代码示例 → 随堂测验**」的教学模式，让学习者：
1. 理解核心概念和原理
2. 掌握实际编码能力
3. 通过测验巩固知识

## 教学方向

| 学科 | 内容 |
|-----|------|
| **Agent 开发** | LangChain、Agent、Tools、Memory、RAG |
| 编程基础 | 变量、控制流、函数、数据结构 |

## 课程内容

### Agent 开发 (LangChain v1.x)

```
Module 1: LangChain 基础
├── 核心概念与架构
├── LCEL 语法
└──六大模块概览

Module 2: Agent 核心
├── ReAct 模式
├── Tool Calling
└── Agent 类型

Module 3: Tools 工具系统
├── 内置工具
├── 自定义 Tool
└── 多工具协作

Module 4: Memory 记忆系统
├── BufferMemory
├── WindowMemory
├── SummaryMemory
└── 向量记忆

Module 5: Chains 链式调用
├── LLMChain
├── SequentialChain
└── RouterChain

Module 6: RAG 检索增强生成
├── 文档处理
├── 向量数据库
└── RAG Agent

Module 7: 实战项目
├── 自主研究 Agent
├── 知识库问答
└── 多 Agent 协作
```

## 插件结构

```
plugins/teacher/
├── .claude-plugin/plugin.json   # 插件元数据
├── commands/teacher.md          # /teacher 命令
├── agents/teacher-agent.md      # Agent 配置
├── skills/
│   ├── agent-development/        # Agent 开发课程
│   │   ├── SKILL.md
│   │   ├── concepts/            # 6 个概念文档
│   │   ├── examples/            # 5 个代码示例
│   │   └── quizzes/             # 2 个测验
│   └── programming-basics/       # 编程基础
└── README.md
```

## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/Chasen-Liao/cc-teacher.git
   ```

2. 安装插件：
   ```bash
   cp -r plugins/teacher ~/.claude/plugins/
   ```

3. 重启 Claude Code

## 使用方法

```bash
# 开始 Agent 开发学习
/teacher agent-development

# 或学习编程基础
/teacher programming-basics
```

## 技术栈

- **框架**: LangChain v1.x
- **Agent**: Claude Sonnet (支持 MCP tools)
- **工具**: context7, WebSearch, Read
- **向量库**: ChromaDB

## 扩展课程

添加新学科只需在 `skills/` 下创建新目录：

```
skills/
├── python/
│   ├── SKILL.md
│   ├── concepts/
│   ├── examples/
│   └── quizzes/
└── agent-development/
    └── ...
```

## License

MIT

## 作者

Chasen - [GitHub](https://github.com/Chasen-Liao)
