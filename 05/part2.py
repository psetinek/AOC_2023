# For part 2, we cannot use a brute force top-down solution like in part 1
# anymore, because it would take O(n) time to compute the min and n is too
# large...

# What do instead is to go mapping by mapping and flick together our new
# seeds after eacht block. The new seeds at the end will be the locations.

with open('input.txt', 'r') as file:
    content = file.read()
    seeds, *mappings = content.split("\n\n")

# create list for seeds with pairs: [range_start, range_end)
seeds = list(map(int, seeds.split(":")[1].strip().split(" ")))
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i+1]))

# iterate over mappings
for mapping in mappings:
    # create ranges for one mapping
    ranges = []
    for line in mapping.splitlines()[1:]:
        dest_start, source_start, length = list(map(int, line.split(" ")))
        ranges.append((dest_start, source_start, length))

    # push seeds through mapping
    new = []
    while seed_ranges:
        start, end = seed_ranges.pop()
        for dest_start, source_start, length in ranges:
            overlap_start = max(start, source_start)
            overlap_end = min(end, source_start + length)
            if overlap_start < overlap_end:
                # overlap is not empty
                new.append((overlap_start - source_start + dest_start,
                            overlap_end - source_start + dest_start))
                if overlap_start > start:
                    seed_ranges.append((start, overlap_start))
                if end > overlap_end:
                    seed_ranges.append((overlap_end, end))
                break
        else:
            new.append((start, end))
    seed_ranges = new

print(min(seed_ranges)[0])
