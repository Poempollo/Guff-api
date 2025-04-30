# Changelog

### [v0.0.2.8] - 2025-04-30 - Javier 
#### Fixed
- Modificado el userService.py y el auth para que tanto el usuario, como el correo electrónico se guarden y manejen siempre en minúscula.
#### Added
- Añadido el create_indexes.py, que hace que la BD gestione siempre los correos y usuarios en minúscula.

### [v0.0.2.7] - 2025-04-30 - Javier 
#### Fixed
- Modificado el userService.py para que el registro de usuario compruebe la existencia de correo y usuario, y devuelva ambos errores si necesario.

### [v0.0.2.6] - 2025-04-30 - Javier 
#### Added
- Añadido un archivo GuiaAPI.md con información relevante sobre como trabajamos la api para modificarla y crear nuevos componentes.

### [v0.0.2.5] - 2025-04-30 - Javier 
#### Added
- Añadido el endpoint para el inicio de sesión, tan sólo recibe el email, y la contraseña.

### [v0.0.2.4] - 2025-04-29 - Javier 
#### Fixed
- Arreglados más problemas con el despliegue en Railway, solucionado un problema de puertos en el main.py.

### [v0.0.2.3] - 2025-04-29 - Javier 
#### Fixed
- Arreglado un problema con la dependencia psycopg2 que no reconocía Railway, ahora se usa su plataforma binaria: psycopg2-binary.

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