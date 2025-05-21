from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from ..models.pet import Pet
from ..schemas.petSchema import PetCreate, VaccinationAdd, PetResponse
from ..models.user import User
from fastapi import HTTPException
from datetime import datetime

def create_pet(db: Session, pet_data: PetCreate, current_user: User) -> Pet:
    new_pet = Pet(
        name=pet_data.name,
        species=pet_data.species,
        breed=pet_data.breed,
        gender=pet_data.gender,
        birth_date=pet_data.birth_date,
        vaccinations=[
            {**v.model_dump(), "date": v.date.isoformat()} for v in pet_data.vaccinations
        ],
        next_vaccines=[
            {**v.model_dump(), "date": v.date.isoformat()} for v in pet_data.next_vaccines
        ],
        photo_url=pet_data.photo_url,
        owner_id=current_user.id,
        distance_walked_km=0.0
    )
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet

def get_user_pets(db: Session, current_user: User):
    return db.query(Pet).filter(Pet.owner_id == current_user.id).all()

def get_pet_by_id(db: Session, pet_id: int, current_user: User):
    pet = db.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == current_user.id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

def update_pet(db: Session, pet_id: int, pet_data: PetCreate, current_user: User):
    pet = get_pet_by_id(db, pet_id, current_user)

    pet.name = pet_data.name
    pet.species = pet_data.species
    pet.breed = pet_data.breed
    pet.gender = pet_data.gender
    pet.birth_date = pet_data.birth_date
    pet.vaccinations=[
            {**v.model_dump(), "date": v.date.isoformat()} for v in pet_data.vaccinations
        ],
    pet.next_vaccines=[
            {**v.model_dump(), "date": v.date.isoformat()} for v in pet_data.next_vaccines
        ],
    pet.photo_url = pet_data.photo_url

    db.commit()
    db.refresh(pet)
    return pet

def add_vaccine_to_pet(db: Session, pet_id: int, vaccine: VaccinationAdd, current_user: User):
    pet = get_pet_by_id(db, pet_id, current_user)
    
    # Asegura que la lista existe
    if not pet.vaccinations:
        pet.vaccinations = []

    # Añadir nueva vacuna
    pet.vaccinations.append({
        "name": vaccine.name,
        "date": vaccine.date.isoformat()
    })

    db.commit()
    db.refresh(pet)
    return pet


def delete_pet(db: Session, pet_id: int, current_user: User):
    pet = get_pet_by_id(db, pet_id, current_user)
    db.delete(pet)
    db.commit()
    return {"message": "Pet deleted succesfully"}

def calculate_age(birth_date):
    today = datetime.today().date()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def pet_to_response(pet: Pet) -> PetResponse:
    birth_date = pet.birth_date
    age = calculate_age(birth_date)

    return PetResponse(
        id=pet.id,
        owner_id=pet.owner_id,
        name=pet.name,
        species=pet.species,
        breed=pet.breed,
        gender=pet.gender,
        birth_date=pet.birth_date,
        vaccinations=pet.vaccinations,
        next_vaccines=pet.next_vaccines,
        photo_url=pet.photo_url,
        distance_walked_km=pet.distance_walked_km,
        age=age
    )

def pets_to_response(pets: list[Pet]) -> list[PetResponse]:
    return [pet_to_response(pet) for pet in pets]
