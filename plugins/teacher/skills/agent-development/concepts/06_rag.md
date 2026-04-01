# RAG 检索增强生成

## 为什么需要 RAG？

LLM 的局限：
- 知识有截止日期
- 无法访问私有数据
- 可能产生幻觉（胡编乱造）

RAG 解决方案：**先检索，后生成**

```
用户问题 ──▶ 检索相关文档 ──▶ 将文档注入 Prompt ──▶ LLM 生成答案
```

## RAG 核心组件

```
                  ┌─────────────┐
                  │   Document  │
                  │   Loading  │
                  └──────┬──────┘
                         ▼
                  ┌─────────────┐
                  │  Splitting  │
                  └──────┬──────┘
                         ▼
                  ┌─────────────┐
                  │ Embedding   │──▶ Vector Store
                  │   Creation  │
                  └──────┬──────┘
                         ▼
                  ┌─────────────┐
                  │  Retrieval  │◀── Query
                  └──────┬──────┘
                         ▼
                  ┌─────────────┐
                  │ Generation  │──▶ Answer
                  └─────────────┘
```

## LangChain 实现

### Step 1: 文档加载

```python
from langchain.document_loaders import WebPageLoader, PDFLoader, DirectoryLoader

# 加载网页
loader = WebPageLoader(web_path="https://example.com/article")
docs = loader.load()

# 加载 PDF
loader = PDFLoader(file_path="document.pdf")

# 加载目录
loader = DirectoryLoader(path="./documents", glob="*.txt")
```

### Step 2: 文档分割

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # 每段500字符
    chunk_overlap=50      # 段间重叠50字符
)

splits = splitter.split_documents(docs)
```

### Step 3: 向量化存储

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="./vectorstore"  # 持久化
)
```

### Step 4: 检索

```python
# 相似度检索
results = vectorstore.similarity_search(query="LangChain是什么", k=3)

# 带分数的检索
results = vectorstore.similarity_search_with_score(query, k=3)
```

### Step 5: 生成

```python
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # 将检索内容塞入 prompt
    retriever=vectorstore.as_retriever()
)

result = qa_chain.run("LangChain 的核心组件有哪些？")
```

## Chain Types

| 类型 | 特点 | 适用场景 |
|-----|------|---------|
| stuff | 所有文档塞入一个 prompt | 少量文档 |
| map_reduce | 每个文档单独处理后汇总 | 大量文档 |
| refine | 逐个优化答案 | 需要精确答案 |
| map_rerank | 每个文档打分选最佳 | 需要最佳匹配 |

```python
# map_reduce 模式
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="map_reduce",
    retriever=vectorstore.as_retriever()
)
```

## RAG Agent

结合 RAG 和 Agent，实现自主检索：

```python
from langchain.agents import AgentType, initialize_agent

# RAG 作为 Tool
rag_tool = Tool(
    name="knowledge_base",
    func=vectorstore.as_retriever().get_relevant_documents,
    description="从知识库检索相关信息"
)

agent = initialize_agent(
    tools=[rag_tool, search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)
```

## 高级 RAG

### 查询改写

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

rewrite_prompt = PromptTemplate(
    template="将这个问题改写得更清晰: {question}",
    input_variables=["question"]
)

rewrite_chain = LLMChain(llm=llm, prompt=rewrite_prompt)
rewritten_query = rewrite_chain.run(question=user_question)
```

### 混合检索

```python
# 关键词 + 向量检索结合
from langchain.retrievers import EnsembleRetriever

retriever = EnsembleRetriever(
    retrievers=[keyword_retriever, vector_retriever],
    weights=[0.3, 0.7]
)
```
