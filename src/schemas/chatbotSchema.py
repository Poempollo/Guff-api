from pydantic import BaseModel
from typing import Literal, List, Optional
from ..services.chatbotService import DEFAULT_MODEL, SYSTEM_PROMPT

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatResponse(BaseModel):
    role: Literal["assistant"]
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: Optional[str] = DEFAULT_MODEL
    system_prompt: Optional[str] = SYSTEM_PROMPT
