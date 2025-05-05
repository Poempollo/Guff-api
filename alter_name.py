from sqlalchemy import text
from src.db.sessions import SessionLocal

def drop_column_name():
    db = SessionLocal()
    try:
        # Ejecuta la consulta para eliminar la columna 'name' de la tabla 'users'
        db.execute(text("ALTER TABLE users DROP COLUMN IF EXISTS name;"))
        db.commit()
        print("Columna 'name' eliminada correctamente")
    except Exception as e:
        print("Error al eliminar la columna:", e)
    finally:
        db.close()

if __name__ == "__main__":
    drop_column_name()
