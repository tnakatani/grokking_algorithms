"""Ch6 Breadth first search"""
from collections import deque

graph = {}
graph["umeda"] = ["tsukamoto", "tenma", "shin osaka"]
graph["tsukamoto"] = ["umeda", "amagasaki"]
graph["amagasaki"] = ["tsukamoto", "kashima"]
graph["tenma"] = ["umeda", "sakuranomiya"]
graph["shin osaka"] = ["umeda", "higashiyodogawa"]
graph["sakuranomiya"] = []
graph["higashiyodogawa"] = []
graph["kashima"] = []


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


if __name__ == "__main__":
    search("umeda", "kashima")
