grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

m, n = len(grid), len(grid[0])

slopes = {"^": 0, ">": 1, "v": 2, "<": 3}
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# iterative dfs (recursive reached recursion limit)
def iterative_dfs(start_r, start_c):
    stack = [(start_r, start_c, 0, set([(start_r, start_c)]))]
    max_length = 0

    while stack:
        r, c, curr_len, curr_visited = stack.pop()

        # check for reaching the bottom row
        if r == m - 1 and grid[r][c] == '.':
            max_length = max(max_length, curr_len)
            continue

        # explore adjacent nodes
        next_moves = []
        if grid[r][c] in slopes:
            dr, dc = dirs[slopes[grid[r][c]]]
            next_moves.append((dr, dc))
        else:
            next_moves = dirs

        for dr, dc in next_moves:
            new_r, new_c = r + dr, c + dc
            if (0 <= new_r < m and 0 <= new_c < n and
                    grid[new_r][new_c] != '#' and (new_r, new_c)
                    not in curr_visited):
                new_visited = curr_visited.copy()
                new_visited.add((new_r, new_c))
                stack.append((new_r, new_c, curr_len + 1, new_visited))

    return max_length


# get output
start_col = grid[0].index('.')
longest_hike = iterative_dfs(0, start_col)

print(longest_hike)
