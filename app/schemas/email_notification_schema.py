from pydantic import BaseModel, Field
from typing import List, Optional
from .priority import Priority  # Asegúrate que esta enum esté bien definida


class EmailNotificationSchema(BaseModel):
    to: str
    subject: Optional[str] = "Comprobante de pago"
    body: Optional[str] = None
    cc: List[str] = Field(default_factory=list)
    bcc: List[str] = Field(default_factory=list)
    attachments: List[str] = Field(default_factory=list)
    priority: Optional[Priority] = Priority.MEDIA
