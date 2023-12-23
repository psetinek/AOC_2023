import heapq


with open("input.txt", "r") as file:
    grid = []
    for line in file:
        grid.append(line.strip())

m = len(grid)
n = len(grid[0])
start = (0, 0)
end = (m - 1, n - 1)

# use minheap for traversal
visited = {}  # {(pos, dir): loss}
q = [(0, start, -1, 0)]  # (loss, pos, dir, dir_continuous)

# store all losses in list
losses = []

# define direction as a number indicating the index in directions list
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up, left, down, right

while q:
    loss, pos, d, d_c = heapq.heappop(q)

    # break if we reached the end
    if pos == end:
        break

    # dont allow same direction and opposite direction
    allowed_dirs = [_d for _d in range(4) if _d != d and (_d + 2) % 4 != d]

    for _d in allowed_dirs:
        _next_loss = loss
        for d_cont in range(1, 4):
            _next_pos = tuple(a + b * d_cont for a, b in zip(pos,
                                                             directions[_d]))
            if 0 <= _next_pos[0] < m and 0 <= _next_pos[1] < n:
                _next_loss += int(grid[_next_pos[0]][_next_pos[1]])
                if _next_loss < visited.get((_next_pos, _d), float("inf")):
                    visited[(_next_pos, _d)] = _next_loss
                    if d_cont >= 1:
                        heapq.heappush(q, (_next_loss, _next_pos, _d, d_cont))

print(loss)
