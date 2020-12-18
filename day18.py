from collections import deque

lines = [line.strip() for line in open("input/18.txt")]

results = []
for line in lines:
    og = line
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    words = line.split()
    stack = deque()
    stackstack = deque()
    for word in words:
        if word in "+*":
            stack.append(word)
        elif word == "(":
            stackstack.append(stack.copy())
            stack.clear()
        elif word == ")":
            while len(stack) >= 3:
                if "+" in stack:
                    i = 0
                    while i + 2 < len(stack):
                        a = stack[i]
                        op = stack[i + 1]
                        b = stack[i + 2]
                        if op == "+":
                            result = eval(a + op + b)
                            del stack[i + 2]
                            del stack[i + 1]
                            stack[i] = str(result)
                            i += 3
                        else:
                            i += 2
                if len(stack) >= 3:
                    b = stack.pop()
                    op = stack.pop()
                    a = stack.pop()
                    result = eval(a + op + b)
                    stack.append(str(result))
            result = stack.pop()
            stack.clear()
            stack.extend(stackstack.pop())
            stack.append(str(result))
            if len(stack) >= 3 and stack[-2] == "+":
                b = stack.pop()
                op = stack.pop()
                a = stack.pop()
                result = eval(a + op + b)
                stack.append(str(result))
        else:
            if len(stack) >= 2 and stack[-1] == "+":
                op = stack.pop()
                a = stack.pop()
                result = eval(a + op + word)
                stack.append(str(result))
            else:
                stack.append(word)
    stack.reverse()
    while len(stack) > 1:
        if "+" in stack:
            i = 0
            while i+2 < len(stack):
                a = stack[i]
                op = stack[i+1]
                b = stack[i+2]
                if op == "+":
                    result = eval(a + op + b)
                    del stack[i+2]
                    del stack[i+1]
                    stack[i] = str(result)
                    i += 3
                else:
                    i += 2
        else:
            a = stack.pop()
            op = stack.pop()
            b = stack.pop()
            result = eval(a + op + b)
            stack.append(str(result))
    result = stack.pop()
    results.append(int(result))
print(sum(results))
