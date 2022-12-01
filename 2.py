day = __file__.split('.')[0]

def algo1(data):
    horiz = 0
    depth = 0

    for entry in data:
        cmd, amt = entry.split(' ')
        amt = int(amt)

        if cmd == 'forward':
            horiz += amt
        elif cmd == 'down':
            depth += amt
        elif cmd == 'up':
            depth -= amt

    return horiz * depth


def algo2(data):
    horiz = 0
    depth = 0
    aim = 0

    for entry in data:
        cmd, amt = entry.split(' ')
        amt = int(amt)

        if cmd == 'forward':
            horiz += amt
            depth += aim * amt
        elif cmd == 'down':
            aim += amt
        elif cmd == 'up':
            aim -= amt

    return horiz * depth
if __name__ == "__main__":
    test1_input = ['forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]
    test1_answer = 150
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = ['forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]
    test2_answer = 900
    if algo2(test2_input) == test2_answer:
        print("Second Question Test 1 Passed")
    else:
        print("Second Question Test 1 FAILED")
    #
    # test2_input = [1, -1]
    # test2_answer = 0
    # if algo2(test2_input) == test2_answer:
    #     print("Second Question Test 2 Passed")
    # else:
    #     print("Second Question Test 2 FAILED")
    #
    # test2_input = [3, 3, 4, -2, -4]
    # test2_answer = 10
    # if algo2(test2_input) == test2_answer:
    #     print("Second Question Test 3 Passed")
    # else:
    #     print("Second Question Test 3 FAILED")
    #
    # test2_input = [-6, 3, 8, 5, -6]
    # test2_answer = 5
    # if algo2(test2_input) == test2_answer:
    #     print("Second Question Test 4 Passed")
    # else:
    #     print("Second Question Test 4 FAILED")
    #
    # test2_input = [7, 7, -2, -7, -4]
    # test2_answer = 14
    # if algo2(test2_input) == test2_answer:
    #     print("Second Question Test 5 Passed")
    # else:
    #     print("Second Question Test 5 FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data))
