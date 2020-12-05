import sys
import itertools
from functools import reduce


def fix_expense_report(data, n):
    pairs = itertools.combinations(data, n)
    expected_pairs = (p for p in pairs if sum(p) == 2020)
    expected_pair = next(expected_pairs, None)

    if expected_pair is None:
        raise ValueError("data is incorrect")

    return reduce(lambda acc, val: acc * val, expected_pair, 1)


if __name__ == '__main__':
    data = [int(line) for line in sys.stdin]
    res_1 = fix_expense_report(data, 2)
    print("First stage:", res_1)
    res_2 = fix_expense_report(data, 3)
    print("Second stage:", res_2)
