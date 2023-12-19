from collections import deque

with open("input.txt", "r") as file:
    grid = []
    for line in file:
        grid.append(line.strip())

m = len(grid)
n = len(grid[0])

# configure all possible starting beams
configurations = []
# beams from top and bottom
for j in range(n):
    configurations.append((0, j, (1, 0)))
    configurations.append((m - 1, j, (-1, 0)))
# beams from left and right
for i in range(m):
    configurations.append((i, 0, (0, 1)))
    configurations.append((i, n - 1, (0, -1)))

max_energized = 0
for configuration in configurations:
    # keep track of beamcounts for each cell
    beamcounts = []
    for i in range(len(grid)):
        beamcounts.append([])
        for j in range(len(grid[0])):
            beamcounts[i].append(set())

    q = deque()
    q.append(configuration)

    while q:
        beam = q.popleft()
        while 0 <= beam[0] < len(grid) and 0 <= beam[1] < len(grid[0]) and \
                beam[2] not in beamcounts[beam[0]][beam[1]]:

            # append it to seen
            beamcounts[beam[0]][beam[1]].add(beam[2])

            if grid[beam[0]][beam[1]] == '.':
                beam = (beam[0] + beam[2][0], beam[1] + beam[2][1], beam[2])

            elif grid[beam[0]][beam[1]] == '|':
                if beam[2] == (1, 0) or beam[2] == (-1, 0):
                    beam = (beam[0] + beam[2][0], beam[1], beam[2])
                else:
                    b1 = (beam[0] - 1, beam[1], (-1, 0))
                    b2 = (beam[0] + 1, beam[1], (1, 0))
                    q.append(b1)
                    q.append(b2)
                    break

            elif grid[beam[0]][beam[1]] == '-':
                if beam[2] == (0, 1) or beam[2] == (0, -1):
                    beam = (beam[0], beam[1] + beam[2][1], beam[2])
                else:
                    b1 = (beam[0], beam[1] - 1, (0, -1))
                    b2 = (beam[0], beam[1] + 1, (0, 1))
                    q.append(b1)
                    q.append(b2)
                    break

            elif grid[beam[0]][beam[1]] == '/':
                if beam[2] == (0, 1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                elif beam[2] == (-1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))

            else:
                if beam[2] == (0, 1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                elif beam[2] == (1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))

    # calculate energized tiles
    energized = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if len(beamcounts[i][j]) > 0:
                energized += 1

    max_energized = max(max_energized, energized)

print(max_energized)
