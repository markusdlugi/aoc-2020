pubkeys = [int(line.strip()) for line in open("input/25.txt")]


def transform(num, loop=None, pubkey=None):
    curr = 1
    for i in range(100000000 if loop is None else loop):
        curr *= num
        curr %= 20201227
        if loop is None and curr == pubkey:
            return i + 1
    else:
        return curr


loop_size = transform(7, pubkey=pubkeys[0])
encryption_key = transform(pubkeys[1], loop=loop_size)
print(encryption_key)
