from functools import reduce


def read_input(filename):
    with open(filename) as f:
        numbers = [int(n.strip()) for n in f.readline().split(",")]
        grids = [
            [[int(n) for n in line.strip().split()] for line in grid.split("\n")]
            for grid in f.read().strip().split("\n\n")
        ]
        return numbers, grids


def board_scores(input):
    numbers, grids = input
    boards = [list(map(set, grid)) + list(map(set, zip(*grid))) for grid in grids]

    def scores():
        for n in numbers:
            for board in filter(lambda b: b, boards):
                for line in board:
                    if n in line:
                        line.remove(n)
                        if not line:
                            yield sum(
                                reduce(lambda a, b: a.union(b), board) - {n},
                            ) * n
                            board.clear()
                            break

    return scores


if __name__ == "__main__":
    input = read_input(__file__[:-3] + ".txt")
    scores = board_scores(input)

    score = next(scores())
    print(f"Part 1: {score}")

    for score in scores():
        pass
    print(f"Part 2: {score}")