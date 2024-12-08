grid = []

with open('input-dec6.txt', 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        grid.append(line.strip())

sr = None # staring guard row
sc = None # starting guard col
num_row = len(grid)
num_col = len(grid[0])
for r in range(num_row):
    for c in range(num_col):
        if grid[r][c] == "^":
            sr, sc = r, c

ans1 = 0
ans2 = 0

# o_r and o_c means obstable row / column
for o_r in range(num_row):
    for o_c in range(num_col):
        r, c = sr, sc # initalise the guard pos
        d = 0 # initialse the direction : 0 is up, 1 is right, 2 is down, 3 is left
        SEEN = set()
        SEEN_RC = set()
        while True:
            if (r, c, d) in SEEN:
                ans2 += 1
                break
            SEEN.add((r,c,d))
            SEEN_RC.add((r,c))
            dr, dc = [(-1,0), (0,1), (1,0), (0,-1)][d] # to move to where
            rr = r + dr # new row
            cc = c + dc # new col
            # if guard is not in the inner grid
            if not (0 <= rr < num_row and 0 <= cc < num_col):
                # for part 1 only - check if the current o_r o_c position is a default obstable
                if grid[o_r][o_c] == "#": 
                    ans1 = len(SEEN_RC)
                break
            # check if the next step is obstacle or not
            if grid[rr][cc] == "#" or rr == o_r and cc == o_c:
                d = (d + 1) % 4
            else:
                r = rr
                c = cc

print(ans1)
print(ans2)


