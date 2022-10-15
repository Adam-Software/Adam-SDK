from Motor import Motor
from typing import Dict, List

from SerializableCommands import SerializableCommands


class AdamController:
    motors: List[Motor]
    __name2Motor: Dict[str, Motor]

    def __init__(self, motors: List[Motor]) -> None:
        self.motors = motors
        self.__name2Motor = {}
        for motor in motors:
            self.__name2Motor[motor.name] = motor

    def SetMotorTargetPosition(self, motorName, targetPosition):
        self.__name2Motor[motorName].target_position = targetPosition
        self.__Update()

    def __Update(self):
        for motor in self.__name2Motor.values():
            joint = motor.joint
            joint.RotateTo(motor.target_position)
            motor.present_position = joint.GetPresentPosition()

    def HandleCommand(self, commands: List[SerializableCommands]):
        for command in commands.motors:
            self.SetMotorTargetPosition(command.name, command.goal_position)
