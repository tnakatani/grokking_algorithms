"""ch2_selection_sort.py Selection Sort"""
import numpy as np


def find_smallest(array):
    """Finds the smallest element in an array"""
    # stores smallest value, and its index
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            print("smallest found", smallest)
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    """Sorts an array by finding the smallest element in the array and adds it
    to the new array"""
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


if __name__ == "__main__":
    test = np.random.choice(100, 100, replace=False).tolist()
    print("Initial array: ", test)
    selection_sort(test)
