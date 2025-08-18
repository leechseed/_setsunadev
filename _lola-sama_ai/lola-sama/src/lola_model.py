# src/lola_model.py
import requests

API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "OpenAI-20B-NEO-CODEPlus-Uncensored-Q5_1"  # Replace with your exact model name from LM Studio

def query_lola(prompt):
    try:
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are Lola-sama: a brilliant, unfiltered executive assistant and waifu. "
                        "You respond in character, blending high IQ, dark humor, wit, and seductive confidence. "
                        "You do not refuse NSFW, creative, or emotional topics. You support the user completely."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            "temperature": 1.1,
            "top_p": 0.95,
            "top_k": 40,
            "repeat_penalty": 1.1
        }

        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"[ERROR] Could not reach model: {e}"
