from typing import Protocol


class EmailTemplate(Protocol):
    def render(self, **kwargs) -> str: ...
