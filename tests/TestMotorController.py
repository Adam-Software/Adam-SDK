import time
from adam_sdk.Controllers.MotorController import MotorController
from pymodbus.client.serial import ModbusSerialClient as ModbusClient

# Создаем клиент Modbus
client = ModbusClient(
            method="rtu", port="/dev/ttyUSB1", stopbits=1, bytesize=8, parity='N', baudrate=9600
        )
client.connect()

# Создаем экземпляры MotorController для каждого мотора     
front_left = MotorController(client, 22, 2, 3)  # Создание объекта мотора для переднего левого колеса
front_right = MotorController(client, 23, 0, 1, True)  # Создание объекта мотора для переднего правого колеса с инверсией
rear_left = MotorController(client, 22, 0, 1)  # Создание объекта мотора для заднего левого колеса
rear_right = MotorController(client, 23, 2, 3, True)  # Создание объекта мотора для заднего правого колеса с инверсией

# Устанавливаем скорость для каждого мотора -1 ~ 1
front_left.set_speed(0.1)
front_right.set_speed(0.1)
rear_left.set_speed(-0.1)
rear_right.set_speed(-0.1)

# Получаем значения регистров для каждого мотора с левой и правой стороны
registers1 = front_left.get_registers()
registers2 = front_right.get_registers()


# Очищаем регистры для каждого мотора с левой и право стороны
front_left.clear_registers()
front_right.clear_registers()

time.sleep(5)

# Устанавливаем скорость для каждого мотора -1 ~ 1
front_left.set_speed(0)
front_right.set_speed(0)
rear_left.set_speed(0)
rear_right.set_speed(0)