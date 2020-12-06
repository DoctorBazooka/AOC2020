def parse(f):
    current_party = []
    for line in f:
        if len(line.strip()) == 0:
            yield current_party
            current_party = []
        else:
            current_party.append(set(line.strip()))
    yield current_party

count_part1 = 0
count_part2 = 0

with open("day6_input.txt") as f:
    for party in parse(f):
       count_part1 += len(set.union(*party))
       count_part2 += len(set.intersection(*party))

print(count_part1)
print(count_part2)