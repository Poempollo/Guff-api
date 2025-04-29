# Changelog

### [v0.0.2.2] - 2025-04-29 - Javier 
#### Added
- Requirements.txt para conseguir que Railway sepa que dependencias debe descargar en el servidor

### [v0.0.2.1] - 2025-04-29 - Javier 
#### Security
- Añadido un archivo .gitignore para algunos archivos críticos.
#### Added
- Nueva licencia
- Readme mejorado

## Minor Update
### [v0.0.2] - 2025-04-29 - Javier 
#### Added
- Creados los archivos .env, create_db.py, database.py, sessions.py y user.py.
- Creada la tabla "users" en el servidor remoto.
- Archivos de autenticación de credenciales, y revisión de usuarios.
- Probado con Postman, API funcional en local, despliegue en la nube próximamente.

### [v0.0.1.2] - 2025-04-29 - Javier 
#### Added
- Añadida la estructura de carpetas para la api.
- controllers/
- db/
- models/
- routers/
- services/
- Cada carpeta tiene un archivo .py con información adicional.
#### Fixed
- añadido el manejo de los CORS a main.py para evitar errores.

### [v0.0.1.1] - 2025-04-29 - Javier 
#### Added
- Cambios en main.py para que ahora tengamos un endpoint que recibe un id y un token y devuelve que lo ha obtenido. ENTORNO DE PRUEBAS.

### [v0.0.1] - 2025-04-28 - Javier 
#### Added
- Configuración inicial, archivo readme, changelog, python, y un main.py que conecta a la API en un servidor remoto: http://127.0.0.1:8000