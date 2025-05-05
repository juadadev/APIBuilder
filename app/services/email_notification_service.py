from app.core.config import Config
from app.domain.builder.director.email_notification_builder_director import (
    EmailNotificationBuilderDirector,
)
from app.domain.builder.email_notification_builder import EmailNotificationBuilder
from app.domain.templates.purchase_summary_template import PurchaseSummaryTemplate
from app.schemas.email_request import EmailRequest
from app.services.email_sender import EmailSender

config = Config()


class EmailNotificationService:
    async def create_email_notification(
        self, email_request: EmailRequest
    ) -> dict[str, str]:
        builder = EmailNotificationBuilder()
        director = EmailNotificationBuilderDirector(builder)
        notification = director.construct_minimal_email(email_request=email_request)

        # Generar HTML
        template = PurchaseSummaryTemplate()
        html_body = template.render(body=notification.body)

        # Enviar correo
        sender = EmailSender(
            config.SMTP_HOST, config.SMTP_PORT, config.SMTP_EMAIL, config.SMTP_PASSWORD
        )
        sender.send_email(
            recipient=email_request.to,
            subject=notification.subject or 'Sin asunto',
            html_body=html_body,
            attachments=email_request.attachments,  # <-- Aquí enviamos directamente UploadFile[]
        )

        return {
            'notification': 'El pago fue procesado y se notificó al usuario por correo'
        }
