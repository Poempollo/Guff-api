from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.reminder import Reminder
from ..models.pet import Pet
from ..models.user import User
from ..schemas.reminderSchema import ReminderCreate, ReminderBase, ReminderResponse, ReminderUpdate
from datetime import date
from sqlalchemy import and_

# Crear un recordatorio
def create_reminder(db: Session, reminder_data: ReminderCreate, current_user: User) -> Reminder:
    pet = db.query(Pet).filter(Pet.id == reminder_data.pet_id, Pet.owner_id == current_user.id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found or not owned by user")
    
    reminder = Reminder(
        type=reminder_data.type,
        start_date=reminder_data.start_date,
        finish_date=reminder_data.finish_date,
        text=reminder_data.text,
        pet_id=reminder_data.pet_id
    )

    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder

# Obtener los recordatorios de un usuario
def get_reminders_for_user(db: Session, current_user: User):
    return db.query(Reminder).join(Pet).filter(Pet.owner_id == current_user.id).all()

# Obtener todos los recordatorios de una mascota
def get_reminders_for_pet(db: Session, pet_id: int, current_user: User):
    pet = db.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == current_user.id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found or not owned by user")
    return db.query(Reminder).filter(Reminder.pet_id == pet_id).all()

# Obtener todos los recordatorios por ID
def get_reminder_by_id(db: Session, reminder_id: int, current_user: User):
    reminder = db.query(Reminder).join(Pet).filter(Reminder.id == reminder_id, Pet.owner_id == current_user.id).first()
    if not reminder:
        raise HTTPException(status_code=404, detail="Pet not found or not authorized")
    return reminder

# Actualizar un recordatorio
def update_reminder(db: Session, reminder_id: int, reminder_data: ReminderUpdate, current_user: User):
    reminder = get_reminder_by_id(db, reminder_id, current_user)

    reminder.type = reminder_data.type
    reminder.start_date = reminder_data.start_date
    reminder.finish_date = reminder_data.finish_date
    reminder.text = reminder_data.text

    db.commit()
    db.refresh(reminder)
    return reminder

# Eliminar un recordatorio
def delete_reminder(db: Session, reminder_id: int, current_user: User):
    reminder = get_reminder_by_id(db, reminder_id, current_user)
    db.delete(reminder)
    db.commit()
    return {"message": "Reminder deleted succesfully"}

def get_future_reminders(db: Session, current_user: User):
    today = date.today()
    return db.query(Reminder).join(Pet).filter(
        Pet.owner_id == current_user.id,
        Reminder.start_date > today
    ).order_by(Reminder.start_date.asc()).all()

def get_active_reminders(db: Session, current_user: User):
    today = date.today()
    return db.query(Reminder).join(Pet).filter(
        Pet.owner_id == current_user.id,
        and_(
            Reminder.start_date <= today,
            Reminder.finish_date >= today
        )
    ).order_by(Reminder.start_date.asc()).all()

def get_past_reminders(db: Session, current_user: User):
    today = date.today()
    return db.query(Reminder).join(Pet).filter(
        Pet.owner_id == current_user.id,
        Reminder.finish_date < today
    ).order_by(Reminder.finish_date.desc()).all()