from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
token = os.getenv("HF_ACCESS_TOKEN")

def word_length(text):
    return len(text.split())

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3n-E4B-it",
    huggingfacehub_api_token=token,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding = 'utf-8')
docs = loader.load()
# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)
# print(docs[0].metadata)

prompt = PromptTemplate(
    template = 'Write a summary for the following poem - \n {poem}',
    input_variables = ['poem']
)

chain = prompt | model | parser
result = chain.invoke({'poem':docs[0].page_content})
print(result)