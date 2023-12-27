# need to prune graph

data = []
with open("input.txt", "r") as file:
    for line in file:
        data.append(line.strip())

m, n = len(data), len(data[0])

slopes = {"^": 0, ">": 1, "v": 2, "<": 3}
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

edges = {}  # (r, c) -> (ar, ac, length)
for r, row in enumerate(data):
    for c, v in enumerate(row):
        if v in ".>v":
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ar, ac = r + dr, c + dc
                if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                    continue
                if data[ar][ac] in ".>v":
                    edges.setdefault((r, c), set()).add((ar, ac, 1))
                    edges.setdefault((ar, ac), set()).add((r, c, 1))

# remove nodes with only two adjacent edges by merging the edges
while True:
    for n, e in edges.items():
        if len(e) == 2:
            a, b = e
            edges[a[:2]].remove(n + (a[2],))
            edges[b[:2]].remove(n + (b[2],))
            edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
            edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
            del edges[n]
            break
    else:
        break

n, m = len(data), len(data[0])

q = [(0, 1, 0)]
visited = set()
best = 0
while q:
    r, c, d = q.pop()
    if d == -1:
        visited.remove((r, c))
        continue
    if (r, c) == (n - 1, m - 2):
        best = max(best, d)
        continue
    if (r, c) in visited:
        continue
    visited.add((r, c))
    q.append((r, c, -1))
    for ar, ac, l in edges[(r, c)]:
        q.append((ar, ac, d + l))

print(best)
