from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, JSON
from sqlalchemy.orm import relationship
from ..db.sessions import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)  # perro, gato, conejo, etc.
    breed = Column(String, nullable=True)     # raza
    gender = Column(String, nullable=False)   # macho, hembra
    birth_date = Column(Date, nullable=False)
    vaccinations = Column(JSON, nullable=True)  # [{nombre: vacunaX, fecha: 2024-05-01}, ...] se usa JSON para almacenar las vacunas y así ser más flexibles.
    next_vaccines = Column(JSON, nullable=True) # [{nombre: vacunaX, fecha: 2025-05-01}, ...]
    distance_walked_km = Column(Float, default=0.0)
    photo_url = Column(String, nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("USer", backref="pets")