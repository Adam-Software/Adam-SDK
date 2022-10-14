import unittest

from AdamController import AdamController
from Joint import Joint
from JsonParser import JsonParser
from Motor import Motor



class TestProject(unittest.TestCase):
    def test_something(self):
        adamController_1 = AdamController(
            motors=[Motor(name="Head", joint=Joint(2000, 3000, 100, 1)),
                    Motor(name="Neck", joint=Joint(1000, 2000, 20, 2))])

        adamController_1.SetMotorTargetPosition("Head", 50)

        config = JsonParser.ReadConfig()

        motors = []
        for element in config:
            motors.append(Motor(name=element['name'],
                                joint=Joint(element['joint']['lover_limit'],
                                            element['joint']['upper_limit'],
                                            element['joint']['speed'],
                                            element['joint']['id'])))

        adamController_2 = AdamController(motors)
        adamController_2.SetMotorTargetPosition("Head", 20)


if __name__ == '__main__':
    unittest.main()
