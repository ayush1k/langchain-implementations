# LangChain Models

This directory contains implementations and experiments with various types of models supported by LangChain, focusing on Chat Models, Embedding Models, and Large Language Models (LLMs).

## What We Learned

### 1. Model Integrations & Providers
- **Google Gemini**: Integration using `langchain_google_genai`. Primarily used `gemini-1.5-flash` for high-speed chat and generation.
- **HuggingFace**: 
    - **Inference API**: Using `HuggingFaceEndpoint` for cloud-hosted models.
    - **Local Execution**: Using `HuggingFacePipeline` and `ChatHuggingFace` to run models locally on hardware (CPU/GPU).

### 2. Model Paradigms
- **Chat Models**: Message-based interaction using `ChatGoogleGenerativeAI`. Learned to manage conversational flow with System and Human messages.
- **LLMs (Completion)**: Using `GoogleGenerativeAI` for traditional text completion tasks.

### 3. Embedding Models & Semantic Search
- **Vector Embeddings**: Converting text into high-dimensional vectors using `GoogleGenerativeAIEmbeddings`.
- **Semantic Search**: Implementing a basic RAG (Retrieval-Augmented Generation) pattern.
    - **Cosine Similarity**: Calculating the "distance" between query embeddings and document embeddings to find relevant content.
- **Local Embeddings**: Using `HuggingFaceEmbeddings` to generate vectors without external API calls.

### 4. Configuration & Environment
- Using `python-dotenv` for secure credential management.
- Handling rate limits and API specific configurations (like `temperature` and `max_tokens`).

## Folder Structure
- **ChatModels/**:
    - `chatmodel-gemini.py`: Google Gemini chat interface.
    - `chatmodel_hf_api.py`: HuggingFace cloud API integration.
    - `chatmodel_hf_local.py`: Local model execution example.
- **EmbeddingModels/**:
    - `embedding_query.py`: Single text embedding generation.
    - `embedding_docs.py`: Batch processing of documents.
    - `document_similarity.py`: Full semantic search workflow.
- **LLMs/**:
    - `LLMDemo.py`: Basic LLM completion demonstration.
