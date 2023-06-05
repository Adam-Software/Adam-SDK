from enum import Enum

from adam_sdk import AdamManager
from adam_sdk.Controllers.JointController import JointController
from adam_sdk import JsonParser
from adam_sdk.Models.Joint import Joint
from adam_sdk.Models.Motor import Motor
from adam_sdk.Models.MotorCommand import MotorCommand
from adam_sdk.Models.SerializableCommands import SerializableCommands


def AdamControllerJson():
    config = JsonParser.ReadConfig()
    motors = []
    for element in config:
        motors.append(Motor(name=element['name'],
                            joint_controller=JointController(joint=Joint(element['joint']['lover_limit'],
                                                                        element['joint']['upper_limit'],
                                                                        element['joint']['speed'],
                                                                        element['joint']['id']))))
    adamController = AdamManager(motors)

    TestJsonCommand(adamController)


def TestJsonCommand(adamController):
    SerializableCommandsJson = JsonParser.ReadCommand()
    commands = []
    for element in SerializableCommandsJson['motors']:
        commands.append(MotorCommand(**element))

    adamController.HandleCommand(SerializableCommands(commands))


AdamControllerJson()
