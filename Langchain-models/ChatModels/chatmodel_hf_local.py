from pathlib import Path
import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


def load_hf_token() -> str:
    """Load HF token from a .env file (searching parents) or environment.

    Supports keys: HF_TOKEN or HF_ACCESS_TOKEN.
    """
    current = Path(__file__).resolve()
    for parent in [current.parent, *current.parents]:
        env_file = parent / ".env"
        if not env_file.exists():
            continue

        for line in env_file.read_text().splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue

            key, value = stripped.split("=", 1)
            key = key.strip()
            if key in ("HF_TOKEN", "HF_ACCESS_TOKEN"):
                return value.strip().strip('"').strip("'")

    return os.getenv("HF_TOKEN") or os.getenv("HF_ACCESS_TOKEN") or ""


hf_token = load_hf_token()
if not hf_token:
    raise RuntimeError("HF token not found in .env or environment (HF_TOKEN or HF_ACCESS_TOKEN)")

# Ensure Hugging Face libraries see the token for authenticated downloads
os.environ.setdefault("HF_TOKEN", hf_token)
os.environ.setdefault("HUGGINGFACE_HUB_TOKEN", hf_token)

# Optional: put models/cache under project .cache/huggingface
project_cache = Path(__file__).resolve().parent.parent / ".cache" / "huggingface"
project_cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("HF_HOME", str(project_cache))
os.environ.setdefault("TRANSFORMERS_CACHE", str(project_cache))


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
    ),
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is a mango")
print(result.content)