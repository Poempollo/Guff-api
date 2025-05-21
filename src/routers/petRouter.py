from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.petSchema import PetCreate, PetResponse, VaccinationAdd
from ..services import petService
from ..services.deps import get_db
from ..services.authUtils import get_current_user
from ..models.user import User

router = APIRouter()

@router.post("/", response_model=PetResponse)
def create_pet(pet: PetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return petService.create_pet(db, pet, current_user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear mascota: {str(e)}"
        )

@router.get("/all")
def get_user_pets(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return petService.get_user_pets(db, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener mascotas: {str(e)}"
        )

@router.get("/{pet_id}")
def get_pet(pet_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return petService.get_pet_by_id(db, pet_id, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener la mascota: {str(e)}"
        )

@router.put("/{pet_id}")
def get_pet(pet_id: int, pet: PetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return petService.update_pet(db, pet_id, pet, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar la mascota: {str(e)}"
        ) 
    
@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return petService.delete_pet(db, pet_id, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar la mascota: {str(e)}"
        )

@router.post("/{pet_id}/vaccines")
def add_vaccine(pet_id: int, vaccine: VaccinationAdd, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return petService.add_vaccine_to_pet(db, pet_id, vaccine, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al añadir vacuna: {str(e)}"
        )
