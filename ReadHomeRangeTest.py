import unittest
from ReadHomeRange import ReadHomeRange


class ReadHomeRangeTest(unittest.TestCase):

    def testRead(self):
        reader = ReadHomeRange
        data = reader.Read()
        self.assertEqual(data['HeadRange'], [2548, 1548, 1800, 2300])


if __name__ == '__main__':
    unittest.main()
