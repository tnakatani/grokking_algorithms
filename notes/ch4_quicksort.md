# Ch.4 Quicksort

## Divide-and-conquer

- __quicksort__ is a type of D&C algorithm
- it's a sorting algorithm

### Method

1. Figure out base case, ie. the simplest possible case
2. Divide or decrease your problem until it becomes the base case.

### Example

Given an array of number, sum the numbers and return the total in a recursive way.

```py
def my_sum(arr):
  if len(arr) == 0:
    return 0
  else:
    arr.pop() + my_sum(arr)

```

## Quicksort

1. Pick a pivot
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Call quicksort recursively on the two sub-arrays.

Quicksort performance heavily depends on the pivot you use. If you're taking the pivot from the first item in a list, it is functioning basically the same way as going through a loop. If you start from the middle of the array, it would be much faster.

Taking the pivot from the first item in a list would be the worst-case scenario (height of call stack stack is `O(n)`, while taking a pivot from the middle would be a best case scenario (height of the call stack is `O(log n)`.  If you always choose a random element as the pivot, __you will get the best case consistently__.


## Recap

- D&C works by breaking a problem down into smaller and smaller pieces. If you’re using D&C on a list, the base case is probably an empty array or an array with one element.
- If you’re implementing quicksort, choose a random element as the pivot. The average runtime of quicksort is `O(n log n)`!
- The constant in Big O notation can matter sometimes. That’s why quicksort is faster than merge sort.
- The constant almost never matters for simple search versus binary search, because `O(log n)` is so much faster than `O(n)` when your list gets big.


