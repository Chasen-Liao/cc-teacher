"""
RAG 实战 - 检索增强生成 Agent
"""

from langchain_openai import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.agents import AgentType, initialize_agent, Tool

llm = ChatOpenAI(model="gpt-4", temperature=0)
embeddings = OpenAIEmbeddings()


# ============== Step 1: 准备知识库 ==============
print("=" * 60)
print("Step 1: 准备知识库")
print("=" * 60)

# 模拟文档（实际项目中从文件/网页加载）
documents = [
    "LangChain 是一个用于构建 LLM 应用的框架。",
    "LangChain 的核心组件包括：Model、Prompt、Chain、Agent、Memory、Tool。",
    "Agent 是 LangChain 中能够自主决策和执行动作的智能体。",
    "Tools 让 Agent 能够与外部世界交互，如搜索、API调用等。",
    "Memory 为 Agent 提供跨对话的记忆能力。",
    "Chain 将多个组件串联成处理流水线。"
]

# 分割文档
splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
docs = splitter.create_documents(documents)

print(f"分割成 {len(docs)} 个文档块")


# ============== Step 2: 创建向量库 ==============
print("\n" + "=" * 60)
print("Step 2: 创建向量库")
print("=" * 60)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"  # 持久化
)
print("向量库已创建")


# ============== Step 3: RAG Chain ==============
print("\n" + "=" * 60)
print("Step 3: RAG问答 Chain")
print("=" * 60)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

questions = [
    "LangChain 的核心组件有哪些？",
    "什么是 Agent？",
    "如何使用 Memory？"
]

for q in questions:
    print(f"\n问题: {q}")
    result = qa_chain({"query": q})
    print(f"答案: {result['result']}")


# ============== Step 4: RAG Agent ==============
print("\n" + "=" * 60)
print("Step 4: RAG Agent（可自主检索）")
print("=" * 60)

# 创建 RAG Tool
def rag_query(query: str) -> str:
    """从知识库检索相关信息"""
    result = qa_chain({"query": query})
    return result["result"]

rag_tool = Tool(
    name="knowledge_base",
    func=rag_query,
    description="当需要回答关于 LangChain 框架的问题时使用此工具"
)

agent = initialize_agent(
    tools=[rag_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("\nAgent 自主回答问题:")
agent.run("LangChain 的六大核心组件是什么？")
