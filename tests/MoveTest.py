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
    linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    angular_velocity = 0.0         # без вращения вокруг оси Z

    adamController.Move(linear_velocity, angular_velocity)
