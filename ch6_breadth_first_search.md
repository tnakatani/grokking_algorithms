# Ch. 6 Breadth-first Search

## Graphs

- A graph models a set of connections (e.g. train stations in a rail line)
- Graphs are made of nodes (station), and edges (rail). 
- A node can be connected to many other nodes.
- __Directed graphs__ show one-way relationships with an arrow.  This is used if relationships only go one-way.
- __Topological graph__ is a linear ordering of its vertices such that for every directed edge `uv` from vertex `u` to vertex `v`, `u` comes before `v` in the ordering.
- A __tree__ is a type of graph where no edges ever point back (think family tree).

## Breadth-first Search (BFS)

Answers 2 types of Qs:
1. Is there a path from node A to node B?
  - FUQ: If there isn't a path at the base node, check its connected node to see if those are connected to node B.
2. What is the shortest path from node A to node B?
  - Meaning, what is the smallest number of nodes/edges required to get to node B?

### Queues
- Graphs depend on a _queue_, ie. the order in which nodes are added to determine proximity to the base node.
- A queue is a type of data structure with 2 operations: __enqueue__ (push) and __dequeue__ (pop)
  - enqueue adds an item to the end of a list (`i[-1]`)
  - enqueue takes an item of at index 0 of a list (`i[0]`)
  - follows the FIFO (first in, first out) structure. A stack, in opposite, is LIFO.

## BFS in code with hash tables

Mapping a rail line network:

```py
graph = {}
graph["umeda"] = ["tsukamoto", "tenma", "shin osaka"]
graph["tsukamoto"] = ["umeda", "amagasaki"]
graph["amagasaki"] = ["tsukamoto", "kashima"]
graph["tenma"] = ["umeda", "sakuranomiya"]
graph["shin osaka"] = ["umeda", "higashiyodogawa"]
graph["sakuranomiya"] = []
graph["higashiyodogawa"] = []
graph["kashima"] = []


```

Implementing a BFS using the rail network

```py
from collections import deque

def search(base_node, destination_node):
    # create new queue, and add all of base node's neighbors to the search queue
    search_queue = deque()
    search_queue += graph[base_node]

    # while queue isn't empty, get first item off queue
    # check if item hasn't already been searched AND is destination.
    # return True if destination.
    # if not, add all of the item's neighbors and do it again.
    searched = {base_node}
    steps = 0
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            if node == destination_node:
                print(f"Found destination in {steps} steps: {node}")
                return True
            else:
                print(f"{node} not destination. Checking its neighbors.")
                search_queue += graph[node]
                searched.add(node)
                steps += 1
    return False
```

### Running time

Breadth-first search takes `O(number of nodes + number of edges)`, more commonly written as `O(V+E)` where V is "number of vertices" and E is "number of edges"


## Recap

- Breadth-first search tells you if there’s a path from A to B.
- If there’s a path, breadth-first search will find the shortest path.
- If you have a problem like “find the shortest X,” try modeling your problem as a graph, and use breadth-first search to solve.
- A directed graph has arrows, and the relationship follows the direction of the arrow (rama -> adit means “rama owes adit money”).
- Undirected graphs don’t have arrows, and the relationship goes both ways (ross - rachel means “ross dated rachel and rachel dated ross”).
- Queues are FIFO (First In, First Out).
- Stacks are LIFO (Last In, First Out).
- You need to check people in the order they were added to the search list, so the search list needs to be a queue. Otherwise, you won’t get the shortest path.
- Once you check someone, make sure you don’t check them again. Otherwise, you might end up in an infinite loop.


