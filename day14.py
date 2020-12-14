from itertools import product

lines = [line.strip() for line in open("input/14.txt")]

bitmask = None
mem_v1 = dict()
mem_v2 = dict()
for line in lines:
    if line.startswith("mask"):
        bitmask = line.split(" = ")[1]
    elif line.startswith("mem"):
        address, number = line.split(" = ")
        address = int(address[4:-1])
        number = int(number)
        value_byte = f"{number:036b}"
        address_byte = f"{address:036b}"

        floating = []
        if bitmask is not None:
            for i, v in enumerate(bitmask):
                # Change value in v1 if 0 or 1
                if v != "X":
                    value_byte = value_byte[:i] + v + value_byte[i + 1:]

                # Change address in v2 if not 0
                if v == "1":
                    address_byte = address_byte[:i] + v + address_byte[i+1:]
                elif v == "X":
                    floating.append(i)
        mem_v1[address] = int(value_byte, 2)

        for comb in product(["0", "1"], repeat=len(floating)):
            address = address_byte
            for i, v in enumerate(comb):
                bit = floating[i]
                address = address[:bit] + v + address[bit+1:]
            mem_v2[int(address, 2)] = number

print(sum(mem_v1.values()))
print(sum(mem_v2.values()))
