from adam_sdk import AdamManager
import time

if __name__ == '__main__':

    adamController = AdamManager()
    #linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    #angular_velocity = 0.0         # без вращения вокруг оси Z

    #linear_velocity = (1.0, 0.0)  # движение вперед по оси X
    #angular_velocity = 0.0         # без вращения вокруг оси Z

    #forward
    adamController.move((0.0, 1.0), 0.0)
    time.sleep(0.05)

    #back
    adamController.move((0.0, -1.0), 0.0)
    time.sleep(0.05)

    #right
    adamController.move((1.0, 0.0), 0.0)
    time.sleep(0.05)

    #left
    adamController.move((-1.0, 0.0), 0.0)
    time.sleep(0.05)

    #left and forward
    adamController.move((-1.0, 1.0), 0.0)
    time.sleep(0.05)

    #rigt and forward
    adamController.move((1.0, 1.0), 0.0)
    time.sleep(0.05)

    #back and left
    adamController.move((-1.0, -1.0), 0.0)
    time.sleep(0.05)

    #back and right
    adamController.move((1.0, -1.0), 0.0)
    time.sleep(0.05)

    #u-turn to the right
    adamController.move((0.0, 0.0), 1.0)
    time.sleep(0.05)

    #u-turn to the left
    adamController.move((0.0, 0.0), -1.0)
    time.sleep(0.05)

    adamController.move((0.0, 0.0), 0.0)
