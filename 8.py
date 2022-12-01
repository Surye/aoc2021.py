day = __file__.split('.')[0]
import copy
from collections import defaultdict

segments = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def part1(data):
    sequences = [y.split(' | ') for y in data]

    ret = 0

    for seq in sequences:
        pattern, output = [x.split() for x in seq]
        for out in output:
            if len(out) in [2,4,3,7]:
                ret += 1

    return ret

def part2(data):
    sequences = [y.split(' | ') for y in data]

    ret = 0

    for seq in sequences:
        pattern, output = [x.split() for x in seq]

        mixed_digits = {}
        possible_digits = defaultdict(list)
        mapped_letters = {}

        possible_letters = {}

        for num in pattern:
            if len(num) == 7:
                mixed_digits[8] = num
            elif len(num) == 3:
                mixed_digits[7] = num
            elif len(num) == 4:
                mixed_digits[4] = num
            elif len(num) == 2:
                mixed_digits[1] = num
            elif len(num) == 6:
                possible_digits[6].append(num)
            elif len(num) == 5:
                possible_digits[5].append(num)


        mapped_letters['a'] = (set(mixed_digits[1]).symmetric_difference(set(mixed_digits[7]))).pop()

        possible_letters['d'] = list(set(mixed_digits[1]).symmetric_difference(set(mixed_digits[4])))
        possible_letters['b'] = list(set(mixed_digits[1]).symmetric_difference(set(mixed_digits[4])))

        for six in possible_digits[6]:
            if not all(x in six for x in possible_letters['d']):
                mixed_digits[0] = six
                mapped_letters['d'] = set(mixed_digits[8]).difference(set(six)).pop()
                mapped_letters['b'] = set(possible_letters['b']).difference(set(mapped_letters['d'])).pop()

        for six in possible_digits[6]:
            if mapped_letters['d'] in six and mapped_letters['b'] in six and mapped_letters['a'] in six and mixed_digits[1][0] in six and mixed_digits[1][1] in six:
                mapped_letters['g'] = set(list(mapped_letters['d'] + mapped_letters['b'] + mapped_letters['a'] + mixed_digits[1])).symmetric_difference(set(six)).pop()

        for five in possible_digits[5]:
            if not(mixed_digits[1][0] in five and mixed_digits[1][1] in five): # 2 or 5
                if mapped_letters['b'] not in five: # 5
                    mapped_letters['f'] = set(mixed_digits[1]).difference(set(five)).pop()
                else: # 2
                    mapped_letters['c'] = set(mixed_digits[1]).difference(set(five)).pop()

        mapped_letters['e'] = set('abcdefg').difference(mapped_letters.values()).pop()
        mapped_letters = {value: key for key, value in mapped_letters.items()}
        outputs = [''.join(sorted([mapped_letters[x] for x in out])) for out in output]
        ret += (segments[outputs[0]] * 1000) + (segments[outputs[1]] * 100) + (segments[outputs[2]] * 10) + segments[outputs[3]]

    return ret


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split('\n')


    test1_answer = 26
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 61229
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
