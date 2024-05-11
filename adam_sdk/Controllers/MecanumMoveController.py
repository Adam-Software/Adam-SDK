from typing import Tuple
from .MotorController import MotorController
from pymodbus.client.serial import ModbusSerialClient as ModbusClient

class MecanumMoveController:
    def __init__(self):
        # Инициализация Modbus клиента для взаимодействия с контроллерами моторов
        client = ModbusClient(
            method="rtu", port="/dev/ttyS0", stopbits=1, bytesize=8, parity='N', baudrate=76800
        )
        client.connect()
        
        self.front_left = MotorController(client, 22, 2, 3)  # Создание объекта мотора для переднего левого колеса
        self.front_right = MotorController(client, 23, 0, 1, True)  # Создание объекта мотора для переднего правого колеса с инверсией
        self.rear_left = MotorController(client, 22, 0, 1)  # Создание объекта мотора для заднего левого колеса
        self.rear_right = MotorController(client, 23, 2, 3, True)  # Создание объекта мотора для заднего правого колеса с инверсией

        # Инициализация переменных для линейной и угловой скоростей
        self.vx = self.vy = self.wz = 0


    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        self.vx, self.vy = linear_velocity
        self.wz = angular_velocity

        speeds = [
                    self.vy + self.vx + self.wz,
                    self.vy - self.vx - self.wz,
                    self.vy - self.vx + self.wz,
                    self.vy + self.vx - self.wz
                ]
        max_speed = max(map(abs, speeds))
        if max_speed > 1:
            speeds = [speed / max_speed for speed in speeds]
                
        for motor, speed in zip([self.front_left, self.front_right, self.rear_left, self.rear_right], speeds):
            motor.set_speed(speed)