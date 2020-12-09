from itertools import combinations

lines = list(map(int, open("input/09.txt")))

# Part A
target = 0
numbers = []
for num in lines:
    if len(numbers) < 25:
        numbers.append(num)
        continue
    valid = False
    for a, b in combinations(numbers, 2):
        if a + b == num:
            valid = True
            break
    if not valid:
        target = num
        break
    numbers.append(num)
    del numbers[0]
print(target)

# Part B
numbers = []
for num in lines:
    numbers.append(num)
    sum_ = sum(numbers)
    while sum_ > target:
        sum_ -= numbers[0]
        del numbers[0]
    if sum_ == target:
        print(min(numbers) + max(numbers))
        break
