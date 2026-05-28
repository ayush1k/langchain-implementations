# LangChain Models

This directory contains implementations and experiments with various types of models supported by LangChain, focusing on Chat Models, Embedding Models, and Large Language Models (LLMs).

## What We Learned

### 1. Model Integrations
- **Google Gemini**: Integration using `langchain_google_genai` for both chat and embedding tasks.
- **HuggingFace**: Using `langchain_huggingface` to connect to models via the Inference API (`HuggingFaceEndpoint`) and running models locally.

### 2. Chat Models vs. LLMs
- **Chat Models**: Learned to use `ChatGoogleGenerativeAI` for interactive, message-based conversations.
- **LLMs**: Basic invocation for completion tasks using `HuggingFaceEndpoint` and `GoogleGenerativeAI`.

### 3. Embedding Models & Semantic Search
- **Embedding Generation**: Using `GoogleGenerativeAIEmbeddings` and local HuggingFace models to convert text into numerical vectors.
- **Document Similarity**: Implementing a basic RAG-like (Retrieval-Augmented Generation) flow by calculating **Cosine Similarity** between query embeddings and document embeddings to find the most relevant information.
- **Batch Processing**: Differences between `embed_query` (single text) and `embed_documents` (multiple texts).

### 4. Configuration & Security
- Utilizing `python-dotenv` to manage API keys (e.g., `GOOGLE_API_KEY`, `HF_ACCESS_TOKEN`) securely.

## Folder Structure
- `ChatModels/`: Scripts for HF API, HF Local, and Gemini chat interfaces.
- `EmbeddingModels/`: Examples of query embedding, document similarity, and local embedding usage.
- `LLMs/`: Basic LLM demonstrations.
