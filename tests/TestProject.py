import unittest

from AdamController import AdamController
from Models.Joint import Joint
from JointController import JointController
from JsonParser import JsonParser
from Models.Motor import Motor
from Models.MotorCommand import MotorCommand
from Models.MotorEnum import MotorEnum
from Models.SerializableCommands import SerializableCommands


class TestProject(unittest.TestCase):
    def test_something(self):
        # Прямое взяимодействие с контроллером
        self.AdamController()
        # Инцилизация контроллера через Json взяимодействие с контроллером
        self.AdamControllerJson()

    def AdamController(self):
        adamController = AdamController(
            motors=[Motor(name="Head", JointController=JointController(joint=Joint(2000, 3000, 100, 1))),
                    Motor(name="Neck", JointController=JointController(joint=Joint(1000, 2000, 20, 2)))])

        adamController.HandleCommand(commands=SerializableCommands(
            [MotorCommand(MotorEnum.Head.name, 100), MotorCommand(MotorEnum.Neck.name, 50)]))

    def AdamControllerJson(self):

        config = JsonParser.ReadConfig()
        motors = []
        for element in config:
            motors.append(Motor(name=element['name'],
                                JointController=JointController(joint=Joint(element['joint']['lover_limit'],
                                                                            element['joint']['upper_limit'],
                                                                            element['joint']['speed'],
                                                                            element['joint']['id']))))
        adamController = AdamController(motors)

        self.TestJsonCommand(adamController)

    def TestJsonCommand(self, adamController):
        SerializableCommandsJson = JsonParser.ReadCommand()
        commands = []
        for element in SerializableCommandsJson['motors']:
            commands.append(MotorCommand(**element))

        adamController.HandleCommand(SerializableCommands(commands))


if __name__ == '__main__':
    unittest.main()