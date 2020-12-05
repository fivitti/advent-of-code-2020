import sys


def decode_number(raw, low, high):
    num = 0

    for c in raw:
        num <<= 1
        num |= 0 if c == low else 1

    return num


def decode_seat(raw):
    row, col = raw[:7], raw[7:]
    row = decode_number(row, 'F', 'B')
    col = decode_number(col, 'L', 'R')
    return row * 8 + col


def find_highest_seat(lines):
    return max(decode_seat(line) for line in lines)


def find_my_seat(lines):
    seats = {decode_seat(line) for line in lines}
    all_seats = set(range(0, 128 * 8))
    candidate_seats = all_seats.difference(seats)

    for seat in candidate_seats:
        if seat == 0 or seat == 128 * 8 - 1:
            continue

        previous_seat = seat - 1
        next_seat = seat + 1

        if previous_seat in seats and next_seat in seats:
            return seat
    return None


if __name__ == '__main__':
    data = [l.strip() for l in sys.stdin]
    highest_seat =find_highest_seat(data)
    print("Stage 1:", highest_seat)

    my_seat = find_my_seat(data)
    print("Stage 2:", my_seat)