from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Setup the model
# Using Mistral-7B as it is free and reliable on the HF Inference API
model_id = "mistralai/Mistral-7B-v0.1"
token = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id=model_id,
    huggingfacehub_api_token=token,
    temperature=0.7,
    max_new_tokens=100
)

# Execute and print results
print(f"Querying {model_id}...")
result = llm.invoke("What is the capital of India?")
print(result)
