import unittest
from main import *

class TestCase_read_CSV_file(unittest.TestCase):
    def test_main(self):
        output = main("data\\Unit_Test_Read.csv", "data\\Unit_Test_Write.csv")
        self.assertEqual(output, {'12':1})

if __name__ == '__main__':
    unittest.main()