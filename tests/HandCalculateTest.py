import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from AdamController import AdamController
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands
import time

def HandCalculate(west: str, angle1: float, angle2: float, angle3: float):
    return SerializableCommands([MotorCommand(west + "_shoulder", angle1),
                                 MotorCommand(west + "_upper_arm", angle2),
                                 MotorCommand(west + "_lower_arm_up", angle3)])


if __name__ == '__main__':

    adamController = AdamController()

    #Выставление в дефолтную позицию
    adamController.HandleCommand(commands=SerializableCommands(
        [MotorCommand('head', 50),
         MotorCommand('neck', 50),
         MotorCommand('right_upper_arm', 10),
         MotorCommand('left_upper_arm', 10),
         MotorCommand('chest', 50),
         MotorCommand('left_upper_leg', 0),
         MotorCommand('right_upper_leg', 0)]))

    time.sleep(5)

    adamController2 = AdamController()
    adamController2.HandleCommand(commands=HandCalculate("left", 0, 65, 0))

    time.sleep(5)

    adamController3 = AdamController()
    adamController3.HandleCommand(commands=HandCalculate("right", 0, 65, 0))
    
    time.sleep(5)

    #возврат в дефолтную позицию
    adamController.Reset()
