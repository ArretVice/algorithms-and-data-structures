import numpy as np 

# import selection_sort


array = list(np.random.randint(0, 100, size=10))
print(array)

def quicksort(array):
    if len(array) < 2:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        pivot = array.pop(0)
        less_array = [x for x in array if x <= pivot]
        greater_array = [x for x in array if x > pivot]
        return quicksort(less_array) + [pivot] + quicksort(greater_array)

print(f'Sorted array: {quicksort(array.copy())}')

# size = 8000
# print(f'Time for size {size} array (selection sort): {(selection_sort.calculate_time(size, selection_sort.selection_sort)):.6f}')
# print(f'Time for size {size} array (quicksort): {(selection_sort.calculate_time(size, quicksort)):.6f}')