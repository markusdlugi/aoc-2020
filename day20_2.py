from collections import Counter

lines = [line.strip() for line in open("input/20_map.txt")]

G = {}
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        G[(x, y)] = ch

width, height = (x, y)


def flip(flipx, flipy, tmap):
    t_new = {}
    for coord, ch in tmap.items():
        x, y = coord
        new_x = width - 1 - x if flipx else x
        new_y = height - 1 - y if flipy else y
        t_new[(new_x, new_y)] = ch
    return t_new


def rot(clockwise, tmap):
    t_new = {}
    for coord, ch in tmap.items():
        x, y = coord
        new_x = y if clockwise else (-y - 1) % height
        new_y = (-x - 1) % width if clockwise else x
        t_new[(new_x, new_y)] = ch
    return t_new


## Looks like this:
##                   #
## #    ##    ##    ###
##  #  #  #  #  #  #
seamonster = [(0, 0), (1, 1), (4, 1), (5, 0), (6, 0), (7, 1), (10, 1), (11, 0), (12, 0), (13, 1), (16, 1), (17, 0), (18, 0), (18, -1), (19, 0)]


def is_seamonster(x, y, seamap):
    exists = True
    for (dx, dy) in seamonster:
        xx, yy = (x + dx, y + dy)
        if (xx, yy) not in seamap or seamap[(xx, yy)] != "#":
            exists = False
            break
    if exists:
        for (dx, dy) in seamonster:
            xx, yy = (x + dx, y + dy)
            seamap[(xx, yy)] = "O"
    return exists


seamonster_count = 0
maps = [G, flip(True, False, G), flip(False, True, G), flip(True, True, G), rot(True, G), rot(False, G), flip(True, False, rot(True, G)), flip(True, False, rot(False, G))]
for i in range(len(maps)):
    seamap = maps[i]
    for y in range(height):
        for x in range(width):
            if is_seamonster(x, y, seamap):
                seamonster_count += 1
    if seamonster_count > 0:
        break

for y in range(height):
    for x in range(width):
        print(seamap[(x, y)], end='')
    print()

hash_count = Counter(G.values())["#"]
seamonster_hashes = seamonster_count * len(seamonster)
print(f"Seamonster Count: {seamonster_count}")
print(f"Non-seamonster hashes: {hash_count - seamonster_hashes}")
