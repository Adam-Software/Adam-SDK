from abc import ABC, abstractmethod
from ast import List, Tuple
from Models.Motor import Motor

class IMoveController(ABC):
    @abstractmethod
    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        pass