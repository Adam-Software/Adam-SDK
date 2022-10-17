from Models.Joint import Joint


class JointController:

    __targetPosition: float
    __joint: Joint

    def __init__(self, joint: Joint) -> None:
        self.__joint = joint
        self.__targetPosition = 0

    def RotateTo(self, newTargetPosition: float) -> None:
        self.__targetPosition = newTargetPosition
        print(((self.__joint.upper_limit - self.__joint.lover_limit) *
              (self.__targetPosition/100)) + self.__joint.lover_limit)

    def GetPresentPosition(self):
        return self.__targetPosition