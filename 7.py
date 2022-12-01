day = __file__.split('.')[0]

def part1(data):
    pos = list(map(int, data[0].split(',')))
    return min([sum([abs(c-dest) for c in pos]) for dest in range(max(pos))])

def binomial_coefficient(n):
    return (pow(n, 2)+n) // 2

def part2(data):
    pos = list(map(int, data[0].split(',')))
    return min([sum([binomial_coefficient(abs(c-dest)) for c in pos]) for dest in range(max(pos))])

if __name__ == "__main__":
    test1_input = """16,1,2,0,4,2,7,1,2,14""".split('\n')
    test1_answer = 37
    test1_result = part1(test1_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    test2_input = """16,1,2,0,4,2,7,1,2,14""".split('\n')
    test2_answer = 168
    test2_result = part2(test2_input)
    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    import copy
    print("Answer 1: ", part1(copy.copy(input_data)))
    print("Answer 2: ", part2(copy.copy(input_data)))
