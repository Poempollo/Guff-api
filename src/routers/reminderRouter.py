from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.reminderSchema import ReminderCreate, ReminderUpdate, ReminderResponse
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

# Obtener todos los recordatorios del usuario
@router.get("/user", response_model=list[ReminderResponse])
def get_user_reminders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_reminders_for_user(db, current_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los recordatorios: {str(e)}")

# Obtener los recordatorios de una mascota
@router.get("/pet/{pet_id}", response_model=list[ReminderResponse])
def get_pet_reminders(pet_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_reminders_for_pet(db, pet_id, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener recordatorios de la mascota: {str(e)}")

# Obtener un recordatorio por ID
@router.get("/{reminder_id}", response_model=ReminderResponse)
def get_reminder(reminder_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_reminder_by_id(db, reminder_id, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el recordatorio: {str(e)}")

# Actualizar un recordatorio
@router.put("/{reminder_id}", response_model=ReminderResponse)
def update_reminder(reminder_id: int, reminder: ReminderUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.update_reminder(db, reminder_id, reminder, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el recordatorio: {str(e)}"
        )

# Eliminar un recordatorio
@router.delete("/{reminder_id}")
def delete_reminder(reminder_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.delete_reminder(db, reminder_id, current_user)
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar el recordatorio: {str(e)}"
        )
    
# Recordatorios futuros
@router.get("/future", response_model=list[ReminderResponse])
def get_future_reminders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_future_reminders(db, current_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener recordatorios futuros: {str(e)}")

# Recordatorios en proceso
@router.get("/active", response_model=list[ReminderResponse])
def get_active_reminders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_active_reminders(db, current_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener recordatorios activos: {str(e)}")

# Recordatorios pasados
@router.get("/past", response_model=list[ReminderResponse])
def get_past_reminders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return reminderService.get_past_reminders(db, current_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener recordatorios pasados: {str(e)}")

