import unittest
from read_write_csv_file import *

class TestCase_read_CSV_file(unittest.TestCase):
    def test_read_csv_file(self):
        treeMap = read_write_csv_file.read_csv_file("data\\Unit_Test_Read.csv")
        self.assertEqual(treeMap, {1:{9:1},2:{9:2},3:{7:1,8:1,9:1}})

if __name__ == '__main__':
    unittest.main()