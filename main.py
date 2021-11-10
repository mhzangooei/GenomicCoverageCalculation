from typing import Dict
from read_write_csv_file import *
from binary_search import *
from sortedcontainers import SortedDict


def main(read_file_path, loci_file_path):	
	#fill nested StoredDictionary
	treeMap = read_write_csv_file.read_csv_file(read_file_path)

	output = dict()
	index_loci_row = 0

	with open(loci_file_path) as file:
		#ignore first line of file
		next(file)

		for line in file:
			coverage = 0
			new_key = line.split(',')[0]
			last_index_search_for_key = binary_search.binary_search_key(int(new_key), treeMap)
			
			for x in range(0, last_index_search_for_key + 1):
				first_index_search_for_value = binary_search.binary_search_value(int(new_key) - treeMap.keys()[x], treeMap[treeMap.keys()[x]])
				for y in range(first_index_search_for_value, len(treeMap[treeMap.keys()[x]])):
						coverage = coverage + (treeMap[treeMap.keys()[x]]).values()[y] 
			output.update({index_loci_row: str(new_key) + "," + str(coverage)})
			index_loci_row = index_loci_row + 1

	read_write_csv_file.write_csv_file(loci_file_path, output)
	return output


if __name__ == "__main__":
	main("data\\reads.csv", "data\\loci.csv")