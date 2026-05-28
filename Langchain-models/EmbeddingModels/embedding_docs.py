from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", output_dimensionality=32)

documents = [
    'Delhi is the capital of india',
    'Kolkata is the capital of west bengal',
    'and my name is ayush'
]

result = embeddings.embed_documents(documents)

print(str(result))