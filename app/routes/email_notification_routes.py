# app/api/email_notification_routes.py

from fastapi import APIRouter

from app.schemas.email_notification_request import (
    EmailNotificationRequest,
    EmailNotificationResponse,
)
from app.services.email_notification_service import EmailNotificationService

email_router = APIRouter()


@email_router.post("/notifications/email")
def create_email_notification(request: EmailNotificationRequest):
    service = EmailNotificationService()
    notification = service.create_payment_notification(
        to=request.to,
        cc=request.cc,
        amount=request.amount,
        payment_method=request.payment_method,
    )
    return notification.__dict__
