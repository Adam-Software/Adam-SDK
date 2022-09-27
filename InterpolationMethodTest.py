import unittest
from InterpolationMethod import calcPosServo


class MyTestCase(unittest.TestCase):

    def testCalcHead(self):
        calcPosition = calcPosServo
        positionHead = calcPosition.CalcHead(self, 10, 10)

        self.assertEqual(positionHead[0], -7452)
        self.assertEqual(positionHead[1], 6800)

    def testCalcArms(self):
        calcPosition = calcPosServo
        positionArms = calcPosition.CalcArms(self, 1000, 1000, 1000, 1000, 1000,
                                             1000, 1000, 1000, 1000, 1000,  True)

        self.assertEqual(positionArms[0], 6747048)
        self.assertEqual(positionArms[1], -1020359)
        self.assertEqual(positionArms[2], -2044457)
        self.assertEqual(positionArms[3], -2044382)
        self.assertEqual(positionArms[4], 6747048)
        self.assertEqual(positionArms[5], 1024487)
        self.assertEqual(positionArms[6], 2048799)
        self.assertEqual(positionArms[7], 2046075)

    def testCalcPress(self):
        calcPosition = calcPosServo
        positionPress = calcPosition.CalcPress(self, 1000, 1000)

        self.assertEqual(positionPress[0], -3496300)
        self.assertEqual(positionPress[1], -3296300)
        print(positionPress)

    def testCalcBody(self):
        calcPosition = calcPosServo
        positionBody = calcPosition.CalcBody(self, 1000)

        self.assertEqual(positionBody, 3900000)

    def testCalcLeg(self):
        calcPosition = calcPosServo
        positionLeg = calcPosition.CalcLeg(self, 1000, 1000, 1000, True)

        print(positionLeg)

        self.assertEqual(positionLeg[0], 1496868)
        self.assertEqual(positionLeg[1], 2991173)
        self.assertEqual(positionLeg[2], -1492243)
        self.assertEqual(positionLeg[3], -1492624)
        self.assertEqual(positionLeg[4], -2987057)
        self.assertEqual(positionLeg[5], 1496004)


if __name__ == '__main__':
    unittest.main()
