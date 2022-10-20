import unittest
import numpy as np

from scservo_sdk import SCS_LOBYTE, SCS_HIBYTE


class MyTestCase(unittest.TestCase):

    @staticmethod
    def goalPositionFloat(targetPosition: float):
        return ((2300 - 1800) * (targetPosition / 100)) + 1800

    @staticmethod
    def goalPositionInt(targetPosition: float):
        return int(((2300 - 1800) * (targetPosition / 100)) + 1800)

    def test_return_type(self):
        self.assertEqual(type(self.goalPositionFloat(20)), float)
        self.assertEqual(type(self.goalPositionInt(20)), int)

    def test_result(self):
        self.assertNotEqual(self.goalPositionFloat(20.05), self.goalPositionInt(20.05))

    def test_result_after_to_int(self):
        self.assertEqual(int(self.goalPositionFloat(20.05)), self.goalPositionInt(20.05))

    def test_sdk_func(self):
        for i in np.arange(0, 100, 0.01):
            positionInt = self.goalPositionInt(i)
            positionFloat = self.goalPositionFloat(i)
            param_goal_position_from_int = [SCS_LOBYTE(positionInt), SCS_HIBYTE(positionInt)]
            param_goal_position_from_float = [SCS_LOBYTE(int(positionFloat)), SCS_HIBYTE(int(positionFloat))]

            print(param_goal_position_from_float)
            print(param_goal_position_from_int)

            self.assertEqual(param_goal_position_from_int[0], param_goal_position_from_float[0])
            self.assertEqual(param_goal_position_from_int[1], param_goal_position_from_float[1])
            print(i)


if __name__ == '__main__':
    unittest.main()
