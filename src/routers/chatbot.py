from fastapi import APIRouter, HTTPException
from schemas.chatbot import ChatMessage, ChatResponse
from services.chatbot_service import get_chatbot_response

router = APIRouter()

@router.post("/chatbot", response_model=ChatResponse)
async def chat_with_bot(messages: list[ChatMessage]):
    try:
        content = await get_chatbot_response(messages)
        return ChatResponse(role="assistant", content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
