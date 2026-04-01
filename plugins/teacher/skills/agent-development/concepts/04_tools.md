# Tools 工具系统

## Tool 的本质

Tool 是 Agent 与外部世界交互的接口。没有 Tools，Agent 只能回答训练数据中的知识；有了 Tools，Agent 可以实时获取信息、执行动作。

```
Agent ──调用──▶ Tool ──执行──▶ 外部世界
     ◀──返回── Result
```

## 内置 Tools

### Wikipedia

```python
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
result = wikipedia.run("Python programming language")
```

### SerpAPI (搜索)

```python
from langchain.utilities import SerpAPIWrapper
import os

os.environ["SERPAPI_API_KEY"] = "your-key"
search = SerpAPIWrapper()
result = search.run("What is LangChain?")
```

### Calculator

```python
from langchain.tools import Calculator

calc = Calculator()
calc.run("sqrt(16) * 2")
```

## 自定义 Tool

### 使用 @tool 装饰器

```python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气情况。
    
    Args:
        city: 城市名称（中文或英文）
    Returns:
        天气描述和温度
    """
    weather_db = {
        "北京": "晴天 25°C",
        "上海": "多云 23°C",
        "东京": "雨天 20°C"
    }
    return weather_db.get(city, f"未找到 {city} 的天气信息")
```

### Tool 输入验证

使用 Pydantic 模型定义严格输入：

```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class WeatherInput(BaseModel):
    city: str = Field(description="城市名称")
    country: str = Field(default="中国", description="国家")

class WeatherTool(BaseTool):
    name = "get_weather"
    description = "获取城市的天气信息"
    args_schema = WeatherInput
    
    def _run(self, city: str, country: str = "中国") -> str:
        # 实现
        return f"{country}{city}：晴天 25°C"
```

## Tool 属性

| 属性 | 说明 |
|-----|------|
| name | 工具唯一标识 |
| description | 描述工具用途（LLM据此选择） |
| args_schema | 输入参数 schema |
| return_direct | 是否直接返回结果 |

## 多工具协作

```python
from langchain.agents import AgentType, initialize_agent

# 组合多个工具
tools = [search, calculator, wikipedia, custom_tool]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Agent 会自动选择合适的工具
agent.run("查一下埃隆·马斯克的年龄，然后计算他出生年份到现在的天数")
```

## Tool 选择的艺术

LLM 根据 description 选择工具。描述要：
- 清晰明确工具用途
- 包含适用场景
- 说明返回格式

```python
# ❌ 模糊
Tool(name="search", func=search, description="搜索")

# ✅ 清晰
Tool(
    name="web_search",
    func=search,
    description="用于搜索网络获取实时信息。当需要查找最新新闻、股价、天气等实时数据时使用。"
)
```
