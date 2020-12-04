import re


def in_range(value, a, b):
    try:
        return a <= int(value) <= b
    except ValueError:
        return False


def field_valid(key, value):
    ranges = {'byr': (1920, 2002), 'iyr': (2010, 2020), 'eyr': (2020, 2030), 'cm': (150, 193), 'in': (59, 76)}
    if key in ranges.keys():
        return in_range(value, *ranges[key])
    elif key == 'hgt':
        unit, height = (value[-2:], value[:-2])
        if unit not in ("cm", "in"):
            return False
        return in_range(height, *ranges[unit])
    elif key == 'hcl':
        return re.match(r'#[0-9a-f]{6}', value)
    elif key == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    elif key == 'pid':
        return len(value) == 9
    elif key == 'cid':
        return True
    return True


lines = [line.strip() for line in open("input/04.txt")]

passports = []
passport = dict()
for line in lines:
    if line == "":
        passports.append(passport)
        passport = dict()
        continue
    fields = line.split()
    for field in fields:
        a, b = field.split(":")
        passport[a] = b
passports.append(passport)

mandatory = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

# Part A
valid = sum(all(m in passport for m in mandatory) for passport in passports)
print(valid)

# Part B
valid = sum(all(m in passport and field_valid(m, passport[m]) for m in mandatory) for passport in passports)
print(valid)
