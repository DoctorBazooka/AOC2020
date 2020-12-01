def sum_to(nums, target):
    vals = set()
    for line in nums:
        if target - (x := int(line)) in vals:
            return x * (target-x)
        vals.add(x)

with open("day1_input.txt") as f:
    print(sum_to(f, 2020))