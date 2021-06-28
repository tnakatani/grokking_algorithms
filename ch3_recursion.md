# Ch.3 Recursion

## Recursion 

- Every recursive function has 2 parts:
  1. __base case__ - when to break out of recursion
  2. __recursive case__ - the recursive action

```py
def countdown(i):
  print(i)
  if i <= 1:  # base case
    return
  else:
    countdown(i-1) # recursive case
```

## Stack

- A stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO (Last In First Out) or FILO (First In Last Out).
- When you call a function from another function, the calling function is paused in a partially completed state.
  - Imagine a plate of dishes - the first one placed will be the last one used.
- Recursion is more memory intensive than a loop because each function calls must be saved to memory. Can get around this by using a `for` loop. 
