import unittest
from ParsingRangeArray import ParsingRangeArray
from collections import namedtuple


# checked name/value
# source file for name: class ParsingRangeArray
# source file for value: position_range.json
class ParsingRangeArrayTest(unittest.TestCase):

    def testHeadRange(self):
        parsing = ParsingRangeArray()
        headRangeActual = parsing.GetHeadRange
        print(headRangeActual)

        headNamed = ["HeadRangeMin", "HeadRangeMax", "NeckRangeMin", "NeckRangeMax"]
        headTuple = namedtuple('HeadRange', headNamed)
        headRangeExpected = headTuple(2548, 1548, 1800, 2300)

        self.assertEqual(headRangeActual, headRangeExpected)

    def testArmRangeRight(self):
        parsing = ParsingRangeArray()
        armRangeActual = parsing.GetArmRangeRight
        print(armRangeActual)

        armNamed = ["ArmShoulderRightMin", "ArmShoulderRightMax",
                    "ArmForearmRightMin", "ArmForearmRightMax", "ArmElbowTopRightMin",
                    "ArmElbowTopRightMax", "ArmElbowBottRightMin", "ArmElbowBottRightMax"]

        armTuple = namedtuple('ArmRange', armNamed)
        armRangeExpected = armTuple(2048, 8793, 3641, 2617, 3543, 1495, 3618, 1570)

        self.assertEqual(armRangeActual, armRangeExpected)

    def testArmRangeLeft(self):
        parsing = ParsingRangeArray()
        armRangeActual = parsing.GetArmRangeLeft
        print(armRangeActual)

        armNamed = ["ArmShoulderLeftMax", "ArmShoulderLeftMin",
                    "ArmForearmLeftMin", "ArmForearmLeftMax", "ArmElbowTopLeftMin",
                    "ArmElbowTopLeftMax", "ArmElbowBottLeftMin", "ArmElbowBottLeftMax"]

        armTuple = namedtuple('ArmRange', armNamed)
        armRangeExpected = armTuple(8793, 2048, 487, 1511, 799, 2847, 75, 2121)

        self.assertEqual(armRangeActual, armRangeExpected)

    def testPressRange(self):
        parsing = ParsingRangeArray()
        pressRangeActual = parsing.GetPressRange
        print(pressRangeActual)

        pressNamed = ["PressTopAngleMin", "PressTopAngleMax",
                      "PressBottAngleMin", "PressBottAngleMax"]
        pressTuple = namedtuple('PressRange', pressNamed)
        pressRangeExpected = pressTuple(3700, 200,
                                3700, 400)

        self.assertEqual(pressRangeActual, pressRangeExpected)

    def testBodyRange(self):
        parsing = ParsingRangeArray()
        bodyRangeActual = parsing.GetBodyRange
        print(bodyRangeActual)

        bodyNamed = ["BodyRotMin", "BodyRotMax"]
        bodyTuple = namedtuple("BodyTuple", bodyNamed)
        bodyRangeExpected = bodyTuple(0, 3900)

        self.assertEqual(bodyRangeActual, bodyRangeExpected)

    def testLegRightRange(self):
        parsing = ParsingRangeArray()
        legRangeActual = parsing.GetLegRightRange
        print(legRangeActual)

        legNamed = ["LegHipAngRightMin", "LegHipAngRightMax",
                    "LegFootAngRightMin", "LegFootAngRightMax",
                    "LegKneeAngRightMin", "LegKneeAngRightMax"]
        legTuple = namedtuple("RightLegTuple", legNamed)
        legRangeExpected = legTuple(3757, 2261, 173, 3164, 1868, 3363)

        self.assertEqual(legRangeActual, legRangeExpected)

    def testLegLeftRange(self):
        parsing = ParsingRangeArray()
        legRangeActual = parsing.GetLegLeftRange
        print(legRangeActual)

        legNamed = ["LegHipAngLeftMin", "LegHipAngLeftMax",
                    "LegFootAngLeftMin", "LegFootAngLeftMax",
                    "LegKneeAngLeftMin", "LegKneeAngLeftMax"]
        legTuple = namedtuple("LeftLegTuple", legNamed)
        legRangeExpected = legTuple(1004, 2499, 3943, 952, 2376, 881)

        self.assertEqual(legRangeActual, legRangeExpected)


if __name__ == '__main__':
    unittest.main()
