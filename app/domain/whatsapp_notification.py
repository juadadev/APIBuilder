from typing import List


class WhatsappNotification:
    def __init__(
        self,
        phone_number: str,
        message: str,
        media_url: str,
        caption: str,
        interactive_buttons: List[str],
        language: str,
    ):
        self._phone_number = phone_number
        self._message = message
        self._media_url = media_url
        self._caption = caption
        self._interactive_buttons = interactive_buttons
        self._language = language
