from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableBranch


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

prompt1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Sunnarize the following text \n {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

report_generation_prompt = RunnableSequence(prompt1, model, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300 , RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_generation_prompt, branch_chain)
print(final_chain.invoke({'topic':'Russia vs Ukraine'}))