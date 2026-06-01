# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
# from dotenv import load_dotenv
# import os
# from langchain_core.prompts import PromptTemplate
#
# load_dotenv()
# token = os.getenv("HF_ACCESS_TOKEN")
#
# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.3",
#     huggingfacehub_api_token=token,
#     task="text-generation",
# )
#
#
# template1 = PromptTemplate(
#     template="Write a detailed report on {topic}",
#     input_variables=["topic"],
# )
#
# template2 = PromptTemplate(
#     template="Write a 5 line summary on the following text\n{text}",
#     input_variables=["text"],
# )
#
# prompt1 = template1.format(topic="black hole")
# result = llm.invoke(prompt1)
#
# prompt2 = template2.format(text=result)
# result1 = llm.invoke(prompt2)
#
# print(result1)

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()
token = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=token,
    task="conversational",
    max_new_tokens=256,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text\n{text}",
    input_variables=["text"],
)

prompt1 = template1.format(topic="black hole")
result = model.invoke(prompt1)

# print("Detailed report:\n", result.content)

prompt2 = template2.format(text=result.content)
result1 = model.invoke(prompt2)

print(result1.content)


