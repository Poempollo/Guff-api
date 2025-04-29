from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o pon tu IP específica
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos que va a recibir tu API
class TokenData(BaseModel):
    user_id: int  # o email, o username... lo que uses
    fcm_token: str

# Endpoint para guardar el token
@app.post("/save-token")
def save_token(data: TokenData):
    # Aquí deberías guardarlo en la base de datos, por ahora solo lo imprimimos
    print(f"Token recibido para user {data.user_id}: {data.fcm_token}")
    return {"message": "Token guardado correctamente"}
