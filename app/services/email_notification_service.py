from app.domain.builder.director.email_notification_builder_director import (
    EmailNotificationBuilderDirector,
)
from app.domain.builder.email_notification_builder import EmailNotificationBuilder
from app.domain.email_notification import EmailNotification
from app.schemas.email_request import EmailRequest


class EmailNotificationService:
    def create_email_notification(
        self, email_request: EmailRequest
    ) -> EmailNotification:
        builder = EmailNotificationBuilder()
        director = EmailNotificationBuilderDirector(builder)
        notification = director.construct_minimal_email(email_request=email_request)
        return notification
