

def binary_search(array: list, item: int) -> int | None:
	low = 0
	high = len(array) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = array[mid]

		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1

	return None
