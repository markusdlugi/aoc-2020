from timeit import default_timer as timer

start = timer()
lines = [line.strip() for line in open("input/15.txt")]

numbers = [int(x) for x in lines[0].split(",")]

D = {}
for i, num in enumerate(numbers):
    D[num] = i

t = len(numbers) - 1
previous = numbers[-1]
end1 = None
while t < 30_000_000 - 1:
    if end1 is None and t == 2020 - 1:
        print(previous)
        end1 = timer()
    t += 1
    new_previous = 0 if previous not in D else t - 1 - D[previous]
    D[previous] = t - 1
    previous = new_previous

end2 = timer()
print(previous)
print(f'Time for part 1: {end1 - start} seconds')
print(f'Time for part 2: {end2 - start} seconds')
