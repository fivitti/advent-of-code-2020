import sys
from functools import reduce


class Terrain:
    def __init__(self, data):
        self._data = data

    def is_tree(self, coordinates):
        row, col = self._normalize_coordinates(coordinates)
        return self._data[row][col] == '#'

    def get_size(self):
        height = len(self._data)
        width = len(self._data[0])
        return height, width

    def _normalize_coordinates(self, coordinates):
        height, width = self.get_size()
        row, col = coordinates
        return row % height, col % width


def count_trees(terrain, move):
    row, col = 0, 0
    bottom, right = move

    end_row, _ = terrain.get_size()

    trees = 0

    while row < end_row:
        if terrain.is_tree((row, col)):
            trees += 1
        row += bottom
        col += right

    return trees


def product_of_encounters(terrain):
    moves = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    trees = [count_trees(terrain, m) for m in moves]
    return reduce(lambda acc, val: acc * val, trees, 1)

if __name__ == '__main__':
    terrain = Terrain([l.strip() for l in sys.stdin])
    trees = count_trees(terrain, (1, 3))
    encounters = product_of_encounters(terrain)

    print("Stage 1:", trees)
    print("Stage 2:", encounters)
