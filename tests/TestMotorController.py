import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import time
from adam_sdk.Controllers.MotorController import MotorController
from pymodbus.client.serial import ModbusSerialClient as ModbusClient

# Создаем клиент Modbus
client = ModbusClient(
    method="rtu", port="/dev/ttyUSB1", stopbits=1, bytesize=8, parity='N', baudrate=9600
)
client.connect()

# Создаем экземпляры MotorController для каждого мотора
# Создание объекта мотора для переднего левого колеса
front_left = MotorController(client, 22, 2, 3)
# Создание объекта мотора для переднего правого колеса с инверсией
front_right = MotorController(client, 23, 0, 1, True)
# Создание объекта мотора для заднего левого колеса
rear_left = MotorController(client, 22, 0, 1)
# Создание объекта мотора для заднего правого колеса с инверсией
rear_right = MotorController(client, 23, 2, 3, True)

# Очищаем регистры для каждого мотора с левой и правой стороны
front_left.clear_registers()
front_right.clear_registers()

# Устанавливаем скорость для каждого мотора -1 ~ 1
front_left.set_speed(0.1)
front_right.set_speed(0.1)
rear_left.set_speed(-0.1)
rear_right.set_speed(-0.1)

# Получаем значения регистров для каждого мотора с левой и правой стороны
registers1 = front_left.get_registers()
registers2 = front_right.get_registers()

time.sleep(5)

# Устанавливаем скорость для каждого мотора -1 ~ 1
front_left.set_speed(0)
front_right.set_speed(0)
rear_left.set_speed(0)
rear_right.set_speed(0)

# Или берем из библиотеки готовый присет MecanumMoveController

from adam_sdk.Controllers.MecanumMoveController import MecanumMoveController

move_controller = MecanumMoveController()

# Очищаем регистры для каждого мотора с левой и правой стороны
move_controller.front_left.clear_registers()
move_controller.front_right.clear_registers()

# Устанавливаем скорость для каждого мотора -1 ~ 1
move_controller.front_left.set_speed(0.1)
move_controller.front_right.set_speed(0.1)
move_controller.rear_left.set_speed(0.1)
move_controller.rear_right.set_speed(0.1)

# Получаем значения регистров для каждого мотора с левой и правой стороны
registers1 = move_controller.front_left.get_registers()
registers2 = move_controller.front_right.get_registers()

time.sleep(5)

# Устанавливаем скорость для каждого мотора -1 ~ 1
move_controller.front_left.set_speed(0)
move_controller.front_right.set_speed(0)

# вариант три, с использованием AdamManager
from adam_sdk import AdamManager
adam_manager = AdamManager()
# Устанавливаем скорость для каждого мотора -1 ~ 1

adam_manager.move_controller.front_left.set_speed(0.1)
adam_manager.move_controller.front_right.set_speed(0.1)
adam_manager.move_controller.rear_left.set_speed(0.1)
adam_manager.move_controller.rear_right.set_speed(0.1)


# Очищаем регистры для каждого мотора с левой и право стороны
adam_manager.move_controller.front_left.clear_registers()
adam_manager.move_controller.front_right.clear_registers()

# Получаем значения регистров для каждого мотора с левой и правой стороны
registers1 = adam_manager.move_controller.front_left.get_registers()
registers2 = adam_manager.move_controller.front_right.get_registers()

time.sleep(5)

# Устанавливаем скорость для каждого мотора -1 ~ 1
adam_manager.move_controller.front_left.set_speed(0)
adam_manager.move_controller.front_right.set_speed(0)
adam_manager.move_controller.rear_left.set_speed(0)
adam_manager.move_controller.rear_right.set_speed(0)
move_controller.rear_left.set_speed(0)
move_controller.rear_right.set_speed(0)
