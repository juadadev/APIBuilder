from dataclasses import dataclass

from ..schemas.priority import Priority


@dataclass()
class EmailNotification:
    to: str
    subject: str | None = None
    body: str | None = None
    cc: list[str] | None = None
    bcc: list[str] | None = None
    attachments: list | None = None
    priority: Priority | None = None
