from typing import List

day = __file__.split('.')[0]
import copy
from collections import defaultdict

map = {
    '{': '}',
    '<': '>',
    '[': ']',
    '(': ')',
    '}': '{',
    '>': '<',
    ']': '[',
    ')': '(',
}

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def part1(data):
    bad_chars = []
    for line_no, line  in enumerate(data):
        stack = []

        try:
            for token in list(line):
                if token in '{([<':
                    stack.append(token)
                else:
                    found = map[token]
                    expected = stack.pop()

                    if found != expected:
                        print(f"Expected {map[expected]}, but found {token} instead.")
                        bad_chars.append(token)
                        raise SyntaxError()
        except SyntaxError:
            pass
    return sum(score[x] for x in bad_chars)

def get_incomplete(data):
    incomplete = []

    for line_no, line in enumerate(data):
        stack = []

        try:
            for token in list(line):
                if token in '{([<':
                    stack.append(token)
                else:
                    found = map[token]
                    expected = stack.pop()
                    if found != expected:
                        raise SyntaxError()
            # print(f"Line #{line_no} incomplete: {line}")
            incomplete.append(line)
        except SyntaxError:
            pass
    return incomplete

def part2(data):
    data = get_incomplete(data)

    scores = []

    for line_no, line in enumerate(data):
        stack = []
        for token in list(line):
            if token in '{([<':
                stack.append(token)
            else:
                stack.pop()
        needed = [map[x] for x in reversed(stack)]
        score = 0
        for el in needed:
            score *= 5
            score += score2[el]

        scores.append(score)
    import statistics
    scores.sort()
    return statistics.median(scores)



if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split('\n')


    test1_answer = 26397
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 288957
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
