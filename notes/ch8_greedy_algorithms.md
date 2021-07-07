# Ch.8 Greedy Algorithms

## Greedy algorithm

- Chooses the most optimal choice at each steps as it attempts to find the overall optimal way to solve the entire problem.
- Doesn't purport to have the most optimal solution overall.

Examples:

1. Packing a truck with different sized boxes: Greedy strategy would be to keep picking the largest box that will fit in the remaining space until you can't pack any more boxes.
2. Thief stealing in a store: Greedy strategy would be to pick the most expensive things until you can't fit your bag.


## Set-covering problem

Wiki definition: Given a set of elements `{1,2,..n}` (called the universe) and a collection `S of m` sets whose union equals the universe, the set cover problem is to identify the smallest sub-collection of `S whose union equals the universe. 

### Example: Radio station coverage throughout USA

__Question__: Given a list of radio stations, each with coverage over different states, how to derive the least number of radio stations needed to cover all 50 states.

- __Power set__: Naive approach is to list every possible subset of stations and pick the set with the smallest number of stations (sounds like traveling salesman?). Takes `O(2^n)` time since there are 2^n subsets.
- __Approximation algorithm__: Pick the stations that covers the most states that haven't been covered yet. Repeat until all states are covered. This is a type of greedy algorithm.
  - AAs are judged by 1) speed and 2) how close they are to the optimal solution.

[link to code](./code/ch8_greedy_algorithms.py)

## NP-complete problems

NP-complete = _"nondeterministic polynomial-time complete"_

From wiki - 
> In computational complexity theory, a problem is NP-complete when:
> 1. a brute-force search algorithm can solve it, and the correctness of each solution can be verified quickly, and
> 2. the problem can be used to simulate any other problem with similar solvability.

- Both traveling-salesperson and set-covering problems are NP-complete problems. They both try to calculate every possible solution and pick the smallest/shortest one.
- These problems are difficult to solve and impossible to write an algorithm that will solve these problems quickly.
- This is where approximation algorithms (like greedy algo) come in, where it does a "good enough" job. 

### How to determine if problem is NP-complete

No set format, but some characteristics:
- Your algorithm runs quickly with a handful of items but really slows down with more items.
- “All combinations of X” usually point to an NP-complete problem.
- Do you have to calculate “every possible version” of X because you can’t break it down into smaller sub-problems? Might be NP-complete.
- If your problem involves a sequence (such as a sequence of cities, like traveling salesperson), and it’s hard to solve, it might be NP-complete.
- If your problem involves a set (like a set of radio stations) and it’s hard to solve, it might be NP-complete.
- Can you restate your problem as the set-covering problem or the traveling-salesperson problem? Then your problem is definitely NP-complete.


## Recap 

- Greedy algorithms optimize locally, hoping to end up with a global optimum.
- NP-complete problems have no known fast solution.
- If you have an NP-complete problem, your best bet is to use an approximation algorithm.
- Greedy algorithms are easy to write and fast to run, so they make good approximation algorithms.
