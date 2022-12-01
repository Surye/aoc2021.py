import sys
from typing import List, Union

day = __file__.split('.')[0]
import copy
import math
import re


class Number:
    def __init__(self, left: Union[int, List, 'Number'], right: Union[int, List, 'Number']):
        self.left = Number(left[0], left[1]) if isinstance(left, list) else left
        self.right = Number(right[0], right[1]) if isinstance(right, list) else right

    def __add__(self, other):
        return Number(self, other)

    def __repr__(self):
        return f"[{self.left.__repr__()}, {self.right.__repr__()}]"

    def get(self,direction):
        if direction == "L": return self.left
        if direction == "R": return self.right

    def set(self,direction, value):
        if direction == "L": self.left = value
        if direction == "R": self.right = value

    def magnitude(self):
        value = 0
        value += (self.left if not isinstance(self.left, Number) else self.left.magnitude()) * 3
        value += (self.right if not isinstance(self.right, Number) else self.right.magnitude()) * 2
        return value

    def explode(self, root, depth=0):
        # TODO: use the root and depth to add to the "next" regular number in a different pair?
        if depth < 3:
            ret = False
            if isinstance(self.left, Number):
                ret = self.left.explode(root, depth=depth + 1)
            if not ret and isinstance(self.right, Number):
                ret = self.right.explode(root, depth=depth + 1)
            return ret
        else:
            if isinstance(self.left, Number):
                # if isinstance(self.right, int):
                #     self.right += self.left.right
                # else:
                #     self.explode_add(root, "R", path, self.left.right)
                self.right += self.left.right
                #self.explode_add(root, "L", self.left.left)
                self.left = 0
                print(f"after explode:  {root}")
                return True
            elif isinstance(self.right, Number):
                # if isinstance(self.left, int):
                #     self.left += self.right.left
                # else:
                #     self.explode_add(root, "L", self.right.left)
                self.left += self.right.left
                # self.explode_add(root, "R", self.right.right)

                if isinstance(root.right, int):
                    root.right += self.right.right
                else:
                    root.right.left += self.right.right
                self.right = 0
                print(f"after explode:  {root}")
                return True
        return False
    #
    # def explode_add(self, root, direction, value):
    #     # node = root.get(direction)
    #     leaf_direction = "L" if direction == "R" else "R"
    #     if isinstance(root.get(direction), Number):
    #         root.get(direction).set(leaf_direction, root.get(direction))
    #     else:
    #         root.set(direction, root.get(direction) + value)




    def split(self):
        if isinstance(self.left, Number):
            return self.left.split()
        elif self.left > 9:
            self.left = Number(math.floor(self.left / 2), math.ceil(self.left / 2))
            print(f"after split:  {self}")
            return True

        if isinstance(self.right, Number):
            return self.right.split()
        elif self.right > 9:
            self.right = Number(math.floor(self.right / 2), math.ceil(self.right / 2))
            print(f"after split:  {self}")
            return True
        return False

    def reduce(self):
        not_reduced = True
        while not_reduced:
            while self.explode(self):
                pass
            not_reduced = self.split()


def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":

    #y = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    y = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
    x = Number(y[0], y[1])
    x.reduce()
    x.reduce()

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
        """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]""".split('\n')

    test1_answer = 4140
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    # test2_answer = 112
    # test2_result = part2(test_input)
    #
    # if test2_result == test2_answer:
    #     print(f"Second Question Test 1 Passed")
    # else:
    #     print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")
    #
    # print("Answer 2: ", part2(copy.copy(input_data)))
