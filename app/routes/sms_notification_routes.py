from fastapi import APIRouter

# from app.services.sms_notification_service import SMSNotificationService

sms_router = APIRouter()


# @sms_router.post("/notifications/sms", response_model=SMSResponse)
# def create_sms_notification(request: SMSRequest):
#     service = SMSNotificationService()
#     notification = service.create_sms_notification(sms_request=request)
#     return notification
