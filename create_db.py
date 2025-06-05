from src.db.sessions import engine, Base

import src.models.reminder

#Creamos todas las tablas registradas
Base.metadata.create_all(bind=engine)