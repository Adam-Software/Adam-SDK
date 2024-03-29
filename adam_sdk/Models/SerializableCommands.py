from typing import List

from .MotorCommand import MotorCommand


class SerializableCommands:
    motors: List[MotorCommand]

    def __init__(self, motors: List[MotorCommand]) -> None:
        self.motors = motors
