digits = "0123456789"
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
           "seven": 7, "eight": 8, "nine": 9}
res = 0
# open file
with open('./01/in.txt', 'r') as file:
    # read line by line
    for line in file:
        first = None
        last = None
        s = ""
        dig = None
        line = line.rstrip()
        for c in line:
            if c.isdigit():
                dig = c
            else:
                s += c
                for k, v in numbers.items():
                    if s.endswith(k):
                        dig = str(v)
            if dig is not None:
                last = dig
                if first is None:
                    first = dig
        res += int(first + last)

print(res)
