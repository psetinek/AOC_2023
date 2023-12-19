def process_character(curr, char):
    ascii_value = ord(char)
    curr += ascii_value
    curr *= 17
    curr = curr % 256
    return curr


out = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.split(",")
        for step in line:
            curr = 0
            for char in step:
                curr = process_character(curr, char)
            out += curr

print(out)
