# LangChain Retrievers

This directory explores advanced retrieval techniques in LangChain. It demonstrates how to fetch relevant documents from various sources and optimize them for LLM context using diversity, multi-querying, and compression.

## What We Learned

### 1. Vector Store Retrievers
- Converting a `Chroma` or `FAISS` vector store into a retriever using `as_retriever()`.
- Configuring retrieval parameters like `k` (number of documents) and `search_type`.

### 2. Diverse and Optimized Retrieval
- **Maximal Marginal Relevance (MMR)**: Balancing relevance and diversity in search results to avoid redundant information.
- **Multi-Query Retriever**: Using an LLM to generate multiple versions of a user query to improve retrieval accuracy from different perspectives.

### 3. Contextual Compression
- **LLMChainExtractor**: Using an LLM to "compress" retrieved documents, extracting only the parts relevant to the query to save tokens and reduce noise.
- **ContextualCompressionRetriever**: Wrapping a base retriever with a compressor to automate the optimization process.

### 4. Third-Party Retrievers
- **WikipediaRetriever**: Directly fetching and processing information from Wikipedia.

## Key Files
- `retriever.ipynb`: A comprehensive notebook demonstrating all retrieval strategies, from basic vector search to advanced compression.
