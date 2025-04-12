from pydantic import BaseModel
from typing import Optional, List, Literal

from app.schemas.priority import Priority


class NotificationRequest(BaseModel):
    channel: Literal["sms", "whatsapp", "email"]
    phone_number: str
    amount: float
    payment_method: str

    # Opcionales según el canal
    sender_id: Optional[str] = "PAYMENT_SYS"
    media_url: Optional[str] = None
    caption: Optional[str] = None
    interactive_buttons: Optional[List[str]] = None
    language: Optional[str] = "es"
    email_address: Optional[str] = None
    subject: Optional[str] = None


class EmailNotificationRequest(BaseModel):
    to: str
    amount: float
    payment_method: str
    channel: Literal["email", "whatsapp", "sms"] = "email"
    cc: Optional[List[str]] = None


class EmailNotificationResponse(BaseModel):
    _to: str
    _subject: str
    _body: str
    _cc: List[str]
    _bcc: List[str]
    _attachments: List[str]
    _priority: Priority
