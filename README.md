# LangChain Implementations

This repository is a collection of practical implementations and experiments using the LangChain framework. It serves as a learning journal and a reference for building LLM-powered applications with various models, prompt patterns, and structured output techniques.

## Project Structure

The project is organized into modular directories, each focusing on a specific aspect of the LangChain ecosystem:

- **[LangChain Agents](./Agents-in-langchain/)**: Construction and execution of autonomous agents using the ReAct framework, custom tool bindings, and LangSmith Hub.
- **[LangChain Chains](./Langchain-chains/)**: Exploration of LCEL, sequential chains, parallel processing, and conditional routing logic.
- **[LangChain Document Loaders](./Langchain-document-loaders/)**: Practical use of various loaders for CSV, PDF, Text, and Web content.
- **[LangChain Models](./Langchain-models/)**: Experiments with Chat Models, Embedding Models, and LLMs using Google Gemini and HuggingFace. Covers semantic search and document similarity.
- **[LangChain Output Parsers](./Langchain-output-parsers/)**: Techniques for transforming LLM output into structured data like JSON, Lists, and Pydantic models.
- **[LangChain Prompts](./Langchain-prompts/)**: Exploration of prompt templates, message structuring, conversational memory, and basic Streamlit UIs.
- **[LangChain RAG](./rag-using-langchain/)**: End-to-end implementation of Retrieval-Augmented Generation using YouTube transcripts and FAISS.
- **[LangChain Retrievers](./Langchain-retrievers/)**: Advanced retrieval strategies including Multi-Query, Contextual Compression, and MMR.
- **[LangChain Runnables](./Langchain-runnables/)**: Deep dive into LangChain Expression Language (LCEL) primitives like Sequences, Parallel execution, Lambdas, and Branching.
- **[LangChain Structured Outputs](./Langchain-structured-outputs/)**: Techniques for extracting validated, structured data from LLMs using Pydantic, TypedDict, and JSON schemas.
- **[LangChain Text Splitters](./Langchain-text-splitters/)**: Implementation of various text splitting strategies like Recursive, Markdown, and Semantic chunking.
- **[LangChain Tool Calling](./Tool-calling-in-langchain/)**: Implementing custom tool definitions and binding them to models for function execution.
- **[LangChain Tools](./Tools-in-langchain/)**: Exploration of built-in tools like DuckDuckGo Search and Shell execution for extended capabilities.
- **[LangChain Vector Stores](./Langchain-vector-stores/)**: Integration and management of vector databases, specifically ChromaDB, for efficient similarity search.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayush1k/langchain-implementations.git
   cd langchain-implementations
   ```

2. **Setup Environment:**
   Create a `.env` file in the root directory (and relevant subdirectories) with your API keys:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   HF_ACCESS_TOKEN=your_huggingface_token
   ```

3. **Install Dependencies:**
   Refer to the `setup/` directory or the individual `README.md` files in each folder for specific installation instructions.

## Security Features

- **Gemini Sandbox**: This project supports the `GEMINI_SANDBOX` mode for isolated execution of AI-generated commands. To enable it, set `GEMINI_SANDBOX=true` in your environment or `.env` file.

## Documentation Standard

Each directory contains its own `README.md` following a consistent pattern defined in [readme-creation-prompt.md](./readme-creation-prompt.md).
the prompt was used to generate readme for each directory
                                 
