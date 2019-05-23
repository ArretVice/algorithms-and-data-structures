import numpy as np 


def binary_search(correct_value, value_range=range(100)):
    low = 0
    high = len(value_range) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if value_range[mid] == correct_value:
            print(f'Your number was {value_range[mid]} at position {mid}')
            break
        elif value_range[mid] < correct_value:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print('Value was not found')

if __name__ == "__main__":
    binary_search(18)
    binary_search(101)
    binary_search(101, range(12, 5248, 2))
    binary_search(260, range(1024))
