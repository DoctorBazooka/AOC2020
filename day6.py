def parse(f):
    for party in f.read().split("\n\n"):
        yield [set(x) for x in party.split("\n")]

count_part1 = 0
count_part2 = 0

with open("day6_input.txt") as f:
    for party in parse(f):
       count_part1 += len(set.union(*party))
       count_part2 += len(set.intersection(*party))

print(count_part1)
print(count_part2)