from typing import List

day = __file__.split('.')[0]
import copy
import re
from collections import defaultdict, Counter
from itertools import chain

def run_step(poly, rules):
    insertions = {}

    for pair, item in rules:
        positions = [idx.start() for idx in re.finditer(pattern='(?={0})'.format(pair), string=poly)]
        for idx in positions:
            insertions[idx + 1] = item

    poly = list(poly)
    for insert_idx in sorted(insertions.keys(), reverse=True):
        poly.insert(insert_idx, insertions[insert_idx])
    return ''.join(chain(*poly))


def part1(data):
    poly = data[0]
    rules = [rule.split(' -> ') for rule in data[2:]]

    for _ in range(10):
        poly = run_step(poly, rules)

    result = Counter(poly)

    return result.most_common()[0][1] - result.most_common()[-1][1]


def run_step_not_stupid(pairs, rules):
    tmp_add = Counter()
    tmp_remove = Counter()

    for pair, item in rules:
        tmp_add[pair[0] + item] += pairs[pair]
        tmp_add[item + pair[1]] += pairs[pair]
        tmp_remove[pair] += pairs[pair]

    for item in tmp_add.keys():
        pairs[item] += tmp_add[item]

    for item in tmp_remove.keys():
        pairs[item] -= tmp_remove[item]

    return pairs


def part2(data):
    poly = data[0]
    rules = [rule.split(' -> ') for rule in data[2:]]
    pairs = Counter([''.join(pair) for pair in zip(poly[:-1], poly[1:])])

    for _ in range(80000):
        pairs = run_step_not_stupid(pairs, rules)

    result = Counter(poly[0])
    for pair in pairs:
        result[pair[1]] += pairs[pair]
    return result.most_common()[0][1] - result.most_common()[-1][1]


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split('\n')


    test1_answer = 1588
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 2188189693529
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
