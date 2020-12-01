def sum_to(target):
    vals = set()
    with open("day1_input.txt") as f:
        for line in f:
            if target - (x := int(line)) in vals:
                return x * (target-x)
            vals.add(x)

with open("day1_input.txt") as f:
    vals = set()
    for a in map(int, f):
        if b := sum_to(2020 - a):
            print(a * b)
            break
        vals.add(a)