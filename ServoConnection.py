from distutils.cmd import Command
from typing import List
from servo_serial.connection import Connection
from scservo_sdk import *


class ServoConnection:
    ADDR_STS_GOAL_POSITION = 42
    ADDR_STS_GOAL_SPEED = 46

    portHandler = Connection().getPortHandler()
    packetHandler = Connection().getPacketHandler()

    groupSyncWrite = GroupSyncWrite(
        portHandler, packetHandler, ADDR_STS_GOAL_POSITION, 2)

    __doubleBuffer = List[int, int, int]

    def AppendCommandBuffer(self, command: List[int, int, int]):
        self.__doubleBuffer.append(command)

    def InsertCommandServo(self):
        self.SyncWriteServos()

    def SyncWriteServos(self, doubleBuffer: List[int, int, int]):

        scs_error, scs_comm_result, scs_add_param_result = None

        for servoId, servoSpeed, goalPos in zip(doubleBuffer):

            scs_comm_result, scs_error = self.packetHandler.write2ByteTxRx(self.portHandler, servoId,
                                                                           self.ADDR_STS_GOAL_SPEED,
                                                                           servoSpeed)
            param_goal_position = [SCS_LOBYTE(goalPos), SCS_HIBYTE(goalPos)]
            scs_add_param_result = self.groupSyncWrite.addParam(
                servoId, param_goal_position)

        scs_comm_result = self.groupSyncWrite.txPacket()

        self.__doubleBuffer.clear()
        self.groupSyncWrite.clearParam()

        return scs_comm_result, scs_error, scs_add_param_result

    def SyncWriteServo(self,
                       servoId: int,
                       servoSpeed: int,
                       goalPos: int):

        scs_comm_result, scs_error = self.packetHandler.write2ByteTxRx(self.portHandler, servoId,
                                                                       self.ADDR_STS_GOAL_SPEED,
                                                                       servoSpeed)

        param_goal_position = [SCS_LOBYTE(goalPos), SCS_HIBYTE(goalPos)]
        scs_add_param_result = self.groupSyncWrite.addParam(
            servoId, param_goal_position)

        scs_comm_result = self.groupSyncWrite.txPacket()

        self.groupSyncWrite.clearParam()

        return scs_comm_result, scs_error, scs_add_param_result
