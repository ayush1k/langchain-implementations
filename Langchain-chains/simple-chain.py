from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
token = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3n-E4B-it",
    huggingfacehub_api_token=token,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about the {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()
chain = prompt | model | parser 
result = chain.invoke({'topic','Lamborghini'})
print(result)

chain.get_graph().print_ascii() # to print the structure of the chain