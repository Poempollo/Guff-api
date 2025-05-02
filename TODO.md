# To do

## [2025-05-02] - Contraseña olvidada - Javier
### Done
- Envío de correo de recuperación:
    Ruta: POST /auth/forgot-password
    Usa FastAPI Mail con Gmail para enviar el email.
    Lógica implementada en userService.send_reset_email().

- Plantilla HTML básica con enlace de recuperación incluida en el email.

### To do
- 1. Crear una pantalla web (frontend) para restablecer la contraseña
    Una web sencilla con un formulario:
        Inputs: nueva contraseña + repetir contraseña.
        Botón: "Cambiar contraseña".
        Validaciones básicas de frontend.
    Esta web se abrirá desde el enlace enviado en el correo:
    https://guff-api-production.up.railway.app/auth/reset-password?email=usuario@gmail.com

- 2. Ruta en el backend para cambiar la contraseña
    Crear una nueva ruta en FastAPI, por ejemplo:

    @router.post("/reset-password")
    def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
        Recibe: email y nueva contraseña.
        Lógica:
            Buscar al usuario por email.
            Hashear la nueva contraseña.
            Guardarla en la BD.

- 3. Esquema Pydantic para el cambio de contraseña
    class ResetPasswordRequest(BaseModel):
        email: EmailStr
        new_password: str

- 4. Actualizar la contraseña en la BD
    En userService.py, una nueva función tipo:

    def update_user_password(db: Session, email: str, new_password: str)
        Verifica si el usuario existe.
        Hashea la nueva contraseña.
        Guarda el cambio.

- 5. Mejoras opcionales para producción (más adelante)
    Enviar token único en el enlace, no solo el email (más seguro).
    Expirar tokens a los 15-30 minutos.
    Logs de envío de correos para control interno.