from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_hf_token() -> str:
    # Try common names for the Hugging Face token
    # The .env file in this project uses HF_ACCESS_TOKEN
    return os.getenv("HF_ACCESS_TOKEN") or os.getenv("HF_TOKEN") or ""

def main():
    # Model ID to use
    # Mistral-7B-v0.1 is used here as it's highly available on the Inference API
    model_id = "mistralai/Mistral-7B-v0.1"
    
    hf_token = get_hf_token()
    
    if not hf_token:
        print("Error: HF_ACCESS_TOKEN was not found in .env or the environment.")
        return

    try:
        # Initialize the Hugging Face Endpoint
        # This uses the modern routing system and handles authentication automatically
        llm = HuggingFaceEndpoint(
            repo_id=model_id,
            huggingfacehub_api_token=hf_token,
            temperature=0.7,
            max_new_tokens=100,
        )

        print(f"Connecting to Hugging Face model: {model_id}...")
        
        # Invoke the model
        prompt = "What is the capital of India?"
        result = llm.invoke(prompt)
        
        print(f"\nPrompt: {prompt}")
        print(f"Model Response:\n{result}")
        
    except Exception as e:
        print(f"Failed to access Hugging Face API: {e}")
        print("\nSuggestions:")
        print("1. Check if the model ID is correct and publicly available.")
        print("2. Ensure your token has 'read' access.")
        print("3. If you get a 503 error, the model is likely loading. Try again in 2-3 minutes.")

if __name__ == "__main__":
    main()
