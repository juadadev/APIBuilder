from typing import List, Optional
from app.domain.email_notification import EmailNotification
from app.domain.interface.iemail_notification_builder import IEmailNotificationBuilder
from app.schemas.priority import Priority


class EmailNotificationBuilder(IEmailNotificationBuilder):
    def __init__(self):
        self._to: Optional[str] = None
        self._subject: Optional[str] = None
        self._body: Optional[str] = None
        self._cc: List[str] = []
        self._bcc: List[str] = []
        self._attachments: List[str] = []
        self._priority: Optional[Priority] = None

    def set_to(self, to: str) -> IEmailNotificationBuilder:
        self._to = to
        return self

    def set_subject(self, subject: str) -> IEmailNotificationBuilder:
        self._subject = subject
        return self

    def set_body(self, body: str) -> IEmailNotificationBuilder:
        self._body = body
        return self

    def set_cc(self, cc: List[str]) -> IEmailNotificationBuilder:
        self._cc = cc
        return self

    def set_bcc(self, bcc: List[str]) -> IEmailNotificationBuilder:
        self._bcc = bcc
        return self

    def set_attachments(self, attachments: List[str]) -> IEmailNotificationBuilder:
        self._attachments = attachments
        return self

    def set_priority(self, priority: Priority) -> IEmailNotificationBuilder:
        self._priority = priority
        return self

    def build(self) -> EmailNotification:
        if not self._to:
            raise ValueError("El correo destinatario es obligatorio")

        return EmailNotification(
            to=self._to,
            subject=self._subject,
            body=self._body,
            cc=self._cc,
            bcc=self._bcc,
            attachments=self._attachments,
            priority=self._priority,
        )
