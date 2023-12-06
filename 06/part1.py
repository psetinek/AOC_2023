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
    times = list(map(int, lines[0].strip().split(":")[1].split()))
    distances = list(map(int, lines[1].strip().split(":")[1].split()))

ranges = []
for i in range(len(times)):
    ranges.append(solve_quadratic(times[i], distances[i]))

out = 1
for start, end in ranges:
    diff = math.ceil(end) - (int(start) + 1)
    out *= diff

print(out)
