# LangChain Tool Calling

This directory demonstrates how to define custom tools and enable Large Language Models to interact with external functions. It focuses on the seamless integration between Google Gemini and LangChain's tool calling capabilities.

## What We Learned

### 1. Defining Custom Tools
- Using the `@tool` decorator to convert standard Python functions into LangChain-compatible tools.
- Importance of detailed docstrings and type hints for model understanding of tool functionality and arguments.

### 2. Binding Tools to Models
- Using `.bind_tools()` to inform the LLM about available functions.
- Understanding how models decide when to invoke a tool versus generating text.

### 3. Tool Execution Flow
- Invoking tools manually using `.invoke()`.
- Managing the communication loop between the LLM and the tool execution environment.

## Key Files
- `tool-calling.ipynb`: Demonstrates creating a custom multiplication tool and binding it to a Google Gemini model.
