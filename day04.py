def in_range(val, min_val, max_val):
    return val.isdigit() and min_val <= int(val) <= max_val

field_checker = {
    "byr": lambda v: in_range(v, 1920, 2002),
    "iyr": lambda v: in_range(v, 2010, 2020),
    "eyr": lambda v: in_range(v, 2020, 2030),
    "hgt": lambda v: (v.endswith("cm") and in_range(v[:-2], 150, 193)) or (v.endswith("in") and in_range(v[:-2], 59, 76)),
    "hcl": lambda v: v.startswith("#") and len(v) == 7 and all(x in "0123456789abcdef" for x in v[1:]),
    "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda v: len(v) == 9 and v.isdigit(),
    "cid": lambda v: True
}

def get_passports(f):
    for line in f.read().split("\n\n"):
        yield dict(pair.split(":") for pair in line.split())

def part1_validate(passport):
    return {'eyr', 'hgt', 'pid', 'iyr', 'hcl', 'ecl', 'byr'} <= passport.keys()

def part2_validate(passport):
    return all(field_checker[k](v) for k, v in passport.items())

count_part1 = 0
count_part2 = 0

with open("day04_input.txt") as f:
    for passport in get_passports(f):
        if part1_validate(passport):
            count_part1 += 1
            if part2_validate(passport):
                count_part2 += 1

print(count_part1)
print(count_part2)