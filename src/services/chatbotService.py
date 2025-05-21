import httpx
import os
from dotenv import load_dotenv
load_dotenv()
from ..schemas.chatbotSchema import ChatMessage
from ..config.chatbotConfig import SYSTEM_PROMPT, DEFAULT_MODEL

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def build_payload(messages: list[ChatMessage], model: str = DEFAULT_MODEL):
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *[msg.dict() for msg in messages]
        ]
    }

# Solo cambia la firma y cómo se pasa el prompt
async def get_chatbot_response(messages: list[ChatMessage], model: str, system_prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        raise Exception("Api Key no cargada")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            *[msg.dict() for msg in messages]
        ]
    }

    async with httpx.AsyncClient() as client:
        print("HEADERS QUE SE ENVIAN --->", headers)
        res = await client.post(API_URL, json=payload, headers=headers)

    if res.status_code != 200:
        print("OpenRouter error:", res.status_code, res.text)
        raise Exception(f"Error al contactar con OpenRouter: {res.status_code} - {res.text}")

    data = res.json()
    content = data.get("choices", [{}])[0].get("message", {}).get("content", "")

    if not isinstance(content, str):
        raise ValueError("La respuesta del chatbot no es un string válido")

    return content
