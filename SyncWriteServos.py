# Available SCServo model on this example : All models using Protocol SCS
# This example is tested with a SCServo(STS/SMS/SCS), and an URT
# Be sure that SCServo(STS/SMS/SCS) properties are already set as %% ID : 1 / Baudnum : 6 (Baudrate : 1000000)
#

#from scservo_sdk import *                    # Uses SCServo SDK library

# Control table address
ADDR_STS_GOAL_POSITION     = 42
ADDR_STS_GOAL_SPEED        = 46

# Default setting
BAUDRATE                    = 1000000           # SCServo default baudrate : 1000000
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

#SCS_MOVING_SPEED            = 2000              # SCServo moving speed
protocol_end                = 0                 # SCServo bit end(STS/SMS=0, SCS=1)

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows

#portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Get methods and members of Protocol

#packetHandler = PacketHandler(protocol_end)

# Initialize GroupSyncWrite instance

#groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_STS_GOAL_POSITION, 2)


class SyncWriteServos():

    def __init__(self):
        super().__init__()
      
    def SyncWriteData(self, ServosID, ServosSpeed, GoalPos):

        i = len(ServosSpeed)
        for num in range(i):
            SCS1_ID = ServosID[num]
            SCS_MOVING_SPEED = ServosSpeed[num]
            # SCServo#1 speed
            result = [SCS1_ID, SCS_MOVING_SPEED]
            print(result)
            #scs_comm_result, scs_error = packetHandler.write2ByteTxRx(portHandler, SCS1_ID, ADDR_STS_GOAL_SPEED, SCS_MOVING_SPEED)

        i = len(GoalPos) 
        for num in range(i):
            SCS1_ID = ServosID[num]
            scs_goal_position = int(GoalPos[num])
            param = [SCS1_ID, scs_goal_position]
            print(param)
            #scs_addparam_result = groupSyncWrite.addParam(SCS1_ID, scs_goal_position)
            
        #scs_comm_result = groupSyncWrite.txPacket()
        # Clear syncwrite parameter storage
        #groupSyncWrite.clearParam()
        
        #return scs_comm_result, scs_error, scs_addparam_result

      
     # Close port
     # portHandler.closePort()