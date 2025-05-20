# Changelog

### [v0.5.6] - 2025-05-20 - Javier 
#### Fixed
- Arreglado un problema con las relaciones entre usuario y mascota.

### [v0.5.5] - 2025-05-20 - Javier 
#### Fixed
- Arreglado el enrutamiento de los endpoints de las mascotas, que daban error 404.

### [v0.5.4] - 2025-05-20 - Javier 
#### Fixed
- Arreglado un problema de imports circulares con las clases del chatbor. Moviendo sus constantes a config/.

### [v0.5.3] - 2025-05-20 - Javier 
#### Added
- Añadidos los endpoints para obtener una mascota, actualizarla o eliminarla.
#### Improved
- Mejorada la estructura, modularidad y legibilidad de chatbot.py y sus endpoints.

### [v0.5.2] - 2025-05-20 - Javier 
#### Added
- Añadidos los endpoints para crear, y obtener las mascotas de un usuario.

### [v0.5.1] - 2025-05-20 - Javier 
#### Added
- Añadida la lógica de funcionamiento de las mascotas en PetService.py. Crear, devolver, actualizar, eliminar y calcular la edad.

### [v0.5] - 2025-05-20 - Javier 
#### Added
- Añadida la estructura básica para las mascotas.
- Clase pet.py que define un objeto de tipo pet (mascota) con todos sus atributos.
- Clase petSchema.py que define la estructura que segirán y el uso con los objetos pet.

### [v0.4.5] - 2025-05-09 - Javier 
#### Improved
- Mejorada la estructura en las clases del chatbot, sus respuestas y peticiones.
#### Fixed
- Instaladas las dependencias para cargar la KEY de la api desde el .env, funcional en local ya.

### [v0.4.5] - 2025-05-09 - Javier 
#### Improved
- Cambiada la respuesta esperada por la api con respecto a una petición. Ahora recibe un ojeto en lugar de una lista, mejor a largo plazo para futuras actualizaciones.

### [v0.4.4] - 2025-05-09 - Javier 
#### Fixed
- Se seguía llamando mal en el main al método del chatbot.

### [v0.4.3] - 2025-05-09 - Javier 
#### Fixed
- Se llamaba mal en el main al método del chatbot.

### [v0.4.2] - 2025-05-09 - Javier 
#### Fixed
- Arregladas varias clases del chatbot, comprobaciones faltantes.

### [v0.4.1] - 2025-05-09 - Javier 
#### Fixed
- Arregladas varias clases del chatbot, comprobaciones faltantes.

### [v0.4] - 2025-05-09 - Javier 
#### Added
- Añadido el funcionamiento de la api para trabajar con la IA, funcionalidad limitada, posibles fallos.

### [v0.3.4] - 2025-05-07 - Javier 
#### Fixed
- Ahora devolvemos un único token tanto par el login como para el registro.
- Arreglado un problema de encriptación con las dependencias en requirement.txt y railway.

### [v0.3.3] - 2025-05-07 - Javier 
#### Fixed
- Ya si que si que devuelve el token correctamente.

### [v0.3.2] - 2025-05-07 - Javier 
#### Fixed
- Ahora, al registrar un usuario, también devuelve un token para la sesión.

### [v0.3.1] - 2025-05-07 - Javier 
#### Fixed
- Arreglado en requirements.txt con psycop no binario que FALLAAAAAAAAAAAAAAAAAAA.

### [v0.3.1] - 2025-05-07 - Javier 
#### Added
- AÑADIDO EL REQUIREMENTS.TXT.

### [v0.3] - 2025-05-07 - Javier 
#### Added
- Añadida las funciones que eliminan un usuario de la bd.
- Añadidad un archivo deps.py que incluye la funcionalidad de obtener el token de usuario de la sesión.

### [v0.2.17] - 2025-05-05 - Javier 
#### Deleted
- Eliminadas las referencias a "name" en la API, para no trabajar con ese campo más.

### [v0.2.16] - 2025-05-05 - Javier 
#### Fixed
- Pequeño error en el inicio que rompía el CORS. Se trataba de hacer un .lower() a username, campo que no aparece en el login, dando el error.

### [v0.2.15] - 2025-05-02 - Javier 
#### Fixed
- Logs para tratar de debuguear problemas con el envío de correos.

### [v0.2.14] - 2025-05-02 - Javier 
#### Fixed
- Algún día dejará desplegar, por ahora solo tiramos poco a poco.

### [v0.2.13] - 2025-05-02 - Javier 
#### Fixed
- Solucionado OTRO problema más con el despliegue en Railway por configuraciones erróneas.

### [v0.2.12] - 2025-05-02 - Javier 
#### Fixed
- Solucionado un problema con la verificación de correos en mailConfig con emailStr. FastAPI ya lo hace automáticamente.

### [v0.2.11] - 2025-05-02 - Javier 
#### Fixed
- Arreglado un fallo al intentar desplegar psycop2, este debe aparecer como psycop2-binary en el Requirements.txt. IMPORTANTE ESTOOOOOO.

### [v0.2.10] - 2025-05-02 - Javier 
#### Fixed
- Añadidas al requirements.txt las nuevas dependencias instaladas para el correo.

### [v0.2.9] - 2025-05-02 - Javier 
#### Added
- Añadida parte de la funcionalidad de recuperación de contraseñas. Actualmente tan sólo tenemos el envío del correo al usuario con el mensaje, y botón que le llevará a la página donde de verdad se hará el cambio. Por tanto, básicamente falta la página con el formulario de restablecimiento de contraseña, y la parte de la api con la que conecta y se encarga de modificar la BD.

### [v0.2.8] - 2025-04-30 - Javier 
#### Fixed
- Modificado el userService.py y el auth para que tanto el usuario, como el correo electrónico se guarden y manejen siempre en minúscula.
#### Added
- Añadido el create_indexes.py, que hace que la BD gestione siempre los correos y usuarios en minúscula.

### [v0.2.7] - 2025-04-30 - Javier 
#### Fixed
- Modificado el userService.py para que el registro de usuario compruebe la existencia de correo y usuario, y devuelva ambos errores si necesario.

### [v0.2.6] - 2025-04-30 - Javier 
#### Added
- Añadido un archivo GuiaAPI.md con información relevante sobre como trabajamos la api para modificarla y crear nuevos componentes.

### [v0.2.5] - 2025-04-30 - Javier 
#### Added
- Añadido el endpoint para el inicio de sesión, tan sólo recibe el email, y la contraseña.

### [v0.2.4] - 2025-04-29 - Javier 
#### Fixed
- Arreglados más problemas con el despliegue en Railway, solucionado un problema de puertos en el main.py.

### [v0.2.3] - 2025-04-29 - Javier 
#### Fixed
- Arreglado un problema con la dependencia psycopg2 que no reconocía Railway, ahora se usa su plataforma binaria: psycopg2-binary.

### [v0.2.2] - 2025-04-29 - Javier 
#### Added
- Requirements.txt para conseguir que Railway sepa que dependencias debe descargar en el servidor

### [v0.2.1] - 2025-04-29 - Javier 
#### Security
- Añadido un archivo .gitignore para algunos archivos críticos.
#### Added
- Nueva licencia
- Readme mejorado

## Minor Update
### [v0.2] - 2025-04-29 - Javier 
#### Added
- Creados los archivos .env, create_db.py, database.py, sessions.py y user.py.
- Creada la tabla "users" en el servidor remoto.
- Archivos de autenticación de credenciales, y revisión de usuarios.
- Probado con Postman, API funcional en local, despliegue en la nube próximamente.

### [v0.1.2] - 2025-04-29 - Javier 
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

### [v0.1.1] - 2025-04-29 - Javier 
#### Added
- Cambios en main.py para que ahora tengamos un endpoint que recibe un id y un token y devuelve que lo ha obtenido. ENTORNO DE PRUEBAS.

### [v0.1] - 2025-04-28 - Javier 
#### Added
- Configuración inicial, archivo readme, changelog, python, y un main.py que conecta a la API en un servidor remoto: http://127.0.0.1:8000