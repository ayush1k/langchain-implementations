from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='books',
    glob = '*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# print(len(docs))
# print(docs[5].page_content)
# print(docs[5].metadata)

for document in docs:
    print(document.metadata)