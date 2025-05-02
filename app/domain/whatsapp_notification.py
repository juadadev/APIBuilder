from dataclasses import dataclass


@dataclass()
class WhatsappNotification:
    phone_number: str
    message: str
    media_url: str
    caption: str
    interactive_buttons: list[str]
    language: str
