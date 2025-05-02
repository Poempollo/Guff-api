from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.userSchema import UserCreate, UserLogin
from ..services import userService
from ..db.sessions import SessionLocal
from ..schemas.resetSchema import ResetPasswordRequest

router = APIRouter()

#Dependencias para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    user.email = user.email.lower()
    user.username = user.username.lower()
    return userService.register_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    user.email = user.email.lower()
    user.username = user.username.lower()
    return userService.login_user(db, user)

@router.post("/forgot-password")
async def forgot_password(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return await userService.send_reset_email(db, request.email)