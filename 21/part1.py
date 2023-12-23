# like game of life so
def simulate(current):
    reachable = set()
    for m, n in current:
        for dm, dn in directions:
            m_new, n_new = m + dm, n + dn
            if 0 <= m_new < m_max and 0 <= n_new < n_max and \
                    grid[m_new][n_new] == ".":
                reachable.add((m_new, n_new))
    return reachable


grid = []
with open("input.txt", "r") as file:
    m = 0
    for line in file:
        grid.append(line.strip())
        n = 0
        for c in line.strip():
            if c == "S":
                s_m, s_n = m, n
                grid[s_m] = grid[s_m].replace("S", ".")
            n += 1
        m += 1

m_max, n_max = len(grid), len(grid[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

current = set()
current.add((s_m, s_n))
for _ in range(64):
    current = simulate(current)

print(len(current))
