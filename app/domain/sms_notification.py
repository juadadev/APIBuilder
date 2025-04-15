from datetime import datetime
from typing import Optional


class SMSNotification:
    def __init__(
        self,
        phone_number: str,
        message: Optional[str] = None,
        sender_id: Optional[str] = None,
        delivery_report_required: Optional[bool] = None,
        schedule_time: Optional[datetime] = None,
    ):
        self._phone_number = phone_number
        self._message = message
        self._sender_id = sender_id
        self._delivery_report_required = delivery_report_required
        self._schedule_time = schedule_time
