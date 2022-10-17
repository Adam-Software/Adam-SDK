
import json


class JsonParser:

    @staticmethod
    def ReadConfig():
        f = open('examples\position_range.json')
        data = json.load(f)
        f.close()

        return data

    @staticmethod
    def ReadCommand():
        f = open('examples\SerializableCommandHead.json')
        data = json.load(f)
        f.close()

        return data
