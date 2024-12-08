from itertools import combinations
import numpy as np

PATH = './input/input-dec8.txt'
grid = []
atennas = set()
with open(PATH, 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        grid.append(line.strip())
        for element in line.strip():
            if element != ".":
                atennas.add(element)

num_row = len(grid)
num_col = len(grid[0])

antinodes = set()

for atenna in atennas:
    positions = []
    print("looking for", atenna, "at :")
    for r in range(num_row):
        for c in range(num_col):
            if grid[r][c] == atenna:
                positions.append((r,c))

    combos = combinations(positions, 2)
    for combo in combos:
        antinodes.add(combo[0])
        antinodes.add(combo[1])
        a = np.array(combo[0])
        b = np.array(combo[1])
        upper = None
        lower = None
        diff = (a - b)
        if a[0] < b[0]:
            upper = a + diff
            lower = b - diff
        else:
            upper = b + diff
            lower = a - diff
        while 0 <= upper[0] < num_row and 0 <= upper[1] < num_col:
            print(upper)
            antinodes.add(tuple(upper))
            upper = upper + diff
        while 0 <= lower[0] < num_row and 0 <= lower[1] < num_col:
            print(lower)
            antinodes.add(tuple(lower))
            lower = lower - diff
        # if 0 <= upper[0] < num_row and 0 <= upper[1] < num_col:
        #     antinodes.add(tuple(upper))
        # if 0 <= lower[0] < num_row and 0 <= lower[1] < num_col:
        #     antinodes.add(tuple(lower))
        # else:
        #     continue
print(len(antinodes))