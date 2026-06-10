# LangChain Text Splitters

This directory demonstrates various techniques for breaking down long documents into smaller, manageable chunks. Proper text splitting is crucial for fitting content into LLM context windows and improving retrieval performance.

## What We Learned

### 1. Character-Based Splitting
- **CharacterTextSplitter**: Splitting text based on a specific character or separator.
- **RecursiveCharacterTextSplitter**: The recommended approach that tries to keep related text (like paragraphs and sentences) together by splitting on multiple characters recursively.

### 2. Language-Specific Splitting
- **Code Splitting**: Using `from_language` to split source code (e.g., Python) or structured text (e.g., Markdown) according to its native syntax rules.

### 3. Semantic Splitting
- **SemanticChunker**: An experimental approach that uses embeddings to determine "meaningful" breakpoints between sentences, ensuring chunks are conceptually coherent.

### 4. Splitting Strategies
- **Chunk Size & Overlap**: Tuning these parameters to ensure context is preserved across chunk boundaries.
- **Document Splitting**: Splitting LangChain `Document` objects while preserving their metadata.

## Key Files
- `recursive-text-splitter.py`: Demonstrates the standard recursive splitting method.
- `markdown-splitter.py`: Shows how to split Markdown files while respecting headers.
- `python-code-splitter.py`: Illustrates splitting Python code based on classes and functions.
- `length_based.py`: Demonstrates basic character-based splitting on PDF documents.
- `semantic_chunker.py`: Explores embedding-based semantic chunking.
