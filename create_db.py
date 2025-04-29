from src.db.sessions import engine, Base
import src.db.database

#Creamos todas las tablas registradas
Base.metadata.create_all(bind=engine)