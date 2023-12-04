def check_neighbours(i, j, neighbours):
    for di, dj in neighbours:
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < m and 0 <= new_j < n:
            if not grid[new_i][new_j].isdigit() and \
                    not grid[new_i][new_j] == '.':
                return True
    return False


with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

neighbours_left = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)]
neighbours_right = [(-1, 1), (0, 1), (1, 1)]
neighbours_middle = [(-1, 0), (1, 0)]
m, n = len(grid), len(grid[0])
i, j = 0, 0
out = 0
while i < m:
    j = 0
    while j < n:
        curr = grid[i][j]
        num = []
        has_adjacents = False
        count = 0
        while curr.isdigit():
            if count == 0:
                # check left corner
                has_adjacents = check_neighbours(i, j, neighbours_left)
            else:
                # check middle
                has_adjacents = has_adjacents or \
                    check_neighbours(i, j, neighbours_middle)
            num.append(curr)
            count += 1
            j += 1
            if j < n:
                curr = grid[i][j]
            else:
                break

        if num:
            # check right
            j -= 1
            has_adjacents = has_adjacents or \
                check_neighbours(i, j, neighbours_right)
            # if it has adjacent special character
            if has_adjacents:
                out += int("".join(num))
        j += 1
    i += 1

print(out)
