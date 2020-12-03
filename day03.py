grid = [line.strip() for line in open("input/03.txt")]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for x, y in slopes:
    r, c = (0, 0)
    trees = 0
    while (r + 1) < len(grid):
        c = (c + x) % len(grid[0])
        r += y
        if grid[r][c] == "#":
            trees += 1
    results.append(trees)

print(results[1])

product = 1
for result in results:
    product *= result
print(product)
