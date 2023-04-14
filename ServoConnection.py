from typing import List
from servo_serial.connection import Connection
from scservo_sdk import *
from serial_fingers_control.FingersControl import *


class ServoConnection:
    __doubleBuffer = List[List[int]]

    def __init__(self):
        self.__doubleBuffer = []
        self.fingersControl = FingersControl()

    ADDR_STS_GOAL_POSITION = 42
    ADDR_STS_GOAL_SPEED = 46

    portHandler = Connection().getPortHandler()
    packetHandler = Connection().getPacketHandler()

    groupSyncWrite = GroupSyncWrite(
        portHandler, packetHandler, ADDR_STS_GOAL_POSITION, 2)

    def AppendCommandBuffer(self, command: [int, int, float]):
        self.__doubleBuffer.append(command)

    def InsertCommandServo(self):
        self.SyncWriteServos(self.__doubleBuffer)

    def SyncWriteServos(self, doubleBuffer: List[List[int]]):

        scs_error = None
        # scs_comm_result = None
        scs_add_param_result = None

        for servoId, servoSpeed, goalPos in doubleBuffer:

            if servoId == 4 or servoId == 3:
                self.fingersControl.FingersManage(servoId, goalPos, servoSpeed)
                continue

            scs_comm_result, scs_error = self.packetHandler.write2ByteTxRx(self.portHandler, servoId,
                                                                           self.ADDR_STS_GOAL_SPEED,
                                                                           servoSpeed)

            param_goal_position = [SCS_LOBYTE(int(goalPos)), SCS_HIBYTE(int(goalPos))]

            scs_add_param_result = self.groupSyncWrite.addParam(servoId, param_goal_position)

        scs_comm_result = self.groupSyncWrite.txPacket()

        self.__doubleBuffer.clear()
        self.groupSyncWrite.clearParam()

        return scs_comm_result, scs_error, scs_add_param_result
