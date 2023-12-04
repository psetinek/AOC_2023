def check_neighbours(i, j, neighbours):
    visited = set()
    nums = []
    for di, dj in neighbours:
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < m and 0 <= new_j < n:
            # check if we find digit
            if grid[new_i][new_j].isdigit() and (new_i, new_j) not in visited:
                visited.add((new_i, new_j))
                # get the total number that is adjacent
                dl, dr = -1, 1
                while new_j + dl >= 0 and grid[new_i][new_j + dl].isdigit():
                    visited.add((new_i, new_j + dl))
                    dl -= 1
                dl += 1
                while new_j + dr < n and grid[new_i][new_j + dr].isdigit():
                    visited.add((new_i, new_j + dr))
                    dr += 1
                dr -= 1
                num = grid[new_i][new_j + dl: new_j + dr + 1]
                # full number
                nums.append(int("".join(num)))

    if len(nums) == 2:
        return nums[0] * nums[1]
    else:
        return 0


with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
              (1, -1), (0, -1)]
m, n = len(grid), len(grid[0])
i, j = 0, 0
out = 0
while i < m:
    j = 0
    while j < n:
        curr = grid[i][j]
        if curr == "*":
            # found a potential gear
            # check if it has two adjacent numbers
            gear = check_neighbours(i, j, neighbours)
            out += gear
        j += 1
    i += 1

print(out)
