lines = [line.strip() for line in open("input/08.txt")]

changed = set()
first_run = True
while True:
    accumulator = ip = 0
    visited = {0}
    curr_change = None
    while ip < len(lines):
        line = lines[ip]
        command, arg = line.split()

        # Change one line if we didn't yet this run
        if not first_run and curr_change is None and command in ("jmp", "nop") and ip not in changed:
            changed.add(ip)
            curr_change = ip
            command = "nop" if command == "jmp" else "jmp"

        # Execute command
        arg = int(arg)
        if command == "acc":
            accumulator += arg
        elif command == "jmp":
            ip += arg - 1
        elif command == "nop":
            pass
        ip += 1

        # Check if we've seen this IP already, then we're in a loop
        if ip not in visited:
            visited.add(ip)
        else:
            # Part A: Result after first run where we hit a loop
            if first_run:
                print(accumulator)
                first_run = False
            break
    else:
        # Part B: We terminated!
        break
print(accumulator)
