from abc import ABC, abstractmethod
from app.domain.inotification import INotification
from ...schemas.priority import Priority


class IEmailNotificationBuilder(ABC):
    @abstractmethod
    def set_to(self, to: str) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def set_subject(self, subject: str) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def set_body(self, body: str) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def set_cc(self, cc: list) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def set_bcc(self, bcc: list) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def set_attachments(self, attachments: list) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def set_priority(self, priority: Priority) -> "IEmailNotificationBuilder":
        pass

    @abstractmethod
    def build(self) -> INotification:
        pass
