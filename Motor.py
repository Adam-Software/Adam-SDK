from enum import Enum
from Joint import Joint


class Motor:
    name: str
    joint: Joint
    target_position: float
    present_position: int

    def __init__(self, name: str, joint: Joint) -> None:
        self.name = name
        self.joint = joint
        self.target_position = 0
    """
    Данный метод это заглушка вместо Update.
    """
    def Changed(self) -> None:
        self.joint.RotateTo(self.target_position)
        #self.present_position = self.joint.GetPresentPosition()
