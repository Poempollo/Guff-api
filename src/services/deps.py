from ..db.sessions import SessionLocal
from sqlalchemy.orm import Session

#Dependencias para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
