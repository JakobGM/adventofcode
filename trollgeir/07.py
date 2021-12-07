import numpy as np

with open("inputs/07.txt") as f:
    initial_alignments = np.array([i for i in f.readline().split(",")]).astype(int)


def calculate_fuel(initial_alignments, constant_rate=True):
    dim1 = initial_alignments.max()
    dim2 = len(initial_alignments)
    alignment_goals = np.tile(range(dim1), dim2).reshape(dim2, dim1).T
    diff = abs(initial_alignments - alignment_goals).T
    if not constant_rate:
        fuel = sum(diff * (diff + 1) / 2)  # formula: n*(n+1)/2
    else:
        fuel = sum(diff)
    return fuel.min()


answer1 = calculate_fuel(input)
answer2 = calculate_fuel(input, constant_rate=False)

print(f"Answer1: {answer1}")  # 348664
print(f"Answer2: {answer2}")  # 100220525.0
