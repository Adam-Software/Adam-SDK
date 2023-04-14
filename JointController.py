from typing import Any
from Models.Joint import Joint
from ServoConnection import ServoConnection


class JointController:

    _goalPosition: int
    _servoConnection: ServoConnection
    __targetPosition: float
    __joint: Joint

    def __init__(self, joint: Joint) -> None:
        self.__joint = joint
        self.__targetPosition = -1
        self._servoConnection = Any

    def RotateTo(self, newTargetPosition: float) -> None:
        if newTargetPosition != self.__targetPosition:
            self.__targetPosition = newTargetPosition
            _goalPosition = ((self.__joint.upper_limit - self.__joint.lover_limit) *
                             (self.__targetPosition/100)) + self.__joint.lover_limit
            self._servoConnection.AppendCommandBuffer([self.__joint.id, self.__joint.speed, _goalPosition])

    def SetSpeed(self, newSpeed: int):
        self.__joint.speed = newSpeed

    def SetServoConnection(self, servoConnection: ServoConnection):
        self._servoConnection = servoConnection

    def GetPresentPosition(self):
        return self.__targetPosition
