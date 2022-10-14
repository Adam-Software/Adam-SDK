import unittest

from ExecuteCommands import ExecuteCommands


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ExecuteCommands('SerializableCommandHead.json')

        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
