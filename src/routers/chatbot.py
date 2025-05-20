from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schemas.chatbotSchema import ChatMessage, ChatResponse, ChatRequest
from ..services.chatbotService import get_chatbot_response
from ..services.deps import get_db
from ..services.authUtils import get_current_user
from ..models.user import User
import httpx

router = APIRouter()

@router.post("/send")
async def chat_with_bot(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
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
        return {"role": "assistant", "content": content}

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
