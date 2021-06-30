"""Ch. 4 Quicksort"""


def my_sum(_list: list):
    """Given a list, sum its items recursively"""
    if len(_list) == 0:
        return 0
    else:
        return _list.pop() + my_sum(_list)


def my_sum_solution(_list: list):
    """Given a list, sum its items recursively"""
    if not _list:
        return 0
    return _list[0] + sum(_list[1:])


def my_count(nums: list):
    """Given a list, count its items recursively"""
    if len(nums) == 0:
        return 0
    else:
        nums.pop()
        return 1 + my_count(nums)


def my_count_solution(_list: list):
    """Given a list, count its items recursively"""
    if not _list:
        return 0
    else:
        return 1 + my_count_solution(_list[1:])


def my_max(_list: list):
    """Given a list of numbers, return its largest number
    This solution doesn't qualify, since it's using max()
    """
    if not _list:
        return 0
    else:
        return max(_list[0], my_max(_list[1:]))


def my_max_solution(_list: list):
    """Given a list of numbers, return its largest number"""
    if len(_list) == 0:
        return None
    if len(_list) == 1:
        return _list[0]
    else:
        sub_max = my_max_solution(_list[1:])
        return _list[0] if _list[0] > sub_max else sub_max


def quick_sort(_list: list):
    """Given a list of numbers, sort them from smallest to largest recursively"""
    # Base case: if array has 0 or 1 element, they are already sorted
    if len(_list) < 2:
        return _list
    else:
        # recusive case; pick a pivot
        pivot = _list[0]
        # get sub-array of all elements smaller than pivot
        less = [i for i in _list[1:] if i <= pivot]
        # get sub-array of all elements greater than pivot
        greater = [i for i in _list[1:] if i > pivot]
        # call quick_sort on the sub-arrays
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    # sum
    assert my_sum([0, 1, 2, 3, 4, 5]) == 15
    assert my_sum_solution([0, 1, 2, 3, 4, 5]) == 15

    # count
    assert my_count(["a", "b", "c"]) == 3
    assert my_count_solution(["a", "b", "c"]) == 3

    # max
    assert my_max([0, 10000, 2, 300, 4, 100]) == 10000
    assert my_max_solution([0, 10000, 2, 300, 4, 100]) == 10000

    # quicksort
    assert quick_sort([5, 6, 6, 11, 29, 10, 0]) == [0, 5, 6, 6, 10, 11, 29]
