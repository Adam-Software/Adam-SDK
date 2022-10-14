from Motor import Motor
from typing import Dict, List

from SerializableCommands import SerializableCommands


class AdamController:
    motors: List[Motor]
    _name2Motor: Dict[str, Motor]

    def __init__(self, motors: List[Motor]) -> None:
        self.motors = motors
        self._name2Motor = {}
        for motor in motors:
            self._name2Motor[motor.name] = motor

    def SetMotorTargetPosition(self, motorName, targetPosition):
        self._name2Motor[motorName].target_position = targetPosition
        self._name2Motor[motorName].Changed()
    
    def HandleCommand(self, commands: List[SerializableCommands]):
        for command in commands.motors:
            self.SetMotorTargetPosition(command.name,command.goal_position)
