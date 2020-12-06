from collections import Counter
import sys


def split_by_blank_line(lines):
    accumulator = []

    for line in lines:
        line = line.strip()

        if line == "":
            yield accumulator
            accumulator = []
        else:
            accumulator.append(line)
    
    if accumulator:
        yield accumulator


def count_answers_in_group_if_anyone(lines):
    answers = set()

    for line in lines:
        for char in line:
            answers.add(char)

    return len(answers)


def count_answers_in_group_if_everyone(lines):
    length = len(lines)
    answers = Counter()

    for line in lines:
        for char in line:
            answers[char] += 1

    return len([k for k, v in answers.items() if v == length])


def sum_answers_in_groups(groups, count_func):
    return sum(count_func(g) for g in groups)


if __name__ == '__main__':
    groups = list(split_by_blank_line(sys.stdin))
    sum_1 = sum_answers_in_groups(groups, count_answers_in_group_if_anyone)
    sum_2 = sum_answers_in_groups(groups, count_answers_in_group_if_everyone)

    print("Stage 1:", sum_1)
    print("Stage 2:", sum_2)
