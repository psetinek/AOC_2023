bag = {"red": 12, "green": 13, "blue": 14}
out = 0
with open('input.txt', 'r') as file:
    for id, line in enumerate(file):
        is_possible = True
        line = line.strip().split(":")
        _, info = line[0], line[1]
        rounds = info.split(";")
        for round in rounds:
            for draw in round.strip().split(","):
                draw = draw.strip().split(" ")
                if bag[draw[1]] < int(draw[0]):
                    is_possible = False
                    break
            if not is_possible:
                break
        if is_possible:
            out += id + 1

print(out)
