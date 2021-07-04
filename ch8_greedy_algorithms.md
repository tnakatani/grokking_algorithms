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

