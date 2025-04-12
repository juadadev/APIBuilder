from typing import Optional
from inotification import INotification
from datetime import datetime


class SMSNotification(INotification):
    def __init__(
        self,
        phone_number: str,
        message: Optional[str] = None,
        sender_id: Optional[str] = None,
        delivery_report_required: bool = False,
        schedule_time: Optional[datetime] = None,
    ):
        self.phone_number = phone_number
        self.message = message
        self.sender_id = sender_id
        self.delivery_report_required = delivery_report_required
        self.schedule_time = schedule_time

    def send(self, amount: float, payment_method: str) -> str:
        return (
            f"[SMS]\nTo: {self.phone_number}\n"
            f"Mensaje: Tu pago de ${amount:.2f} con {payment_method} fue exitoso."
        )
