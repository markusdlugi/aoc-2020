from llist import dllist
from timeit import default_timer as timer

start = timer()
puzzle = int(open("input/23.txt").read())


def solve(p2):
    lookup = dict()
    cups = dllist()
    for x in str(puzzle):
        node = cups.append(int(x))
        lookup[int(x)] = node

    if p2:
        for x in range(10, 1_000_000 + 1):
            node = cups.append(x)
            lookup[x] = node

    max_number = max(cups)
    for i in range(10_000_000 if p2 else 100):
        current_cup = cups.popleft()
        picked_up = [cups.popleft(), cups.popleft(), cups.popleft()]

        node = cups.appendleft(current_cup)
        lookup[current_cup] = node

        destination = current_cup - 1
        while destination in picked_up or destination < 1:
            destination -= 1
            if destination < 1:
                destination = max_number

        insert_node = lookup[destination].next
        for cup in picked_up:
            node = cups.insert(cup, insert_node)
            lookup[cup] = node

        node = cups.append(cups.popleft())
        lookup[current_cup] = node

    if p2:
        one_node = lookup[1]
        one_after = one_node.next
        two_after = one_after.next
        return one_after.value * two_after.value
    else:
        while cups[0] != 1:
            cups.append(cups.popleft())
        cups.popleft()
        return "".join(str(x) for x in cups)


print(solve(False))
print(solve(True))
end = timer()
print(f'Took {round((end - start) * 1000, 2)} ms.')
