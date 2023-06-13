import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from adam_sdk import AdamManager
from adam_sdk import MotorCommand
from adam_sdk import SerializableCommands
import time

def HandCalculate(west: str, angle1: float, angle2: float, angle3: float, angle4: float):
    return SerializableCommands([MotorCommand(west + "_shoulder", angle1),
                                 MotorCommand(west + "_upper_arm", angle2),
                                 MotorCommand(west + "_lower_arm_up", angle3)])


if __name__ == '__main__':

    adamController = AdamManager()

    #Базовые значения
    adamController.handle_command(commands=SerializableCommands(
        [MotorCommand('head', 100),
         MotorCommand('neck', 100),
         MotorCommand('right_upper_arm', 10),
         MotorCommand('left_upper_arm', 10),
         MotorCommand('chest', 50)]))

    time.sleep(5)

    adamController2 = AdamManager()
    adamController2.handle_command(commands=HandCalculate("left", 0, 30, 0, 0))

    time.sleep(5)

    adamController3 = AdamManager()
    adamController3.handle_command(commands=HandCalculate("right", 0, 30, 0, 0))
