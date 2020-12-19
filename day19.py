from collections import defaultdict
import re
from timeit import default_timer as timer

start = timer()
with open("input/19.txt") as field:
    sections = [section.splitlines() for section in field.read().split("\n\n")]

rules = sections[0]
messages = sections[1]


def parse_rules():
    rule_map = defaultdict(list)
    for rule in rules:
        n, r = rule.split(": ")
        n = int(n)
        if "\"" in r:
            rule_map[n].append(r[1])
        elif "|" in r:
            rule_map[n].extend(tuple(int(i) for i in x.split()) for x in r.split(" | "))
        else:
            rule_map[n].append(tuple(int(i) for i in r.split()))
    return rule_map


rule_map = parse_rules()


def build_regex(p2):
    regex = "^"
    for i in rule_map[0][0]:
        res = build_regex_for_rule(i, p2)
        if isinstance(res, list):
            regex += "(" + "|".join(res) + ")"
        else:
            regex += res
    regex += "$"
    return regex


def build_regex_for_rule(n, p2):
    rule = rule_map[n]
    if "a" in rule or "b" in rule:
        return rule[0]
    options = []

    # Special rules for part 2
    if p2:
        # Rule 8: Transform to (42)+
        if n == 8:
            option = build_regex_for_rule(rule[0][0], p2)
            return "(" + "|".join(option) + ")+"
        # Rule 11: Transform to (42){1}(31){1}|(42){2}(31){2}|...
        elif n == 11:
            parts = ["|".join(build_regex_for_rule(i, p2)) for i in rule[0]]

            options = []
            for option in range(1, 5):
                options.append("".join("(" + part + "){" + str(option) + "}" for part in parts))
            return "(" + "|".join(options) + ")"

    for part in rule:
        option = ""
        for i in part:
            regex = build_regex_for_rule(i, p2)
            if isinstance(regex, list) and len(regex) > 1:
                option += "(" + "|".join("".join(o) for o in regex) + ")"
            else:
                option += "".join(regex)
        options.append(option)
    return options


regex1 = build_regex(False)
print(sum(1 for m in messages if re.match(regex1, m)))

regex2 = build_regex(True)
print(sum(1 for m in messages if re.match(regex2, m)))

end = timer()
print(f'Took {end - start} seconds.')
