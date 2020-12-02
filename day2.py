from collections import Counter

def parse_line(line):
    limits, letter, password = line.split(" ")
    return [*tuple(int(x) for x in limits.split("-")), letter[0], password]

def part1_policy(x, y, letter, password):
    return letter in password and x <= Counter(password)[letter] <= y

def part2_policy(x, y, letter, password):
    return (password[x-1] == letter) ^ (password[y-1] == letter)

count_part1 = 0
count_part2 = 0
with open("day2_input.txt") as f:
    for line in f:
        x, y, letter, password = parse_line(line)
        if part1_policy(x, y, letter, password):
            count_part1 += 1
        if part2_policy(x, y, letter, password):
            count_part2 += 1
print(count_part1)
print(count_part2)