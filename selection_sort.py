import numpy as np 
from time import time


def find_smallest(array):
    smallest_index = 0
    smallest_item = array[0]
    for index, item in enumerate(array):
        if smallest_item > item:
            smallest_item = item
            smallest_index = index
    return smallest_index

def selection_sort(array):
    result = []
    arr = array.copy()
    while len(arr) != 0:
        result.append(arr.pop(find_smallest(arr)))
    return result

def calculate_time(size, func):
    array = list(np.random.randint(0, 100, size=size))
    t0 = time()
    sorted_array = func(array)
    t1 = time()
    return t1 - t0

if __name__ == '__main__':
    # print(f'Unsorted array: {array}')
    # smallest_index = find_smallest(array)
    # print(f'Smallest element of array at index: {smallest_index}, value: {array[smallest_index]}')
    # print(f'Sorted array: {sorted_array}')
    size1 = 2000
    print(f'Time for size {size1} array: {(calculate_time(size1, selection_sort)):.6f}')
    size2 = 4000
    print(f'Time for size {size2} array: {(calculate_time(size2, selection_sort)):.6f}')
