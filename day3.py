def skip_lines(f, count):
    for idx, line in enumerate(f, 1):
        if idx % count == 0:
            yield line

def slope(right, down):
    count = 0
    position = 0
    with open("day3_input.txt") as f:
        first_line = next(f)
        width = len(first_line) - 1 # Removing \n
        for line in skip_lines(f, down):
            position = (position + right) % width
            if line[position] == "#":
                count += 1
    return count

with open("day3_input.txt") as f:
    lines = list(f.read())

print(slope(lines, 3, 1))
print(slope(lines, 1, 1) * slope(lines, 3, 1) * slope(lines, 5, 1) * slope(lines, 7, 1) * slope(lines, 1, 2))