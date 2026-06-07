from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough


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
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

# prompt2 = PromptTemplate(
#     template = 'Explain the following joke - {text}',
#     input_variables = ['text']
# )

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count': RunnableLambda(word_length)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
print(final_chain.invoke({'topic':'AI'}))