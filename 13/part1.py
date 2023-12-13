def horizontal(block):
    m = len(block)

    for i in range(1, m):
        # loop to check different possible mirror lines
        min_same = min(i, m - i)
        for di in range(1, min_same + 1):
            if block[i - di] != block[i + di - 1]:
                break
        else:
            # return numbers of rows above mirror
            return i
    return 0


with open("input.txt", "r") as file:
    data = file.read().split("\n\n")

out = 0
for block in data:
    block = block.split("\n")
    # check horizontal lines
    out += 100 * horizontal(block)
    # check vertical lines
    transposed_block = ["".join(row) for row in zip(*block)]
    out += horizontal(transposed_block)

print(out)
