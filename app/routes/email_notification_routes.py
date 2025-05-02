from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.email_request import EmailRequest, EmailResponse
from app.services.email_notification_service import EmailNotificationService

email_router = APIRouter()


@email_router.post('/notifications/email', response_model=EmailResponse)
async def create_email_notification(
    email_request: Annotated[EmailRequest, Depends()],
):
    service = EmailNotificationService()
    notification = await service.create_email_notification(email_request=email_request)
    return notification
