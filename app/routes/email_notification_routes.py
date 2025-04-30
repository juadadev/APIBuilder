from fastapi import APIRouter, Depends

from app.schemas.email_request import EmailRequest, EmailResponse
from app.services.email_notification_service import EmailNotificationService

email_router = APIRouter()

@email_router.post("/notifications/email", response_model=EmailResponse)
async def create_email_notification(
    email_request: EmailRequest = Depends(),
):
    # Guardar archivos temporalmente y obtener sus rutas
    attachment_paths = []
    for file in email_request.attachments:
        file_path = f"temp_uploads/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        attachment_paths.append(file_path)

    service = EmailNotificationService()
    notification = service.create_email_notification(email_request=email_request)
    return notification
