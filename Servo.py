class Servo:
    def __init__(self, name, goalPosition):
        self.__name = name
        self.__goalPosition = goalPosition

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def goalPosition(self):
        return self.__goalPosition

    @goalPosition.setter
    def goalPosition(self, goalPosition):
        self.__goalPosition = goalPosition
