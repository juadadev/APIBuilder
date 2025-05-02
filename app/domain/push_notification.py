from dataclasses import dataclass

from app.schemas.priority import PriorityPush


@dataclass()
class PUSHNotification:
    device_token: str
    priority: PriorityPush
    title: str | None = None
    message: str | None = None
    image_url: str | None = None
    click_action: str | None = None
