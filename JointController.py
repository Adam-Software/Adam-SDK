from typing import Any
from Models.Joint import Joint
from ServoConnection import ServoConnection


class JointController:

    _goal_position: int
    _servo_connection: ServoConnection
    __target_position: float
    __joint: Joint

    def __init__(self, joint: Joint) -> None:
        self.__joint = joint
        self.__target_position = -1
        self._servo_connection = Any

    def RotateTo(self, target_position: float) -> None:
        if target_position != self.__target_position:
            self.__target_position = target_position
            _goal_position = ((self.__joint.upper_limit - self.__joint.lover_limit) *
                             (self.__target_position/100)) + self.__joint.lover_limit
            self._servo_connection.AppendCommandBuffer((self.__joint.id, self.__joint.speed, _goal_position))

    def set_speed(self, speed: int):
        self.__joint.speed = speed

    def servo_connection(self, servo_connection: ServoConnection):
        self._servo_connection = servo_connection

    def get_present_position(self):
        return self.__target_position
