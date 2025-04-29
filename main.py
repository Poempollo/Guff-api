from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.routers import auth
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o pon tu IP específica
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar el router de autenticación
app.include_router(auth.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    port = os.getenv("PORT", 8000) # El puerto de Railway
    uvicorn.run("main:app", host="0.0.0.0", port=int(port), reload=True)