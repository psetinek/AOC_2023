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
    3: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    0: (0, 1),
}
points = [curr]
edges = 0

with open("input.txt", "r") as file:
    for line in file:
        _, _, out = line.split(" ")
        # process out
        out = out.strip().strip("(").strip(")")
        hexa_distance = out[1:-1]
        length = int(hexa_distance, 16)
        direction = int(out[-1])
        edges += int(length)
        end = tuple(a + int(length) * b for a, b in zip(curr, dirs[direction]))
        points.append(end)
        curr = end

print(shoelace(points, edges))
