import itertools
import math


def find_2020(x, length=2):
    for i in itertools.permutations(x, length):
        if sum(i) == 2020:
            return i


def read_inputs(filepath) -> list:
    with open(filepath) as f:
        return [int(i.strip()) for i in f.readlines()]


if __name__ == '__main__':
    fp = "inputs/day1_1.csv"
    expense_report = read_inputs(fp)
    entries = find_2020(expense_report, 3)
    print(math.prod(entries))
