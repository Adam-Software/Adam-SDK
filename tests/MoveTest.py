import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from AdamController import AdamController
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands
import time

if __name__ == '__main__':

    adamController = AdamController()
    #linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    #angular_velocity = 0.0         # без вращения вокруг оси Z

    #linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    #angular_velocity = 0.0         # без вращения вокруг оси Z

    #forward
    adamController.Move((0.0, 1.0), 0.0)
    time.sleep(0.05)

    #back
    adamController.Move((0.0, -1.0), 0.0)
    time.sleep(0.05)

    #right
    adamController.Move((1.0, 0.0), 0.0)
    time.sleep(0.05)

    #left
    adamController.Move((-1.0, 0.0), 0.0)
    time.sleep(0.05)

    #left and forward
    adamController.Move((-1.0, 1.0), 0.0)
    time.sleep(0.05)

    #rigt and forward
    adamController.Move((1.0, 1.0), 0.0)
    time.sleep(0.05)

    #back and left
    adamController.Move((-1.0, -1.0), 0.0)
    time.sleep(0.05)

    #back and right
    adamController.Move((1.0, -1.0), 0.0)
    time.sleep(0.05)

    #u-turn to the right
    adamController.Move((0.0, 0.0), 1.0)
    time.sleep(0.05)

    #u-turn to the left
    adamController.Move((0.0, 0.0), -1.0)
    time.sleep(0.05)

    adamController.Move((0.0, 0.0), 0.0)
