# This is a simple brute force solution using some custom classes

class Mapping:
    def __init__(self):
        self.intervals = []

    def insert_interval(self, interval):
        self.intervals.append(interval)

    def get_mapping(self, num):
        for interval in self.intervals:
            if interval.isin(num):
                return interval.get_interval_mapping(num)
        return num


class Interval:
    def __init__(self, dest_start, source_start, length):
        self.dest = [dest_start, dest_start + length - 1]  # inclusive
        self.source = [source_start, source_start + length - 1]

    def isin(self, number):
        # to check whether given number lies in interval
        return self.source[0] <= number <= self.source[1]

    def get_interval_mapping(self, number):
        # to get the mapping
        assert self.source[0] <= number <= self.source[1]
        return self.dest[0] + (number - self.source[0])


with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

mappings = []
new_category = False
n = len(lines)
i = 0
while i < n:
    if i == 0:
        # parse seeds
        _, seeds = lines[i].strip().split(":")
        seeds = seeds.strip()
        seeds_list = seeds.split(" ")
        i += 1
        continue

    if not lines[i]:  # empty line denotes new map
        new_category = True
        i += 2
        continue

    if new_category:
        mappings.append(Mapping())
    new_category = False
    # parse line containing map info
    # create interval
    dest_start, source_start, length = lines[i].strip().split(" ")
    interval = Interval(int(dest_start), int(source_start), int(length))
    mappings[-1].insert_interval(interval)
    i += 1

# push numbers through the mappings
location_numbers = []
for seed in seeds_list:
    curr = int(seed)
    for mapping in mappings:
        curr = mapping.get_mapping(curr)
    location_numbers.append(curr)

print(min(location_numbers))
