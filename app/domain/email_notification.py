from typing import List, Optional
from ..schemas.priority import Priority


class EmailNotification:
    def __init__(
        self,
        to: str,
        subject: Optional[str] = None,
        body: Optional[str] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        attachments: Optional[List] = None,
        priority: Optional[Priority] = None,
    ):
        self._to = to
        self._subject = subject
        self._body = body
        self._cc = cc or []
        self._bcc = bcc or []
        self._attachments = attachments or []
        self._priority = priority
