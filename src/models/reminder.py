from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..db.sessions import Base
from .pet import Pet

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True, nullable=False)
    start_date = Column(Date, nullable=False)
    finish_date = Column(Date, nullable=True)
    text = Column(String, nullable=True)

    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    pet = relationship(Pet, backref="reminders")