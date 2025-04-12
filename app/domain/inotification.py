from abc import ABC, abstractmethod


class INotification(ABC):
    @abstractmethod
    def send(self, amount: float, payment_method) -> str:
        pass
