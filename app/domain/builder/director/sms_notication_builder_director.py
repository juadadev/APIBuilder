from datetime import datetime
from enum import Enum

from app.domain.interface.isms_notification_builder import ISMSNotificationBuilder
from app.schemas.sms_request_and_response import SMSRequest


class SMSNotificationBuilderDirector:
    def __init__(self, builder: ISMSNotificationBuilder):
        self._builder = builder

    def construct_minimal_sms(self, sms_request: SMSRequest):
        # Si los campos son Enum, usamos .value, si no, los usamos directamente
        payment_method = (
            sms_request.payment_method.value
            if isinstance(sms_request.payment_method, Enum)
            else str(sms_request.payment_method)
        )

        notification_type = (
            sms_request.notification_type.value
            if isinstance(sms_request.notification_type, Enum)
            else str(sms_request.notification_type)
        )

        return (
            self._builder.set_phone_number(sms_request.phone_number)
            .set_message(
                f"Pago por ${sms_request.amount:.2f} con {payment_method} confirmado. NOTIFICACION: {notification_type}"
            )
            .set_schedule_time(datetime.now())
            .build()
        )
