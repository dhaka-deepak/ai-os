import requests
import re


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate(prompt: str):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3:8b",

            "prompt": prompt,

            "stream": False,

            # Force JSON mode
            "format": "json",

            "options": {

                "temperature": 0,

                "num_predict": 1024,

                "top_p": 0.9,

                "top_k": 40

            }
        },
        timeout=300
    )

    response.raise_for_status()

    data = response.json()

    answer = data["response"].strip()

    # Remove reasoning if present
    answer = re.sub(
        r"<think>.*?</think>",
        "",
        answer,
        flags=re.DOTALL
    ).strip()

    return answer