class Joint:
    lover_limit: int
    upper_limit: int
    speed: int
    servo_Id: int
    id: int
    __targetPosition: float

    def __init__(self, lover_limit: int, upper_limit: int, speed: int, id: int) -> None:
        self.lover_limit = lover_limit
        self.upper_limit = upper_limit
        self.speed = speed
        self.id = id
        self.__targetPosition = 0

    def RotateTo(self, newTargetPosition: float) -> None:
        self.__targetPosition = newTargetPosition
        print(((self.upper_limit - self.lover_limit) *
              (self.__targetPosition/100)) + self.lover_limit)
        #__packetHandler.write2ByteTxRx(PortHandler('/dev/ttyUSB0'), servoId, ADDR_STS_GOAL_SPEED,SCS_MOVING_SPEED)

    def GetPresentPosition(self):
        return self.__targetPosition  # не затейлево спросить какой параметр у сервы
