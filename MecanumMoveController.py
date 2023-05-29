from typing import List, Tuple
from Models.IMoveController import IMoveController
from Models.Motor import Motor


class MecanumMoveController(IMoveController):
    def move(self, linear_velocity: Tuple[float, float], angular_velocity: float) -> None:
        vx, vy = linear_velocity
        wz = angular_velocity

        # Порядок следующим образом: [front_left, front_right, rear_left, rear_right]
        wheel_speeds = [
            vx - vy - wz,  # front_left
            vx + vy + wz,  # front_right
            vx + vy - wz,  # rear_left
            vx - vy + wz   # rear_right
        ]
        print("Wheel speeds:")
        print("front_left: ", wheel_speeds[0])
        print("front_right: ", wheel_speeds[1])
        print("rear_left: ", wheel_speeds[2])
        print("rear_right: ", wheel_speeds[3])