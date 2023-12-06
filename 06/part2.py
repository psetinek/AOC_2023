import math


# distance at the end can be described with function: d(h) = h * (T-h)
# = Th - h**2
# so we can find h by solving a quadratic equation
def solve_quadratic(time, distance):
    pre = time/2
    post = math.sqrt(pre**2 - distance)
    return pre - post, pre + post


with open("input.txt", "r") as file:
    lines = file.readlines()
    times = lines[0].strip().split(":")[1].split()
    time = int("".join(times))
    distances = lines[1].strip().split(":")[1].split()
    distance = int("".join(distances))

start, end = solve_quadratic(time, distance)
diff = math.ceil(end) - (int(start) + 1)

print(diff)
