from collections import Counter
from timeit import default_timer as timer

visible_seats = dict()


def moves(grid, x, y, new_rules):
    global visible_seats
    dx, dy = ((0, 1, 1, 1, 0, -1, -1, -1), (-1, -1, 0, 1, 1, 1, 0, -1))
    for i in range(8):
        if (x, y, i) in visible_seats:
            new_pos = visible_seats[(x, y, i)]
        else:
            new_pos = (x + dx[i], y + dy[i])
            while new_rules and new_pos in grid and grid[new_pos] == ".":
                new_pos = (new_pos[0] + dx[i], new_pos[1] + dy[i])
            visible_seats[(x, y, i)] = new_pos
        yield grid[new_pos] if new_pos in grid else None


def show(grid, max_x, max_y):
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            print(grid[(x, y)], sep='', end='')
        print()
    print()


def simulate(grid, new_rules):
    changes = True
    while changes:
        changes = False
        new_grid = grid.copy()

        for (x, y), state in grid.items():
            adj_count = Counter(moves(grid, x, y, new_rules))["#"]
            if state == "L" and adj_count == 0:
                new_grid[(x, y)] = "#"
                changes = True
            if state == "#" and adj_count >= (5 if new_rules else 4):
                new_grid[(x, y)] = "L"
                changes = True
        grid = new_grid
        # show(grid, max_x, max_y)
    return grid


lines = [line.strip() for line in open("input/11.txt")]

grid = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x, y)] = c

max_x, max_y = (x, y)

# Part A
start = timer()
original_grid = grid.copy()
grid = simulate(grid, False)
occ = Counter(grid.values())["#"]
print(occ)

# Part B
visible_seats.clear()
grid = original_grid.copy()
grid = simulate(grid, True)
occ = Counter(grid.values())["#"]
print(occ)
end = timer()
print(f'Took {end - start} seconds.')
