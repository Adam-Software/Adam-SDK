from enum import Enum

from AdamController import AdamController
from Joint import Joint
from JsonParser import JsonParser
from Motor import Motor
from MotorCommand import MotorCommand
from SerializableCommands import SerializableCommands


class MotorEnum(Enum):
    Head = 13
    Neck = 2


def AdamControllerJson():
    config = JsonParser.ReadConfig()
    motors = []
    for element in config:
        motors.append(Motor(name=element['name'],
                            joint=Joint(element['joint']['lover_limit'],
                                        element['joint']['upper_limit'],
                                        element['joint']['speed'],
                                        element['joint']['id'])))
    adamController = AdamController(motors)

    adamController.SetMotorTargetPosition(MotorEnum.Head.name, 50)

    TestJsonCommand(adamController)


def TestJsonCommand(adamController):
    SerializableCommandsJson = JsonParser.ReadCommand()
    commands = []
    for element in SerializableCommandsJson['motors']:
        commands.append(MotorCommand(**element))

    adamController.HandleCommand(SerializableCommands(commands))

AdamControllerJson()