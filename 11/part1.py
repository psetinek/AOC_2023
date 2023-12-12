with open("input.txt", "r") as file:
    grid = file.readlines()

m = len(grid)
n = len(grid[0])

# get empty rows
empty_rows = []
for i in range(m):
    if "#" not in grid[i]:
        empty_rows.append(i)

# get empty cols
empty_cols = []
for c, col in enumerate(zip(*grid)):
    if "#" not in col:
        empty_cols.append(c)

# calculate minimum distances
galaxies = [(i, j) for i in range(m) for j in range(m) if grid[i][j] == "#"]
out = 0
for i, (r1, c1) in enumerate(galaxies):
    for (r2, c2) in galaxies[:i]:
        for r in range(min(r1, r2), max(r1, r2)):
            out += 2 if r in empty_rows else 1
        for c in range(min(c1, c2), max(c1, c2)):
            out += 2 if c in empty_cols else 1

print(out)
