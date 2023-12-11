def extend_sequence(seq):
    # base case
    if all(num == 0 for num in seq):
        return 0

    diff = []
    for i in zip(seq, seq[1:]):
        diff.append(i[1] - i[0])

    return seq[-1] + extend_sequence(diff)


out = 0
with open("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.strip().split(" ")))
        out += extend_sequence(nums)

print(out)
