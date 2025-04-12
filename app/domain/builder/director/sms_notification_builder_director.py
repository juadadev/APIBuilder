from datetime import datetime
from ...inotification import INotification
from ..sms_notification_builder import SMSNotificationBuilder


class SMSNotificationBuilderDirector:
    def __init__(self, builder: SMSNotificationBuilder):
        self._builder = builder

    def construct_sms_notification(
        self,
        phone_number: str,
        amount: float,
        payment_method: str,
        sender_id: str = "PAYMENT_SYS",
        delivery_report_required: bool = False,
    ) -> INotification:
        message = f"Gracias por tu pago. Se ha procesado ${amount:.2f} usando {payment_method}"
        return (
            self._builder.set_phone_number(phone_number)
            .set_message(message)
            .set_sender_id(sender_id)
            .set_delivery_report_required(delivery_report_required)
            .set_schedule_time(datetime.now())
            .build()
        )
