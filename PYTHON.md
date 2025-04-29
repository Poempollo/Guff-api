# Python
Información útil sobre la instalación y funcionamiento de Python para trabajar con la API.

## FastAPI
### Crear entorno virtual
- Iniciar entorno virtual: 
python -m venv venv

- Activar el entorno virtual:
.\venv\scripts\activate

- Aparece (venv) justo al lado de la ruta en el cmd.
- Instalar FastAPI:
pip install fastapi uvicorn

- FastAPI el framework para hacer la API, y Uvicorn el servidor que la corre

- Para lanzar el servidor:
uvicorn main:app --reload

- Para parar el servidor, sobre el mismo terminal:
ctrl + c

- Vemos la información que devuelve, un JSON