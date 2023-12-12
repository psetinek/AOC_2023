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

    if r < m - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and \
            (r + 1, c) not in visited:
        visited.add((r + 1, c))
        q.append((r + 1, c))

    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and \
            (r, c - 1) not in visited:
        visited.add((r, c - 1))
        q.append((r, c - 1))

    if c < n - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and \
            (r, c + 1) not in visited:
        visited.add((r, c + 1))
        q.append((r, c + 1))

print(len(visited) // 2)
