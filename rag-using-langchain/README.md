# LangChain RAG (Retrieval-Augmented Generation)

This directory demonstrates the implementation of a RAG system that allows users to chat with the content of YouTube videos. It covers the entire pipeline from data ingestion to retrieval-based generation.

## What We Learned

### 1. Data Ingestion & Processing
- **YouTube Transcripts**: Using `youtube-transcript-api` to programmatically fetch video captions.
- **Text Splitting**: Implementing `RecursiveCharacterTextSplitter` to break long transcripts into manageable, overlapping chunks for better context preservation.

### 2. Vector Stores & Embeddings
- **Semantic Representation**: Using `GoogleGenerativeAIEmbeddings` to convert text chunks into high-dimensional vector embeddings.
- **FAISS (Facebook AI Similarity Search)**: Utilizing FAISS as an efficient in-memory vector database for storing and performing similarity searches on embeddings.

### 3. Retrieval & Generation
- **Contextual Querying**: Searching the vector store for the most relevant transcript segments based on a user's question.
- **Gemini Integration**: Passing retrieved context to the `ChatGoogleGenerativeAI` (Gemini) model to generate grounded and accurate responses.

### 4. Robust Implementation
- **Rate Limit Management**: Implementing manual retries with exponential backoff to handle API limits in free tiers.

## Key Files
- `youtube_chat_rag.ipynb`: A comprehensive notebook demonstrating the full RAG workflow for YouTube video transcripts.
