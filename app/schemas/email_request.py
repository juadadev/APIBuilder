from typing import List
from pydantic import BaseModel, Field
from app.schemas.notification_type import NotificationType
from app.schemas.payment_method import PaymentMethod
from app.schemas.priority import Priority


class EmailRequest(BaseModel):
    to: str
    amount: float
    payment_method: PaymentMethod
    notification_type: NotificationType


class EmailResponse(BaseModel):
    to: str = Field(..., alias="_to")
    subject: str = Field(..., alias="_subject")
    body: str = Field(..., alias="_body")
    cc: List[str] = Field(..., alias="_cc")
    bcc: List[str] = Field(..., alias="_bcc")
    attachments: List[str] = Field(..., alias="_attachments")
    priority: Priority = Field(..., alias="_priority")

    class Config:
        validate_by_name = True
        from_attributes = True  # Por si usas objetos tipo ORM
