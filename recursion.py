import numpy as np


array = list(np.random.randint(0, 100, 10))
print(f'Initial array: {array}\nSum = {sum(array)}\nLength = {len(array)}\nMax = {max(array)}')

# recursive sum
def rec_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array.pop(0) + rec_sum(array)


print(f'Recursive sum = {rec_sum(array.copy())}')


# recursive length
def rec_len(array):
    if array == list():
        return 0
    else:
        array.pop(0)
        return 1 + rec_len(array)

print(f'Recursive length = {rec_len(array.copy())}')


# recursive max
def rec_max(array):
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return array.pop(0)
    else:
        if array[0] > array[1]:
            array.pop(1)
        else:
            array.pop(0)
        return rec_max(array)

print(f'Recursive max = {rec_max(array.copy())}')


# recursive binary search
def rec_binary_search(array, item):
    if array[0] <= item <= array[-1]:
        mid = len(array) // 2 
        if item == array[mid]:
            return item
        elif item < array[mid]:
            return rec_binary_search(array[:mid], item)
        else:
            return rec_binary_search(array[mid:], item)

print(
    rec_binary_search(range(19), 18),
    rec_binary_search(range(100), 101),
    rec_binary_search(range(12, 5248, 2), 101),
    rec_binary_search(range(1024), 260),
    sep='\n'
)