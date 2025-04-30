from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.userSchema import UserCreate, UserLogin
from .authUtils import create_user, verify_password, create_access_token
from ..models.user import User
from sqlalchemy import func

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
