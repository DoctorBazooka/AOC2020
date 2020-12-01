def sum_to(nums, target):
    vals = set()
    for a in nums:
        if target - a in vals:
            return a * (target - a)
        vals.add(a)

with open("day1_input.txt") as f:
    lines = list(map(int, f.readlines()))

print(sum_to(lines, 2020))
for a in lines:
    if b := sum_to(lines, 2020 - a):
        print(a * b)
        break