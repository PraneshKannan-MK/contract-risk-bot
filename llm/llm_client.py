import requests
from config.settings import FEATURES

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:1b"


def call_llama(prompt: str) -> str:
    # If LLM is disabled, exit cleanly
    if not FEATURES.get("enable_llm_explanations", False):
        return "LLM explanations are disabled in this environment."

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=20
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception:
        return "LLM service unavailable."