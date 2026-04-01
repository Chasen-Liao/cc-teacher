# Agent 核心概念

## 什么是 Agent？

Agent = LLM（大脑）+ Tools（工具）+ Loop（循环）

Agent 能够：
1. **感知** - 接收用户输入和工具返回
2. **思考** - LLM 推理下一步行动
3. **行动** - 调用工具执行动作
4. **循环** - 重复直到任务完成

## Agent 工作流程

```
┌─────────────────────────────────────────────────────┐
│                     User Input                       │
│                         ▼                           │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    │
│  │  LLM     │───▶│  Action  │───▶│  Result  │    │
│  │  Think   │    │  Select  │    │  Return  │    │
│  └──────────┘    └──────────┘    └──────────┘    │
│       │                                    │       │
│       └──────────── Loop ◀─────────────────┘       │
└─────────────────────────────────────────────────────┘
```

## ReAct 模式

ReAct = Reasoning + Acting

让 LLM 显式地：
1. **Thought** - 思考当前情况
2. **Action** - 选择要执行的工具
3. **Observation** - 观察工具返回结果
4. 重复直到得出答案

### 示例对话

```
User: 今天北京的天气如何？

Thought: 用户想知道北京天气，我需要调用天气工具
Action: search_weather
Input: 北京
Observation: 今天北京晴天，25度
Final Answer: 今天北京天气晴朗，气温25度。
```

## Tool Calling Agent

LangChain 内置的工具调用 Agent：

```python
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

tools = [
    Tool(name="calculator", func=lambda x: str(eval(x)), description="数学计算")
]

agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("计算 (15 + 23) * 3 是多少？")
```

## 自定义 Tool

### 方式一：简单函数

```python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """获取城市天气"""
    weather_data = {
        "北京": "晴天 25°C",
        "上海": "雨天 20°C"
    }
    return weather_data.get(city, "未知城市")
```

### 方式二：BaseTool 类

```python
from langchain.tools import BaseTool
from pydantic import BaseModel

class WeatherInput(BaseModel):
    city: str

class WeatherTool(BaseTool):
    name = "get_weather"
    description = "获取指定城市的天气"
    args_schema = WeatherInput
    
    def _run(self, city: str) -> str:
        return f"{city} 今天是晴天，25度"
```

## Agent 类型对比

| 类型 | 特点 | 适用场景 |
|-----|------|---------|
| ZERO_SHOT_REACT_DESCRIPTION | 零样本，描述驱动 | 通用任务 |
| CHAT_ZERO_SHOT_REACT_DESCRIPTION | 对话优化 | 对话场景 |
| CONVERSATION_REACT_DESCRIPTION | 多轮对话 | 有记忆需求 |
| SELF_ASK_WITH_SEARCH | 自我追问 | 复杂推理 |

## 输出解析

Agent 返回需要解析为结构化数据：

```python
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

parser = StructuredOutputParser.from_response_schemas([
    ResponseSchema(name="answer", description="最终答案"),
    ResponseSchema(name="confidence", description="置信度 0-1")
])

chain = prompt | llm | parser
result = chain.invoke({"question": "..."})
```
