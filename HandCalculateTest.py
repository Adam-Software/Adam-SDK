from turtle import right
from AdamController import AdamController
from Models.Joint import Joint
from JointController import JointController
from JsonParser import JsonParser
from Models.Motor import Motor
from Models.MotorCommand import MotorCommand
from Models.MotorEnum import MotorEnum
from Models.SerializableCommands import SerializableCommands
import time

def HandCalculate(west: str, angle1: float, angle2: float, angle3: float):
    return SerializableCommands([MotorCommand(west + "_shoulder", angle1),
                                 MotorCommand(west + "_upper_arm", angle2),
                                 MotorCommand(west + "_lower_arm_up", angle3)])


if __name__ == '__main__':

    adamController = AdamController()

    #Базовые значения
    adamController.HandleCommand(commands=SerializableCommands(
        [MotorCommand('head', 50),
         MotorCommand('neck', 50),
         MotorCommand('right_upper_arm', 10),
         MotorCommand('left_upper_arm', 10),
         MotorCommand('chest', 50)]))

    time.sleep(5)

    adamController2 = AdamController()
    adamController2.HandleCommand(commands=HandCalculate("left", 0, 15, 0))

    time.sleep(5)

    adamController3 = AdamController()
    adamController3.HandleCommand(commands=HandCalculate("right", 0, 15, 0))
