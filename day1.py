def sum_to(nums, target):
    for a in nums:
        if target - a in nums:
            return a * (target - a)

with open("day1_input.txt") as f:
    lines = set(map(int, f.readlines()))

print(sum_to(lines, 2020))
for a in lines:
    if b := sum_to(lines, 2020 - a):
        print(a * b)
        break