from langchain_huggingface import HuggingFaceEmbeddings
 
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text = 'My name is ayush'
# vector = embedding.embed_query(text)

documents = [
    'Delhi is the capital of india',
    'Kolkata is the capital of west bengal',
    'and my name is ayush'
]
vector = embedding.embed_documents(documents)


print(str(vector))