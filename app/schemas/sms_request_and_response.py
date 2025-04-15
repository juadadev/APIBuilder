from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.notification_type import NotificationType
from app.schemas.payment_method import PaymentMethod


class SMSRequest(BaseModel):
    phone_number: str
    amount: float
    payment_method: PaymentMethod
    notification_type: NotificationType

    # example sms request body
    class Config:
        json_schema_extra = {
            "example": {
                "phone_number": "+57 3123235233",
                "amount": 300.0,
                "payment_method": PaymentMethod.CREDIT_CARD,
                "notification_type": NotificationType.SMS,
            }
        }


class SMSResponse(BaseModel):
    phone_number: str = Field(..., alias="_phone_number")
    message: Optional[str] = Field(None, alias="_message")
    sender_id: Optional[str] = Field(None, alias="_sender_id")
    delivery_report_required: Optional[bool] = Field(
        None, alias="_delivery_report_required"
    )
    schedule_time: Optional[datetime] = Field(None, alias="_schedule_time")

    class Config:
        validate_by_name = True
        from_attributes = True
