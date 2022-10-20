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
    motors: List[Motor]
    __name2Motor: Dict[str, Motor]
    __servoConnection = ServoConnection

    def __init__(self) -> None:
        self.motors = JsonParser.ReadConfig()
        self.__name2Motor = {}
        self.__servoConnection = ServoConnection()

        for motor in self.motors:
            motor.JointController.SetServoConnection(self.__servoConnection)
            self.__name2Motor[motor.name] = motor

    def __SetMotorTargetPosition(self, motorName, targetPosition, speed):
        self.__name2Motor[motorName].target_position = targetPosition
        joint: JointController
        if speed != 0:
            joint = self.__name2Motor[motorName].JointController
            joint.SetSpeed(speed)

    def __Update(self):
        joint: JointController
        for motor in self.__name2Motor.values():
            joint = motor.JointController
            joint.RotateTo(motor.target_position)
            motor.present_position = joint.GetPresentPosition()
        self.__servoConnection.InsertCommandServo()

    def HandleCommand(self, commands: SerializableCommands):
        for command in commands.motors:
            self.__SetMotorTargetPosition(
                command.name, command.goal_position, command.speed)
        self.__Update()
