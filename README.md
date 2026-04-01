# cc-teacher

Claude Code 交互式教学插件，通过「**概念解释 → 代码示例 → 随堂测验**」的教学模式帮助学生学习编程。

## 功能特性

- `/teacher <学科>` - 开启交互式学习会话
- **MCP 工具集成**：context7（查文档）、WebSearch（搜索）、Read（读文件）
- **三段式教学**：概念 → 示例 → 测验
- **可扩展结构**：每个学科一个 skill 目录

## 插件结构

```
plugins/teacher/
├── .claude-plugin/plugin.json   # 插件元数据
├── commands/teacher.md          # /teacher 命令定义
├── agents/teacher-agent.md      # Agent 配置（含 MCP 工具）
├── skills/                      # 学科内容
│   └── programming-basics/       # 示例学科：编程基础
│       ├── SKILL.md              # 课程大纲
│       ├── concepts/             # 概念详解
│       ├── examples/             # 代码示例
│       │   └── variables.py
│       └── quizzes/              # 测验题
│           └── quiz1.md
└── README.md
```

## 安装

1. 克隆此仓库：
   ```bash
   git clone https://github.com/Chasen-Liao/cc-teacher.git
   ```

2. 将 `plugins/teacher` 目录复制到 Claude Code 插件目录：
   ```bash
   cp -r plugins/teacher ~/.claude/plugins/
   ```

3. 重启 Claude Code

## 使用方法

### 启动教学会话

```
/teacher python
/teacher programming-basics
/teacher <任意学科>
```

### 教学流程

1. **概念解释** - 分解核心概念，建立基础理解
2. **代码示例** - 展示实际代码，边学边练
3. **随堂测验** - 测试学习效果，即时反馈

## 添加新学科

在 `plugins/teacher/skills/` 下创建新目录：

```
skills/
├── python/                    # 新学科
│   ├── SKILL.md               # 学科概述和课程大纲
│   ├── concepts/              # 概念详解
│   ├── examples/              # 代码示例
│   └── quizzes/               # 测验题
└── programming-basics/        # 已有学科
    └── ...
```

## 技术栈

- **Agent**: Claude Sonnet
- **工具**: context7 (文档查询), WebSearch (网络搜索), Read (文件读取)
- **模式**: 交互式问答 + 实践练习

## License

MIT

## 作者

Chasen - [GitHub](https://github.com/Chasen-Liao)
