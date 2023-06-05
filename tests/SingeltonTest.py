from adam_sdk import AdamManager
from adam_sdk.Models.MotorCommand import MotorCommand
from adam_sdk.Models.SerializableCommands import SerializableCommands
import time

#def AdamControllerJson():
#    config = JsonParser.ReadConfig()
#    motors = []
#    for element in config:
#        motors.append(Motor(name=element['name'],
#                            JointController=JointController(joint=Joint(element['joint']['lover_limit'],
#                                                                        element['joint']['upper_limit'],
#                                                                        element['joint']['speed'],
#                                                                        element['joint']['id']))))
#    return AdamController(motors)


def HandCalculate(west: str, angle1: float, angle2: float, angle3: float, angle4: float):
    return SerializableCommands([MotorCommand(west + "_Shoulder", angle1),
                                 MotorCommand(west + "_UpperArm", angle2),
                                 MotorCommand(west + "_LowerArm_Up", angle3),
                                 MotorCommand(west + "_LowerArm_Down", angle4)])


if __name__ == '__main__':

    adamController = AdamManager()

    #Базовые значения
    adamController.handle_command(commands=SerializableCommands(
        [MotorCommand('Head', 100),
         MotorCommand('Neck', 100),
         MotorCommand('Right_UpperArm', 10),
         MotorCommand('Left_UpperArm', 10),
         MotorCommand('Chest', 50)]))

    time.sleep(5)

    adamController2 = AdamManager()
    adamController2.handle_command(commands=HandCalculate("Left", 0, 30, 0, 0))

    time.sleep(5)

    adamController3 = AdamManager()
    adamController3.handle_command(commands=HandCalculate("Right", 0, 30, 0, 0))
