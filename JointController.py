from Models.Joint import Joint
from ServoConnection import ServoConnection


class JointController:


    _goalPosition: int
    _servoConnection: ServoConnection
    __targetPosition: float
    __joint: Joint

    def __init__(self, joint: Joint) -> None:
        self.__joint = joint
        self.__targetPosition = 0
        self._servoConnection = ServoConnection()

    def RotateTo(self, newTargetPosition: float) -> None:
        self.__targetPosition = newTargetPosition

        _goalPosition = int(((self.__joint.upper_limit - self.__joint.lover_limit) *
                         (self.__targetPosition/100)) + self.__joint.lover_limit)

        self._servoConnection.SyncWriteServo(self.__joint.id, self.__joint.speed, _goalPosition)



    def GetPresentPosition(self):
        return self.__targetPosition