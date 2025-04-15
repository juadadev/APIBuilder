from datetime import datetime
from typing import Optional

from app.domain.interface.isms_notification_builder import ISMSNotificationBuilder
from app.domain.sms_notification import SMSNotification


class SMSNotificationBuilder(ISMSNotificationBuilder):
    def __init__(self):
        self._phone_number: str
        self._message: Optional[str] = None
        self._sender_id: Optional[str] = None
        self._delivery_report_required = None
        self._schedule_time = None

    def set_phone_number(self, phone_number: str) -> ISMSNotificationBuilder:
        self._phone_number = phone_number
        return self

    def set_message(self, message: str) -> ISMSNotificationBuilder:
        self._message = message
        return self

    def set_sender_id(self, sender_id: str) -> ISMSNotificationBuilder:
        self._sender_id = sender_id
        return self

    def set_delivery_report_required(
        self, delivery_report_required: bool
    ) -> ISMSNotificationBuilder:
        self._delivery_report_required = delivery_report_required
        return self

    def set_schedule_time(self, schedule_time: datetime) -> ISMSNotificationBuilder:
        self._schedule_time = schedule_time
        return self

    def build(self) -> SMSNotification:
        return SMSNotification(
            phone_number=self._phone_number,
            message=self._message,
            sender_id=self._sender_id,
            delivery_report_required=self._delivery_report_required,
            schedule_time=self._schedule_time,
        )
