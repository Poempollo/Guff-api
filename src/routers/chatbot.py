from fastapi import APIRouter, HTTPException, status
from ..schemas.chatbotSchema import ChatResponse, ChatRequest
from ..services.chatbotService import get_chatbot_response
import httpx

router = APIRouter()

@router.post("/chatbot", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    if not request.messages:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se recibieron mensajes para procesar"
        )

    for message in request.messages:
        if not message.content.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El mensaje con rol {message.role} tiene contenido vacío"
            )

    try:
        content = await get_chatbot_response(
            messages=request.messages,
            model=request.model,
            system_prompt=request.system_prompt
        )
        return ChatResponse(role="assistant", content=content)

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Error al contactar con el servicio del chatbot: {str(e)}"
        )
    except Exception as e:
        print("ERROR GENERAL:", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )
