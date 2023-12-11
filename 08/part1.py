with open("input.txt", "r") as file:
    out = file.read()

directions, nodes = out.split("\n\n")
nodes = nodes.split("\n")

# create adjacency dictionary
adjacencies = {}
for line in nodes:
    node, adjacents = line.split(" = ")
    adjacencies[node] = (adjacents[1:4], adjacents[6:9])


# walk through graph
count = 0
curr_node = "AAA"
while curr_node != "ZZZ":
    if count >= len(directions):
        idx = count % len(directions)
    else:
        idx = count
    if directions[idx] == "L":
        curr_node = adjacencies[curr_node][0]
    else:
        curr_node = adjacencies[curr_node][1]
    count += 1

print(count)
