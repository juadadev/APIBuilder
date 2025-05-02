from fastapi import File, Form, UploadFile
from pydantic import BaseModel

from app.schemas.notification_type import NotificationType
from app.schemas.payment_method import PaymentMethod


class EmailRequest(BaseModel):
    to: str = Form(...)
    amount: float = Form(...)
    payment_method: PaymentMethod = Form(...)
    notification_type: NotificationType = Form(...)
    attachments: list[UploadFile] = File([])

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            'example': {
                'to': 'jdayala@unicesar.edu.co',
                'amount': 3000,
                'payment_method': PaymentMethod.CREDIT_CARD,
                'notification_type': NotificationType.EMAIL,
                'attachments': ['comprobantedepago.pdf'],
            }
        }


class EmailResponse(BaseModel):
    notification: str
