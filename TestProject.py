import unittest

from AdamController import AdamController
from Joint import Joint
from JsonParser import JsonParser
from Motor import Motor



class TestProject(unittest.TestCase):
    def test_something(self):
        adamController_1 = AdamController(
            motors=[Motor(name="Head", joint=Joint(2000, 3000, 100)), Motor(name="Neck", joint=Joint(1000, 2000, 20))])

        adamController_1.SetMotorTargetPosition("Head", 50)

        config = JsonParser.ReadConfig()

        motors = []
        for element in config:
            motors.append(Motor(**element))

        adamController_2 = AdamController(motors=motors)
        adamController_2.SetMotorTargetPosition("Head", 20)


if __name__ == '__main__':
    unittest.main()
