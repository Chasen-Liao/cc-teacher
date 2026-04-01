"""
LangChain Hello World - 构建你的第一个 Agent
"""

from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool

# 1. 初始化 LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key="your-api-key"  # 或使用环境变量
)

# 2. 定义工具
def get_current_time(*args) -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate(expression: str) -> str:
    """数学计算器"""
    try:
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {e}"

# 3. 创建工具列表
tools = [
    Tool(
        name="get_time",
        func=get_current_time,
        description="获取当前时间，格式为 YYYY-MM-DD HH:MM:SS"
    ),
    Tool(
        name="calculator",
        func=calculate,
        description="进行数学计算，例如: 15 + 23 * 3"
    )
]

# 4. 初始化 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,  # 显示思考过程
    max_iterations=5
)

# 5. 运行 Agent
if __name__ == "__main__":
    # 测试问题
    questions = [
        "现在几点了？",
        "计算 (100 + 200) / 3",
        "今天日期是什么？顺便帮我算一下 25 * 4"
    ]
    
    for q in questions:
        print(f"\n{'='*50}")
        print(f"问题: {q}")
        print('='*50)
        result = agent.run(q)
        print(f"答案: {result}")
