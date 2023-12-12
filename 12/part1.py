def get_cnfgs(chars, nums):
    # base cases
    if not chars:
        return 1 if not nums else 0
    if not nums:
        return 0 if "#" in chars else 1

    # recurrence relation
    result = 0
    if chars[0] in ".?":
        result += get_cnfgs(chars[1:], nums)
    if chars[0] in "#?":
        if nums[0] <= len(chars) and "." not in chars[:nums[0]] and \
                (nums[0] == len(chars) or chars[nums[0]] != "#"):
            result += get_cnfgs(chars[nums[0] + 1:], nums[1:])

    return result


out = 0
with open("input.txt", "r") as file:
    for line in file:
        chars = line.strip().split(" ")[0]
        nums = list(map(int, line.strip().split(" ")[1].split(",")))
        out += get_cnfgs(chars, nums)

print(out)
