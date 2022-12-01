from typing import List

day = __file__.split('.')[0]
import copy
from collections import defaultdict
from itertools import chain

class Octo:
    def __init__(self, init_val):
        self.energy = int(init_val)
        self.has_flashed = False



def part1(data):
    data = [[Octo(x) for x in line] for line in data]

    flashes = 0

    for step in range(100):
        found_flashes = True
        for row in range(len(data)):
            for col in range(len(data[row])):
                data[row][col].energy += 1

        while found_flashes:
            found_flashes = False
            for row in range(len(data)):
                for col in range(len(data[row])):
                    octo = data[row][col]
                    #print(f"Processing [{row}][{col}]: {octo.energy}, {octo.has_flashed}")
                    if octo.energy > 9 and not octo.has_flashed:
                        octo.has_flashed = True
                        found_flashes = True

                        flashes += 1
                        above = row + 1 < len(data)
                        below = row - 1 >= 0
                        left = col - 1 >= 0
                        right = col + 1 < len(data[row])

                        if above:
                            data[row + 1][col].energy += 1
                            if left:
                                data[row + 1][col - 1].energy += 1
                            if right:
                                data[row + 1][col + 1].energy += 1

                        if below:
                            data[row-1][col].energy += 1
                            if left:
                                data[row - 1][col - 1].energy += 1
                            if right:
                                data[row - 1][col + 1].energy += 1

                        if left:
                            data[row][col-1].energy += 1
                        if right:
                            data[row][col+1].energy += 1

        for row in range(len(data)):
            for col in range(len(data[row])):
                octo = data[row][col]
                if octo.energy > 9:
                    octo.energy = 0
                    octo.has_flashed = False

    return flashes


def part2(data):
    data = [[Octo(x) for x in line] for line in data]

    steps = 0

    while True:
        steps += 1
        found_flashes = True
        for row in range(len(data)):
            for col in range(len(data[row])):
                data[row][col].energy += 1

        while found_flashes:
            found_flashes = False
            for row in range(len(data)):
                for col in range(len(data[row])):
                    octo = data[row][col]
                    if octo.energy > 9 and not octo.has_flashed:
                        octo.has_flashed = True
                        found_flashes = True

                        above = row + 1 < len(data)
                        below = row - 1 >= 0
                        left = col - 1 >= 0
                        right = col + 1 < len(data[row])

                        if above:
                            data[row + 1][col].energy += 1
                            if left:
                                data[row + 1][col - 1].energy += 1
                            if right:
                                data[row + 1][col + 1].energy += 1

                        if below:
                            data[row-1][col].energy += 1
                            if left:
                                data[row - 1][col - 1].energy += 1
                            if right:
                                data[row - 1][col + 1].energy += 1

                        if left:
                            data[row][col-1].energy += 1
                        if right:
                            data[row][col+1].energy += 1

        if all(chain(*[[x.has_flashed for x in row] for row in data])):
            return steps

        for row in range(len(data)):
            for col in range(len(data[row])):
                octo = data[row][col]
                if octo.energy > 9:
                    octo.energy = 0
                    octo.has_flashed = False


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split('\n')


    test1_answer = 1656
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 195
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
