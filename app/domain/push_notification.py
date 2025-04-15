from typing import Optional

from app.schemas.priority import PriorityPush


class PUSHNotification:
    def __init__(
        self,
        device_token: str,
        priority: PriorityPush,
        title: Optional[str] = None,
        message: Optional[str] = None,
        image_url: Optional[str] = None,
        click_action: Optional[str] = None,
    ):
        self._device_token = device_token
        self._title = title
        self._message = message
        self._priority = priority
        self._image_url = image_url
        self._click_action = click_action
