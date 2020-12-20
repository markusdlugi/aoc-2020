from itertools import combinations, permutations, product

with open("input/20.txt") as field:
    tiles = [section.splitlines() for section in field.read().split("\n\n")]

tilemap = {}
for tile in tiles:
    id = int(tile[0].split()[1][:-1])
    tile = tile[1:]

    G = {}
    for y, line in enumerate(tile):
        for x, ch in enumerate(line):
            G[(x, y)] = ch
    tilemap[id] = G

width = 10
height = 10


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


dx, dy = ((0, 1, 0, -1), (-1, 0, 1, 0))


def show(tile):
    for y in range(height):
        for x in range(width):
            print(tile[(x, y)], end='')
        print()
    print("====================")


def aligns(a, b):
    #show(a)
    #show(b)
    border_range = {0: (range(width), [0]), 1: ([width - 1], range(height)), 2: (range(width), [height - 1]),
                    3: ([0], range(height))}
    for border in range(4):
        rx, ry = border_range[border]
        align = True
        for x in rx:
            for y in ry:
                try:
                    if a[(x, y)] != b[((x + dx[border]) % width, (y + dy[border]) % height)]:
                        align = False
                        break
                except KeyError:
                    print((x, y), ((x + dx[border]) % width, (y + dy[border]) % height), a, b)
                    raise KeyError
            if not align:
                break
        if align:
            return border
    return -1


arranged = {}
k = next(iter(tilemap.keys()))
# x, y, flipx, flipy, clockwise, counterclockwise
arranged[k] = (0, 0)

unarranged = set(tilemap.keys()).copy()
unarranged.remove(k)

minx = miny = maxx = maxy = None
while len(arranged) < len(tilemap):
    print(len(arranged))
    for a, b in product(arranged.keys(), unarranged):
        if a == b or a not in arranged or b in arranged:
            continue
        # print(a, b)
        ta = tilemap[a]
        tb = tilemap[b]

        bs = [tb, flip(True, False, tb), flip(False, True, tb), flip(True, True, tb), rot(True, tb), rot(False, tb), flip(True, False, rot(True, tb)), flip(True, False, rot(False, tb))]

        found = False
        for i, varb in enumerate(bs):
            border = aligns(ta, varb)
            if border != -1:
                x = arranged[a][0] + dx[border]
                y = arranged[a][1] + dy[border]
                if minx is None or x < minx:
                    minx = x
                elif maxx is None or x > maxx:
                    maxx = x
                if miny is None or y < miny:
                    miny = y
                elif maxy is None or y > maxy:
                    maxy = y
                arranged[b] = (x, y)
                tilemap[b] = varb
                unarranged.remove(b)
                found = True
                break

arr_inv = {v: k for k, v in arranged.items()}

for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        print(arr_inv[(x, y)], end="\t")
    print()


prod_ = 1
for x in [minx, maxx]:
    for y in [miny, maxy]:
        prod_ *= arr_inv[(x, y)]
print(prod_)

for tid, tmap in tilemap.items():
    for x in [0, width - 1]:
        for y in [0, height - 1]:
            del tmap[(x, y)]

seamap = {}

for r, y in enumerate(range(miny, maxy + 1)):
    for yy in range(1, height - 1):
        for c, x in enumerate(range(minx, maxx + 1)):
            k = arr_inv[(x, y)]
            for xx in range(1, width - 1):
                print(tilemap[k][(xx, yy)], end='')
        print()

