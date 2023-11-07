from typing import List, Optional
from .MotorCommand import MotorCommand
from typing import Tuple

class SerializableCommands:
    motors: Optional[List[MotorCommand]]
    gif_paths: Optional[List[List[str]]]
    move_data: Optional[Tuple[Tuple[float, float], float]]

    def __init__(self, motors: Optional[List[MotorCommand]] = None, gif_paths: Optional[List[List[str]]] = None, move_data: Optional[Tuple[Tuple[float, float], float]] = None) -> None:
        self.motors = motors
        self.gif_paths = gif_paths
        self.move_data = move_data