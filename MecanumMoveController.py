from nis import match
from typing import List, Tuple
from Models.IMoveController import IMoveController
from Models.Motor import Motor
import pymodbus
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.serial import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer

class MecanumWheelMotor:
    def __init__(self, client, address, directionAddress, speedAddress):
        self.address = address
        self.directionAddress = directionAddress
        self.speedAddress = speedAddress
        self.speed = 0
        self.direction = 0
        self.client = client

    def setSpeed(self, speed):
        if (self.speed == 0 and speed != 0):
            self.client.write_registers(self.speedAddress, 1023, self.address)
            self.client.write_registers(self.speedAddress, speed , self.address)
        elif speed == 0:
            self.client.write_registers(self.speedAddress, speed, self.address)
        elif self.speed != speed:
            self.client.write_registers(self.speedAddress, speed, self.address)
        self.speed = speed

    def setDirection(self, direction):
        self.direction = direction
        self.client.write_registers(
            self.directionAddress, self.direction, self.address)
    
    def getRegisters(self):
        read_reg = self.client.read_input_registers(0, 10, self.address)
        print(read_reg.registers)
        
class MecanumMoveController(IMoveController):
    def __init__(self) -> None:
        client = ModbusClient(method="rtu", port="/dev/ttyUSB1",
                      stopbits=1, bytesize=8, parity='N', baudrate=9600)
        client.connect()

        self.front_left = MecanumWheelMotor(
            client=client,
            address=22,
            directionAddress=2,
            speedAddress=3
        )
        self.front_right = MecanumWheelMotor(
            client=client,
            address=23,
            directionAddress=0,
            speedAddress=1
        )
        self.rear_left = MecanumWheelMotor(
            client=client,
            address=22,
            directionAddress=0,
            speedAddress=1
        )

        self.rear_right = MecanumWheelMotor(
            client=client,
            address=23,
            directionAddress=2,
            speedAddress=3
        )

    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        vx, vy = linear_velocity
        wz = angular_velocity

        front_left_speed = vx - vy - wz
        front_right_speed = vx + vy + wz
        rear_left_speed = vx + vy - wz
        rear_right_speed = vx - vy + wz

        max_speed = max(abs(front_left_speed), abs(front_right_speed), abs(rear_left_speed), abs(rear_right_speed))
        print(linear_velocity,angular_velocity)

        if max_speed > 1:
            front_left_speed /= max_speed
            front_right_speed /= max_speed
            rear_left_speed /= max_speed
            rear_right_speed /= max_speed
        print("front_left_speed ",front_left_speed,"front_right_speed ",front_right_speed,"rear_left_speed ",rear_left_speed,"rear_right_speed ",rear_right_speed)

        if(front_left_speed >= 0):
            self.front_left.setDirection(True)
            self.front_left.setSpeed(int(abs(front_left_speed)*1023))
        else:
            self.front_left.setDirection(False)
            self.front_left.setSpeed(int(abs(front_left_speed)*1023))

        if(front_right_speed >= 0):
            self.front_right.setDirection(False)
            self.front_right.setSpeed(int(abs(front_right_speed)*1023))
        else:
            self.front_right.setDirection(True)
            self.front_right.setSpeed(int(abs(front_right_speed)*1023))

        if(rear_left_speed >= 0):
            self.rear_left.setDirection(True)
            self.rear_left.setSpeed(int(abs(rear_left_speed)*1023))
        else:
            self.rear_left.setDirection(False)
            self.rear_left.setSpeed(int(abs(rear_left_speed)*1023))
        
        if(rear_right_speed >= 0):
            self.rear_right.setDirection(False)
            self.rear_right.setSpeed(int(abs(rear_right_speed)*1023))
        else:
            self.rear_right.setDirection(True)
            self.rear_right.setSpeed(int(abs(rear_right_speed)*1023))




