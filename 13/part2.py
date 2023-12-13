def horizontal(block):
    m = len(block)
    n = len(block[0])

    for i in range(1, m):
        # loop to check different possible mirror lines
        min_same = min(i, m - i)
        smudge = 0
        for di in range(1, min_same + 1):
            for j in range(n):
                # check for smudge
                if block[i - di][j] != block[i + di - 1][j]:
                    smudge += 1
        if smudge == 1:
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
