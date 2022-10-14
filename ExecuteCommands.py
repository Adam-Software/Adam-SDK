from InterpolationMethods import InterpolationMethods
from JsonDeserialize import JsonDeserialize
from JsonParser import JsonParser


class ExecuteCommands:
    def __init__(self, jsonCommand):
        self.parsingFile(jsonCommand)

    def parsingFile(self, jsonCommand):
        data = JsonParser.ReadExamplesCommand(jsonCommand)
        servos = JsonDeserialize.commands(data)
        self.recognizeServos(servos)

    def recognizeServos(self, servos):

        position = []
        for servo in servos:
            idServo = self.servoNameToId(servo.name)
            goalPosition = servo.goalPosition
            position.append(self.calculateGoalPosition(idServo, goalPosition))

        print(position)

    @staticmethod
    def servoNameToId(name):
        return ({
            name == 'Head': 1,
            name == 'Neck': 2
        })[False]

    @staticmethod
    def calculateGoalPosition(idServo, goalPosition):
        calculate = InterpolationMethods()
        return ({
            idServo == 1: calculate.CalcHead(goalPosition),
            idServo == 2: calculate.CalcNeck(goalPosition)
        })[False]
