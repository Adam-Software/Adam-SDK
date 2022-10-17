from servo_serial.connection import Connection
from scservo_sdk import *


class ServoConnection:
    ADDR_STS_GOAL_POSITION = 42
    ADDR_STS_GOAL_SPEED = 46

    portHandler = Connection().getPacketHandler()
    packetHandler = Connection().getPortHandler()

    groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_STS_GOAL_POSITION, 2)

    def SyncWriteData(self, ServosID, ServosSpeed, GoalPos):
        scs_error = None
        scs_add_param_result = None

        # Open port
        #self.portHandler.openPort()

        i = len(ServosSpeed)
        for num in range(i):
            servos = ServosID[num]
            servos_speed = ServosSpeed[num]

            scs_comm_result, scs_error = self.packetHandler.write2ByteTxRx(self.portHandler, servos,
                                                                           self.ADDR_STS_GOAL_SPEED,
                                                                           servos_speed)

        i = len(GoalPos)
        for num in range(i):
            servos = ServosID[num]
            scs_goal_position = int(GoalPos[num])
            param_goal_position = [SCS_LOBYTE(scs_goal_position), SCS_HIBYTE(scs_goal_position)]
            scs_add_param_result = self.groupSyncWrite.addParam(servos, param_goal_position)

        scs_comm_result = self.groupSyncWrite.txPacket()

        self.groupSyncWrite.clearParam()

        return scs_comm_result, scs_error, scs_add_param_result
