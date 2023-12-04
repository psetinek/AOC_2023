digits = "0123456789"
res = 0
# open file
with open('input.txt', 'r') as file:
    # read line by line
    for line in file:
        for i in range(len(line)):
            if line[i] in digits:
                first = line[i]
                break
        for i in reversed(range(len(line))):
            if line[i] in digits:
                last = line[i]
                break
        res = res + int(first + last)

print(res)
