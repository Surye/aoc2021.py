from typing import List

day = __file__.split('.')[0]
import copy
from collections import defaultdict


def part1(data):
    map = [[int(x) for x in line] for line in data]

    low_points = []

    for row in range(len(map)):
        for col in range(len(map[row])):
            other = []
            try:
                if row - 1 >= 0:
                    other.append(map[row-1][col])
            except:
                pass
            try:
                if col - 1 >= 0:
                    other.append(map[row][col-1])
            except:
                pass
            try:
                other.append(map[row][col+1])
            except:
                pass
            try:
                other.append(map[row+1][col])
            except:
                pass

            if map[row][col] < min(other):
                low_points.append(map[row][col]+1)

    return sum(low_points)

def part2(data):
    map = [[int(x) for x in line] for line in data]

    low_points = []

    for row in range(len(map)):
        for col in range(len(map[row])):
            other = []
            try:
                if row - 1 >= 0:
                    other.append(map[row-1][col])
            except:
                pass
            try:
                if col - 1 >= 0:
                    other.append(map[row][col-1])
            except:
                pass
            try:
                other.append(map[row][col+1])
            except:
                pass
            try:
                other.append(map[row+1][col])
            except:
                pass

            if map[row][col] < min(other):
                low_points.append((row, col))

    basin_sizes = []

    for point in low_points:
        basin_points.clear()
        basin_sizes.append(len(get_basin(map, point)))
    basin_sizes.sort(reverse=True)

    return  basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

basin_points = []

def get_basin(map, point):
    basin_points.append(point)
    x, y = point
    stop = False
    while not stop:
        x += 1
        if x < len(map) and map[x][y] != 9:
            if (x,y) not in basin_points:
                basin_points.extend(get_basin(map, (x,y)))
        else:
            stop = True

    x, y = point
    stop = False
    while not stop:
        x -= 1
        if x >= 0 and map[x][y] != 9:
            if (x, y) not in basin_points:
                basin_points.extend(get_basin(map, (x,y)))
        else:
            stop = True

    x, y = point
    stop = False
    while not stop:
        y += 1
        if y < len(map[x]) and map[x][y] != 9:
            if (x, y) not in basin_points:
                basin_points.extend(get_basin(map, (x,y)))
        else:
            stop = True

    x, y = point
    stop = False
    while not stop:
        y -= 1
        if y >= 0 and map[x][y] != 9:
            if (x, y) not in basin_points:
                basin_points.extend(get_basin(map, (x,y)))
        else:
            stop = True

    return set(basin_points)



if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""2199943210
3987894921
9856789892
8767896789
9899965678""".split('\n')


    test1_answer = 15
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 1134
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
