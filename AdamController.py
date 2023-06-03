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
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AdamController(metaclass=MetaSingleton):
    def __init__(self) -> None:
        self.motors = self._parseConfigJson()
        self.name_to_motor = self._create_name_to_motor_mapping()
        self.servo_connection = ServoConnection()
        self._initialize_joint_controllers()
        self.move_controller = MecanumMoveController()

        for motor in self.motors:
            motor.start_position = motor.target_position

        self._update()

    def _parseConfigJson(self) -> List[Motor]:
        return JsonParser.parse_config_json()

    def _create_name_to_motor_mapping(self) -> Dict[str, Motor]:
        return {motor.name: motor for motor in self.motors}

    def _initialize_joint_controllers(self):
        for motor in self.motors:
            motor.joint_controller.set_servo_connection(self.servo_connection)

    def _set_motor_target_position(self, motor_name: str, target_position: float, speed: float):
        motor = self.name_to_motor[motor_name]
        motor.target_position = target_position

        if speed != 0:
            joint = motor.joint_controller
            joint.set_speed(speed)

    def _update(self):
        for motor in self.name_to_motor.values():
            joint = motor.joint_controller
            joint.rotate_to(motor.target_position)
            motor.present_position = joint.get_present_position()

        self.servo_connection.insert_command_servo()

    def handle_command(self, commands: SerializableCommands):
        for command in commands.motors:
            self._set_motor_target_position(
                command.name, command.goal_position, command.speed)
        self._update()

    def return_to_start_position(self):
        for motor in self.motors:
            motor.target_position = motor.start_position
        self._update()

    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        self.move_controller.move(linear_velocity, angular_velocity)
