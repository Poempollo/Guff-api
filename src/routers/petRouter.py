from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.petSchema import PetCreate, PetResponse
from ..services import petService
from ..db.sessions import get_db
from ..services.authUtils import get_current_user
from ..models.user import User

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)

@router.post("/", response_model=PetResponse)
def create_pet(
    pet: PetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return petService.create_pet(db, pet, current_user)

@router.get("/", response_model=list[PetResponse])
def get_all_pets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return petService.get_user_pets(db, current_user)