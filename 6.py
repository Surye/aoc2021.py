day = __file__.split('.')[0]


def part1(data):
    return simulate(data, 80)


def part2(data):
    return simulate(data, 256)


def simulate(data, days):
    fs = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }

    for n in data[0].split(','):
        fs[int(n)] += 1

    for _ in range(days):
        new_fish = fs[0]
        fs[0] = fs[1]
        fs[1] = fs[2]
        fs[2] = fs[3]
        fs[3] = fs[4]
        fs[4] = fs[5]
        fs[5] = fs[6]
        fs[6] = fs[7] + new_fish
        fs[7] = fs[8]
        fs[8] = new_fish

    return sum(fs.values())


if __name__ == "__main__":
    test1_input = """3,4,3,1,2""".split('\n')
    test1_answer = 5934

    if part1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = """3,4,3,1,2""".split('\n')
    test2_answer = 26984457539
    if part2(test2_input) == test2_answer:
        print("Second Question Test 1 Passed")
    else:
        print("Second Question Test 1 FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    import copy
    print("Answer 1: ", part1(copy.copy(input_data)))
    print("Answer 2: ", part2(copy.copy(input_data)))
