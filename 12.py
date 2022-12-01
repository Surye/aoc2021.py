from enum import Enum
from typing import List, Dict
from pprint import pp

day = __file__.split('.')[0]
import copy
from collections import defaultdict, deque, Counter
from itertools import chain


class Type(Enum):
    START = 1
    BIG = 2
    SMALL = 3
    END = 4

class Cave:
    def __init__(self, name):
        self.name = name  # type: str
        self.connections = []  # type: List[Cave]
        self.visited = 0

    @property
    def type(self) -> Type:
        if self.name == 'start':
            return Type.START
        elif self.name == 'end':
            return Type.END
        elif self.name.isupper():
            return Type.BIG
        else:
            return Type.SMALL

    def __str__(self):
        return f"{self.type} Cave {self.name}: Connected To [{','.join([x.name for x in self.connections])}]"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        str.__hash__(self.name)


def part1(data):
    connections = [x.split('-') for x in data]  # type: List[List[str]]
    caves = {x: Cave(x) for x in set(chain(*connections))}  # type: Dict[str,Cave]
    for c1, c2 in connections:
        caves[c1].connections.append(caves[c2])
        caves[c2].connections.append(caves[c1])

    start = caves['start']
    end = caves['end']

    paths = find_all_paths_bfs(caves, start, end)

    return len(paths)

def find_all_paths_bfs(graph: Dict[str,Cave], start: Cave, end: Cave):
    nodes = deque()
    nodes.append([start.name])
    all_possible_paths = []

    while nodes:
        previous_path = nodes.popleft()
        last_node = previous_path[-1]
        #Reached path, append it to all_paths
        if last_node == end.name:
            all_possible_paths.append(previous_path)
        for node in graph[last_node].connections:
            if node.type == Type.BIG or (node.type == Type.SMALL and 2 not in Counter([x for x in previous_path if x.islower()]).values()) or node.name not in previous_path:
                new_path = previous_path + [node.name]
                nodes.append(new_path)
    return all_possible_paths

def part2(data):
    pass

if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split('\n')


    test1_answer = 3509
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    # test2_answer = 195
    # test2_result = part2(test_input)
    #
    # if test2_result == test2_answer:
    #     print(f"Second Question Test 1 Passed")
    # else:
    #     print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")
    #
    # print("Answer 2: ", part2(copy.copy(input_data)))
