from collections import namedtuple, defaultdict
import sys
from pprint import pformat


Bag = namedtuple("Bag", "kind color")


class Tree:
    def __init__(self):
        self._parent_to_children = defaultdict(lambda: [])
        self._child_to_parents = defaultdict(lambda: [])

    def add_edge(self, from_, to, count):
        self._parent_to_children[from_].append((to, count))
        self._child_to_parents[to].append(from_)

    def parents(self, bag):
        return self._child_to_parents[bag]

    def children(self, bag):
        return self._parent_to_children[bag]

    def count_bags_outside(self, bag):
        result = set()
        to_check = set(self.parents(bag))

        while to_check:
            current = to_check.pop()
            result.add(current)

            for parent in self.parents(current):
                to_check.add(parent)

        return len(result)

    def count_bags_inside(self, bag):
        total_count = 0
        children = [(c, 1) for c in self.children(bag)]

        while children:
            (child_bag, count), parent_count = children.pop()
            count *= parent_count
            total_count += count
            children.extend([(c, count) for c in self.children(child_bag)])
        
        return total_count

    @staticmethod
    def from_rules(rules):
        tree = Tree()

        for begin, ends in rules:
            for end, count in ends:
                tree.add_edge(begin, end, count)

        return tree

    def __str__(self):
        return pformat(self._parent_to_children)


def parse_bag_part(txt):
    *count, kind, color, _ = txt.strip().split()
    if count:
        count = int(count[0])
    else:
        count = 1

    return Bag(kind, color), count


def parse_rule(txt):
    begin, ends = txt.split('contain')
    ends = ends.strip().rstrip('.')
    begin_bag, _ = parse_bag_part(begin)

    if ends.strip() == 'no other bags':
        end_rules = []
    else:
        end_rules = [parse_bag_part(e) for e in ends.split(",")]

    return begin_bag, end_rules


if __name__ == '__main__':
    rules = [parse_rule(line) for line in sys.stdin]
    tree = Tree.from_rules(rules)
    bag = Bag("shiny", "gold")
    outside_count = tree.count_bags_outside(bag)
    inside_count = tree.count_bags_inside(bag)

    print("Stage 1:", outside_count)
    print("Stage 2:", inside_count)
