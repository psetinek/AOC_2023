import copy

with open("input.txt", "r") as file:
    grid = list(map(list, file.read().split("\n")))


def tilt(grid):
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


def rotate(grid):
    m = len(grid)
    n = len(grid[0])
    # Rotate by 90 deg clockwise
    new_grid = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            new_grid[j][m-1-i] = grid[i][j]
    return new_grid


def do_cycle(grid):
    for i in range(4):
        tilt(grid)
        rotated_grid = rotate(grid)
        grid = copy.deepcopy(rotated_grid)
    return grid


def hash_grid(grid):
    return "\n".join(["".join(line) for line in grid])


def calc_load(grid):
    m = len(grid)
    n = len(grid[0])
    out = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "O":
                # Calculate load for each rock
                out += m - i
    return out


cycle2grid = {}
seen = {}
for cycle in range(1000000000):
    grid = do_cycle(grid)
    h = hash_grid(grid)
    if h in seen:
        period = cycle - seen[h]
        final_grid = cycle2grid[(10**9 - 1 - seen[h]) % period + seen[h]]
        print(calc_load(final_grid))
        break

    seen[h] = cycle
    cycle2grid[cycle] = copy.deepcopy(grid)
