import re
import copy

# helper lookup table
lookup = {"x": 0, "m": 1, "a": 2, "s": 3}

out_ranges = []


def process_workflow(name, ranges):
    # base cases
    if name == "A":
        out_ranges.append(ranges)
        return
    if name == "R":
        return

    # recurrence relation
    workflow = workflows[name]
    regex_cond = re.compile(r"([xmas])([<>])(\d+):([a-zAR]+)")
    conditions = workflow[0]
    for condition in conditions:
        match = re.match(regex_cond, condition)
        variable, smaller_larger, num, out = match.groups()
        num = int(num)

        if smaller_larger == "<":
            # split intervals
            ranges_new = copy.deepcopy(ranges)
            ranges_new[lookup[variable]] = (ranges_new[lookup[variable]][0],
                                            num - 1)
            ranges[lookup[variable]] = (num, ranges[lookup[variable]][1])
            process_workflow(out, ranges_new)

        elif smaller_larger == ">":
            # split intervals
            ranges_new = copy.deepcopy(ranges)
            ranges_new[lookup[variable]] = (num + 1,
                                            ranges_new[lookup[variable]][1])
            ranges[lookup[variable]] = (ranges[lookup[variable]][0], num)
            process_workflow(out, ranges_new)

        else:
            raise ValueError

    return process_workflow(workflow[1], ranges)


with open("input.txt", "r") as file:
    inputs = file.read()
    workflows, parts = inputs.split("\n\n")
    workflows_raw = workflows.split("\n")
    parts_raw = parts.split("\n")

# workflow parsing
workflows = {}
regex = re.compile(r"([a-z]+){((?:[xmas][<>]\d+:[a-zAR]+,)+)([a-zAR]+)}")
for wf in workflows_raw:
    match = re.match(regex, wf)
    prefix = match.group(1)
    conditions_group = match.group(2)
    suffix = match.group(3)
    # Split individual conditions
    conditions = conditions_group.split(',')
    workflows[prefix] = [(conditions[:-1]), suffix]

# parts can be all in range(0, 5)
ranges = [(1, 4000) for i in range(4)]
# m = [(1, 4000)]
# a = [(1, 4000)]
# s = [(1, 4000)]
process_workflow("in", ranges)

# # calc result
out = 0
for i in out_ranges:
    possibilities = 1
    for j in i:
        possibilities *= (j[1] - j[0] + 1)
    out += possibilities

print(out)
# print(res)
