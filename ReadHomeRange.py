import json


class ReadHomeRange:

    @staticmethod
    def Read():
        f = open('position_range.json')
        data = json.load(f)
        f.close()

        return data
