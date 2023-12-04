out = 0
with open('input.txt', 'r') as file:
    for line in file:
        count = -1
        left, right = line.strip().split(' | ')
        _, left = left.split(':')
        valid_nums = set()
        for num in left.strip().split(' '):
            if num.strip():
                valid_nums.add(int(num.strip()))
        for num in right.strip().split(' '):
            if num.strip():
                if int(num.strip()) in valid_nums:
                    count += 1
        out += 0 if count == -1 else 2**count

print(out)
