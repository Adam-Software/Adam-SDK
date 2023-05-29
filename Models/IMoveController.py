from abc import ABC, abstractmethod
from Models.Motor import Motor

class IMoveController(ABC):
    @abstractmethod
    def move(self, motor: Motor, target_position: float, speed: float) -> None:
        pass