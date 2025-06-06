from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.routers import auth, chatbot, petRouter, reminderRouter
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar el router de autenticación
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chatbot.router, prefix="", tags=["chatbot"])
app.include_router(petRouter.router, prefix="/pets", tags=["pets"])
app.include_router(reminderRouter.router)

if __name__ == "__main__":
    port = os.getenv("PORT", 8000) # El puerto de Railway
    uvicorn.run("main:app", host="0.0.0.0", port=int(port), reload=True)