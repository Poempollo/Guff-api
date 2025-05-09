import httpx
from ..schemas.chatbotSchema import ChatMessage
from dotenv import load_dotenv
import os

load_dotenv() # carga las variables de entorno desde el .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def get_chatbot_response(messages: list[ChatMessage]) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Referer": "https://tuapp.com",
        "X-Title": "Guff Chatbot"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un asistente amigable que ayuda con dudas veterinarias generales."},
            *[msg.dict() for msg in messages]
        ]
    }

    async with httpx.AsyncClient() as client:
        res = await client.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        if res.status_code != 200:
            print("Error:", res.text)
            raise Exception("Error al contactar con OpenRouter")
        data = res.json()
        return data["choices"][0]["message"]["content"]
