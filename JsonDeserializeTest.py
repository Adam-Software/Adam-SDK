import unittest

from JsonDeserialize import JsonDeserialize
from JsonParser import JsonParser


class JsonDeserializeTest(unittest.TestCase):

    def testHeadCommandDeserialize(self):
        data = JsonParser.ReadExamplesCommand('SerializableCommandHead.json')
        servos = JsonDeserialize.commands(data)

        for servo in servos:
            self.assertEqual(servo.name, 'Head')
            self.assertEqual(servo.goalPosition, -0.0019112753216177225)

        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
