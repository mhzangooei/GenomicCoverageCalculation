import unittest
from sortedcontainers import SortedDict
from binary_search import *

class TestCase_read_CSV_file(unittest.TestCase):
    def test_binary_search(self):	    
        #for example suppose Data {Start (Or key):Length (Or value)} => {3:7, 3:9, 3:8, 2:9, 2:9, 1:9} then we construct a nested sorted dictionary
        treeMap = SortedDict()
        treeMap.update({3:SortedDict({7:1, 9:1, 8:1}),2:SortedDict({9:2}),1:SortedDict({9:1})}) # it sorts: {1:{9:1}, 2{9:2, 3{7:1, 8:1, 9:1}}}

        last_index_search_for_key = binary_search.binary_search_key(2, treeMap) #for 2, last index of keys is 1
        first_index_search_for_value = binary_search.binary_search_value(5,treeMap[treeMap.keys()[2]]) # for value 8 of 3, first index is 0 => binary_search_value(8-3,{7:1,8:1, 9:1})

        self.assertEqual(last_index_search_for_key, 1)
        self.assertEqual(first_index_search_for_value, 0)


if __name__ == '__main__':
    unittest.main()