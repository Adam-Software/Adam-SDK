class Joint:
    lover_limit: int
    upper_limit: int
    speed: int
    servo_Id:int
    id: int

    def __init__(self, lover_limit: int, upper_limit: int, speed: int, id: int) -> None:
        self.lover_limit = lover_limit
        self.upper_limit = upper_limit
        self.speed = speed
        self.id = id

    def RotateTo(self,newTargetPosition:float) -> None:
        print(((self.upper_limit - self.lover_limit) * (newTargetPosition/100)) + self.lover_limit)
        #__packetHandler.write2ByteTxRx(PortHandler('/dev/ttyUSB0'), servoId, ADDR_STS_GOAL_SPEED,SCS_MOVING_SPEED)
