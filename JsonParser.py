import json


class JsonParser:

    @staticmethod
    def ReadPositionRange():
        f = open('position_range.json')
        data = json.load(f)
        f.close()

        return data

    @staticmethod
    def ReadExamplesCommand(filename):
        f = open(f'examples/{filename}')
        data = json.load(f)
        f.close()

        return data
