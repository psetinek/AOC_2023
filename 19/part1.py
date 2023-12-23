import re
import operator

# helper lookup table
lookup = {"x": 0, "m": 1, "a": 2, "s": 3}


def process_workflow(workflow, part):
    regex_cond = re.compile(r"([xmas])([<>])(\d+):([a-zAR]+)")
    conditions = workflow[0]
    operators = {'<': operator.lt, '>': operator.gt}
    for condition in conditions:
        match = re.match(regex_cond, condition)
        variable, smaller_larger, num, out = match.groups()
        num = int(num)

        # Get the function corresponding to the operator
        op_func = operators[smaller_larger]

        # Perform the comparison and return the output if true
        if op_func(part[lookup[variable]], num):
            return out
    return workflow[1]


with open("input.txt", "r") as file:
    inputs = file.read()
    workflows, parts = inputs.split("\n\n")
    workflows_raw = workflows.split("\n")
    parts_raw = parts.split("\n")

# Parts parsing
parts = set()
regex = re.compile("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
for part in parts_raw:
    match = re.fullmatch(regex, part)
    parts.add(tuple(map(int, match.groups())))

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

# calc result
res = 0
for part in parts:
    out = process_workflow(workflows["in"], part)
    while out not in "AR":
        out = process_workflow(workflows[out], part)
    if out == "A":
        for i in part:
            res += i

print(res)
