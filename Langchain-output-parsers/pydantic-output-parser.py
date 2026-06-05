from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()
token = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3n-E4B-it",
    huggingfacehub_api_token=token,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description="Name of the city to which the person belongs to")

parser = PydanticOutputParser(pydantic_object = Person)
template = PromptTemplate(
    template = 'Generate the name, age and city of a fictional {place} person \n  {format_instructions}',
    input_variables = ['place'],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
)

# prompt = template.invoke({'place': 'indian'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser
result = chain.invoke({'place': 'indian'})
print(result)