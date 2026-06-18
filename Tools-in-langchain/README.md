# LangChain Built-in Tools

This directory explores the variety of pre-defined tools available in LangChain that allow models to interact with the external world. It demonstrates how to integrate web search, shell execution, and Python REPL as tools for Large Language Models. By binding these tools, the agent gains dynamic access to real-time information and computational capabilities.

## What We Learned

### 1. Web Search Integration
- Using `DuckDuckGoSearchRun` to provide models with real-time access to the internet.
- Configuring and invoking search tools to retrieve current information (e.g., sports results).

### 2. System Interaction
- Implementing the `ShellTool` to allow controlled execution of shell commands.
- Exploring `PythonREPLTool` for dynamic code execution and calculation.

### 3. Tool Metadata
- Understanding tool attributes such as `name`, `description`, and `args` which are crucial for the LLM to understand how to use them.

## Key Files
- `tools-in-langchain.ipynb`: Demonstrates the usage of built-in tools like DuckDuckGo search and the shell interaction tool.
