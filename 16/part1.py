from collections import deque

with open("input.txt", "r") as file:
    grid = []
    for line in file:
        grid.append(line.strip())

m = len(grid)
n = len(grid[0])

# keep track of beamcounts for each cell
beamcounts = []
for i in range(len(grid)):
    beamcounts.append([])
    for j in range(len(grid[0])):
        beamcounts[i].append(set())

q = deque()
q.append((0, 0, (0, 1)))

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
out = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if len(beamcounts[i][j]) > 0:
            out += 1

print(out)
