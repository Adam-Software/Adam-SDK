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

    #forward
    adamController.Move((1.0, 0.0), 0.0)
    time.sleep(0.01)

    #back
    adamController.Move((-1.0, 0.0), 0.0)
    time.sleep(0.01)

    #right
    adamController.Move((0.0, -1.0), 0.0)
    time.sleep(0.01)

    #left
    adamController.Move((0.0, 1.0), 0.0)
    time.sleep(0.01)

    #left and forward
    adamController.Move((1.0, 1.0), 0.0)
    time.sleep(0.01)

    #rigt and forward
    adamController.Move((1.0, -1.0), 0.0)
    time.sleep(0.01)

    #back and left
    adamController.Move((-1.0, 1.0), 0.0)
    time.sleep(0.01)

    #back and right
    adamController.Move((-1.0, -1.0), 0.0)
    time.sleep(0.01)

    #u-turn to the right
    adamController.Move((0.0, 0.0), -1.0)
    time.sleep(0.01)

    #u-turn to the left
    adamController.Move((0.0, 0.0), 1.0)
    time.sleep(0.01)

    adamController.Move((0.0, 0.0), 0)
