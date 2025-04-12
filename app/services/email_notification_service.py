from typing import List
from app.domain.builder.director.email_notification_builder_director import (
    EmailNotificationBuilderDirector,
)
from app.domain.builder.email_notification_builder import EmailNotificationBuilder
from app.domain.inotification import INotification


class EmailNotificationService:
    def create_payment_notification(
        self, to: str, cc: List[str], amount: float, payment_method: str
    ) -> INotification:
        builder = EmailNotificationBuilder()
        director = EmailNotificationBuilderDirector(builder)
        notification = director.construct_email_notification(
            to, cc, amount, payment_method
        )
        return notification
