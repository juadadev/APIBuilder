from typing import List, Optional
from .inotification import INotification
from ..schemas.priority import Priority


class EmailNotification(INotification):
    def __init__(
        self,
        to: str,
        subject: Optional[str] = None,
        body: Optional[str] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
        priority: Optional[Priority] = None,
    ):
        self._to = to
        self._subject = subject
        self._body = body
        self._cc = cc or []
        self._bcc = bcc or []
        self._attachments = attachments or []
        self._priority = priority

    def send(self, amount: float, payment_method: str) -> str:
        body = (
            self._body
            or f"Se ha procesado tu pago de ${amount:.2f} usando {payment_method}."
        )
        return (
            f"[EMAIL]\n"
            f"To: {self._to}\n"
            f"Subject: {self._subject or 'Notificación de pago'}\n"
            f"Body: {body}.\n"
            f"CC: {', '.join(self._cc)}\n"
            f"BCC: {', '.join(self._bcc)}\n"
            f"Attachments: {', '.join(self._attachments)} | Priority: {self._priority}"
        )

    def to_response(self) -> dict:
        return {
            "_to": self._to,
            "_subject": self._subject or "Notificación de pago",
            "_body": self._body,
            "_cc": self._cc,
            "_bcc": self._bcc,
            "_attachments": self._attachments,
            "_priority": self._priority.value if self._priority else None,
        }
