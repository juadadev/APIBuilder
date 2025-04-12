from typing import List
from app.domain.builder.whatsapp_notification_builder import WhatsappNotificationBuilder


class WhatsAppNotificationBuilderDirector:
    def __init__(self, builder: WhatsappNotificationBuilder):
        self._builder = builder

    def construct_whatsapp_notification(
        self,
        amount: float,
        payment_method: str,
        phone_number: str,
        message: str,
        media_url: str,
        caption: str,
        interactive_buttons: List[str],
        language: str,
    ):
        message = f"Gracias por tu pago. Se ha procesado ${amount:.2f} usando {payment_method}"

        return (
            self._builder.set_phone_number(phone_number)
            .set_message(message)
            .set_media_url(media_url)
            .set_caption(caption)
            .set_interactive_buttons(interactive_buttons)
            .set_language(language)
            .build()
        )
