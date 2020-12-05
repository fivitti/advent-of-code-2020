import sys
from collections import Counter, namedtuple


Rule = namedtuple("Rule", "min max letter")


def parse_rule(raw):
    limits, letter = raw.split()
    minimum, maximum = limits.split('-')
    minimum = int(minimum)
    maximum = int(maximum)

    return Rule(minimum, maximum, letter)


def is_valid_password_1(rule, password):
    counter = Counter(password)
    count = counter[rule.letter]
    return count >= rule.min and count <= rule.max


def is_valid_password_2(rule, password):
    return (password[rule.min - 1] == rule.letter) != \
        (password[rule.max - 1] == rule.letter)


def count_valid_passwords(lines):
    valid_passwords_1 = 0
    valid_passwords_2 = 0

    for line in lines:
        rule_raw, password = line.split(": ")
        rule = parse_rule(rule_raw)
        if is_valid_password_1(rule, password):
            valid_passwords_1 += 1
        if is_valid_password_2(rule, password):
            valid_passwords_2 += 1

    return valid_passwords_1, valid_passwords_2


if __name__ == '__main__':
    data = list(sys.stdin)
    valid_1, valid_2 = count_valid_passwords(data)
    print("Stage 1:", valid_1)
    print("Stage 2:", valid_2)