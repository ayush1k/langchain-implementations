# LangChain Agents

This directory explores how to construct and execute autonomous agents using LangChain. It demonstrates how to combine Large Language Models (LLMs) with tools, prompts, and memory to perform multi-step reasoning and dynamic decision-making.

## What We Learned

### 1. Agent Architecture & Execution
- **ReAct Framework**: Implementing the Reason-and-Act paradigm to guide the agent's problem-solving process.
- **AgentExecutor**: Using the executor to manage the agent loop, handling tool inputs, executing operations, and parsing observations back to the LLM.

### 2. Prompting with LangSmith Hub
- **Dynamic Prompt Retrieval**: Using `Client.pull_prompt` to pull standardized and tested ReAct prompt templates (such as `hwchase17/react-chat`) from the LangSmith Hub.
- **Prompt Structure**: Structuring prompt templates to include tool lists, formatting instructions, and chat history placeholders.

### 3. Custom and Pre-built Tools
- **Pre-built Tools**: Utilizing built-in tools like `DuckDuckGoSearchRun` to provide the agent with real-time web search capabilities.
- **Custom Tools**: Creating custom tools using the `@tool` decorator, detailing tool instructions via docstrings and setting expected arguments with python type hints.

### 4. Interactive Reasoning & Orchestration
- **Sequential Multi-step Queries**: Orchestrating agents to handle complex, multi-hop tasks (e.g., retrieving state capitals and then looking up weather conditions).
- **Graceful Handling of Limitations**: Managing API output constraints and date references safely within agent reasoning blocks.

## Key Files
- `agents_using_langchain.ipynb`: Interactive notebook demonstrating ReAct agent construction, tool binding, and LangSmith Hub integration.
