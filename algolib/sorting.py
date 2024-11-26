

def find_smallest_index(array: list):
	smallest = array[0]
	smallest_index = 0
	for i in range(1, len(array)):
		if array[i] < smallest:
			smallest = array[i]
			smallest_index = i
	return smallest_index


def selection_sort(arr: list):
	new_arr = []
	copied_arr = list(arr)
	for i in range(len(copied_arr)):
		smallest = find_smallest_index(copied_arr)
		new_arr.append(copied_arr.pop(smallest))

	return new_arr
