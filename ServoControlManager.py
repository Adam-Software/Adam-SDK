from InterpolationMethods import InterpolationMethods
from SyncWriteServos import SyncWriteServos

ServosID = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
ServosSpeed = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 600, 600, 2000, 2000, 1200, 1200]

HeadID = 1
NeckID = 2
HeadSpeed = [2000, 2000]
ArmID = [11, 9, 7, 5, 12, 10, 8, 6]
ArmSpeed = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000]
PressID = [14, 15]
PressSpeed = [2000, 2000]
BodyID = [13]
BodySpeed = [2000]
LegID = [17, 19, 21, 16, 18, 20]
LegSpeed = [600, 2000, 1200, 600, 2000, 1200]

GoalPosHeadPer = 0
GoalPosNeckPer = 0

ArmShoulderAnglRightPer = 0
ArmForearmAnglRightPer = 0
ArmElbowTopAnglRightPer = 0
ArmElbowBottAnglRightPer = 0
ArmElbowAnglRightPer = 0

ArmShoulderAnglLeftPer = 0
ArmForearmAnglLeftPer = 0
ArmElbowTopAnglLeftPer = 0
ArmElbowBottAnglLeftPer = 0
ArmElbowAnglLeftPer = 0
SwitchBothElbow = True

PressTopAnglPer = 0
PressBottAnglPer = 0

BodyRotPer = 0.5

HightBothLegPer = 0
HightLeftLegPer = 0
HightRightLegPer = 0
SwitchBothLeg = True

def CalcHeadPos():
    ReadPosArray = InterpolationMethods()
    HeadPos = ReadPosArray.CalcHead(GoalPosHeadPer)
    return HeadPos

def CalcArmPos():
    ReadPosArray = InterpolationMethods()
    ArmPos = ReadPosArray.CalcArms(ArmShoulderAnglRightPer, ArmForearmAnglRightPer, ArmElbowTopAnglRightPer, ArmElbowBottAnglRightPer, ArmElbowAnglRightPer,
                 ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer, ArmElbowTopAnglLeftPer, ArmElbowBottAnglLeftPer, ArmElbowAnglLeftPer, SwitchBothElbow)
    return ArmPos

def CalcPressPos():
    ReadPosArray = InterpolationMethods()
    PressPos = ReadPosArray.CalcPress(PressTopAnglPer, PressBottAnglPer)
    return PressPos

def CalcBodyPos():
    ReadPosArray = InterpolationMethods()
    BodyPos = ReadPosArray.CalcBody(BodyRotPer)
    return BodyPos

def CalcLegPos():
    ReadPosArray = InterpolationMethods()
    LegPos = ReadPosArray.CalcLeg(HightBothLegPer, HightLeftLegPer, HightRightLegPer, SwitchBothLeg)
    return LegPos

#Function run example
WritePos = SyncWriteServos()
GoalPos = CalcArmPos()
#ServosID = ArmID
#ServosSpeed = ArmSpeed
WritePos = WritePos.SyncWriteData(ServosID, ServosSpeed, GoalPos)
print(WritePos)