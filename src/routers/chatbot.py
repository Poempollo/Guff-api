from fastapi import APIRouter, HTTPException, status
from ..schemas.chatbotSchema import ChatMessage, ChatResponse
from ..services.chatbotService import get_chatbot_response
from typing import List
from pydantic import BaseModel
import httpx

router = APIRouter()

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

@router.post("/chatbot", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    messages = request.messages

    if not messages:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se recibieron mensajes para procesar"
        )
    
    for message in messages:
        if not message.content.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El mensaje con rol {message.role} tiene contenido vacío"
            )
    
    try:
        content = await get_chatbot_response(messages)
        return ChatResponse(role="assistant", content=content)
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Error al contactar con el servicio del chatbot: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )
    