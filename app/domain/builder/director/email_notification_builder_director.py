from typing import List, Optional

from app.schemas.email_request import EmailRequest
from ...interface.iemail_notification_builder import IEmailNotificationBuilder
from app.schemas.priority import Priority


class EmailNotificationBuilderDirector:
    def __init__(self, builder: IEmailNotificationBuilder):
        self._builder = builder

    def construct_minimal_email(self, email_request: EmailRequest):
        return (
            self._builder.set_to(email_request.to)
            .set_subject("Pago confirmado")
            .set_body(
                f"Notificación via {email_request.notification_type.value} de Pago por ${email_request.amount:.2f} con {email_request.payment_method.value} confirmado."
            )
            .set_priority(Priority.ALTA)
            .build()
        )

    def construct_full_email(
        self,
        to: str,
        subject: str,
        body: str,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
        priority: Optional[Priority] = None,
    ):
        return (
            self._builder.set_to(to)
            .set_subject(subject)
            .set_body(body)
            .set_cc(cc or [])
            .set_bcc(bcc or [])
            .set_attachments(attachments or [])
            .set_priority(Priority.ALTA if priority is None else priority)
            .build()
        )
