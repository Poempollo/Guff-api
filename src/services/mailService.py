from fastapi_mail import MessageSchema
from pydantic import EmailStr
from .mailConfig import fast_mail

async def send_reset_password_email(email: EmailStr, reset_link: str):
    message = MessageSchema(
        subject="Restablece tu contraseña",
        recipients=[email],
        body=f"""
        <h2>Hola, </h2>
        <p>Has solicitado restablecer tu contraseña.</p>
        <p>Haz click en el siguiente enlace para cambiarla:</p>
        <a href="{reset_link}">Restablecer contraseña</a>
        <br><br>
        <p>Si no solicitaste esto, ignora este mensaje.</p>
        """,
        subtype="html"
    )
    
    try:
        await fast_mail.send_message(message)

    except Exception as e:
        print("ERROR EN ENVÍO DE CORREO: ", str(e))
        raise