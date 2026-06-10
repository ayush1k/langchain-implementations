# LangChain Vector Stores

This directory focuses on managing and querying vector databases, which are essential for semantic search and Retrieval-Augmented Generation (RAG). It primarily explores the use of ChromaDB for high-performance vector storage.

## What We Learned

### 1. Vector Database Integration
- **ChromaDB**: Setting up and using Chroma as a local vector database.
- **Persistence**: Using `persist_directory` to save embeddings to disk, allowing data to persist across sessions.

### 2. Document Management
- **Adding Documents**: Converting LangChain `Document` objects into vectors and storing them in collections.
- **Metadata Handling**: Storing and retrieving metadata alongside document content for filtered searches.
- **CRUD Operations**: Implementing updates and deletions of documents within the vector store.

### 3. Semantic Search Patterns
- **Similarity Search**: Basic retrieval of documents based on vector distance.
- **Similarity Search with Score**: Obtaining confidence scores to measure the relevance of retrieved content.

## Key Files
- `chromadb.ipynb`: A detailed guide covering the entire lifecycle of a Chroma collection, including creation, querying, and management.
- `my_chroma_db/`: Local directory where the persistent Chroma database is stored.
