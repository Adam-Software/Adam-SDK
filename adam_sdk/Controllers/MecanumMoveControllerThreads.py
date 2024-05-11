from typing import Tuple
from .MotorController import MotorController
from pymodbus.client.serial import ModbusSerialClient as ModbusClient
from threading import Thread, Lock
import time
class MecanumMoveControllerThreads:
    def __init__(self):

        self.lock = Lock()  # Добавляем блокировку для синхронизации

        self.changed = False
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
        


        # Создание и запуск потока для выполнения управления моторами
        self.thread_intent = Thread(target=self._thread_move)
        self.thread_intent.daemon = True  # Устанавливаем фоновый режим для потока
        self.thread_intent.start()

    def _thread_move(self):
       while True:
            with self.lock:  # Захватываем блокировку
                if not self.changed:
                    time.sleep(0)
                    continue
                # Расчет скоростей для каждого колеса на основе линейной и угловой скоростей
                speeds = [
                    self.vy + self.vx + self.wz,
                    self.vy - self.vx - self.wz,
                    self.vy - self.vx + self.wz,
                    self.vy + self.vx - self.wz
                ]
                # Нормализация скоростей, если максимальная скорость больше 1
                max_speed = max(map(abs, speeds))
                if max_speed > 1:
                    speeds = [speed / max_speed for speed in speeds]
                # Установка скоростей для каждого мотора    
                for motor, speed in zip([self.front_left, self.front_right, self.rear_left, self.rear_right], speeds):
                    motor.set_speed(speed)

                self.changed = False
            

    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        with self.lock:  # Захватываем блокировку
            self.vx, self.vy = linear_velocity
            self.wz = angular_velocity
            self.changed = True