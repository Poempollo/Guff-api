# Python
- Información útil sobre la instalación y funcionamiento de Python para trabajar con la API.

## FastAPI
### Crear entorno virtual
- Iniciar entorno virtual: 
    python -m venv venv

- Activar el entorno virtual:
    .\venv\scripts\activate

- Aparece (venv) justo al lado de la ruta en el cmd.
- Instalar todas las dependencias:
    pip install -r requirements.txt

- FastAPI el framework para hacer la API, y Uvicorn el servidor que la corre

- Para lanzar el servidor:
    uvicorn main:app --reload

- Rutas para Swagger y ReDoc:
    ruta generada por el servidor /docs o /redoc

- Para parar el servidor, sobre el mismo terminal:
    ctrl + c

- Para lanzar el servidor de pruebas en local:
    uvicorn main:app --host 192.xxx.xxx.xxx --port 8000 --reload

- Vemos la información que devuelve, un JSON

- Para evitar errores con fastapi, instalamos todas sus dependencias:
    pip install fastapi[all]

- Para poder manegar la API, necesitamos las siguientes dependencias:
    pip install sqlalchemy passlib[bcrypt] databases pydantic

- Para poder conectar la api a PostgreSQL instalamos la siguiente dependencia:
    pip install psycopg2

- Para instalar las librerías JWT que gestionan la autenticación, para contraseñas seguras etc:
    pip install passlib[bcrypt] pyjwt

- Para generar y manejar las claves cifradas, instalamos las siguientes dependencias:
    pip install python-dotenv

- CADA VEZ QUE SE INSTALA UN NUEVA DEPENDENCIA HAY QUE HACER ESTO:
    Para crear las dependencias que descargará railway en el proyecto:
        pip freeze > requirements.txt
    
    ADEMÁS, SIEMPRE CAMBIAR psycop2 a psycop2-binary RAILWAY NO RECONOCE AL PRIMERO