from enum import Enum

from AdamManager import AdamManager
from Controllers.JointController import JointController
from JsonParser import JsonParser
from Models.Joint import Joint
from Models.Motor import Motor
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands


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
