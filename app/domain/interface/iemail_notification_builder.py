from abc import ABC, abstractmethod

from ...domain.email_notification import EmailNotification
from ...schemas.priority import Priority


# Interface
class IEmailNotificationBuilder(ABC):
    @abstractmethod
    def set_to(self, to: str) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def set_subject(self, subject: str) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def set_body(self, body: str) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def set_cc(self, cc: list[str]) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def set_bcc(self, bcc: list[str]) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def set_attachments(self, attachment: list[str]) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def set_priority(self, priority: Priority) -> 'IEmailNotificationBuilder':
        pass

    @abstractmethod
    def build(self) -> EmailNotification:
        pass
