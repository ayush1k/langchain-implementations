# LangChain Chains

This directory explores various ways to compose LangChain components into functional workflows using the LangChain Expression Language (LCEL). It covers linear sequences, parallel processing, and conditional branching logic.

## What We Learned

### 1. LangChain Expression Language (LCEL)
- Using the pipe operator (`|`) to compose prompts, models, and parsers.
- Visualizing chain structures using `chain.get_graph().print_ascii()`.

### 2. Sequential Chains
- Passing the output of one component as the input to the next.
- Building multi-step reasoning or transformation pipelines.

### 3. Parallel Execution
- Using `RunnableParallel` to execute multiple chains simultaneously.
- Combining results from different models (e.g., HuggingFace and Google Gemini) into a single context.

### 4. Conditional Routing
- Implementing dynamic logic with `RunnableBranch`.
- Using `RunnableLambda` for custom processing logic within a chain.
- Classification-based routing (e.g., sentiment analysis leading to different response strategies).

## Key Files
- `simple-chain.py`: Demonstrates a basic Prompt | Model | Parser sequence.
- `sequential-chain.py`: Shows how to link multiple prompt-model-parser blocks in a series.
- `parallel-chain.py`: Implements concurrent processing using `RunnableParallel`.
- `conditional-chain.py`: Uses `RunnableBranch` to route execution based on sentiment analysis.
