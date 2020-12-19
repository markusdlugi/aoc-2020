from collections import defaultdict
import re
from timeit import default_timer as timer

start = timer()
with open("input/19.txt") as field:
    sections = [section.splitlines() for section in field.read().split("\n\n")]

rules = sections[0]
msgs = sections[1]


def build_rules(p2):
    rule_map = defaultdict(list)
    for rule in rules:
        if p2:
            if rule.startswith("8:"):
                rule = "8: 42 | 42 8"
            elif rule.startswith("11:"):
                rule = "11: 42 31 | 42 11 31"
        n, r = rule.split(": ")
        n = int(n)
        if "\"" in r:
            rule_map[n].append(r[1])
        elif "|" in r:
            rs = r.split(" | ")
            for x in rs:
                rule_map[n].append(tuple(int(i) for i in x.split()))
        else:
            rule_map[n].append(tuple(int(i) for i in r.split()))
    return rule_map


def build(rule_map, p2):
    options = "^"
    for i in rule_map[0][0]:
        res = build_strings(i, rule_map, p2)
        if isinstance(res, list):
            option = "("
            option += "|".join(res)
            option += ")"
            options += option
        else:
            options += res
    options += "$"
    return options


def build_strings(n, rule_map, p2):
    r = rule_map[n]
    if "a" in r or "b" in r:
        return r[0]
    options = []

    if p2:
        if n == 8:
            x = build_strings(r[0][0], rule_map, p2)
            return "(" + "|".join(x) + ")+"
        elif n == 11:
            parts = []
            for i in r[0]:
                parts.append("|".join(build_strings(i, rule_map, p2)))

            options = []
            for x in range(1, 10):
                option = ""
                for part in parts:
                    option += "(" + part + "){" + str(x) + "}"
                options.append(option)
            return "(" + "|".join(options) + ")"

    for x in r:
        result = ""
        for i in x:
            msg = build_strings(i, rule_map, p2)
            subr = "("
            if type(msg) == list:
                subr += "|".join("".join(o) for o in msg)
                subr += ")"
                result += subr
            else:
                result += "".join(msg)
        options.append(result)
    return options


rule_map1 = build_rules(False)
regex1 = build(rule_map1, False)
print(sum(1 for m in msgs if re.match(regex1, m)))

rule_map2 = build_rules(True)
regex2 = build(rule_map1, True)
print(sum(1 for m in msgs if re.match(regex2, m)))

end = timer()
print(f'Took {end - start} seconds.')
