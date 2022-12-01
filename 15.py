import sys
from typing import List

day = __file__.split('.')[0]
import copy
import re
import numpy
from collections import defaultdict, Counter
from itertools import chain

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# def get_neighbors(x, y, map, visited, cost):
#     ret = []
#
#     if x+1 < len(map[0]) and not visited[x+1][y]:
#         ret.append((x+1, y))
#     if x-1 >= 0 and not visited[x-1][y]:
#         ret.append((x-1, y))
#     if y+1 < len(map) and not visited[x][y+1]:
#         ret.append((x, y+1))
#     if y-1 >= 0 and not visited[x][y-1]:
#         ret.append((x, y-1))
#
#     return ret
#
# def part1(data):
#     map = [list(x) for x in data]
#     n = len(map[0])
#     m = len(map)
#
#
#     visited = numpy.full((n, m), False, numpy.bool)
#     cost = numpy.full((n, m), numpy.Inf)
#
#     shortest_path = {}
#     previous_nodes = {}
#
#
#     cost[0, 0] = 0
#
#

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def get_neighbors(x, y, map):
    ret = []

    if x+1 < len(map[0]):
        ret.append((x+1, y))
    if x-1 >= 0:
        ret.append((x-1, y))
    if y+1 < len(map):
        ret.append((x, y+1))
    if y-1 >= 0:
        ret.append((x, y-1))

    return ret

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

def part1(data):
    map = [list(int(y) for y in x) for x in data]

    start_node = (0, 0)
    target_node = (len(map[0])-1, len(map)-1)

    import networkx as nx
    graph = nx.DiGraph()
    for x in range(len(map[0])):
        for y in range(len(map)):
            graph.add_node((x, y))
    for x in range(len(map[0])):
        for y in range(len(map)):
            for neighbor in get_neighbors(x, y, map):
                weight = map[neighbor[0]][neighbor[1]]
                graph.add_edge((x, y), neighbor, weight=weight)


    path = nx.dijkstra_path(graph, source=start_node, target=target_node, weight="weight")

    print(path)
    for x in range(len(map[0])):
        for y in range(len(map)):
            prefix = color.RED if (x, y) in path else ''
            suffix = color.END if (x, y) in path else ''
            print(f"{prefix}{map[x][y]}{suffix}", end='')
        print()

    return nx.dijkstra_path_length(graph, source=start_node, target=target_node, weight="weight")


def part2(data):
    map = [list(int(y) for y in x) for x in data]
    bigmap = []
    for row in map:
        new_row = [row]
        for i in range(1,5):
            addl_row = []
            for x in row:
                new_val = x + i
                if new_val > 9:
                    new_val -= 9
                addl_row.append(new_val)
            new_row.append(addl_row)
        bigmap.append(list(chain(*new_row)))

    map = copy.copy(bigmap)
    for i in range(1, 5):
        for row in bigmap:
            new_row = [x+i if x+i <= 9 else x+i-9 for x in row]
            map.append(new_row)

    start_node = (0, 0)
    target_node = (len(map[0])-1, len(map)-1)

    import networkx as nx
    graph = nx.DiGraph()
    for y in range(len(map[0])):
        for x in range(len(map)):
            for neighbor in get_neighbors(x, y, map):
                graph.add_edge((x, y), neighbor, weight=map[neighbor[0]][neighbor[1]])

    return nx.shortest_path_length(graph, source=start_node, target=target_node, weight="weight")


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split('\n')


    test1_answer = 40
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 315
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
