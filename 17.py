import sys
from typing import List

day = __file__.split('.')[0]
import copy
import math
import re
from enum import Enum
from typing import Tuple


class Status(Enum):
    HIT = 0
    SHORT = 1
    OVER = 2

def evaluate_target(x_range: Tuple[int, int], y_range: Tuple[int, int], coord: List[int]) -> Status:
    if x_range[0] <= coord[0] <= x_range[1] and y_range[1] >= coord[1] >= y_range[0]:
        return Status.HIT
    elif coord[0] > x_range[1] or coord[1] < y_range[0]:
        return Status.OVER
    else:
        return Status.SHORT

def part1(data):
    (x1, x2, y1, y2) = map(int, re.match(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', data[0]).groups())

    hit_max_height = 0

    for x_velocity in range(1, x2+1):
        for y_velocity in range(1, abs(x2)):
            x_vel_calc = x_velocity
            y_vel_calc = y_velocity
            step = 1
            max_height = 0
            pos = [0, 0]
            overshot = False
            while not overshot:
                step += 1
                pos[0] += x_vel_calc
                pos[1] += y_vel_calc
                y_vel_calc -= 1
                if x_vel_calc > 0:
                    x_vel_calc -= 1
                elif x_vel_calc < 0:
                    x_vel_calc += 1
                result = evaluate_target((x1, x2), (y1, y2), pos)
                # print(f"({x_velocity}, {y_velocity}), Steps {step}, Pos {pos}, Result {result}")
                max_height = max(max_height, pos[1])
                if result == Status.HIT:
                    hit_max_height = max(max_height, hit_max_height)
                elif result == Status.OVER:
                    overshot = True
            # print(f"({x_velocity}, {y_velocity}), Steps {step}, Height {max_height}")
    return hit_max_height

def part2(data):
    (x1, x2, y1, y2) = map(int, re.match(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', data[0]).groups())

    valid_initial = set()

    for x_velocity in range(1, x2+1):
        for y_velocity in range(-1*abs(x2), abs(x2)+1):
            x_vel_calc = x_velocity
            y_vel_calc = y_velocity
            step = 1
            max_height = 0
            pos = [0, 0]
            overshot = False
            while not overshot:
                step += 1
                pos[0] += x_vel_calc
                pos[1] += y_vel_calc
                y_vel_calc -= 1
                if x_vel_calc > 0:
                    x_vel_calc -= 1
                elif x_vel_calc < 0:
                    x_vel_calc += 1
                result = evaluate_target((x1, x2), (y1, y2), pos)
                if result == Status.HIT:
                    valid_initial.add((x_velocity, y_velocity))
                elif result == Status.OVER:
                    overshot = True
    return len(valid_initial)

if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""target area: x=20..30, y=-10..-5""".split('\n')


    test1_answer = 45
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 112
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
