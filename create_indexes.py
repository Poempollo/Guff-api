from sqlalchemy import text
from src.db.sessions import SessionLocal

def create_unique_indexes():
    db = SessionLocal()
    try:
        db.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS unique_lower_email ON users (LOWER(email));"))
        db.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS unique_lower_username ON users (LOWER(username));"))
        db.commit()
        print("Índices únicos creados correctamente")
    except Exception as e:
        print("Error al crear los índices:", e)
    finally:
        db.close()

if __name__ == "__main__":
    create_unique_indexes()
