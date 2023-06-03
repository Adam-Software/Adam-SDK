from typing import List
from servo_serial.connection import Connection
from scservo_sdk import GroupSyncWrite, SCS_LOBYTE, SCS_HIBYTE

class ServoConnection:
    def __init__(self):
        self.__doubleBuffer = []

    def append_command_buffer(self, command: tuple[int, int, float]):
        self.__doubleBuffer.append(command)

    def sync_write_servos(self):
        ADDR_STS_GOAL_POSITION = 42
        ADDR_STS_GOAL_SPEED = 46

        portHandler = Connection().getPortHandler()
        packetHandler = Connection().getPacketHandler()
        groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_STS_GOAL_POSITION, 2)

        scs_comm_result = []
        scs_error = []
        scs_add_param_result = []

        for servoId, servoSpeed, goalPos in self.__doubleBuffer:
            scs_comm_result.append(packetHandler.write2ByteTxRx(portHandler, servoId,
                                                                ADDR_STS_GOAL_SPEED, servoSpeed))

            param_goal_position = [SCS_LOBYTE(int(goalPos)), SCS_HIBYTE(int(goalPos))]
            scs_add_param_result.append(groupSyncWrite.addParam(servoId, param_goal_position))

        scs_comm_result.append(groupSyncWrite.txPacket())

        self.__doubleBuffer.clear()
        groupSyncWrite.clearParam()

        return scs_comm_result, scs_error, scs_add_param_result