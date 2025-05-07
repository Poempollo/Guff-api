from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.userSchema import UserCreate, UserLogin
from .authUtils import create_user, verify_password, create_access_token
from ..models.user import User
from sqlalchemy import func
from .mailService import send_reset_password_email
from fastapi import Depends
from ..services.authUtils import get_current_user

def register_user(db: Session, user: UserCreate):
    errors = {}

    #Verificar si ya está en uso el correo
    if db.query(User).filter(User.email == user.email).first():
        errors["email"] = "Email already registered"
    
    #Verificar si ya está en uso el username
    if db.query(User).filter(User.username == user.username).first():
        errors["username"] = "Username already registered"

    if errors:
        raise HTTPException(status_code=400, detail=errors) 
    
    #Crear un nuevo usuario
    new_user = create_user(db, user)
    return new_user

def login_user(db: Session, user: UserLogin):
    errors = {}

    #Verificar si el usuario existe
    db_user = db.query(User).filter(func.lower(User.email) == user.email.lower()).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        errors["credentials"] = "Invalid email or password"
        raise HTTPException(status_code=400, detail=errors)
    
    #Crear el token JWT
    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

async def send_reset_email(db: Session, email: str):
    user = db.query(User).filter(func.lower(User.email) == email.lower()).first()

    if not user:
        raise HTTPException(status_code=404, detail={"email": "No user found with this email"})
    
    try:
        reset_link = f"https://guff.app/reset-password?email={email}"  # usar el enlace de la petición a la api desde el front
        await send_reset_password_email(email, reset_link)
        return {"message": "Reset password email sent"}
    except Exception as e:
        print("ERROR AL ENVIAR EL EMAIL DESDE userService: ", str(e))
        raise HTTPException(status_code=500, detail="Error sending reset email")

def delete_user(db: Session, current_user: User):
    user = db.query(User).filter(User.id == current_user.id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "Account successfully deleted"}

