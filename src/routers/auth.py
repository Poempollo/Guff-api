from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.userSchema import UserCreate, UserLogin
from ..services import userService
from ..db.sessions import SessionLocal
from ..schemas.resetSchema import ResetPasswordRequest
from ..services.authUtils import get_current_user, create_access_token
from ..models.user import User
from ..services.deps import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user.email = user.email.lower()
        user.username = user.username.lower()

        new_user = userService.register_user(db, user)
        access_token = create_access_token(data={"sub": new_user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException as http_error:
        raise HTTPException(
            status_code=http_error.status_code,
            detail=http_error.detail
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al registrar usuario: {str(e)}"
        )


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return userService.login_user(db, user)

@router.post("/forgot-password")
async def forgot_password(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return await userService.send_reset_email(db, request.email)

@router.delete("/delete-account")
def delete_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return userService.delete_user(db, current_user)
