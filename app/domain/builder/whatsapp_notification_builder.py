from typing import List
from ..whatsapp_notification import WhatsAppNotification
from .inotification_builder import INotificationBuilder


class WhatsappNotificationBuilder(INotificationBuilder):
    def __init__(self):
        self._phone_number = None
        self._message = None
        self._media_url = None
        self._caption = None
        self._interactive_buttons = []
        self._language = "es"

    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number
        return self

    def set_message(self, message: str):
        self._message = message
        return self

    def set_media_url(self, media_url: str):
        self._media_url = media_url
        return self

    def set_caption(self, caption: str):
        self._caption = caption
        return self

    def set_interactive_buttons(self, buttons: List[str]):
        self._interactive_buttons = buttons
        return self

    def set_language(self, language: str):
        self._language = language
        return self

    def build(self) -> WhatsAppNotification:
        if not self._phone_number:
            raise ValueError("El número de teléfono es obligatorio")
        return WhatsAppNotification(
            phone_number=self._phone_number,
            message=self._message,
            media_url=self._media_url,
            caption=self._caption,
            interactive_buttons=self._interactive_buttons,
            language=self._language,
        )
