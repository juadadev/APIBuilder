from fastapi import APIRouter
from app.schemas.email_request import EmailRequest, EmailResponse
from app.services.email_notification_service import EmailNotificationService

email_router = APIRouter()


@email_router.post("/notifications/email", response_model=EmailResponse)
def create_email_notification(request: EmailRequest):
    service = EmailNotificationService()
    notification = service.create_email_notification(email_request=request)
    return notification
