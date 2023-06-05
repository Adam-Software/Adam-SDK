import unittest

from adam_sdk import AdamManager
from adam_sdk.Models.Joint import Joint
from adam_sdk.Controllers.JointController import JointController
from adam_sdk import JsonParser
from adam_sdk.Models.Motor import Motor
from adam_sdk.Models.MotorCommand import MotorCommand
from adam_sdk.Models.MotorEnum import MotorEnum
from adam_sdk.Models.SerializableCommands import SerializableCommands


class TestProject(unittest.TestCase):
    def test_something(self):
        # Прямое взяимодействие с контроллером
        self.AdamController()
        # Инцилизация контроллера через Json взяимодействие с контроллером
        self.AdamControllerJson()

    def AdamController(self):
        adamController = AdamManager(
            motors=[Motor(name="Head", joint_controller=JointController(joint=Joint(2000, 3000, 100, 1))),
                    Motor(name="Neck", joint_controller=JointController(joint=Joint(1000, 2000, 20, 2)))])

        adamController.handle_command(commands=SerializableCommands(
            [MotorCommand(MotorEnum.Head.name, 100), MotorCommand(MotorEnum.Neck.name, 50)]))

    def AdamControllerJson(self):

        config = JsonParser._read_config()
        motors = []
        for element in config:
            motors.append(Motor(name=element['name'],
                                joint_controller=JointController(joint=Joint(element['joint']['lover_limit'],
                                                                            element['joint']['upper_limit'],
                                                                            element['joint']['speed'],
                                                                            element['joint']['id']))))
        adamController = AdamManager(motors)

        self.TestJsonCommand(adamController)

    def TestJsonCommand(self, adamController):
        SerializableCommandsJson = JsonParser.ReadCommand()
        commands = []
        for element in SerializableCommandsJson['motors']:
            commands.append(MotorCommand(**element))

        adamController.HandleCommand(SerializableCommands(commands))


if __name__ == '__main__':
    unittest.main()
