# Ch.2 Selection Sort

## Linked Lists vs Arrays

In Python, Linked Lists = Dicts and Arrays = Lists.

- LLs are more efficients than arrays because each items doesn't have to be adjacent in memory.
  - Each item in a linked list has the address of next item.
- OTOH, arrays are faster at reading elements since they are next to each other.
- Arrays have fast reads and slow inserts.
- Linked Lists have slow reads and fast inserts.
- Linked Lists are easier to insert elements into the middle. Array require reshuffling.  Same with deleting items.

## Selection Sort 

- Used for sorting names, dates, etcs.
- Slower than Quicksort (explained later)
- Big O: `O(n)`, 
  - Each sorting operation requires algorithm to check each item in the list.
  - Big O is constant even though the number of items to check decreases each time.  Technically, selection sort is `O(n*0.5n)` based on average number of checks in a list, but constants like `0.5` are ignored in Big O notation.
