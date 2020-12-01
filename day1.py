with open("day1_input.txt") as f:
    vals = set()
    for line in f:
        if 2020 - (x := int(line)) in vals:
            print(x * (2020-x))
            break
        vals.add(x)