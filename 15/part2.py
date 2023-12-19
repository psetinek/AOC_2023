def process_label(label):
    curr = 0
    for i in range(len(label)):
        ascii_value = ord(label[i])
        curr += ascii_value
        curr *= 17
        curr = curr % 256
    return curr


# letters in the beginning is label
boxes = [[] for i in range(256)]

with open("input.txt", "r") as file:
    for line in file:
        line = line.split(",")
        for step in line:
            if "-" in step:
                label = step[:step.index("-")]
                box = process_label(label)
                lens = list(filter(lambda x: x[0] == label, boxes[box]))
                if len(lens) > 0:
                    idx = boxes[box].index(lens[0])
                    boxes[box].pop(idx)

            if "=" in step:
                label = step[:step.index("=")]
                box = process_label(label)
                focal_len = int(step[step.index("=")+1:])

                lens = list(filter(lambda x: x[0] == label, boxes[box]))
                if len(lens) > 0:
                    idx = boxes[box].index(lens[0])
                    boxes[box][idx] = [label, focal_len]
                else:
                    boxes[box].append([label, focal_len])

out = 0
for i in range(256):
    if boxes[i]:
        for idx, slot in enumerate(boxes[i]):
            print(idx, slot[1])
            out = out + (i + 1) * (idx + 1) * slot[1]

print(out)
