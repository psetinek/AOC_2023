# Could not solve this by myself. Thanks to the community on reddit for
# telling me about the shoelace formula:)

def shoelace(points, edges):
    r = 0
    for i in range(len(points) - 1):
        y1, x1 = points[i]
        y2, x2 = points[i + 1]
        r += x1 * y2 - x2 * y1

    return abs(r) // 2 + edges // 2 + 1


curr = (0, 0)
dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
points = [curr]
edges = 0

with open("input.txt", "r") as file:
    for line in file:
        direction, length, _ = line.split(" ")
        edges += int(length)
        end = tuple(a + int(length) * b for a, b in zip(curr, dirs[direction]))
        points.append(end)
        curr = end

print(shoelace(points, edges))
