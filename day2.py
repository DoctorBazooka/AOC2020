from collections import Counter

def parse_line(line):
    policy, letter, data = line.split(" ")
    return [*tuple(int(x) for x in policy.split("-")), letter[0], Counter(data)]

count = 0
with open("day2_input.txt") as f:
    for line in f:
        low, high, letter, data = parse_line(line)
        if letter in data and low <= data[letter] <= high:
            count += 1
print(count)