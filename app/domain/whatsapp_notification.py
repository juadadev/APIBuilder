from typing import List, Optional
from inotification import INotification


class WhatsAppNotification(INotification):
    def __init__(
        self,
        phone_number: str,
        message: Optional[str] = None,
        media_url: Optional[str] = None,
        caption: Optional[str] = None,
        interactive_buttons: Optional[List[str]] = None,
        language: str = "es",
    ):
        self.phone_number = phone_number
        self.message = message
        self.media_url = media_url
        self.caption = caption
        self.interactive_buttons = interactive_buttons or []
        self.language = language

    def send(self, amount: float, payment_method: str) -> str:
        return (
            f"[WHATSAPP]\nTo: {self.phone_number}\n"
            f"Mensaje: Pago de ${amount:.2f} con {payment_method} confirmado.\n"
            f"Botones: {', '.join(self.interactive_buttons)}"
        )
