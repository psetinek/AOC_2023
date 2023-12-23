import numpy as np


# Had a lot from the reddit thread again...
# we have a perfect quadratic function
# from charr3:
# "Let f(n) be the number of spaces you can reach after n steps. Let X be
# the length of your input grid. f(n), f(n+X), f(n+2X), ...., is a quadratic,
# so you can find it by finding the first 3 values, then use that to
# interpolate the final answer."


def calc_n_steps(n):
    current = set()
    current.add((s_m, s_n))
    for _ in range(n):
        current = simulate(current)
    return len(current)


def simulate(current):
    reachable = set()
    for m, n in current:
        for dm, dn in directions:
            m_new, n_new = m + dm, n + dn
            if grid[m_new % m_max][n_new % n_max] != "#":
                reachable.add((m_new, n_new))
    return reachable


def evaluate_quadratic_equation(points, x):
    # Fit a quadratic polynomial (degree=2) through the points
    coefficients = np.polyfit(*zip(*points), 2)

    # Evaluate the quadratic equation at the given x value
    result = np.polyval(coefficients, x)
    return round(result)


grid = []
with open("input.txt", "r") as file:
    m = 0
    for line in file:
        grid.append(line.strip())
        n = 0
        for c in line.strip():
            if c == "S":
                s_m, s_n = m, n
                # grid[s_m] = grid[s_m].replace("S", ".")
            n += 1
        m += 1

m_max, n_max = len(grid), len(grid[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# f(n), f(n+X), f(n+2X), ...., is a quadratic
# define points
points = [(i, calc_n_steps(65 + i * 131)) for i in range(3)]
print(points)

print(evaluate_quadratic_equation(points, 26501365//m))
