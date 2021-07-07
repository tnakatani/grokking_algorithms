# Ch.1 Introduction to Algorithms

## Binary Search

- With binary search, you guess the middle number and eliminate half the remaining numbers every time.
- When talking about running time in Big O notation, log always means log<sub>2</sub>.
- In general, for any list of `n`, binary search will take log<sub>2</sub>`n` steps to run in the worst case, whereas simple search will take `n` steps.
  - For a list of 8 numbers, binary search will require log<sub>2</sub>8 (3).
  - For a list of 1024 numbers, binary search will require log<sub>2</sub>1024 (10) 
- Binary search only work if your list is in sorted order.
- Binary search runs in _logarithmic time_, as opposed to _linear time_
  - For example, what takes a simple search 100ms to run can be done in 7ms with binary search (log<sub>2</sub>100).

__Exercises__

> Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?
> What about double the size?

```py
import math
math.log2(128) # 7.0
math.log2(256) # 8.0
```

## Big O Notation

- __Big O Notation__ is a special type of notation that tells you how fast an algorithm is.
- Big O lets you __compare the number of operations__ between algorithms.
  - `O(n)`: `O` is "Big O", `n` is number of operations.
- For example, given a list of size `n`:
  - Simple search needs to check each element. Run time in Big O is `O(n)`
  - Binary search needs to log `n` operations to check the same. Run time in Big O is `O(log n)`

### Common Big O run times

Sorted from fastest to slowest:
- `O(log n)`, also known as log time. Example: Binary search.
- `O(n),` also known as linear time. Example: Simple search.
- `O(n * log n).` Example: A fast sorting algorithm, like quicksort (coming up in chapter 4).
- `O(n2)`. Example: A slow sorting algorithm, like selection sort (coming up in chapter 2).
- `O(n!)`. Example: A really slow algorithm, like the traveling salesperson (coming up next!).

## Takeaways

- Algorithm speed isn’t measured in seconds, but in growth of the number of operations.
- Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
- Run time of algorithms is expressed in Big O notation.
- O(log n) is faster than O(n), but it gets a lot faster as the list of items you’re searching grows.
