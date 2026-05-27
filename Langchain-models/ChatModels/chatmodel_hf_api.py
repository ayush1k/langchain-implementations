from pathlib import Path
import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def load_hf_token() -> str:
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
            if key.strip() == "HF_TOKEN":
                return value.strip().strip('"').strip("'")

    return os.getenv("HF_TOKEN", "")


model_id = "TinyLlama/TinyLlama-1.1B-step-50K-105b"
prompt = "What is the capital of India?"
hf_token = load_hf_token()

if not hf_token:
    raise RuntimeError("HF_TOKEN was not found in .env or the environment.")

url = f"https://api-inference.huggingface.co/models/{model_id}"
payload = json.dumps(
    {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.95,
            "return_full_text": False,
        },
    }
).encode("utf-8")

request = Request(
    url,
    data=payload,
    headers={
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))
except HTTPError as error:
    error_body = error.read().decode("utf-8")
    raise RuntimeError(f"HF API request failed ({error.code}): {error_body}") from error

if isinstance(result, list) and result and "generated_text" in result[0]:
    print(result[0]["generated_text"])
else:
    print(result)