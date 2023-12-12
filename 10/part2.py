from collections import deque


# furtherst point is at exactly in the middle of the loop
with open("input.txt", "r") as file:
    grid = [line.strip() for line in file]

directions = [None] * 2

# find start
m = len(grid)
n = len(grid[0])
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            start_row, start_col = i, j

# start bfs
# need to find character that is actually represented by s
s_actually = {"|", "-", "J", "L", "7", "F"}
visited = set()
visited.add((start_row, start_col))
q = deque([(start_row, start_col)])
while q:
    r, c = q.popleft()
    ch = grid[r][c]

    if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and \
            (r - 1, c) not in visited:
        visited.add((r - 1, c))
        q.append((r - 1, c))
        if ch == "S":
            s_actually &= {"|", "J", "L"}

    if r < m - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and \
            (r + 1, c) not in visited:
        visited.add((r + 1, c))
        q.append((r + 1, c))
        if ch == "S":
            s_actually &= {"|", "7", "F"}

    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and \
            (r, c - 1) not in visited:
        visited.add((r, c - 1))
        q.append((r, c - 1))
        if ch == "S":
            s_actually &= {"-", "J", "7"}

    if c < n - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and \
            (r, c + 1) not in visited:
        visited.add((r, c + 1))
        q.append((r, c + 1))
        if ch == "S":
            s_actually &= {"-", "L", "F"}

# check if we found the character that s actually represents
assert len(s_actually) == 1

# replace S with the appropriate character
s_replacement, = s_actually
grid = [row.replace("S", s_replacement) for row in grid]

# new grid for counting
grid = ["".join(ch if (r, c) in visited else "." for c, ch in enumerate(row))
        for r, row in enumerate(grid)]


# find outside elements in grid
outside = set()

for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"unexpected character (horizontal): {ch}")
        if not within:
            outside.add((r, c))

print(len(grid) * len(grid[0]) - len(outside | visited))
