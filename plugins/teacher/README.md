# Teacher Plugin

交互式教学插件，通过「概念解释 → 代码示例 → 随堂测验」的教学模式帮助学生学习各种学科。

## 功能

- `/teacher <学科>` - 开始学习某个学科
- Agent 具备 MCP 工具：context7（查文档）、WebSearch（搜索）、Read（读文件）
- 教学模式：解释概念 → 代码示例 → 随堂测验
- 可扩展的 skills 目录，每个学科一个子目录

## 插件结构

```
plugins/teacher/
├── .claude-plugin/plugin.json
├── commands/teacher.md
├── agents/teacher-agent.md
├── skills/
│   └── programming-basics/  # 示例学科
│       ├── SKILL.md
│       ├── concepts/
│       ├── examples/
│       └── quizzes/
└── README.md
```

## 添加新学科

在 `skills/` 目录下创建新的学科文件夹，例如 `python/`：

```
skills/python/
├── SKILL.md          # 学科概述和课程大纲
├── concepts/         # 概念详解
├── examples/         # 代码示例
└── quizzes/          # 测验题
```

## 使用方法

1. 安装插件（将 `plugins/teacher` 目录放入 Claude Code 插件目录）
2. 运行 `/teacher <学科>` 开始学习
3. 按照教学流程：概念 → 示例 → 测验
