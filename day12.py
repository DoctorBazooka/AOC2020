def instructions():
    with open("day12_input.txt") as f:
        for line in f:
            yield line[0], int(line[1:])

def move(pos, direction, value):
    x, y = pos
    if direction == "N":
        return (x, y + value)
    if direction == "S":
        return (x, y - value)
    if direction == "E":
        return (x + value, y)
    if direction == "W":
        return (x - value, y)

def get_direction(rotation):
    return {0: "N", 90: "E", 180: "S", 270: "W"}[rotation]

def part1():
    position = (0, 0)
    rotation = 90 # E
    for action, value in instructions():
        if action in {"N", "E", "S", "W"}:
            position = move(position, action, value)
        elif action == "R":
            rotation = (rotation + value) % 360
        elif action == "L":
            rotation = (rotation - value) % 360
        elif action == "F":
            direction = get_direction(rotation)
            position = move(position, direction, value)
    return abs(position[0]) + abs(position[1])

print(part1())