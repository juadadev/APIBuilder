from typing import List
from app.domain.inotification import INotification
from ...interface.iemail_notification_builder import IEmailNotificationBuilder
from app.schemas.priority import Priority


class EmailNotificationBuilderDirector:
    def __init__(self, builder: IEmailNotificationBuilder):
        self._builder = builder

    def construct_email_notification(
        self, to: str, cc: List[str], amount: float, payment_method: str
    ) -> INotification:
        body = f"Gracias por tu pago de ${amount:.2f} usando {payment_method}"
        return (
            self._builder.set_to(to)
            .set_cc(cc)
            .set_body(body)
            .set_priority(Priority.ALTA)
            .build()
        )
