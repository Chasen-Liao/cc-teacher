# Chains 链式调用

## 什么是 Chain？

Chain 将多个组件串联起来，形成处理流水线。简单理解为：**输入 → 处理1 → 处理2 → ... → 输出**

## LCEL 语法

LangChain Expression Language 用 `|` 串联组件：

```python
prompt | llm | output_parser
```

## 常见 Chain 类型

### 1. LLMChain

最基础的 Chain，结合 Prompt 和 LLM：

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="为 {product} 写一句广告语"
)

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(product="手机")
```

### 2. SimpleSequentialChain

顺序执行的 Chain，上一个输出作为下一个输入：

```python
from langchain.chains import SimpleSequentialChain

# Chain 1: 生成公司名
chain1 = LLMChain(llm=llm, prompt=company_name_prompt)

# Chain 2: 基于公司名生成 slogan
chain2 = LLMChain(llm=llm, prompt=slogan_prompt)

overall = SimpleSequentialChain(chains=[chain1, chain2])
result = overall.run("AI写作工具")
```

### 3. SequentialChain

多输入多输出的顺序 Chain：

```python
from langchain.chains import SequentialChain

chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["input"],
    output_variables=["final_output"]
)
```

### 4. RouterChain

根据输入动态选择子 Chain：

```python
from langchain.chains import RouterChain
from langchain.prompts import PromptTemplate

# 定义多个子 Chain
math_chain = LLMChain(llm=llm, prompt=math_prompt)
history_chain = LLMChain(llm=llm, prompt=history_prompt)

# 路由选择
router_chain = RouterChain(
    default_chain=general_chain,
    route_selector=...
)
```

## TransformationChain

数据转换：

```python
from langchain.chains import TransformationChain

def transform_func(inputs):
    return {"output": inputs["input"].upper()}

chain = TransformationChain(
    input_variables=["input"],
    output_variables=["output"],
    transform_func=transform_func
)
```

## Chain 与 Agent 的区别

| 特性 | Chain | Agent |
|-----|-------|-------|
| 执行方式 | 固定流程 | 动态决策 |
| 工具调用 | 手动 | 自动 |
| 循环控制 | 无 | 有 |
| 适用场景 | 确定性任务 | 开放性任务 |

## 组合使用

```python
# Chain 预处理输入
preprocessing_chain = LLMChain(llm=llm, prompt=preprocess_prompt)

# Agent 执行核心任务
agent = initialize_agent(tools, llm, ...)

# Chain 后处理输出
postprocessing_chain = LLMChain(llm=llm, prompt=postprocess_prompt)

# 组合
full_pipeline = preprocessing_chain | agent | postprocessing_chain
```
