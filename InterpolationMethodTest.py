import unittest
from InterpolationMethods import InterpolationMethods


class InterpolationMethodTest(unittest.TestCase):

    def testCalcHead(self):
        calcPosition = InterpolationMethods()
        positionHead = calcPosition.CalcHead(1, 1)

        print(positionHead)
        self.assertEqual(positionHead[0], 1548)
        self.assertEqual(positionHead[1], 2300)

    def testCalcArms(self):
        calcPosition = InterpolationMethods()
        positionArms = calcPosition.CalcArms(1, 1, 1, 1, 1, 1, 1, 1, 1,  1, True)

        print(positionArms)
        self.assertEqual(positionArms[0], 8793)
        self.assertEqual(positionArms[1], 2617)
        self.assertEqual(positionArms[2], 1495)
        self.assertEqual(positionArms[3], 1570)

        self.assertEqual(positionArms[4], 8793)
        self.assertEqual(positionArms[5], 1511)
        self.assertEqual(positionArms[6], 2847)
        self.assertEqual(positionArms[7], 2121)

    def testCalcPress(self):
        calcPosition = InterpolationMethods()
        positionPress = calcPosition.CalcPress(1, 1)

        print(positionPress)
        self.assertEqual(positionPress[0], 200)
        self.assertEqual(positionPress[1], 400)
        print(positionPress)

    def testCalcBody(self):
        calcPosition = InterpolationMethods()
        positionBody = calcPosition.CalcBody(1)

        print(positionBody)
        self.assertEqual(positionBody, 3900)

    def testCalcLeg(self):
        calcPosition = InterpolationMethods()
        positionLeg = calcPosition.CalcLeg(1, 1, 1, False)

        print(positionLeg)

        self.assertEqual(positionLeg[0], 3363)
        self.assertEqual(positionLeg[1], 3164)
        self.assertEqual(positionLeg[2], 2261)
        self.assertEqual(positionLeg[3], 881)
        self.assertEqual(positionLeg[4], 952)
        self.assertEqual(positionLeg[5], 2499)


if __name__ == '__main__':
    unittest.main()
