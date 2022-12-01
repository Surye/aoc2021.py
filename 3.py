day = __file__.split('.')[0]

def algo1(data):
    total = len(data)
    gamma = epsilon = ''

    for number, _ in enumerate(data[0]):
        ones = 0
        for line in data:
            ones += 1 if line[number] == '1' else 0

        gamma += '1' if ones > total / 2 else '0'
        epsilon += '0' if ones > total / 2 else '1'
    return int(gamma, 2) * int(epsilon, 2)


def algo2(data):
    oxy_list = co2_list = data
    oxy = co2 = ''

    for number, _ in enumerate(data[0]):

        if len(oxy_list) > 1:
            ones = 0
            for line in oxy_list:
                ones += 1 if line[number] == '1' else 0
            filter = '1' if ones >= len(oxy_list) / 2 else '0'
            oxy_list = [x for x in oxy_list if x[number] == filter]
            oxy = oxy_list[0]

        if len(co2_list) > 1:
            ones = 0
            for line in co2_list:
                ones += 1 if line[number] == '1' else 0
            filter = '0' if ones >= len(co2_list) / 2 else '1'
            co2_list = [x for x in co2_list if x[number] == filter]
            co2 = co2_list[0]

    return int(oxy, 2) * int(co2, 2)


if __name__ == "__main__":
    test1_input = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    test1_answer = 198
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    test2_answer = 230
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
