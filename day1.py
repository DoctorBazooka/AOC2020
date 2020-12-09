def sum_to(nums, target, count):
    if count > 1:
        for a in nums:
            if b := sum_to(nums, target - a, count - 1):
                return a * b
    elif target in nums:
        return target

if __name__ == "__main__":
    with open("day1_input.txt") as f:
        lines = set(map(int, f.readlines()))
    
    print(sum_to(lines, 2020, 2))
    print(sum_to(lines, 2020, 3))