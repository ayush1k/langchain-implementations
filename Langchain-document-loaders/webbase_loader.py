# pip install langchain_community beautifulsoup4
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader('https://dev.to/thecodingcutie/unlocking-web-data-with-langchain-a-deep-dive-into-web-loaders-4e6l')
docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)
