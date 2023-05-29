import sys
import os
import json
from JointController import JointController
from Models.Joint import Joint
from Models.Motor import Motor

current = os.path.dirname(os.path.realpath(__file__))


class JsonParser:

    @staticmethod
    def _ReadConfig():
        f = open(f'{current}/examples/position_range.json')
        data = json.load(f)
        f.close()

        return data

    @staticmethod
    def ReadCommand():
        f = open(f'{current}/examples/SerializableCommandHead.json')
        data = json.load(f)
        f.close()

        return data

    @staticmethod
    def ParseConfigJson():
        config = JsonParser._ReadConfig()
        motors = []
        for element in config:
            motors.append(Motor(name=element['name'],
                                target_position=element['target_position'],
                                JointController=JointController(joint=Joint(element['joint']['lover_limit'],
                                                                            element['joint']['upper_limit'],
                                                                            element['joint']['speed'],
                                                                            element['joint']['id']))))
        return motors
