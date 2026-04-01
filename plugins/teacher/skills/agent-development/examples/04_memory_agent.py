"""
记忆系统实战 - 带记忆的对话 Agent
"""

from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
    ChatMessageHistory
)

llm = ChatOpenAI(model="gpt-4", temperature=0)

# 定义简单工具
def get_time(*args) -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tools = [Tool(name="get_time", func=get_time, description="获取当前时间")]


# ============== 示例 1: BufferMemory ==============
print("=" * 60)
print("示例 1: ConversationBufferMemory")
print("=" * 60)

memory1 = ConversationBufferMemory(memory_key="chat_history")

agent1 = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory1,
    verbose=False
)

agent1.run("我叫张三，在阿里巴巴工作")
agent1.run("我喜欢机器学习和 Python 编程")
response = agent1.run("你还记得我叫什么名字吗？")
print(f"回答: {response}")

# 查看记忆内容
print(f"\n记忆内容: {memory1.chat_memory.messages}")


# ============== 示例 2: WindowMemory ==============
print("\n" + "=" * 60)
print("示例 2: ConversationBufferWindowMemory (k=2)")
print("=" * 60)

memory2 = ConversationBufferWindowMemory(k=2, memory_key="chat_history")

agent2 = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory2,
    verbose=False
)

agent2.run("第一条消息")
agent2.run("第二条消息")
agent2.run("第三条消息")
agent2.run("第四条消息")

print("只保留最近 2 轮对话")


# ============== 示例 3: SummaryMemory ==============
print("\n" + "=" * 60)
print("示例 3: ConversationSummaryMemory")
print("=" * 60)

memory3 = ConversationSummaryMemory(llm=llm, memory_key="chat_history")

agent3 = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATION_REACT_DESCRIPTION,
    memory=memory3,
    verbose=False
)

# 长对话会被自动摘要
for i in range(5):
    agent3.run(f"这是第 {i+1} 条消息，内容是关于某个技术话题的讨论")

print("长对话已自动摘要，节省 token")


# ============== 示例 4: 持久化 Memory ==============
print("\n" + "=" * 60)
print("示例 4: 持久化记忆")
print("=" * 60)

# 从文件加载历史
import pickle
from pathlib import Path

history = ChatMessageHistory()
try:
    with open("chat_history.pkl", "rb") as f:
        history = pickle.load(f)
except FileNotFoundError:
    pass

memory4 = ConversationBufferMemory(chat_memory=history, memory_key="chat_history")

# ... 进行对话 ...

# 保存到文件
with open("chat_history.pkl", "wb") as f:
    pickle.dump(history, f)

print("记忆已持久化到 chat_history.pkl")
