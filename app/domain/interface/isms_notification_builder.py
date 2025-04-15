from abc import ABC, abstractmethod
from datetime import datetime

from ...domain.sms_notification import SMSNotification


class ISMSNotificationBuilder(ABC):
    @abstractmethod
    def set_phone_number(self, phone_number: str) -> "ISMSNotificationBuilder":
        pass

    @abstractmethod
    def set_message(self, message: str) -> "ISMSNotificationBuilder":
        pass

    @abstractmethod
    def set_sender_id(self, sender_id: str) -> "ISMSNotificationBuilder":
        pass

    @abstractmethod
    def set_delivery_report_required(
        self, delivery_report_required: bool
    ) -> "ISMSNotificationBuilder":
        pass

    @abstractmethod
    def set_schedule_time(self, schedule_time: datetime) -> "ISMSNotificationBuilder":
        pass

    @abstractmethod
    def build(self) -> SMSNotification:
        pass
