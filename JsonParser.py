
import json


class JsonParser:

    @staticmethod
    def ReadConfig():
        f = open('position_range.json')
        data = json.load(f)
        f.close()

        return data