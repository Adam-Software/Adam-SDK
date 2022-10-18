from servo_serial.connection import Connection
from scservo_sdk import *


class ServoConnection:
    ADDR_STS_GOAL_POSITION = 42
    ADDR_STS_GOAL_SPEED = 46

    portHandler = Connection().getPortHandler()
    packetHandler = Connection().getPacketHandler()

    groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_STS_GOAL_POSITION, 2)

    def SyncWriteServos(self,
                        servosIds: [int],
                        servosSpeed: [int],
                        goalsPos: [int]):
        scs_error = None
        scs_add_param_result = None

        i = len(servosSpeed)
        for num in range(i):
            servos = servosIds[num]
            servos_speed = servosSpeed[num]

            scs_comm_result, scs_error = self.packetHandler.write2ByteTxRx(self.portHandler, servos,
                                                                           self.ADDR_STS_GOAL_SPEED,
                                                                           servos_speed)

        i = len(goalsPos)
        for num in range(i):
            servos = servosIds[num]
            scs_goal_position = int(goalsPos[num])
            param_goal_position = [SCS_LOBYTE(scs_goal_position), SCS_HIBYTE(scs_goal_position)]
            scs_add_param_result = self.groupSyncWrite.addParam(servos, param_goal_position)

        scs_comm_result = self.groupSyncWrite.txPacket()

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
        scs_add_param_result = self.groupSyncWrite.addParam(servoId, param_goal_position)

        scs_comm_result = self.groupSyncWrite.txPacket()

        self.groupSyncWrite.clearParam()

        return scs_comm_result, scs_error, scs_add_param_result
