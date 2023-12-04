from collections import defaultdict

out = 0
with open('input.txt', 'r') as file:
    for id, line in enumerate(file):
        min_cubes = defaultdict(int)
        line = line.strip().split(":")
        _, info = line[0], line[1]
        rounds = info.split(";")
        for round in rounds:
            for draw in round.strip().split(","):
                draw = draw.strip().split(" ")
                if min_cubes[draw[1]] < int(draw[0]):
                    min_cubes[draw[1]] = int(draw[0])
        power_sum = 1
        for colour, minimum in min_cubes.items():
            power_sum *= minimum
        out += power_sum

print(out)
