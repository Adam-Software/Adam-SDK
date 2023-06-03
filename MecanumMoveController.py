from typing import Tuple
from pymodbus.client.serial import ModbusSerialClient as ModbusClient


class MecanumWheelMotor:
    def __init__(
        self,
        client: ModbusClient,
        address: int,
        direction_address: int,
        speed_address: int,
        inverse: bool = False,
    ):
        self.address = address
        self.direction_address = direction_address
        self.speed_address = speed_address
        self.speed = 0
        self.direction = 0
        self.client = client
        self.inverse = inverse

    def set_speed(self, speed: float) -> None:
        self.set_direction(speed >= 0)
        speed_value = self.calculate_speed_value(speed)
        self.handle_initial_speed_condition(speed_value)
        self.write_speed_registers(speed_value)

    def calculate_speed_value(self, speed: float) -> int:
        if speed >= 0.1:
            return int(524 + speed * 524)
        return 0

    def handle_initial_speed_condition(self, speed_value: int) -> None:
        if self.speed == 0 and speed_value != 0:
            self.client.write_registers(self.speed_address, 1048, self.address)

    def write_speed_registers(self, speed_value: int) -> None:
        self.client.write_registers(
            self.speed_address, abs(speed_value), self.address)
        self.speed = speed_value

    def set_direction(self, direction: bool) -> None:
        if self.inverse:
            direction = not direction
        if self.direction != direction:
            self.direction = direction
            self.client.write_registers(
                self.direction_address, int(direction), self.address)

    def get_registers(self) -> None:
        read_reg = self.client.read_input_registers(0, 10, self.address)
        print(read_reg.registers)


class MecanumMoveController:
    def __init__(self):
        client = ModbusClient(
            method="rtu", port="/dev/ttyUSB1", stopbits=1, bytesize=8, parity='N', baudrate=9600
        )
        client.connect()

        self.front_left = MecanumWheelMotor(client, 22, 2, 3)
        self.front_right = MecanumWheelMotor(client, 23, 0, 1, True)
        self.rear_left = MecanumWheelMotor(client, 22, 0, 1)
        self.rear_right = MecanumWheelMotor(client, 23, 2, 3, True)

    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        vx, vy = linear_velocity
        wz = angular_velocity

        speeds = [
            vx + vy + wz,
            vx - vy - wz,
            vx - vy + wz,
            vx + vy - wz,
        ]

        max_speed = max(map(abs, speeds))

        if max_speed > 1:
            speeds = [speed / max_speed for speed in speeds]

        self.front_left.set_speed(speeds[0])
        self.front_right.set_speed(speeds[1])
        self.rear_left.set_speed(speeds[2])
        self.rear_right.set_speed(speeds[3])
