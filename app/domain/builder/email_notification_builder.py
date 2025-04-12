from typing import List
from ..interface.iemail_notification_builder import IEmailNotificationBuilder
from ..email_notification import EmailNotification
from ...schemas.priority import Priority


class EmailNotificationBuilder(IEmailNotificationBuilder):
    def __init__(self):
        self._to = None
        self._subject = "Notificación de pago"
        self._body = None
        self._cc = []
        self._bcc = []
        self._attachments = []
        self._priority = Priority.ALTA

    def set_to(self, to: str):
        self._to = to
        return self

    def set_subject(self, subject: str):
        self._subject = subject
        return self

    def set_body(self, body: str):
        self._body = body
        return self

    def set_cc(self, cc: List[str]):
        self._cc = cc
        return self

    def set_bcc(self, bcc: List[str]):
        self._bcc = bcc
        return self

    def set_attachments(self, attachments: List[str]):
        self._attachments = attachments
        return self

    def set_priority(self, priority: Priority):
        self._priority = priority
        return self

    def build(self) -> EmailNotification:
        if not self._to:
            raise ValueError("El destinatario es obligatorio")
        return EmailNotification(
            to=self._to,
            subject=self._subject,
            body=self._body,
            cc=self._cc,
            bcc=self._bcc,
            attachments=self._attachments,
            priority=self._priority,
        )
