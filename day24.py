import re
from collections import defaultdict

lines = [line.strip() for line in open("input/24.txt")]

d = {"nw": 0, "ne": 1, "e": 2, "se": 3, "sw": 4, "w": 5}
dx, dy, dz = ((0, 1, 1, 0, -1, -1), (1, 0, -1, -1, 0, 1), (-1, -1, 0, 1, 1, 0))
paths = [[d[x] for x in re.findall(r"(nw|ne|sw|se|e|w)", line)] for line in lines]

tiles = defaultdict(int)
for path in paths:
    x, y, z = (0, 0, 0)
    for dir in path:
        x, y, z = (x + dx[dir], y + dy[dir], z + dz[dir])
    tiles[(x, y, z)] += 1

G = set([k for k, v in tiles.items() if v % 2 == 1])
print(len(G))


def neighbours(x, y, z):
    for i in range(6):
        yield (x + dx[i], y + dy[i], z + dz[i])


def count_active(G, pos):
    sum_ = 0
    for neighbor in neighbours(*pos):
        if neighbor in G:
            sum_ += 1
    return sum_


def simulate(G):
    for i in range(100):
        new_G = G.copy()

        changeset = set()
        for pos in G:
            changeset.add(pos)
            changeset.update(neighbours(*pos))

        for pos in changeset:
            state = "#" if pos in G else "."
            adj_count = count_active(G, pos)
            if state == "#" and (adj_count > 2 or adj_count == 0):
                new_G.remove(pos)
            if state == "." and adj_count == 2:
                new_G.add(pos)
        G = new_G
    return G


G = simulate(G)
print(len(G))
