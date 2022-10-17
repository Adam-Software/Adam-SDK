from enum import Enum
from imaplib import Commands
import unittest

from AdamController import AdamController
from Joint import Joint
from JsonParser import JsonParser
from Motor import Motor
from MotorCommand import MotorCommand
from SerializableCommands import SerializableCommands


class MotorEnum(Enum):
    Head = 7
    Neck = 2


class TestProject(unittest.TestCase):
    def test_something(self):
        # Прямое взяимодействие с контроллером
        self.AdamController()
        # Инцилизация контроллера через Json взяимодействие с контроллером
        self.AdamControllerJson()

    def AdamController(self):
        adamController = AdamController(
            motors=[Motor(name="Head", joint=Joint(2000, 3000, 100, 1)),
                    Motor(name="Neck", joint=Joint(1000, 2000, 20, 2))])

        self.TestSetMotorTargetPosition(adamController)

        adamController.SetMotorTargetPosition("Head", 50)
        adamController.HandleCommand(commands=SerializableCommands(
            [MotorCommand(MotorEnum.Head.name, 100),MotorCommand(MotorEnum.Neck.name, 50)]))

    def AdamControllerJson(self):

        config = JsonParser.ReadConfig()
        motors = []
        for element in config:
            motors.append(Motor(name=element['name'],
                                joint=Joint(element['joint']['lover_limit'],
                                            element['joint']['upper_limit'],
                                            element['joint']['speed'],
                                            element['joint']['id'])))
        adamController = AdamController(motors)
        self.TestSetMotorTargetPosition(adamController)

        self.TestJsonCommand(adamController)

    def TestJsonCommand(self, adamController):
        SerializableCommandsJson = JsonParser.ReadCommand()
        commands = []
        for element in SerializableCommandsJson['motors']:
            commands.append(MotorCommand(**element))

        adamController.HandleCommand(SerializableCommands(commands))

    def TestSetMotorTargetPosition(self, adamController):
        adamController.SetMotorTargetPosition(MotorEnum.Head.name, 50)

if __name__ == '__main__':
    unittest.main()
