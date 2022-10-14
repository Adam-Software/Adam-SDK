from enum import Enum
from Joint import Joint

class MotorEnum(Enum):
    Head = 7
    Neck = 2

class Motor:
    name: str
    joint: Joint
    target_position: float
    present_position: int

    def __init__(self, name: str, joint: Joint) -> None:
        self.name = name
        self.joint = joint
        #self.joint.servo_Id = MotorEnum[name].value
        self.target_position = 0
    
    def Changed(self) -> None:
        self.joint.RotateTo(self.target_position)