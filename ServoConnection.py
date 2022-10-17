from servo_serial.connection import Connection
from scservo_sdk import *

class ServoConnection():
    ADDR_STS_GOAL_POSITION = 42
    ADDR_STS_GOAL_SPEED = 46

    @staticmethod
    def getPacketHandler():
        return Connection().getPacketHandler()

    @staticmethod
    def getPortHandler():
        return Connection().getPortHandler()