from turtle import right
from AdamController import AdamController
from Models.Joint import Joint
from JointController import JointController
from JsonParser import JsonParser
from Models.Motor import Motor
from Models.MotorCommand import MotorCommand
from Models.MotorEnum import MotorEnum
from Models.SerializableCommands import SerializableCommands


def AdamControllerJson():
    config = JsonParser.ReadConfig()
    motors = []
    for element in config:
        motors.append(Motor(name=element['name'],
                            JointController=JointController(joint=Joint(element['joint']['lover_limit'],
                                                                        element['joint']['upper_limit'],
                                                                        element['joint']['speed'],
                                                                        element['joint']['id']))))
    return AdamController(motors)


def HandCalculate(west: str, angle1: float, angle2: float, angle3: float, angle4: float):
    return SerializableCommands([MotorCommand(west + "_Shoulder", angle1),
                                 MotorCommand(west + "_UpperArm", angle2),
                                 MotorCommand(west + "_LowerArm_Up", angle3),
                                 MotorCommand(west + "_LowerArm_Down", angle4)])


if __name__ == '__main__':

    adamController = AdamControllerJson()

    #Базовые значения
    adamController.HandleCommand(commands=SerializableCommands(
        [MotorCommand('Head', 50), MotorCommand('Neck', 50), MotorCommand('Right_UpperArm', 10), MotorCommand('Left_UpperArm', 10), MotorCommand('Chest', 50)]))

    adamController.HandleCommand(commands=HandCalculate("Left", 0, 15, 0, 0))
    adamController.HandleCommand(commands=HandCalculate("Right", 0, 15, 0, 0))
