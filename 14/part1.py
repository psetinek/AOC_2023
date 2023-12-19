with open("input.txt", "r") as file:
    grid = list(map(list, file.read().split("\n")))


m = len(grid)
n = len(grid[0])
# Tilt board so stones go north
for i in reversed(range(1, m)):
    for j in range(n):
        if grid[i][j] == "O" and grid[i - 1][j] == ".":
            # move current stone north
            grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
            # check if we have stones below to also move north
            r = i
            while r < m - 1 and grid[r + 1][j] == "O":
                grid[r + 1][j], grid[r][j] = grid[r][j], grid[r + 1][j]
                r += 1

out = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "O":
            # Calculate load for each rock
            out += m - i

print(out)
