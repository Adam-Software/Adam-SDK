from JsonParser import JsonParser
from Models.Motor import Motor
from typing import Dict, List
from JointController import JointController
from Models.SerializableCommands import SerializableCommands
from ServoConnection import ServoConnection


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AdamController(metaclass=MetaSingleton):
    def __init__(self) -> None:
        self.motors = JsonParser.ParseConfigJson()
        self.__name2Motor = self._create_name_to_motor_mapping()
        self.__servoConnection = ServoConnection()
        self._initialize_joint_controllers()

    def _create_name_to_motor_mapping(self) -> Dict[str, Motor]:
        return {motor.name: motor for motor in self.motors}

    def _initialize_joint_controllers(self):
        for motor in self.motors:
            motor.JointController.SetServoConnection(self.__servoConnection)

    def _set_motor_target_position(self, motorName, targetPosition, speed):
        motor = self.__name2Motor[motorName]
        motor.target_position = targetPosition

        if speed != 0:
            joint = motor.JointController
            joint.SetSpeed(speed)

    def _update(self):
        for motor in self.__name2Motor.values():
            joint = motor.JointController
            joint.RotateTo(motor.target_position)
            motor.present_position = joint.GetPresentPosition()

        self.__servoConnection.InsertCommandServo()

    def HandleCommand(self, commands: SerializableCommands):
        for command in commands.motors:
            self._set_motor_target_position(
                command.name, command.goal_position, command.speed)
        self._update()
