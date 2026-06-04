from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()
token = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3n-E4B-it",
    huggingfacehub_api_token=token,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a frictional character \n {format_instructions}',
    input_variables=[],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)
# print(type(final_result))
# print(final_result['name'])
# print(final_result['age'])
# print(final_result['city'])


chain = template | model | parser
result = chain.invoke({})
print(result)
