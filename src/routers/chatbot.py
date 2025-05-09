from fastapi import APIRouter, HTTPException, status
from ..schemas.chatbotSchema import ChatMessage, ChatResponse
from ..services.chatbotService import get_chatbot_response
from typing import List
import httpx

router = APIRouter()

@router.post("/chatbot", response_model=ChatResponse)
async def chat_with_bot(messages: List[ChatMessage]):
    # Validación: Asegurarse de que los mensajes no están vacíos
    if not messages:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se recibieron mensajes para procesar"
        )
    
    # Validación adicional: Asegurarse de que todos los mensajes tienen el contenido
    for message in messages:
        if not message.content.strip():  # Check if content is not empty
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El mensaje con rol {message.role} tiene contenido vacío"
            )
    
    try:
        content = await get_chatbot_response(messages)
        return ChatResponse(role="assistant", content=content)
    except httpx.HTTPStatusError as e:
        # Manejo específico de error de HTTP
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Error al contactar con el servicio del chatbot: {str(e)}"
        )
    except Exception as e:
        # Error genérico
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )
