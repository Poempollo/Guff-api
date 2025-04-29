from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.userSchema import UserCreate, UserLogin
from .authUtils import create_user, verify_password, create_access_token
from ..models.user import User

def register_user(db: Session, user: UserCreate):
    #Verificar si ya existe el usuario
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #Crear un nuevo usuario
    new_user = create_user(db, user)
    return new_user

def login_user(db: Session, user: UserLogin):
    #Verificar si el usuario existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    #Crear el token JWT
    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}