from datetime import datetime


class SMSNotification:
    def __init__(
        self,
        phone_number: str,
        message: str | None = None,
        sender_id: str | None = None,
        delivery_report_required: bool | None = None,
        schedule_time: datetime | None = None,
    ):
        self._phone_number = phone_number
        self._message = message
        self._sender_id = sender_id
        self._delivery_report_required = delivery_report_required
        self._schedule_time = schedule_time
