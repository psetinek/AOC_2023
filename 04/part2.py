from collections import defaultdict

with open('input.txt', 'r') as file:
    number_of_copies = defaultdict(int)
    for id, line in enumerate(file):
        card_num = id + 1
        count = 0
        left, right = line.strip().split(' | ')
        _, left = left.split(':')

        # set of valid nums
        valid_nums = set()
        for num in left.strip().split(' '):
            if num.strip():
                valid_nums.add(int(num.strip()))

        # check for matches
        for num in right.strip().split(' '):
            if num.strip():
                if int(num.strip()) in valid_nums:
                    count += 1

        while count > 0:
            number_of_copies[card_num + count] = \
                number_of_copies[card_num + count] + 1 \
                + number_of_copies[card_num]
            count -= 1

out = 0
for num_copies in number_of_copies.values():
    out += num_copies
out += card_num

print(out)
