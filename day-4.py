import sys


REQUIRED_KEYS = ("byr", "iyr", "eyr",
                 "hgt", "hcl", "ecl",
                "pid")

OPTIONAL_KEYS = ("cid",)


ALL_KEYS = REQUIRED_KEYS + OPTIONAL_KEYS


def is_valid_year(year, min_, max_):
    if not year.isdigit():
        return False
    year = int(year)
    return year >= min_ and year <= max_


def is_valid_height(height):
    if len(height) < 2:
        return False
    height_value, height_unit = height[:-2], height[-2:]
    if not height_value.isdigit():
        return False

    height_value = int(height_value)

    if height_unit == "cm":
        return height_value >= 150 and height_value <= 193
    elif height_unit == "in":
        return height_value >= 59 and height_value <= 76
    else:
        return False


def is_valid_passport_id(pid):
    return pid.isdigit() and len(pid) == 9


def is_valid_hair_color(hcl):
    if not hcl.startswith('#'):
        return False

    hcl = hcl[1:]

    return all(c.isdigit() or c in ('a', 'b', 'c', 'd', 'e', 'f') for c in hcl)


def is_valid_eye_color(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def is_valid(passport):
    if not all(key in passport for key in REQUIRED_KEYS):
        return False

    if not is_valid_year(passport['byr'], 1920, 2002):
        return False

    if not is_valid_year(passport['iyr'], 2010, 2020):
        return False

    if not is_valid_year(passport['eyr'], 2020, 2030):
        return False

    if not is_valid_height(passport['hgt']):
        return False

    if not is_valid_hair_color(passport['hcl']):
        return False

    if not is_valid_eye_color(passport['ecl']):
        return False

    if not is_valid_passport_id(passport['pid']):
        return False

    print(passport)
    return True


def parse_passport(lines):
    passport = {}

    for line in lines:
        fields = line.split()
        for field in fields:
            key, value = field.split(":")
            passport[key] = value

    return passport


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


if __name__ == '__main__':
    passports = [parse_passport(p)
                 for p in split_by_blank_line(sys.stdin)]
    valid_passports_num = len([p for p in passports if is_valid(p)])

    print("Stage 2:", valid_passports_num)