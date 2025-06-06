from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.reminderSchema import ReminderCreate, ReminderResponse
from ..services import reminderService
from ..services.deps import get_db
from ..services.authUtils import get_current_user
from ..models.user import User

router = APIRouter(prefix="/reminders", tags=["Reminders"])

# Crear un recordatorio
@router.post("", response_model=ReminderResponse)
def create_reminder(reminder: ReminderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.create_reminder(db, reminder, current_user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear el recordatorio: {str(e)}"
        )

# Eliminar un recordatorio
@router.delete("/{reminder_id}")
def delete_reminder(reminder_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.delete_reminder(db, reminder_id, current_user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar el recordatorio: {str(e)}"
        )

# Obtener todos los recordatorios futuros del usuario (ordenados por fecha)
@router.get("/future", response_model=list[ReminderResponse])
def get_future_reminders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_future_reminders(db, current_user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener recordatorios futuros: {str(e)}"
        )
