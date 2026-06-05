from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()
token = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3n-E4B-it",
    huggingfacehub_api_token=token,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = 'fact1', description = 'Fact1 about the topic'),
    ResponseSchema(name = 'fact2', description = 'Fact2 about the topic'),
    ResponseSchema(name = 'fact3', description = 'Fact3 about the topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instructions}',
    input_variables = ['topic'],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'Black hole'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser
result = chain.invoke({'topic':'Black hole'})
print(result)