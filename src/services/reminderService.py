from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.reminder import Reminder
from ..models.pet import Pet
from ..models.user import User
from ..schemas.reminderSchema import ReminderCreate
from datetime import date

# Crear un recordatorio
def create_reminder(db: Session, reminder_data: ReminderCreate, current_user: User) -> Reminder:
    pet = db.query(Pet).filter(Pet.id == reminder_data.pet_id, Pet.owner_id == current_user.id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found or not owned by user")

    reminder = Reminder(
        type=reminder_data.type,
        title=reminder_data.title,
        start_date=reminder_data.start_date,
        finish_date=reminder_data.finish_date,
        text=reminder_data.text,
        pet_id=reminder_data.pet_id
    )

    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder

# Eliminar un recordatorio
def delete_reminder(db: Session, reminder_id: int, current_user: User):
    reminder = db.query(Reminder).join(Pet).filter(Reminder.id == reminder_id, Pet.owner_id == current_user.id).first()
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found or not authorized")
    db.delete(reminder)
    db.commit()
    return {"message": "Reminder deleted successfully"}

# Obtener TODOS los recordatorios futuros del usuario
def get_future_reminders(db: Session, current_user: User):
    today = date.today()
    return db.query(Reminder).join(Pet).filter(
        Pet.owner_id == current_user.id,
        Reminder.start_date > today
    ).order_by(Reminder.start_date.asc()).all()
