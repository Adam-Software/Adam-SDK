
from typing import Tuple

from pymodbus.client.serial import ModbusSerialClient as ModbusClient


class MecanumWheelMotor:
    def __init__(self, client: ModbusClient, address: int, direction_address: int, speed_address: int, inverse: bool = False):
        self.address = address
        self.direction_address = direction_address
        self.speed_address = speed_address
        self.speed = 0
        self.direction = 0
        self.client = client
        self.inverse = inverse

    def set_speed(self, speed: float) -> None:
        self.set_direction(speed >= 0)
        if self.speed == 0 and speed != 0:
            self.client.write_registers(self.speed_address, 1023, self.address)
        self.client.write_registers(
            self.speed_address, int(abs(speed)), self.address)
        self.speed = speed

    def set_direction(self, direction: bool) -> None:
        if self.inverse:
            direction = not direction
        if (self.direction != direction):
            self.direction = direction
            self.client.write_registers(
                self.direction_address, int(direction), self.address)

    def get_registers(self) -> None:
        read_reg = self.client.read_input_registers(0, 10, self.address)
        print(read_reg.registers)


class MecanumMoveController:
    def __init__(self):
        client = ModbusClient(method="rtu", port="/dev/ttyUSB1",
                              stopbits=1, bytesize=8, parity='N', baudrate=9600)
        client.connect()

        self.front_left = MecanumWheelMotor(client, 22, 2, 3)
        self.front_right = MecanumWheelMotor(client, 23, 0, 1, True)
        self.rear_left = MecanumWheelMotor(client, 22, 0, 1)
        self.rear_right = MecanumWheelMotor(client, 23, 2, 3, True)

    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        vx, vy = linear_velocity
        wz = angular_velocity

        front_left_speed = vx + vy + wz
        front_right_speed = vx - vy - wz
        rear_left_speed = vx - vy + wz
        rear_right_speed = vx + vy - wz

        max_speed = max(abs(front_left_speed), abs(front_right_speed), abs(
            rear_left_speed), abs(rear_right_speed))

        # normalize_speed
        if max_speed > 1:
            front_left_speed /= max_speed
            front_right_speed /= max_speed
            rear_left_speed /= max_speed
            rear_right_speed /= max_speed

        self.front_left.set_speed(front_left_speed * 1023)
        self.front_right.set_speed(front_right_speed * 1023)
        self.rear_left.set_speed(rear_left_speed * 1023)
        self.rear_right.set_speed(rear_right_speed * 1023)
