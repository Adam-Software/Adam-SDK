from JsonParser import JsonParser
from collections import namedtuple


class ParsingRangeArray:

    def __init__(self):
        self._data = JsonParser.ReadPositionRange()
        self._headRange = self._data['HeadRange']
        self._armRangeRight = self._data['ArmRangeRight']
        self._armRangeLeft = self._data['ArmRangeLeft']
        self._pressRange = self._data['PressRange']
        self._bodyRange = self._data['BodyRange']
        self._legRightRange = self._data['LegRightRange']
        self._legLeftRange = self._data['LegLeftRange']
        self._handsRange = self._data['HandsRange']

    @property
    def GetHeadRange(self):
        headNamed = ["HeadRangeMin", "HeadRangeMax", "NeckRangeMin", "NeckRangeMax"]
        headTuple = namedtuple('HeadRange', headNamed)
        headRange = headTuple(self._headRange[0], self._headRange[1],
                              self._headRange[2], self._headRange[3])

        return headRange

    @property
    def GetArmRangeRight(self):
        armNamed = ["ArmShoulderRightMin", "ArmShoulderRightMax",
                    "ArmForearmRightMin", "ArmForearmRightMax", "ArmElbowTopRightMin",
                    "ArmElbowTopRightMax", "ArmElbowBottRightMin", "ArmElbowBottRightMax"]

        armTuple = namedtuple('ArmRange', armNamed)
        armRange = armTuple(self._armRangeRight[0], self._armRangeRight[1],
                            self._armRangeRight[2], self._armRangeRight[3],
                            self._armRangeRight[4], self._armRangeRight[5],
                            self._armRangeRight[6], self._armRangeRight[7])
        return armRange

    @property
    def GetArmRangeLeft(self):
        armNamed = ["ArmShoulderLeftMax", "ArmShoulderLeftMin",
                    "ArmForearmLeftMin", "ArmForearmLeftMax", "ArmElbowTopLeftMin",
                    "ArmElbowTopLeftMax", "ArmElbowBottLeftMin", "ArmElbowBottLeftMax"]

        armTuple = namedtuple('ArmRange', armNamed)
        armRange = armTuple(self._armRangeLeft[0], self._armRangeLeft[1],
                            self._armRangeLeft[2], self._armRangeLeft[3],
                            self._armRangeLeft[4], self._armRangeLeft[5],
                            self._armRangeLeft[6], self._armRangeLeft[7])

        return armRange

    @property
    def GetPressRange(self):
        pressNamed = ["PressTopAngleMin", "PressTopAngleMax",
                      "PressBottAngleMin", "PressBottAngleMax"]
        pressTuple = namedtuple('PressRange', pressNamed)
        pressRange = pressTuple(self._pressRange[0], self._pressRange[1],
                                self._pressRange[2], self._pressRange[3])

        return pressRange

    @property
    def GetBodyRange(self):
        bodyNamed = ["BodyRotMin", "BodyRotMax"]
        bodyTuple = namedtuple("BodyTuple", bodyNamed)
        bodyRange = bodyTuple(self._bodyRange[0], self._bodyRange[1])

        return bodyRange

    @property
    def GetLegRightRange(self):
        legNamed = ["LegHipAngRightMin", "LegHipAngRightMax",
                    "LegFootAngRightMin", "LegFootAngRightMax",
                    "LegKneeAngRightMin", "LegKneeAngRightMax"]
        legTuple = namedtuple("RightLegTuple", legNamed)
        legRange = legTuple(self._legRightRange[0], self._legRightRange[1],
                            self._legRightRange[2], self._legRightRange[3],
                            self._legRightRange[4], self._legRightRange[5])

        return legRange

    @property
    def GetLegLeftRange(self):
        legNamed = ["LegHipAngLeftMin", "LegHipAngLeftMax",
                    "LegFootAngLeftMin", "LegFootAngLeftMax",
                    "LegKneeAngLeftMin", "LegKneeAngLeftMax"]
        legTuple = namedtuple("LeftLegTuple", legNamed)
        legRange = legTuple(self._legLeftRange[0], self._legLeftRange[1],
                            self._legLeftRange[2], self._legLeftRange[3],
                            self._legLeftRange[4], self._legLeftRange[5])

        return legRange

    @property
    def GetHandsRange(self):
        return self._handsRange
