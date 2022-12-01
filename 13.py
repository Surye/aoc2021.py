from typing import List

day = __file__.split('.')[0]
import copy
from collections import defaultdict
from itertools import chain


def part1(data):
    dots = []
    folds = []

    for line in data:
        if line.startswith('fold along'):
            direction, where = line[11:].split('=')
            folds.append([direction, int(where)])
        elif line:
            x, y = line.split(',')
            dots.append([int(x), int(y)])

    direction = folds[0][0]
    where = folds[0][1]

    new_dots = []
    if direction == 'y':
        for x,y in dots:
            if y < where:
                if [x,y] not in new_dots:
                    new_dots.append([x,y])
            else:
                new_y = ((where - y) * 2) + y
                if [x, new_y] not in new_dots:
                    new_dots.append([x, new_y])

    if direction == 'x':
        for x,y in dots:
            if x < where:
                if [x,y] not in new_dots:
                    new_dots.append([x,y])
            else:
                new_x = ((where - x) * 2) + x
                if [new_x, y] not in new_dots:
                    new_dots.append([new_x, y])

    #print_grid(new_dots)
    return len(new_dots)


def print_grid(dots):
    for y in range(max([x[1] for x in dots])+1):
        for x in range(max([x[0] for x in dots])+1):
            print([x, y] in dots and '█' or ' ', end='')
        print()

def part2(data):
    dots = []
    folds = []

    for line in data:
        if line.startswith('fold along'):
            direction, where = line[11:].split('=')
            folds.append([direction, int(where)])
        elif line:
            x, y = line.split(',')
            dots.append([int(x), int(y)])


    for direction, where in folds:
        new_dots = []
        if direction == 'y':
            for x, y in dots:
                if y < where:
                    if [x, y] not in new_dots:
                        new_dots.append([x, y])
                else:
                    new_y = ((where - y) * 2) + y
                    if [x, new_y] not in new_dots:
                        new_dots.append([x, new_y])

        if direction == 'x':
            for x, y in dots:
                if x < where:
                    if [x, y] not in new_dots:
                        new_dots.append([x, y])
                else:
                    new_x = ((where - x) * 2) + x
                    if [new_x, y] not in new_dots:
                        new_dots.append([new_x, y])
        dots = new_dots
    print_grid(dots)


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split('\n')


    test1_answer = 17
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = None
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
