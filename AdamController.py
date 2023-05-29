from JsonParser import JsonParser
from MecanumMoveController import MecanumMoveController
from Models.Motor import Motor
from typing import Dict, List, Tuple
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
        self.nameToMotor = self._createNameToMotorMapping()
        self.servoConnection = ServoConnection()
        self._initializeJointControllers()
        self.moveController = MecanumMoveController()

        for motor in self.motors:
            motor.start_position = motor.present_position
        self._update()

    def _createNameToMotorMapping(self) -> Dict[str, Motor]:
        return {motor.name: motor for motor in self.motors}

    def _initializeJointControllers(self):
        for motor in self.motors:
            motor.JointController.SetServoConnection(self.servoConnection)

    def _setMotorTargetPosition(self, motorName, targetPosition, speed):
        motor = self.nameToMotor[motorName]
        motor.target_position = targetPosition

        if speed != 0:
            joint = motor.JointController
            joint.SetSpeed(speed)

    def _update(self):
        for motor in self.nameToMotor.values():
            joint = motor.JointController
            joint.RotateTo(motor.target_position)
            motor.present_position = joint.GetPresentPosition()

        self.servoConnection.InsertCommandServo()

    def HandleCommand(self, commands: SerializableCommands):
        for command in commands.motors:
            self._setMotorTargetPosition(
                command.name, command.goal_position, command.speed)
        self._update()

    def ReturnToStartPosition(self):
        for motor in self.motors:
            motor.target_position = motor.start_position
        self._update()
    
    def Move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        self.moveController.move(linear_velocity, angular_velocity)