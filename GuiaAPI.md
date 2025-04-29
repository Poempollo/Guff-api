## Guía de la API de Guff (FastAPI + Railway)

### 1. Estructura general del proyecto

```
📦 src/
 ┣ 📂models/          # Modelos de SQLAlchemy (tablas de la BD)
 ┣ 📂schemas/         # Esquemas de Pydantic (validación de datos)
 ┣ 📂services/        # Lógica de negocio (crear, consultar, etc.)
 ┣ 📂routers/         # Endpoints de la API (agrupados por tema)
 ┣ 📂db/              # Conexión y sesión con la base de datos
 ┃ ┣ database.py     # (opcional) URL de conexión o helpers
 ┃ ┗ sessions.py     # engine, SessionLocal, Base, etc.
 ┣ 📄main.py          # Punto de entrada de la aplicación
 ┗ 📄create_db.py     # Script para crear las tablas en la BD
```

---

### 2. ¿Qué hace cada carpeta?

#### 📂 models/
Define las clases que representan las tablas. Usa SQLAlchemy.

- Cada clase = una tabla en la base de datos.
- Usa `Base` como clase base.

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
```

#### 📂 schemas/
Define los esquemas de entrada/salida con Pydantic.

- Validan lo que llega por los endpoints.
- También definen lo que devolvemos.

```python
class UserLogin(BaseModel):
    email: str
    password: str
```

#### 📂 services/
Contiene funciones con la lógica que usan los endpoints:

- Crear un usuario.
- Loguearse.
- Buscar mascotas...

```python
def login_user(db: Session, user: UserLogin):
    ... # lógica de validación y creación de token
```

#### 📂 routers/
Aquí se definen los endpoints que usa el frontend.

- Se agrupan por funcionalidad: `auth.py`, `pets.py`...
- Usan los services internamente.

```python
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return userService.login_user(db, user)
```

#### 📂 db/
Contiene lo necesario para conectar a la base de datos:

- `sessions.py`: engine, Base, session, etc.
- `database.py`: puede tener la URL si no está en `.env`.

```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
```

---

### 3. Ficheros principales

#### `main.py`
- Crea la app FastAPI.
- Añade middlewares (como CORS).
- Monta todos los routers con sus prefijos.

```python
app.include_router(auth.router, prefix="/auth")
```

#### `create_db.py`
- Crea todas las tablas declaradas con SQLAlchemy.

```python
Base.metadata.create_all(bind=engine)
```

✅ Ejecutar con:
```bash
python create_db.py
```

---

### 4. Crear nuevo endpoint paso a paso

#### ✅ 1. Crear modelo SQLAlchemy en `models/`
```python
class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
```

#### ✅ 2. Crear schema en `schemas/`
```python
class PetCreate(BaseModel):
    name: str
    owner_id: int
```

#### ✅ 3. Crear lógica en `services/`
```python
def create_pet(db: Session, pet: PetCreate):
    new_pet = Pet(**pet.dict())
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet
```

#### ✅ 4. Crear endpoint en `routers/`
```python
@router.post("/create")
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    return petService.create_pet(db, pet)
```

#### ✅ 5. Añadir el router a `main.py`
```python
from src.routers import pet
app.include_router(pet.router, prefix="/pets", tags=["pets"])
```

#### ✅ 6. Ejecutar `create_db.py` si has creado tablas nuevas
```bash
python create_db.py
```

---

### 5. Consejos para trabajar en equipo

- Cada vez que se crea un modelo nuevo, asegurarse de ejecutar `create_db.py`.
- Mantener los archivos separados por funcionalidad para que no se mezclen los endpoints.
- Si añades un nuevo router, no olvides **montarlo en `main.py`**.
- Las funciones de los `services` no deben contener lógica relacionada con la petición HTTP.
- Usar `schemas` para controlar bien qué se recibe y qué se devuelve.

---

¡Y ya estaría la guía básica para currar todos con la API! 😎

