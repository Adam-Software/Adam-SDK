from pymodbus.client.serial import ModbusSerialClient as ModbusClient

class MotorController:
    def __init__(
        self,
        client: ModbusClient,
        address: int,
        direction_address: int,
        speed_address: int,
        inverse: bool = False,
    ):
        self.address = address  # Адрес модуля мотора
        self.direction_address = direction_address  # Адрес регистра для установки направления движения
        self.speed_address = speed_address  # Адрес регистра для установки скорости движения
        self.speed = 0  # Текущая установленная скорость
        self.direction = 0  # Текущее установленное направление
        self.client = client  # Клиент Modbus
        self.inverse = inverse  # Флаг инверсии направления движения

    def set_speed(self, speed: float) -> None:
        self.set_direction(speed >= 0)  # Установка направления движения в зависимости от знака скорости
        speed_value = self.calculate_speed_value(speed)  # Вычисление значения скорости
        self.handle_initial_speed_condition(speed_value)  # Обработка начального условия скорости
        self.write_speed_registers(speed_value)  # Запись значения скорости в регистр

    def calculate_speed_value(self, speed: float) -> int:
        if abs(speed) > 0:
            return int(524 + abs(speed) * 499)  # Вычисление значения скорости в соответствии с диапазоном
        return 0  # Если скорость меньше 0.1, то установка значения скорости в 0

    def handle_initial_speed_condition(self, speed_value: int) -> None:
        if self.speed == 0 and speed_value != 0:
            self.client.write_registers(self.speed_address, 1023, self.address)  # Запись значения инициализации скорости

    def write_speed_registers(self, speed_value: int) -> None:
        self.client.write_registers(self.speed_address, speed_value, self.address)  # Запись значения скорости в регистр
        self.speed = speed_value  # Обновление текущей установленной скорости

    def set_direction(self, direction: bool) -> None:
        if self.inverse:
            direction = not direction  # Инвертирование направления движения, если установлен флаг инверсии
        #if self.direction != direction:
        self.client.write_registers(self.direction_address, int(direction), self.address)  # Запись значения направления движения в регистр
        self.direction = direction
    def get_registers(self) -> None:
        read_reg = self.client.read_input_registers(0, 10, self.address)  # Чтение регистров из устройства
        print(read_reg.registers)  # Вывод прочитанных значений регистров
