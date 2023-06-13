import time
import os
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from adam_sdk import AdamManager


if __name__ == '__main__':

    adam_manager = AdamManager()
    #linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    #angular_velocity = 0.0         # без вращения вокруг оси Z

    #linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    #angular_velocity = 0.0         # без вращения вокруг оси Z

    #forward
    adam_manager.move((0.0, 1.0), 0.0)
    time.sleep(0.05)

    #back
    adam_manager.move((0.0, -1.0), 0.0)
    time.sleep(0.05)

    #right
    adam_manager.move((1.0, 0.0), 0.0)
    time.sleep(0.05)

    #left
    adam_manager.move((-1.0, 0.0), 0.0)
    time.sleep(0.05)

    #left and forward
    adam_manager.move((-1.0, 1.0), 0.0)
    time.sleep(0.05)

    #rigt and forward
    adam_manager.move((1.0, 1.0), 0.0)
    time.sleep(0.05)

    #back and left
    adam_manager.move((-1.0, -1.0), 0.0)
    time.sleep(0.05)

    #back and right
    adam_manager.move((1.0, -1.0), 0.0)
    time.sleep(0.05)

    #u-turn to the right
    adam_manager.move((0.0, 0.0), 1.0)
    time.sleep(0.05)

    #u-turn to the left
    adam_manager.move((0.0, 0.0), -1.0)
    time.sleep(0.05)

    adam_manager.move((0.0, 0.0), 0.0)
