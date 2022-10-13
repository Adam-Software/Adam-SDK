import unittest
from JsonParser import JsonParser


class JsonParserTest(unittest.TestCase):

    def testReadPositionRange(self):
        data = JsonParser.ReadPositionRange()
        self.assertEqual(data['HeadRange'], [2548, 1548, 1800, 2300])

    def testReadExamplesCommand(self):
        data = JsonParser.ReadExamplesCommand('SerializableCommands.json')
        print(data)

if __name__ == '__main__':
    unittest.main()
