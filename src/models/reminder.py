from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.sessions import Base
from .pet import Pet

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=True)

    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    petReminder = relationship(Pet, backref="users")