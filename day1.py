def sum_to(target):
    with open("day1_input.txt") as f:
        vals = set()
        for a in map(int, f):
            if target - a in vals:
                return a * (target - a)
            vals.add(a)
with open("day1_input.txt") as f:
    for a in map(int, f):
        if b := sum_to(2020 - a):
            print(a * b)