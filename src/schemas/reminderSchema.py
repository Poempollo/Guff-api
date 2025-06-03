from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReminderBase(BaseModel):
    type: str
    start_date: date
    finish_date: Optional[date] = None
    text: Optional[str] = None

class ReminderCreate(ReminderBase):
    pet_id: int # para crear recordatorio

class ReminderUpdate(ReminderBase):
    pass # para modificar todos los campos

class ReminderResponse(ReminderBase):
    id: int
    pet_id: int

    class config:
        from_attributes = True # Pydantic v2, para mapear desde ORM