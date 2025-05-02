from pydantic import BaseModel, Field

from .priority import Priority  # Asegúrate que esta enum esté bien definida


class EmailNotificationSchema(BaseModel):
    to: str
    subject: str | None = 'Comprobante de pago'
    body: str | None = None
    cc: list[str] = Field(default_factory=list)
    bcc: list[str] = Field(default_factory=list)
    attachments: list[str] = Field(default_factory=list)
    priority: Priority | None = Priority.MEDIA
