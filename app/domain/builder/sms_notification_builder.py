from datetime import datetime
from .inotification_builder import INotificationBuilder
from ..sms_notification import SMSNotification


class SMSNotificationBuilder(INotificationBuilder):
    def __init__(self):
        self._phone_number = None
        self._message = None
        self._sender_id = None
        self._delivery_report_required = False
        self._schedule_time = None

    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number
        return self

    def set_message(self, message: str):
        self._message = message
        return self

    def set_sender_id(self, sender_id: str):
        self._sender_id = sender_id
        return self

    def set_delivery_report_required(self, required: bool):
        self._delivery_report_required = required
        return self

    def set_schedule_time(self, schedule_time: datetime):
        self._schedule_time = schedule_time
        return self

    def build(self) -> SMSNotification:
        if not self._phone_number:
            raise ValueError("El número de teléfono es obligatorio")
        return SMSNotification(
            phone_number=self._phone_number,
            message=self._message,
            sender_id=self._sender_id,
            delivery_report_required=self._delivery_report_required,
            schedule_time=self._schedule_time,
        )
