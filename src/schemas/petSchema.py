from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class Vaccination(BaseModel):
    name: str
    date: date

class PetCreate(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    gender: str
    birth_date: date
    vaccinations: Optional[List[Vaccination]] = []
    next_vaccines: Optional[List[Vaccination]] = []
    photo_url: Optional[str] = None

class PetResponse(PetCreate):
    id: int
    owner_id: int
    distance_walked_km: float = 0.0

    class Config:
        from_attributes = True # o orm_mode = True si es pydantic v1