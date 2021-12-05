from collections import defaultdict
import re


def read_input(filename):
    with open(filename) as f:
        return [tuple(int(n) for n in (re.findall("\d+", line))) for line in f]


def count_overlaps(lines):
    seafloor = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        dx = 1 if x1 < x2 else -1 if x1 > x2 else 0
        dy = 1 if y1 < y2 else -1 if y1 > y2 else 0
        for i in range(max(x1 - x2, x2 - x1, y1 - y2, y2 - y1) + 1):
            seafloor[(x1 + i * dx, y1 + i * dy)] += 1

    return sum(1 for n in seafloor.values() if n > 1)


if __name__ == "__main__":
    input = read_input(__file__[:-3] + ".txt")

    # Part 1
    result = count_overlaps(l for l in input if l[0] == l[2] or l[1] == l[3])
    print(f"Part 1: {result}")

    # Part 2
    result = count_overlaps(input)
    print(f"Part 2: {result}")
