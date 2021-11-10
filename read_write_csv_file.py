from sortedcontainers import SortedDict

class read_write_csv_file():
	def read_csv_file(read_file_path):
		#data structure nested SortedDictionary
		treeMap = SortedDict()

		#read from file
		with open(read_file_path) as file:
			#ignore first line of file
			next(file)

			for line in file:
				#this variable indicates the number of 'identical values' for a 'key'
				count = 0

				new_key, new_value = (int(x) for x in line.split(','))

				
				if new_key in treeMap.keys(): #O(1) because of the internal hash function for SortedDict
					index = 0
					threshold = len(treeMap[new_key])
					for value, count in treeMap[new_key].items(): # It would be around O(1) since for each key usually (maybe by the way!) there are some values 
						if new_value == value:
							treeMap[new_key].update({new_value:(count + 1)}) #O(1)
							break

						index = index + 1 
						if index == threshold:
							treeMap[new_key].update({new_value:1}) #O(1)
							break


				else:
					treeMap.update({new_key:SortedDict({new_value:1})}) #O(1)
						
		return treeMap

	def write_csv_file(loci_file_path, output):
		textfile = open(loci_file_path, "w")
		textfile.write("position,coverage\n")
		for key, value in output.items():
			textfile.write('{}\n'.format(value))
		textfile.close()

