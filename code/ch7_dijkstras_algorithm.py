"""Ch.7 Dijkstra's algorithm"""

"""Storing the graph"""
# start node and neighbors
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# neighbors to destination node
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

# destination node, no neighbors
graph["fin"] = {}


"""Hash table to store the costs for each node"""
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")


"""Hash table to store each node's parents"""
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        # if it's the lowest cost so far and hasn't been processed
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstras_algorithm(graph: dict, costs: dict, parents: dict):
    # array to keep track of all nodes processed
    processed = []
    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        # go through all the neighbors of this node
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # if it's cheaper to get to this neighbor by going through it
            if costs[n] > new_cost:
                # update the cost for this node
                costs[n] = new_cost
                # this node becomes the new parent for this neighbor
                parents[n] = node
        # mark node as processed
        processed.append(node)
        # find next node to process and loop
        node = find_lowest_cost_node(costs, processed)

    return costs


if __name__ == "__main__":
    costs = dijkstras_algorithm(graph, costs, parents)
    print(f"Cost from the start to each node: \n{costs}")
