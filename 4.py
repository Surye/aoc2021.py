day = __file__.split('.')[0]
import re

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class BingoCard:
    def __init__(self, lines):
        self.values = [
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
        ]
        self.matches = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        
        for row, line in enumerate(lines):
            for col, value in enumerate([int(x.strip()) for x in line.split(' ') if x]):
                self.values[row][col] = value

    def mark_board(self, selected_num):
        for row, line in enumerate(self.values):
            for col, value in enumerate(line):
                if value == selected_num:
                    self.matches[row][col] = 1

    def score(self):
        score = 0
        for row, line in enumerate(self.values):
            for col, value in enumerate(line):
                if self.matches[row][col] == 0:
                    score += value
        return score

    def is_winner(self):
        for row in self.matches:
            if all(row):
                return True
        for col in range(len(self.matches[0])):
            if all([x[col] for x in self.matches]):
                return True
        return False

    def __str__(self):
        ret = ""
        for row, line in enumerate(self.values):
            for col, value in enumerate(line):
                prefix = color.RED if self.matches[row][col] == 1 else ''
                suffix = color.END if self.matches[row][col] == 1 else ''
                ret += f"{prefix}{value: 3d}{suffix}"
            ret += "\n"
        return ret.rstrip()

def algo1(data):
    selections = data.pop(0)

    data = [x for x in data if x.strip()]

    cards = []

    for card in [data[i:i+5] for i in range(0, len(data), 5)]:
        cards.append(BingoCard(card))

    for selected_num in [int(x) for x in selections.split(',')]:
        for card in cards:
            card.mark_board(selected_num)

        for card in cards:
            if card.is_winner():
                return card.score() * selected_num


def algo2(data):
    selections = data.pop(0)

    data = [x for x in data if x.strip()]

    cards = []
    scores = []

    for card in [data[i:i+5] for i in range(0, len(data), 5)]:
        cards.append(BingoCard(card))

    for selected_num in [int(x) for x in selections.split(',') if x.strip()]:
        for card in cards:
            card.mark_board(selected_num)

        for card in cards:
            if card.is_winner():
                # print(f"{card}\nScore: {card.score()}, Selected Number: {selected_num}  => {card.score() * selected_num}")
                scores.append(card.score() * selected_num)
                cards.remove(card)

    return scores[-1]


if __name__ == "__main__":
    test1_input = """7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7""".split('\n')

    test1_answer = 4512
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = """7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1

22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19

3 15  0  2 22
9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7""".split('\n')
    test2_answer = 1924
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

    import copy
    print("Answer 1: ", algo1(copy.copy(input_data)))
    print("Answer 2: ", algo2(copy.copy(input_data)))
