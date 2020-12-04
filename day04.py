import re


def isnum(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


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
valid = 0
for passport in passports:
    invalid = False
    for m in mandatory:
        if m not in passport:
            invalid = True
            break
    if not invalid:
        valid += 1
print(valid)

# Part B
valid = 0
for passport in passports:
    invalid = False
    for m in mandatory:
        try:
            if m not in passport:
                raise ValueError
            elif m == 'byr':
                byr = passport['byr']
                if not isnum(byr) or int(byr) < 1920 or int(byr) > 2002:
                    raise ValueError
            elif m == 'iyr':
                iyr = passport['iyr']
                if not isnum(iyr) or int(iyr) < 2010 or int(iyr) > 2020:
                    raise ValueError
            elif m == 'eyr':
                eyr = passport['eyr']
                if not isnum(eyr) or int(eyr) < 2020 or int(eyr) > 2030:
                    raise ValueError
            elif m == 'hgt':
                hgt = passport['hgt']
                if hgt[-2:] not in ("cm", "in") or not isnum(hgt[:-2]):
                    raise ValueError
                unit = hgt[-2:]
                value = int(hgt[:-2])
                if unit == "cm":
                    if value < 150 or value > 193:
                        raise ValueError
                elif unit == "in":
                    if value < 59 or value > 76:
                        raise ValueError
            elif m == 'hcl':
                hcl = passport['hcl']
                matches = re.match(r'#[0-9a-f]{6}', hcl)
                if not matches:
                    raise ValueError
            elif m == 'ecl':
                ecl = passport['ecl']
                if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    raise ValueError
            elif m == 'pid':
                pid = passport['pid']
                if not isnum(pid) or len(pid) != 9:
                    raise ValueError
        except ValueError:
            break
    else:
        valid += 1
print(valid)
