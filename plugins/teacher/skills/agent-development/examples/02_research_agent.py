"""
ReAct 研究 Agent - 能够自主研究问题的 Agent
"""

from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(model="gpt-4", temperature=0)

# 定义工具
def search_web(query: str) -> str:
    """搜索网络获取信息"""
    # 实际项目中可接入 SerpAPI、Tavily 等
    return f"[搜索结果] 关于 '{query}' 的信息..."

def read_file(filename: str) -> str:
    """读取本地文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()[:500]  # 限制长度
    except:
        return f"无法读取文件: {filename}"

tools = [
    Tool(name="search", func=search_web, description="搜索网络信息"),
    Tool(name="read_file", func=read_file, description="读取本地文件")
]

# 带 Memory 的研究 Agent
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

if __name__ == "__main__":
    print("=== 研究 Agent 测试 ===\n")
    
    # 多轮对话
    agent.run("我想了解 Python 异步编程")
    print("\n" + "="*50 + "\n")
    agent.run("能给我一个 asyncio 的代码示例吗？")
    print("\n" + "="*50 + "\n")
    agent.run("和 Node.js 的异步有什么不同？")
