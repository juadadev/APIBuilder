from abc import ABC, abstractmethod
from inotification import INotification


class INotificationBuilder(ABC):
    @abstractmethod
    def build(self) -> INotification:
        pass
