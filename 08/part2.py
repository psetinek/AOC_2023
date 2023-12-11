from math import gcd


with open("input.txt", "r") as file:
    out = file.read()

directions, nodes = out.split("\n\n")
nodes = nodes.split("\n")

# create adjacency dictionary and start nodes
adjacencies = {}
start_nodes = []
for line in nodes:
    node, adjacents = line.split(" = ")
    adjacencies[node] = (adjacents[1:4], adjacents[6:9])
    if node.endswith("A"):
        start_nodes.append(node)


# walk through graph and find cycles
cycles = []
for node in start_nodes:
    cycle = []
    first_z = None
    count = 0

    while True:
        while count == 0 or not node.endswith("Z"):
            if count >= len(directions):
                idx = count % len(directions)
            else:
                idx = count
            if directions[idx] == "L":
                node = adjacencies[node][0]
            else:
                node = adjacencies[node][1]
            count += 1

        cycle.append(count)
        if not first_z:
            first_z = node
            count = 0
        elif node == first_z:
            break

    cycles.append(cycle)

# find least common multiplier of cycles
nums = [cycle[0] for cycle in cycles]
lcm = nums.pop()
for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)
