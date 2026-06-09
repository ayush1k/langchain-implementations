# pip install -U langchain-community pypdf
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()
print(docs[1].page_content)