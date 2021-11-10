
class binary_search():

    #binary search for key on nested Sorted Dictionary
    def binary_search_key(new_key, sorted_Dict):

        first_key = 0
        last_key = len(sorted_Dict)-1
        found = False

        if sorted_Dict.keys()[first_key] == new_key:
            found = False
            mid_key = first_key
        if  sorted_Dict.keys()[last_key] == new_key :
            found = False
            mid_key = last_key

        while (first_key<=last_key and not found):
            mid_key = (first_key + last_key)//2
            if sorted_Dict.keys()[mid_key] == new_key :
                return mid_key
            else:
                if new_key < sorted_Dict.keys()[mid_key]:
                    last_key = mid_key - 1
                    if last_key < 0:
                        return -1
                    
                else:
                    first_key = mid_key + 1
                    if len(sorted_Dict) <= first_key:
                        return len(sorted_Dict) - 1

        if sorted_Dict.keys()[mid_key] <= new_key:
            return mid_key
        else:
            return mid_key - 1

     #binary search for value on nested Sorted Dictionary
    def binary_search_value(new_value, sorted_Dict):

        first_value = 0
        last_value = len(sorted_Dict)-1
        found = False

        if sorted_Dict.keys()[first_value] == new_value:
            found = False
            mid_value = first_value
        if  sorted_Dict.keys()[last_value] == new_value :
            found = False
            mid_value = last_value

        while (first_value<=last_value and not found):
            mid_value = (first_value + last_value)//2
            if sorted_Dict.keys()[mid_value] == new_value :
                return mid_value
            else:
                if new_value < sorted_Dict.keys()[mid_value]:
                    last_value = mid_value - 1
                    if last_value < 0:
                        return 0
                    
                else:
                    first_value = mid_value + 1
                    if len(sorted_Dict) <= first_value:
                        return len(sorted_Dict)

        if sorted_Dict.keys()[mid_value] >= new_value:
            return mid_value
        else:
            return mid_value + 1