# LangChain Document Loaders

This directory demonstrates how to load data from various sources into LangChain's Document format. It covers a range of loaders for text, CSV, PDF, directories, and web content, providing the foundation for any RAG-based application.

## What We Learned

### 1. Standard Document Loaders
- **TextLoader**: Loading raw text files with specific encodings.
- **CSVLoader**: Converting tabular data from CSV files into a list of Documents, where each row becomes a document.
- **PyPDFLoader**: Extracting text content and metadata from PDF files.

### 2. Batch and Directory Loading
- **DirectoryLoader**: Loading multiple files from a folder using glob patterns.
- **Lazy Loading**: Using `lazy_load()` to efficiently process large datasets without loading everything into memory at once.

### 3. Web Scraping
- **WebBaseLoader**: Extracting content from URLs using `beautifulsoup4` for use in LLM pipelines.

## Key Files
- `text_loader.py`: Demonstrates loading text and summarizing it using a HuggingFace model.
- `csv_loader.py`: Shows how to load and print data from CSV files.
- `pypdf_loader.py`: Extracts and prints content from specific pages of a PDF.
- `directory_loader.py`: Demonstrates batch loading of PDF files from a subdirectory.
- `webbase_loader.py`: Shows how to scrape and process content from a web page.
